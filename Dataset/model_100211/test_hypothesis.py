import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    documentation::TextContainer,
    documentation::Width,
    documentation::TableRow,
    documentation::TableHeader,
    documentation::TableCell,
    documentation::ListItem,
    documentation::NamedElement,
    TextContainer,
    documentation::FragmentContainer,
    Fragment,
    documentation::Text,
    documentation::Paragraph,
    documentation::PageBreak,
    documentation::Table,
    documentation::Listing,
    NamedElement,
    documentation::Image,
    documentation::Link,
    documentation::XML,
    FragmentContainer,
    documentation::Subsection,
    documentation::Subsubsection,
    documentation::List,
    Text,
    documentation::Code,
    documentation::HtmlCode,
    documentation::Reference,
    documentation::Line,
    documentation::Fragment,
    documentation::TermEntry,
    documentation::Section,
    documentation::Documentation,
    Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_documentation::textcontainer_is_not_abstract():
    assert not inspect.isabstract(documentation::TextContainer)


def test_documentation::textcontainer_constructor_exists():
    assert callable(documentation::TextContainer.__init__)


def test_documentation::textcontainer_constructor_args():
    sig = inspect.signature(documentation::TextContainer.__init__)
    params = list(sig.parameters.keys())



def test_documentation::width_is_not_abstract():
    assert not inspect.isabstract(documentation::Width)


def test_documentation::width_constructor_exists():
    assert callable(documentation::Width.__init__)


