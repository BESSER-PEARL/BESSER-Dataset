import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BlockLevelComponent,
    InlineComponent,
    ric::ObjectComponent,
    ric::CheckGroup,
    ric::RadioGroup,
    ric::SelectItem,
    ric::InlineComponent,
    ric::BlockLevelComponent,
    ric::Script,
    FormControl,
    ric::Radio,
    ric::InputFile,
    ric::TextArea,
    ric::Checkbox,
    ric::Select,
    ric::TextField,
    ric::Button,
    EventComponent,
    ric::Document,
    ClassifiableComponent,
    IdentifiableComponent,
    ric::LineBreak,
    ric::Heading,
    ric::Fieldset,
    ric::Div,
    ric::Span,
    ric::List,
    ric::RichWidget,
    ric::Label,
    ric::PhraseElement,
    ric::Form,
    ric::FormControl,
    ric::Event,
    ric::EventComponent,
    ric::ClassifiableComponent,
    ric::IdentifiableComponent,
    ric::ListItem,
    List,
    ric::UnorderedList,
    ric::OrderedList,
    ric::ContentRegion,
    ric::LinkGroup,
    ric::Logo,
    ric::FooterRegion,
    ric::SearchRegion,
    ric::ContextualNavigationRegion,
    ric::NavigationRegion,
    ric::HeaderRegion,
    ric::Portal,
    FormControlConstraint,
    ric::ValidDateConstraint,
    ric::NumberValueConstraint,
    ric::ValueConstraint,
    ric::RequiredFieldConstraint,
    ric::FormControlConstraint,
    TextField,
    ric::MessageDialogButton,
    ric::Section,
    ric::Tab,
    RichWidget,
    ric::Datepicker,
    ric::MessageDialog,
    ric::AccordionPanel,
    ric::TabbedPanel,
    ObjectComponent,
    ric::Image,
    ric::Link,
    ric::Paragraph,
    MessageDialogEvent,
    DateFormat,
    FieldSetLegendAlign,
    LogicalOperator,
    Align,
    MatchingOperator,
    UnorderedListType,
    Orientation,
    EventType,
    Locale,
    PhraseElementType,
    OrderedListType,
    ScriptType,
    Extension,
    SubmitFormMethod,
    ObjectAlign,
    ButtonType,
    HeadingLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blocklevelcomponent_is_not_abstract():
    assert not inspect.isabstract(BlockLevelComponent)


def test_blocklevelcomponent_constructor_exists():
    assert callable(BlockLevelComponent.__init__)


def test_blocklevelcomponent_constructor_args():
    sig = inspect.signature(BlockLevelComponent.__init__)
    params = list(sig.parameters.keys())



def test_inlinecomponent_is_not_abstract():
    assert not inspect.isabstract(InlineComponent)


def test_inlinecomponent_constructor_exists():
    assert callable(InlineComponent.__init__)


