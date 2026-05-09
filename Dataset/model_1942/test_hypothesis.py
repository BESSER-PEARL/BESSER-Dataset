import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    docbook::ImageData,
    docbook::ImageObject,
    docbook::XMLElement,
    docbook::MediaObject,
    ParaMixedContent,
    docbook::SimpleText,
    Para,
    docbook::Tip,
    docbook::ProgramListing,
    docbook::Link,
    docbook::Ulink,
    docbook::Emphasis,
    XMLElement,
    docbook::Bookinfo,
    SectionMixedContent,
    docbook::Para,
    docbook::ParaMixedContent,
    docbook::TitledElement,
    docbook::Title,
    docbook::SectionMixedContent,
    TitledElement,
    docbook::Figure,
    docbook::Chapter,
    docbook::Section,
    docbook::Author,
    docbook::Subtitle,
    docbook::Book,
    docbook::Warning,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook::imagedata_is_not_abstract():
    assert not inspect.isabstract(docbook::ImageData)


def test_docbook::imagedata_constructor_exists():
    assert callable(docbook::ImageData.__init__)


def test_docbook::imagedata_constructor_args():
    sig = inspect.signature(docbook::ImageData.__init__)
    params = list(sig.parameters.keys())
    assert "depth" in params, "Missing parameter 'depth'"
    assert "width" in params, "Missing parameter 'width'"
    assert "fileref" in params, "Missing parameter 'fileref'"

def test_docbook::imagedata_has_depth():
    assert hasattr(docbook::ImageData, "depth")
    descriptor = None
    for klass in docbook::ImageData.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedata_has_width():
    assert hasattr(docbook::ImageData, "width")
    descriptor = None
    for klass in docbook::ImageData.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedata_has_fileref():
    assert hasattr(docbook::ImageData, "fileref")
    descriptor = None
    for klass in docbook::ImageData.__mro__:
        if "fileref" in klass.__dict__:
            descriptor = klass.__dict__["fileref"]
            break
    assert isinstance(descriptor, property)



def test_docbook::imageobject_is_not_abstract():
    assert not inspect.isabstract(docbook::ImageObject)


def test_docbook::imageobject_constructor_exists():
    assert callable(docbook::ImageObject.__init__)


def test_docbook::imageobject_constructor_args():
    sig = inspect.signature(docbook::ImageObject.__init__)
    params = list(sig.parameters.keys())



def test_docbook::xmlelement_is_not_abstract():
    assert not inspect.isabstract(docbook::XMLElement)


def test_docbook::xmlelement_constructor_exists():
    assert callable(docbook::XMLElement.__init__)