def test_documentation::width_constructor_args():
    sig = inspect.signature(documentation::Width.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_documentation::width_has_width():
    assert hasattr(documentation::Width, "width")
    descriptor = None
    for klass in documentation::Width.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_documentation::width_has_unit():
    assert hasattr(documentation::Width, "unit")
    descriptor = None
    for klass in documentation::Width.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_documentation::tablerow_is_not_abstract():
    assert not inspect.isabstract(documentation::TableRow)


def test_documentation::tablerow_constructor_exists():
    assert callable(documentation::TableRow.__init__)


def test_documentation::tablerow_constructor_args():
    sig = inspect.signature(documentation::TableRow.__init__)
    params = list(sig.parameters.keys())



def test_documentation::tableheader_is_not_abstract():
    assert not inspect.isabstract(documentation::TableHeader)


def test_documentation::tableheader_constructor_exists():
    assert callable(documentation::TableHeader.__init__)


def test_documentation::tableheader_constructor_args():
    sig = inspect.signature(documentation::TableHeader.__init__)
    params = list(sig.parameters.keys())



def test_documentation::tablecell_is_not_abstract():
    assert not inspect.isabstract(documentation::TableCell)


def test_documentation::tablecell_constructor_exists():
    assert callable(documentation::TableCell.__init__)


def test_documentation::tablecell_constructor_args():
    sig = inspect.signature(documentation::TableCell.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "content" in params, "Missing parameter 'content'"

def test_documentation::tablecell_has_span():
    assert hasattr(documentation::TableCell, "span")
    descriptor = None
    for klass in documentation::TableCell.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_documentation::tablecell_has_content():
    assert hasattr(documentation::TableCell, "content")
    descriptor = None
    for klass in documentation::TableCell.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_documentation::listitem_is_not_abstract():
    assert not inspect.isabstract(documentation::ListItem)


def test_documentation::listitem_constructor_exists():
    assert callable(documentation::ListItem.__init__)


def test_documentation::listitem_constructor_args():
    sig = inspect.signature(documentation::ListItem.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_documentation::listitem_has_text():
    assert hasattr(documentation::ListItem, "text")
    descriptor = None
    for klass in documentation::ListItem.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_documentation::namedelement_is_not_abstract():
    assert not inspect.isabstract(documentation::NamedElement)


def test_documentation::namedelement_constructor_exists():
    assert callable(documentation::NamedElement.__init__)


def test_documentation::namedelement_constructor_args():
    sig = inspect.signature(documentation::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_documentation::namedelement_has_id():
    assert hasattr(documentation::NamedElement, "id")
    descriptor = None
    for klass in documentation::NamedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_documentation::namedelement_has_name():
    assert hasattr(documentation::NamedElement, "name")
    descriptor = None
    for klass in documentation::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_documentation::namedelement_has_label():
    assert hasattr(documentation::NamedElement, "label")
    descriptor = None
    for klass in documentation::NamedElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_textcontainer_is_not_abstract():
    assert not inspect.isabstract(TextContainer)


def test_textcontainer_constructor_exists():
    assert callable(TextContainer.__init__)


def test_textcontainer_constructor_args():
    sig = inspect.signature(TextContainer.__init__)
    params = list(sig.parameters.keys())



def test_documentation::fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(documentation::FragmentContainer)


def test_documentation::fragmentcontainer_constructor_exists():
    assert callable(documentation::FragmentContainer.__init__)


def test_documentation::fragmentcontainer_constructor_args():
    sig = inspect.signature(documentation::FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_fragment_is_not_abstract():
    assert not inspect.isabstract(Fragment)


def test_fragment_constructor_exists():
    assert callable(Fragment.__init__)


def test_fragment_constructor_args():
    sig = inspect.signature(Fragment.__init__)
    params = list(sig.parameters.keys())



def test_documentation::text_is_not_abstract():
    assert not inspect.isabstract(documentation::Text)


def test_documentation::text_constructor_exists():
    assert callable(documentation::Text.__init__)


def test_documentation::text_constructor_args():
    sig = inspect.signature(documentation::Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_documentation::text_has_text():
    assert hasattr(documentation::Text, "text")
    descriptor = None
    for klass in documentation::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_documentation::paragraph_is_not_abstract():
    assert not inspect.isabstract(documentation::Paragraph)


def test_documentation::paragraph_constructor_exists():
    assert callable(documentation::Paragraph.__init__)


def test_documentation::paragraph_constructor_args():
    sig = inspect.signature(documentation::Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_documentation::pagebreak_is_not_abstract():
    assert not inspect.isabstract(documentation::PageBreak)


def test_documentation::pagebreak_constructor_exists():
    assert callable(documentation::PageBreak.__init__)


def test_documentation::pagebreak_constructor_args():
    sig = inspect.signature(documentation::PageBreak.__init__)
    params = list(sig.parameters.keys())



def test_documentation::table_is_not_abstract():
    assert not inspect.isabstract(documentation::Table)


def test_documentation::table_constructor_exists():
    assert callable(documentation::Table.__init__)


def test_documentation::table_constructor_args():
    sig = inspect.signature(documentation::Table.__init__)
    params = list(sig.parameters.keys())



def test_documentation::listing_is_not_abstract():
    assert not inspect.isabstract(documentation::Listing)


def test_documentation::listing_constructor_exists():
    assert callable(documentation::Listing.__init__)


def test_documentation::listing_constructor_args():
    sig = inspect.signature(documentation::Listing.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_documentation::image_is_not_abstract():
    assert not inspect.isabstract(documentation::Image)


def test_documentation::image_constructor_exists():
    assert callable(documentation::Image.__init__)


def test_documentation::image_constructor_args():
    sig = inspect.signature(documentation::Image.__init__)
    params = list(sig.parameters.keys())
    assert "contextClassName" in params, "Missing parameter 'contextClassName'"
    assert "resource" in params, "Missing parameter 'resource'"
    assert "originalSource" in params, "Missing parameter 'originalSource'"

def test_documentation::image_has_contextClassName():
    assert hasattr(documentation::Image, "contextClassName")
    descriptor = None
    for klass in documentation::Image.__mro__:
        if "contextClassName" in klass.__dict__:
            descriptor = klass.__dict__["contextClassName"]
            break
    assert isinstance(descriptor, property)

def test_documentation::image_has_resource():
    assert hasattr(documentation::Image, "resource")
    descriptor = None
    for klass in documentation::Image.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)

def test_documentation::image_has_originalSource():
    assert hasattr(documentation::Image, "originalSource")
    descriptor = None
    for klass in documentation::Image.__mro__:
        if "originalSource" in klass.__dict__:
            descriptor = klass.__dict__["originalSource"]
            break
    assert isinstance(descriptor, property)



def test_documentation::link_is_not_abstract():
    assert not inspect.isabstract(documentation::Link)


def test_documentation::link_constructor_exists():
    assert callable(documentation::Link.__init__)


def test_documentation::link_constructor_args():
    sig = inspect.signature(documentation::Link.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_documentation::link_has_uri():
    assert hasattr(documentation::Link, "uri")
    descriptor = None
    for klass in documentation::Link.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_documentation::xml_is_not_abstract():
    assert not inspect.isabstract(documentation::XML)


def test_documentation::xml_constructor_exists():
    assert callable(documentation::XML.__init__)


def test_documentation::xml_constructor_args():
    sig = inspect.signature(documentation::XML.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "contextClassName" in params, "Missing parameter 'contextClassName'"
    assert "resource" in params, "Missing parameter 'resource'"

def test_documentation::xml_has_content():
    assert hasattr(documentation::XML, "content")
    descriptor = None
    for klass in documentation::XML.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_documentation::xml_has_contextClassName():
    assert hasattr(documentation::XML, "contextClassName")
    descriptor = None
    for klass in documentation::XML.__mro__:
        if "contextClassName" in klass.__dict__:
            descriptor = klass.__dict__["contextClassName"]
            break
    assert isinstance(descriptor, property)

def test_documentation::xml_has_resource():
    assert hasattr(documentation::XML, "resource")
    descriptor = None
    for klass in documentation::XML.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)



def test_fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(FragmentContainer)


def test_fragmentcontainer_constructor_exists():
    assert callable(FragmentContainer.__init__)


def test_fragmentcontainer_constructor_args():
    sig = inspect.signature(FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_documentation::subsection_is_not_abstract():
    assert not inspect.isabstract(documentation::Subsection)


def test_documentation::subsection_constructor_exists():
    assert callable(documentation::Subsection.__init__)


def test_documentation::subsection_constructor_args():
    sig = inspect.signature(documentation::Subsection.__init__)
    params = list(sig.parameters.keys())



def test_documentation::subsubsection_is_not_abstract():
    assert not inspect.isabstract(documentation::Subsubsection)


def test_documentation::subsubsection_constructor_exists():
    assert callable(documentation::Subsubsection.__init__)


def test_documentation::subsubsection_constructor_args():
    sig = inspect.signature(documentation::Subsubsection.__init__)
    params = list(sig.parameters.keys())



def test_documentation::list_is_not_abstract():
    assert not inspect.isabstract(documentation::List)


def test_documentation::list_constructor_exists():
    assert callable(documentation::List.__init__)


def test_documentation::list_constructor_args():
    sig = inspect.signature(documentation::List.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_documentation::code_is_not_abstract():
    assert not inspect.isabstract(documentation::Code)


def test_documentation::code_constructor_exists():
    assert callable(documentation::Code.__init__)


def test_documentation::code_constructor_args():
    sig = inspect.signature(documentation::Code.__init__)
    params = list(sig.parameters.keys())



def test_documentation::htmlcode_is_not_abstract():
    assert not inspect.isabstract(documentation::HtmlCode)


def test_documentation::htmlcode_constructor_exists():
    assert callable(documentation::HtmlCode.__init__)


def test_documentation::htmlcode_constructor_args():
    sig = inspect.signature(documentation::HtmlCode.__init__)
    params = list(sig.parameters.keys())



def test_documentation::reference_is_not_abstract():
    assert not inspect.isabstract(documentation::Reference)


def test_documentation::reference_constructor_exists():
    assert callable(documentation::Reference.__init__)


def test_documentation::reference_constructor_args():
    sig = inspect.signature(documentation::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "referredLabel" in params, "Missing parameter 'referredLabel'"

def test_documentation::reference_has_referredLabel():
    assert hasattr(documentation::Reference, "referredLabel")
    descriptor = None
    for klass in documentation::Reference.__mro__:
        if "referredLabel" in klass.__dict__:
            descriptor = klass.__dict__["referredLabel"]
            break
    assert isinstance(descriptor, property)



def test_documentation::line_is_not_abstract():
    assert not inspect.isabstract(documentation::Line)


def test_documentation::line_constructor_exists():
    assert callable(documentation::Line.__init__)


def test_documentation::line_constructor_args():
    sig = inspect.signature(documentation::Line.__init__)
    params = list(sig.parameters.keys())



def test_documentation::fragment_is_not_abstract():
    assert not inspect.isabstract(documentation::Fragment)


def test_documentation::fragment_constructor_exists():
    assert callable(documentation::Fragment.__init__)


def test_documentation::fragment_constructor_args():
    sig = inspect.signature(documentation::Fragment.__init__)
    params = list(sig.parameters.keys())



def test_documentation::termentry_is_not_abstract():
    assert not inspect.isabstract(documentation::TermEntry)


def test_documentation::termentry_constructor_exists():
    assert callable(documentation::TermEntry.__init__)


def test_documentation::termentry_constructor_args():
    sig = inspect.signature(documentation::TermEntry.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_documentation::termentry_has_description():
    assert hasattr(documentation::TermEntry, "description")
    descriptor = None
    for klass in documentation::TermEntry.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_documentation::section_is_not_abstract():
    assert not inspect.isabstract(documentation::Section)


def test_documentation::section_constructor_exists():
    assert callable(documentation::Section.__init__)


def test_documentation::section_constructor_args():
    sig = inspect.signature(documentation::Section.__init__)
    params = list(sig.parameters.keys())



def test_documentation::documentation_is_not_abstract():
    assert not inspect.isabstract(documentation::Documentation)


def test_documentation::documentation_constructor_exists():
    assert callable(documentation::Documentation.__init__)


def test_documentation::documentation_constructor_args():
    sig = inspect.signature(documentation::Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_documentation::documentation_has_title():
    assert hasattr(documentation::Documentation, "title")
    descriptor = None
    for klass in documentation::Documentation.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_unit_exists():
    # Check that the Enumeration exists
    assert Unit is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Unit]
    expected_literals = [
        "PERCENT",
        "PIXELS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Unit"


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
documentation::TextContainer_strategy = st.builds(
    documentation::TextContainer,
)
documentation::Width_strategy = st.builds(
    documentation::Width,
    width=
        safe_text,
    unit=
        safe_text
)
documentation::TableRow_strategy = st.builds(
    documentation::TableRow,
)
documentation::TableHeader_strategy = st.builds(
    documentation::TableHeader,
)
documentation::TableCell_strategy = st.builds(
    documentation::TableCell,
    span=
        st.integers(),
    content=
        safe_text
)
documentation::ListItem_strategy = st.builds(
    documentation::ListItem,
    text=
        safe_text
)
documentation::NamedElement_strategy = st.builds(
    documentation::NamedElement,
    id=
        safe_text,
    name=
        safe_text,
    label=
        safe_text
)
TextContainer_strategy = st.builds(
    TextContainer,
)
documentation::FragmentContainer_strategy = st.builds(
    documentation::FragmentContainer,
)
Fragment_strategy = st.builds(
    Fragment,
)
documentation::Text_strategy = st.builds(
    documentation::Text,
    text=
        safe_text
)
documentation::Paragraph_strategy = st.builds(
    documentation::Paragraph,
)
documentation::PageBreak_strategy = st.builds(
    documentation::PageBreak,
)
documentation::Table_strategy = st.builds(
    documentation::Table,
)
documentation::Listing_strategy = st.builds(
    documentation::Listing,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
documentation::Image_strategy = st.builds(
    documentation::Image,
    contextClassName=
        safe_text,
    resource=
        safe_text,
    originalSource=
        safe_text
)
documentation::Link_strategy = st.builds(
    documentation::Link,
    uri=
        safe_text
)
documentation::XML_strategy = st.builds(
    documentation::XML,
    content=
        safe_text,
    contextClassName=
        safe_text,
    resource=
        safe_text
)
FragmentContainer_strategy = st.builds(
    FragmentContainer,
)
documentation::Subsection_strategy = st.builds(
    documentation::Subsection,
)
documentation::Subsubsection_strategy = st.builds(
    documentation::Subsubsection,
)
documentation::List_strategy = st.builds(
    documentation::List,
)
Text_strategy = st.builds(
    Text,
)
documentation::Code_strategy = st.builds(
    documentation::Code,
)
documentation::HtmlCode_strategy = st.builds(
    documentation::HtmlCode,
)
documentation::Reference_strategy = st.builds(
    documentation::Reference,
    referredLabel=
        safe_text
)
documentation::Line_strategy = st.builds(
    documentation::Line,
)
documentation::Fragment_strategy = st.builds(
    documentation::Fragment,
)
documentation::TermEntry_strategy = st.builds(
    documentation::TermEntry,
    description=
        safe_text
)
documentation::Section_strategy = st.builds(
    documentation::Section,
)
documentation::Documentation_strategy = st.builds(
    documentation::Documentation,
    title=
        safe_text
)

@given(instance=documentation::TextContainer_strategy)
@settings(max_examples=50)
def test_documentation::textcontainer_instantiation(instance):
    assert isinstance(instance, documentation::TextContainer)

@given(instance=documentation::Width_strategy)
@settings(max_examples=50)
def test_documentation::width_instantiation(instance):
    assert isinstance(instance, documentation::Width)

@given(instance=documentation::Width_strategy)
def test_documentation::width_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=documentation::Width_strategy)
def test_documentation::width_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=documentation::Width_strategy)
def test_documentation::width_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=documentation::Width_strategy)
def test_documentation::width_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=documentation::TableRow_strategy)
@settings(max_examples=50)
def test_documentation::tablerow_instantiation(instance):
    assert isinstance(instance, documentation::TableRow)

@given(instance=documentation::TableHeader_strategy)
@settings(max_examples=50)
def test_documentation::tableheader_instantiation(instance):
    assert isinstance(instance, documentation::TableHeader)

@given(instance=documentation::TableCell_strategy)
@settings(max_examples=50)
def test_documentation::tablecell_instantiation(instance):
    assert isinstance(instance, documentation::TableCell)

@given(instance=documentation::TableCell_strategy)
def test_documentation::tablecell_span_type(instance):
    assert isinstance(instance.span, int)


@given(instance=documentation::TableCell_strategy)
def test_documentation::tablecell_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=documentation::TableCell_strategy)
def test_documentation::tablecell_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=documentation::TableCell_strategy)
def test_documentation::tablecell_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=documentation::ListItem_strategy)
@settings(max_examples=50)
def test_documentation::listitem_instantiation(instance):
    assert isinstance(instance, documentation::ListItem)

@given(instance=documentation::ListItem_strategy)
def test_documentation::listitem_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=documentation::ListItem_strategy)
def test_documentation::listitem_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=documentation::NamedElement_strategy)
@settings(max_examples=50)
def test_documentation::namedelement_instantiation(instance):
    assert isinstance(instance, documentation::NamedElement)

@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=documentation::NamedElement_strategy)
def test_documentation::namedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=TextContainer_strategy)
@settings(max_examples=50)
def test_textcontainer_instantiation(instance):
    assert isinstance(instance, TextContainer)

@given(instance=documentation::FragmentContainer_strategy)
@settings(max_examples=50)
def test_documentation::fragmentcontainer_instantiation(instance):
    assert isinstance(instance, documentation::FragmentContainer)

@given(instance=Fragment_strategy)
@settings(max_examples=50)
def test_fragment_instantiation(instance):
    assert isinstance(instance, Fragment)

@given(instance=documentation::Text_strategy)
@settings(max_examples=50)
def test_documentation::text_instantiation(instance):
    assert isinstance(instance, documentation::Text)

@given(instance=documentation::Text_strategy)
def test_documentation::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=documentation::Text_strategy)
def test_documentation::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=documentation::Paragraph_strategy)
@settings(max_examples=50)
def test_documentation::paragraph_instantiation(instance):
    assert isinstance(instance, documentation::Paragraph)

@given(instance=documentation::PageBreak_strategy)
@settings(max_examples=50)
def test_documentation::pagebreak_instantiation(instance):
    assert isinstance(instance, documentation::PageBreak)

@given(instance=documentation::Table_strategy)
@settings(max_examples=50)
def test_documentation::table_instantiation(instance):
    assert isinstance(instance, documentation::Table)

@given(instance=documentation::Listing_strategy)
@settings(max_examples=50)
def test_documentation::listing_instantiation(instance):
    assert isinstance(instance, documentation::Listing)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=documentation::Image_strategy)