def test_inlinecomponent_constructor_args():
    sig = inspect.signature(InlineComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::objectcomponent_is_not_abstract():
    assert not inspect.isabstract(ric::ObjectComponent)


def test_ric::objectcomponent_constructor_exists():
    assert callable(ric::ObjectComponent.__init__)


def test_ric::objectcomponent_constructor_args():
    sig = inspect.signature(ric::ObjectComponent.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "border" in params, "Missing parameter 'border'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_ric::objectcomponent_has_align():
    assert hasattr(ric::ObjectComponent, "align")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_ric::objectcomponent_has_hspace():
    assert hasattr(ric::ObjectComponent, "hspace")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_ric::objectcomponent_has_border():
    assert hasattr(ric::ObjectComponent, "border")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_ric::objectcomponent_has_vspace():
    assert hasattr(ric::ObjectComponent, "vspace")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_ric::objectcomponent_has_width():
    assert hasattr(ric::ObjectComponent, "width")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ric::objectcomponent_has_height():
    assert hasattr(ric::ObjectComponent, "height")
    descriptor = None
    for klass in ric::ObjectComponent.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_ric::checkgroup_is_not_abstract():
    assert not inspect.isabstract(ric::CheckGroup)


def test_ric::checkgroup_constructor_exists():
    assert callable(ric::CheckGroup.__init__)


def test_ric::checkgroup_constructor_args():
    sig = inspect.signature(ric::CheckGroup.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric::checkgroup_has_orientation():
    assert hasattr(ric::CheckGroup, "orientation")
    descriptor = None
    for klass in ric::CheckGroup.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric::radiogroup_is_not_abstract():
    assert not inspect.isabstract(ric::RadioGroup)


def test_ric::radiogroup_constructor_exists():
    assert callable(ric::RadioGroup.__init__)


def test_ric::radiogroup_constructor_args():
    sig = inspect.signature(ric::RadioGroup.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric::radiogroup_has_orientation():
    assert hasattr(ric::RadioGroup, "orientation")
    descriptor = None
    for klass in ric::RadioGroup.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric::selectitem_is_not_abstract():
    assert not inspect.isabstract(ric::SelectItem)


def test_ric::selectitem_constructor_exists():
    assert callable(ric::SelectItem.__init__)


def test_ric::selectitem_constructor_args():
    sig = inspect.signature(ric::SelectItem.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "itemLabel" in params, "Missing parameter 'itemLabel'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_ric::selectitem_has_value():
    assert hasattr(ric::SelectItem, "value")
    descriptor = None
    for klass in ric::SelectItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ric::selectitem_has_itemLabel():
    assert hasattr(ric::SelectItem, "itemLabel")
    descriptor = None
    for klass in ric::SelectItem.__mro__:
        if "itemLabel" in klass.__dict__:
            descriptor = klass.__dict__["itemLabel"]
            break
    assert isinstance(descriptor, property)

def test_ric::selectitem_has_selected():
    assert hasattr(ric::SelectItem, "selected")
    descriptor = None
    for klass in ric::SelectItem.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_ric::inlinecomponent_is_not_abstract():
    assert not inspect.isabstract(ric::InlineComponent)


def test_ric::inlinecomponent_constructor_exists():
    assert callable(ric::InlineComponent.__init__)


def test_ric::inlinecomponent_constructor_args():
    sig = inspect.signature(ric::InlineComponent.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ric::inlinecomponent_has_text():
    assert hasattr(ric::InlineComponent, "text")
    descriptor = None
    for klass in ric::InlineComponent.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ric::blocklevelcomponent_is_not_abstract():
    assert not inspect.isabstract(ric::BlockLevelComponent)


def test_ric::blocklevelcomponent_constructor_exists():
    assert callable(ric::BlockLevelComponent.__init__)


def test_ric::blocklevelcomponent_constructor_args():
    sig = inspect.signature(ric::BlockLevelComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::script_is_not_abstract():
    assert not inspect.isabstract(ric::Script)


def test_ric::script_constructor_exists():
    assert callable(ric::Script.__init__)


def test_ric::script_constructor_args():
    sig = inspect.signature(ric::Script.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "type" in params, "Missing parameter 'type'"

def test_ric::script_has_name():
    assert hasattr(ric::Script, "name")
    descriptor = None
    for klass in ric::Script.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric::script_has_implementation():
    assert hasattr(ric::Script, "implementation")
    descriptor = None
    for klass in ric::Script.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_ric::script_has_type():
    assert hasattr(ric::Script, "type")
    descriptor = None
    for klass in ric::Script.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_formcontrol_is_not_abstract():
    assert not inspect.isabstract(FormControl)


def test_formcontrol_constructor_exists():
    assert callable(FormControl.__init__)


def test_formcontrol_constructor_args():
    sig = inspect.signature(FormControl.__init__)
    params = list(sig.parameters.keys())



def test_ric::radio_is_not_abstract():
    assert not inspect.isabstract(ric::Radio)


def test_ric::radio_constructor_exists():
    assert callable(ric::Radio.__init__)


def test_ric::radio_constructor_args():
    sig = inspect.signature(ric::Radio.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_ric::radio_has_checked():
    assert hasattr(ric::Radio, "checked")
    descriptor = None
    for klass in ric::Radio.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_ric::inputfile_is_not_abstract():
    assert not inspect.isabstract(ric::InputFile)


def test_ric::inputfile_constructor_exists():
    assert callable(ric::InputFile.__init__)


def test_ric::inputfile_constructor_args():
    sig = inspect.signature(ric::InputFile.__init__)
    params = list(sig.parameters.keys())
    assert "charWidth" in params, "Missing parameter 'charWidth'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "maxChars" in params, "Missing parameter 'maxChars'"

def test_ric::inputfile_has_charWidth():
    assert hasattr(ric::InputFile, "charWidth")
    descriptor = None
    for klass in ric::InputFile.__mro__:
        if "charWidth" in klass.__dict__:
            descriptor = klass.__dict__["charWidth"]
            break
    assert isinstance(descriptor, property)

def test_ric::inputfile_has_readonly():
    assert hasattr(ric::InputFile, "readonly")
    descriptor = None
    for klass in ric::InputFile.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_ric::inputfile_has_maxChars():
    assert hasattr(ric::InputFile, "maxChars")
    descriptor = None
    for klass in ric::InputFile.__mro__:
        if "maxChars" in klass.__dict__:
            descriptor = klass.__dict__["maxChars"]
            break
    assert isinstance(descriptor, property)



def test_ric::textarea_is_not_abstract():
    assert not inspect.isabstract(ric::TextArea)


def test_ric::textarea_constructor_exists():
    assert callable(ric::TextArea.__init__)


def test_ric::textarea_constructor_args():
    sig = inspect.signature(ric::TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "cols" in params, "Missing parameter 'cols'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "rols" in params, "Missing parameter 'rols'"

def test_ric::textarea_has_cols():
    assert hasattr(ric::TextArea, "cols")
    descriptor = None
    for klass in ric::TextArea.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_ric::textarea_has_readonly():
    assert hasattr(ric::TextArea, "readonly")
    descriptor = None
    for klass in ric::TextArea.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_ric::textarea_has_rols():
    assert hasattr(ric::TextArea, "rols")
    descriptor = None
    for klass in ric::TextArea.__mro__:
        if "rols" in klass.__dict__:
            descriptor = klass.__dict__["rols"]
            break
    assert isinstance(descriptor, property)



def test_ric::checkbox_is_not_abstract():
    assert not inspect.isabstract(ric::Checkbox)


def test_ric::checkbox_constructor_exists():
    assert callable(ric::Checkbox.__init__)


def test_ric::checkbox_constructor_args():
    sig = inspect.signature(ric::Checkbox.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_ric::checkbox_has_checked():
    assert hasattr(ric::Checkbox, "checked")
    descriptor = None
    for klass in ric::Checkbox.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_ric::select_is_not_abstract():
    assert not inspect.isabstract(ric::Select)


def test_ric::select_constructor_exists():
    assert callable(ric::Select.__init__)


def test_ric::select_constructor_args():
    sig = inspect.signature(ric::Select.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "size" in params, "Missing parameter 'size'"

def test_ric::select_has_multiple():
    assert hasattr(ric::Select, "multiple")
    descriptor = None
    for klass in ric::Select.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_ric::select_has_size():
    assert hasattr(ric::Select, "size")
    descriptor = None
    for klass in ric::Select.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ric::textfield_is_not_abstract():
    assert not inspect.isabstract(ric::TextField)


def test_ric::textfield_constructor_exists():
    assert callable(ric::TextField.__init__)


def test_ric::textfield_constructor_args():
    sig = inspect.signature(ric::TextField.__init__)
    params = list(sig.parameters.keys())
    assert "charWidth" in params, "Missing parameter 'charWidth'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "maxChars" in params, "Missing parameter 'maxChars'"
    assert "password" in params, "Missing parameter 'password'"

def test_ric::textfield_has_charWidth():
    assert hasattr(ric::TextField, "charWidth")
    descriptor = None
    for klass in ric::TextField.__mro__:
        if "charWidth" in klass.__dict__:
            descriptor = klass.__dict__["charWidth"]
            break
    assert isinstance(descriptor, property)

def test_ric::textfield_has_readonly():
    assert hasattr(ric::TextField, "readonly")
    descriptor = None
    for klass in ric::TextField.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_ric::textfield_has_maxChars():
    assert hasattr(ric::TextField, "maxChars")
    descriptor = None
    for klass in ric::TextField.__mro__:
        if "maxChars" in klass.__dict__:
            descriptor = klass.__dict__["maxChars"]
            break
    assert isinstance(descriptor, property)

def test_ric::textfield_has_password():
    assert hasattr(ric::TextField, "password")
    descriptor = None
    for klass in ric::TextField.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_ric::button_is_not_abstract():
    assert not inspect.isabstract(ric::Button)


def test_ric::button_constructor_exists():
    assert callable(ric::Button.__init__)


def test_ric::button_constructor_args():
    sig = inspect.signature(ric::Button.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "type" in params, "Missing parameter 'type'"
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_ric::button_has_image():
    assert hasattr(ric::Button, "image")
    descriptor = None
    for klass in ric::Button.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_ric::button_has_type():
    assert hasattr(ric::Button, "type")
    descriptor = None
    for klass in ric::Button.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ric::button_has_disabled():
    assert hasattr(ric::Button, "disabled")
    descriptor = None
    for klass in ric::Button.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_eventcomponent_is_not_abstract():
    assert not inspect.isabstract(EventComponent)


def test_eventcomponent_constructor_exists():
    assert callable(EventComponent.__init__)


def test_eventcomponent_constructor_args():
    sig = inspect.signature(EventComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::document_is_not_abstract():
    assert not inspect.isabstract(ric::Document)


def test_ric::document_constructor_exists():
    assert callable(ric::Document.__init__)


def test_ric::document_constructor_args():
    sig = inspect.signature(ric::Document.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "title" in params, "Missing parameter 'title'"
    assert "index" in params, "Missing parameter 'index'"

def test_ric::document_has_fileName():
    assert hasattr(ric::Document, "fileName")
    descriptor = None
    for klass in ric::Document.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_ric::document_has_title():
    assert hasattr(ric::Document, "title")
    descriptor = None
    for klass in ric::Document.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_ric::document_has_index():
    assert hasattr(ric::Document, "index")
    descriptor = None
    for klass in ric::Document.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_classifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(ClassifiableComponent)


def test_classifiablecomponent_constructor_exists():
    assert callable(ClassifiableComponent.__init__)


def test_classifiablecomponent_constructor_args():
    sig = inspect.signature(ClassifiableComponent.__init__)
    params = list(sig.parameters.keys())



def test_identifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(IdentifiableComponent)


def test_identifiablecomponent_constructor_exists():
    assert callable(IdentifiableComponent.__init__)


def test_identifiablecomponent_constructor_args():
    sig = inspect.signature(IdentifiableComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::linebreak_is_not_abstract():
    assert not inspect.isabstract(ric::LineBreak)


def test_ric::linebreak_constructor_exists():
    assert callable(ric::LineBreak.__init__)


def test_ric::linebreak_constructor_args():
    sig = inspect.signature(ric::LineBreak.__init__)
    params = list(sig.parameters.keys())



def test_ric::heading_is_not_abstract():
    assert not inspect.isabstract(ric::Heading)


def test_ric::heading_constructor_exists():
    assert callable(ric::Heading.__init__)


def test_ric::heading_constructor_args():
    sig = inspect.signature(ric::Heading.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_ric::heading_has_level():
    assert hasattr(ric::Heading, "level")
    descriptor = None
    for klass in ric::Heading.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_ric::fieldset_is_not_abstract():
    assert not inspect.isabstract(ric::Fieldset)


def test_ric::fieldset_constructor_exists():
    assert callable(ric::Fieldset.__init__)


def test_ric::fieldset_constructor_args():
    sig = inspect.signature(ric::Fieldset.__init__)
    params = list(sig.parameters.keys())
    assert "legendFormat" in params, "Missing parameter 'legendFormat'"
    assert "legend" in params, "Missing parameter 'legend'"
    assert "legendAlign" in params, "Missing parameter 'legendAlign'"

def test_ric::fieldset_has_legendFormat():
    assert hasattr(ric::Fieldset, "legendFormat")
    descriptor = None
    for klass in ric::Fieldset.__mro__:
        if "legendFormat" in klass.__dict__:
            descriptor = klass.__dict__["legendFormat"]
            break
    assert isinstance(descriptor, property)

def test_ric::fieldset_has_legend():
    assert hasattr(ric::Fieldset, "legend")
    descriptor = None
    for klass in ric::Fieldset.__mro__:
        if "legend" in klass.__dict__:
            descriptor = klass.__dict__["legend"]
            break
    assert isinstance(descriptor, property)

def test_ric::fieldset_has_legendAlign():
    assert hasattr(ric::Fieldset, "legendAlign")
    descriptor = None
    for klass in ric::Fieldset.__mro__:
        if "legendAlign" in klass.__dict__:
            descriptor = klass.__dict__["legendAlign"]
            break
    assert isinstance(descriptor, property)



def test_ric::div_is_not_abstract():
    assert not inspect.isabstract(ric::Div)


def test_ric::div_constructor_exists():
    assert callable(ric::Div.__init__)


def test_ric::div_constructor_args():
    sig = inspect.signature(ric::Div.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric::div_has_align():
    assert hasattr(ric::Div, "align")
    descriptor = None
    for klass in ric::Div.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ric::span_is_not_abstract():
    assert not inspect.isabstract(ric::Span)


def test_ric::span_constructor_exists():
    assert callable(ric::Span.__init__)


def test_ric::span_constructor_args():
    sig = inspect.signature(ric::Span.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric::span_has_align():
    assert hasattr(ric::Span, "align")
    descriptor = None
    for klass in ric::Span.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ric::list_is_not_abstract():
    assert not inspect.isabstract(ric::List)


def test_ric::list_constructor_exists():
    assert callable(ric::List.__init__)


def test_ric::list_constructor_args():
    sig = inspect.signature(ric::List.__init__)
    params = list(sig.parameters.keys())



def test_ric::richwidget_is_not_abstract():
    assert not inspect.isabstract(ric::RichWidget)


def test_ric::richwidget_constructor_exists():
    assert callable(ric::RichWidget.__init__)


def test_ric::richwidget_constructor_args():
    sig = inspect.signature(ric::RichWidget.__init__)
    params = list(sig.parameters.keys())



def test_ric::label_is_not_abstract():
    assert not inspect.isabstract(ric::Label)


def test_ric::label_constructor_exists():
    assert callable(ric::Label.__init__)


def test_ric::label_constructor_args():
    sig = inspect.signature(ric::Label.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "text" in params, "Missing parameter 'text'"

def test_ric::label_has_format():
    assert hasattr(ric::Label, "format")
    descriptor = None
    for klass in ric::Label.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_ric::label_has_text():
    assert hasattr(ric::Label, "text")
    descriptor = None
    for klass in ric::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ric::phraseelement_is_not_abstract():
    assert not inspect.isabstract(ric::PhraseElement)


def test_ric::phraseelement_constructor_exists():
    assert callable(ric::PhraseElement.__init__)


def test_ric::phraseelement_constructor_args():
    sig = inspect.signature(ric::PhraseElement.__init__)
    params = list(sig.parameters.keys())
    assert "phraseType" in params, "Missing parameter 'phraseType'"
    assert "title" in params, "Missing parameter 'title'"

def test_ric::phraseelement_has_phraseType():
    assert hasattr(ric::PhraseElement, "phraseType")
    descriptor = None
    for klass in ric::PhraseElement.__mro__:
        if "phraseType" in klass.__dict__:
            descriptor = klass.__dict__["phraseType"]
            break
    assert isinstance(descriptor, property)

def test_ric::phraseelement_has_title():
    assert hasattr(ric::PhraseElement, "title")
    descriptor = None
    for klass in ric::PhraseElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric::form_is_not_abstract():
    assert not inspect.isabstract(ric::Form)


def test_ric::form_constructor_exists():
    assert callable(ric::Form.__init__)


def test_ric::form_constructor_args():
    sig = inspect.signature(ric::Form.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"

def test_ric::form_has_name():
    assert hasattr(ric::Form, "name")
    descriptor = None
    for klass in ric::Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric::form_has_method():
    assert hasattr(ric::Form, "method")
    descriptor = None
    for klass in ric::Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_ric::formcontrol_is_not_abstract():
    assert not inspect.isabstract(ric::FormControl)


def test_ric::formcontrol_constructor_exists():
    assert callable(ric::FormControl.__init__)


def test_ric::formcontrol_constructor_args():
    sig = inspect.signature(ric::FormControl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_ric::formcontrol_has_name():
    assert hasattr(ric::FormControl, "name")
    descriptor = None
    for klass in ric::FormControl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric::formcontrol_has_value():
    assert hasattr(ric::FormControl, "value")
    descriptor = None
    for klass in ric::FormControl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ric::event_is_not_abstract():
    assert not inspect.isabstract(ric::Event)


def test_ric::event_constructor_exists():
    assert callable(ric::Event.__init__)


def test_ric::event_constructor_args():
    sig = inspect.signature(ric::Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric::event_has_type():
    assert hasattr(ric::Event, "type")
    descriptor = None
    for klass in ric::Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric::eventcomponent_is_not_abstract():
    assert not inspect.isabstract(ric::EventComponent)


def test_ric::eventcomponent_constructor_exists():
    assert callable(ric::EventComponent.__init__)


def test_ric::eventcomponent_constructor_args():
    sig = inspect.signature(ric::EventComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::classifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(ric::ClassifiableComponent)


def test_ric::classifiablecomponent_constructor_exists():
    assert callable(ric::ClassifiableComponent.__init__)


def test_ric::classifiablecomponent_constructor_args():
    sig = inspect.signature(ric::ClassifiableComponent.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_ric::classifiablecomponent_has_class_():
    assert hasattr(ric::ClassifiableComponent, "class_")
    descriptor = None
    for klass in ric::ClassifiableComponent.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_ric::identifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(ric::IdentifiableComponent)


def test_ric::identifiablecomponent_constructor_exists():
    assert callable(ric::IdentifiableComponent.__init__)


def test_ric::identifiablecomponent_constructor_args():
    sig = inspect.signature(ric::IdentifiableComponent.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ric::identifiablecomponent_has_id():
    assert hasattr(ric::IdentifiableComponent, "id")
    descriptor = None
    for klass in ric::IdentifiableComponent.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ric::listitem_is_not_abstract():
    assert not inspect.isabstract(ric::ListItem)


def test_ric::listitem_constructor_exists():
    assert callable(ric::ListItem.__init__)


def test_ric::listitem_constructor_args():
    sig = inspect.signature(ric::ListItem.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "text" in params, "Missing parameter 'text'"

def test_ric::listitem_has_format():
    assert hasattr(ric::ListItem, "format")
    descriptor = None
    for klass in ric::ListItem.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_ric::listitem_has_text():
    assert hasattr(ric::ListItem, "text")
    descriptor = None
    for klass in ric::ListItem.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_list_is_not_abstract():
    assert not inspect.isabstract(List)


def test_list_constructor_exists():
    assert callable(List.__init__)


def test_list_constructor_args():
    sig = inspect.signature(List.__init__)
    params = list(sig.parameters.keys())



def test_ric::unorderedlist_is_not_abstract():
    assert not inspect.isabstract(ric::UnorderedList)


def test_ric::unorderedlist_constructor_exists():
    assert callable(ric::UnorderedList.__init__)


def test_ric::unorderedlist_constructor_args():
    sig = inspect.signature(ric::UnorderedList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric::unorderedlist_has_type():
    assert hasattr(ric::UnorderedList, "type")
    descriptor = None
    for klass in ric::UnorderedList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric::orderedlist_is_not_abstract():
    assert not inspect.isabstract(ric::OrderedList)


def test_ric::orderedlist_constructor_exists():
    assert callable(ric::OrderedList.__init__)


def test_ric::orderedlist_constructor_args():
    sig = inspect.signature(ric::OrderedList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric::orderedlist_has_type():
    assert hasattr(ric::OrderedList, "type")
    descriptor = None
    for klass in ric::OrderedList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric::contentregion_is_not_abstract():
    assert not inspect.isabstract(ric::ContentRegion)


def test_ric::contentregion_constructor_exists():
    assert callable(ric::ContentRegion.__init__)


def test_ric::contentregion_constructor_args():
    sig = inspect.signature(ric::ContentRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric::linkgroup_is_not_abstract():
    assert not inspect.isabstract(ric::LinkGroup)


def test_ric::linkgroup_constructor_exists():
    assert callable(ric::LinkGroup.__init__)


def test_ric::linkgroup_constructor_args():
    sig = inspect.signature(ric::LinkGroup.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric::linkgroup_has_title():
    assert hasattr(ric::LinkGroup, "title")
    descriptor = None
    for klass in ric::LinkGroup.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric::logo_is_not_abstract():
    assert not inspect.isabstract(ric::Logo)


def test_ric::logo_constructor_exists():
    assert callable(ric::Logo.__init__)


def test_ric::logo_constructor_args():
    sig = inspect.signature(ric::Logo.__init__)
    params = list(sig.parameters.keys())



def test_ric::footerregion_is_not_abstract():
    assert not inspect.isabstract(ric::FooterRegion)


def test_ric::footerregion_constructor_exists():
    assert callable(ric::FooterRegion.__init__)


def test_ric::footerregion_constructor_args():
    sig = inspect.signature(ric::FooterRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric::searchregion_is_not_abstract():
    assert not inspect.isabstract(ric::SearchRegion)


def test_ric::searchregion_constructor_exists():
    assert callable(ric::SearchRegion.__init__)


def test_ric::searchregion_constructor_args():
    sig = inspect.signature(ric::SearchRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric::contextualnavigationregion_is_not_abstract():
    assert not inspect.isabstract(ric::ContextualNavigationRegion)


def test_ric::contextualnavigationregion_constructor_exists():
    assert callable(ric::ContextualNavigationRegion.__init__)


def test_ric::contextualnavigationregion_constructor_args():
    sig = inspect.signature(ric::ContextualNavigationRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric::navigationregion_is_not_abstract():
    assert not inspect.isabstract(ric::NavigationRegion)


def test_ric::navigationregion_constructor_exists():
    assert callable(ric::NavigationRegion.__init__)


def test_ric::navigationregion_constructor_args():
    sig = inspect.signature(ric::NavigationRegion.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric::navigationregion_has_orientation():
    assert hasattr(ric::NavigationRegion, "orientation")
    descriptor = None
    for klass in ric::NavigationRegion.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric::headerregion_is_not_abstract():
    assert not inspect.isabstract(ric::HeaderRegion)


def test_ric::headerregion_constructor_exists():
    assert callable(ric::HeaderRegion.__init__)


def test_ric::headerregion_constructor_args():
    sig = inspect.signature(ric::HeaderRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric::portal_is_not_abstract():
    assert not inspect.isabstract(ric::Portal)


def test_ric::portal_constructor_exists():
    assert callable(ric::Portal.__init__)


def test_ric::portal_constructor_args():
    sig = inspect.signature(ric::Portal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "documentsExtension" in params, "Missing parameter 'documentsExtension'"

def test_ric::portal_has_name():
    assert hasattr(ric::Portal, "name")
    descriptor = None
    for klass in ric::Portal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric::portal_has_documentsExtension():
    assert hasattr(ric::Portal, "documentsExtension")
    descriptor = None
    for klass in ric::Portal.__mro__:
        if "documentsExtension" in klass.__dict__:
            descriptor = klass.__dict__["documentsExtension"]
            break
    assert isinstance(descriptor, property)



def test_formcontrolconstraint_is_not_abstract():
    assert not inspect.isabstract(FormControlConstraint)


def test_formcontrolconstraint_constructor_exists():
    assert callable(FormControlConstraint.__init__)


def test_formcontrolconstraint_constructor_args():
    sig = inspect.signature(FormControlConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric::validdateconstraint_is_not_abstract():
    assert not inspect.isabstract(ric::ValidDateConstraint)


def test_ric::validdateconstraint_constructor_exists():
    assert callable(ric::ValidDateConstraint.__init__)


def test_ric::validdateconstraint_constructor_args():
    sig = inspect.signature(ric::ValidDateConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_ric::validdateconstraint_has_dateFormat():
    assert hasattr(ric::ValidDateConstraint, "dateFormat")
    descriptor = None
    for klass in ric::ValidDateConstraint.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_ric::numbervalueconstraint_is_not_abstract():
    assert not inspect.isabstract(ric::NumberValueConstraint)


def test_ric::numbervalueconstraint_constructor_exists():
    assert callable(ric::NumberValueConstraint.__init__)


def test_ric::numbervalueconstraint_constructor_args():
    sig = inspect.signature(ric::NumberValueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric::valueconstraint_is_not_abstract():
    assert not inspect.isabstract(ric::ValueConstraint)


def test_ric::valueconstraint_constructor_exists():
    assert callable(ric::ValueConstraint.__init__)


def test_ric::valueconstraint_constructor_args():
    sig = inspect.signature(ric::ValueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"
    assert "matchingOperator" in params, "Missing parameter 'matchingOperator'"
    assert "matchingValue" in params, "Missing parameter 'matchingValue'"

def test_ric::valueconstraint_has_logicalOperator():
    assert hasattr(ric::ValueConstraint, "logicalOperator")
    descriptor = None
    for klass in ric::ValueConstraint.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)

def test_ric::valueconstraint_has_matchingOperator():
    assert hasattr(ric::ValueConstraint, "matchingOperator")
    descriptor = None
    for klass in ric::ValueConstraint.__mro__:
        if "matchingOperator" in klass.__dict__:
            descriptor = klass.__dict__["matchingOperator"]
            break
    assert isinstance(descriptor, property)

def test_ric::valueconstraint_has_matchingValue():
    assert hasattr(ric::ValueConstraint, "matchingValue")
    descriptor = None
    for klass in ric::ValueConstraint.__mro__:
        if "matchingValue" in klass.__dict__:
            descriptor = klass.__dict__["matchingValue"]
            break
    assert isinstance(descriptor, property)



def test_ric::requiredfieldconstraint_is_not_abstract():
    assert not inspect.isabstract(ric::RequiredFieldConstraint)


def test_ric::requiredfieldconstraint_constructor_exists():
    assert callable(ric::RequiredFieldConstraint.__init__)


def test_ric::requiredfieldconstraint_constructor_args():
    sig = inspect.signature(ric::RequiredFieldConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric::formcontrolconstraint_is_not_abstract():
    assert not inspect.isabstract(ric::FormControlConstraint)


def test_ric::formcontrolconstraint_constructor_exists():
    assert callable(ric::FormControlConstraint.__init__)


def test_ric::formcontrolconstraint_constructor_args():
    sig = inspect.signature(ric::FormControlConstraint.__init__)
    params = list(sig.parameters.keys())



def test_textfield_is_not_abstract():
    assert not inspect.isabstract(TextField)


def test_textfield_constructor_exists():
    assert callable(TextField.__init__)


def test_textfield_constructor_args():
    sig = inspect.signature(TextField.__init__)
    params = list(sig.parameters.keys())



def test_ric::messagedialogbutton_is_not_abstract():
    assert not inspect.isabstract(ric::MessageDialogButton)


def test_ric::messagedialogbutton_constructor_exists():
    assert callable(ric::MessageDialogButton.__init__)


def test_ric::messagedialogbutton_constructor_args():
    sig = inspect.signature(ric::MessageDialogButton.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "label" in params, "Missing parameter 'label'"

def test_ric::messagedialogbutton_has_event():
    assert hasattr(ric::MessageDialogButton, "event")
    descriptor = None
    for klass in ric::MessageDialogButton.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialogbutton_has_label():
    assert hasattr(ric::MessageDialogButton, "label")
    descriptor = None
    for klass in ric::MessageDialogButton.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_ric::section_is_not_abstract():
    assert not inspect.isabstract(ric::Section)


def test_ric::section_constructor_exists():
    assert callable(ric::Section.__init__)


def test_ric::section_constructor_args():
    sig = inspect.signature(ric::Section.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric::section_has_title():
    assert hasattr(ric::Section, "title")
    descriptor = None
    for klass in ric::Section.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric::tab_is_not_abstract():
    assert not inspect.isabstract(ric::Tab)


def test_ric::tab_constructor_exists():
    assert callable(ric::Tab.__init__)


def test_ric::tab_constructor_args():
    sig = inspect.signature(ric::Tab.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric::tab_has_title():
    assert hasattr(ric::Tab, "title")
    descriptor = None
    for klass in ric::Tab.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_richwidget_is_not_abstract():
    assert not inspect.isabstract(RichWidget)


def test_richwidget_constructor_exists():
    assert callable(RichWidget.__init__)


def test_richwidget_constructor_args():
    sig = inspect.signature(RichWidget.__init__)
    params = list(sig.parameters.keys())



def test_ric::datepicker_is_not_abstract():
    assert not inspect.isabstract(ric::Datepicker)


def test_ric::datepicker_constructor_exists():
    assert callable(ric::Datepicker.__init__)


def test_ric::datepicker_constructor_args():
    sig = inspect.signature(ric::Datepicker.__init__)
    params = list(sig.parameters.keys())
    assert "numberMonthsToShow" in params, "Missing parameter 'numberMonthsToShow'"
    assert "showButtonImage" in params, "Missing parameter 'showButtonImage'"
    assert "showButtonClosePanel" in params, "Missing parameter 'showButtonClosePanel'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"
    assert "showMonthMenu" in params, "Missing parameter 'showMonthMenu'"
    assert "showWeekOfYear" in params, "Missing parameter 'showWeekOfYear'"
    assert "showYearMenu" in params, "Missing parameter 'showYearMenu'"

def test_ric::datepicker_has_numberMonthsToShow():
    assert hasattr(ric::Datepicker, "numberMonthsToShow")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "numberMonthsToShow" in klass.__dict__:
            descriptor = klass.__dict__["numberMonthsToShow"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_showButtonImage():
    assert hasattr(ric::Datepicker, "showButtonImage")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "showButtonImage" in klass.__dict__:
            descriptor = klass.__dict__["showButtonImage"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_showButtonClosePanel():
    assert hasattr(ric::Datepicker, "showButtonClosePanel")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "showButtonClosePanel" in klass.__dict__:
            descriptor = klass.__dict__["showButtonClosePanel"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_locale():
    assert hasattr(ric::Datepicker, "locale")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_dateFormat():
    assert hasattr(ric::Datepicker, "dateFormat")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_showMonthMenu():
    assert hasattr(ric::Datepicker, "showMonthMenu")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "showMonthMenu" in klass.__dict__:
            descriptor = klass.__dict__["showMonthMenu"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_showWeekOfYear():
    assert hasattr(ric::Datepicker, "showWeekOfYear")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "showWeekOfYear" in klass.__dict__:
            descriptor = klass.__dict__["showWeekOfYear"]
            break
    assert isinstance(descriptor, property)

def test_ric::datepicker_has_showYearMenu():
    assert hasattr(ric::Datepicker, "showYearMenu")
    descriptor = None
    for klass in ric::Datepicker.__mro__:
        if "showYearMenu" in klass.__dict__:
            descriptor = klass.__dict__["showYearMenu"]
            break
    assert isinstance(descriptor, property)



def test_ric::messagedialog_is_not_abstract():
    assert not inspect.isabstract(ric::MessageDialog)


def test_ric::messagedialog_constructor_exists():
    assert callable(ric::MessageDialog.__init__)


def test_ric::messagedialog_constructor_args():
    sig = inspect.signature(ric::MessageDialog.__init__)
    params = list(sig.parameters.keys())
    assert "autoOpen" in params, "Missing parameter 'autoOpen'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "minWidthResize" in params, "Missing parameter 'minWidthResize'"
    assert "modal" in params, "Missing parameter 'modal'"
    assert "maxWidthResize" in params, "Missing parameter 'maxWidthResize'"
    assert "minHeightResize" in params, "Missing parameter 'minHeightResize'"
    assert "width" in params, "Missing parameter 'width'"
    assert "maxHeightResize" in params, "Missing parameter 'maxHeightResize'"
    assert "message" in params, "Missing parameter 'message'"
    assert "height" in params, "Missing parameter 'height'"
    assert "title" in params, "Missing parameter 'title'"

def test_ric::messagedialog_has_autoOpen():
    assert hasattr(ric::MessageDialog, "autoOpen")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "autoOpen" in klass.__dict__:
            descriptor = klass.__dict__["autoOpen"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_resizable():
    assert hasattr(ric::MessageDialog, "resizable")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_minWidthResize():
    assert hasattr(ric::MessageDialog, "minWidthResize")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "minWidthResize" in klass.__dict__:
            descriptor = klass.__dict__["minWidthResize"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_modal():
    assert hasattr(ric::MessageDialog, "modal")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "modal" in klass.__dict__:
            descriptor = klass.__dict__["modal"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_maxWidthResize():
    assert hasattr(ric::MessageDialog, "maxWidthResize")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "maxWidthResize" in klass.__dict__:
            descriptor = klass.__dict__["maxWidthResize"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_minHeightResize():
    assert hasattr(ric::MessageDialog, "minHeightResize")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "minHeightResize" in klass.__dict__:
            descriptor = klass.__dict__["minHeightResize"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_width():
    assert hasattr(ric::MessageDialog, "width")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_maxHeightResize():
    assert hasattr(ric::MessageDialog, "maxHeightResize")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "maxHeightResize" in klass.__dict__:
            descriptor = klass.__dict__["maxHeightResize"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_message():
    assert hasattr(ric::MessageDialog, "message")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_height():
    assert hasattr(ric::MessageDialog, "height")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_ric::messagedialog_has_title():
    assert hasattr(ric::MessageDialog, "title")
    descriptor = None
    for klass in ric::MessageDialog.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric::accordionpanel_is_not_abstract():
    assert not inspect.isabstract(ric::AccordionPanel)


def test_ric::accordionpanel_constructor_exists():
    assert callable(ric::AccordionPanel.__init__)


def test_ric::accordionpanel_constructor_args():
    sig = inspect.signature(ric::AccordionPanel.__init__)
    params = list(sig.parameters.keys())



def test_ric::tabbedpanel_is_not_abstract():
    assert not inspect.isabstract(ric::TabbedPanel)


def test_ric::tabbedpanel_constructor_exists():
    assert callable(ric::TabbedPanel.__init__)


def test_ric::tabbedpanel_constructor_args():
    sig = inspect.signature(ric::TabbedPanel.__init__)
    params = list(sig.parameters.keys())



def test_objectcomponent_is_not_abstract():
    assert not inspect.isabstract(ObjectComponent)


def test_objectcomponent_constructor_exists():
    assert callable(ObjectComponent.__init__)


def test_objectcomponent_constructor_args():
    sig = inspect.signature(ObjectComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric::image_is_not_abstract():
    assert not inspect.isabstract(ric::Image)


def test_ric::image_constructor_exists():
    assert callable(ric::Image.__init__)


def test_ric::image_constructor_args():
    sig = inspect.signature(ric::Image.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "alt" in params, "Missing parameter 'alt'"

def test_ric::image_has_src():
    assert hasattr(ric::Image, "src")
    descriptor = None
    for klass in ric::Image.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_ric::image_has_alt():
    assert hasattr(ric::Image, "alt")
    descriptor = None
    for klass in ric::Image.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)



def test_ric::link_is_not_abstract():
    assert not inspect.isabstract(ric::Link)


def test_ric::link_constructor_exists():
    assert callable(ric::Link.__init__)


def test_ric::link_constructor_args():
    sig = inspect.signature(ric::Link.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric::link_has_title():
    assert hasattr(ric::Link, "title")
    descriptor = None
    for klass in ric::Link.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric::paragraph_is_not_abstract():
    assert not inspect.isabstract(ric::Paragraph)


def test_ric::paragraph_constructor_exists():
    assert callable(ric::Paragraph.__init__)


def test_ric::paragraph_constructor_args():
    sig = inspect.signature(ric::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric::paragraph_has_align():
    assert hasattr(ric::Paragraph, "align")
    descriptor = None
    for klass in ric::Paragraph.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_messagedialogevent_exists():
    # Check that the Enumeration exists
    assert MessageDialogEvent is not None

def test_messagedialogevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageDialogEvent]
    expected_literals = [
        "closeDialog",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageDialogEvent"

def test_dateformat_exists():
    # Check that the Enumeration exists
    assert DateFormat is not None

def test_dateformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateFormat]
    expected_literals = [
        "ISO8601",
        "Medium",
        "Full",
        "Default",
        "Short",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateFormat"

def test_fieldsetlegendalign_exists():
    # Check that the Enumeration exists
    assert FieldSetLegendAlign is not None

def test_fieldsetlegendalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FieldSetLegendAlign]
    expected_literals = [
        "bottom",
        "center",
        "top",
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FieldSetLegendAlign"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_align_exists():
    # Check that the Enumeration exists
    assert Align is not None

def test_align_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Align]
    expected_literals = [
        "right",
        "center",
        "left",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Align"

def test_matchingoperator_exists():
    # Check that the Enumeration exists
    assert MatchingOperator is not None

def test_matchingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MatchingOperator]
    expected_literals = [
        "Different",
        "LessThan",
        "Equals",
        "LessOrEqualsThan",
        "GreaterThan",
        "Contains",
        "GreaterOrEqualsThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchingOperator"

def test_unorderedlisttype_exists():
    # Check that the Enumeration exists
    assert UnorderedListType is not None

def test_unorderedlisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnorderedListType]
    expected_literals = [
        "none",
        "square",
        "circle",
        "disc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnorderedListType"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "Vertical",
        "Horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "ondblclick",
        "onload",
        "onmousedown",
        "onmousemove",
        "onreset",
        "onmouseup",
        "onmouseout",
        "onfocus",
        "onkeydown",
        "onselect",
        "onblur",
        "onclick",
        "onsubmit",
        "onunload",
        "onchange",
        "onkeyup",
        "onmouseover",
        "onkeypress",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_locale_exists():
    # Check that the Enumeration exists
    assert Locale is not None

def test_locale_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Locale]
    expected_literals = [
        "Spanish",
        "English_UK",
        "German",
        "Portuguese_Brazilian",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Locale"

def test_phraseelementtype_exists():
    # Check that the Enumeration exists
    assert PhraseElementType is not None

def test_phraseelementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhraseElementType]
    expected_literals = [
        "EntryFromUser",
        "StrongerEmphasis",
        "VariableInstance",
        "Citation",
        "Definition",
        "Emphasis",
        "Acronym",
        "ComputerCode",
        "None_",
        "SampleProgramOutput",
        "Abbreviation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhraseElementType"

def test_orderedlisttype_exists():
    # Check that the Enumeration exists
    assert OrderedListType is not None

def test_orderedlisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderedListType]
    expected_literals = [
        "UpperRoman",
        "LowerAlpha",
        "UpperAlpha",
        "ArabicNumber",
        "none",
        "LowerRoman",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderedListType"

def test_scripttype_exists():
    # Check that the Enumeration exists
    assert ScriptType is not None

def test_scripttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScriptType]
    expected_literals = [
        "textJavaScript",
        "textTcl",
        "textVBScript",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScriptType"

def test_extension_exists():
    # Check that the Enumeration exists
    assert Extension is not None

def test_extension_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Extension]
    expected_literals = [
        "jsp",
        "php",
        "html",
        "asp",
        "xhtml",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Extension"

def test_submitformmethod_exists():
    # Check that the Enumeration exists
    assert SubmitFormMethod is not None

def test_submitformmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubmitFormMethod]
    expected_literals = [
        "post",
        "get",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubmitFormMethod"

def test_objectalign_exists():
    # Check that the Enumeration exists
    assert ObjectAlign is not None

def test_objectalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectAlign]
    expected_literals = [
        "right",
        "textTop",
        "baseline",
        "middle",
        "bottom",
        "default",
        "left",
        "absoluteBottom",
        "absoluteMiddle",
        "top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectAlign"

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "Push",
        "Reset",
        "Submit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"

def test_headinglevel_exists():
    # Check that the Enumeration exists
    assert HeadingLevel is not None

def test_headinglevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HeadingLevel]
    expected_literals = [
        "h3",
        "h2",
        "h4",
        "h1",
        "h6",
        "h5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HeadingLevel"


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
BlockLevelComponent_strategy = st.builds(
    BlockLevelComponent,
)
InlineComponent_strategy = st.builds(
    InlineComponent,
)
ric::ObjectComponent_strategy = st.builds(
    ric::ObjectComponent,
    align=
        safe_text,
    hspace=
        st.integers(),
    border=
        st.integers(),
    vspace=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers()
)
ric::CheckGroup_strategy = st.builds(
    ric::CheckGroup,
    orientation=
        safe_text
)
ric::RadioGroup_strategy = st.builds(
    ric::RadioGroup,
    orientation=
        safe_text
)
ric::SelectItem_strategy = st.builds(
    ric::SelectItem,
    value=
        safe_text,
    itemLabel=
        safe_text,
    selected=
        st.booleans()
)
ric::InlineComponent_strategy = st.builds(
    ric::InlineComponent,
    text=
        safe_text
)
ric::BlockLevelComponent_strategy = st.builds(
    ric::BlockLevelComponent,
)
ric::Script_strategy = st.builds(
    ric::Script,
    name=
        safe_text,
    implementation=
        safe_text,
    type=
        safe_text
)
FormControl_strategy = st.builds(
    FormControl,
)
ric::Radio_strategy = st.builds(
    ric::Radio,
    checked=
        st.booleans()
)
ric::InputFile_strategy = st.builds(
    ric::InputFile,
    charWidth=
        st.integers(),
    readonly=
        st.booleans(),
    maxChars=
        st.integers()
)
ric::TextArea_strategy = st.builds(
    ric::TextArea,
    cols=
        st.integers(),
    readonly=
        st.booleans(),
    rols=
        st.integers()
)
ric::Checkbox_strategy = st.builds(
    ric::Checkbox,
    checked=
        st.booleans()
)
ric::Select_strategy = st.builds(
    ric::Select,
    multiple=
        st.booleans(),
    size=
        st.integers()
)
ric::TextField_strategy = st.builds(
    ric::TextField,
    charWidth=
        st.integers(),
    readonly=
        st.booleans(),
    maxChars=
        st.integers(),
    password=
        st.booleans()
)
ric::Button_strategy = st.builds(
    ric::Button,
    image=
        safe_text,
    type=
        safe_text,
    disabled=
        st.booleans()
)
EventComponent_strategy = st.builds(
    EventComponent,
)
ric::Document_strategy = st.builds(
    ric::Document,
    fileName=
        safe_text,
    title=
        safe_text,
    index=
        st.booleans()
)
ClassifiableComponent_strategy = st.builds(
    ClassifiableComponent,
)
IdentifiableComponent_strategy = st.builds(
    IdentifiableComponent,
)
ric::LineBreak_strategy = st.builds(
    ric::LineBreak,
)
ric::Heading_strategy = st.builds(
    ric::Heading,
    level=
        safe_text
)
ric::Fieldset_strategy = st.builds(
    ric::Fieldset,
    legendFormat=
        safe_text,
    legend=
        safe_text,
    legendAlign=
        safe_text
)
ric::Div_strategy = st.builds(
    ric::Div,
    align=
        safe_text
)
ric::Span_strategy = st.builds(
    ric::Span,
    align=
        safe_text
)
ric::List_strategy = st.builds(
    ric::List,
)
ric::RichWidget_strategy = st.builds(
    ric::RichWidget,
)
ric::Label_strategy = st.builds(
    ric::Label,
    format=
        safe_text,
    text=
        safe_text
)
ric::PhraseElement_strategy = st.builds(
    ric::PhraseElement,
    phraseType=
        safe_text,
    title=
        safe_text
)
ric::Form_strategy = st.builds(
    ric::Form,
    name=
        safe_text,
    method=
        safe_text
)
ric::FormControl_strategy = st.builds(
    ric::FormControl,
    name=
        safe_text,
    value=
        safe_text
)
ric::Event_strategy = st.builds(
    ric::Event,
    type=
        safe_text
)
ric::EventComponent_strategy = st.builds(
    ric::EventComponent,
)
ric::ClassifiableComponent_strategy = st.builds(
    ric::ClassifiableComponent,
    class_=
        safe_text
)
ric::IdentifiableComponent_strategy = st.builds(
    ric::IdentifiableComponent,
    id=
        safe_text
)
ric::ListItem_strategy = st.builds(
    ric::ListItem,
    format=
        safe_text,
    text=
        safe_text
)
List_strategy = st.builds(
    List,
)
ric::UnorderedList_strategy = st.builds(
    ric::UnorderedList,
    type=
        safe_text
)
ric::OrderedList_strategy = st.builds(
    ric::OrderedList,
    type=
        safe_text
)
ric::ContentRegion_strategy = st.builds(
    ric::ContentRegion,
)
ric::LinkGroup_strategy = st.builds(
    ric::LinkGroup,
    title=
        safe_text
)
ric::Logo_strategy = st.builds(
    ric::Logo,
)
ric::FooterRegion_strategy = st.builds(
    ric::FooterRegion,
)
ric::SearchRegion_strategy = st.builds(
    ric::SearchRegion,
)
ric::ContextualNavigationRegion_strategy = st.builds(
    ric::ContextualNavigationRegion,
)
ric::NavigationRegion_strategy = st.builds(
    ric::NavigationRegion,
    orientation=
        safe_text
)
ric::HeaderRegion_strategy = st.builds(
    ric::HeaderRegion,
)
ric::Portal_strategy = st.builds(
    ric::Portal,
    name=
        safe_text,
    documentsExtension=
        safe_text
)
FormControlConstraint_strategy = st.builds(
    FormControlConstraint,
)
ric::ValidDateConstraint_strategy = st.builds(
    ric::ValidDateConstraint,
    dateFormat=
        safe_text
)
ric::NumberValueConstraint_strategy = st.builds(
    ric::NumberValueConstraint,
)
ric::ValueConstraint_strategy = st.builds(
    ric::ValueConstraint,
    logicalOperator=
        safe_text,
    matchingOperator=
        safe_text,
    matchingValue=
        safe_text
)
ric::RequiredFieldConstraint_strategy = st.builds(
    ric::RequiredFieldConstraint,
)
ric::FormControlConstraint_strategy = st.builds(
    ric::FormControlConstraint,
)
TextField_strategy = st.builds(
    TextField,
)
ric::MessageDialogButton_strategy = st.builds(
    ric::MessageDialogButton,
    event=
        safe_text,
    label=
        safe_text
)
ric::Section_strategy = st.builds(
    ric::Section,
    title=
        safe_text
)
ric::Tab_strategy = st.builds(
    ric::Tab,
    title=
        safe_text
)
RichWidget_strategy = st.builds(
    RichWidget,
)
ric::Datepicker_strategy = st.builds(
    ric::Datepicker,
    numberMonthsToShow=
        st.integers(),
    showButtonImage=
        st.booleans(),
    showButtonClosePanel=
        st.booleans(),
    locale=
        safe_text,
    dateFormat=
        safe_text,
    showMonthMenu=
        st.booleans(),
    showWeekOfYear=
        st.booleans(),
    showYearMenu=
        st.booleans()
)
ric::MessageDialog_strategy = st.builds(
    ric::MessageDialog,
    autoOpen=
        st.booleans(),
    resizable=
        st.booleans(),
    minWidthResize=
        st.integers(),
    modal=
        st.booleans(),
    maxWidthResize=
        st.integers(),
    minHeightResize=
        st.integers(),
    width=
        st.integers(),
    maxHeightResize=
        st.integers(),
    message=
        safe_text,
    height=
        st.integers(),
    title=
        safe_text
)
ric::AccordionPanel_strategy = st.builds(
    ric::AccordionPanel,
)
ric::TabbedPanel_strategy = st.builds(
    ric::TabbedPanel,
)
ObjectComponent_strategy = st.builds(
    ObjectComponent,
)
ric::Image_strategy = st.builds(
    ric::Image,
    src=
        safe_text,
    alt=
        safe_text
)
ric::Link_strategy = st.builds(
    ric::Link,
    title=
        safe_text
)
ric::Paragraph_strategy = st.builds(
    ric::Paragraph,
    align=
        safe_text
)

@given(instance=BlockLevelComponent_strategy)
@settings(max_examples=50)
def test_blocklevelcomponent_instantiation(instance):
    assert isinstance(instance, BlockLevelComponent)

@given(instance=InlineComponent_strategy)
@settings(max_examples=50)
def test_inlinecomponent_instantiation(instance):
    assert isinstance(instance, InlineComponent)

@given(instance=ric::ObjectComponent_strategy)
@settings(max_examples=50)
def test_ric::objectcomponent_instantiation(instance):
    assert isinstance(instance, ric::ObjectComponent)

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_hspace_type(instance):
    assert isinstance(instance.hspace, int)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_border_type(instance):
    assert isinstance(instance.border, int)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_vspace_type(instance):
    assert isinstance(instance.vspace, int)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=ric::ObjectComponent_strategy)
def test_ric::objectcomponent_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=ric::CheckGroup_strategy)
@settings(max_examples=50)
def test_ric::checkgroup_instantiation(instance):
    assert isinstance(instance, ric::CheckGroup)

@given(instance=ric::CheckGroup_strategy)
def test_ric::checkgroup_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=ric::CheckGroup_strategy)
def test_ric::checkgroup_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric::RadioGroup_strategy)
@settings(max_examples=50)
def test_ric::radiogroup_instantiation(instance):
    assert isinstance(instance, ric::RadioGroup)

@given(instance=ric::RadioGroup_strategy)
def test_ric::radiogroup_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=ric::RadioGroup_strategy)
def test_ric::radiogroup_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric::SelectItem_strategy)
@settings(max_examples=50)
def test_ric::selectitem_instantiation(instance):
    assert isinstance(instance, ric::SelectItem)

@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_itemLabel_type(instance):
    assert isinstance(instance.itemLabel, str)


@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_itemLabel_setter(instance):
    original = instance.itemLabel
    instance.itemLabel = original
    assert instance.itemLabel == original

@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=ric::SelectItem_strategy)
def test_ric::selectitem_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=ric::InlineComponent_strategy)
@settings(max_examples=50)
def test_ric::inlinecomponent_instantiation(instance):
    assert isinstance(instance, ric::InlineComponent)

@given(instance=ric::InlineComponent_strategy)
def test_ric::inlinecomponent_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ric::InlineComponent_strategy)
def test_ric::inlinecomponent_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ric::BlockLevelComponent_strategy)
@settings(max_examples=50)
def test_ric::blocklevelcomponent_instantiation(instance):
    assert isinstance(instance, ric::BlockLevelComponent)

@given(instance=ric::Script_strategy)
@settings(max_examples=50)
def test_ric::script_instantiation(instance):
    assert isinstance(instance, ric::Script)

@given(instance=ric::Script_strategy)
def test_ric::script_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ric::Script_strategy)
def test_ric::script_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ric::Script_strategy)
def test_ric::script_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=ric::Script_strategy)
def test_ric::script_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=ric::Script_strategy)
def test_ric::script_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ric::Script_strategy)
def test_ric::script_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=FormControl_strategy)
@settings(max_examples=50)
def test_formcontrol_instantiation(instance):
    assert isinstance(instance, FormControl)

@given(instance=ric::Radio_strategy)
@settings(max_examples=50)
def test_ric::radio_instantiation(instance):
    assert isinstance(instance, ric::Radio)

@given(instance=ric::Radio_strategy)
def test_ric::radio_checked_type(instance):
    assert isinstance(instance.checked, bool)


@given(instance=ric::Radio_strategy)
def test_ric::radio_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=ric::InputFile_strategy)
@settings(max_examples=50)
def test_ric::inputfile_instantiation(instance):
    assert isinstance(instance, ric::InputFile)

@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_charWidth_type(instance):
    assert isinstance(instance.charWidth, int)


@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_charWidth_setter(instance):
    original = instance.charWidth
    instance.charWidth = original
    assert instance.charWidth == original

@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_maxChars_type(instance):
    assert isinstance(instance.maxChars, int)


@given(instance=ric::InputFile_strategy)
def test_ric::inputfile_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original

@given(instance=ric::TextArea_strategy)
@settings(max_examples=50)
def test_ric::textarea_instantiation(instance):
    assert isinstance(instance, ric::TextArea)

@given(instance=ric::TextArea_strategy)
def test_ric::textarea_cols_type(instance):
    assert isinstance(instance.cols, int)


@given(instance=ric::TextArea_strategy)
def test_ric::textarea_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original

@given(instance=ric::TextArea_strategy)
def test_ric::textarea_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=ric::TextArea_strategy)
def test_ric::textarea_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=ric::TextArea_strategy)
def test_ric::textarea_rols_type(instance):
    assert isinstance(instance.rols, int)


@given(instance=ric::TextArea_strategy)
def test_ric::textarea_rols_setter(instance):
    original = instance.rols
    instance.rols = original
    assert instance.rols == original

@given(instance=ric::Checkbox_strategy)
@settings(max_examples=50)
def test_ric::checkbox_instantiation(instance):
    assert isinstance(instance, ric::Checkbox)

@given(instance=ric::Checkbox_strategy)
def test_ric::checkbox_checked_type(instance):
    assert isinstance(instance.checked, bool)


@given(instance=ric::Checkbox_strategy)
def test_ric::checkbox_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=ric::Select_strategy)
@settings(max_examples=50)
def test_ric::select_instantiation(instance):
    assert isinstance(instance, ric::Select)

@given(instance=ric::Select_strategy)
def test_ric::select_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=ric::Select_strategy)
def test_ric::select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ric::Select_strategy)
def test_ric::select_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=ric::Select_strategy)
def test_ric::select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ric::TextField_strategy)
@settings(max_examples=50)
def test_ric::textfield_instantiation(instance):
    assert isinstance(instance, ric::TextField)

@given(instance=ric::TextField_strategy)
def test_ric::textfield_charWidth_type(instance):
    assert isinstance(instance.charWidth, int)


@given(instance=ric::TextField_strategy)
def test_ric::textfield_charWidth_setter(instance):
    original = instance.charWidth
    instance.charWidth = original
    assert instance.charWidth == original

@given(instance=ric::TextField_strategy)
def test_ric::textfield_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=ric::TextField_strategy)
def test_ric::textfield_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=ric::TextField_strategy)
def test_ric::textfield_maxChars_type(instance):
    assert isinstance(instance.maxChars, int)


@given(instance=ric::TextField_strategy)
def test_ric::textfield_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original

@given(instance=ric::TextField_strategy)
def test_ric::textfield_password_type(instance):
    assert isinstance(instance.password, bool)


@given(instance=ric::TextField_strategy)
def test_ric::textfield_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=ric::Button_strategy)
@settings(max_examples=50)
def test_ric::button_instantiation(instance):
    assert isinstance(instance, ric::Button)

@given(instance=ric::Button_strategy)
def test_ric::button_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=ric::Button_strategy)
def test_ric::button_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=ric::Button_strategy)
def test_ric::button_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ric::Button_strategy)
def test_ric::button_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric::Button_strategy)
def test_ric::button_disabled_type(instance):
    assert isinstance(instance.disabled, bool)


@given(instance=ric::Button_strategy)
def test_ric::button_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=EventComponent_strategy)
@settings(max_examples=50)
def test_eventcomponent_instantiation(instance):
    assert isinstance(instance, EventComponent)

@given(instance=ric::Document_strategy)
@settings(max_examples=50)
def test_ric::document_instantiation(instance):
    assert isinstance(instance, ric::Document)

@given(instance=ric::Document_strategy)
def test_ric::document_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=ric::Document_strategy)
def test_ric::document_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=ric::Document_strategy)
def test_ric::document_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::Document_strategy)
def test_ric::document_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::Document_strategy)
def test_ric::document_index_type(instance):
    assert isinstance(instance.index, bool)


@given(instance=ric::Document_strategy)
def test_ric::document_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=ClassifiableComponent_strategy)
@settings(max_examples=50)
def test_classifiablecomponent_instantiation(instance):
    assert isinstance(instance, ClassifiableComponent)

@given(instance=IdentifiableComponent_strategy)
@settings(max_examples=50)
def test_identifiablecomponent_instantiation(instance):
    assert isinstance(instance, IdentifiableComponent)

@given(instance=ric::LineBreak_strategy)
@settings(max_examples=50)
def test_ric::linebreak_instantiation(instance):
    assert isinstance(instance, ric::LineBreak)

@given(instance=ric::Heading_strategy)
@settings(max_examples=50)
def test_ric::heading_instantiation(instance):
    assert isinstance(instance, ric::Heading)

@given(instance=ric::Heading_strategy)
def test_ric::heading_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=ric::Heading_strategy)
def test_ric::heading_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=ric::Fieldset_strategy)
@settings(max_examples=50)
def test_ric::fieldset_instantiation(instance):
    assert isinstance(instance, ric::Fieldset)

@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legendFormat_type(instance):
    assert isinstance(instance.legendFormat, str)


@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legendFormat_setter(instance):
    original = instance.legendFormat
    instance.legendFormat = original
    assert instance.legendFormat == original

@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legend_type(instance):
    assert isinstance(instance.legend, str)


@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legend_setter(instance):
    original = instance.legend
    instance.legend = original
    assert instance.legend == original

@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legendAlign_type(instance):
    assert isinstance(instance.legendAlign, str)


@given(instance=ric::Fieldset_strategy)
def test_ric::fieldset_legendAlign_setter(instance):
    original = instance.legendAlign
    instance.legendAlign = original
    assert instance.legendAlign == original

@given(instance=ric::Div_strategy)
@settings(max_examples=50)
def test_ric::div_instantiation(instance):
    assert isinstance(instance, ric::Div)

@given(instance=ric::Div_strategy)
def test_ric::div_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=ric::Div_strategy)
def test_ric::div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric::Span_strategy)
@settings(max_examples=50)
def test_ric::span_instantiation(instance):
    assert isinstance(instance, ric::Span)

@given(instance=ric::Span_strategy)
def test_ric::span_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=ric::Span_strategy)
def test_ric::span_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric::List_strategy)
@settings(max_examples=50)
def test_ric::list_instantiation(instance):
    assert isinstance(instance, ric::List)

@given(instance=ric::RichWidget_strategy)
@settings(max_examples=50)
def test_ric::richwidget_instantiation(instance):
    assert isinstance(instance, ric::RichWidget)

@given(instance=ric::Label_strategy)
@settings(max_examples=50)
def test_ric::label_instantiation(instance):
    assert isinstance(instance, ric::Label)

@given(instance=ric::Label_strategy)
def test_ric::label_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=ric::Label_strategy)
def test_ric::label_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=ric::Label_strategy)
def test_ric::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ric::Label_strategy)
def test_ric::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ric::PhraseElement_strategy)
@settings(max_examples=50)
def test_ric::phraseelement_instantiation(instance):
    assert isinstance(instance, ric::PhraseElement)

@given(instance=ric::PhraseElement_strategy)
def test_ric::phraseelement_phraseType_type(instance):
    assert isinstance(instance.phraseType, str)


@given(instance=ric::PhraseElement_strategy)
def test_ric::phraseelement_phraseType_setter(instance):
    original = instance.phraseType
    instance.phraseType = original
    assert instance.phraseType == original

@given(instance=ric::PhraseElement_strategy)
def test_ric::phraseelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::PhraseElement_strategy)
def test_ric::phraseelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::Form_strategy)
@settings(max_examples=50)
def test_ric::form_instantiation(instance):
    assert isinstance(instance, ric::Form)

@given(instance=ric::Form_strategy)
def test_ric::form_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ric::Form_strategy)
def test_ric::form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ric::Form_strategy)
def test_ric::form_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=ric::Form_strategy)
def test_ric::form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=ric::FormControl_strategy)
@settings(max_examples=50)
def test_ric::formcontrol_instantiation(instance):
    assert isinstance(instance, ric::FormControl)

@given(instance=ric::FormControl_strategy)
def test_ric::formcontrol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ric::FormControl_strategy)
def test_ric::formcontrol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ric::FormControl_strategy)
def test_ric::formcontrol_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ric::FormControl_strategy)
def test_ric::formcontrol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ric::Event_strategy)
@settings(max_examples=50)
def test_ric::event_instantiation(instance):
    assert isinstance(instance, ric::Event)