def test_docbook::xmlelement_constructor_args():
    sig = inspect.signature(docbook::XMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::xmlelement_has_id():
    assert hasattr(docbook::XMLElement, "id")
    descriptor = None
    for klass in docbook::XMLElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::mediaobject_is_not_abstract():
    assert not inspect.isabstract(docbook::MediaObject)


def test_docbook::mediaobject_constructor_exists():
    assert callable(docbook::MediaObject.__init__)


def test_docbook::mediaobject_constructor_args():
    sig = inspect.signature(docbook::MediaObject.__init__)
    params = list(sig.parameters.keys())



def test_paramixedcontent_is_not_abstract():
    assert not inspect.isabstract(ParaMixedContent)


def test_paramixedcontent_constructor_exists():
    assert callable(ParaMixedContent.__init__)


def test_paramixedcontent_constructor_args():
    sig = inspect.signature(ParaMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_docbook::simpletext_is_not_abstract():
    assert not inspect.isabstract(docbook::SimpleText)


def test_docbook::simpletext_constructor_exists():
    assert callable(docbook::SimpleText.__init__)


def test_docbook::simpletext_constructor_args():
    sig = inspect.signature(docbook::SimpleText.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_docbook::simpletext_has_data():
    assert hasattr(docbook::SimpleText, "data")
    descriptor = None
    for klass in docbook::SimpleText.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_para_is_not_abstract():
    assert not inspect.isabstract(Para)


def test_para_constructor_exists():
    assert callable(Para.__init__)


def test_para_constructor_args():
    sig = inspect.signature(Para.__init__)
    params = list(sig.parameters.keys())



def test_docbook::tip_is_not_abstract():
    assert not inspect.isabstract(docbook::Tip)


def test_docbook::tip_constructor_exists():
    assert callable(docbook::Tip.__init__)


def test_docbook::tip_constructor_args():
    sig = inspect.signature(docbook::Tip.__init__)
    params = list(sig.parameters.keys())



def test_docbook::programlisting_is_not_abstract():
    assert not inspect.isabstract(docbook::ProgramListing)


def test_docbook::programlisting_constructor_exists():
    assert callable(docbook::ProgramListing.__init__)


def test_docbook::programlisting_constructor_args():
    sig = inspect.signature(docbook::ProgramListing.__init__)
    params = list(sig.parameters.keys())



def test_docbook::link_is_not_abstract():
    assert not inspect.isabstract(docbook::Link)


def test_docbook::link_constructor_exists():
    assert callable(docbook::Link.__init__)


def test_docbook::link_constructor_args():
    sig = inspect.signature(docbook::Link.__init__)
    params = list(sig.parameters.keys())



def test_docbook::ulink_is_not_abstract():
    assert not inspect.isabstract(docbook::Ulink)


def test_docbook::ulink_constructor_exists():
    assert callable(docbook::Ulink.__init__)


def test_docbook::ulink_constructor_args():
    sig = inspect.signature(docbook::Ulink.__init__)
    params = list(sig.parameters.keys())



def test_docbook::emphasis_is_not_abstract():
    assert not inspect.isabstract(docbook::Emphasis)


def test_docbook::emphasis_constructor_exists():
    assert callable(docbook::Emphasis.__init__)


def test_docbook::emphasis_constructor_args():
    sig = inspect.signature(docbook::Emphasis.__init__)
    params = list(sig.parameters.keys())



def test_xmlelement_is_not_abstract():
    assert not inspect.isabstract(XMLElement)


def test_xmlelement_constructor_exists():
    assert callable(XMLElement.__init__)


def test_xmlelement_constructor_args():
    sig = inspect.signature(XMLElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook::bookinfo_is_not_abstract():
    assert not inspect.isabstract(docbook::Bookinfo)


def test_docbook::bookinfo_constructor_exists():
    assert callable(docbook::Bookinfo.__init__)


def test_docbook::bookinfo_constructor_args():
    sig = inspect.signature(docbook::Bookinfo.__init__)
    params = list(sig.parameters.keys())
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "date" in params, "Missing parameter 'date'"

def test_docbook::bookinfo_has_pubdate():
    assert hasattr(docbook::Bookinfo, "pubdate")
    descriptor = None
    for klass in docbook::Bookinfo.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_docbook::bookinfo_has_date():
    assert hasattr(docbook::Bookinfo, "date")
    descriptor = None
    for klass in docbook::Bookinfo.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_sectionmixedcontent_is_not_abstract():
    assert not inspect.isabstract(SectionMixedContent)


def test_sectionmixedcontent_constructor_exists():
    assert callable(SectionMixedContent.__init__)


def test_sectionmixedcontent_constructor_args():
    sig = inspect.signature(SectionMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_docbook::para_is_not_abstract():
    assert not inspect.isabstract(docbook::Para)


def test_docbook::para_constructor_exists():
    assert callable(docbook::Para.__init__)


def test_docbook::para_constructor_args():
    sig = inspect.signature(docbook::Para.__init__)
    params = list(sig.parameters.keys())



def test_docbook::paramixedcontent_is_not_abstract():
    assert not inspect.isabstract(docbook::ParaMixedContent)


def test_docbook::paramixedcontent_constructor_exists():
    assert callable(docbook::ParaMixedContent.__init__)


def test_docbook::paramixedcontent_constructor_args():
    sig = inspect.signature(docbook::ParaMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_docbook::titledelement_is_not_abstract():
    assert not inspect.isabstract(docbook::TitledElement)


def test_docbook::titledelement_constructor_exists():
    assert callable(docbook::TitledElement.__init__)


def test_docbook::titledelement_constructor_args():
    sig = inspect.signature(docbook::TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook::title_is_not_abstract():
    assert not inspect.isabstract(docbook::Title)


def test_docbook::title_constructor_exists():
    assert callable(docbook::Title.__init__)


def test_docbook::title_constructor_args():
    sig = inspect.signature(docbook::Title.__init__)
    params = list(sig.parameters.keys())



def test_docbook::sectionmixedcontent_is_not_abstract():
    assert not inspect.isabstract(docbook::SectionMixedContent)


def test_docbook::sectionmixedcontent_constructor_exists():
    assert callable(docbook::SectionMixedContent.__init__)


def test_docbook::sectionmixedcontent_constructor_args():
    sig = inspect.signature(docbook::SectionMixedContent.__init__)
    params = list(sig.parameters.keys())



def test_titledelement_is_not_abstract():
    assert not inspect.isabstract(TitledElement)


def test_titledelement_constructor_exists():
    assert callable(TitledElement.__init__)


def test_titledelement_constructor_args():
    sig = inspect.signature(TitledElement.__init__)
    params = list(sig.parameters.keys())



def test_docbook::figure_is_not_abstract():
    assert not inspect.isabstract(docbook::Figure)


def test_docbook::figure_constructor_exists():
    assert callable(docbook::Figure.__init__)


def test_docbook::figure_constructor_args():
    sig = inspect.signature(docbook::Figure.__init__)
    params = list(sig.parameters.keys())



def test_docbook::chapter_is_not_abstract():
    assert not inspect.isabstract(docbook::Chapter)


def test_docbook::chapter_constructor_exists():
    assert callable(docbook::Chapter.__init__)


def test_docbook::chapter_constructor_args():
    sig = inspect.signature(docbook::Chapter.__init__)
    params = list(sig.parameters.keys())



def test_docbook::section_is_not_abstract():
    assert not inspect.isabstract(docbook::Section)


def test_docbook::section_constructor_exists():
    assert callable(docbook::Section.__init__)


def test_docbook::section_constructor_args():
    sig = inspect.signature(docbook::Section.__init__)
    params = list(sig.parameters.keys())



def test_docbook::author_is_not_abstract():
    assert not inspect.isabstract(docbook::Author)


def test_docbook::author_constructor_exists():
    assert callable(docbook::Author.__init__)


def test_docbook::author_constructor_args():
    sig = inspect.signature(docbook::Author.__init__)
    params = list(sig.parameters.keys())
    assert "authorblug" in params, "Missing parameter 'authorblug'"
    assert "honorific" in params, "Missing parameter 'honorific'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_docbook::author_has_authorblug():
    assert hasattr(docbook::Author, "authorblug")
    descriptor = None
    for klass in docbook::Author.__mro__:
        if "authorblug" in klass.__dict__:
            descriptor = klass.__dict__["authorblug"]
            break
    assert isinstance(descriptor, property)

def test_docbook::author_has_honorific():
    assert hasattr(docbook::Author, "honorific")
    descriptor = None
    for klass in docbook::Author.__mro__:
        if "honorific" in klass.__dict__:
            descriptor = klass.__dict__["honorific"]
            break
    assert isinstance(descriptor, property)

def test_docbook::author_has_surname():
    assert hasattr(docbook::Author, "surname")
    descriptor = None
    for klass in docbook::Author.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_docbook::author_has_firstname():
    assert hasattr(docbook::Author, "firstname")
    descriptor = None
    for klass in docbook::Author.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_docbook::subtitle_is_not_abstract():
    assert not inspect.isabstract(docbook::Subtitle)


def test_docbook::subtitle_constructor_exists():
    assert callable(docbook::Subtitle.__init__)


def test_docbook::subtitle_constructor_args():
    sig = inspect.signature(docbook::Subtitle.__init__)
    params = list(sig.parameters.keys())



def test_docbook::book_is_not_abstract():
    assert not inspect.isabstract(docbook::Book)


def test_docbook::book_constructor_exists():
    assert callable(docbook::Book.__init__)


def test_docbook::book_constructor_args():
    sig = inspect.signature(docbook::Book.__init__)
    params = list(sig.parameters.keys())



def test_docbook::warning_is_not_abstract():
    assert not inspect.isabstract(docbook::Warning)


def test_docbook::warning_constructor_exists():
    assert callable(docbook::Warning.__init__)


def test_docbook::warning_constructor_args():
    sig = inspect.signature(docbook::Warning.__init__)
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
docbook::ImageData_strategy = st.builds(
    docbook::ImageData,
    depth=
        safe_text,
    width=
        safe_text,
    fileref=
        safe_text
)
docbook::ImageObject_strategy = st.builds(
    docbook::ImageObject,
)
docbook::XMLElement_strategy = st.builds(
    docbook::XMLElement,
    id=
        safe_text
)
docbook::MediaObject_strategy = st.builds(
    docbook::MediaObject,
)
ParaMixedContent_strategy = st.builds(
    ParaMixedContent,
)
docbook::SimpleText_strategy = st.builds(
    docbook::SimpleText,
    data=
        safe_text
)
Para_strategy = st.builds(
    Para,
)
docbook::Tip_strategy = st.builds(
    docbook::Tip,
)
docbook::ProgramListing_strategy = st.builds(
    docbook::ProgramListing,
)
docbook::Link_strategy = st.builds(
    docbook::Link,
)
docbook::Ulink_strategy = st.builds(
    docbook::Ulink,
)
docbook::Emphasis_strategy = st.builds(
    docbook::Emphasis,
)
XMLElement_strategy = st.builds(
    XMLElement,
)
docbook::Bookinfo_strategy = st.builds(
    docbook::Bookinfo,
    pubdate=
        safe_text,
    date=
        safe_text
)
SectionMixedContent_strategy = st.builds(
    SectionMixedContent,
)
docbook::Para_strategy = st.builds(
    docbook::Para,
)
docbook::ParaMixedContent_strategy = st.builds(
    docbook::ParaMixedContent,
)
docbook::TitledElement_strategy = st.builds(
    docbook::TitledElement,
)
docbook::Title_strategy = st.builds(
    docbook::Title,
)
docbook::SectionMixedContent_strategy = st.builds(
    docbook::SectionMixedContent,
)
TitledElement_strategy = st.builds(
    TitledElement,
)
docbook::Figure_strategy = st.builds(
    docbook::Figure,
)
docbook::Chapter_strategy = st.builds(
    docbook::Chapter,
)
docbook::Section_strategy = st.builds(
    docbook::Section,
)
docbook::Author_strategy = st.builds(
    docbook::Author,
    authorblug=
        safe_text,
    honorific=
        safe_text,
    surname=
        safe_text,
    firstname=
        safe_text
)
docbook::Subtitle_strategy = st.builds(
    docbook::Subtitle,
)
docbook::Book_strategy = st.builds(
    docbook::Book,
)
docbook::Warning_strategy = st.builds(
    docbook::Warning,
)

@given(instance=docbook::ImageData_strategy)
@settings(max_examples=50)
def test_docbook::imagedata_instantiation(instance):
    assert isinstance(instance, docbook::ImageData)

@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_depth_type(instance):
    assert isinstance(instance.depth, str)


@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_fileref_type(instance):
    assert isinstance(instance.fileref, str)


@given(instance=docbook::ImageData_strategy)
def test_docbook::imagedata_fileref_setter(instance):
    original = instance.fileref
    instance.fileref = original
    assert instance.fileref == original

@given(instance=docbook::ImageObject_strategy)
@settings(max_examples=50)
def test_docbook::imageobject_instantiation(instance):
    assert isinstance(instance, docbook::ImageObject)

@given(instance=docbook::XMLElement_strategy)
@settings(max_examples=50)
def test_docbook::xmlelement_instantiation(instance):
    assert isinstance(instance, docbook::XMLElement)

@given(instance=docbook::XMLElement_strategy)
def test_docbook::xmlelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=docbook::XMLElement_strategy)
def test_docbook::xmlelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=docbook::MediaObject_strategy)
@settings(max_examples=50)
def test_docbook::mediaobject_instantiation(instance):
    assert isinstance(instance, docbook::MediaObject)

@given(instance=ParaMixedContent_strategy)
@settings(max_examples=50)
def test_paramixedcontent_instantiation(instance):
    assert isinstance(instance, ParaMixedContent)

@given(instance=docbook::SimpleText_strategy)
@settings(max_examples=50)
def test_docbook::simpletext_instantiation(instance):
    assert isinstance(instance, docbook::SimpleText)

@given(instance=docbook::SimpleText_strategy)
def test_docbook::simpletext_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=docbook::SimpleText_strategy)
def test_docbook::simpletext_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Para_strategy)
@settings(max_examples=50)
def test_para_instantiation(instance):
    assert isinstance(instance, Para)

@given(instance=docbook::Tip_strategy)
@settings(max_examples=50)
def test_docbook::tip_instantiation(instance):
    assert isinstance(instance, docbook::Tip)

@given(instance=docbook::ProgramListing_strategy)
@settings(max_examples=50)
def test_docbook::programlisting_instantiation(instance):
    assert isinstance(instance, docbook::ProgramListing)

@given(instance=docbook::Link_strategy)
@settings(max_examples=50)
def test_docbook::link_instantiation(instance):
    assert isinstance(instance, docbook::Link)

@given(instance=docbook::Ulink_strategy)
@settings(max_examples=50)
def test_docbook::ulink_instantiation(instance):
    assert isinstance(instance, docbook::Ulink)

@given(instance=docbook::Emphasis_strategy)
@settings(max_examples=50)
def test_docbook::emphasis_instantiation(instance):
    assert isinstance(instance, docbook::Emphasis)

@given(instance=XMLElement_strategy)
@settings(max_examples=50)
def test_xmlelement_instantiation(instance):
    assert isinstance(instance, XMLElement)

@given(instance=docbook::Bookinfo_strategy)
@settings(max_examples=50)
def test_docbook::bookinfo_instantiation(instance):
    assert isinstance(instance, docbook::Bookinfo)

@given(instance=docbook::Bookinfo_strategy)
def test_docbook::bookinfo_pubdate_type(instance):
    assert isinstance(instance.pubdate, str)


@given(instance=docbook::Bookinfo_strategy)
def test_docbook::bookinfo_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original

@given(instance=docbook::Bookinfo_strategy)
def test_docbook::bookinfo_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=docbook::Bookinfo_strategy)
def test_docbook::bookinfo_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=SectionMixedContent_strategy)
@settings(max_examples=50)
def test_sectionmixedcontent_instantiation(instance):
    assert isinstance(instance, SectionMixedContent)

@given(instance=docbook::Para_strategy)
@settings(max_examples=50)
def test_docbook::para_instantiation(instance):
    assert isinstance(instance, docbook::Para)

@given(instance=docbook::ParaMixedContent_strategy)
@settings(max_examples=50)
def test_docbook::paramixedcontent_instantiation(instance):
    assert isinstance(instance, docbook::ParaMixedContent)

@given(instance=docbook::TitledElement_strategy)
@settings(max_examples=50)
def test_docbook::titledelement_instantiation(instance):
    assert isinstance(instance, docbook::TitledElement)

@given(instance=docbook::Title_strategy)
@settings(max_examples=50)
def test_docbook::title_instantiation(instance):
    assert isinstance(instance, docbook::Title)

@given(instance=docbook::SectionMixedContent_strategy)
@settings(max_examples=50)
def test_docbook::sectionmixedcontent_instantiation(instance):
    assert isinstance(instance, docbook::SectionMixedContent)

@given(instance=TitledElement_strategy)
@settings(max_examples=50)
def test_titledelement_instantiation(instance):
    assert isinstance(instance, TitledElement)

@given(instance=docbook::Figure_strategy)
@settings(max_examples=50)
def test_docbook::figure_instantiation(instance):
    assert isinstance(instance, docbook::Figure)

@given(instance=docbook::Chapter_strategy)
@settings(max_examples=50)
def test_docbook::chapter_instantiation(instance):
    assert isinstance(instance, docbook::Chapter)

@given(instance=docbook::Section_strategy)
@settings(max_examples=50)
def test_docbook::section_instantiation(instance):
    assert isinstance(instance, docbook::Section)

@given(instance=docbook::Author_strategy)
@settings(max_examples=50)
def test_docbook::author_instantiation(instance):
    assert isinstance(instance, docbook::Author)

@given(instance=docbook::Author_strategy)
def test_docbook::author_authorblug_type(instance):
    assert isinstance(instance.authorblug, str)


@given(instance=docbook::Author_strategy)
def test_docbook::author_authorblug_setter(instance):
    original = instance.authorblug
    instance.authorblug = original
    assert instance.authorblug == original

@given(instance=docbook::Author_strategy)
def test_docbook::author_honorific_type(instance):
    assert isinstance(instance.honorific, str)


@given(instance=docbook::Author_strategy)
def test_docbook::author_honorific_setter(instance):
    original = instance.honorific
    instance.honorific = original
    assert instance.honorific == original

@given(instance=docbook::Author_strategy)
def test_docbook::author_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=docbook::Author_strategy)
def test_docbook::author_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=docbook::Author_strategy)
def test_docbook::author_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=docbook::Author_strategy)
def test_docbook::author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=docbook::Subtitle_strategy)
@settings(max_examples=50)
def test_docbook::subtitle_instantiation(instance):
    assert isinstance(instance, docbook::Subtitle)

@given(instance=docbook::Book_strategy)
@settings(max_examples=50)
def test_docbook::book_instantiation(instance):
    assert isinstance(instance, docbook::Book)

@given(instance=docbook::Warning_strategy)
@settings(max_examples=50)
def test_docbook::warning_instantiation(instance):
    assert isinstance(instance, docbook::Warning)