@settings(max_examples=50)
def test_documentation::image_instantiation(instance):
    assert isinstance(instance, documentation::Image)

@given(instance=documentation::Image_strategy)
def test_documentation::image_contextClassName_type(instance):
    assert isinstance(instance.contextClassName, str)


@given(instance=documentation::Image_strategy)
def test_documentation::image_contextClassName_setter(instance):
    original = instance.contextClassName
    instance.contextClassName = original
    assert instance.contextClassName == original

@given(instance=documentation::Image_strategy)
def test_documentation::image_resource_type(instance):
    assert isinstance(instance.resource, str)


@given(instance=documentation::Image_strategy)
def test_documentation::image_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=documentation::Image_strategy)
def test_documentation::image_originalSource_type(instance):
    assert isinstance(instance.originalSource, str)


@given(instance=documentation::Image_strategy)
def test_documentation::image_originalSource_setter(instance):
    original = instance.originalSource
    instance.originalSource = original
    assert instance.originalSource == original

@given(instance=documentation::Link_strategy)
@settings(max_examples=50)
def test_documentation::link_instantiation(instance):
    assert isinstance(instance, documentation::Link)

@given(instance=documentation::Link_strategy)
def test_documentation::link_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=documentation::Link_strategy)
def test_documentation::link_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=documentation::XML_strategy)
@settings(max_examples=50)
def test_documentation::xml_instantiation(instance):
    assert isinstance(instance, documentation::XML)