@given(instance=ric::Event_strategy)
def test_ric::event_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ric::Event_strategy)
def test_ric::event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric::EventComponent_strategy)
@settings(max_examples=50)
def test_ric::eventcomponent_instantiation(instance):
    assert isinstance(instance, ric::EventComponent)

@given(instance=ric::ClassifiableComponent_strategy)
@settings(max_examples=50)
def test_ric::classifiablecomponent_instantiation(instance):
    assert isinstance(instance, ric::ClassifiableComponent)

@given(instance=ric::ClassifiableComponent_strategy)
def test_ric::classifiablecomponent_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=ric::ClassifiableComponent_strategy)
def test_ric::classifiablecomponent_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=ric::IdentifiableComponent_strategy)
@settings(max_examples=50)
def test_ric::identifiablecomponent_instantiation(instance):
    assert isinstance(instance, ric::IdentifiableComponent)

@given(instance=ric::IdentifiableComponent_strategy)
def test_ric::identifiablecomponent_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ric::IdentifiableComponent_strategy)
def test_ric::identifiablecomponent_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ric::ListItem_strategy)
@settings(max_examples=50)
def test_ric::listitem_instantiation(instance):
    assert isinstance(instance, ric::ListItem)

@given(instance=ric::ListItem_strategy)
def test_ric::listitem_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=ric::ListItem_strategy)
def test_ric::listitem_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=ric::ListItem_strategy)
def test_ric::listitem_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ric::ListItem_strategy)
def test_ric::listitem_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=List_strategy)
@settings(max_examples=50)
def test_list_instantiation(instance):
    assert isinstance(instance, List)

