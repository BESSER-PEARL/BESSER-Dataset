import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PageSummary,
    ObjectSummary,
    xwiki::LinkCollection,
    xwiki::Link,
    xwiki::Page,
    xwiki::Object,
    xwiki::EStringToStringMapEntry,
    xwiki::DocumentRoot,
    LinkCollection,
    xwiki::Space,
    xwiki::XWiki,
    xwiki::Translation,
    xwiki::AttachmentsType,
    xwiki::Class,
    xwiki::HistoryType,
    xwiki::Tag,
    xwiki::TagsType,
    xwiki::SearchResultsType,
    xwiki::Syntaxes,
    xwiki::Wiki,
    xwiki::HistorySummary,
    xwiki::CommentsType,
    xwiki::PropertiesType,
    xwiki::Translations,
    xwiki::ClassesType,
    xwiki::SearchResult,
    xwiki::SpacesType,
    xwiki::ObjectSummary,
    xwiki::Comment,
    xwiki::ObjectsType,
    xwiki::PagesType,
    xwiki::WikisType,
    xwiki::Attribute,
    xwiki::Property,
    xwiki::PageSummary,
    xwiki::Attachment,
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



def test_xwiki::linkcollection_is_not_abstract():
    assert not inspect.isabstract(xwiki::LinkCollection)


def test_xwiki::linkcollection_constructor_exists():
    assert callable(xwiki::LinkCollection.__init__)