@given(instance=documentation::XML_strategy)
def test_documentation::xml_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=documentation::XML_strategy)
def test_documentation::xml_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=documentation::XML_strategy)
def test_documentation::xml_contextClassName_type(instance):
    assert isinstance(instance.contextClassName, str)


@given(instance=documentation::XML_strategy)
def test_documentation::xml_contextClassName_setter(instance):
    original = instance.contextClassName
    instance.contextClassName = original
    assert instance.contextClassName == original

@given(instance=documentation::XML_strategy)
def test_documentation::xml_resource_type(instance):
    assert isinstance(instance.resource, str)


@given(instance=documentation::XML_strategy)
def test_documentation::xml_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=FragmentContainer_strategy)
@settings(max_examples=50)
def test_fragmentcontainer_instantiation(instance):
    assert isinstance(instance, FragmentContainer)

@given(instance=documentation::Subsection_strategy)
@settings(max_examples=50)
def test_documentation::subsection_instantiation(instance):
    assert isinstance(instance, documentation::Subsection)

@given(instance=documentation::Subsubsection_strategy)
@settings(max_examples=50)
def test_documentation::subsubsection_instantiation(instance):
    assert isinstance(instance, documentation::Subsubsection)

@given(instance=documentation::List_strategy)
@settings(max_examples=50)
def test_documentation::list_instantiation(instance):
    assert isinstance(instance, documentation::List)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=documentation::Code_strategy)