@given(instance=ric::UnorderedList_strategy)
@settings(max_examples=50)
def test_ric::unorderedlist_instantiation(instance):
    assert isinstance(instance, ric::UnorderedList)

@given(instance=ric::UnorderedList_strategy)
def test_ric::unorderedlist_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ric::UnorderedList_strategy)
def test_ric::unorderedlist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric::OrderedList_strategy)
@settings(max_examples=50)
def test_ric::orderedlist_instantiation(instance):
    assert isinstance(instance, ric::OrderedList)

@given(instance=ric::OrderedList_strategy)
def test_ric::orderedlist_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ric::OrderedList_strategy)
def test_ric::orderedlist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric::ContentRegion_strategy)
@settings(max_examples=50)
def test_ric::contentregion_instantiation(instance):
    assert isinstance(instance, ric::ContentRegion)

@given(instance=ric::LinkGroup_strategy)
@settings(max_examples=50)
def test_ric::linkgroup_instantiation(instance):
    assert isinstance(instance, ric::LinkGroup)

@given(instance=ric::LinkGroup_strategy)
def test_ric::linkgroup_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::LinkGroup_strategy)
def test_ric::linkgroup_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::Logo_strategy)
@settings(max_examples=50)
def test_ric::logo_instantiation(instance):
    assert isinstance(instance, ric::Logo)