def test_xwiki::linkcollection_constructor_args():
    sig = inspect.signature(xwiki::LinkCollection.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::link_is_not_abstract():
    assert not inspect.isabstract(xwiki::Link)


def test_xwiki::link_constructor_exists():
    assert callable(xwiki::Link.__init__)


def test_xwiki::link_constructor_args():
    sig = inspect.signature(xwiki::Link.__init__)
    params = list(sig.parameters.keys())
    assert "rel" in params, "Missing parameter 'rel'"
    assert "hrefLang" in params, "Missing parameter 'hrefLang'"
    assert "href" in params, "Missing parameter 'href'"
    assert "type" in params, "Missing parameter 'type'"

def test_xwiki::link_has_rel():
    assert hasattr(xwiki::Link, "rel")
    descriptor = None
    for klass in xwiki::Link.__mro__:
        if "rel" in klass.__dict__:
            descriptor = klass.__dict__["rel"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::link_has_hrefLang():
    assert hasattr(xwiki::Link, "hrefLang")
    descriptor = None
    for klass in xwiki::Link.__mro__:
        if "hrefLang" in klass.__dict__:
            descriptor = klass.__dict__["hrefLang"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::link_has_href():
    assert hasattr(xwiki::Link, "href")
    descriptor = None
    for klass in xwiki::Link.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::link_has_type():
    assert hasattr(xwiki::Link, "type")
    descriptor = None
    for klass in xwiki::Link.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::page_is_not_abstract():
    assert not inspect.isabstract(xwiki::Page)


def test_xwiki::page_constructor_exists():
    assert callable(xwiki::Page.__init__)


def test_xwiki::page_constructor_args():
    sig = inspect.signature(xwiki::Page.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "created" in params, "Missing parameter 'created'"
    assert "content" in params, "Missing parameter 'content'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "creatorName" in params, "Missing parameter 'creatorName'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "creator" in params, "Missing parameter 'creator'"

def test_xwiki::page_has_language():
    assert hasattr(xwiki::Page, "language")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_comment():
    assert hasattr(xwiki::Page, "comment")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_minorVersion():
    assert hasattr(xwiki::Page, "minorVersion")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "minorVersion" in klass.__dict__:
            descriptor = klass.__dict__["minorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_modifierName():
    assert hasattr(xwiki::Page, "modifierName")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "modifierName" in klass.__dict__:
            descriptor = klass.__dict__["modifierName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_created():
    assert hasattr(xwiki::Page, "created")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_content():
    assert hasattr(xwiki::Page, "content")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_majorVersion():
    assert hasattr(xwiki::Page, "majorVersion")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "majorVersion" in klass.__dict__:
            descriptor = klass.__dict__["majorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_creatorName():
    assert hasattr(xwiki::Page, "creatorName")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "creatorName" in klass.__dict__:
            descriptor = klass.__dict__["creatorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_modified():
    assert hasattr(xwiki::Page, "modified")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_modifier():
    assert hasattr(xwiki::Page, "modifier")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::page_has_creator():
    assert hasattr(xwiki::Page, "creator")
    descriptor = None
    for klass in xwiki::Page.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::object_is_not_abstract():
    assert not inspect.isabstract(xwiki::Object)


def test_xwiki::object_constructor_exists():
    assert callable(xwiki::Object.__init__)


def test_xwiki::object_constructor_args():
    sig = inspect.signature(xwiki::Object.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xwiki::EStringToStringMapEntry)


def test_xwiki::estringtostringmapentry_constructor_exists():
    assert callable(xwiki::EStringToStringMapEntry.__init__)


def test_xwiki::estringtostringmapentry_constructor_args():
    sig = inspect.signature(xwiki::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::documentroot_is_not_abstract():
    assert not inspect.isabstract(xwiki::DocumentRoot)


def test_xwiki::documentroot_constructor_exists():
    assert callable(xwiki::DocumentRoot.__init__)


def test_xwiki::documentroot_constructor_args():
    sig = inspect.signature(xwiki::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xwiki::documentroot_has_mixed():
    assert hasattr(xwiki::DocumentRoot, "mixed")
    descriptor = None
    for klass in xwiki::DocumentRoot.__mro__:
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



def test_xwiki::space_is_not_abstract():
    assert not inspect.isabstract(xwiki::Space)


def test_xwiki::space_constructor_exists():
    assert callable(xwiki::Space.__init__)


def test_xwiki::space_constructor_args():
    sig = inspect.signature(xwiki::Space.__init__)
    params = list(sig.parameters.keys())
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "home" in params, "Missing parameter 'home'"

def test_xwiki::space_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki::Space, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::space_has_id():
    assert hasattr(xwiki::Space, "id")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::space_has_name():
    assert hasattr(xwiki::Space, "name")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::space_has_xwikiRelativeUrl():
    assert hasattr(xwiki::Space, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::space_has_wiki():
    assert hasattr(xwiki::Space, "wiki")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::space_has_home():
    assert hasattr(xwiki::Space, "home")
    descriptor = None
    for klass in xwiki::Space.__mro__:
        if "home" in klass.__dict__:
            descriptor = klass.__dict__["home"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::xwiki_is_not_abstract():
    assert not inspect.isabstract(xwiki::XWiki)


def test_xwiki::xwiki_constructor_exists():
    assert callable(xwiki::XWiki.__init__)


def test_xwiki::xwiki_constructor_args():
    sig = inspect.signature(xwiki::XWiki.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_xwiki::xwiki_has_version():
    assert hasattr(xwiki::XWiki, "version")
    descriptor = None
    for klass in xwiki::XWiki.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::translation_is_not_abstract():
    assert not inspect.isabstract(xwiki::Translation)


def test_xwiki::translation_constructor_exists():
    assert callable(xwiki::Translation.__init__)


def test_xwiki::translation_constructor_args():
    sig = inspect.signature(xwiki::Translation.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_xwiki::translation_has_language():
    assert hasattr(xwiki::Translation, "language")
    descriptor = None
    for klass in xwiki::Translation.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::attachmentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki::AttachmentsType)


def test_xwiki::attachmentstype_constructor_exists():
    assert callable(xwiki::AttachmentsType.__init__)


def test_xwiki::attachmentstype_constructor_args():
    sig = inspect.signature(xwiki::AttachmentsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::class_is_not_abstract():
    assert not inspect.isabstract(xwiki::Class)


def test_xwiki::class_constructor_exists():
    assert callable(xwiki::Class.__init__)


def test_xwiki::class_constructor_args():
    sig = inspect.signature(xwiki::Class.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::class_has_id():
    assert hasattr(xwiki::Class, "id")
    descriptor = None
    for klass in xwiki::Class.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::class_has_name():
    assert hasattr(xwiki::Class, "name")
    descriptor = None
    for klass in xwiki::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::historytype_is_not_abstract():
    assert not inspect.isabstract(xwiki::HistoryType)


def test_xwiki::historytype_constructor_exists():
    assert callable(xwiki::HistoryType.__init__)


def test_xwiki::historytype_constructor_args():
    sig = inspect.signature(xwiki::HistoryType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::tag_is_not_abstract():
    assert not inspect.isabstract(xwiki::Tag)


def test_xwiki::tag_constructor_exists():
    assert callable(xwiki::Tag.__init__)


def test_xwiki::tag_constructor_args():
    sig = inspect.signature(xwiki::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::tag_has_name():
    assert hasattr(xwiki::Tag, "name")
    descriptor = None
    for klass in xwiki::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::tagstype_is_not_abstract():
    assert not inspect.isabstract(xwiki::TagsType)


def test_xwiki::tagstype_constructor_exists():
    assert callable(xwiki::TagsType.__init__)


def test_xwiki::tagstype_constructor_args():
    sig = inspect.signature(xwiki::TagsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::searchresultstype_is_not_abstract():
    assert not inspect.isabstract(xwiki::SearchResultsType)


def test_xwiki::searchresultstype_constructor_exists():
    assert callable(xwiki::SearchResultsType.__init__)


def test_xwiki::searchresultstype_constructor_args():
    sig = inspect.signature(xwiki::SearchResultsType.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"

def test_xwiki::searchresultstype_has_template():
    assert hasattr(xwiki::SearchResultsType, "template")
    descriptor = None
    for klass in xwiki::SearchResultsType.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::syntaxes_is_not_abstract():
    assert not inspect.isabstract(xwiki::Syntaxes)


def test_xwiki::syntaxes_constructor_exists():
    assert callable(xwiki::Syntaxes.__init__)


def test_xwiki::syntaxes_constructor_args():
    sig = inspect.signature(xwiki::Syntaxes.__init__)
    params = list(sig.parameters.keys())
    assert "syntax" in params, "Missing parameter 'syntax'"

def test_xwiki::syntaxes_has_syntax():
    assert hasattr(xwiki::Syntaxes, "syntax")
    descriptor = None
    for klass in xwiki::Syntaxes.__mro__:
        if "syntax" in klass.__dict__:
            descriptor = klass.__dict__["syntax"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::wiki_is_not_abstract():
    assert not inspect.isabstract(xwiki::Wiki)


def test_xwiki::wiki_constructor_exists():
    assert callable(xwiki::Wiki.__init__)


def test_xwiki::wiki_constructor_args():
    sig = inspect.signature(xwiki::Wiki.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_xwiki::wiki_has_owner():
    assert hasattr(xwiki::Wiki, "owner")
    descriptor = None
    for klass in xwiki::Wiki.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::wiki_has_name():
    assert hasattr(xwiki::Wiki, "name")
    descriptor = None
    for klass in xwiki::Wiki.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::wiki_has_id():
    assert hasattr(xwiki::Wiki, "id")
    descriptor = None
    for klass in xwiki::Wiki.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::wiki_has_description():
    assert hasattr(xwiki::Wiki, "description")
    descriptor = None
    for klass in xwiki::Wiki.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::historysummary_is_not_abstract():
    assert not inspect.isabstract(xwiki::HistorySummary)


def test_xwiki::historysummary_constructor_exists():
    assert callable(xwiki::HistorySummary.__init__)


def test_xwiki::historysummary_constructor_args():
    sig = inspect.signature(xwiki::HistorySummary.__init__)
    params = list(sig.parameters.keys())
    assert "modifierName" in params, "Missing parameter 'modifierName'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "language" in params, "Missing parameter 'language'"
    assert "space" in params, "Missing parameter 'space'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "minorVersion" in params, "Missing parameter 'minorVersion'"
    assert "majorVersion" in params, "Missing parameter 'majorVersion'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::historysummary_has_modifierName():
    assert hasattr(xwiki::HistorySummary, "modifierName")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "modifierName" in klass.__dict__:
            descriptor = klass.__dict__["modifierName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_modified():
    assert hasattr(xwiki::HistorySummary, "modified")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_language():
    assert hasattr(xwiki::HistorySummary, "language")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_space():
    assert hasattr(xwiki::HistorySummary, "space")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_comment():
    assert hasattr(xwiki::HistorySummary, "comment")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_wiki():
    assert hasattr(xwiki::HistorySummary, "wiki")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_pageId():
    assert hasattr(xwiki::HistorySummary, "pageId")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_version():
    assert hasattr(xwiki::HistorySummary, "version")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_minorVersion():
    assert hasattr(xwiki::HistorySummary, "minorVersion")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "minorVersion" in klass.__dict__:
            descriptor = klass.__dict__["minorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_majorVersion():
    assert hasattr(xwiki::HistorySummary, "majorVersion")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "majorVersion" in klass.__dict__:
            descriptor = klass.__dict__["majorVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_modifier():
    assert hasattr(xwiki::HistorySummary, "modifier")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::historysummary_has_name():
    assert hasattr(xwiki::HistorySummary, "name")
    descriptor = None
    for klass in xwiki::HistorySummary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::commentstype_is_not_abstract():
    assert not inspect.isabstract(xwiki::CommentsType)


def test_xwiki::commentstype_constructor_exists():
    assert callable(xwiki::CommentsType.__init__)


def test_xwiki::commentstype_constructor_args():
    sig = inspect.signature(xwiki::CommentsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::propertiestype_is_not_abstract():
    assert not inspect.isabstract(xwiki::PropertiesType)


def test_xwiki::propertiestype_constructor_exists():
    assert callable(xwiki::PropertiesType.__init__)


def test_xwiki::propertiestype_constructor_args():
    sig = inspect.signature(xwiki::PropertiesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::translations_is_not_abstract():
    assert not inspect.isabstract(xwiki::Translations)


def test_xwiki::translations_constructor_exists():
    assert callable(xwiki::Translations.__init__)


def test_xwiki::translations_constructor_args():
    sig = inspect.signature(xwiki::Translations.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_xwiki::translations_has_default():
    assert hasattr(xwiki::Translations, "default")
    descriptor = None
    for klass in xwiki::Translations.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::classestype_is_not_abstract():
    assert not inspect.isabstract(xwiki::ClassesType)


def test_xwiki::classestype_constructor_exists():
    assert callable(xwiki::ClassesType.__init__)


def test_xwiki::classestype_constructor_args():
    sig = inspect.signature(xwiki::ClassesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::searchresult_is_not_abstract():
    assert not inspect.isabstract(xwiki::SearchResult)


def test_xwiki::searchresult_constructor_exists():
    assert callable(xwiki::SearchResult.__init__)


def test_xwiki::searchresult_constructor_args():
    sig = inspect.signature(xwiki::SearchResult.__init__)
    params = list(sig.parameters.keys())
    assert "modified" in params, "Missing parameter 'modified'"
    assert "language" in params, "Missing parameter 'language'"
    assert "space" in params, "Missing parameter 'space'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"
    assert "className" in params, "Missing parameter 'className'"
    assert "objectNumber" in params, "Missing parameter 'objectNumber'"
    assert "pageFullName" in params, "Missing parameter 'pageFullName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "score" in params, "Missing parameter 'score'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "author" in params, "Missing parameter 'author'"
    assert "id" in params, "Missing parameter 'id'"
    assert "authorName" in params, "Missing parameter 'authorName'"

def test_xwiki::searchresult_has_modified():
    assert hasattr(xwiki::SearchResult, "modified")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_language():
    assert hasattr(xwiki::SearchResult, "language")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_space():
    assert hasattr(xwiki::SearchResult, "space")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_pageName():
    assert hasattr(xwiki::SearchResult, "pageName")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "pageName" in klass.__dict__:
            descriptor = klass.__dict__["pageName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_type():
    assert hasattr(xwiki::SearchResult, "type")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_title():
    assert hasattr(xwiki::SearchResult, "title")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_className():
    assert hasattr(xwiki::SearchResult, "className")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_objectNumber():
    assert hasattr(xwiki::SearchResult, "objectNumber")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "objectNumber" in klass.__dict__:
            descriptor = klass.__dict__["objectNumber"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_pageFullName():
    assert hasattr(xwiki::SearchResult, "pageFullName")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "pageFullName" in klass.__dict__:
            descriptor = klass.__dict__["pageFullName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_version():
    assert hasattr(xwiki::SearchResult, "version")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_score():
    assert hasattr(xwiki::SearchResult, "score")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_filename():
    assert hasattr(xwiki::SearchResult, "filename")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_wiki():
    assert hasattr(xwiki::SearchResult, "wiki")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_author():
    assert hasattr(xwiki::SearchResult, "author")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_id():
    assert hasattr(xwiki::SearchResult, "id")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::searchresult_has_authorName():
    assert hasattr(xwiki::SearchResult, "authorName")
    descriptor = None
    for klass in xwiki::SearchResult.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::spacestype_is_not_abstract():
    assert not inspect.isabstract(xwiki::SpacesType)


def test_xwiki::spacestype_constructor_exists():
    assert callable(xwiki::SpacesType.__init__)


def test_xwiki::spacestype_constructor_args():
    sig = inspect.signature(xwiki::SpacesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::objectsummary_is_not_abstract():
    assert not inspect.isabstract(xwiki::ObjectSummary)


def test_xwiki::objectsummary_constructor_exists():
    assert callable(xwiki::ObjectSummary.__init__)


def test_xwiki::objectsummary_constructor_args():
    sig = inspect.signature(xwiki::ObjectSummary.__init__)
    params = list(sig.parameters.keys())
    assert "pageAuthor" in params, "Missing parameter 'pageAuthor'"
    assert "number" in params, "Missing parameter 'number'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "className" in params, "Missing parameter 'className'"
    assert "space" in params, "Missing parameter 'space'"
    assert "pageName" in params, "Missing parameter 'pageName'"
    assert "pageAuthorName" in params, "Missing parameter 'pageAuthorName'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "guid" in params, "Missing parameter 'guid'"

def test_xwiki::objectsummary_has_pageAuthor():
    assert hasattr(xwiki::ObjectSummary, "pageAuthor")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "pageAuthor" in klass.__dict__:
            descriptor = klass.__dict__["pageAuthor"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_number():
    assert hasattr(xwiki::ObjectSummary, "number")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_pageId():
    assert hasattr(xwiki::ObjectSummary, "pageId")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_id():
    assert hasattr(xwiki::ObjectSummary, "id")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_pageVersion():
    assert hasattr(xwiki::ObjectSummary, "pageVersion")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "pageVersion" in klass.__dict__:
            descriptor = klass.__dict__["pageVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_className():
    assert hasattr(xwiki::ObjectSummary, "className")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_space():
    assert hasattr(xwiki::ObjectSummary, "space")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_pageName():
    assert hasattr(xwiki::ObjectSummary, "pageName")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "pageName" in klass.__dict__:
            descriptor = klass.__dict__["pageName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_pageAuthorName():
    assert hasattr(xwiki::ObjectSummary, "pageAuthorName")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "pageAuthorName" in klass.__dict__:
            descriptor = klass.__dict__["pageAuthorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_headline():
    assert hasattr(xwiki::ObjectSummary, "headline")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_wiki():
    assert hasattr(xwiki::ObjectSummary, "wiki")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::objectsummary_has_guid():
    assert hasattr(xwiki::ObjectSummary, "guid")
    descriptor = None
    for klass in xwiki::ObjectSummary.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::comment_is_not_abstract():
    assert not inspect.isabstract(xwiki::Comment)


def test_xwiki::comment_constructor_exists():
    assert callable(xwiki::Comment.__init__)


def test_xwiki::comment_constructor_args():
    sig = inspect.signature(xwiki::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "highlight" in params, "Missing parameter 'highlight'"
    assert "date" in params, "Missing parameter 'date'"
    assert "author" in params, "Missing parameter 'author'"
    assert "text" in params, "Missing parameter 'text'"
    assert "replyTo" in params, "Missing parameter 'replyTo'"
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "id" in params, "Missing parameter 'id'"

def test_xwiki::comment_has_highlight():
    assert hasattr(xwiki::Comment, "highlight")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "highlight" in klass.__dict__:
            descriptor = klass.__dict__["highlight"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_date():
    assert hasattr(xwiki::Comment, "date")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_author():
    assert hasattr(xwiki::Comment, "author")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_text():
    assert hasattr(xwiki::Comment, "text")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_replyTo():
    assert hasattr(xwiki::Comment, "replyTo")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "replyTo" in klass.__dict__:
            descriptor = klass.__dict__["replyTo"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_pageId():
    assert hasattr(xwiki::Comment, "pageId")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_authorName():
    assert hasattr(xwiki::Comment, "authorName")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::comment_has_id():
    assert hasattr(xwiki::Comment, "id")
    descriptor = None
    for klass in xwiki::Comment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::objectstype_is_not_abstract():
    assert not inspect.isabstract(xwiki::ObjectsType)


def test_xwiki::objectstype_constructor_exists():
    assert callable(xwiki::ObjectsType.__init__)


def test_xwiki::objectstype_constructor_args():
    sig = inspect.signature(xwiki::ObjectsType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::pagestype_is_not_abstract():
    assert not inspect.isabstract(xwiki::PagesType)


def test_xwiki::pagestype_constructor_exists():
    assert callable(xwiki::PagesType.__init__)


def test_xwiki::pagestype_constructor_args():
    sig = inspect.signature(xwiki::PagesType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::wikistype_is_not_abstract():
    assert not inspect.isabstract(xwiki::WikisType)


def test_xwiki::wikistype_constructor_exists():
    assert callable(xwiki::WikisType.__init__)


def test_xwiki::wikistype_constructor_args():
    sig = inspect.signature(xwiki::WikisType.__init__)
    params = list(sig.parameters.keys())



def test_xwiki::attribute_is_not_abstract():
    assert not inspect.isabstract(xwiki::Attribute)


def test_xwiki::attribute_constructor_exists():
    assert callable(xwiki::Attribute.__init__)


def test_xwiki::attribute_constructor_args():
    sig = inspect.signature(xwiki::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::attribute_has_value():
    assert hasattr(xwiki::Attribute, "value")
    descriptor = None
    for klass in xwiki::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attribute_has_name():
    assert hasattr(xwiki::Attribute, "name")
    descriptor = None
    for klass in xwiki::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::property_is_not_abstract():
    assert not inspect.isabstract(xwiki::Property)


def test_xwiki::property_constructor_exists():
    assert callable(xwiki::Property.__init__)


def test_xwiki::property_constructor_args():
    sig = inspect.signature(xwiki::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::property_has_value():
    assert hasattr(xwiki::Property, "value")
    descriptor = None
    for klass in xwiki::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::property_has_type():
    assert hasattr(xwiki::Property, "type")
    descriptor = None
    for klass in xwiki::Property.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::property_has_name():
    assert hasattr(xwiki::Property, "name")
    descriptor = None
    for klass in xwiki::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::pagesummary_is_not_abstract():
    assert not inspect.isabstract(xwiki::PageSummary)


def test_xwiki::pagesummary_constructor_exists():
    assert callable(xwiki::PageSummary.__init__)


def test_xwiki::pagesummary_constructor_args():
    sig = inspect.signature(xwiki::PageSummary.__init__)
    params = list(sig.parameters.keys())
    assert "syntax" in params, "Missing parameter 'syntax'"
    assert "wiki" in params, "Missing parameter 'wiki'"
    assert "author" in params, "Missing parameter 'author'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "title" in params, "Missing parameter 'title'"
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "space" in params, "Missing parameter 'space'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "parent" in params, "Missing parameter 'parent'"
    assert "version" in params, "Missing parameter 'version'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "name" in params, "Missing parameter 'name'"

def test_xwiki::pagesummary_has_syntax():
    assert hasattr(xwiki::PageSummary, "syntax")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "syntax" in klass.__dict__:
            descriptor = klass.__dict__["syntax"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_wiki():
    assert hasattr(xwiki::PageSummary, "wiki")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "wiki" in klass.__dict__:
            descriptor = klass.__dict__["wiki"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_author():
    assert hasattr(xwiki::PageSummary, "author")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_xwikiRelativeUrl():
    assert hasattr(xwiki::PageSummary, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_title():
    assert hasattr(xwiki::PageSummary, "title")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_parentId():
    assert hasattr(xwiki::PageSummary, "parentId")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_space():
    assert hasattr(xwiki::PageSummary, "space")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_fullName():
    assert hasattr(xwiki::PageSummary, "fullName")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_id():
    assert hasattr(xwiki::PageSummary, "id")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_parent():
    assert hasattr(xwiki::PageSummary, "parent")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_version():
    assert hasattr(xwiki::PageSummary, "version")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_authorName():
    assert hasattr(xwiki::PageSummary, "authorName")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki::PageSummary, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::pagesummary_has_name():
    assert hasattr(xwiki::PageSummary, "name")
    descriptor = None
    for klass in xwiki::PageSummary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xwiki::attachment_is_not_abstract():
    assert not inspect.isabstract(xwiki::Attachment)


def test_xwiki::attachment_constructor_exists():
    assert callable(xwiki::Attachment.__init__)


def test_xwiki::attachment_constructor_args():
    sig = inspect.signature(xwiki::Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "pageId" in params, "Missing parameter 'pageId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "date" in params, "Missing parameter 'date'"
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "pageVersion" in params, "Missing parameter 'pageVersion'"
    assert "version" in params, "Missing parameter 'version'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "xwikiRelativeUrl" in params, "Missing parameter 'xwikiRelativeUrl'"
    assert "xwikiAbsoluteUrl" in params, "Missing parameter 'xwikiAbsoluteUrl'"
    assert "author" in params, "Missing parameter 'author'"
    assert "size" in params, "Missing parameter 'size'"
    assert "id" in params, "Missing parameter 'id'"

def test_xwiki::attachment_has_pageId():
    assert hasattr(xwiki::Attachment, "pageId")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "pageId" in klass.__dict__:
            descriptor = klass.__dict__["pageId"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_name():
    assert hasattr(xwiki::Attachment, "name")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_date():
    assert hasattr(xwiki::Attachment, "date")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_authorName():
    assert hasattr(xwiki::Attachment, "authorName")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_pageVersion():
    assert hasattr(xwiki::Attachment, "pageVersion")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "pageVersion" in klass.__dict__:
            descriptor = klass.__dict__["pageVersion"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_version():
    assert hasattr(xwiki::Attachment, "version")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_mimeType():
    assert hasattr(xwiki::Attachment, "mimeType")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_xwikiRelativeUrl():
    assert hasattr(xwiki::Attachment, "xwikiRelativeUrl")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "xwikiRelativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiRelativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_xwikiAbsoluteUrl():
    assert hasattr(xwiki::Attachment, "xwikiAbsoluteUrl")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "xwikiAbsoluteUrl" in klass.__dict__:
            descriptor = klass.__dict__["xwikiAbsoluteUrl"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_author():
    assert hasattr(xwiki::Attachment, "author")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_size():
    assert hasattr(xwiki::Attachment, "size")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_xwiki::attachment_has_id():
    assert hasattr(xwiki::Attachment, "id")
    descriptor = None
    for klass in xwiki::Attachment.__mro__:
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
xwiki::LinkCollection_strategy = st.builds(
    xwiki::LinkCollection,
)
xwiki::Link_strategy = st.builds(
    xwiki::Link,
    rel=
        safe_text,
    hrefLang=
        safe_text,
    href=
        safe_text,
    type=
        safe_text
)
xwiki::Page_strategy = st.builds(
    xwiki::Page,
    language=
        safe_text,
    comment=
        safe_text,
    minorVersion=
        safe_text,
    modifierName=
        safe_text,
    created=
        safe_text,
    content=
        safe_text,
    majorVersion=
        safe_text,
    creatorName=
        safe_text,
    modified=
        safe_text,
    modifier=
        safe_text,
    creator=
        safe_text
)
xwiki::Object_strategy = st.builds(
    xwiki::Object,
)
xwiki::EStringToStringMapEntry_strategy = st.builds(
    xwiki::EStringToStringMapEntry,
)
xwiki::DocumentRoot_strategy = st.builds(
    xwiki::DocumentRoot,
    mixed=
        safe_text
)
LinkCollection_strategy = st.builds(
    LinkCollection,
)
xwiki::Space_strategy = st.builds(
    xwiki::Space,
    xwikiAbsoluteUrl=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    wiki=
        safe_text,
    home=
        safe_text
)
xwiki::XWiki_strategy = st.builds(
    xwiki::XWiki,
    version=
        safe_text
)
xwiki::Translation_strategy = st.builds(
    xwiki::Translation,
    language=
        safe_text
)
xwiki::AttachmentsType_strategy = st.builds(
    xwiki::AttachmentsType,
)
xwiki::Class_strategy = st.builds(
    xwiki::Class,
    id=
        safe_text,
    name=
        safe_text
)
xwiki::HistoryType_strategy = st.builds(
    xwiki::HistoryType,
)
xwiki::Tag_strategy = st.builds(
    xwiki::Tag,
    name=
        safe_text
)
xwiki::TagsType_strategy = st.builds(
    xwiki::TagsType,
)
xwiki::SearchResultsType_strategy = st.builds(
    xwiki::SearchResultsType,
    template=
        safe_text
)
xwiki::Syntaxes_strategy = st.builds(
    xwiki::Syntaxes,
    syntax=
        safe_text
)
xwiki::Wiki_strategy = st.builds(
    xwiki::Wiki,
    owner=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    description=
        safe_text
)
xwiki::HistorySummary_strategy = st.builds(
    xwiki::HistorySummary,
    modifierName=
        safe_text,
    modified=
        safe_text,
    language=
        safe_text,
    space=
        safe_text,
    comment=
        safe_text,
    wiki=
        safe_text,
    pageId=
        safe_text,
    version=
        safe_text,
    minorVersion=
        safe_text,
    majorVersion=
        safe_text,
    modifier=
        safe_text,
    name=
        safe_text
)
xwiki::CommentsType_strategy = st.builds(
    xwiki::CommentsType,
)
xwiki::PropertiesType_strategy = st.builds(
    xwiki::PropertiesType,
)
xwiki::Translations_strategy = st.builds(
    xwiki::Translations,
    default=
        safe_text
)
xwiki::ClassesType_strategy = st.builds(
    xwiki::ClassesType,
)
xwiki::SearchResult_strategy = st.builds(
    xwiki::SearchResult,
    modified=
        safe_text,
    language=
        safe_text,
    space=
        safe_text,
    pageName=
        safe_text,
    type=
        safe_text,
    title=
        safe_text,
    className=
        safe_text,
    objectNumber=
        safe_text,
    pageFullName=
        safe_text,
    version=
        safe_text,
    score=
        safe_text,
    filename=
        safe_text,
    wiki=
        safe_text,
    author=
        safe_text,
    id=
        safe_text,
    authorName=
        safe_text
)
xwiki::SpacesType_strategy = st.builds(
    xwiki::SpacesType,
)
xwiki::ObjectSummary_strategy = st.builds(
    xwiki::ObjectSummary,
    pageAuthor=
        safe_text,
    number=
        safe_text,
    pageId=
        safe_text,
    id=
        safe_text,
    pageVersion=
        safe_text,
    className=
        safe_text,
    space=
        safe_text,
    pageName=
        safe_text,
    pageAuthorName=
        safe_text,
    headline=
        safe_text,
    wiki=
        safe_text,
    guid=
        safe_text
)
xwiki::Comment_strategy = st.builds(
    xwiki::Comment,
    highlight=
        safe_text,
    date=
        safe_text,
    author=
        safe_text,
    text=
        safe_text,
    replyTo=
        safe_text,
    pageId=
        safe_text,
    authorName=
        safe_text,
    id=
        safe_text
)
xwiki::ObjectsType_strategy = st.builds(
    xwiki::ObjectsType,
)
xwiki::PagesType_strategy = st.builds(
    xwiki::PagesType,
)
xwiki::WikisType_strategy = st.builds(
    xwiki::WikisType,
)
xwiki::Attribute_strategy = st.builds(
    xwiki::Attribute,
    value=
        safe_text,
    name=
        safe_text
)
xwiki::Property_strategy = st.builds(
    xwiki::Property,
    value=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
xwiki::PageSummary_strategy = st.builds(
    xwiki::PageSummary,
    syntax=
        safe_text,
    wiki=
        safe_text,
    author=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    title=
        safe_text,
    parentId=
        safe_text,
    space=
        safe_text,
    fullName=
        safe_text,
    id=
        safe_text,
    parent=
        safe_text,
    version=
        safe_text,
    authorName=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    name=
        safe_text
)
xwiki::Attachment_strategy = st.builds(
    xwiki::Attachment,
    pageId=
        safe_text,
    name=
        safe_text,
    date=
        safe_text,
    authorName=
        safe_text,
    pageVersion=
        safe_text,
    version=
        safe_text,
    mimeType=
        safe_text,
    xwikiRelativeUrl=
        safe_text,
    xwikiAbsoluteUrl=
        safe_text,
    author=
        safe_text,
    size=
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

@given(instance=xwiki::LinkCollection_strategy)
@settings(max_examples=50)
def test_xwiki::linkcollection_instantiation(instance):
    assert isinstance(instance, xwiki::LinkCollection)

@given(instance=xwiki::Link_strategy)
@settings(max_examples=50)
def test_xwiki::link_instantiation(instance):
    assert isinstance(instance, xwiki::Link)

@given(instance=xwiki::Link_strategy)
def test_xwiki::link_rel_type(instance):
    assert isinstance(instance.rel, str)


@given(instance=xwiki::Link_strategy)
def test_xwiki::link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original

@given(instance=xwiki::Link_strategy)
def test_xwiki::link_hrefLang_type(instance):
    assert isinstance(instance.hrefLang, str)


@given(instance=xwiki::Link_strategy)
def test_xwiki::link_hrefLang_setter(instance):
    original = instance.hrefLang
    instance.hrefLang = original
    assert instance.hrefLang == original

@given(instance=xwiki::Link_strategy)
def test_xwiki::link_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=xwiki::Link_strategy)
def test_xwiki::link_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xwiki::Link_strategy)
def test_xwiki::link_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xwiki::Link_strategy)
def test_xwiki::link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xwiki::Page_strategy)
@settings(max_examples=50)
def test_xwiki::page_instantiation(instance):
    assert isinstance(instance, xwiki::Page)

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_minorVersion_type(instance):
    assert isinstance(instance.minorVersion, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modifierName_type(instance):
    assert isinstance(instance.modifierName, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_created_type(instance):
    assert isinstance(instance.created, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_majorVersion_type(instance):
    assert isinstance(instance.majorVersion, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_creatorName_type(instance):
    assert isinstance(instance.creatorName, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_creatorName_setter(instance):
    original = instance.creatorName
    instance.creatorName = original
    assert instance.creatorName == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modified_type(instance):
    assert isinstance(instance.modified, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=xwiki::Page_strategy)
def test_xwiki::page_creator_type(instance):
    assert isinstance(instance.creator, str)


@given(instance=xwiki::Page_strategy)
def test_xwiki::page_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=xwiki::Object_strategy)
@settings(max_examples=50)
def test_xwiki::object_instantiation(instance):
    assert isinstance(instance, xwiki::Object)

@given(instance=xwiki::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xwiki::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xwiki::EStringToStringMapEntry)

@given(instance=xwiki::DocumentRoot_strategy)
@settings(max_examples=50)
def test_xwiki::documentroot_instantiation(instance):
    assert isinstance(instance, xwiki::DocumentRoot)

@given(instance=xwiki::DocumentRoot_strategy)
def test_xwiki::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xwiki::DocumentRoot_strategy)
def test_xwiki::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=LinkCollection_strategy)
@settings(max_examples=50)
def test_linkcollection_instantiation(instance):
    assert isinstance(instance, LinkCollection)

@given(instance=xwiki::Space_strategy)
@settings(max_examples=50)
def test_xwiki::space_instantiation(instance):
    assert isinstance(instance, xwiki::Space)

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_xwikiAbsoluteUrl_type(instance):
    assert isinstance(instance.xwikiAbsoluteUrl, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_xwikiRelativeUrl_type(instance):
    assert isinstance(instance.xwikiRelativeUrl, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_wiki_type(instance):
    assert isinstance(instance.wiki, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original

@given(instance=xwiki::Space_strategy)
def test_xwiki::space_home_type(instance):
    assert isinstance(instance.home, str)


@given(instance=xwiki::Space_strategy)
def test_xwiki::space_home_setter(instance):
    original = instance.home
    instance.home = original
    assert instance.home == original

@given(instance=xwiki::XWiki_strategy)
@settings(max_examples=50)
def test_xwiki::xwiki_instantiation(instance):
    assert isinstance(instance, xwiki::XWiki)

@given(instance=xwiki::XWiki_strategy)
def test_xwiki::xwiki_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xwiki::XWiki_strategy)
def test_xwiki::xwiki_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki::Translation_strategy)
@settings(max_examples=50)
def test_xwiki::translation_instantiation(instance):
    assert isinstance(instance, xwiki::Translation)

@given(instance=xwiki::Translation_strategy)
def test_xwiki::translation_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=xwiki::Translation_strategy)
def test_xwiki::translation_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki::AttachmentsType_strategy)
@settings(max_examples=50)
def test_xwiki::attachmentstype_instantiation(instance):
    assert isinstance(instance, xwiki::AttachmentsType)

@given(instance=xwiki::Class_strategy)
@settings(max_examples=50)
def test_xwiki::class_instantiation(instance):
    assert isinstance(instance, xwiki::Class)

@given(instance=xwiki::Class_strategy)
def test_xwiki::class_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::Class_strategy)
def test_xwiki::class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::Class_strategy)
def test_xwiki::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Class_strategy)
def test_xwiki::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::HistoryType_strategy)
@settings(max_examples=50)
def test_xwiki::historytype_instantiation(instance):
    assert isinstance(instance, xwiki::HistoryType)

@given(instance=xwiki::Tag_strategy)
@settings(max_examples=50)
def test_xwiki::tag_instantiation(instance):
    assert isinstance(instance, xwiki::Tag)

@given(instance=xwiki::Tag_strategy)
def test_xwiki::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Tag_strategy)
def test_xwiki::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::TagsType_strategy)
@settings(max_examples=50)
def test_xwiki::tagstype_instantiation(instance):
    assert isinstance(instance, xwiki::TagsType)

@given(instance=xwiki::SearchResultsType_strategy)
@settings(max_examples=50)
def test_xwiki::searchresultstype_instantiation(instance):
    assert isinstance(instance, xwiki::SearchResultsType)

@given(instance=xwiki::SearchResultsType_strategy)
def test_xwiki::searchresultstype_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=xwiki::SearchResultsType_strategy)
def test_xwiki::searchresultstype_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=xwiki::Syntaxes_strategy)
@settings(max_examples=50)
def test_xwiki::syntaxes_instantiation(instance):
    assert isinstance(instance, xwiki::Syntaxes)

@given(instance=xwiki::Syntaxes_strategy)
def test_xwiki::syntaxes_syntax_type(instance):
    assert isinstance(instance.syntax, str)


@given(instance=xwiki::Syntaxes_strategy)
def test_xwiki::syntaxes_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original

@given(instance=xwiki::Wiki_strategy)
@settings(max_examples=50)
def test_xwiki::wiki_instantiation(instance):
    assert isinstance(instance, xwiki::Wiki)

@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xwiki::Wiki_strategy)
def test_xwiki::wiki_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xwiki::HistorySummary_strategy)
@settings(max_examples=50)
def test_xwiki::historysummary_instantiation(instance):
    assert isinstance(instance, xwiki::HistorySummary)

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modifierName_type(instance):
    assert isinstance(instance.modifierName, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modifierName_setter(instance):
    original = instance.modifierName
    instance.modifierName = original
    assert instance.modifierName == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modified_type(instance):
    assert isinstance(instance.modified, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_wiki_type(instance):
    assert isinstance(instance.wiki, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_pageId_type(instance):
    assert isinstance(instance.pageId, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_minorVersion_type(instance):
    assert isinstance(instance.minorVersion, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_minorVersion_setter(instance):
    original = instance.minorVersion
    instance.minorVersion = original
    assert instance.minorVersion == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_majorVersion_type(instance):
    assert isinstance(instance.majorVersion, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_majorVersion_setter(instance):
    original = instance.majorVersion
    instance.majorVersion = original
    assert instance.majorVersion == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::HistorySummary_strategy)
def test_xwiki::historysummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::CommentsType_strategy)
@settings(max_examples=50)
def test_xwiki::commentstype_instantiation(instance):
    assert isinstance(instance, xwiki::CommentsType)

@given(instance=xwiki::PropertiesType_strategy)
@settings(max_examples=50)
def test_xwiki::propertiestype_instantiation(instance):
    assert isinstance(instance, xwiki::PropertiesType)

@given(instance=xwiki::Translations_strategy)
@settings(max_examples=50)
def test_xwiki::translations_instantiation(instance):
    assert isinstance(instance, xwiki::Translations)

@given(instance=xwiki::Translations_strategy)
def test_xwiki::translations_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=xwiki::Translations_strategy)
def test_xwiki::translations_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=xwiki::ClassesType_strategy)
@settings(max_examples=50)
def test_xwiki::classestype_instantiation(instance):
    assert isinstance(instance, xwiki::ClassesType)

@given(instance=xwiki::SearchResult_strategy)
@settings(max_examples=50)
def test_xwiki::searchresult_instantiation(instance):
    assert isinstance(instance, xwiki::SearchResult)

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_modified_type(instance):
    assert isinstance(instance.modified, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_pageName_type(instance):
    assert isinstance(instance.pageName, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_objectNumber_type(instance):
    assert isinstance(instance.objectNumber, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_objectNumber_setter(instance):
    original = instance.objectNumber
    instance.objectNumber = original
    assert instance.objectNumber == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_pageFullName_type(instance):
    assert isinstance(instance.pageFullName, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_pageFullName_setter(instance):
    original = instance.pageFullName
    instance.pageFullName = original
    assert instance.pageFullName == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_score_type(instance):
    assert isinstance(instance.score, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_wiki_type(instance):
    assert isinstance(instance.wiki, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_authorName_type(instance):
    assert isinstance(instance.authorName, str)


@given(instance=xwiki::SearchResult_strategy)
def test_xwiki::searchresult_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original

@given(instance=xwiki::SpacesType_strategy)
@settings(max_examples=50)
def test_xwiki::spacestype_instantiation(instance):
    assert isinstance(instance, xwiki::SpacesType)

@given(instance=xwiki::ObjectSummary_strategy)
@settings(max_examples=50)
def test_xwiki::objectsummary_instantiation(instance):
    assert isinstance(instance, xwiki::ObjectSummary)

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageAuthor_type(instance):
    assert isinstance(instance.pageAuthor, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageAuthor_setter(instance):
    original = instance.pageAuthor
    instance.pageAuthor = original
    assert instance.pageAuthor == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageId_type(instance):
    assert isinstance(instance.pageId, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageVersion_type(instance):
    assert isinstance(instance.pageVersion, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageName_type(instance):
    assert isinstance(instance.pageName, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageName_setter(instance):
    original = instance.pageName
    instance.pageName = original
    assert instance.pageName == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageAuthorName_type(instance):
    assert isinstance(instance.pageAuthorName, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_pageAuthorName_setter(instance):
    original = instance.pageAuthorName
    instance.pageAuthorName = original
    assert instance.pageAuthorName == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_headline_type(instance):
    assert isinstance(instance.headline, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_wiki_type(instance):
    assert isinstance(instance.wiki, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original

@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=xwiki::ObjectSummary_strategy)
def test_xwiki::objectsummary_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=xwiki::Comment_strategy)
@settings(max_examples=50)
def test_xwiki::comment_instantiation(instance):
    assert isinstance(instance, xwiki::Comment)

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_highlight_type(instance):
    assert isinstance(instance.highlight, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_highlight_setter(instance):
    original = instance.highlight
    instance.highlight = original
    assert instance.highlight == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_replyTo_type(instance):
    assert isinstance(instance.replyTo, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_replyTo_setter(instance):
    original = instance.replyTo
    instance.replyTo = original
    assert instance.replyTo == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_pageId_type(instance):
    assert isinstance(instance.pageId, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_authorName_type(instance):
    assert isinstance(instance.authorName, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original

@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::Comment_strategy)
def test_xwiki::comment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::ObjectsType_strategy)
@settings(max_examples=50)
def test_xwiki::objectstype_instantiation(instance):
    assert isinstance(instance, xwiki::ObjectsType)

@given(instance=xwiki::PagesType_strategy)
@settings(max_examples=50)
def test_xwiki::pagestype_instantiation(instance):
    assert isinstance(instance, xwiki::PagesType)

@given(instance=xwiki::WikisType_strategy)
@settings(max_examples=50)
def test_xwiki::wikistype_instantiation(instance):
    assert isinstance(instance, xwiki::WikisType)

@given(instance=xwiki::Attribute_strategy)
@settings(max_examples=50)
def test_xwiki::attribute_instantiation(instance):
    assert isinstance(instance, xwiki::Attribute)

@given(instance=xwiki::Attribute_strategy)
def test_xwiki::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xwiki::Attribute_strategy)
def test_xwiki::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xwiki::Attribute_strategy)
def test_xwiki::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Attribute_strategy)
def test_xwiki::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::Property_strategy)
@settings(max_examples=50)
def test_xwiki::property_instantiation(instance):
    assert isinstance(instance, xwiki::Property)

@given(instance=xwiki::Property_strategy)
def test_xwiki::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xwiki::Property_strategy)
def test_xwiki::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xwiki::Property_strategy)
def test_xwiki::property_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xwiki::Property_strategy)
def test_xwiki::property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xwiki::Property_strategy)
def test_xwiki::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Property_strategy)
def test_xwiki::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::PageSummary_strategy)
@settings(max_examples=50)
def test_xwiki::pagesummary_instantiation(instance):
    assert isinstance(instance, xwiki::PageSummary)

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_syntax_type(instance):
    assert isinstance(instance.syntax, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_syntax_setter(instance):
    original = instance.syntax
    instance.syntax = original
    assert instance.syntax == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_wiki_type(instance):
    assert isinstance(instance.wiki, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_wiki_setter(instance):
    original = instance.wiki
    instance.wiki = original
    assert instance.wiki == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_xwikiRelativeUrl_type(instance):
    assert isinstance(instance.xwikiRelativeUrl, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_parentId_type(instance):
    assert isinstance(instance.parentId, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_parent_type(instance):
    assert isinstance(instance.parent, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_authorName_type(instance):
    assert isinstance(instance.authorName, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_xwikiAbsoluteUrl_type(instance):
    assert isinstance(instance.xwikiAbsoluteUrl, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original

@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::PageSummary_strategy)
def test_xwiki::pagesummary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::Attachment_strategy)
@settings(max_examples=50)
def test_xwiki::attachment_instantiation(instance):
    assert isinstance(instance, xwiki::Attachment)

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_pageId_type(instance):
    assert isinstance(instance.pageId, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_pageId_setter(instance):
    original = instance.pageId
    instance.pageId = original
    assert instance.pageId == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_authorName_type(instance):
    assert isinstance(instance.authorName, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_pageVersion_type(instance):
    assert isinstance(instance.pageVersion, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_pageVersion_setter(instance):
    original = instance.pageVersion
    instance.pageVersion = original
    assert instance.pageVersion == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_mimeType_type(instance):
    assert isinstance(instance.mimeType, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_xwikiRelativeUrl_type(instance):
    assert isinstance(instance.xwikiRelativeUrl, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_xwikiRelativeUrl_setter(instance):
    original = instance.xwikiRelativeUrl
    instance.xwikiRelativeUrl = original
    assert instance.xwikiRelativeUrl == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_xwikiAbsoluteUrl_type(instance):
    assert isinstance(instance.xwikiAbsoluteUrl, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_xwikiAbsoluteUrl_setter(instance):
    original = instance.xwikiAbsoluteUrl
    instance.xwikiAbsoluteUrl = original
    assert instance.xwikiAbsoluteUrl == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xwiki::Attachment_strategy)
def test_xwiki::attachment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
