import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ric_ListItem,
    List,
    ric_UnorderedList,
    ric_OrderedList,
    ric_ContentRegion,
    ric_LinkGroup,
    ric_Logo,
    ric_FooterRegion,
    ric_SearchRegion,
    ric_ContextualNavigationRegion,
    ric_NavigationRegion,
    ric_HeaderRegion,
    ric_Portal,
    FormControlConstraint,
    ric_FormControlConstraint,
    TextField,
    ric_MessageDialogButton,
    ric_Section,
    ric_Tab,
    RichWidget,
    ric_AccordionPanel,
    ric_MessageDialog,
    ric_Datepicker,
    ric_TabbedPanel,
    ObjectComponent,
    BlockLevelComponent,
    InlineComponent,
    ric_ObjectComponent,
    ric_CheckGroup,
    ric_RadioGroup,
    ric_SelectItem,
    ric_InlineComponent,
    ric_BlockLevelComponent,
    ric_Script,
    FormControl,
    ric_InputFile,
    ric_Checkbox,
    ric_TextArea,
    ric_Radio,
    ric_TextField,
    ric_Select,
    ric_Button,
    ric_ValidDateConstraint,
    ric_RequiredFieldConstraint,
    ric_NumberValueConstraint,
    ric_ValueConstraint,
    EventComponent,
    ric_Document,
    ClassifiableComponent,
    IdentifiableComponent,
    ric_RichWidget,
    ric_Div,
    ric_Label,
    ric_Fieldset,
    ric_Link,
    ric_List,
    ric_Image,
    ric_Span,
    ric_Form,
    ric_Paragraph,
    ric_PhraseElement,
    ric_LineBreak,
    ric_Heading,
    ric_FormControl,
    ric_Event,
    ric_EventComponent,
    ric_ClassifiableComponent,
    ric_IdentifiableComponent,
    Extension,
    FieldSetLegendAlign,
    ObjectAlign,
    LogicalOperator,
    EventType,
    Align,
    MatchingOperator,
    ButtonType,
    Locale,
    OrderedListType,
    MessageDialogEvent,
    DateFormat,
    Orientation,
    UnorderedListType,
    HeadingLevel,
    ScriptType,
    SubmitFormMethod,
    PhraseElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ric_listitem_is_not_abstract():
    assert not inspect.isabstract(ric_ListItem)


def test_ric_listitem_constructor_exists():
    assert callable(ric_ListItem.__init__)