@given(instance=ric::FooterRegion_strategy)
@settings(max_examples=50)
def test_ric::footerregion_instantiation(instance):
    assert isinstance(instance, ric::FooterRegion)

@given(instance=ric::SearchRegion_strategy)
@settings(max_examples=50)
def test_ric::searchregion_instantiation(instance):
    assert isinstance(instance, ric::SearchRegion)

@given(instance=ric::ContextualNavigationRegion_strategy)
@settings(max_examples=50)
def test_ric::contextualnavigationregion_instantiation(instance):
    assert isinstance(instance, ric::ContextualNavigationRegion)

@given(instance=ric::NavigationRegion_strategy)
@settings(max_examples=50)
def test_ric::navigationregion_instantiation(instance):
    assert isinstance(instance, ric::NavigationRegion)

@given(instance=ric::NavigationRegion_strategy)
def test_ric::navigationregion_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=ric::NavigationRegion_strategy)
def test_ric::navigationregion_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric::HeaderRegion_strategy)
@settings(max_examples=50)
def test_ric::headerregion_instantiation(instance):
    assert isinstance(instance, ric::HeaderRegion)

@given(instance=ric::Portal_strategy)
@settings(max_examples=50)
def test_ric::portal_instantiation(instance):
    assert isinstance(instance, ric::Portal)