@settings(max_examples=50)
def test_documentation::code_instantiation(instance):
    assert isinstance(instance, documentation::Code)

@given(instance=documentation::HtmlCode_strategy)
@settings(max_examples=50)
def test_documentation::htmlcode_instantiation(instance):
    assert isinstance(instance, documentation::HtmlCode)

@given(instance=documentation::Reference_strategy)
@settings(max_examples=50)
def test_documentation::reference_instantiation(instance):
    assert isinstance(instance, documentation::Reference)

@given(instance=documentation::Reference_strategy)
def test_documentation::reference_referredLabel_type(instance):
    assert isinstance(instance.referredLabel, str)


@given(instance=documentation::Reference_strategy)
def test_documentation::reference_referredLabel_setter(instance):
    original = instance.referredLabel
    instance.referredLabel = original
    assert instance.referredLabel == original

@given(instance=documentation::Line_strategy)
@settings(max_examples=50)
def test_documentation::line_instantiation(instance):
    assert isinstance(instance, documentation::Line)

@given(instance=documentation::Fragment_strategy)
@settings(max_examples=50)
def test_documentation::fragment_instantiation(instance):
    assert isinstance(instance, documentation::Fragment)

@given(instance=documentation::TermEntry_strategy)
@settings(max_examples=50)
def test_documentation::termentry_instantiation(instance):
    assert isinstance(instance, documentation::TermEntry)

@given(instance=documentation::TermEntry_strategy)
def test_documentation::termentry_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=documentation::TermEntry_strategy)
def test_documentation::termentry_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=documentation::Section_strategy)
@settings(max_examples=50)
def test_documentation::section_instantiation(instance):
    assert isinstance(instance, documentation::Section)

@given(instance=documentation::Documentation_strategy)
@settings(max_examples=50)
def test_documentation::documentation_instantiation(instance):
    assert isinstance(instance, documentation::Documentation)

@given(instance=documentation::Documentation_strategy)
def test_documentation::documentation_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=documentation::Documentation_strategy)
def test_documentation::documentation_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