def test_ric_listitem_constructor_args():
    sig = inspect.signature(ric_ListItem.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "format" in params, "Missing parameter 'format'"

def test_ric_listitem_has_text():
    assert hasattr(ric_ListItem, "text")
    descriptor = None
    for klass in ric_ListItem.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_ric_listitem_has_format():
    assert hasattr(ric_ListItem, "format")
    descriptor = None
    for klass in ric_ListItem.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_list_is_not_abstract():
    assert not inspect.isabstract(List)


def test_list_constructor_exists():
    assert callable(List.__init__)


def test_list_constructor_args():
    sig = inspect.signature(List.__init__)
    params = list(sig.parameters.keys())



def test_ric_unorderedlist_is_not_abstract():
    assert not inspect.isabstract(ric_UnorderedList)


def test_ric_unorderedlist_constructor_exists():
    assert callable(ric_UnorderedList.__init__)


def test_ric_unorderedlist_constructor_args():
    sig = inspect.signature(ric_UnorderedList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric_unorderedlist_has_type():
    assert hasattr(ric_UnorderedList, "type")
    descriptor = None
    for klass in ric_UnorderedList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric_orderedlist_is_not_abstract():
    assert not inspect.isabstract(ric_OrderedList)


def test_ric_orderedlist_constructor_exists():
    assert callable(ric_OrderedList.__init__)


def test_ric_orderedlist_constructor_args():
    sig = inspect.signature(ric_OrderedList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric_orderedlist_has_type():
    assert hasattr(ric_OrderedList, "type")
    descriptor = None
    for klass in ric_OrderedList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric_contentregion_is_not_abstract():
    assert not inspect.isabstract(ric_ContentRegion)


def test_ric_contentregion_constructor_exists():
    assert callable(ric_ContentRegion.__init__)


def test_ric_contentregion_constructor_args():
    sig = inspect.signature(ric_ContentRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric_linkgroup_is_not_abstract():
    assert not inspect.isabstract(ric_LinkGroup)


def test_ric_linkgroup_constructor_exists():
    assert callable(ric_LinkGroup.__init__)


def test_ric_linkgroup_constructor_args():
    sig = inspect.signature(ric_LinkGroup.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric_linkgroup_has_title():
    assert hasattr(ric_LinkGroup, "title")
    descriptor = None
    for klass in ric_LinkGroup.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric_logo_is_not_abstract():
    assert not inspect.isabstract(ric_Logo)


def test_ric_logo_constructor_exists():
    assert callable(ric_Logo.__init__)


def test_ric_logo_constructor_args():
    sig = inspect.signature(ric_Logo.__init__)
    params = list(sig.parameters.keys())



def test_ric_footerregion_is_not_abstract():
    assert not inspect.isabstract(ric_FooterRegion)


def test_ric_footerregion_constructor_exists():
    assert callable(ric_FooterRegion.__init__)


def test_ric_footerregion_constructor_args():
    sig = inspect.signature(ric_FooterRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric_searchregion_is_not_abstract():
    assert not inspect.isabstract(ric_SearchRegion)


def test_ric_searchregion_constructor_exists():
    assert callable(ric_SearchRegion.__init__)


def test_ric_searchregion_constructor_args():
    sig = inspect.signature(ric_SearchRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric_contextualnavigationregion_is_not_abstract():
    assert not inspect.isabstract(ric_ContextualNavigationRegion)


def test_ric_contextualnavigationregion_constructor_exists():
    assert callable(ric_ContextualNavigationRegion.__init__)


def test_ric_contextualnavigationregion_constructor_args():
    sig = inspect.signature(ric_ContextualNavigationRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric_navigationregion_is_not_abstract():
    assert not inspect.isabstract(ric_NavigationRegion)


def test_ric_navigationregion_constructor_exists():
    assert callable(ric_NavigationRegion.__init__)


def test_ric_navigationregion_constructor_args():
    sig = inspect.signature(ric_NavigationRegion.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric_navigationregion_has_orientation():
    assert hasattr(ric_NavigationRegion, "orientation")
    descriptor = None
    for klass in ric_NavigationRegion.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric_headerregion_is_not_abstract():
    assert not inspect.isabstract(ric_HeaderRegion)


def test_ric_headerregion_constructor_exists():
    assert callable(ric_HeaderRegion.__init__)


def test_ric_headerregion_constructor_args():
    sig = inspect.signature(ric_HeaderRegion.__init__)
    params = list(sig.parameters.keys())



def test_ric_portal_is_not_abstract():
    assert not inspect.isabstract(ric_Portal)


def test_ric_portal_constructor_exists():
    assert callable(ric_Portal.__init__)


def test_ric_portal_constructor_args():
    sig = inspect.signature(ric_Portal.__init__)
    params = list(sig.parameters.keys())
    assert "documentsExtension" in params, "Missing parameter 'documentsExtension'"
    assert "name" in params, "Missing parameter 'name'"

def test_ric_portal_has_documentsExtension():
    assert hasattr(ric_Portal, "documentsExtension")
    descriptor = None
    for klass in ric_Portal.__mro__:
        if "documentsExtension" in klass.__dict__:
            descriptor = klass.__dict__["documentsExtension"]
            break
    assert isinstance(descriptor, property)

def test_ric_portal_has_name():
    assert hasattr(ric_Portal, "name")
    descriptor = None
    for klass in ric_Portal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_formcontrolconstraint_is_not_abstract():
    assert not inspect.isabstract(FormControlConstraint)


def test_formcontrolconstraint_constructor_exists():
    assert callable(FormControlConstraint.__init__)


def test_formcontrolconstraint_constructor_args():
    sig = inspect.signature(FormControlConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric_formcontrolconstraint_is_not_abstract():
    assert not inspect.isabstract(ric_FormControlConstraint)


def test_ric_formcontrolconstraint_constructor_exists():
    assert callable(ric_FormControlConstraint.__init__)


def test_ric_formcontrolconstraint_constructor_args():
    sig = inspect.signature(ric_FormControlConstraint.__init__)
    params = list(sig.parameters.keys())



def test_textfield_is_not_abstract():
    assert not inspect.isabstract(TextField)


def test_textfield_constructor_exists():
    assert callable(TextField.__init__)


def test_textfield_constructor_args():
    sig = inspect.signature(TextField.__init__)
    params = list(sig.parameters.keys())



def test_ric_messagedialogbutton_is_not_abstract():
    assert not inspect.isabstract(ric_MessageDialogButton)


def test_ric_messagedialogbutton_constructor_exists():
    assert callable(ric_MessageDialogButton.__init__)


def test_ric_messagedialogbutton_constructor_args():
    sig = inspect.signature(ric_MessageDialogButton.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "event" in params, "Missing parameter 'event'"

def test_ric_messagedialogbutton_has_label():
    assert hasattr(ric_MessageDialogButton, "label")
    descriptor = None
    for klass in ric_MessageDialogButton.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialogbutton_has_event():
    assert hasattr(ric_MessageDialogButton, "event")
    descriptor = None
    for klass in ric_MessageDialogButton.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_ric_section_is_not_abstract():
    assert not inspect.isabstract(ric_Section)


def test_ric_section_constructor_exists():
    assert callable(ric_Section.__init__)


def test_ric_section_constructor_args():
    sig = inspect.signature(ric_Section.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric_section_has_title():
    assert hasattr(ric_Section, "title")
    descriptor = None
    for klass in ric_Section.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric_tab_is_not_abstract():
    assert not inspect.isabstract(ric_Tab)


def test_ric_tab_constructor_exists():
    assert callable(ric_Tab.__init__)


def test_ric_tab_constructor_args():
    sig = inspect.signature(ric_Tab.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric_tab_has_title():
    assert hasattr(ric_Tab, "title")
    descriptor = None
    for klass in ric_Tab.__mro__:
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



def test_ric_accordionpanel_is_not_abstract():
    assert not inspect.isabstract(ric_AccordionPanel)


def test_ric_accordionpanel_constructor_exists():
    assert callable(ric_AccordionPanel.__init__)


def test_ric_accordionpanel_constructor_args():
    sig = inspect.signature(ric_AccordionPanel.__init__)
    params = list(sig.parameters.keys())



def test_ric_messagedialog_is_not_abstract():
    assert not inspect.isabstract(ric_MessageDialog)


def test_ric_messagedialog_constructor_exists():
    assert callable(ric_MessageDialog.__init__)


def test_ric_messagedialog_constructor_args():
    sig = inspect.signature(ric_MessageDialog.__init__)
    params = list(sig.parameters.keys())
    assert "autoOpen" in params, "Missing parameter 'autoOpen'"
    assert "minWidthResize" in params, "Missing parameter 'minWidthResize'"
    assert "maxHeightResize" in params, "Missing parameter 'maxHeightResize'"
    assert "width" in params, "Missing parameter 'width'"
    assert "message" in params, "Missing parameter 'message'"
    assert "maxWidthResize" in params, "Missing parameter 'maxWidthResize'"
    assert "minHeightResize" in params, "Missing parameter 'minHeightResize'"
    assert "modal" in params, "Missing parameter 'modal'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "height" in params, "Missing parameter 'height'"
    assert "title" in params, "Missing parameter 'title'"

def test_ric_messagedialog_has_autoOpen():
    assert hasattr(ric_MessageDialog, "autoOpen")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "autoOpen" in klass.__dict__:
            descriptor = klass.__dict__["autoOpen"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_minWidthResize():
    assert hasattr(ric_MessageDialog, "minWidthResize")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "minWidthResize" in klass.__dict__:
            descriptor = klass.__dict__["minWidthResize"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_maxHeightResize():
    assert hasattr(ric_MessageDialog, "maxHeightResize")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "maxHeightResize" in klass.__dict__:
            descriptor = klass.__dict__["maxHeightResize"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_width():
    assert hasattr(ric_MessageDialog, "width")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_message():
    assert hasattr(ric_MessageDialog, "message")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_maxWidthResize():
    assert hasattr(ric_MessageDialog, "maxWidthResize")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "maxWidthResize" in klass.__dict__:
            descriptor = klass.__dict__["maxWidthResize"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_minHeightResize():
    assert hasattr(ric_MessageDialog, "minHeightResize")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "minHeightResize" in klass.__dict__:
            descriptor = klass.__dict__["minHeightResize"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_modal():
    assert hasattr(ric_MessageDialog, "modal")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "modal" in klass.__dict__:
            descriptor = klass.__dict__["modal"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_resizable():
    assert hasattr(ric_MessageDialog, "resizable")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_height():
    assert hasattr(ric_MessageDialog, "height")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_ric_messagedialog_has_title():
    assert hasattr(ric_MessageDialog, "title")
    descriptor = None
    for klass in ric_MessageDialog.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric_datepicker_is_not_abstract():
    assert not inspect.isabstract(ric_Datepicker)


def test_ric_datepicker_constructor_exists():
    assert callable(ric_Datepicker.__init__)


def test_ric_datepicker_constructor_args():
    sig = inspect.signature(ric_Datepicker.__init__)
    params = list(sig.parameters.keys())
    assert "showButtonImage" in params, "Missing parameter 'showButtonImage'"
    assert "showButtonClosePanel" in params, "Missing parameter 'showButtonClosePanel'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"
    assert "showYearMenu" in params, "Missing parameter 'showYearMenu'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "showWeekOfYear" in params, "Missing parameter 'showWeekOfYear'"
    assert "numberMonthsToShow" in params, "Missing parameter 'numberMonthsToShow'"
    assert "showMonthMenu" in params, "Missing parameter 'showMonthMenu'"

def test_ric_datepicker_has_showButtonImage():
    assert hasattr(ric_Datepicker, "showButtonImage")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "showButtonImage" in klass.__dict__:
            descriptor = klass.__dict__["showButtonImage"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_showButtonClosePanel():
    assert hasattr(ric_Datepicker, "showButtonClosePanel")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "showButtonClosePanel" in klass.__dict__:
            descriptor = klass.__dict__["showButtonClosePanel"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_dateFormat():
    assert hasattr(ric_Datepicker, "dateFormat")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_showYearMenu():
    assert hasattr(ric_Datepicker, "showYearMenu")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "showYearMenu" in klass.__dict__:
            descriptor = klass.__dict__["showYearMenu"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_locale():
    assert hasattr(ric_Datepicker, "locale")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_showWeekOfYear():
    assert hasattr(ric_Datepicker, "showWeekOfYear")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "showWeekOfYear" in klass.__dict__:
            descriptor = klass.__dict__["showWeekOfYear"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_numberMonthsToShow():
    assert hasattr(ric_Datepicker, "numberMonthsToShow")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "numberMonthsToShow" in klass.__dict__:
            descriptor = klass.__dict__["numberMonthsToShow"]
            break
    assert isinstance(descriptor, property)

def test_ric_datepicker_has_showMonthMenu():
    assert hasattr(ric_Datepicker, "showMonthMenu")
    descriptor = None
    for klass in ric_Datepicker.__mro__:
        if "showMonthMenu" in klass.__dict__:
            descriptor = klass.__dict__["showMonthMenu"]
            break
    assert isinstance(descriptor, property)



def test_ric_tabbedpanel_is_not_abstract():
    assert not inspect.isabstract(ric_TabbedPanel)


def test_ric_tabbedpanel_constructor_exists():
    assert callable(ric_TabbedPanel.__init__)


def test_ric_tabbedpanel_constructor_args():
    sig = inspect.signature(ric_TabbedPanel.__init__)
    params = list(sig.parameters.keys())



def test_objectcomponent_is_not_abstract():
    assert not inspect.isabstract(ObjectComponent)


def test_objectcomponent_constructor_exists():
    assert callable(ObjectComponent.__init__)


def test_objectcomponent_constructor_args():
    sig = inspect.signature(ObjectComponent.__init__)
    params = list(sig.parameters.keys())



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



def test_ric_objectcomponent_is_not_abstract():
    assert not inspect.isabstract(ric_ObjectComponent)


def test_ric_objectcomponent_constructor_exists():
    assert callable(ric_ObjectComponent.__init__)


def test_ric_objectcomponent_constructor_args():
    sig = inspect.signature(ric_ObjectComponent.__init__)
    params = list(sig.parameters.keys())
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "align" in params, "Missing parameter 'align'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "border" in params, "Missing parameter 'border'"

def test_ric_objectcomponent_has_hspace():
    assert hasattr(ric_ObjectComponent, "hspace")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_ric_objectcomponent_has_width():
    assert hasattr(ric_ObjectComponent, "width")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ric_objectcomponent_has_height():
    assert hasattr(ric_ObjectComponent, "height")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_ric_objectcomponent_has_align():
    assert hasattr(ric_ObjectComponent, "align")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_ric_objectcomponent_has_vspace():
    assert hasattr(ric_ObjectComponent, "vspace")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_ric_objectcomponent_has_border():
    assert hasattr(ric_ObjectComponent, "border")
    descriptor = None
    for klass in ric_ObjectComponent.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)



def test_ric_checkgroup_is_not_abstract():
    assert not inspect.isabstract(ric_CheckGroup)


def test_ric_checkgroup_constructor_exists():
    assert callable(ric_CheckGroup.__init__)


def test_ric_checkgroup_constructor_args():
    sig = inspect.signature(ric_CheckGroup.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric_checkgroup_has_orientation():
    assert hasattr(ric_CheckGroup, "orientation")
    descriptor = None
    for klass in ric_CheckGroup.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric_radiogroup_is_not_abstract():
    assert not inspect.isabstract(ric_RadioGroup)


def test_ric_radiogroup_constructor_exists():
    assert callable(ric_RadioGroup.__init__)


def test_ric_radiogroup_constructor_args():
    sig = inspect.signature(ric_RadioGroup.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_ric_radiogroup_has_orientation():
    assert hasattr(ric_RadioGroup, "orientation")
    descriptor = None
    for klass in ric_RadioGroup.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_ric_selectitem_is_not_abstract():
    assert not inspect.isabstract(ric_SelectItem)


def test_ric_selectitem_constructor_exists():
    assert callable(ric_SelectItem.__init__)


def test_ric_selectitem_constructor_args():
    sig = inspect.signature(ric_SelectItem.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "value" in params, "Missing parameter 'value'"
    assert "itemLabel" in params, "Missing parameter 'itemLabel'"

def test_ric_selectitem_has_selected():
    assert hasattr(ric_SelectItem, "selected")
    descriptor = None
    for klass in ric_SelectItem.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_ric_selectitem_has_value():
    assert hasattr(ric_SelectItem, "value")
    descriptor = None
    for klass in ric_SelectItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ric_selectitem_has_itemLabel():
    assert hasattr(ric_SelectItem, "itemLabel")
    descriptor = None
    for klass in ric_SelectItem.__mro__:
        if "itemLabel" in klass.__dict__:
            descriptor = klass.__dict__["itemLabel"]
            break
    assert isinstance(descriptor, property)



def test_ric_inlinecomponent_is_not_abstract():
    assert not inspect.isabstract(ric_InlineComponent)


def test_ric_inlinecomponent_constructor_exists():
    assert callable(ric_InlineComponent.__init__)


def test_ric_inlinecomponent_constructor_args():
    sig = inspect.signature(ric_InlineComponent.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ric_inlinecomponent_has_text():
    assert hasattr(ric_InlineComponent, "text")
    descriptor = None
    for klass in ric_InlineComponent.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ric_blocklevelcomponent_is_not_abstract():
    assert not inspect.isabstract(ric_BlockLevelComponent)


def test_ric_blocklevelcomponent_constructor_exists():
    assert callable(ric_BlockLevelComponent.__init__)


def test_ric_blocklevelcomponent_constructor_args():
    sig = inspect.signature(ric_BlockLevelComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric_script_is_not_abstract():
    assert not inspect.isabstract(ric_Script)


def test_ric_script_constructor_exists():
    assert callable(ric_Script.__init__)


def test_ric_script_constructor_args():
    sig = inspect.signature(ric_Script.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "type" in params, "Missing parameter 'type'"

def test_ric_script_has_name():
    assert hasattr(ric_Script, "name")
    descriptor = None
    for klass in ric_Script.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric_script_has_implementation():
    assert hasattr(ric_Script, "implementation")
    descriptor = None
    for klass in ric_Script.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_ric_script_has_type():
    assert hasattr(ric_Script, "type")
    descriptor = None
    for klass in ric_Script.__mro__:
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



def test_ric_inputfile_is_not_abstract():
    assert not inspect.isabstract(ric_InputFile)


def test_ric_inputfile_constructor_exists():
    assert callable(ric_InputFile.__init__)


def test_ric_inputfile_constructor_args():
    sig = inspect.signature(ric_InputFile.__init__)
    params = list(sig.parameters.keys())
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "charWidth" in params, "Missing parameter 'charWidth'"
    assert "maxChars" in params, "Missing parameter 'maxChars'"

def test_ric_inputfile_has_readonly():
    assert hasattr(ric_InputFile, "readonly")
    descriptor = None
    for klass in ric_InputFile.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_ric_inputfile_has_charWidth():
    assert hasattr(ric_InputFile, "charWidth")
    descriptor = None
    for klass in ric_InputFile.__mro__:
        if "charWidth" in klass.__dict__:
            descriptor = klass.__dict__["charWidth"]
            break
    assert isinstance(descriptor, property)

def test_ric_inputfile_has_maxChars():
    assert hasattr(ric_InputFile, "maxChars")
    descriptor = None
    for klass in ric_InputFile.__mro__:
        if "maxChars" in klass.__dict__:
            descriptor = klass.__dict__["maxChars"]
            break
    assert isinstance(descriptor, property)



def test_ric_checkbox_is_not_abstract():
    assert not inspect.isabstract(ric_Checkbox)


def test_ric_checkbox_constructor_exists():
    assert callable(ric_Checkbox.__init__)


def test_ric_checkbox_constructor_args():
    sig = inspect.signature(ric_Checkbox.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_ric_checkbox_has_checked():
    assert hasattr(ric_Checkbox, "checked")
    descriptor = None
    for klass in ric_Checkbox.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_ric_textarea_is_not_abstract():
    assert not inspect.isabstract(ric_TextArea)


def test_ric_textarea_constructor_exists():
    assert callable(ric_TextArea.__init__)


def test_ric_textarea_constructor_args():
    sig = inspect.signature(ric_TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "rols" in params, "Missing parameter 'rols'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_ric_textarea_has_rols():
    assert hasattr(ric_TextArea, "rols")
    descriptor = None
    for klass in ric_TextArea.__mro__:
        if "rols" in klass.__dict__:
            descriptor = klass.__dict__["rols"]
            break
    assert isinstance(descriptor, property)

def test_ric_textarea_has_cols():
    assert hasattr(ric_TextArea, "cols")
    descriptor = None
    for klass in ric_TextArea.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_ric_textarea_has_readonly():
    assert hasattr(ric_TextArea, "readonly")
    descriptor = None
    for klass in ric_TextArea.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_ric_radio_is_not_abstract():
    assert not inspect.isabstract(ric_Radio)


def test_ric_radio_constructor_exists():
    assert callable(ric_Radio.__init__)


def test_ric_radio_constructor_args():
    sig = inspect.signature(ric_Radio.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_ric_radio_has_checked():
    assert hasattr(ric_Radio, "checked")
    descriptor = None
    for klass in ric_Radio.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_ric_textfield_is_not_abstract():
    assert not inspect.isabstract(ric_TextField)


def test_ric_textfield_constructor_exists():
    assert callable(ric_TextField.__init__)


def test_ric_textfield_constructor_args():
    sig = inspect.signature(ric_TextField.__init__)
    params = list(sig.parameters.keys())
    assert "maxChars" in params, "Missing parameter 'maxChars'"
    assert "charWidth" in params, "Missing parameter 'charWidth'"
    assert "password" in params, "Missing parameter 'password'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_ric_textfield_has_maxChars():
    assert hasattr(ric_TextField, "maxChars")
    descriptor = None
    for klass in ric_TextField.__mro__:
        if "maxChars" in klass.__dict__:
            descriptor = klass.__dict__["maxChars"]
            break
    assert isinstance(descriptor, property)

def test_ric_textfield_has_charWidth():
    assert hasattr(ric_TextField, "charWidth")
    descriptor = None
    for klass in ric_TextField.__mro__:
        if "charWidth" in klass.__dict__:
            descriptor = klass.__dict__["charWidth"]
            break
    assert isinstance(descriptor, property)

def test_ric_textfield_has_password():
    assert hasattr(ric_TextField, "password")
    descriptor = None
    for klass in ric_TextField.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_ric_textfield_has_readonly():
    assert hasattr(ric_TextField, "readonly")
    descriptor = None
    for klass in ric_TextField.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_ric_select_is_not_abstract():
    assert not inspect.isabstract(ric_Select)


def test_ric_select_constructor_exists():
    assert callable(ric_Select.__init__)


def test_ric_select_constructor_args():
    sig = inspect.signature(ric_Select.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_ric_select_has_size():
    assert hasattr(ric_Select, "size")
    descriptor = None
    for klass in ric_Select.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ric_select_has_multiple():
    assert hasattr(ric_Select, "multiple")
    descriptor = None
    for klass in ric_Select.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_ric_button_is_not_abstract():
    assert not inspect.isabstract(ric_Button)


def test_ric_button_constructor_exists():
    assert callable(ric_Button.__init__)


def test_ric_button_constructor_args():
    sig = inspect.signature(ric_Button.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "type" in params, "Missing parameter 'type'"

def test_ric_button_has_image():
    assert hasattr(ric_Button, "image")
    descriptor = None
    for klass in ric_Button.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_ric_button_has_disabled():
    assert hasattr(ric_Button, "disabled")
    descriptor = None
    for klass in ric_Button.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_ric_button_has_type():
    assert hasattr(ric_Button, "type")
    descriptor = None
    for klass in ric_Button.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric_validdateconstraint_is_not_abstract():
    assert not inspect.isabstract(ric_ValidDateConstraint)


def test_ric_validdateconstraint_constructor_exists():
    assert callable(ric_ValidDateConstraint.__init__)


def test_ric_validdateconstraint_constructor_args():
    sig = inspect.signature(ric_ValidDateConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_ric_validdateconstraint_has_dateFormat():
    assert hasattr(ric_ValidDateConstraint, "dateFormat")
    descriptor = None
    for klass in ric_ValidDateConstraint.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_ric_requiredfieldconstraint_is_not_abstract():
    assert not inspect.isabstract(ric_RequiredFieldConstraint)


def test_ric_requiredfieldconstraint_constructor_exists():
    assert callable(ric_RequiredFieldConstraint.__init__)


def test_ric_requiredfieldconstraint_constructor_args():
    sig = inspect.signature(ric_RequiredFieldConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric_numbervalueconstraint_is_not_abstract():
    assert not inspect.isabstract(ric_NumberValueConstraint)


def test_ric_numbervalueconstraint_constructor_exists():
    assert callable(ric_NumberValueConstraint.__init__)


def test_ric_numbervalueconstraint_constructor_args():
    sig = inspect.signature(ric_NumberValueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_ric_valueconstraint_is_not_abstract():
    assert not inspect.isabstract(ric_ValueConstraint)


def test_ric_valueconstraint_constructor_exists():
    assert callable(ric_ValueConstraint.__init__)


def test_ric_valueconstraint_constructor_args():
    sig = inspect.signature(ric_ValueConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "matchingValue" in params, "Missing parameter 'matchingValue'"
    assert "matchingOperator" in params, "Missing parameter 'matchingOperator'"
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"

def test_ric_valueconstraint_has_matchingValue():
    assert hasattr(ric_ValueConstraint, "matchingValue")
    descriptor = None
    for klass in ric_ValueConstraint.__mro__:
        if "matchingValue" in klass.__dict__:
            descriptor = klass.__dict__["matchingValue"]
            break
    assert isinstance(descriptor, property)

def test_ric_valueconstraint_has_matchingOperator():
    assert hasattr(ric_ValueConstraint, "matchingOperator")
    descriptor = None
    for klass in ric_ValueConstraint.__mro__:
        if "matchingOperator" in klass.__dict__:
            descriptor = klass.__dict__["matchingOperator"]
            break
    assert isinstance(descriptor, property)

def test_ric_valueconstraint_has_logicalOperator():
    assert hasattr(ric_ValueConstraint, "logicalOperator")
    descriptor = None
    for klass in ric_ValueConstraint.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)



def test_eventcomponent_is_not_abstract():
    assert not inspect.isabstract(EventComponent)


def test_eventcomponent_constructor_exists():
    assert callable(EventComponent.__init__)


def test_eventcomponent_constructor_args():
    sig = inspect.signature(EventComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric_document_is_not_abstract():
    assert not inspect.isabstract(ric_Document)


def test_ric_document_constructor_exists():
    assert callable(ric_Document.__init__)


def test_ric_document_constructor_args():
    sig = inspect.signature(ric_Document.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "index" in params, "Missing parameter 'index'"

def test_ric_document_has_title():
    assert hasattr(ric_Document, "title")
    descriptor = None
    for klass in ric_Document.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_ric_document_has_fileName():
    assert hasattr(ric_Document, "fileName")
    descriptor = None
    for klass in ric_Document.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_ric_document_has_index():
    assert hasattr(ric_Document, "index")
    descriptor = None
    for klass in ric_Document.__mro__:
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



def test_ric_richwidget_is_not_abstract():
    assert not inspect.isabstract(ric_RichWidget)


def test_ric_richwidget_constructor_exists():
    assert callable(ric_RichWidget.__init__)


def test_ric_richwidget_constructor_args():
    sig = inspect.signature(ric_RichWidget.__init__)
    params = list(sig.parameters.keys())



def test_ric_div_is_not_abstract():
    assert not inspect.isabstract(ric_Div)


def test_ric_div_constructor_exists():
    assert callable(ric_Div.__init__)


def test_ric_div_constructor_args():
    sig = inspect.signature(ric_Div.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric_div_has_align():
    assert hasattr(ric_Div, "align")
    descriptor = None
    for klass in ric_Div.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ric_label_is_not_abstract():
    assert not inspect.isabstract(ric_Label)


def test_ric_label_constructor_exists():
    assert callable(ric_Label.__init__)


def test_ric_label_constructor_args():
    sig = inspect.signature(ric_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "format" in params, "Missing parameter 'format'"

def test_ric_label_has_text():
    assert hasattr(ric_Label, "text")
    descriptor = None
    for klass in ric_Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_ric_label_has_format():
    assert hasattr(ric_Label, "format")
    descriptor = None
    for klass in ric_Label.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_ric_fieldset_is_not_abstract():
    assert not inspect.isabstract(ric_Fieldset)


def test_ric_fieldset_constructor_exists():
    assert callable(ric_Fieldset.__init__)


def test_ric_fieldset_constructor_args():
    sig = inspect.signature(ric_Fieldset.__init__)
    params = list(sig.parameters.keys())
    assert "legendAlign" in params, "Missing parameter 'legendAlign'"
    assert "legend" in params, "Missing parameter 'legend'"
    assert "legendFormat" in params, "Missing parameter 'legendFormat'"

def test_ric_fieldset_has_legendAlign():
    assert hasattr(ric_Fieldset, "legendAlign")
    descriptor = None
    for klass in ric_Fieldset.__mro__:
        if "legendAlign" in klass.__dict__:
            descriptor = klass.__dict__["legendAlign"]
            break
    assert isinstance(descriptor, property)

def test_ric_fieldset_has_legend():
    assert hasattr(ric_Fieldset, "legend")
    descriptor = None
    for klass in ric_Fieldset.__mro__:
        if "legend" in klass.__dict__:
            descriptor = klass.__dict__["legend"]
            break
    assert isinstance(descriptor, property)

def test_ric_fieldset_has_legendFormat():
    assert hasattr(ric_Fieldset, "legendFormat")
    descriptor = None
    for klass in ric_Fieldset.__mro__:
        if "legendFormat" in klass.__dict__:
            descriptor = klass.__dict__["legendFormat"]
            break
    assert isinstance(descriptor, property)



def test_ric_link_is_not_abstract():
    assert not inspect.isabstract(ric_Link)


def test_ric_link_constructor_exists():
    assert callable(ric_Link.__init__)


def test_ric_link_constructor_args():
    sig = inspect.signature(ric_Link.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_ric_link_has_title():
    assert hasattr(ric_Link, "title")
    descriptor = None
    for klass in ric_Link.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric_list_is_not_abstract():
    assert not inspect.isabstract(ric_List)


def test_ric_list_constructor_exists():
    assert callable(ric_List.__init__)


def test_ric_list_constructor_args():
    sig = inspect.signature(ric_List.__init__)
    params = list(sig.parameters.keys())



def test_ric_image_is_not_abstract():
    assert not inspect.isabstract(ric_Image)


def test_ric_image_constructor_exists():
    assert callable(ric_Image.__init__)


def test_ric_image_constructor_args():
    sig = inspect.signature(ric_Image.__init__)
    params = list(sig.parameters.keys())
    assert "alt" in params, "Missing parameter 'alt'"
    assert "src" in params, "Missing parameter 'src'"

def test_ric_image_has_alt():
    assert hasattr(ric_Image, "alt")
    descriptor = None
    for klass in ric_Image.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)

def test_ric_image_has_src():
    assert hasattr(ric_Image, "src")
    descriptor = None
    for klass in ric_Image.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_ric_span_is_not_abstract():
    assert not inspect.isabstract(ric_Span)


def test_ric_span_constructor_exists():
    assert callable(ric_Span.__init__)


def test_ric_span_constructor_args():
    sig = inspect.signature(ric_Span.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric_span_has_align():
    assert hasattr(ric_Span, "align")
    descriptor = None
    for klass in ric_Span.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ric_form_is_not_abstract():
    assert not inspect.isabstract(ric_Form)


def test_ric_form_constructor_exists():
    assert callable(ric_Form.__init__)


def test_ric_form_constructor_args():
    sig = inspect.signature(ric_Form.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "method" in params, "Missing parameter 'method'"

def test_ric_form_has_name():
    assert hasattr(ric_Form, "name")
    descriptor = None
    for klass in ric_Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric_form_has_method():
    assert hasattr(ric_Form, "method")
    descriptor = None
    for klass in ric_Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_ric_paragraph_is_not_abstract():
    assert not inspect.isabstract(ric_Paragraph)


def test_ric_paragraph_constructor_exists():
    assert callable(ric_Paragraph.__init__)


def test_ric_paragraph_constructor_args():
    sig = inspect.signature(ric_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_ric_paragraph_has_align():
    assert hasattr(ric_Paragraph, "align")
    descriptor = None
    for klass in ric_Paragraph.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ric_phraseelement_is_not_abstract():
    assert not inspect.isabstract(ric_PhraseElement)


def test_ric_phraseelement_constructor_exists():
    assert callable(ric_PhraseElement.__init__)


def test_ric_phraseelement_constructor_args():
    sig = inspect.signature(ric_PhraseElement.__init__)
    params = list(sig.parameters.keys())
    assert "phraseType" in params, "Missing parameter 'phraseType'"
    assert "title" in params, "Missing parameter 'title'"

def test_ric_phraseelement_has_phraseType():
    assert hasattr(ric_PhraseElement, "phraseType")
    descriptor = None
    for klass in ric_PhraseElement.__mro__:
        if "phraseType" in klass.__dict__:
            descriptor = klass.__dict__["phraseType"]
            break
    assert isinstance(descriptor, property)

def test_ric_phraseelement_has_title():
    assert hasattr(ric_PhraseElement, "title")
    descriptor = None
    for klass in ric_PhraseElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_ric_linebreak_is_not_abstract():
    assert not inspect.isabstract(ric_LineBreak)


def test_ric_linebreak_constructor_exists():
    assert callable(ric_LineBreak.__init__)


def test_ric_linebreak_constructor_args():
    sig = inspect.signature(ric_LineBreak.__init__)
    params = list(sig.parameters.keys())



def test_ric_heading_is_not_abstract():
    assert not inspect.isabstract(ric_Heading)


def test_ric_heading_constructor_exists():
    assert callable(ric_Heading.__init__)


def test_ric_heading_constructor_args():
    sig = inspect.signature(ric_Heading.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_ric_heading_has_level():
    assert hasattr(ric_Heading, "level")
    descriptor = None
    for klass in ric_Heading.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_ric_formcontrol_is_not_abstract():
    assert not inspect.isabstract(ric_FormControl)


def test_ric_formcontrol_constructor_exists():
    assert callable(ric_FormControl.__init__)


def test_ric_formcontrol_constructor_args():
    sig = inspect.signature(ric_FormControl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_ric_formcontrol_has_name():
    assert hasattr(ric_FormControl, "name")
    descriptor = None
    for klass in ric_FormControl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ric_formcontrol_has_value():
    assert hasattr(ric_FormControl, "value")
    descriptor = None
    for klass in ric_FormControl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ric_event_is_not_abstract():
    assert not inspect.isabstract(ric_Event)


def test_ric_event_constructor_exists():
    assert callable(ric_Event.__init__)


def test_ric_event_constructor_args():
    sig = inspect.signature(ric_Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ric_event_has_type():
    assert hasattr(ric_Event, "type")
    descriptor = None
    for klass in ric_Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ric_eventcomponent_is_not_abstract():
    assert not inspect.isabstract(ric_EventComponent)


def test_ric_eventcomponent_constructor_exists():
    assert callable(ric_EventComponent.__init__)


def test_ric_eventcomponent_constructor_args():
    sig = inspect.signature(ric_EventComponent.__init__)
    params = list(sig.parameters.keys())



def test_ric_classifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(ric_ClassifiableComponent)


def test_ric_classifiablecomponent_constructor_exists():
    assert callable(ric_ClassifiableComponent.__init__)


def test_ric_classifiablecomponent_constructor_args():
    sig = inspect.signature(ric_ClassifiableComponent.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_ric_classifiablecomponent_has_class_():
    assert hasattr(ric_ClassifiableComponent, "class_")
    descriptor = None
    for klass in ric_ClassifiableComponent.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_ric_identifiablecomponent_is_not_abstract():
    assert not inspect.isabstract(ric_IdentifiableComponent)


def test_ric_identifiablecomponent_constructor_exists():
    assert callable(ric_IdentifiableComponent.__init__)


def test_ric_identifiablecomponent_constructor_args():
    sig = inspect.signature(ric_IdentifiableComponent.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ric_identifiablecomponent_has_id():
    assert hasattr(ric_IdentifiableComponent, "id")
    descriptor = None
    for klass in ric_IdentifiableComponent.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_extension_exists():
    # Check that the Enumeration exists
    assert Extension is not None

def test_extension_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Extension]
    expected_literals = [
        "xhtml",
        "jsp",
        "html",
        "php",
        "asp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Extension"

def test_fieldsetlegendalign_exists():
    # Check that the Enumeration exists
    assert FieldSetLegendAlign is not None

def test_fieldsetlegendalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FieldSetLegendAlign]
    expected_literals = [
        "center",
        "bottom",
        "top",
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FieldSetLegendAlign"

def test_objectalign_exists():
    # Check that the Enumeration exists
    assert ObjectAlign is not None

def test_objectalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectAlign]
    expected_literals = [
        "middle",
        "default",
        "bottom",
        "absoluteBottom",
        "textTop",
        "top",
        "right",
        "baseline",
        "left",
        "absoluteMiddle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectAlign"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "onkeydown",
        "onsubmit",
        "onfocus",
        "onkeypress",
        "onchange",
        "onclick",
        "onmouseover",
        "onkeyup",
        "ondblclick",
        "onselect",
        "onmouseout",
        "onunload",
        "onmousedown",
        "onmouseup",
        "onreset",
        "onmousemove",
        "onload",
        "onblur",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_align_exists():
    # Check that the Enumeration exists
    assert Align is not None

def test_align_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Align]
    expected_literals = [
        "right",
        "center",
        "justify",
        "left",
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
        "LessThan",
        "GreaterOrEqualsThan",
        "Equals",
        "Contains",
        "Different",
        "GreaterThan",
        "LessOrEqualsThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MatchingOperator"

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "Submit",
        "Reset",
        "Push",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"

def test_locale_exists():
    # Check that the Enumeration exists
    assert Locale is not None

def test_locale_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Locale]
    expected_literals = [
        "Portuguese_Brazilian",
        "German",
        "English_UK",
        "Spanish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Locale"

def test_orderedlisttype_exists():
    # Check that the Enumeration exists
    assert OrderedListType is not None

def test_orderedlisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderedListType]
    expected_literals = [
        "UpperRoman",
        "none",
        "LowerRoman",
        "LowerAlpha",
        "UpperAlpha",
        "ArabicNumber",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderedListType"

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
        "Full",
        "Default",
        "Short",
        "ISO8601",
        "Medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateFormat"

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

def test_unorderedlisttype_exists():
    # Check that the Enumeration exists
    assert UnorderedListType is not None

def test_unorderedlisttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnorderedListType]
    expected_literals = [
        "circle",
        "none",
        "disc",
        "square",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnorderedListType"

def test_headinglevel_exists():
    # Check that the Enumeration exists
    assert HeadingLevel is not None

def test_headinglevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HeadingLevel]
    expected_literals = [
        "h4",
        "h1",
        "h3",
        "h5",
        "h2",
        "h6",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HeadingLevel"

def test_scripttype_exists():
    # Check that the Enumeration exists
    assert ScriptType is not None

def test_scripttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScriptType]
    expected_literals = [
        "textVBScript",
        "textTcl",
        "textJavaScript",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScriptType"

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

def test_phraseelementtype_exists():
    # Check that the Enumeration exists
    assert PhraseElementType is not None

def test_phraseelementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PhraseElementType]
    expected_literals = [
        "StrongerEmphasis",
        "Definition",
        "Acronym",
        "None_",
        "Emphasis",
        "ComputerCode",
        "Abbreviation",
        "VariableInstance",
        "SampleProgramOutput",
        "EntryFromUser",
        "Citation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PhraseElementType"


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
ric_ListItem_strategy = st.builds(
    ric_ListItem,
    text=
        safe_text,
    format=
        safe_text
)
List_strategy = st.builds(
    List,
)
ric_UnorderedList_strategy = st.builds(
    ric_UnorderedList,
    type=
        safe_text
)
ric_OrderedList_strategy = st.builds(
    ric_OrderedList,
    type=
        safe_text
)
ric_ContentRegion_strategy = st.builds(
    ric_ContentRegion,
)
ric_LinkGroup_strategy = st.builds(
    ric_LinkGroup,
    title=
        safe_text
)
ric_Logo_strategy = st.builds(
    ric_Logo,
)
ric_FooterRegion_strategy = st.builds(
    ric_FooterRegion,
)
ric_SearchRegion_strategy = st.builds(
    ric_SearchRegion,
)
ric_ContextualNavigationRegion_strategy = st.builds(
    ric_ContextualNavigationRegion,
)
ric_NavigationRegion_strategy = st.builds(
    ric_NavigationRegion,
    orientation=
        safe_text
)
ric_HeaderRegion_strategy = st.builds(
    ric_HeaderRegion,
)
ric_Portal_strategy = st.builds(
    ric_Portal,
    documentsExtension=
        safe_text,
    name=
        safe_text
)
FormControlConstraint_strategy = st.builds(
    FormControlConstraint,
)
ric_FormControlConstraint_strategy = st.builds(
    ric_FormControlConstraint,
)
TextField_strategy = st.builds(
    TextField,
)
ric_MessageDialogButton_strategy = st.builds(
    ric_MessageDialogButton,
    label=
        safe_text,
    event=
        safe_text
)
ric_Section_strategy = st.builds(
    ric_Section,
    title=
        safe_text
)
ric_Tab_strategy = st.builds(
    ric_Tab,
    title=
        safe_text
)
RichWidget_strategy = st.builds(
    RichWidget,
)
ric_AccordionPanel_strategy = st.builds(
    ric_AccordionPanel,
)
ric_MessageDialog_strategy = st.builds(
    ric_MessageDialog,
    autoOpen=
        st.booleans(),
    minWidthResize=
        st.integers(),
    maxHeightResize=
        st.integers(),
    width=
        st.integers(),
    message=
        safe_text,
    maxWidthResize=
        st.integers(),
    minHeightResize=
        st.integers(),
    modal=
        st.booleans(),
    resizable=
        st.booleans(),
    height=
        st.integers(),
    title=
        safe_text
)
ric_Datepicker_strategy = st.builds(
    ric_Datepicker,
    showButtonImage=
        st.booleans(),
    showButtonClosePanel=
        st.booleans(),
    dateFormat=
        safe_text,
    showYearMenu=
        st.booleans(),
    locale=
        safe_text,
    showWeekOfYear=
        st.booleans(),
    numberMonthsToShow=
        st.integers(),
    showMonthMenu=
        st.booleans()
)
ric_TabbedPanel_strategy = st.builds(
    ric_TabbedPanel,
)
ObjectComponent_strategy = st.builds(
    ObjectComponent,
)
BlockLevelComponent_strategy = st.builds(
    BlockLevelComponent,
)
InlineComponent_strategy = st.builds(
    InlineComponent,
)
ric_ObjectComponent_strategy = st.builds(
    ric_ObjectComponent,
    hspace=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers(),
    align=
        safe_text,
    vspace=
        st.integers(),
    border=
        st.integers()
)
ric_CheckGroup_strategy = st.builds(
    ric_CheckGroup,
    orientation=
        safe_text
)
ric_RadioGroup_strategy = st.builds(
    ric_RadioGroup,
    orientation=
        safe_text
)
ric_SelectItem_strategy = st.builds(
    ric_SelectItem,
    selected=
        st.booleans(),
    value=
        safe_text,
    itemLabel=
        safe_text
)
ric_InlineComponent_strategy = st.builds(
    ric_InlineComponent,
    text=
        safe_text
)
ric_BlockLevelComponent_strategy = st.builds(
    ric_BlockLevelComponent,
)
ric_Script_strategy = st.builds(
    ric_Script,
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
ric_InputFile_strategy = st.builds(
    ric_InputFile,
    readonly=
        st.booleans(),
    charWidth=
        st.integers(),
    maxChars=
        st.integers()
)
ric_Checkbox_strategy = st.builds(
    ric_Checkbox,
    checked=
        st.booleans()
)
ric_TextArea_strategy = st.builds(
    ric_TextArea,
    rols=
        st.integers(),
    cols=
        st.integers(),
    readonly=
        st.booleans()
)
ric_Radio_strategy = st.builds(
    ric_Radio,
    checked=
        st.booleans()
)
ric_TextField_strategy = st.builds(
    ric_TextField,
    maxChars=
        st.integers(),
    charWidth=
        st.integers(),
    password=
        st.booleans(),
    readonly=
        st.booleans()
)
ric_Select_strategy = st.builds(
    ric_Select,
    size=
        st.integers(),
    multiple=
        st.booleans()
)
ric_Button_strategy = st.builds(
    ric_Button,
    image=
        safe_text,
    disabled=
        st.booleans(),
    type=
        safe_text
)
ric_ValidDateConstraint_strategy = st.builds(
    ric_ValidDateConstraint,
    dateFormat=
        safe_text
)
ric_RequiredFieldConstraint_strategy = st.builds(
    ric_RequiredFieldConstraint,
)
ric_NumberValueConstraint_strategy = st.builds(
    ric_NumberValueConstraint,
)
ric_ValueConstraint_strategy = st.builds(
    ric_ValueConstraint,
    matchingValue=
        safe_text,
    matchingOperator=
        safe_text,
    logicalOperator=
        safe_text
)
EventComponent_strategy = st.builds(
    EventComponent,
)
ric_Document_strategy = st.builds(
    ric_Document,
    title=
        safe_text,
    fileName=
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
ric_RichWidget_strategy = st.builds(
    ric_RichWidget,
)
ric_Div_strategy = st.builds(
    ric_Div,
    align=
        safe_text
)
ric_Label_strategy = st.builds(
    ric_Label,
    text=
        safe_text,
    format=
        safe_text
)
ric_Fieldset_strategy = st.builds(
    ric_Fieldset,
    legendAlign=
        safe_text,
    legend=
        safe_text,
    legendFormat=
        safe_text
)
ric_Link_strategy = st.builds(
    ric_Link,
    title=
        safe_text
)
ric_List_strategy = st.builds(
    ric_List,
)
ric_Image_strategy = st.builds(
    ric_Image,
    alt=
        safe_text,
    src=
        safe_text
)
ric_Span_strategy = st.builds(
    ric_Span,
    align=
        safe_text
)
ric_Form_strategy = st.builds(
    ric_Form,
    name=
        safe_text,
    method=
        safe_text
)
ric_Paragraph_strategy = st.builds(
    ric_Paragraph,
    align=
        safe_text
)
ric_PhraseElement_strategy = st.builds(
    ric_PhraseElement,
    phraseType=
        safe_text,
    title=
        safe_text
)
ric_LineBreak_strategy = st.builds(
    ric_LineBreak,
)
ric_Heading_strategy = st.builds(
    ric_Heading,
    level=
        safe_text
)
ric_FormControl_strategy = st.builds(
    ric_FormControl,
    name=
        safe_text,
    value=
        safe_text
)
ric_Event_strategy = st.builds(
    ric_Event,
    type=
        safe_text
)
ric_EventComponent_strategy = st.builds(
    ric_EventComponent,
)
ric_ClassifiableComponent_strategy = st.builds(
    ric_ClassifiableComponent,
    class_=
        safe_text
)
ric_IdentifiableComponent_strategy = st.builds(
    ric_IdentifiableComponent,
    id=
        safe_text
)

@given(instance=ric_ListItem_strategy)
@settings(max_examples=50)
def test_ric_listitem_instantiation(instance):
    assert isinstance(instance, ric_ListItem)



@given(instance=ric_ListItem_strategy)
def test_ric_listitem_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=ric_ListItem_strategy)
def test_ric_listitem_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=List_strategy)
@settings(max_examples=50)
def test_list_instantiation(instance):
    assert isinstance(instance, List)

@given(instance=ric_UnorderedList_strategy)
@settings(max_examples=50)
def test_ric_unorderedlist_instantiation(instance):
    assert isinstance(instance, ric_UnorderedList)



@given(instance=ric_UnorderedList_strategy)
def test_ric_unorderedlist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric_OrderedList_strategy)
@settings(max_examples=50)
def test_ric_orderedlist_instantiation(instance):
    assert isinstance(instance, ric_OrderedList)



@given(instance=ric_OrderedList_strategy)
def test_ric_orderedlist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric_ContentRegion_strategy)
@settings(max_examples=50)
def test_ric_contentregion_instantiation(instance):
    assert isinstance(instance, ric_ContentRegion)

@given(instance=ric_LinkGroup_strategy)
@settings(max_examples=50)
def test_ric_linkgroup_instantiation(instance):
    assert isinstance(instance, ric_LinkGroup)



@given(instance=ric_LinkGroup_strategy)
def test_ric_linkgroup_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric_Logo_strategy)
@settings(max_examples=50)
def test_ric_logo_instantiation(instance):
    assert isinstance(instance, ric_Logo)

@given(instance=ric_FooterRegion_strategy)
@settings(max_examples=50)
def test_ric_footerregion_instantiation(instance):
    assert isinstance(instance, ric_FooterRegion)

@given(instance=ric_SearchRegion_strategy)
@settings(max_examples=50)
def test_ric_searchregion_instantiation(instance):
    assert isinstance(instance, ric_SearchRegion)

@given(instance=ric_ContextualNavigationRegion_strategy)
@settings(max_examples=50)
def test_ric_contextualnavigationregion_instantiation(instance):
    assert isinstance(instance, ric_ContextualNavigationRegion)

@given(instance=ric_NavigationRegion_strategy)
@settings(max_examples=50)
def test_ric_navigationregion_instantiation(instance):
    assert isinstance(instance, ric_NavigationRegion)



@given(instance=ric_NavigationRegion_strategy)
def test_ric_navigationregion_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric_HeaderRegion_strategy)
@settings(max_examples=50)
def test_ric_headerregion_instantiation(instance):
    assert isinstance(instance, ric_HeaderRegion)

@given(instance=ric_Portal_strategy)
@settings(max_examples=50)
def test_ric_portal_instantiation(instance):
    assert isinstance(instance, ric_Portal)



@given(instance=ric_Portal_strategy)
def test_ric_portal_documentsExtension_setter(instance):
    original = instance.documentsExtension
    instance.documentsExtension = original
    assert instance.documentsExtension == original



@given(instance=ric_Portal_strategy)
def test_ric_portal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FormControlConstraint_strategy)
@settings(max_examples=50)
def test_formcontrolconstraint_instantiation(instance):
    assert isinstance(instance, FormControlConstraint)

@given(instance=ric_FormControlConstraint_strategy)
@settings(max_examples=50)
def test_ric_formcontrolconstraint_instantiation(instance):
    assert isinstance(instance, ric_FormControlConstraint)

@given(instance=TextField_strategy)
@settings(max_examples=50)
def test_textfield_instantiation(instance):
    assert isinstance(instance, TextField)

@given(instance=ric_MessageDialogButton_strategy)
@settings(max_examples=50)
def test_ric_messagedialogbutton_instantiation(instance):
    assert isinstance(instance, ric_MessageDialogButton)



@given(instance=ric_MessageDialogButton_strategy)
def test_ric_messagedialogbutton_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=ric_MessageDialogButton_strategy)
def test_ric_messagedialogbutton_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=ric_Section_strategy)
@settings(max_examples=50)
def test_ric_section_instantiation(instance):
    assert isinstance(instance, ric_Section)



@given(instance=ric_Section_strategy)
def test_ric_section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric_Tab_strategy)
@settings(max_examples=50)
def test_ric_tab_instantiation(instance):
    assert isinstance(instance, ric_Tab)



@given(instance=ric_Tab_strategy)
def test_ric_tab_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=RichWidget_strategy)
@settings(max_examples=50)
def test_richwidget_instantiation(instance):
    assert isinstance(instance, RichWidget)

@given(instance=ric_AccordionPanel_strategy)
@settings(max_examples=50)
def test_ric_accordionpanel_instantiation(instance):
    assert isinstance(instance, ric_AccordionPanel)

@given(instance=ric_MessageDialog_strategy)
@settings(max_examples=50)
def test_ric_messagedialog_instantiation(instance):
    assert isinstance(instance, ric_MessageDialog)



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_autoOpen_setter(instance):
    original = instance.autoOpen
    instance.autoOpen = original
    assert instance.autoOpen == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_minWidthResize_setter(instance):
    original = instance.minWidthResize
    instance.minWidthResize = original
    assert instance.minWidthResize == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_maxHeightResize_setter(instance):
    original = instance.maxHeightResize
    instance.maxHeightResize = original
    assert instance.maxHeightResize == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_maxWidthResize_setter(instance):
    original = instance.maxWidthResize
    instance.maxWidthResize = original
    assert instance.maxWidthResize == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_minHeightResize_setter(instance):
    original = instance.minHeightResize
    instance.minHeightResize = original
    assert instance.minHeightResize == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_modal_setter(instance):
    original = instance.modal
    instance.modal = original
    assert instance.modal == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=ric_MessageDialog_strategy)
def test_ric_messagedialog_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric_Datepicker_strategy)
@settings(max_examples=50)
def test_ric_datepicker_instantiation(instance):
    assert isinstance(instance, ric_Datepicker)



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_showButtonImage_setter(instance):
    original = instance.showButtonImage
    instance.showButtonImage = original
    assert instance.showButtonImage == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_showButtonClosePanel_setter(instance):
    original = instance.showButtonClosePanel
    instance.showButtonClosePanel = original
    assert instance.showButtonClosePanel == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_showYearMenu_setter(instance):
    original = instance.showYearMenu
    instance.showYearMenu = original
    assert instance.showYearMenu == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_showWeekOfYear_setter(instance):
    original = instance.showWeekOfYear
    instance.showWeekOfYear = original
    assert instance.showWeekOfYear == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_numberMonthsToShow_setter(instance):
    original = instance.numberMonthsToShow
    instance.numberMonthsToShow = original
    assert instance.numberMonthsToShow == original



@given(instance=ric_Datepicker_strategy)
def test_ric_datepicker_showMonthMenu_setter(instance):
    original = instance.showMonthMenu
    instance.showMonthMenu = original
    assert instance.showMonthMenu == original

@given(instance=ric_TabbedPanel_strategy)
@settings(max_examples=50)
def test_ric_tabbedpanel_instantiation(instance):
    assert isinstance(instance, ric_TabbedPanel)

@given(instance=ObjectComponent_strategy)
@settings(max_examples=50)
def test_objectcomponent_instantiation(instance):
    assert isinstance(instance, ObjectComponent)

@given(instance=BlockLevelComponent_strategy)
@settings(max_examples=50)
def test_blocklevelcomponent_instantiation(instance):
    assert isinstance(instance, BlockLevelComponent)

@given(instance=InlineComponent_strategy)
@settings(max_examples=50)
def test_inlinecomponent_instantiation(instance):
    assert isinstance(instance, InlineComponent)

@given(instance=ric_ObjectComponent_strategy)
@settings(max_examples=50)
def test_ric_objectcomponent_instantiation(instance):
    assert isinstance(instance, ric_ObjectComponent)



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original



@given(instance=ric_ObjectComponent_strategy)
def test_ric_objectcomponent_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=ric_CheckGroup_strategy)
@settings(max_examples=50)
def test_ric_checkgroup_instantiation(instance):
    assert isinstance(instance, ric_CheckGroup)



@given(instance=ric_CheckGroup_strategy)
def test_ric_checkgroup_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric_RadioGroup_strategy)
@settings(max_examples=50)
def test_ric_radiogroup_instantiation(instance):
    assert isinstance(instance, ric_RadioGroup)



@given(instance=ric_RadioGroup_strategy)
def test_ric_radiogroup_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=ric_SelectItem_strategy)
@settings(max_examples=50)
def test_ric_selectitem_instantiation(instance):
    assert isinstance(instance, ric_SelectItem)



@given(instance=ric_SelectItem_strategy)
def test_ric_selectitem_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=ric_SelectItem_strategy)
def test_ric_selectitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ric_SelectItem_strategy)
def test_ric_selectitem_itemLabel_setter(instance):
    original = instance.itemLabel
    instance.itemLabel = original
    assert instance.itemLabel == original

@given(instance=ric_InlineComponent_strategy)
@settings(max_examples=50)
def test_ric_inlinecomponent_instantiation(instance):
    assert isinstance(instance, ric_InlineComponent)



@given(instance=ric_InlineComponent_strategy)
def test_ric_inlinecomponent_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ric_BlockLevelComponent_strategy)
@settings(max_examples=50)
def test_ric_blocklevelcomponent_instantiation(instance):
    assert isinstance(instance, ric_BlockLevelComponent)

@given(instance=ric_Script_strategy)
@settings(max_examples=50)
def test_ric_script_instantiation(instance):
    assert isinstance(instance, ric_Script)



@given(instance=ric_Script_strategy)
def test_ric_script_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ric_Script_strategy)
def test_ric_script_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=ric_Script_strategy)
def test_ric_script_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=FormControl_strategy)
@settings(max_examples=50)
def test_formcontrol_instantiation(instance):
    assert isinstance(instance, FormControl)

@given(instance=ric_InputFile_strategy)
@settings(max_examples=50)
def test_ric_inputfile_instantiation(instance):
    assert isinstance(instance, ric_InputFile)



@given(instance=ric_InputFile_strategy)
def test_ric_inputfile_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original



@given(instance=ric_InputFile_strategy)
def test_ric_inputfile_charWidth_setter(instance):
    original = instance.charWidth
    instance.charWidth = original
    assert instance.charWidth == original



@given(instance=ric_InputFile_strategy)
def test_ric_inputfile_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original

@given(instance=ric_Checkbox_strategy)
@settings(max_examples=50)
def test_ric_checkbox_instantiation(instance):
    assert isinstance(instance, ric_Checkbox)



@given(instance=ric_Checkbox_strategy)
def test_ric_checkbox_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=ric_TextArea_strategy)
@settings(max_examples=50)
def test_ric_textarea_instantiation(instance):
    assert isinstance(instance, ric_TextArea)



@given(instance=ric_TextArea_strategy)
def test_ric_textarea_rols_setter(instance):
    original = instance.rols
    instance.rols = original
    assert instance.rols == original



@given(instance=ric_TextArea_strategy)
def test_ric_textarea_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original



@given(instance=ric_TextArea_strategy)
def test_ric_textarea_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=ric_Radio_strategy)
@settings(max_examples=50)
def test_ric_radio_instantiation(instance):
    assert isinstance(instance, ric_Radio)



@given(instance=ric_Radio_strategy)
def test_ric_radio_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=ric_TextField_strategy)
@settings(max_examples=50)
def test_ric_textfield_instantiation(instance):
    assert isinstance(instance, ric_TextField)



@given(instance=ric_TextField_strategy)
def test_ric_textfield_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original



@given(instance=ric_TextField_strategy)
def test_ric_textfield_charWidth_setter(instance):
    original = instance.charWidth
    instance.charWidth = original
    assert instance.charWidth == original



@given(instance=ric_TextField_strategy)
def test_ric_textfield_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=ric_TextField_strategy)
def test_ric_textfield_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=ric_Select_strategy)
@settings(max_examples=50)
def test_ric_select_instantiation(instance):
    assert isinstance(instance, ric_Select)



@given(instance=ric_Select_strategy)
def test_ric_select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ric_Select_strategy)
def test_ric_select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ric_Button_strategy)
@settings(max_examples=50)
def test_ric_button_instantiation(instance):
    assert isinstance(instance, ric_Button)



@given(instance=ric_Button_strategy)
def test_ric_button_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=ric_Button_strategy)
def test_ric_button_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=ric_Button_strategy)
def test_ric_button_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric_ValidDateConstraint_strategy)
@settings(max_examples=50)
def test_ric_validdateconstraint_instantiation(instance):
    assert isinstance(instance, ric_ValidDateConstraint)



@given(instance=ric_ValidDateConstraint_strategy)
def test_ric_validdateconstraint_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=ric_RequiredFieldConstraint_strategy)
@settings(max_examples=50)
def test_ric_requiredfieldconstraint_instantiation(instance):
    assert isinstance(instance, ric_RequiredFieldConstraint)

@given(instance=ric_NumberValueConstraint_strategy)
@settings(max_examples=50)
def test_ric_numbervalueconstraint_instantiation(instance):
    assert isinstance(instance, ric_NumberValueConstraint)

@given(instance=ric_ValueConstraint_strategy)
@settings(max_examples=50)
def test_ric_valueconstraint_instantiation(instance):
    assert isinstance(instance, ric_ValueConstraint)



@given(instance=ric_ValueConstraint_strategy)
def test_ric_valueconstraint_matchingValue_setter(instance):
    original = instance.matchingValue
    instance.matchingValue = original
    assert instance.matchingValue == original



@given(instance=ric_ValueConstraint_strategy)
def test_ric_valueconstraint_matchingOperator_setter(instance):
    original = instance.matchingOperator
    instance.matchingOperator = original
    assert instance.matchingOperator == original



@given(instance=ric_ValueConstraint_strategy)
def test_ric_valueconstraint_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original

@given(instance=EventComponent_strategy)
@settings(max_examples=50)
def test_eventcomponent_instantiation(instance):
    assert isinstance(instance, EventComponent)

@given(instance=ric_Document_strategy)
@settings(max_examples=50)
def test_ric_document_instantiation(instance):
    assert isinstance(instance, ric_Document)



@given(instance=ric_Document_strategy)
def test_ric_document_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=ric_Document_strategy)
def test_ric_document_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=ric_Document_strategy)
def test_ric_document_index_setter(instance):
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

@given(instance=ric_RichWidget_strategy)
@settings(max_examples=50)
def test_ric_richwidget_instantiation(instance):
    assert isinstance(instance, ric_RichWidget)

@given(instance=ric_Div_strategy)
@settings(max_examples=50)
def test_ric_div_instantiation(instance):
    assert isinstance(instance, ric_Div)



@given(instance=ric_Div_strategy)
def test_ric_div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric_Label_strategy)
@settings(max_examples=50)
def test_ric_label_instantiation(instance):
    assert isinstance(instance, ric_Label)



@given(instance=ric_Label_strategy)
def test_ric_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=ric_Label_strategy)
def test_ric_label_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=ric_Fieldset_strategy)
@settings(max_examples=50)
def test_ric_fieldset_instantiation(instance):
    assert isinstance(instance, ric_Fieldset)



@given(instance=ric_Fieldset_strategy)
def test_ric_fieldset_legendAlign_setter(instance):
    original = instance.legendAlign
    instance.legendAlign = original
    assert instance.legendAlign == original



@given(instance=ric_Fieldset_strategy)
def test_ric_fieldset_legend_setter(instance):
    original = instance.legend
    instance.legend = original
    assert instance.legend == original



@given(instance=ric_Fieldset_strategy)
def test_ric_fieldset_legendFormat_setter(instance):
    original = instance.legendFormat
    instance.legendFormat = original
    assert instance.legendFormat == original

@given(instance=ric_Link_strategy)
@settings(max_examples=50)
def test_ric_link_instantiation(instance):
    assert isinstance(instance, ric_Link)



@given(instance=ric_Link_strategy)
def test_ric_link_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric_List_strategy)
@settings(max_examples=50)
def test_ric_list_instantiation(instance):
    assert isinstance(instance, ric_List)

@given(instance=ric_Image_strategy)
@settings(max_examples=50)
def test_ric_image_instantiation(instance):
    assert isinstance(instance, ric_Image)



@given(instance=ric_Image_strategy)
def test_ric_image_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=ric_Image_strategy)
def test_ric_image_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=ric_Span_strategy)
@settings(max_examples=50)
def test_ric_span_instantiation(instance):
    assert isinstance(instance, ric_Span)



@given(instance=ric_Span_strategy)
def test_ric_span_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric_Form_strategy)
@settings(max_examples=50)
def test_ric_form_instantiation(instance):
    assert isinstance(instance, ric_Form)



@given(instance=ric_Form_strategy)
def test_ric_form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ric_Form_strategy)
def test_ric_form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=ric_Paragraph_strategy)
@settings(max_examples=50)
def test_ric_paragraph_instantiation(instance):
    assert isinstance(instance, ric_Paragraph)



@given(instance=ric_Paragraph_strategy)
def test_ric_paragraph_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ric_PhraseElement_strategy)
@settings(max_examples=50)
def test_ric_phraseelement_instantiation(instance):
    assert isinstance(instance, ric_PhraseElement)



@given(instance=ric_PhraseElement_strategy)
def test_ric_phraseelement_phraseType_setter(instance):
    original = instance.phraseType
    instance.phraseType = original
    assert instance.phraseType == original



@given(instance=ric_PhraseElement_strategy)
def test_ric_phraseelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=ric_LineBreak_strategy)
@settings(max_examples=50)
def test_ric_linebreak_instantiation(instance):
    assert isinstance(instance, ric_LineBreak)

@given(instance=ric_Heading_strategy)
@settings(max_examples=50)
def test_ric_heading_instantiation(instance):
    assert isinstance(instance, ric_Heading)



@given(instance=ric_Heading_strategy)
def test_ric_heading_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=ric_FormControl_strategy)
@settings(max_examples=50)
def test_ric_formcontrol_instantiation(instance):
    assert isinstance(instance, ric_FormControl)



@given(instance=ric_FormControl_strategy)
def test_ric_formcontrol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ric_FormControl_strategy)
def test_ric_formcontrol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ric_Event_strategy)
@settings(max_examples=50)
def test_ric_event_instantiation(instance):
    assert isinstance(instance, ric_Event)



@given(instance=ric_Event_strategy)
def test_ric_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ric_EventComponent_strategy)
@settings(max_examples=50)
def test_ric_eventcomponent_instantiation(instance):
    assert isinstance(instance, ric_EventComponent)

@given(instance=ric_ClassifiableComponent_strategy)
@settings(max_examples=50)
def test_ric_classifiablecomponent_instantiation(instance):
    assert isinstance(instance, ric_ClassifiableComponent)



@given(instance=ric_ClassifiableComponent_strategy)
def test_ric_classifiablecomponent_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=ric_IdentifiableComponent_strategy)
@settings(max_examples=50)
def test_ric_identifiablecomponent_instantiation(instance):
    assert isinstance(instance, ric_IdentifiableComponent)



@given(instance=ric_IdentifiableComponent_strategy)
def test_ric_identifiablecomponent_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