@given(instance=ric::Portal_strategy)
def test_ric::portal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ric::Portal_strategy)
def test_ric::portal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ric::Portal_strategy)
def test_ric::portal_documentsExtension_type(instance):
    assert isinstance(instance.documentsExtension, str)


@given(instance=ric::Portal_strategy)
def test_ric::portal_documentsExtension_setter(instance):
    original = instance.documentsExtension
    instance.documentsExtension = original
    assert instance.documentsExtension == original

@given(instance=FormControlConstraint_strategy)
@settings(max_examples=50)
def test_formcontrolconstraint_instantiation(instance):
    assert isinstance(instance, FormControlConstraint)

@given(instance=ric::ValidDateConstraint_strategy)
@settings(max_examples=50)
def test_ric::validdateconstraint_instantiation(instance):
    assert isinstance(instance, ric::ValidDateConstraint)

@given(instance=ric::ValidDateConstraint_strategy)
def test_ric::validdateconstraint_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=ric::ValidDateConstraint_strategy)
def test_ric::validdateconstraint_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=ric::NumberValueConstraint_strategy)
@settings(max_examples=50)
def test_ric::numbervalueconstraint_instantiation(instance):
    assert isinstance(instance, ric::NumberValueConstraint)

@given(instance=ric::ValueConstraint_strategy)
@settings(max_examples=50)
def test_ric::valueconstraint_instantiation(instance):
    assert isinstance(instance, ric::ValueConstraint)

@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_logicalOperator_type(instance):
    assert isinstance(instance.logicalOperator, str)


@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original

@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_matchingOperator_type(instance):
    assert isinstance(instance.matchingOperator, str)


@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_matchingOperator_setter(instance):
    original = instance.matchingOperator
    instance.matchingOperator = original
    assert instance.matchingOperator == original

@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_matchingValue_type(instance):
    assert isinstance(instance.matchingValue, str)


@given(instance=ric::ValueConstraint_strategy)
def test_ric::valueconstraint_matchingValue_setter(instance):
    original = instance.matchingValue
    instance.matchingValue = original
    assert instance.matchingValue == original

@given(instance=ric::RequiredFieldConstraint_strategy)
@settings(max_examples=50)
def test_ric::requiredfieldconstraint_instantiation(instance):
    assert isinstance(instance, ric::RequiredFieldConstraint)

@given(instance=ric::FormControlConstraint_strategy)
@settings(max_examples=50)
def test_ric::formcontrolconstraint_instantiation(instance):
    assert isinstance(instance, ric::FormControlConstraint)

@given(instance=TextField_strategy)
@settings(max_examples=50)
def test_textfield_instantiation(instance):
    assert isinstance(instance, TextField)

@given(instance=ric::MessageDialogButton_strategy)
@settings(max_examples=50)
def test_ric::messagedialogbutton_instantiation(instance):
    assert isinstance(instance, ric::MessageDialogButton)

@given(instance=ric::MessageDialogButton_strategy)
def test_ric::messagedialogbutton_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=ric::MessageDialogButton_strategy)
def test_ric::messagedialogbutton_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=ric::MessageDialogButton_strategy)
def test_ric::messagedialogbutton_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ric::MessageDialogButton_strategy)
def test_ric::messagedialogbutton_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ric::Section_strategy)
@settings(max_examples=50)
def test_ric::section_instantiation(instance):
    assert isinstance(instance, ric::Section)

@given(instance=ric::Section_strategy)
def test_ric::section_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::Section_strategy)
def test_ric::section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::Tab_strategy)
@settings(max_examples=50)
def test_ric::tab_instantiation(instance):
    assert isinstance(instance, ric::Tab)

@given(instance=ric::Tab_strategy)
def test_ric::tab_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::Tab_strategy)
def test_ric::tab_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=RichWidget_strategy)
@settings(max_examples=50)
def test_richwidget_instantiation(instance):
    assert isinstance(instance, RichWidget)

@given(instance=ric::Datepicker_strategy)
@settings(max_examples=50)
def test_ric::datepicker_instantiation(instance):
    assert isinstance(instance, ric::Datepicker)

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_numberMonthsToShow_type(instance):
    assert isinstance(instance.numberMonthsToShow, int)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_numberMonthsToShow_setter(instance):
    original = instance.numberMonthsToShow
    instance.numberMonthsToShow = original
    assert instance.numberMonthsToShow == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showButtonImage_type(instance):
    assert isinstance(instance.showButtonImage, bool)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showButtonImage_setter(instance):
    original = instance.showButtonImage
    instance.showButtonImage = original
    assert instance.showButtonImage == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showButtonClosePanel_type(instance):
    assert isinstance(instance.showButtonClosePanel, bool)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showButtonClosePanel_setter(instance):
    original = instance.showButtonClosePanel
    instance.showButtonClosePanel = original
    assert instance.showButtonClosePanel == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_locale_type(instance):
    assert isinstance(instance.locale, str)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showMonthMenu_type(instance):
    assert isinstance(instance.showMonthMenu, bool)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showMonthMenu_setter(instance):
    original = instance.showMonthMenu
    instance.showMonthMenu = original
    assert instance.showMonthMenu == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showWeekOfYear_type(instance):
    assert isinstance(instance.showWeekOfYear, bool)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showWeekOfYear_setter(instance):
    original = instance.showWeekOfYear
    instance.showWeekOfYear = original
    assert instance.showWeekOfYear == original

@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showYearMenu_type(instance):
    assert isinstance(instance.showYearMenu, bool)


@given(instance=ric::Datepicker_strategy)
def test_ric::datepicker_showYearMenu_setter(instance):
    original = instance.showYearMenu
    instance.showYearMenu = original
    assert instance.showYearMenu == original

@given(instance=ric::MessageDialog_strategy)
@settings(max_examples=50)
def test_ric::messagedialog_instantiation(instance):
    assert isinstance(instance, ric::MessageDialog)

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_autoOpen_type(instance):
    assert isinstance(instance.autoOpen, bool)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_autoOpen_setter(instance):
    original = instance.autoOpen
    instance.autoOpen = original
    assert instance.autoOpen == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_resizable_type(instance):
    assert isinstance(instance.resizable, bool)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_minWidthResize_type(instance):
    assert isinstance(instance.minWidthResize, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_minWidthResize_setter(instance):
    original = instance.minWidthResize
    instance.minWidthResize = original
    assert instance.minWidthResize == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_modal_type(instance):
    assert isinstance(instance.modal, bool)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_modal_setter(instance):
    original = instance.modal
    instance.modal = original
    assert instance.modal == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_maxWidthResize_type(instance):
    assert isinstance(instance.maxWidthResize, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_maxWidthResize_setter(instance):
    original = instance.maxWidthResize
    instance.maxWidthResize = original
    assert instance.maxWidthResize == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_minHeightResize_type(instance):
    assert isinstance(instance.minHeightResize, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_minHeightResize_setter(instance):
    original = instance.minHeightResize
    instance.minHeightResize = original
    assert instance.minHeightResize == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_maxHeightResize_type(instance):
    assert isinstance(instance.maxHeightResize, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_maxHeightResize_setter(instance):
    original = instance.maxHeightResize
    instance.maxHeightResize = original
    assert instance.maxHeightResize == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::MessageDialog_strategy)
def test_ric::messagedialog_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::AccordionPanel_strategy)
@settings(max_examples=50)
def test_ric::accordionpanel_instantiation(instance):
    assert isinstance(instance, ric::AccordionPanel)

@given(instance=ric::TabbedPanel_strategy)
@settings(max_examples=50)
def test_ric::tabbedpanel_instantiation(instance):
    assert isinstance(instance, ric::TabbedPanel)

@given(instance=ObjectComponent_strategy)
@settings(max_examples=50)
def test_objectcomponent_instantiation(instance):
    assert isinstance(instance, ObjectComponent)

@given(instance=ric::Image_strategy)
@settings(max_examples=50)
def test_ric::image_instantiation(instance):
    assert isinstance(instance, ric::Image)

@given(instance=ric::Image_strategy)
def test_ric::image_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=ric::Image_strategy)
def test_ric::image_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=ric::Image_strategy)
def test_ric::image_alt_type(instance):
    assert isinstance(instance.alt, str)


@given(instance=ric::Image_strategy)
def test_ric::image_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original

@given(instance=ric::Link_strategy)
@settings(max_examples=50)
def test_ric::link_instantiation(instance):
    assert isinstance(instance, ric::Link)

@given(instance=ric::Link_strategy)
def test_ric::link_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=ric::Link_strategy)
def test_ric::link_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric::Paragraph_strategy)
@settings(max_examples=50)
def test_ric::paragraph_instantiation(instance):
    assert isinstance(instance, ric::Paragraph)

@given(instance=ric::Paragraph_strategy)
def test_ric::paragraph_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=ric::Paragraph_strategy)
def test_ric::paragraph_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original
