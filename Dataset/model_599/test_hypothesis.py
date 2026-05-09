import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Dialog,
    presentation::MessageBox,
    presentation::Observable,
    presentation::Listener,
    presentation::ISelection,
    presentation::TextStyle,
    presentation::IElementComparer,
    presentation::GridData,
    presentation::FormAttachment,
    Layout,
    presentation::FormLayout,
    presentation::GridLayout,
    presentation::FillLayout,
    presentation::FormData,
    DocumentObject,
    presentation::Element,
    presentation::Window,
    presentation::DocumentRoot,
    Observable,
    presentation::DocumentObject,
    presentation::Document,
    presentation::DialogTray,
    presentation::IDialogBlockedHandler,
    Window,
    presentation::Dialog,
    presentation::EStringToStringMapEntry,
    presentation::DefaultCellModifier,
    presentation::DefaultLabelProvider,
    Resource,
    presentation::RGB,
    Item,
    presentation::CTabItem,
    presentation::ExpandItem,
    presentation::MenuItem,
    presentation::CoolItem,
    presentation::ControlEditor,
    presentation::Cursor,
    presentation::IContentProvider,
    Viewer,
    presentation::ContentViewer,
    presentation::Layout,
    Scrollable,
    presentation::List,
    presentation::Composite,
    AbstractListViewer,
    presentation::ListViewer,
    presentation::ComboViewer,
    presentation::IBaseLabelProvider,
    presentation::IStructuredContentProvider,
    AbstractComboBoxCellEditor,
    presentation::ComboBoxViewerCellEditor,
    presentation::ComboBoxCellEditor,
    presentation::ICellModifier,
    presentation::ColumnViewerEditor,
    DialogCellEditor,
    presentation::ColorCellEditor,
    presentation::Class,
    Canvas,
    presentation::Decorations,
    presentation::CLabel,
    TreeViewer,
    presentation::CheckboxTreeViewer,
    presentation::Collection,
    presentation::ICheckStateProvider,
    TableViewer,
    presentation::CheckboxTableViewer,
    presentation::LayoutData,
    presentation::ICellEditorValidator,
    presentation::TableItem,
    presentation::Cell,
    presentation::CellEditor,
    Widget,
    presentation::Item,
    presentation::Menu,
    presentation::Control,
    presentation::Caret,
    presentation::IME,
    presentation::ICommand,
    Control,
    presentation::Link,
    presentation::Label,
    presentation::Button,
    Composite,
    presentation::CTabFolder,
    presentation::Combo,
    presentation::Group,
    presentation::CCombo,
    presentation::ExpandBar,
    presentation::DateTime,
    presentation::Canvas,
    presentation::CoolBar,
    presentation::Browser,
    presentation::Binding,
    presentation::Accessible,
    presentation::EObject,
    presentation::TreePath,
    presentation::Widget,
    ColumnViewer,
    presentation::AbstractTreeViewer,
    presentation::AbstractTableViewer,
    StructuredViewer,
    presentation::ColumnViewer,
    presentation::AbstractListViewer,
    presentation::IBindingContext,
    presentation::AbstractDataProvider,
    CellEditor,
    presentation::DialogCellEditor,
    presentation::CheckboxCellEditor,
    presentation::AbstractComboBoxCellEditor,
    presentation::WindowManager,
    ViewerComparator,
    presentation::ViewerColumn,
    presentation::Viewer,
    presentation::URL,
    presentation::TreeItem,
    presentation::TreeColumn,
    presentation::Tree,
    presentation::TrayDialog,
    presentation::TrayItem,
    presentation::Tray,
    presentation::Tracker,
    presentation::ToolTip,
    presentation::ToolItem,
    presentation::ToolBar,
    TrayDialog,
    presentation::TitleAreaDialog,
    presentation::TextCellEditor,
    presentation::Text,
    AbstractTableViewer,
    presentation::TableViewer,
    AbstractTreeViewer,
    presentation::TreeViewer,
    presentation::TableTreeViewer,
    presentation::TableTree,
    ViewerColumn,
    presentation::TableViewerColumn,
    ControlEditor,
    presentation::TableEditor,
    presentation::TableColumn,
    presentation::Table,
    presentation::TabFolder,
    TextStyle,
    presentation::TabItem,
    presentation::StyledTextContent,
    presentation::StyleRange,
    presentation::StyledText,
    presentation::ViewerSorter,
    presentation::ViewerComparator,
    ContentViewer,
    presentation::StructuredViewer,
    presentation::StackLayout,
    presentation::ViewerFilter,
    presentation::Spinner,
    Decorations,
    presentation::Shell,
    presentation::Slider,
    presentation::ScrollBar,
    presentation::Scale,
    presentation::Scrollable,
    presentation::Sash,
    presentation::SashForm,
    presentation::RowLayout,
    presentation::RowData,
    presentation::Resource,
    presentation::ProgressBar,
    AbstractDataProvider,
    presentation::ObjectDataProvider,
    presentation::XMLDataProvider,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dialog_is_not_abstract():
    assert not inspect.isabstract(Dialog)


def test_dialog_constructor_exists():
    assert callable(Dialog.__init__)


def test_dialog_constructor_args():
    sig = inspect.signature(Dialog.__init__)
    params = list(sig.parameters.keys())



def test_presentation::messagebox_is_not_abstract():
    assert not inspect.isabstract(presentation::MessageBox)


def test_presentation::messagebox_constructor_exists():
    assert callable(presentation::MessageBox.__init__)


def test_presentation::messagebox_constructor_args():
    sig = inspect.signature(presentation::MessageBox.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_presentation::messagebox_has_message():
    assert hasattr(presentation::MessageBox, "message")
    descriptor = None
    for klass in presentation::MessageBox.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_presentation::observable_is_not_abstract():
    assert not inspect.isabstract(presentation::Observable)


def test_presentation::observable_constructor_exists():
    assert callable(presentation::Observable.__init__)


def test_presentation::observable_constructor_args():
    sig = inspect.signature(presentation::Observable.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::observable_has_mixed():
    assert hasattr(presentation::Observable, "mixed")
    descriptor = None
    for klass in presentation::Observable.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::listener_is_not_abstract():
    assert not inspect.isabstract(presentation::Listener)


def test_presentation::listener_constructor_exists():
    assert callable(presentation::Listener.__init__)


def test_presentation::listener_constructor_args():
    sig = inspect.signature(presentation::Listener.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::listener_has_mixed():
    assert hasattr(presentation::Listener, "mixed")
    descriptor = None
    for klass in presentation::Listener.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::iselection_is_not_abstract():
    assert not inspect.isabstract(presentation::ISelection)


def test_presentation::iselection_constructor_exists():
    assert callable(presentation::ISelection.__init__)


def test_presentation::iselection_constructor_args():
    sig = inspect.signature(presentation::ISelection.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::iselection_has_mixed():
    assert hasattr(presentation::ISelection, "mixed")
    descriptor = None
    for klass in presentation::ISelection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::textstyle_is_not_abstract():
    assert not inspect.isabstract(presentation::TextStyle)


def test_presentation::textstyle_constructor_exists():
    assert callable(presentation::TextStyle.__init__)


def test_presentation::textstyle_constructor_args():
    sig = inspect.signature(presentation::TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::textstyle_has_mixed():
    assert hasattr(presentation::TextStyle, "mixed")
    descriptor = None
    for klass in presentation::TextStyle.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::ielementcomparer_is_not_abstract():
    assert not inspect.isabstract(presentation::IElementComparer)


def test_presentation::ielementcomparer_constructor_exists():
    assert callable(presentation::IElementComparer.__init__)


def test_presentation::ielementcomparer_constructor_args():
    sig = inspect.signature(presentation::IElementComparer.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::ielementcomparer_has_mixed():
    assert hasattr(presentation::IElementComparer, "mixed")
    descriptor = None
    for klass in presentation::IElementComparer.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::griddata_is_not_abstract():
    assert not inspect.isabstract(presentation::GridData)


def test_presentation::griddata_constructor_exists():
    assert callable(presentation::GridData.__init__)


def test_presentation::griddata_constructor_args():
    sig = inspect.signature(presentation::GridData.__init__)
    params = list(sig.parameters.keys())
    assert "exclude" in params, "Missing parameter 'exclude'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "minimumHeight" in params, "Missing parameter 'minimumHeight'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"
    assert "minimumWidth" in params, "Missing parameter 'minimumWidth'"
    assert "heightHint" in params, "Missing parameter 'heightHint'"
    assert "verticalIndent" in params, "Missing parameter 'verticalIndent'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"
    assert "widthHint" in params, "Missing parameter 'widthHint'"

def test_presentation::griddata_has_exclude():
    assert hasattr(presentation::GridData, "exclude")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "exclude" in klass.__dict__:
            descriptor = klass.__dict__["exclude"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_horizontalIndent():
    assert hasattr(presentation::GridData, "horizontalIndent")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "horizontalIndent" in klass.__dict__:
            descriptor = klass.__dict__["horizontalIndent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_mixed():
    assert hasattr(presentation::GridData, "mixed")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_verticalAlignment():
    assert hasattr(presentation::GridData, "verticalAlignment")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_grabExcessVerticalSpace():
    assert hasattr(presentation::GridData, "grabExcessVerticalSpace")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "grabExcessVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_minimumHeight():
    assert hasattr(presentation::GridData, "minimumHeight")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "minimumHeight" in klass.__dict__:
            descriptor = klass.__dict__["minimumHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_horizontalAlignment():
    assert hasattr(presentation::GridData, "horizontalAlignment")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_horizontalSpan():
    assert hasattr(presentation::GridData, "horizontalSpan")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "horizontalSpan" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpan"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_minimumWidth():
    assert hasattr(presentation::GridData, "minimumWidth")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "minimumWidth" in klass.__dict__:
            descriptor = klass.__dict__["minimumWidth"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_heightHint():
    assert hasattr(presentation::GridData, "heightHint")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "heightHint" in klass.__dict__:
            descriptor = klass.__dict__["heightHint"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_verticalIndent():
    assert hasattr(presentation::GridData, "verticalIndent")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "verticalIndent" in klass.__dict__:
            descriptor = klass.__dict__["verticalIndent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_verticalSpan():
    assert hasattr(presentation::GridData, "verticalSpan")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "verticalSpan" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpan"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_grabExcessHorizontalSpace():
    assert hasattr(presentation::GridData, "grabExcessHorizontalSpace")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "grabExcessHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_presentation::griddata_has_widthHint():
    assert hasattr(presentation::GridData, "widthHint")
    descriptor = None
    for klass in presentation::GridData.__mro__:
        if "widthHint" in klass.__dict__:
            descriptor = klass.__dict__["widthHint"]
            break
    assert isinstance(descriptor, property)



def test_presentation::formattachment_is_not_abstract():
    assert not inspect.isabstract(presentation::FormAttachment)


def test_presentation::formattachment_constructor_exists():
    assert callable(presentation::FormAttachment.__init__)


def test_presentation::formattachment_constructor_args():
    sig = inspect.signature(presentation::FormAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "numerator" in params, "Missing parameter 'numerator'"
    assert "group" in params, "Missing parameter 'group'"
    assert "offset" in params, "Missing parameter 'offset'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_presentation::formattachment_has_mixed():
    assert hasattr(presentation::FormAttachment, "mixed")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formattachment_has_alignment():
    assert hasattr(presentation::FormAttachment, "alignment")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formattachment_has_numerator():
    assert hasattr(presentation::FormAttachment, "numerator")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "numerator" in klass.__dict__:
            descriptor = klass.__dict__["numerator"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formattachment_has_group():
    assert hasattr(presentation::FormAttachment, "group")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formattachment_has_offset():
    assert hasattr(presentation::FormAttachment, "offset")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formattachment_has_denominator():
    assert hasattr(presentation::FormAttachment, "denominator")
    descriptor = None
    for klass in presentation::FormAttachment.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_presentation::formlayout_is_not_abstract():
    assert not inspect.isabstract(presentation::FormLayout)


def test_presentation::formlayout_constructor_exists():
    assert callable(presentation::FormLayout.__init__)


def test_presentation::formlayout_constructor_args():
    sig = inspect.signature(presentation::FormLayout.__init__)
    params = list(sig.parameters.keys())
    assert "marginLeft" in params, "Missing parameter 'marginLeft'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "marginBottom" in params, "Missing parameter 'marginBottom'"
    assert "marginRight" in params, "Missing parameter 'marginRight'"
    assert "marginTop" in params, "Missing parameter 'marginTop'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"

def test_presentation::formlayout_has_marginLeft():
    assert hasattr(presentation::FormLayout, "marginLeft")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginLeft" in klass.__dict__:
            descriptor = klass.__dict__["marginLeft"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_marginHeight():
    assert hasattr(presentation::FormLayout, "marginHeight")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_spacing():
    assert hasattr(presentation::FormLayout, "spacing")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_marginBottom():
    assert hasattr(presentation::FormLayout, "marginBottom")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginBottom" in klass.__dict__:
            descriptor = klass.__dict__["marginBottom"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_marginRight():
    assert hasattr(presentation::FormLayout, "marginRight")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginRight" in klass.__dict__:
            descriptor = klass.__dict__["marginRight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_marginTop():
    assert hasattr(presentation::FormLayout, "marginTop")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginTop" in klass.__dict__:
            descriptor = klass.__dict__["marginTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formlayout_has_marginWidth():
    assert hasattr(presentation::FormLayout, "marginWidth")
    descriptor = None
    for klass in presentation::FormLayout.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)



def test_presentation::gridlayout_is_not_abstract():
    assert not inspect.isabstract(presentation::GridLayout)


def test_presentation::gridlayout_constructor_exists():
    assert callable(presentation::GridLayout.__init__)


def test_presentation::gridlayout_constructor_args():
    sig = inspect.signature(presentation::GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "marginLeft" in params, "Missing parameter 'marginLeft'"
    assert "makeColumnsEqualWidth" in params, "Missing parameter 'makeColumnsEqualWidth'"
    assert "numColumns" in params, "Missing parameter 'numColumns'"
    assert "marginBottom" in params, "Missing parameter 'marginBottom'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "marginTop" in params, "Missing parameter 'marginTop'"
    assert "marginRight" in params, "Missing parameter 'marginRight'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"

def test_presentation::gridlayout_has_marginLeft():
    assert hasattr(presentation::GridLayout, "marginLeft")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginLeft" in klass.__dict__:
            descriptor = klass.__dict__["marginLeft"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_makeColumnsEqualWidth():
    assert hasattr(presentation::GridLayout, "makeColumnsEqualWidth")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "makeColumnsEqualWidth" in klass.__dict__:
            descriptor = klass.__dict__["makeColumnsEqualWidth"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_numColumns():
    assert hasattr(presentation::GridLayout, "numColumns")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "numColumns" in klass.__dict__:
            descriptor = klass.__dict__["numColumns"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_marginBottom():
    assert hasattr(presentation::GridLayout, "marginBottom")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginBottom" in klass.__dict__:
            descriptor = klass.__dict__["marginBottom"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_marginWidth():
    assert hasattr(presentation::GridLayout, "marginWidth")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_marginTop():
    assert hasattr(presentation::GridLayout, "marginTop")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginTop" in klass.__dict__:
            descriptor = klass.__dict__["marginTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_marginRight():
    assert hasattr(presentation::GridLayout, "marginRight")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginRight" in klass.__dict__:
            descriptor = klass.__dict__["marginRight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_verticalSpacing():
    assert hasattr(presentation::GridLayout, "verticalSpacing")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_marginHeight():
    assert hasattr(presentation::GridLayout, "marginHeight")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::gridlayout_has_horizontalSpacing():
    assert hasattr(presentation::GridLayout, "horizontalSpacing")
    descriptor = None
    for klass in presentation::GridLayout.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)



def test_presentation::filllayout_is_not_abstract():
    assert not inspect.isabstract(presentation::FillLayout)


def test_presentation::filllayout_constructor_exists():
    assert callable(presentation::FillLayout.__init__)


def test_presentation::filllayout_constructor_args():
    sig = inspect.signature(presentation::FillLayout.__init__)
    params = list(sig.parameters.keys())
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "type" in params, "Missing parameter 'type'"
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"

def test_presentation::filllayout_has_marginHeight():
    assert hasattr(presentation::FillLayout, "marginHeight")
    descriptor = None
    for klass in presentation::FillLayout.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::filllayout_has_type():
    assert hasattr(presentation::FillLayout, "type")
    descriptor = None
    for klass in presentation::FillLayout.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation::filllayout_has_spacing():
    assert hasattr(presentation::FillLayout, "spacing")
    descriptor = None
    for klass in presentation::FillLayout.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_presentation::filllayout_has_marginWidth():
    assert hasattr(presentation::FillLayout, "marginWidth")
    descriptor = None
    for klass in presentation::FillLayout.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)



def test_presentation::formdata_is_not_abstract():
    assert not inspect.isabstract(presentation::FormData)


def test_presentation::formdata_constructor_exists():
    assert callable(presentation::FormData.__init__)


def test_presentation::formdata_constructor_args():
    sig = inspect.signature(presentation::FormData.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::formdata_has_height():
    assert hasattr(presentation::FormData, "height")
    descriptor = None
    for klass in presentation::FormData.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formdata_has_width():
    assert hasattr(presentation::FormData, "width")
    descriptor = None
    for klass in presentation::FormData.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formdata_has_group():
    assert hasattr(presentation::FormData, "group")
    descriptor = None
    for klass in presentation::FormData.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::formdata_has_mixed():
    assert hasattr(presentation::FormData, "mixed")
    descriptor = None
    for klass in presentation::FormData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_documentobject_is_not_abstract():
    assert not inspect.isabstract(DocumentObject)


def test_documentobject_constructor_exists():
    assert callable(DocumentObject.__init__)


def test_documentobject_constructor_args():
    sig = inspect.signature(DocumentObject.__init__)
    params = list(sig.parameters.keys())



def test_presentation::element_is_not_abstract():
    assert not inspect.isabstract(presentation::Element)


def test_presentation::element_constructor_exists():
    assert callable(presentation::Element.__init__)


def test_presentation::element_constructor_args():
    sig = inspect.signature(presentation::Element.__init__)
    params = list(sig.parameters.keys())



def test_presentation::window_is_not_abstract():
    assert not inspect.isabstract(presentation::Window)


def test_presentation::window_constructor_exists():
    assert callable(presentation::Window.__init__)


def test_presentation::window_constructor_args():
    sig = inspect.signature(presentation::Window.__init__)
    params = list(sig.parameters.keys())
    assert "blockOnOpen" in params, "Missing parameter 'blockOnOpen'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::window_has_blockOnOpen():
    assert hasattr(presentation::Window, "blockOnOpen")
    descriptor = None
    for klass in presentation::Window.__mro__:
        if "blockOnOpen" in klass.__dict__:
            descriptor = klass.__dict__["blockOnOpen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::window_has_group():
    assert hasattr(presentation::Window, "group")
    descriptor = None
    for klass in presentation::Window.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::window_has_mixed():
    assert hasattr(presentation::Window, "mixed")
    descriptor = None
    for klass in presentation::Window.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::documentroot_is_not_abstract():
    assert not inspect.isabstract(presentation::DocumentRoot)


def test_presentation::documentroot_constructor_exists():
    assert callable(presentation::DocumentRoot.__init__)


def test_presentation::documentroot_constructor_args():
    sig = inspect.signature(presentation::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::documentroot_has_mixed():
    assert hasattr(presentation::DocumentRoot, "mixed")
    descriptor = None
    for klass in presentation::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_observable_is_not_abstract():
    assert not inspect.isabstract(Observable)


def test_observable_constructor_exists():
    assert callable(Observable.__init__)


def test_observable_constructor_args():
    sig = inspect.signature(Observable.__init__)
    params = list(sig.parameters.keys())



def test_presentation::documentobject_is_not_abstract():
    assert not inspect.isabstract(presentation::DocumentObject)


def test_presentation::documentobject_constructor_exists():
    assert callable(presentation::DocumentObject.__init__)


def test_presentation::documentobject_constructor_args():
    sig = inspect.signature(presentation::DocumentObject.__init__)
    params = list(sig.parameters.keys())



def test_presentation::document_is_not_abstract():
    assert not inspect.isabstract(presentation::Document)


def test_presentation::document_constructor_exists():
    assert callable(presentation::Document.__init__)


def test_presentation::document_constructor_args():
    sig = inspect.signature(presentation::Document.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::document_has_mixed():
    assert hasattr(presentation::Document, "mixed")
    descriptor = None
    for klass in presentation::Document.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::dialogtray_is_not_abstract():
    assert not inspect.isabstract(presentation::DialogTray)


def test_presentation::dialogtray_constructor_exists():
    assert callable(presentation::DialogTray.__init__)


def test_presentation::dialogtray_constructor_args():
    sig = inspect.signature(presentation::DialogTray.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::dialogtray_has_mixed():
    assert hasattr(presentation::DialogTray, "mixed")
    descriptor = None
    for klass in presentation::DialogTray.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::idialogblockedhandler_is_not_abstract():
    assert not inspect.isabstract(presentation::IDialogBlockedHandler)


def test_presentation::idialogblockedhandler_constructor_exists():
    assert callable(presentation::IDialogBlockedHandler.__init__)


def test_presentation::idialogblockedhandler_constructor_args():
    sig = inspect.signature(presentation::IDialogBlockedHandler.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::idialogblockedhandler_has_mixed():
    assert hasattr(presentation::IDialogBlockedHandler, "mixed")
    descriptor = None
    for klass in presentation::IDialogBlockedHandler.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_window_is_not_abstract():
    assert not inspect.isabstract(Window)


def test_window_constructor_exists():
    assert callable(Window.__init__)


def test_window_constructor_args():
    sig = inspect.signature(Window.__init__)
    params = list(sig.parameters.keys())



def test_presentation::dialog_is_not_abstract():
    assert not inspect.isabstract(presentation::Dialog)


def test_presentation::dialog_constructor_exists():
    assert callable(presentation::Dialog.__init__)


def test_presentation::dialog_constructor_args():
    sig = inspect.signature(presentation::Dialog.__init__)
    params = list(sig.parameters.keys())
    assert "group1" in params, "Missing parameter 'group1'"

def test_presentation::dialog_has_group1():
    assert hasattr(presentation::Dialog, "group1")
    descriptor = None
    for klass in presentation::Dialog.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)



def test_presentation::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(presentation::EStringToStringMapEntry)


def test_presentation::estringtostringmapentry_constructor_exists():
    assert callable(presentation::EStringToStringMapEntry.__init__)


def test_presentation::estringtostringmapentry_constructor_args():
    sig = inspect.signature(presentation::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_presentation::defaultcellmodifier_is_not_abstract():
    assert not inspect.isabstract(presentation::DefaultCellModifier)


def test_presentation::defaultcellmodifier_constructor_exists():
    assert callable(presentation::DefaultCellModifier.__init__)


def test_presentation::defaultcellmodifier_constructor_args():
    sig = inspect.signature(presentation::DefaultCellModifier.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::defaultcellmodifier_has_mixed():
    assert hasattr(presentation::DefaultCellModifier, "mixed")
    descriptor = None
    for klass in presentation::DefaultCellModifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::defaultlabelprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::DefaultLabelProvider)


def test_presentation::defaultlabelprovider_constructor_exists():
    assert callable(presentation::DefaultLabelProvider.__init__)


def test_presentation::defaultlabelprovider_constructor_args():
    sig = inspect.signature(presentation::DefaultLabelProvider.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::defaultlabelprovider_has_mixed():
    assert hasattr(presentation::DefaultLabelProvider, "mixed")
    descriptor = None
    for klass in presentation::DefaultLabelProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_presentation::rgb_is_not_abstract():
    assert not inspect.isabstract(presentation::RGB)


def test_presentation::rgb_constructor_exists():
    assert callable(presentation::RGB.__init__)


def test_presentation::rgb_constructor_args():
    sig = inspect.signature(presentation::RGB.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::rgb_has_mixed():
    assert hasattr(presentation::RGB, "mixed")
    descriptor = None
    for klass in presentation::RGB.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_presentation::ctabitem_is_not_abstract():
    assert not inspect.isabstract(presentation::CTabItem)


def test_presentation::ctabitem_constructor_exists():
    assert callable(presentation::CTabItem.__init__)


def test_presentation::ctabitem_constructor_args():
    sig = inspect.signature(presentation::CTabItem.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "showClose" in params, "Missing parameter 'showClose'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "disabledImage" in params, "Missing parameter 'disabledImage'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "font" in params, "Missing parameter 'font'"

def test_presentation::ctabitem_has_group():
    assert hasattr(presentation::CTabItem, "group")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabitem_has_showClose():
    assert hasattr(presentation::CTabItem, "showClose")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "showClose" in klass.__dict__:
            descriptor = klass.__dict__["showClose"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabitem_has_bounds():
    assert hasattr(presentation::CTabItem, "bounds")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabitem_has_disabledImage():
    assert hasattr(presentation::CTabItem, "disabledImage")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "disabledImage" in klass.__dict__:
            descriptor = klass.__dict__["disabledImage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabitem_has_toolTipText():
    assert hasattr(presentation::CTabItem, "toolTipText")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabitem_has_font():
    assert hasattr(presentation::CTabItem, "font")
    descriptor = None
    for klass in presentation::CTabItem.__mro__:
        if "font" in klass.__dict__:
            descriptor = klass.__dict__["font"]
            break
    assert isinstance(descriptor, property)



def test_presentation::expanditem_is_not_abstract():
    assert not inspect.isabstract(presentation::ExpandItem)


def test_presentation::expanditem_constructor_exists():
    assert callable(presentation::ExpandItem.__init__)


def test_presentation::expanditem_constructor_args():
    sig = inspect.signature(presentation::ExpandItem.__init__)
    params = list(sig.parameters.keys())
    assert "expanded" in params, "Missing parameter 'expanded'"
    assert "group" in params, "Missing parameter 'group'"
    assert "height" in params, "Missing parameter 'height'"

def test_presentation::expanditem_has_expanded():
    assert hasattr(presentation::ExpandItem, "expanded")
    descriptor = None
    for klass in presentation::ExpandItem.__mro__:
        if "expanded" in klass.__dict__:
            descriptor = klass.__dict__["expanded"]
            break
    assert isinstance(descriptor, property)

def test_presentation::expanditem_has_group():
    assert hasattr(presentation::ExpandItem, "group")
    descriptor = None
    for klass in presentation::ExpandItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::expanditem_has_height():
    assert hasattr(presentation::ExpandItem, "height")
    descriptor = None
    for klass in presentation::ExpandItem.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_presentation::menuitem_is_not_abstract():
    assert not inspect.isabstract(presentation::MenuItem)


def test_presentation::menuitem_constructor_exists():
    assert callable(presentation::MenuItem.__init__)


def test_presentation::menuitem_constructor_args():
    sig = inspect.signature(presentation::MenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "accelerator" in params, "Missing parameter 'accelerator'"
    assert "group" in params, "Missing parameter 'group'"
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_presentation::menuitem_has_selection():
    assert hasattr(presentation::MenuItem, "selection")
    descriptor = None
    for klass in presentation::MenuItem.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menuitem_has_accelerator():
    assert hasattr(presentation::MenuItem, "accelerator")
    descriptor = None
    for klass in presentation::MenuItem.__mro__:
        if "accelerator" in klass.__dict__:
            descriptor = klass.__dict__["accelerator"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menuitem_has_group():
    assert hasattr(presentation::MenuItem, "group")
    descriptor = None
    for klass in presentation::MenuItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menuitem_has_enabled():
    assert hasattr(presentation::MenuItem, "enabled")
    descriptor = None
    for klass in presentation::MenuItem.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_presentation::coolitem_is_not_abstract():
    assert not inspect.isabstract(presentation::CoolItem)


def test_presentation::coolitem_constructor_exists():
    assert callable(presentation::CoolItem.__init__)


def test_presentation::coolitem_constructor_args():
    sig = inspect.signature(presentation::CoolItem.__init__)
    params = list(sig.parameters.keys())
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "group" in params, "Missing parameter 'group'"
    assert "size" in params, "Missing parameter 'size'"
    assert "preferredSize" in params, "Missing parameter 'preferredSize'"
    assert "minimumSize" in params, "Missing parameter 'minimumSize'"

def test_presentation::coolitem_has_bounds():
    assert hasattr(presentation::CoolItem, "bounds")
    descriptor = None
    for klass in presentation::CoolItem.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolitem_has_group():
    assert hasattr(presentation::CoolItem, "group")
    descriptor = None
    for klass in presentation::CoolItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolitem_has_size():
    assert hasattr(presentation::CoolItem, "size")
    descriptor = None
    for klass in presentation::CoolItem.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolitem_has_preferredSize():
    assert hasattr(presentation::CoolItem, "preferredSize")
    descriptor = None
    for klass in presentation::CoolItem.__mro__:
        if "preferredSize" in klass.__dict__:
            descriptor = klass.__dict__["preferredSize"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolitem_has_minimumSize():
    assert hasattr(presentation::CoolItem, "minimumSize")
    descriptor = None
    for klass in presentation::CoolItem.__mro__:
        if "minimumSize" in klass.__dict__:
            descriptor = klass.__dict__["minimumSize"]
            break
    assert isinstance(descriptor, property)



def test_presentation::controleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::ControlEditor)


def test_presentation::controleditor_constructor_exists():
    assert callable(presentation::ControlEditor.__init__)


def test_presentation::controleditor_constructor_args():
    sig = inspect.signature(presentation::ControlEditor.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "minimumHeight" in params, "Missing parameter 'minimumHeight'"
    assert "group" in params, "Missing parameter 'group'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "grabHorizontal" in params, "Missing parameter 'grabHorizontal'"
    assert "grabVertical" in params, "Missing parameter 'grabVertical'"
    assert "minimumWidth" in params, "Missing parameter 'minimumWidth'"

def test_presentation::controleditor_has_mixed():
    assert hasattr(presentation::ControlEditor, "mixed")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_horizontalAlignment():
    assert hasattr(presentation::ControlEditor, "horizontalAlignment")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_minimumHeight():
    assert hasattr(presentation::ControlEditor, "minimumHeight")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "minimumHeight" in klass.__dict__:
            descriptor = klass.__dict__["minimumHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_group():
    assert hasattr(presentation::ControlEditor, "group")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_verticalAlignment():
    assert hasattr(presentation::ControlEditor, "verticalAlignment")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_grabHorizontal():
    assert hasattr(presentation::ControlEditor, "grabHorizontal")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "grabHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["grabHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_grabVertical():
    assert hasattr(presentation::ControlEditor, "grabVertical")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "grabVertical" in klass.__dict__:
            descriptor = klass.__dict__["grabVertical"]
            break
    assert isinstance(descriptor, property)

def test_presentation::controleditor_has_minimumWidth():
    assert hasattr(presentation::ControlEditor, "minimumWidth")
    descriptor = None
    for klass in presentation::ControlEditor.__mro__:
        if "minimumWidth" in klass.__dict__:
            descriptor = klass.__dict__["minimumWidth"]
            break
    assert isinstance(descriptor, property)



def test_presentation::cursor_is_not_abstract():
    assert not inspect.isabstract(presentation::Cursor)


def test_presentation::cursor_constructor_exists():
    assert callable(presentation::Cursor.__init__)


def test_presentation::cursor_constructor_args():
    sig = inspect.signature(presentation::Cursor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::icontentprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::IContentProvider)


def test_presentation::icontentprovider_constructor_exists():
    assert callable(presentation::IContentProvider.__init__)


def test_presentation::icontentprovider_constructor_args():
    sig = inspect.signature(presentation::IContentProvider.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::icontentprovider_has_mixed():
    assert hasattr(presentation::IContentProvider, "mixed")
    descriptor = None
    for klass in presentation::IContentProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_viewer_is_not_abstract():
    assert not inspect.isabstract(Viewer)


def test_viewer_constructor_exists():
    assert callable(Viewer.__init__)


def test_viewer_constructor_args():
    sig = inspect.signature(Viewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::contentviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::ContentViewer)


def test_presentation::contentviewer_constructor_exists():
    assert callable(presentation::ContentViewer.__init__)


def test_presentation::contentviewer_constructor_args():
    sig = inspect.signature(presentation::ContentViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group1" in params, "Missing parameter 'group1'"

def test_presentation::contentviewer_has_group1():
    assert hasattr(presentation::ContentViewer, "group1")
    descriptor = None
    for klass in presentation::ContentViewer.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)



def test_presentation::layout_is_not_abstract():
    assert not inspect.isabstract(presentation::Layout)


def test_presentation::layout_constructor_exists():
    assert callable(presentation::Layout.__init__)


def test_presentation::layout_constructor_args():
    sig = inspect.signature(presentation::Layout.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::layout_has_mixed():
    assert hasattr(presentation::Layout, "mixed")
    descriptor = None
    for klass in presentation::Layout.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_scrollable_is_not_abstract():
    assert not inspect.isabstract(Scrollable)


def test_scrollable_constructor_exists():
    assert callable(Scrollable.__init__)


def test_scrollable_constructor_args():
    sig = inspect.signature(Scrollable.__init__)
    params = list(sig.parameters.keys())



def test_presentation::list_is_not_abstract():
    assert not inspect.isabstract(presentation::List)


def test_presentation::list_constructor_exists():
    assert callable(presentation::List.__init__)


def test_presentation::list_constructor_args():
    sig = inspect.signature(presentation::List.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "selectionIndices" in params, "Missing parameter 'selectionIndices'"
    assert "items" in params, "Missing parameter 'items'"
    assert "topIndex" in params, "Missing parameter 'topIndex'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_presentation::list_has_selection():
    assert hasattr(presentation::List, "selection")
    descriptor = None
    for klass in presentation::List.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::list_has_selectionIndices():
    assert hasattr(presentation::List, "selectionIndices")
    descriptor = None
    for klass in presentation::List.__mro__:
        if "selectionIndices" in klass.__dict__:
            descriptor = klass.__dict__["selectionIndices"]
            break
    assert isinstance(descriptor, property)

def test_presentation::list_has_items():
    assert hasattr(presentation::List, "items")
    descriptor = None
    for klass in presentation::List.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_presentation::list_has_topIndex():
    assert hasattr(presentation::List, "topIndex")
    descriptor = None
    for klass in presentation::List.__mro__:
        if "topIndex" in klass.__dict__:
            descriptor = klass.__dict__["topIndex"]
            break
    assert isinstance(descriptor, property)

def test_presentation::list_has_group2():
    assert hasattr(presentation::List, "group2")
    descriptor = None
    for klass in presentation::List.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_presentation::composite_is_not_abstract():
    assert not inspect.isabstract(presentation::Composite)


def test_presentation::composite_constructor_exists():
    assert callable(presentation::Composite.__init__)


def test_presentation::composite_constructor_args():
    sig = inspect.signature(presentation::Composite.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "backgroundMode" in params, "Missing parameter 'backgroundMode'"
    assert "layoutDeferred" in params, "Missing parameter 'layoutDeferred'"

def test_presentation::composite_has_group2():
    assert hasattr(presentation::Composite, "group2")
    descriptor = None
    for klass in presentation::Composite.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_presentation::composite_has_backgroundMode():
    assert hasattr(presentation::Composite, "backgroundMode")
    descriptor = None
    for klass in presentation::Composite.__mro__:
        if "backgroundMode" in klass.__dict__:
            descriptor = klass.__dict__["backgroundMode"]
            break
    assert isinstance(descriptor, property)

def test_presentation::composite_has_layoutDeferred():
    assert hasattr(presentation::Composite, "layoutDeferred")
    descriptor = None
    for klass in presentation::Composite.__mro__:
        if "layoutDeferred" in klass.__dict__:
            descriptor = klass.__dict__["layoutDeferred"]
            break
    assert isinstance(descriptor, property)



def test_abstractlistviewer_is_not_abstract():
    assert not inspect.isabstract(AbstractListViewer)


def test_abstractlistviewer_constructor_exists():
    assert callable(AbstractListViewer.__init__)


def test_abstractlistviewer_constructor_args():
    sig = inspect.signature(AbstractListViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::listviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::ListViewer)


def test_presentation::listviewer_constructor_exists():
    assert callable(presentation::ListViewer.__init__)


def test_presentation::listviewer_constructor_args():
    sig = inspect.signature(presentation::ListViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::listviewer_has_group3():
    assert hasattr(presentation::ListViewer, "group3")
    descriptor = None
    for klass in presentation::ListViewer.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_presentation::comboviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::ComboViewer)


def test_presentation::comboviewer_constructor_exists():
    assert callable(presentation::ComboViewer.__init__)


def test_presentation::comboviewer_constructor_args():
    sig = inspect.signature(presentation::ComboViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::ibaselabelprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::IBaseLabelProvider)


def test_presentation::ibaselabelprovider_constructor_exists():
    assert callable(presentation::IBaseLabelProvider.__init__)


def test_presentation::ibaselabelprovider_constructor_args():
    sig = inspect.signature(presentation::IBaseLabelProvider.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::ibaselabelprovider_has_mixed():
    assert hasattr(presentation::IBaseLabelProvider, "mixed")
    descriptor = None
    for klass in presentation::IBaseLabelProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::istructuredcontentprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::IStructuredContentProvider)


def test_presentation::istructuredcontentprovider_constructor_exists():
    assert callable(presentation::IStructuredContentProvider.__init__)


def test_presentation::istructuredcontentprovider_constructor_args():
    sig = inspect.signature(presentation::IStructuredContentProvider.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::istructuredcontentprovider_has_mixed():
    assert hasattr(presentation::IStructuredContentProvider, "mixed")
    descriptor = None
    for klass in presentation::IStructuredContentProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_abstractcomboboxcelleditor_is_not_abstract():
    assert not inspect.isabstract(AbstractComboBoxCellEditor)


def test_abstractcomboboxcelleditor_constructor_exists():
    assert callable(AbstractComboBoxCellEditor.__init__)


def test_abstractcomboboxcelleditor_constructor_args():
    sig = inspect.signature(AbstractComboBoxCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::comboboxviewercelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::ComboBoxViewerCellEditor)


def test_presentation::comboboxviewercelleditor_constructor_exists():
    assert callable(presentation::ComboBoxViewerCellEditor.__init__)


def test_presentation::comboboxviewercelleditor_constructor_args():
    sig = inspect.signature(presentation::ComboBoxViewerCellEditor.__init__)
    params = list(sig.parameters.keys())
    assert "group1" in params, "Missing parameter 'group1'"

def test_presentation::comboboxviewercelleditor_has_group1():
    assert hasattr(presentation::ComboBoxViewerCellEditor, "group1")
    descriptor = None
    for klass in presentation::ComboBoxViewerCellEditor.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)



def test_presentation::comboboxcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::ComboBoxCellEditor)


def test_presentation::comboboxcelleditor_constructor_exists():
    assert callable(presentation::ComboBoxCellEditor.__init__)


def test_presentation::comboboxcelleditor_constructor_args():
    sig = inspect.signature(presentation::ComboBoxCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::icellmodifier_is_not_abstract():
    assert not inspect.isabstract(presentation::ICellModifier)


def test_presentation::icellmodifier_constructor_exists():
    assert callable(presentation::ICellModifier.__init__)


def test_presentation::icellmodifier_constructor_args():
    sig = inspect.signature(presentation::ICellModifier.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::icellmodifier_has_mixed():
    assert hasattr(presentation::ICellModifier, "mixed")
    descriptor = None
    for klass in presentation::ICellModifier.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::columnviewereditor_is_not_abstract():
    assert not inspect.isabstract(presentation::ColumnViewerEditor)


def test_presentation::columnviewereditor_constructor_exists():
    assert callable(presentation::ColumnViewerEditor.__init__)


def test_presentation::columnviewereditor_constructor_args():
    sig = inspect.signature(presentation::ColumnViewerEditor.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::columnviewereditor_has_mixed():
    assert hasattr(presentation::ColumnViewerEditor, "mixed")
    descriptor = None
    for klass in presentation::ColumnViewerEditor.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_dialogcelleditor_is_not_abstract():
    assert not inspect.isabstract(DialogCellEditor)


def test_dialogcelleditor_constructor_exists():
    assert callable(DialogCellEditor.__init__)


def test_dialogcelleditor_constructor_args():
    sig = inspect.signature(DialogCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::colorcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::ColorCellEditor)


def test_presentation::colorcelleditor_constructor_exists():
    assert callable(presentation::ColorCellEditor.__init__)


def test_presentation::colorcelleditor_constructor_args():
    sig = inspect.signature(presentation::ColorCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::class_is_not_abstract():
    assert not inspect.isabstract(presentation::Class)


def test_presentation::class_constructor_exists():
    assert callable(presentation::Class.__init__)


def test_presentation::class_constructor_args():
    sig = inspect.signature(presentation::Class.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::class_has_mixed():
    assert hasattr(presentation::Class, "mixed")
    descriptor = None
    for klass in presentation::Class.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_presentation::decorations_is_not_abstract():
    assert not inspect.isabstract(presentation::Decorations)


def test_presentation::decorations_constructor_exists():
    assert callable(presentation::Decorations.__init__)


def test_presentation::decorations_constructor_args():
    sig = inspect.signature(presentation::Decorations.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "image" in params, "Missing parameter 'image'"
    assert "images" in params, "Missing parameter 'images'"
    assert "maximized" in params, "Missing parameter 'maximized'"
    assert "minimized" in params, "Missing parameter 'minimized'"
    assert "group4" in params, "Missing parameter 'group4'"

def test_presentation::decorations_has_text():
    assert hasattr(presentation::Decorations, "text")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::decorations_has_image():
    assert hasattr(presentation::Decorations, "image")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_presentation::decorations_has_images():
    assert hasattr(presentation::Decorations, "images")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "images" in klass.__dict__:
            descriptor = klass.__dict__["images"]
            break
    assert isinstance(descriptor, property)

def test_presentation::decorations_has_maximized():
    assert hasattr(presentation::Decorations, "maximized")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "maximized" in klass.__dict__:
            descriptor = klass.__dict__["maximized"]
            break
    assert isinstance(descriptor, property)

def test_presentation::decorations_has_minimized():
    assert hasattr(presentation::Decorations, "minimized")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "minimized" in klass.__dict__:
            descriptor = klass.__dict__["minimized"]
            break
    assert isinstance(descriptor, property)

def test_presentation::decorations_has_group4():
    assert hasattr(presentation::Decorations, "group4")
    descriptor = None
    for klass in presentation::Decorations.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)



def test_presentation::clabel_is_not_abstract():
    assert not inspect.isabstract(presentation::CLabel)


def test_presentation::clabel_constructor_exists():
    assert callable(presentation::CLabel.__init__)


def test_presentation::clabel_constructor_args():
    sig = inspect.signature(presentation::CLabel.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "text" in params, "Missing parameter 'text'"
    assert "image" in params, "Missing parameter 'image'"

def test_presentation::clabel_has_alignment():
    assert hasattr(presentation::CLabel, "alignment")
    descriptor = None
    for klass in presentation::CLabel.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::clabel_has_text():
    assert hasattr(presentation::CLabel, "text")
    descriptor = None
    for klass in presentation::CLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::clabel_has_image():
    assert hasattr(presentation::CLabel, "image")
    descriptor = None
    for klass in presentation::CLabel.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_treeviewer_is_not_abstract():
    assert not inspect.isabstract(TreeViewer)


def test_treeviewer_constructor_exists():
    assert callable(TreeViewer.__init__)


def test_treeviewer_constructor_args():
    sig = inspect.signature(TreeViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::checkboxtreeviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::CheckboxTreeViewer)


def test_presentation::checkboxtreeviewer_constructor_exists():
    assert callable(presentation::CheckboxTreeViewer.__init__)


def test_presentation::checkboxtreeviewer_constructor_args():
    sig = inspect.signature(presentation::CheckboxTreeViewer.__init__)
    params = list(sig.parameters.keys())
    assert "allChecked" in params, "Missing parameter 'allChecked'"
    assert "group6" in params, "Missing parameter 'group6'"

def test_presentation::checkboxtreeviewer_has_allChecked():
    assert hasattr(presentation::CheckboxTreeViewer, "allChecked")
    descriptor = None
    for klass in presentation::CheckboxTreeViewer.__mro__:
        if "allChecked" in klass.__dict__:
            descriptor = klass.__dict__["allChecked"]
            break
    assert isinstance(descriptor, property)

def test_presentation::checkboxtreeviewer_has_group6():
    assert hasattr(presentation::CheckboxTreeViewer, "group6")
    descriptor = None
    for klass in presentation::CheckboxTreeViewer.__mro__:
        if "group6" in klass.__dict__:
            descriptor = klass.__dict__["group6"]
            break
    assert isinstance(descriptor, property)



def test_presentation::collection_is_not_abstract():
    assert not inspect.isabstract(presentation::Collection)


def test_presentation::collection_constructor_exists():
    assert callable(presentation::Collection.__init__)


def test_presentation::collection_constructor_args():
    sig = inspect.signature(presentation::Collection.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::collection_has_mixed():
    assert hasattr(presentation::Collection, "mixed")
    descriptor = None
    for klass in presentation::Collection.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::icheckstateprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::ICheckStateProvider)


def test_presentation::icheckstateprovider_constructor_exists():
    assert callable(presentation::ICheckStateProvider.__init__)


def test_presentation::icheckstateprovider_constructor_args():
    sig = inspect.signature(presentation::ICheckStateProvider.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::icheckstateprovider_has_mixed():
    assert hasattr(presentation::ICheckStateProvider, "mixed")
    descriptor = None
    for klass in presentation::ICheckStateProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_tableviewer_is_not_abstract():
    assert not inspect.isabstract(TableViewer)


def test_tableviewer_constructor_exists():
    assert callable(TableViewer.__init__)


def test_tableviewer_constructor_args():
    sig = inspect.signature(TableViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::checkboxtableviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::CheckboxTableViewer)


def test_presentation::checkboxtableviewer_constructor_exists():
    assert callable(presentation::CheckboxTableViewer.__init__)


def test_presentation::checkboxtableviewer_constructor_args():
    sig = inspect.signature(presentation::CheckboxTableViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group5" in params, "Missing parameter 'group5'"
    assert "allGrayed" in params, "Missing parameter 'allGrayed'"
    assert "allChecked" in params, "Missing parameter 'allChecked'"

def test_presentation::checkboxtableviewer_has_group5():
    assert hasattr(presentation::CheckboxTableViewer, "group5")
    descriptor = None
    for klass in presentation::CheckboxTableViewer.__mro__:
        if "group5" in klass.__dict__:
            descriptor = klass.__dict__["group5"]
            break
    assert isinstance(descriptor, property)

def test_presentation::checkboxtableviewer_has_allGrayed():
    assert hasattr(presentation::CheckboxTableViewer, "allGrayed")
    descriptor = None
    for klass in presentation::CheckboxTableViewer.__mro__:
        if "allGrayed" in klass.__dict__:
            descriptor = klass.__dict__["allGrayed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::checkboxtableviewer_has_allChecked():
    assert hasattr(presentation::CheckboxTableViewer, "allChecked")
    descriptor = None
    for klass in presentation::CheckboxTableViewer.__mro__:
        if "allChecked" in klass.__dict__:
            descriptor = klass.__dict__["allChecked"]
            break
    assert isinstance(descriptor, property)



def test_presentation::layoutdata_is_not_abstract():
    assert not inspect.isabstract(presentation::LayoutData)


def test_presentation::layoutdata_constructor_exists():
    assert callable(presentation::LayoutData.__init__)


def test_presentation::layoutdata_constructor_args():
    sig = inspect.signature(presentation::LayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::layoutdata_has_mixed():
    assert hasattr(presentation::LayoutData, "mixed")
    descriptor = None
    for klass in presentation::LayoutData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::icelleditorvalidator_is_not_abstract():
    assert not inspect.isabstract(presentation::ICellEditorValidator)


def test_presentation::icelleditorvalidator_constructor_exists():
    assert callable(presentation::ICellEditorValidator.__init__)


def test_presentation::icelleditorvalidator_constructor_args():
    sig = inspect.signature(presentation::ICellEditorValidator.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::icelleditorvalidator_has_mixed():
    assert hasattr(presentation::ICellEditorValidator, "mixed")
    descriptor = None
    for klass in presentation::ICellEditorValidator.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tableitem_is_not_abstract():
    assert not inspect.isabstract(presentation::TableItem)


def test_presentation::tableitem_constructor_exists():
    assert callable(presentation::TableItem.__init__)


def test_presentation::tableitem_constructor_args():
    sig = inspect.signature(presentation::TableItem.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "texts" in params, "Missing parameter 'texts'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "imageIndent" in params, "Missing parameter 'imageIndent'"
    assert "grayed" in params, "Missing parameter 'grayed'"

def test_presentation::tableitem_has_group():
    assert hasattr(presentation::TableItem, "group")
    descriptor = None
    for klass in presentation::TableItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableitem_has_texts():
    assert hasattr(presentation::TableItem, "texts")
    descriptor = None
    for klass in presentation::TableItem.__mro__:
        if "texts" in klass.__dict__:
            descriptor = klass.__dict__["texts"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableitem_has_checked():
    assert hasattr(presentation::TableItem, "checked")
    descriptor = None
    for klass in presentation::TableItem.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableitem_has_imageIndent():
    assert hasattr(presentation::TableItem, "imageIndent")
    descriptor = None
    for klass in presentation::TableItem.__mro__:
        if "imageIndent" in klass.__dict__:
            descriptor = klass.__dict__["imageIndent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableitem_has_grayed():
    assert hasattr(presentation::TableItem, "grayed")
    descriptor = None
    for klass in presentation::TableItem.__mro__:
        if "grayed" in klass.__dict__:
            descriptor = klass.__dict__["grayed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::cell_is_not_abstract():
    assert not inspect.isabstract(presentation::Cell)


def test_presentation::cell_constructor_exists():
    assert callable(presentation::Cell.__init__)


def test_presentation::cell_constructor_args():
    sig = inspect.signature(presentation::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "text" in params, "Missing parameter 'text'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::cell_has_image():
    assert hasattr(presentation::Cell, "image")
    descriptor = None
    for klass in presentation::Cell.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_presentation::cell_has_text():
    assert hasattr(presentation::Cell, "text")
    descriptor = None
    for klass in presentation::Cell.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::cell_has_group():
    assert hasattr(presentation::Cell, "group")
    descriptor = None
    for klass in presentation::Cell.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::cell_has_mixed():
    assert hasattr(presentation::Cell, "mixed")
    descriptor = None
    for klass in presentation::Cell.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::celleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::CellEditor)


def test_presentation::celleditor_constructor_exists():
    assert callable(presentation::CellEditor.__init__)


def test_presentation::celleditor_constructor_args():
    sig = inspect.signature(presentation::CellEditor.__init__)
    params = list(sig.parameters.keys())
    assert "errorMessage" in params, "Missing parameter 'errorMessage'"
    assert "style" in params, "Missing parameter 'style'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_presentation::celleditor_has_errorMessage():
    assert hasattr(presentation::CellEditor, "errorMessage")
    descriptor = None
    for klass in presentation::CellEditor.__mro__:
        if "errorMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorMessage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::celleditor_has_style():
    assert hasattr(presentation::CellEditor, "style")
    descriptor = None
    for klass in presentation::CellEditor.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_presentation::celleditor_has_mixed():
    assert hasattr(presentation::CellEditor, "mixed")
    descriptor = None
    for klass in presentation::CellEditor.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::celleditor_has_group():
    assert hasattr(presentation::CellEditor, "group")
    descriptor = None
    for klass in presentation::CellEditor.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_presentation::item_is_not_abstract():
    assert not inspect.isabstract(presentation::Item)


def test_presentation::item_constructor_exists():
    assert callable(presentation::Item.__init__)


def test_presentation::item_constructor_args():
    sig = inspect.signature(presentation::Item.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "image" in params, "Missing parameter 'image'"

def test_presentation::item_has_text():
    assert hasattr(presentation::Item, "text")
    descriptor = None
    for klass in presentation::Item.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::item_has_image():
    assert hasattr(presentation::Item, "image")
    descriptor = None
    for klass in presentation::Item.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_presentation::menu_is_not_abstract():
    assert not inspect.isabstract(presentation::Menu)


def test_presentation::menu_constructor_exists():
    assert callable(presentation::Menu.__init__)


def test_presentation::menu_constructor_args():
    sig = inspect.signature(presentation::Menu.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "handle" in params, "Missing parameter 'handle'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_presentation::menu_has_group():
    assert hasattr(presentation::Menu, "group")
    descriptor = None
    for klass in presentation::Menu.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menu_has_handle():
    assert hasattr(presentation::Menu, "handle")
    descriptor = None
    for klass in presentation::Menu.__mro__:
        if "handle" in klass.__dict__:
            descriptor = klass.__dict__["handle"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menu_has_visible():
    assert hasattr(presentation::Menu, "visible")
    descriptor = None
    for klass in presentation::Menu.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::menu_has_enabled():
    assert hasattr(presentation::Menu, "enabled")
    descriptor = None
    for klass in presentation::Menu.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_presentation::control_is_not_abstract():
    assert not inspect.isabstract(presentation::Control)


def test_presentation::control_constructor_exists():
    assert callable(presentation::Control.__init__)


def test_presentation::control_constructor_args():
    sig = inspect.signature(presentation::Control.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "backgroundImage" in params, "Missing parameter 'backgroundImage'"
    assert "size" in params, "Missing parameter 'size'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "location" in params, "Missing parameter 'location'"
    assert "font" in params, "Missing parameter 'font'"
    assert "background" in params, "Missing parameter 'background'"
    assert "handle" in params, "Missing parameter 'handle'"
    assert "capture" in params, "Missing parameter 'capture'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "foreground" in params, "Missing parameter 'foreground'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "redraw" in params, "Missing parameter 'redraw'"
    assert "dragDetect" in params, "Missing parameter 'dragDetect'"

def test_presentation::control_has_group():
    assert hasattr(presentation::Control, "group")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_backgroundImage():
    assert hasattr(presentation::Control, "backgroundImage")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "backgroundImage" in klass.__dict__:
            descriptor = klass.__dict__["backgroundImage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_size():
    assert hasattr(presentation::Control, "size")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_visible():
    assert hasattr(presentation::Control, "visible")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_location():
    assert hasattr(presentation::Control, "location")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_font():
    assert hasattr(presentation::Control, "font")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "font" in klass.__dict__:
            descriptor = klass.__dict__["font"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_background():
    assert hasattr(presentation::Control, "background")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_handle():
    assert hasattr(presentation::Control, "handle")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "handle" in klass.__dict__:
            descriptor = klass.__dict__["handle"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_capture():
    assert hasattr(presentation::Control, "capture")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "capture" in klass.__dict__:
            descriptor = klass.__dict__["capture"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_enabled():
    assert hasattr(presentation::Control, "enabled")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_foreground():
    assert hasattr(presentation::Control, "foreground")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "foreground" in klass.__dict__:
            descriptor = klass.__dict__["foreground"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_bounds():
    assert hasattr(presentation::Control, "bounds")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_toolTipText():
    assert hasattr(presentation::Control, "toolTipText")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_redraw():
    assert hasattr(presentation::Control, "redraw")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "redraw" in klass.__dict__:
            descriptor = klass.__dict__["redraw"]
            break
    assert isinstance(descriptor, property)

def test_presentation::control_has_dragDetect():
    assert hasattr(presentation::Control, "dragDetect")
    descriptor = None
    for klass in presentation::Control.__mro__:
        if "dragDetect" in klass.__dict__:
            descriptor = klass.__dict__["dragDetect"]
            break
    assert isinstance(descriptor, property)



def test_presentation::caret_is_not_abstract():
    assert not inspect.isabstract(presentation::Caret)


def test_presentation::caret_constructor_exists():
    assert callable(presentation::Caret.__init__)


def test_presentation::caret_constructor_args():
    sig = inspect.signature(presentation::Caret.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "location" in params, "Missing parameter 'location'"
    assert "font" in params, "Missing parameter 'font'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "image" in params, "Missing parameter 'image'"
    assert "group" in params, "Missing parameter 'group'"

def test_presentation::caret_has_size():
    assert hasattr(presentation::Caret, "size")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_bounds():
    assert hasattr(presentation::Caret, "bounds")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_location():
    assert hasattr(presentation::Caret, "location")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_font():
    assert hasattr(presentation::Caret, "font")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "font" in klass.__dict__:
            descriptor = klass.__dict__["font"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_visible():
    assert hasattr(presentation::Caret, "visible")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_image():
    assert hasattr(presentation::Caret, "image")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_presentation::caret_has_group():
    assert hasattr(presentation::Caret, "group")
    descriptor = None
    for klass in presentation::Caret.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_presentation::ime_is_not_abstract():
    assert not inspect.isabstract(presentation::IME)


def test_presentation::ime_constructor_exists():
    assert callable(presentation::IME.__init__)


def test_presentation::ime_constructor_args():
    sig = inspect.signature(presentation::IME.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"
    assert "text" in params, "Missing parameter 'text'"
    assert "group" in params, "Missing parameter 'group'"
    assert "compositionOffset" in params, "Missing parameter 'compositionOffset'"

def test_presentation::ime_has_ranges():
    assert hasattr(presentation::IME, "ranges")
    descriptor = None
    for klass in presentation::IME.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ime_has_text():
    assert hasattr(presentation::IME, "text")
    descriptor = None
    for klass in presentation::IME.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ime_has_group():
    assert hasattr(presentation::IME, "group")
    descriptor = None
    for klass in presentation::IME.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ime_has_compositionOffset():
    assert hasattr(presentation::IME, "compositionOffset")
    descriptor = None
    for klass in presentation::IME.__mro__:
        if "compositionOffset" in klass.__dict__:
            descriptor = klass.__dict__["compositionOffset"]
            break
    assert isinstance(descriptor, property)



def test_presentation::icommand_is_not_abstract():
    assert not inspect.isabstract(presentation::ICommand)


def test_presentation::icommand_constructor_exists():
    assert callable(presentation::ICommand.__init__)


def test_presentation::icommand_constructor_args():
    sig = inspect.signature(presentation::ICommand.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::icommand_has_mixed():
    assert hasattr(presentation::ICommand, "mixed")
    descriptor = None
    for klass in presentation::ICommand.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_presentation::link_is_not_abstract():
    assert not inspect.isabstract(presentation::Link)


def test_presentation::link_constructor_exists():
    assert callable(presentation::Link.__init__)


def test_presentation::link_constructor_args():
    sig = inspect.signature(presentation::Link.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::link_has_text():
    assert hasattr(presentation::Link, "text")
    descriptor = None
    for klass in presentation::Link.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_presentation::label_is_not_abstract():
    assert not inspect.isabstract(presentation::Label)


def test_presentation::label_constructor_exists():
    assert callable(presentation::Label.__init__)


def test_presentation::label_constructor_args():
    sig = inspect.signature(presentation::Label.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::label_has_image():
    assert hasattr(presentation::Label, "image")
    descriptor = None
    for klass in presentation::Label.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_presentation::label_has_alignment():
    assert hasattr(presentation::Label, "alignment")
    descriptor = None
    for klass in presentation::Label.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::label_has_text():
    assert hasattr(presentation::Label, "text")
    descriptor = None
    for klass in presentation::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_presentation::button_is_not_abstract():
    assert not inspect.isabstract(presentation::Button)


def test_presentation::button_constructor_exists():
    assert callable(presentation::Button.__init__)


def test_presentation::button_constructor_args():
    sig = inspect.signature(presentation::Button.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "grayed" in params, "Missing parameter 'grayed'"
    assert "image" in params, "Missing parameter 'image'"
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::button_has_selection():
    assert hasattr(presentation::Button, "selection")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::button_has_group1():
    assert hasattr(presentation::Button, "group1")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::button_has_grayed():
    assert hasattr(presentation::Button, "grayed")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "grayed" in klass.__dict__:
            descriptor = klass.__dict__["grayed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::button_has_image():
    assert hasattr(presentation::Button, "image")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_presentation::button_has_alignment():
    assert hasattr(presentation::Button, "alignment")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::button_has_text():
    assert hasattr(presentation::Button, "text")
    descriptor = None
    for klass in presentation::Button.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_composite_is_not_abstract():
    assert not inspect.isabstract(Composite)


def test_composite_constructor_exists():
    assert callable(Composite.__init__)


def test_composite_constructor_args():
    sig = inspect.signature(Composite.__init__)
    params = list(sig.parameters.keys())



def test_presentation::ctabfolder_is_not_abstract():
    assert not inspect.isabstract(presentation::CTabFolder)


def test_presentation::ctabfolder_constructor_exists():
    assert callable(presentation::CTabFolder.__init__)


def test_presentation::ctabfolder_constructor_args():
    sig = inspect.signature(presentation::CTabFolder.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"
    assert "mINTABWIDTH" in params, "Missing parameter 'mINTABWIDTH'"
    assert "minimized" in params, "Missing parameter 'minimized'"
    assert "mRUVisible" in params, "Missing parameter 'mRUVisible'"
    assert "tabPosition" in params, "Missing parameter 'tabPosition'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "borderVisible" in params, "Missing parameter 'borderVisible'"
    assert "single" in params, "Missing parameter 'single'"
    assert "maximizeVisible" in params, "Missing parameter 'maximizeVisible'"
    assert "maximized" in params, "Missing parameter 'maximized'"
    assert "minimizeVisible" in params, "Missing parameter 'minimizeVisible'"
    assert "selectionForeground" in params, "Missing parameter 'selectionForeground'"
    assert "unselectedImageVisible" in params, "Missing parameter 'unselectedImageVisible'"
    assert "unselectedCloseVisible" in params, "Missing parameter 'unselectedCloseVisible'"
    assert "tabHeight" in params, "Missing parameter 'tabHeight'"
    assert "selectionBackground" in params, "Missing parameter 'selectionBackground'"
    assert "minimumCharacters" in params, "Missing parameter 'minimumCharacters'"
    assert "simple" in params, "Missing parameter 'simple'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"

def test_presentation::ctabfolder_has_group3():
    assert hasattr(presentation::CTabFolder, "group3")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_mINTABWIDTH():
    assert hasattr(presentation::CTabFolder, "mINTABWIDTH")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "mINTABWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["mINTABWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_minimized():
    assert hasattr(presentation::CTabFolder, "minimized")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "minimized" in klass.__dict__:
            descriptor = klass.__dict__["minimized"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_mRUVisible():
    assert hasattr(presentation::CTabFolder, "mRUVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "mRUVisible" in klass.__dict__:
            descriptor = klass.__dict__["mRUVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_tabPosition():
    assert hasattr(presentation::CTabFolder, "tabPosition")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "tabPosition" in klass.__dict__:
            descriptor = klass.__dict__["tabPosition"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_marginWidth():
    assert hasattr(presentation::CTabFolder, "marginWidth")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_borderVisible():
    assert hasattr(presentation::CTabFolder, "borderVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "borderVisible" in klass.__dict__:
            descriptor = klass.__dict__["borderVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_single():
    assert hasattr(presentation::CTabFolder, "single")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_maximizeVisible():
    assert hasattr(presentation::CTabFolder, "maximizeVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "maximizeVisible" in klass.__dict__:
            descriptor = klass.__dict__["maximizeVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_maximized():
    assert hasattr(presentation::CTabFolder, "maximized")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "maximized" in klass.__dict__:
            descriptor = klass.__dict__["maximized"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_minimizeVisible():
    assert hasattr(presentation::CTabFolder, "minimizeVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "minimizeVisible" in klass.__dict__:
            descriptor = klass.__dict__["minimizeVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_selectionForeground():
    assert hasattr(presentation::CTabFolder, "selectionForeground")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "selectionForeground" in klass.__dict__:
            descriptor = klass.__dict__["selectionForeground"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_unselectedImageVisible():
    assert hasattr(presentation::CTabFolder, "unselectedImageVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "unselectedImageVisible" in klass.__dict__:
            descriptor = klass.__dict__["unselectedImageVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_unselectedCloseVisible():
    assert hasattr(presentation::CTabFolder, "unselectedCloseVisible")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "unselectedCloseVisible" in klass.__dict__:
            descriptor = klass.__dict__["unselectedCloseVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_tabHeight():
    assert hasattr(presentation::CTabFolder, "tabHeight")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "tabHeight" in klass.__dict__:
            descriptor = klass.__dict__["tabHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_selectionBackground():
    assert hasattr(presentation::CTabFolder, "selectionBackground")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "selectionBackground" in klass.__dict__:
            descriptor = klass.__dict__["selectionBackground"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_minimumCharacters():
    assert hasattr(presentation::CTabFolder, "minimumCharacters")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "minimumCharacters" in klass.__dict__:
            descriptor = klass.__dict__["minimumCharacters"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_simple():
    assert hasattr(presentation::CTabFolder, "simple")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "simple" in klass.__dict__:
            descriptor = klass.__dict__["simple"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ctabfolder_has_marginHeight():
    assert hasattr(presentation::CTabFolder, "marginHeight")
    descriptor = None
    for klass in presentation::CTabFolder.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)



def test_presentation::combo_is_not_abstract():
    assert not inspect.isabstract(presentation::Combo)


def test_presentation::combo_constructor_exists():
    assert callable(presentation::Combo.__init__)


def test_presentation::combo_constructor_args():
    sig = inspect.signature(presentation::Combo.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "listVisible" in params, "Missing parameter 'listVisible'"
    assert "visibleItemCount" in params, "Missing parameter 'visibleItemCount'"
    assert "items" in params, "Missing parameter 'items'"
    assert "textLimit" in params, "Missing parameter 'textLimit'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_presentation::combo_has_text():
    assert hasattr(presentation::Combo, "text")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_group3():
    assert hasattr(presentation::Combo, "group3")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_listVisible():
    assert hasattr(presentation::Combo, "listVisible")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "listVisible" in klass.__dict__:
            descriptor = klass.__dict__["listVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_visibleItemCount():
    assert hasattr(presentation::Combo, "visibleItemCount")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "visibleItemCount" in klass.__dict__:
            descriptor = klass.__dict__["visibleItemCount"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_items():
    assert hasattr(presentation::Combo, "items")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_textLimit():
    assert hasattr(presentation::Combo, "textLimit")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "textLimit" in klass.__dict__:
            descriptor = klass.__dict__["textLimit"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_selection():
    assert hasattr(presentation::Combo, "selection")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::combo_has_orientation():
    assert hasattr(presentation::Combo, "orientation")
    descriptor = None
    for klass in presentation::Combo.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_presentation::group_is_not_abstract():
    assert not inspect.isabstract(presentation::Group)


def test_presentation::group_constructor_exists():
    assert callable(presentation::Group.__init__)


def test_presentation::group_constructor_args():
    sig = inspect.signature(presentation::Group.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::group_has_text():
    assert hasattr(presentation::Group, "text")
    descriptor = None
    for klass in presentation::Group.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_presentation::ccombo_is_not_abstract():
    assert not inspect.isabstract(presentation::CCombo)


def test_presentation::ccombo_constructor_exists():
    assert callable(presentation::CCombo.__init__)


def test_presentation::ccombo_constructor_args():
    sig = inspect.signature(presentation::CCombo.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "editable" in params, "Missing parameter 'editable'"
    assert "visibleItemCount" in params, "Missing parameter 'visibleItemCount'"
    assert "listVisible" in params, "Missing parameter 'listVisible'"
    assert "text" in params, "Missing parameter 'text'"
    assert "items" in params, "Missing parameter 'items'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "textLimit" in params, "Missing parameter 'textLimit'"

def test_presentation::ccombo_has_selection():
    assert hasattr(presentation::CCombo, "selection")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_editable():
    assert hasattr(presentation::CCombo, "editable")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_visibleItemCount():
    assert hasattr(presentation::CCombo, "visibleItemCount")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "visibleItemCount" in klass.__dict__:
            descriptor = klass.__dict__["visibleItemCount"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_listVisible():
    assert hasattr(presentation::CCombo, "listVisible")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "listVisible" in klass.__dict__:
            descriptor = klass.__dict__["listVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_text():
    assert hasattr(presentation::CCombo, "text")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_items():
    assert hasattr(presentation::CCombo, "items")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_group3():
    assert hasattr(presentation::CCombo, "group3")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::ccombo_has_textLimit():
    assert hasattr(presentation::CCombo, "textLimit")
    descriptor = None
    for klass in presentation::CCombo.__mro__:
        if "textLimit" in klass.__dict__:
            descriptor = klass.__dict__["textLimit"]
            break
    assert isinstance(descriptor, property)



def test_presentation::expandbar_is_not_abstract():
    assert not inspect.isabstract(presentation::ExpandBar)


def test_presentation::expandbar_constructor_exists():
    assert callable(presentation::ExpandBar.__init__)


def test_presentation::expandbar_constructor_args():
    sig = inspect.signature(presentation::ExpandBar.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"
    assert "spacing" in params, "Missing parameter 'spacing'"

def test_presentation::expandbar_has_group3():
    assert hasattr(presentation::ExpandBar, "group3")
    descriptor = None
    for klass in presentation::ExpandBar.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::expandbar_has_spacing():
    assert hasattr(presentation::ExpandBar, "spacing")
    descriptor = None
    for klass in presentation::ExpandBar.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)



def test_presentation::datetime_is_not_abstract():
    assert not inspect.isabstract(presentation::DateTime)


def test_presentation::datetime_constructor_exists():
    assert callable(presentation::DateTime.__init__)


def test_presentation::datetime_constructor_args():
    sig = inspect.signature(presentation::DateTime.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "seconds" in params, "Missing parameter 'seconds'"
    assert "day" in params, "Missing parameter 'day'"
    assert "hours" in params, "Missing parameter 'hours'"
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"

def test_presentation::datetime_has_minutes():
    assert hasattr(presentation::DateTime, "minutes")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetime_has_seconds():
    assert hasattr(presentation::DateTime, "seconds")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "seconds" in klass.__dict__:
            descriptor = klass.__dict__["seconds"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetime_has_day():
    assert hasattr(presentation::DateTime, "day")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetime_has_hours():
    assert hasattr(presentation::DateTime, "hours")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetime_has_month():
    assert hasattr(presentation::DateTime, "month")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_presentation::datetime_has_year():
    assert hasattr(presentation::DateTime, "year")
    descriptor = None
    for klass in presentation::DateTime.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_presentation::canvas_is_not_abstract():
    assert not inspect.isabstract(presentation::Canvas)


def test_presentation::canvas_constructor_exists():
    assert callable(presentation::Canvas.__init__)


def test_presentation::canvas_constructor_args():
    sig = inspect.signature(presentation::Canvas.__init__)
    params = list(sig.parameters.keys())
    assert "mixed1" in params, "Missing parameter 'mixed1'"
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::canvas_has_mixed1():
    assert hasattr(presentation::Canvas, "mixed1")
    descriptor = None
    for klass in presentation::Canvas.__mro__:
        if "mixed1" in klass.__dict__:
            descriptor = klass.__dict__["mixed1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::canvas_has_group3():
    assert hasattr(presentation::Canvas, "group3")
    descriptor = None
    for klass in presentation::Canvas.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_presentation::coolbar_is_not_abstract():
    assert not inspect.isabstract(presentation::CoolBar)


def test_presentation::coolbar_constructor_exists():
    assert callable(presentation::CoolBar.__init__)


def test_presentation::coolbar_constructor_args():
    sig = inspect.signature(presentation::CoolBar.__init__)
    params = list(sig.parameters.keys())
    assert "locked" in params, "Missing parameter 'locked'"
    assert "itemOrder" in params, "Missing parameter 'itemOrder'"
    assert "itemSizes" in params, "Missing parameter 'itemSizes'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "wrapIndices" in params, "Missing parameter 'wrapIndices'"

def test_presentation::coolbar_has_locked():
    assert hasattr(presentation::CoolBar, "locked")
    descriptor = None
    for klass in presentation::CoolBar.__mro__:
        if "locked" in klass.__dict__:
            descriptor = klass.__dict__["locked"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolbar_has_itemOrder():
    assert hasattr(presentation::CoolBar, "itemOrder")
    descriptor = None
    for klass in presentation::CoolBar.__mro__:
        if "itemOrder" in klass.__dict__:
            descriptor = klass.__dict__["itemOrder"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolbar_has_itemSizes():
    assert hasattr(presentation::CoolBar, "itemSizes")
    descriptor = None
    for klass in presentation::CoolBar.__mro__:
        if "itemSizes" in klass.__dict__:
            descriptor = klass.__dict__["itemSizes"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolbar_has_group3():
    assert hasattr(presentation::CoolBar, "group3")
    descriptor = None
    for klass in presentation::CoolBar.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::coolbar_has_wrapIndices():
    assert hasattr(presentation::CoolBar, "wrapIndices")
    descriptor = None
    for klass in presentation::CoolBar.__mro__:
        if "wrapIndices" in klass.__dict__:
            descriptor = klass.__dict__["wrapIndices"]
            break
    assert isinstance(descriptor, property)



def test_presentation::browser_is_not_abstract():
    assert not inspect.isabstract(presentation::Browser)


def test_presentation::browser_constructor_exists():
    assert callable(presentation::Browser.__init__)


def test_presentation::browser_constructor_args():
    sig = inspect.signature(presentation::Browser.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "browserType" in params, "Missing parameter 'browserType'"
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::browser_has_url():
    assert hasattr(presentation::Browser, "url")
    descriptor = None
    for klass in presentation::Browser.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_presentation::browser_has_group3():
    assert hasattr(presentation::Browser, "group3")
    descriptor = None
    for klass in presentation::Browser.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::browser_has_browserType():
    assert hasattr(presentation::Browser, "browserType")
    descriptor = None
    for klass in presentation::Browser.__mro__:
        if "browserType" in klass.__dict__:
            descriptor = klass.__dict__["browserType"]
            break
    assert isinstance(descriptor, property)

def test_presentation::browser_has_text():
    assert hasattr(presentation::Browser, "text")
    descriptor = None
    for klass in presentation::Browser.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_presentation::binding_is_not_abstract():
    assert not inspect.isabstract(presentation::Binding)


def test_presentation::binding_constructor_exists():
    assert callable(presentation::Binding.__init__)


def test_presentation::binding_constructor_args():
    sig = inspect.signature(presentation::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "xPath" in params, "Missing parameter 'xPath'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "path" in params, "Missing parameter 'path'"

def test_presentation::binding_has_elementName():
    assert hasattr(presentation::Binding, "elementName")
    descriptor = None
    for klass in presentation::Binding.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_presentation::binding_has_xPath():
    assert hasattr(presentation::Binding, "xPath")
    descriptor = None
    for klass in presentation::Binding.__mro__:
        if "xPath" in klass.__dict__:
            descriptor = klass.__dict__["xPath"]
            break
    assert isinstance(descriptor, property)

def test_presentation::binding_has_mixed():
    assert hasattr(presentation::Binding, "mixed")
    descriptor = None
    for klass in presentation::Binding.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::binding_has_group():
    assert hasattr(presentation::Binding, "group")
    descriptor = None
    for klass in presentation::Binding.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::binding_has_path():
    assert hasattr(presentation::Binding, "path")
    descriptor = None
    for klass in presentation::Binding.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_presentation::accessible_is_not_abstract():
    assert not inspect.isabstract(presentation::Accessible)


def test_presentation::accessible_constructor_exists():
    assert callable(presentation::Accessible.__init__)


def test_presentation::accessible_constructor_args():
    sig = inspect.signature(presentation::Accessible.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::accessible_has_mixed():
    assert hasattr(presentation::Accessible, "mixed")
    descriptor = None
    for klass in presentation::Accessible.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::eobject_is_not_abstract():
    assert not inspect.isabstract(presentation::EObject)


def test_presentation::eobject_constructor_exists():
    assert callable(presentation::EObject.__init__)


def test_presentation::eobject_constructor_args():
    sig = inspect.signature(presentation::EObject.__init__)
    params = list(sig.parameters.keys())



def test_presentation::treepath_is_not_abstract():
    assert not inspect.isabstract(presentation::TreePath)


def test_presentation::treepath_constructor_exists():
    assert callable(presentation::TreePath.__init__)


def test_presentation::treepath_constructor_args():
    sig = inspect.signature(presentation::TreePath.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::treepath_has_mixed():
    assert hasattr(presentation::TreePath, "mixed")
    descriptor = None
    for klass in presentation::TreePath.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::widget_is_not_abstract():
    assert not inspect.isabstract(presentation::Widget)


def test_presentation::widget_constructor_exists():
    assert callable(presentation::Widget.__init__)


def test_presentation::widget_constructor_args():
    sig = inspect.signature(presentation::Widget.__init__)
    params = list(sig.parameters.keys())
    assert "mouseMoveEvent" in params, "Missing parameter 'mouseMoveEvent'"
    assert "activateEvent" in params, "Missing parameter 'activateEvent'"
    assert "mouseUpEvent" in params, "Missing parameter 'mouseUpEvent'"
    assert "hideEvent" in params, "Missing parameter 'hideEvent'"
    assert "showEvent" in params, "Missing parameter 'showEvent'"
    assert "focusInEvent" in params, "Missing parameter 'focusInEvent'"
    assert "mouseDownEvent" in params, "Missing parameter 'mouseDownEvent'"
    assert "style" in params, "Missing parameter 'style'"
    assert "mouseWheelEvent" in params, "Missing parameter 'mouseWheelEvent'"
    assert "mouseEnterEvent" in params, "Missing parameter 'mouseEnterEvent'"
    assert "hardKeyDownEvent" in params, "Missing parameter 'hardKeyDownEvent'"
    assert "modifyEvent" in params, "Missing parameter 'modifyEvent'"
    assert "deactivateEvent" in params, "Missing parameter 'deactivateEvent'"
    assert "keyDownEvent" in params, "Missing parameter 'keyDownEvent'"
    assert "moveEvent" in params, "Missing parameter 'moveEvent'"
    assert "keyUpEvent" in params, "Missing parameter 'keyUpEvent'"
    assert "helpEvent" in params, "Missing parameter 'helpEvent'"
    assert "verifyEvent" in params, "Missing parameter 'verifyEvent'"
    assert "disposeEvent" in params, "Missing parameter 'disposeEvent'"
    assert "armEvent" in params, "Missing parameter 'armEvent'"
    assert "mouseHoverEvent" in params, "Missing parameter 'mouseHoverEvent'"
    assert "measureItemEvent" in params, "Missing parameter 'measureItemEvent'"
    assert "mouseExitEvent" in params, "Missing parameter 'mouseExitEvent'"
    assert "traverseEvent" in params, "Missing parameter 'traverseEvent'"
    assert "collapseEvent" in params, "Missing parameter 'collapseEvent'"
    assert "setDataEvent" in params, "Missing parameter 'setDataEvent'"
    assert "dataContext" in params, "Missing parameter 'dataContext'"
    assert "resizeEvent" in params, "Missing parameter 'resizeEvent'"
    assert "menuDetectEvent" in params, "Missing parameter 'menuDetectEvent'"
    assert "deiconifyEvent" in params, "Missing parameter 'deiconifyEvent'"
    assert "defaultSelectionEvent" in params, "Missing parameter 'defaultSelectionEvent'"
    assert "closeEvent" in params, "Missing parameter 'closeEvent'"
    assert "mouseDoubleClickEvent" in params, "Missing parameter 'mouseDoubleClickEvent'"
    assert "selectionEvent" in params, "Missing parameter 'selectionEvent'"
    assert "iconifyEvent" in params, "Missing parameter 'iconifyEvent'"
    assert "hardKeyUpEvent" in params, "Missing parameter 'hardKeyUpEvent'"
    assert "dragDetectEvent" in params, "Missing parameter 'dragDetectEvent'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "imeCompositionEvent" in params, "Missing parameter 'imeCompositionEvent'"
    assert "paintEvent" in params, "Missing parameter 'paintEvent'"
    assert "focusOutEvent" in params, "Missing parameter 'focusOutEvent'"
    assert "expandEvent" in params, "Missing parameter 'expandEvent'"
    assert "eraseItemEvent" in params, "Missing parameter 'eraseItemEvent'"
    assert "paintItemEvent" in params, "Missing parameter 'paintItemEvent'"

def test_presentation::widget_has_mouseMoveEvent():
    assert hasattr(presentation::Widget, "mouseMoveEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseMoveEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseMoveEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_activateEvent():
    assert hasattr(presentation::Widget, "activateEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "activateEvent" in klass.__dict__:
            descriptor = klass.__dict__["activateEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseUpEvent():
    assert hasattr(presentation::Widget, "mouseUpEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseUpEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseUpEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_hideEvent():
    assert hasattr(presentation::Widget, "hideEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "hideEvent" in klass.__dict__:
            descriptor = klass.__dict__["hideEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_showEvent():
    assert hasattr(presentation::Widget, "showEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "showEvent" in klass.__dict__:
            descriptor = klass.__dict__["showEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_focusInEvent():
    assert hasattr(presentation::Widget, "focusInEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "focusInEvent" in klass.__dict__:
            descriptor = klass.__dict__["focusInEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseDownEvent():
    assert hasattr(presentation::Widget, "mouseDownEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseDownEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseDownEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_style():
    assert hasattr(presentation::Widget, "style")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseWheelEvent():
    assert hasattr(presentation::Widget, "mouseWheelEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseWheelEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseWheelEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseEnterEvent():
    assert hasattr(presentation::Widget, "mouseEnterEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseEnterEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseEnterEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_hardKeyDownEvent():
    assert hasattr(presentation::Widget, "hardKeyDownEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "hardKeyDownEvent" in klass.__dict__:
            descriptor = klass.__dict__["hardKeyDownEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_modifyEvent():
    assert hasattr(presentation::Widget, "modifyEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "modifyEvent" in klass.__dict__:
            descriptor = klass.__dict__["modifyEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_deactivateEvent():
    assert hasattr(presentation::Widget, "deactivateEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "deactivateEvent" in klass.__dict__:
            descriptor = klass.__dict__["deactivateEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_keyDownEvent():
    assert hasattr(presentation::Widget, "keyDownEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "keyDownEvent" in klass.__dict__:
            descriptor = klass.__dict__["keyDownEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_moveEvent():
    assert hasattr(presentation::Widget, "moveEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "moveEvent" in klass.__dict__:
            descriptor = klass.__dict__["moveEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_keyUpEvent():
    assert hasattr(presentation::Widget, "keyUpEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "keyUpEvent" in klass.__dict__:
            descriptor = klass.__dict__["keyUpEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_helpEvent():
    assert hasattr(presentation::Widget, "helpEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "helpEvent" in klass.__dict__:
            descriptor = klass.__dict__["helpEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_verifyEvent():
    assert hasattr(presentation::Widget, "verifyEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "verifyEvent" in klass.__dict__:
            descriptor = klass.__dict__["verifyEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_disposeEvent():
    assert hasattr(presentation::Widget, "disposeEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "disposeEvent" in klass.__dict__:
            descriptor = klass.__dict__["disposeEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_armEvent():
    assert hasattr(presentation::Widget, "armEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "armEvent" in klass.__dict__:
            descriptor = klass.__dict__["armEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseHoverEvent():
    assert hasattr(presentation::Widget, "mouseHoverEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseHoverEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseHoverEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_measureItemEvent():
    assert hasattr(presentation::Widget, "measureItemEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "measureItemEvent" in klass.__dict__:
            descriptor = klass.__dict__["measureItemEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseExitEvent():
    assert hasattr(presentation::Widget, "mouseExitEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseExitEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseExitEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_traverseEvent():
    assert hasattr(presentation::Widget, "traverseEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "traverseEvent" in klass.__dict__:
            descriptor = klass.__dict__["traverseEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_collapseEvent():
    assert hasattr(presentation::Widget, "collapseEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "collapseEvent" in klass.__dict__:
            descriptor = klass.__dict__["collapseEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_setDataEvent():
    assert hasattr(presentation::Widget, "setDataEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "setDataEvent" in klass.__dict__:
            descriptor = klass.__dict__["setDataEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_dataContext():
    assert hasattr(presentation::Widget, "dataContext")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "dataContext" in klass.__dict__:
            descriptor = klass.__dict__["dataContext"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_resizeEvent():
    assert hasattr(presentation::Widget, "resizeEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "resizeEvent" in klass.__dict__:
            descriptor = klass.__dict__["resizeEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_menuDetectEvent():
    assert hasattr(presentation::Widget, "menuDetectEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "menuDetectEvent" in klass.__dict__:
            descriptor = klass.__dict__["menuDetectEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_deiconifyEvent():
    assert hasattr(presentation::Widget, "deiconifyEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "deiconifyEvent" in klass.__dict__:
            descriptor = klass.__dict__["deiconifyEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_defaultSelectionEvent():
    assert hasattr(presentation::Widget, "defaultSelectionEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "defaultSelectionEvent" in klass.__dict__:
            descriptor = klass.__dict__["defaultSelectionEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_closeEvent():
    assert hasattr(presentation::Widget, "closeEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "closeEvent" in klass.__dict__:
            descriptor = klass.__dict__["closeEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mouseDoubleClickEvent():
    assert hasattr(presentation::Widget, "mouseDoubleClickEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mouseDoubleClickEvent" in klass.__dict__:
            descriptor = klass.__dict__["mouseDoubleClickEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_selectionEvent():
    assert hasattr(presentation::Widget, "selectionEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "selectionEvent" in klass.__dict__:
            descriptor = klass.__dict__["selectionEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_iconifyEvent():
    assert hasattr(presentation::Widget, "iconifyEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "iconifyEvent" in klass.__dict__:
            descriptor = klass.__dict__["iconifyEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_hardKeyUpEvent():
    assert hasattr(presentation::Widget, "hardKeyUpEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "hardKeyUpEvent" in klass.__dict__:
            descriptor = klass.__dict__["hardKeyUpEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_dragDetectEvent():
    assert hasattr(presentation::Widget, "dragDetectEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "dragDetectEvent" in klass.__dict__:
            descriptor = klass.__dict__["dragDetectEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_mixed():
    assert hasattr(presentation::Widget, "mixed")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_imeCompositionEvent():
    assert hasattr(presentation::Widget, "imeCompositionEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "imeCompositionEvent" in klass.__dict__:
            descriptor = klass.__dict__["imeCompositionEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_paintEvent():
    assert hasattr(presentation::Widget, "paintEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "paintEvent" in klass.__dict__:
            descriptor = klass.__dict__["paintEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_focusOutEvent():
    assert hasattr(presentation::Widget, "focusOutEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "focusOutEvent" in klass.__dict__:
            descriptor = klass.__dict__["focusOutEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_expandEvent():
    assert hasattr(presentation::Widget, "expandEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "expandEvent" in klass.__dict__:
            descriptor = klass.__dict__["expandEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_eraseItemEvent():
    assert hasattr(presentation::Widget, "eraseItemEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "eraseItemEvent" in klass.__dict__:
            descriptor = klass.__dict__["eraseItemEvent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::widget_has_paintItemEvent():
    assert hasattr(presentation::Widget, "paintItemEvent")
    descriptor = None
    for klass in presentation::Widget.__mro__:
        if "paintItemEvent" in klass.__dict__:
            descriptor = klass.__dict__["paintItemEvent"]
            break
    assert isinstance(descriptor, property)



def test_columnviewer_is_not_abstract():
    assert not inspect.isabstract(ColumnViewer)


def test_columnviewer_constructor_exists():
    assert callable(ColumnViewer.__init__)


def test_columnviewer_constructor_args():
    sig = inspect.signature(ColumnViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::abstracttreeviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::AbstractTreeViewer)


def test_presentation::abstracttreeviewer_constructor_exists():
    assert callable(presentation::AbstractTreeViewer.__init__)


def test_presentation::abstracttreeviewer_constructor_args():
    sig = inspect.signature(presentation::AbstractTreeViewer.__init__)
    params = list(sig.parameters.keys())
    assert "autoExpandLevel" in params, "Missing parameter 'autoExpandLevel'"
    assert "group4" in params, "Missing parameter 'group4'"

def test_presentation::abstracttreeviewer_has_autoExpandLevel():
    assert hasattr(presentation::AbstractTreeViewer, "autoExpandLevel")
    descriptor = None
    for klass in presentation::AbstractTreeViewer.__mro__:
        if "autoExpandLevel" in klass.__dict__:
            descriptor = klass.__dict__["autoExpandLevel"]
            break
    assert isinstance(descriptor, property)

def test_presentation::abstracttreeviewer_has_group4():
    assert hasattr(presentation::AbstractTreeViewer, "group4")
    descriptor = None
    for klass in presentation::AbstractTreeViewer.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)



def test_presentation::abstracttableviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::AbstractTableViewer)


def test_presentation::abstracttableviewer_constructor_exists():
    assert callable(presentation::AbstractTableViewer.__init__)


def test_presentation::abstracttableviewer_constructor_args():
    sig = inspect.signature(presentation::AbstractTableViewer.__init__)
    params = list(sig.parameters.keys())
    assert "itemCount" in params, "Missing parameter 'itemCount'"

def test_presentation::abstracttableviewer_has_itemCount():
    assert hasattr(presentation::AbstractTableViewer, "itemCount")
    descriptor = None
    for klass in presentation::AbstractTableViewer.__mro__:
        if "itemCount" in klass.__dict__:
            descriptor = klass.__dict__["itemCount"]
            break
    assert isinstance(descriptor, property)



def test_structuredviewer_is_not_abstract():
    assert not inspect.isabstract(StructuredViewer)


def test_structuredviewer_constructor_exists():
    assert callable(StructuredViewer.__init__)


def test_structuredviewer_constructor_args():
    sig = inspect.signature(StructuredViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::columnviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::ColumnViewer)


def test_presentation::columnviewer_constructor_exists():
    assert callable(presentation::ColumnViewer.__init__)


def test_presentation::columnviewer_constructor_args():
    sig = inspect.signature(presentation::ColumnViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::columnviewer_has_group3():
    assert hasattr(presentation::ColumnViewer, "group3")
    descriptor = None
    for klass in presentation::ColumnViewer.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_presentation::abstractlistviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::AbstractListViewer)


def test_presentation::abstractlistviewer_constructor_exists():
    assert callable(presentation::AbstractListViewer.__init__)


def test_presentation::abstractlistviewer_constructor_args():
    sig = inspect.signature(presentation::AbstractListViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::ibindingcontext_is_not_abstract():
    assert not inspect.isabstract(presentation::IBindingContext)


def test_presentation::ibindingcontext_constructor_exists():
    assert callable(presentation::IBindingContext.__init__)


def test_presentation::ibindingcontext_constructor_args():
    sig = inspect.signature(presentation::IBindingContext.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::ibindingcontext_has_mixed():
    assert hasattr(presentation::IBindingContext, "mixed")
    descriptor = None
    for klass in presentation::IBindingContext.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::abstractdataprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::AbstractDataProvider)


def test_presentation::abstractdataprovider_constructor_exists():
    assert callable(presentation::AbstractDataProvider.__init__)


def test_presentation::abstractdataprovider_constructor_args():
    sig = inspect.signature(presentation::AbstractDataProvider.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "key" in params, "Missing parameter 'key'"

def test_presentation::abstractdataprovider_has_group():
    assert hasattr(presentation::AbstractDataProvider, "group")
    descriptor = None
    for klass in presentation::AbstractDataProvider.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::abstractdataprovider_has_mixed():
    assert hasattr(presentation::AbstractDataProvider, "mixed")
    descriptor = None
    for klass in presentation::AbstractDataProvider.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::abstractdataprovider_has_key():
    assert hasattr(presentation::AbstractDataProvider, "key")
    descriptor = None
    for klass in presentation::AbstractDataProvider.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_celleditor_is_not_abstract():
    assert not inspect.isabstract(CellEditor)


def test_celleditor_constructor_exists():
    assert callable(CellEditor.__init__)


def test_celleditor_constructor_args():
    sig = inspect.signature(CellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::dialogcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::DialogCellEditor)


def test_presentation::dialogcelleditor_constructor_exists():
    assert callable(presentation::DialogCellEditor.__init__)


def test_presentation::dialogcelleditor_constructor_args():
    sig = inspect.signature(presentation::DialogCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::checkboxcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::CheckboxCellEditor)


def test_presentation::checkboxcelleditor_constructor_exists():
    assert callable(presentation::CheckboxCellEditor.__init__)


def test_presentation::checkboxcelleditor_constructor_args():
    sig = inspect.signature(presentation::CheckboxCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::abstractcomboboxcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::AbstractComboBoxCellEditor)


def test_presentation::abstractcomboboxcelleditor_constructor_exists():
    assert callable(presentation::AbstractComboBoxCellEditor.__init__)


def test_presentation::abstractcomboboxcelleditor_constructor_args():
    sig = inspect.signature(presentation::AbstractComboBoxCellEditor.__init__)
    params = list(sig.parameters.keys())
    assert "activationStyle" in params, "Missing parameter 'activationStyle'"

def test_presentation::abstractcomboboxcelleditor_has_activationStyle():
    assert hasattr(presentation::AbstractComboBoxCellEditor, "activationStyle")
    descriptor = None
    for klass in presentation::AbstractComboBoxCellEditor.__mro__:
        if "activationStyle" in klass.__dict__:
            descriptor = klass.__dict__["activationStyle"]
            break
    assert isinstance(descriptor, property)



def test_presentation::windowmanager_is_not_abstract():
    assert not inspect.isabstract(presentation::WindowManager)


def test_presentation::windowmanager_constructor_exists():
    assert callable(presentation::WindowManager.__init__)


def test_presentation::windowmanager_constructor_args():
    sig = inspect.signature(presentation::WindowManager.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::windowmanager_has_mixed():
    assert hasattr(presentation::WindowManager, "mixed")
    descriptor = None
    for klass in presentation::WindowManager.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_viewercomparator_is_not_abstract():
    assert not inspect.isabstract(ViewerComparator)


def test_viewercomparator_constructor_exists():
    assert callable(ViewerComparator.__init__)


def test_viewercomparator_constructor_args():
    sig = inspect.signature(ViewerComparator.__init__)
    params = list(sig.parameters.keys())



def test_presentation::viewercolumn_is_not_abstract():
    assert not inspect.isabstract(presentation::ViewerColumn)


def test_presentation::viewercolumn_constructor_exists():
    assert callable(presentation::ViewerColumn.__init__)


def test_presentation::viewercolumn_constructor_args():
    sig = inspect.signature(presentation::ViewerColumn.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::viewercolumn_has_mixed():
    assert hasattr(presentation::ViewerColumn, "mixed")
    descriptor = None
    for klass in presentation::ViewerColumn.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::viewer_is_not_abstract():
    assert not inspect.isabstract(presentation::Viewer)


def test_presentation::viewer_constructor_exists():
    assert callable(presentation::Viewer.__init__)


def test_presentation::viewer_constructor_args():
    sig = inspect.signature(presentation::Viewer.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::viewer_has_group():
    assert hasattr(presentation::Viewer, "group")
    descriptor = None
    for klass in presentation::Viewer.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::viewer_has_mixed():
    assert hasattr(presentation::Viewer, "mixed")
    descriptor = None
    for klass in presentation::Viewer.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::url_is_not_abstract():
    assert not inspect.isabstract(presentation::URL)


def test_presentation::url_constructor_exists():
    assert callable(presentation::URL.__init__)


def test_presentation::url_constructor_args():
    sig = inspect.signature(presentation::URL.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::url_has_mixed():
    assert hasattr(presentation::URL, "mixed")
    descriptor = None
    for klass in presentation::URL.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::treeitem_is_not_abstract():
    assert not inspect.isabstract(presentation::TreeItem)


def test_presentation::treeitem_constructor_exists():
    assert callable(presentation::TreeItem.__init__)


def test_presentation::treeitem_constructor_args():
    sig = inspect.signature(presentation::TreeItem.__init__)
    params = list(sig.parameters.keys())
    assert "grayed" in params, "Missing parameter 'grayed'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "group" in params, "Missing parameter 'group'"
    assert "itemCount" in params, "Missing parameter 'itemCount'"
    assert "expanded" in params, "Missing parameter 'expanded'"
    assert "texts" in params, "Missing parameter 'texts'"
    assert "handle" in params, "Missing parameter 'handle'"

def test_presentation::treeitem_has_grayed():
    assert hasattr(presentation::TreeItem, "grayed")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "grayed" in klass.__dict__:
            descriptor = klass.__dict__["grayed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_checked():
    assert hasattr(presentation::TreeItem, "checked")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_group():
    assert hasattr(presentation::TreeItem, "group")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_itemCount():
    assert hasattr(presentation::TreeItem, "itemCount")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "itemCount" in klass.__dict__:
            descriptor = klass.__dict__["itemCount"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_expanded():
    assert hasattr(presentation::TreeItem, "expanded")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "expanded" in klass.__dict__:
            descriptor = klass.__dict__["expanded"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_texts():
    assert hasattr(presentation::TreeItem, "texts")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "texts" in klass.__dict__:
            descriptor = klass.__dict__["texts"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treeitem_has_handle():
    assert hasattr(presentation::TreeItem, "handle")
    descriptor = None
    for klass in presentation::TreeItem.__mro__:
        if "handle" in klass.__dict__:
            descriptor = klass.__dict__["handle"]
            break
    assert isinstance(descriptor, property)



def test_presentation::treecolumn_is_not_abstract():
    assert not inspect.isabstract(presentation::TreeColumn)


def test_presentation::treecolumn_constructor_exists():
    assert callable(presentation::TreeColumn.__init__)


def test_presentation::treecolumn_constructor_args():
    sig = inspect.signature(presentation::TreeColumn.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "group" in params, "Missing parameter 'group'"
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "moveable" in params, "Missing parameter 'moveable'"

def test_presentation::treecolumn_has_width():
    assert hasattr(presentation::TreeColumn, "width")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treecolumn_has_toolTipText():
    assert hasattr(presentation::TreeColumn, "toolTipText")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treecolumn_has_group():
    assert hasattr(presentation::TreeColumn, "group")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treecolumn_has_alignment():
    assert hasattr(presentation::TreeColumn, "alignment")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treecolumn_has_resizable():
    assert hasattr(presentation::TreeColumn, "resizable")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::treecolumn_has_moveable():
    assert hasattr(presentation::TreeColumn, "moveable")
    descriptor = None
    for klass in presentation::TreeColumn.__mro__:
        if "moveable" in klass.__dict__:
            descriptor = klass.__dict__["moveable"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tree_is_not_abstract():
    assert not inspect.isabstract(presentation::Tree)


def test_presentation::tree_constructor_exists():
    assert callable(presentation::Tree.__init__)


def test_presentation::tree_constructor_args():
    sig = inspect.signature(presentation::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "columnOrder" in params, "Missing parameter 'columnOrder'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "itemCount" in params, "Missing parameter 'itemCount'"
    assert "sortDirection" in params, "Missing parameter 'sortDirection'"
    assert "linesVisible" in params, "Missing parameter 'linesVisible'"
    assert "headerVisible" in params, "Missing parameter 'headerVisible'"

def test_presentation::tree_has_columnOrder():
    assert hasattr(presentation::Tree, "columnOrder")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "columnOrder" in klass.__dict__:
            descriptor = klass.__dict__["columnOrder"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tree_has_group3():
    assert hasattr(presentation::Tree, "group3")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tree_has_itemCount():
    assert hasattr(presentation::Tree, "itemCount")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "itemCount" in klass.__dict__:
            descriptor = klass.__dict__["itemCount"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tree_has_sortDirection():
    assert hasattr(presentation::Tree, "sortDirection")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "sortDirection" in klass.__dict__:
            descriptor = klass.__dict__["sortDirection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tree_has_linesVisible():
    assert hasattr(presentation::Tree, "linesVisible")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "linesVisible" in klass.__dict__:
            descriptor = klass.__dict__["linesVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tree_has_headerVisible():
    assert hasattr(presentation::Tree, "headerVisible")
    descriptor = None
    for klass in presentation::Tree.__mro__:
        if "headerVisible" in klass.__dict__:
            descriptor = klass.__dict__["headerVisible"]
            break
    assert isinstance(descriptor, property)



def test_presentation::traydialog_is_not_abstract():
    assert not inspect.isabstract(presentation::TrayDialog)


def test_presentation::traydialog_constructor_exists():
    assert callable(presentation::TrayDialog.__init__)


def test_presentation::traydialog_constructor_args():
    sig = inspect.signature(presentation::TrayDialog.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "helpAvailable" in params, "Missing parameter 'helpAvailable'"

def test_presentation::traydialog_has_group2():
    assert hasattr(presentation::TrayDialog, "group2")
    descriptor = None
    for klass in presentation::TrayDialog.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_presentation::traydialog_has_helpAvailable():
    assert hasattr(presentation::TrayDialog, "helpAvailable")
    descriptor = None
    for klass in presentation::TrayDialog.__mro__:
        if "helpAvailable" in klass.__dict__:
            descriptor = klass.__dict__["helpAvailable"]
            break
    assert isinstance(descriptor, property)



def test_presentation::trayitem_is_not_abstract():
    assert not inspect.isabstract(presentation::TrayItem)


def test_presentation::trayitem_constructor_exists():
    assert callable(presentation::TrayItem.__init__)


def test_presentation::trayitem_constructor_args():
    sig = inspect.signature(presentation::TrayItem.__init__)
    params = list(sig.parameters.keys())



def test_presentation::tray_is_not_abstract():
    assert not inspect.isabstract(presentation::Tray)


def test_presentation::tray_constructor_exists():
    assert callable(presentation::Tray.__init__)


def test_presentation::tray_constructor_args():
    sig = inspect.signature(presentation::Tray.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_presentation::tray_has_group():
    assert hasattr(presentation::Tray, "group")
    descriptor = None
    for klass in presentation::Tray.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tracker_is_not_abstract():
    assert not inspect.isabstract(presentation::Tracker)


def test_presentation::tracker_constructor_exists():
    assert callable(presentation::Tracker.__init__)


def test_presentation::tracker_constructor_args():
    sig = inspect.signature(presentation::Tracker.__init__)
    params = list(sig.parameters.keys())
    assert "rectangles" in params, "Missing parameter 'rectangles'"
    assert "group" in params, "Missing parameter 'group'"
    assert "stippled" in params, "Missing parameter 'stippled'"

def test_presentation::tracker_has_rectangles():
    assert hasattr(presentation::Tracker, "rectangles")
    descriptor = None
    for klass in presentation::Tracker.__mro__:
        if "rectangles" in klass.__dict__:
            descriptor = klass.__dict__["rectangles"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tracker_has_group():
    assert hasattr(presentation::Tracker, "group")
    descriptor = None
    for klass in presentation::Tracker.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tracker_has_stippled():
    assert hasattr(presentation::Tracker, "stippled")
    descriptor = None
    for klass in presentation::Tracker.__mro__:
        if "stippled" in klass.__dict__:
            descriptor = klass.__dict__["stippled"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tooltip_is_not_abstract():
    assert not inspect.isabstract(presentation::ToolTip)


def test_presentation::tooltip_constructor_exists():
    assert callable(presentation::ToolTip.__init__)


def test_presentation::tooltip_constructor_args():
    sig = inspect.signature(presentation::ToolTip.__init__)
    params = list(sig.parameters.keys())
    assert "autoHide" in params, "Missing parameter 'autoHide'"
    assert "message" in params, "Missing parameter 'message'"
    assert "text" in params, "Missing parameter 'text'"
    assert "group" in params, "Missing parameter 'group'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_presentation::tooltip_has_autoHide():
    assert hasattr(presentation::ToolTip, "autoHide")
    descriptor = None
    for klass in presentation::ToolTip.__mro__:
        if "autoHide" in klass.__dict__:
            descriptor = klass.__dict__["autoHide"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tooltip_has_message():
    assert hasattr(presentation::ToolTip, "message")
    descriptor = None
    for klass in presentation::ToolTip.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tooltip_has_text():
    assert hasattr(presentation::ToolTip, "text")
    descriptor = None
    for klass in presentation::ToolTip.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tooltip_has_group():
    assert hasattr(presentation::ToolTip, "group")
    descriptor = None
    for klass in presentation::ToolTip.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tooltip_has_visible():
    assert hasattr(presentation::ToolTip, "visible")
    descriptor = None
    for klass in presentation::ToolTip.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_presentation::toolitem_is_not_abstract():
    assert not inspect.isabstract(presentation::ToolItem)


def test_presentation::toolitem_constructor_exists():
    assert callable(presentation::ToolItem.__init__)


def test_presentation::toolitem_constructor_args():
    sig = inspect.signature(presentation::ToolItem.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "group" in params, "Missing parameter 'group'"
    assert "hotImage" in params, "Missing parameter 'hotImage'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "disabledImage" in params, "Missing parameter 'disabledImage'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "width" in params, "Missing parameter 'width'"
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_presentation::toolitem_has_enabled():
    assert hasattr(presentation::ToolItem, "enabled")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_group():
    assert hasattr(presentation::ToolItem, "group")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_hotImage():
    assert hasattr(presentation::ToolItem, "hotImage")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "hotImage" in klass.__dict__:
            descriptor = klass.__dict__["hotImage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_toolTipText():
    assert hasattr(presentation::ToolItem, "toolTipText")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_disabledImage():
    assert hasattr(presentation::ToolItem, "disabledImage")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "disabledImage" in klass.__dict__:
            descriptor = klass.__dict__["disabledImage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_selection():
    assert hasattr(presentation::ToolItem, "selection")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_width():
    assert hasattr(presentation::ToolItem, "width")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::toolitem_has_bounds():
    assert hasattr(presentation::ToolItem, "bounds")
    descriptor = None
    for klass in presentation::ToolItem.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_presentation::toolbar_is_not_abstract():
    assert not inspect.isabstract(presentation::ToolBar)


def test_presentation::toolbar_constructor_exists():
    assert callable(presentation::ToolBar.__init__)


def test_presentation::toolbar_constructor_args():
    sig = inspect.signature(presentation::ToolBar.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::toolbar_has_group3():
    assert hasattr(presentation::ToolBar, "group3")
    descriptor = None
    for klass in presentation::ToolBar.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_traydialog_is_not_abstract():
    assert not inspect.isabstract(TrayDialog)


def test_traydialog_constructor_exists():
    assert callable(TrayDialog.__init__)


def test_traydialog_constructor_args():
    sig = inspect.signature(TrayDialog.__init__)
    params = list(sig.parameters.keys())



def test_presentation::titleareadialog_is_not_abstract():
    assert not inspect.isabstract(presentation::TitleAreaDialog)


def test_presentation::titleareadialog_constructor_exists():
    assert callable(presentation::TitleAreaDialog.__init__)


def test_presentation::titleareadialog_constructor_args():
    sig = inspect.signature(presentation::TitleAreaDialog.__init__)
    params = list(sig.parameters.keys())
    assert "titleImage" in params, "Missing parameter 'titleImage'"
    assert "message" in params, "Missing parameter 'message'"
    assert "errorMessage" in params, "Missing parameter 'errorMessage'"
    assert "title" in params, "Missing parameter 'title'"
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::titleareadialog_has_titleImage():
    assert hasattr(presentation::TitleAreaDialog, "titleImage")
    descriptor = None
    for klass in presentation::TitleAreaDialog.__mro__:
        if "titleImage" in klass.__dict__:
            descriptor = klass.__dict__["titleImage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::titleareadialog_has_message():
    assert hasattr(presentation::TitleAreaDialog, "message")
    descriptor = None
    for klass in presentation::TitleAreaDialog.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_presentation::titleareadialog_has_errorMessage():
    assert hasattr(presentation::TitleAreaDialog, "errorMessage")
    descriptor = None
    for klass in presentation::TitleAreaDialog.__mro__:
        if "errorMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorMessage"]
            break
    assert isinstance(descriptor, property)

def test_presentation::titleareadialog_has_title():
    assert hasattr(presentation::TitleAreaDialog, "title")
    descriptor = None
    for klass in presentation::TitleAreaDialog.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_presentation::titleareadialog_has_group3():
    assert hasattr(presentation::TitleAreaDialog, "group3")
    descriptor = None
    for klass in presentation::TitleAreaDialog.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_presentation::textcelleditor_is_not_abstract():
    assert not inspect.isabstract(presentation::TextCellEditor)


def test_presentation::textcelleditor_constructor_exists():
    assert callable(presentation::TextCellEditor.__init__)


def test_presentation::textcelleditor_constructor_args():
    sig = inspect.signature(presentation::TextCellEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::text_is_not_abstract():
    assert not inspect.isabstract(presentation::Text)


def test_presentation::text_constructor_exists():
    assert callable(presentation::Text.__init__)


def test_presentation::text_constructor_args():
    sig = inspect.signature(presentation::Text.__init__)
    params = list(sig.parameters.keys())
    assert "textLimit" in params, "Missing parameter 'textLimit'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "editable" in params, "Missing parameter 'editable'"
    assert "topIndex" in params, "Missing parameter 'topIndex'"
    assert "echoChar" in params, "Missing parameter 'echoChar'"
    assert "doubleClickEnabled" in params, "Missing parameter 'doubleClickEnabled'"
    assert "selectionText" in params, "Missing parameter 'selectionText'"
    assert "text" in params, "Missing parameter 'text'"
    assert "caretLocation" in params, "Missing parameter 'caretLocation'"
    assert "lineDelimiter" in params, "Missing parameter 'lineDelimiter'"
    assert "tabs" in params, "Missing parameter 'tabs'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "message" in params, "Missing parameter 'message'"

def test_presentation::text_has_textLimit():
    assert hasattr(presentation::Text, "textLimit")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "textLimit" in klass.__dict__:
            descriptor = klass.__dict__["textLimit"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_orientation():
    assert hasattr(presentation::Text, "orientation")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_editable():
    assert hasattr(presentation::Text, "editable")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_topIndex():
    assert hasattr(presentation::Text, "topIndex")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "topIndex" in klass.__dict__:
            descriptor = klass.__dict__["topIndex"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_echoChar():
    assert hasattr(presentation::Text, "echoChar")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "echoChar" in klass.__dict__:
            descriptor = klass.__dict__["echoChar"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_doubleClickEnabled():
    assert hasattr(presentation::Text, "doubleClickEnabled")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "doubleClickEnabled" in klass.__dict__:
            descriptor = klass.__dict__["doubleClickEnabled"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_selectionText():
    assert hasattr(presentation::Text, "selectionText")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "selectionText" in klass.__dict__:
            descriptor = klass.__dict__["selectionText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_text():
    assert hasattr(presentation::Text, "text")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_caretLocation():
    assert hasattr(presentation::Text, "caretLocation")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "caretLocation" in klass.__dict__:
            descriptor = klass.__dict__["caretLocation"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_lineDelimiter():
    assert hasattr(presentation::Text, "lineDelimiter")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "lineDelimiter" in klass.__dict__:
            descriptor = klass.__dict__["lineDelimiter"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_tabs():
    assert hasattr(presentation::Text, "tabs")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "tabs" in klass.__dict__:
            descriptor = klass.__dict__["tabs"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_selection():
    assert hasattr(presentation::Text, "selection")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::text_has_message():
    assert hasattr(presentation::Text, "message")
    descriptor = None
    for klass in presentation::Text.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_abstracttableviewer_is_not_abstract():
    assert not inspect.isabstract(AbstractTableViewer)


def test_abstracttableviewer_constructor_exists():
    assert callable(AbstractTableViewer.__init__)


def test_abstracttableviewer_constructor_args():
    sig = inspect.signature(AbstractTableViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::tableviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::TableViewer)


def test_presentation::tableviewer_constructor_exists():
    assert callable(presentation::TableViewer.__init__)


def test_presentation::tableviewer_constructor_args():
    sig = inspect.signature(presentation::TableViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group4" in params, "Missing parameter 'group4'"

def test_presentation::tableviewer_has_group4():
    assert hasattr(presentation::TableViewer, "group4")
    descriptor = None
    for klass in presentation::TableViewer.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)



def test_abstracttreeviewer_is_not_abstract():
    assert not inspect.isabstract(AbstractTreeViewer)


def test_abstracttreeviewer_constructor_exists():
    assert callable(AbstractTreeViewer.__init__)


def test_abstracttreeviewer_constructor_args():
    sig = inspect.signature(AbstractTreeViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::treeviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::TreeViewer)


def test_presentation::treeviewer_constructor_exists():
    assert callable(presentation::TreeViewer.__init__)


def test_presentation::treeviewer_constructor_args():
    sig = inspect.signature(presentation::TreeViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group5" in params, "Missing parameter 'group5'"

def test_presentation::treeviewer_has_group5():
    assert hasattr(presentation::TreeViewer, "group5")
    descriptor = None
    for klass in presentation::TreeViewer.__mro__:
        if "group5" in klass.__dict__:
            descriptor = klass.__dict__["group5"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tabletreeviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::TableTreeViewer)


def test_presentation::tabletreeviewer_constructor_exists():
    assert callable(presentation::TableTreeViewer.__init__)


def test_presentation::tabletreeviewer_constructor_args():
    sig = inspect.signature(presentation::TableTreeViewer.__init__)
    params = list(sig.parameters.keys())
    assert "group5" in params, "Missing parameter 'group5'"

def test_presentation::tabletreeviewer_has_group5():
    assert hasattr(presentation::TableTreeViewer, "group5")
    descriptor = None
    for klass in presentation::TableTreeViewer.__mro__:
        if "group5" in klass.__dict__:
            descriptor = klass.__dict__["group5"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tabletree_is_not_abstract():
    assert not inspect.isabstract(presentation::TableTree)


def test_presentation::tabletree_constructor_exists():
    assert callable(presentation::TableTree.__init__)


def test_presentation::tabletree_constructor_args():
    sig = inspect.signature(presentation::TableTree.__init__)
    params = list(sig.parameters.keys())



def test_viewercolumn_is_not_abstract():
    assert not inspect.isabstract(ViewerColumn)


def test_viewercolumn_constructor_exists():
    assert callable(ViewerColumn.__init__)


def test_viewercolumn_constructor_args():
    sig = inspect.signature(ViewerColumn.__init__)
    params = list(sig.parameters.keys())



def test_presentation::tableviewercolumn_is_not_abstract():
    assert not inspect.isabstract(presentation::TableViewerColumn)


def test_presentation::tableviewercolumn_constructor_exists():
    assert callable(presentation::TableViewerColumn.__init__)


def test_presentation::tableviewercolumn_constructor_args():
    sig = inspect.signature(presentation::TableViewerColumn.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"

def test_presentation::tableviewercolumn_has_group():
    assert hasattr(presentation::TableViewerColumn, "group")
    descriptor = None
    for klass in presentation::TableViewerColumn.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableviewercolumn_has_width():
    assert hasattr(presentation::TableViewerColumn, "width")
    descriptor = None
    for klass in presentation::TableViewerColumn.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableviewercolumn_has_text():
    assert hasattr(presentation::TableViewerColumn, "text")
    descriptor = None
    for klass in presentation::TableViewerColumn.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_controleditor_is_not_abstract():
    assert not inspect.isabstract(ControlEditor)


def test_controleditor_constructor_exists():
    assert callable(ControlEditor.__init__)


def test_controleditor_constructor_args():
    sig = inspect.signature(ControlEditor.__init__)
    params = list(sig.parameters.keys())



def test_presentation::tableeditor_is_not_abstract():
    assert not inspect.isabstract(presentation::TableEditor)


def test_presentation::tableeditor_constructor_exists():
    assert callable(presentation::TableEditor.__init__)


def test_presentation::tableeditor_constructor_args():
    sig = inspect.signature(presentation::TableEditor.__init__)
    params = list(sig.parameters.keys())
    assert "dynamic" in params, "Missing parameter 'dynamic'"
    assert "column" in params, "Missing parameter 'column'"
    assert "group1" in params, "Missing parameter 'group1'"

def test_presentation::tableeditor_has_dynamic():
    assert hasattr(presentation::TableEditor, "dynamic")
    descriptor = None
    for klass in presentation::TableEditor.__mro__:
        if "dynamic" in klass.__dict__:
            descriptor = klass.__dict__["dynamic"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableeditor_has_column():
    assert hasattr(presentation::TableEditor, "column")
    descriptor = None
    for klass in presentation::TableEditor.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tableeditor_has_group1():
    assert hasattr(presentation::TableEditor, "group1")
    descriptor = None
    for klass in presentation::TableEditor.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tablecolumn_is_not_abstract():
    assert not inspect.isabstract(presentation::TableColumn)


def test_presentation::tablecolumn_constructor_exists():
    assert callable(presentation::TableColumn.__init__)


def test_presentation::tablecolumn_constructor_args():
    sig = inspect.signature(presentation::TableColumn.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "width" in params, "Missing parameter 'width'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "moveable" in params, "Missing parameter 'moveable'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "group" in params, "Missing parameter 'group'"

def test_presentation::tablecolumn_has_alignment():
    assert hasattr(presentation::TableColumn, "alignment")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tablecolumn_has_width():
    assert hasattr(presentation::TableColumn, "width")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tablecolumn_has_resizable():
    assert hasattr(presentation::TableColumn, "resizable")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tablecolumn_has_moveable():
    assert hasattr(presentation::TableColumn, "moveable")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "moveable" in klass.__dict__:
            descriptor = klass.__dict__["moveable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tablecolumn_has_toolTipText():
    assert hasattr(presentation::TableColumn, "toolTipText")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tablecolumn_has_group():
    assert hasattr(presentation::TableColumn, "group")
    descriptor = None
    for klass in presentation::TableColumn.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_presentation::table_is_not_abstract():
    assert not inspect.isabstract(presentation::Table)


def test_presentation::table_constructor_exists():
    assert callable(presentation::Table.__init__)


def test_presentation::table_constructor_args():
    sig = inspect.signature(presentation::Table.__init__)
    params = list(sig.parameters.keys())
    assert "topIndex" in params, "Missing parameter 'topIndex'"
    assert "sortDirection" in params, "Missing parameter 'sortDirection'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "selectionIndices" in params, "Missing parameter 'selectionIndices'"
    assert "columnOrder" in params, "Missing parameter 'columnOrder'"
    assert "linesVisible" in params, "Missing parameter 'linesVisible'"
    assert "itemCount" in params, "Missing parameter 'itemCount'"
    assert "headerVisible" in params, "Missing parameter 'headerVisible'"

def test_presentation::table_has_topIndex():
    assert hasattr(presentation::Table, "topIndex")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "topIndex" in klass.__dict__:
            descriptor = klass.__dict__["topIndex"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_sortDirection():
    assert hasattr(presentation::Table, "sortDirection")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "sortDirection" in klass.__dict__:
            descriptor = klass.__dict__["sortDirection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_group3():
    assert hasattr(presentation::Table, "group3")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_selectionIndices():
    assert hasattr(presentation::Table, "selectionIndices")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "selectionIndices" in klass.__dict__:
            descriptor = klass.__dict__["selectionIndices"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_columnOrder():
    assert hasattr(presentation::Table, "columnOrder")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "columnOrder" in klass.__dict__:
            descriptor = klass.__dict__["columnOrder"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_linesVisible():
    assert hasattr(presentation::Table, "linesVisible")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "linesVisible" in klass.__dict__:
            descriptor = klass.__dict__["linesVisible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_itemCount():
    assert hasattr(presentation::Table, "itemCount")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "itemCount" in klass.__dict__:
            descriptor = klass.__dict__["itemCount"]
            break
    assert isinstance(descriptor, property)

def test_presentation::table_has_headerVisible():
    assert hasattr(presentation::Table, "headerVisible")
    descriptor = None
    for klass in presentation::Table.__mro__:
        if "headerVisible" in klass.__dict__:
            descriptor = klass.__dict__["headerVisible"]
            break
    assert isinstance(descriptor, property)



def test_presentation::tabfolder_is_not_abstract():
    assert not inspect.isabstract(presentation::TabFolder)


def test_presentation::tabfolder_constructor_exists():
    assert callable(presentation::TabFolder.__init__)


def test_presentation::tabfolder_constructor_args():
    sig = inspect.signature(presentation::TabFolder.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::tabfolder_has_group3():
    assert hasattr(presentation::TabFolder, "group3")
    descriptor = None
    for klass in presentation::TabFolder.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_textstyle_is_not_abstract():
    assert not inspect.isabstract(TextStyle)


def test_textstyle_constructor_exists():
    assert callable(TextStyle.__init__)


def test_textstyle_constructor_args():
    sig = inspect.signature(TextStyle.__init__)
    params = list(sig.parameters.keys())



def test_presentation::tabitem_is_not_abstract():
    assert not inspect.isabstract(presentation::TabItem)


def test_presentation::tabitem_constructor_exists():
    assert callable(presentation::TabItem.__init__)


def test_presentation::tabitem_constructor_args():
    sig = inspect.signature(presentation::TabItem.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "toolTipText" in params, "Missing parameter 'toolTipText'"
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_presentation::tabitem_has_group():
    assert hasattr(presentation::TabItem, "group")
    descriptor = None
    for klass in presentation::TabItem.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tabitem_has_toolTipText():
    assert hasattr(presentation::TabItem, "toolTipText")
    descriptor = None
    for klass in presentation::TabItem.__mro__:
        if "toolTipText" in klass.__dict__:
            descriptor = klass.__dict__["toolTipText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::tabitem_has_bounds():
    assert hasattr(presentation::TabItem, "bounds")
    descriptor = None
    for klass in presentation::TabItem.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_presentation::styledtextcontent_is_not_abstract():
    assert not inspect.isabstract(presentation::StyledTextContent)


def test_presentation::styledtextcontent_constructor_exists():
    assert callable(presentation::StyledTextContent.__init__)


def test_presentation::styledtextcontent_constructor_args():
    sig = inspect.signature(presentation::StyledTextContent.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::styledtextcontent_has_mixed():
    assert hasattr(presentation::StyledTextContent, "mixed")
    descriptor = None
    for klass in presentation::StyledTextContent.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::stylerange_is_not_abstract():
    assert not inspect.isabstract(presentation::StyleRange)


def test_presentation::stylerange_constructor_exists():
    assert callable(presentation::StyleRange.__init__)


def test_presentation::stylerange_constructor_args():
    sig = inspect.signature(presentation::StyleRange.__init__)
    params = list(sig.parameters.keys())



def test_presentation::styledtext_is_not_abstract():
    assert not inspect.isabstract(presentation::StyledText)


def test_presentation::styledtext_constructor_exists():
    assert callable(presentation::StyledText.__init__)


def test_presentation::styledtext_constructor_args():
    sig = inspect.signature(presentation::StyledText.__init__)
    params = list(sig.parameters.keys())
    assert "caretOffset" in params, "Missing parameter 'caretOffset'"
    assert "selectionRanges" in params, "Missing parameter 'selectionRanges'"
    assert "horizontalIndex" in params, "Missing parameter 'horizontalIndex'"
    assert "bidiColoring" in params, "Missing parameter 'bidiColoring'"
    assert "topIndex" in params, "Missing parameter 'topIndex'"
    assert "topPixel" in params, "Missing parameter 'topPixel'"
    assert "editable" in params, "Missing parameter 'editable'"
    assert "ranges" in params, "Missing parameter 'ranges'"
    assert "textLimit" in params, "Missing parameter 'textLimit'"
    assert "text" in params, "Missing parameter 'text'"
    assert "tabs" in params, "Missing parameter 'tabs'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "selectionText" in params, "Missing parameter 'selectionText'"
    assert "doubleClickEnabled" in params, "Missing parameter 'doubleClickEnabled'"
    assert "selectionForeground" in params, "Missing parameter 'selectionForeground'"
    assert "horizontalPixel" in params, "Missing parameter 'horizontalPixel'"
    assert "lineDelimiter" in params, "Missing parameter 'lineDelimiter'"
    assert "blockSelection" in params, "Missing parameter 'blockSelection'"
    assert "indent" in params, "Missing parameter 'indent'"
    assert "wordWrap" in params, "Missing parameter 'wordWrap'"
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "selectionBackground" in params, "Missing parameter 'selectionBackground'"
    assert "lineSpacing" in params, "Missing parameter 'lineSpacing'"
    assert "group4" in params, "Missing parameter 'group4'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "justify" in params, "Missing parameter 'justify'"

def test_presentation::styledtext_has_caretOffset():
    assert hasattr(presentation::StyledText, "caretOffset")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "caretOffset" in klass.__dict__:
            descriptor = klass.__dict__["caretOffset"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_selectionRanges():
    assert hasattr(presentation::StyledText, "selectionRanges")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "selectionRanges" in klass.__dict__:
            descriptor = klass.__dict__["selectionRanges"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_horizontalIndex():
    assert hasattr(presentation::StyledText, "horizontalIndex")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "horizontalIndex" in klass.__dict__:
            descriptor = klass.__dict__["horizontalIndex"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_bidiColoring():
    assert hasattr(presentation::StyledText, "bidiColoring")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "bidiColoring" in klass.__dict__:
            descriptor = klass.__dict__["bidiColoring"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_topIndex():
    assert hasattr(presentation::StyledText, "topIndex")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "topIndex" in klass.__dict__:
            descriptor = klass.__dict__["topIndex"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_topPixel():
    assert hasattr(presentation::StyledText, "topPixel")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "topPixel" in klass.__dict__:
            descriptor = klass.__dict__["topPixel"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_editable():
    assert hasattr(presentation::StyledText, "editable")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_ranges():
    assert hasattr(presentation::StyledText, "ranges")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_textLimit():
    assert hasattr(presentation::StyledText, "textLimit")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "textLimit" in klass.__dict__:
            descriptor = klass.__dict__["textLimit"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_text():
    assert hasattr(presentation::StyledText, "text")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_tabs():
    assert hasattr(presentation::StyledText, "tabs")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "tabs" in klass.__dict__:
            descriptor = klass.__dict__["tabs"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_selection():
    assert hasattr(presentation::StyledText, "selection")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_selectionText():
    assert hasattr(presentation::StyledText, "selectionText")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "selectionText" in klass.__dict__:
            descriptor = klass.__dict__["selectionText"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_doubleClickEnabled():
    assert hasattr(presentation::StyledText, "doubleClickEnabled")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "doubleClickEnabled" in klass.__dict__:
            descriptor = klass.__dict__["doubleClickEnabled"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_selectionForeground():
    assert hasattr(presentation::StyledText, "selectionForeground")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "selectionForeground" in klass.__dict__:
            descriptor = klass.__dict__["selectionForeground"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_horizontalPixel():
    assert hasattr(presentation::StyledText, "horizontalPixel")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "horizontalPixel" in klass.__dict__:
            descriptor = klass.__dict__["horizontalPixel"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_lineDelimiter():
    assert hasattr(presentation::StyledText, "lineDelimiter")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "lineDelimiter" in klass.__dict__:
            descriptor = klass.__dict__["lineDelimiter"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_blockSelection():
    assert hasattr(presentation::StyledText, "blockSelection")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "blockSelection" in klass.__dict__:
            descriptor = klass.__dict__["blockSelection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_indent():
    assert hasattr(presentation::StyledText, "indent")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "indent" in klass.__dict__:
            descriptor = klass.__dict__["indent"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_wordWrap():
    assert hasattr(presentation::StyledText, "wordWrap")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "wordWrap" in klass.__dict__:
            descriptor = klass.__dict__["wordWrap"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_alignment():
    assert hasattr(presentation::StyledText, "alignment")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_selectionBackground():
    assert hasattr(presentation::StyledText, "selectionBackground")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "selectionBackground" in klass.__dict__:
            descriptor = klass.__dict__["selectionBackground"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_lineSpacing():
    assert hasattr(presentation::StyledText, "lineSpacing")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "lineSpacing" in klass.__dict__:
            descriptor = klass.__dict__["lineSpacing"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_group4():
    assert hasattr(presentation::StyledText, "group4")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_orientation():
    assert hasattr(presentation::StyledText, "orientation")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_presentation::styledtext_has_justify():
    assert hasattr(presentation::StyledText, "justify")
    descriptor = None
    for klass in presentation::StyledText.__mro__:
        if "justify" in klass.__dict__:
            descriptor = klass.__dict__["justify"]
            break
    assert isinstance(descriptor, property)



def test_presentation::viewersorter_is_not_abstract():
    assert not inspect.isabstract(presentation::ViewerSorter)


def test_presentation::viewersorter_constructor_exists():
    assert callable(presentation::ViewerSorter.__init__)


def test_presentation::viewersorter_constructor_args():
    sig = inspect.signature(presentation::ViewerSorter.__init__)
    params = list(sig.parameters.keys())



def test_presentation::viewercomparator_is_not_abstract():
    assert not inspect.isabstract(presentation::ViewerComparator)


def test_presentation::viewercomparator_constructor_exists():
    assert callable(presentation::ViewerComparator.__init__)


def test_presentation::viewercomparator_constructor_args():
    sig = inspect.signature(presentation::ViewerComparator.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::viewercomparator_has_mixed():
    assert hasattr(presentation::ViewerComparator, "mixed")
    descriptor = None
    for klass in presentation::ViewerComparator.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_contentviewer_is_not_abstract():
    assert not inspect.isabstract(ContentViewer)


def test_contentviewer_constructor_exists():
    assert callable(ContentViewer.__init__)


def test_contentviewer_constructor_args():
    sig = inspect.signature(ContentViewer.__init__)
    params = list(sig.parameters.keys())



def test_presentation::structuredviewer_is_not_abstract():
    assert not inspect.isabstract(presentation::StructuredViewer)


def test_presentation::structuredviewer_constructor_exists():
    assert callable(presentation::StructuredViewer.__init__)


def test_presentation::structuredviewer_constructor_args():
    sig = inspect.signature(presentation::StructuredViewer.__init__)
    params = list(sig.parameters.keys())
    assert "useHashlookup" in params, "Missing parameter 'useHashlookup'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_presentation::structuredviewer_has_useHashlookup():
    assert hasattr(presentation::StructuredViewer, "useHashlookup")
    descriptor = None
    for klass in presentation::StructuredViewer.__mro__:
        if "useHashlookup" in klass.__dict__:
            descriptor = klass.__dict__["useHashlookup"]
            break
    assert isinstance(descriptor, property)

def test_presentation::structuredviewer_has_group2():
    assert hasattr(presentation::StructuredViewer, "group2")
    descriptor = None
    for klass in presentation::StructuredViewer.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_presentation::stacklayout_is_not_abstract():
    assert not inspect.isabstract(presentation::StackLayout)


def test_presentation::stacklayout_constructor_exists():
    assert callable(presentation::StackLayout.__init__)


def test_presentation::stacklayout_constructor_args():
    sig = inspect.signature(presentation::StackLayout.__init__)
    params = list(sig.parameters.keys())
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "group" in params, "Missing parameter 'group'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"

def test_presentation::stacklayout_has_marginHeight():
    assert hasattr(presentation::StackLayout, "marginHeight")
    descriptor = None
    for klass in presentation::StackLayout.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::stacklayout_has_group():
    assert hasattr(presentation::StackLayout, "group")
    descriptor = None
    for klass in presentation::StackLayout.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::stacklayout_has_marginWidth():
    assert hasattr(presentation::StackLayout, "marginWidth")
    descriptor = None
    for klass in presentation::StackLayout.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)



def test_presentation::viewerfilter_is_not_abstract():
    assert not inspect.isabstract(presentation::ViewerFilter)


def test_presentation::viewerfilter_constructor_exists():
    assert callable(presentation::ViewerFilter.__init__)


def test_presentation::viewerfilter_constructor_args():
    sig = inspect.signature(presentation::ViewerFilter.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::viewerfilter_has_mixed():
    assert hasattr(presentation::ViewerFilter, "mixed")
    descriptor = None
    for klass in presentation::ViewerFilter.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::spinner_is_not_abstract():
    assert not inspect.isabstract(presentation::Spinner)


def test_presentation::spinner_constructor_exists():
    assert callable(presentation::Spinner.__init__)


def test_presentation::spinner_constructor_args():
    sig = inspect.signature(presentation::Spinner.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "pageIncrement" in params, "Missing parameter 'pageIncrement'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "textLimit" in params, "Missing parameter 'textLimit'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "text" in params, "Missing parameter 'text'"
    assert "digits" in params, "Missing parameter 'digits'"

def test_presentation::spinner_has_selection():
    assert hasattr(presentation::Spinner, "selection")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_pageIncrement():
    assert hasattr(presentation::Spinner, "pageIncrement")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "pageIncrement" in klass.__dict__:
            descriptor = klass.__dict__["pageIncrement"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_increment():
    assert hasattr(presentation::Spinner, "increment")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_maximum():
    assert hasattr(presentation::Spinner, "maximum")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_textLimit():
    assert hasattr(presentation::Spinner, "textLimit")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "textLimit" in klass.__dict__:
            descriptor = klass.__dict__["textLimit"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_minimum():
    assert hasattr(presentation::Spinner, "minimum")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_text():
    assert hasattr(presentation::Spinner, "text")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_presentation::spinner_has_digits():
    assert hasattr(presentation::Spinner, "digits")
    descriptor = None
    for klass in presentation::Spinner.__mro__:
        if "digits" in klass.__dict__:
            descriptor = klass.__dict__["digits"]
            break
    assert isinstance(descriptor, property)



def test_decorations_is_not_abstract():
    assert not inspect.isabstract(Decorations)


def test_decorations_constructor_exists():
    assert callable(Decorations.__init__)


def test_decorations_constructor_args():
    sig = inspect.signature(Decorations.__init__)
    params = list(sig.parameters.keys())



def test_presentation::shell_is_not_abstract():
    assert not inspect.isabstract(presentation::Shell)


def test_presentation::shell_constructor_exists():
    assert callable(presentation::Shell.__init__)


def test_presentation::shell_constructor_args():
    sig = inspect.signature(presentation::Shell.__init__)
    params = list(sig.parameters.keys())
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "minimumSize" in params, "Missing parameter 'minimumSize'"
    assert "imeInputMode" in params, "Missing parameter 'imeInputMode'"
    assert "fullScreen" in params, "Missing parameter 'fullScreen'"
    assert "group5" in params, "Missing parameter 'group5'"

def test_presentation::shell_has_alpha():
    assert hasattr(presentation::Shell, "alpha")
    descriptor = None
    for klass in presentation::Shell.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_presentation::shell_has_minimumSize():
    assert hasattr(presentation::Shell, "minimumSize")
    descriptor = None
    for klass in presentation::Shell.__mro__:
        if "minimumSize" in klass.__dict__:
            descriptor = klass.__dict__["minimumSize"]
            break
    assert isinstance(descriptor, property)

def test_presentation::shell_has_imeInputMode():
    assert hasattr(presentation::Shell, "imeInputMode")
    descriptor = None
    for klass in presentation::Shell.__mro__:
        if "imeInputMode" in klass.__dict__:
            descriptor = klass.__dict__["imeInputMode"]
            break
    assert isinstance(descriptor, property)

def test_presentation::shell_has_fullScreen():
    assert hasattr(presentation::Shell, "fullScreen")
    descriptor = None
    for klass in presentation::Shell.__mro__:
        if "fullScreen" in klass.__dict__:
            descriptor = klass.__dict__["fullScreen"]
            break
    assert isinstance(descriptor, property)

def test_presentation::shell_has_group5():
    assert hasattr(presentation::Shell, "group5")
    descriptor = None
    for klass in presentation::Shell.__mro__:
        if "group5" in klass.__dict__:
            descriptor = klass.__dict__["group5"]
            break
    assert isinstance(descriptor, property)



def test_presentation::slider_is_not_abstract():
    assert not inspect.isabstract(presentation::Slider)


def test_presentation::slider_constructor_exists():
    assert callable(presentation::Slider.__init__)


def test_presentation::slider_constructor_args():
    sig = inspect.signature(presentation::Slider.__init__)
    params = list(sig.parameters.keys())
    assert "pageIncrement" in params, "Missing parameter 'pageIncrement'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "thumb" in params, "Missing parameter 'thumb'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"

def test_presentation::slider_has_pageIncrement():
    assert hasattr(presentation::Slider, "pageIncrement")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "pageIncrement" in klass.__dict__:
            descriptor = klass.__dict__["pageIncrement"]
            break
    assert isinstance(descriptor, property)

def test_presentation::slider_has_increment():
    assert hasattr(presentation::Slider, "increment")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::slider_has_selection():
    assert hasattr(presentation::Slider, "selection")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::slider_has_thumb():
    assert hasattr(presentation::Slider, "thumb")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "thumb" in klass.__dict__:
            descriptor = klass.__dict__["thumb"]
            break
    assert isinstance(descriptor, property)

def test_presentation::slider_has_minimum():
    assert hasattr(presentation::Slider, "minimum")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::slider_has_maximum():
    assert hasattr(presentation::Slider, "maximum")
    descriptor = None
    for klass in presentation::Slider.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)



def test_presentation::scrollbar_is_not_abstract():
    assert not inspect.isabstract(presentation::ScrollBar)


def test_presentation::scrollbar_constructor_exists():
    assert callable(presentation::ScrollBar.__init__)


def test_presentation::scrollbar_constructor_args():
    sig = inspect.signature(presentation::ScrollBar.__init__)
    params = list(sig.parameters.keys())
    assert "thumb" in params, "Missing parameter 'thumb'"
    assert "size" in params, "Missing parameter 'size'"
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "group" in params, "Missing parameter 'group'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "pageIncrement" in params, "Missing parameter 'pageIncrement'"
    assert "maximum" in params, "Missing parameter 'maximum'"

def test_presentation::scrollbar_has_thumb():
    assert hasattr(presentation::ScrollBar, "thumb")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "thumb" in klass.__dict__:
            descriptor = klass.__dict__["thumb"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_size():
    assert hasattr(presentation::ScrollBar, "size")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_enabled():
    assert hasattr(presentation::ScrollBar, "enabled")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_increment():
    assert hasattr(presentation::ScrollBar, "increment")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_group():
    assert hasattr(presentation::ScrollBar, "group")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_visible():
    assert hasattr(presentation::ScrollBar, "visible")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_selection():
    assert hasattr(presentation::ScrollBar, "selection")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_minimum():
    assert hasattr(presentation::ScrollBar, "minimum")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_pageIncrement():
    assert hasattr(presentation::ScrollBar, "pageIncrement")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "pageIncrement" in klass.__dict__:
            descriptor = klass.__dict__["pageIncrement"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollbar_has_maximum():
    assert hasattr(presentation::ScrollBar, "maximum")
    descriptor = None
    for klass in presentation::ScrollBar.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)



def test_presentation::scale_is_not_abstract():
    assert not inspect.isabstract(presentation::Scale)


def test_presentation::scale_constructor_exists():
    assert callable(presentation::Scale.__init__)


def test_presentation::scale_constructor_args():
    sig = inspect.signature(presentation::Scale.__init__)
    params = list(sig.parameters.keys())
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "pageIncrement" in params, "Missing parameter 'pageIncrement'"

def test_presentation::scale_has_maximum():
    assert hasattr(presentation::Scale, "maximum")
    descriptor = None
    for klass in presentation::Scale.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scale_has_selection():
    assert hasattr(presentation::Scale, "selection")
    descriptor = None
    for klass in presentation::Scale.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scale_has_increment():
    assert hasattr(presentation::Scale, "increment")
    descriptor = None
    for klass in presentation::Scale.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scale_has_minimum():
    assert hasattr(presentation::Scale, "minimum")
    descriptor = None
    for klass in presentation::Scale.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scale_has_pageIncrement():
    assert hasattr(presentation::Scale, "pageIncrement")
    descriptor = None
    for klass in presentation::Scale.__mro__:
        if "pageIncrement" in klass.__dict__:
            descriptor = klass.__dict__["pageIncrement"]
            break
    assert isinstance(descriptor, property)



def test_presentation::scrollable_is_not_abstract():
    assert not inspect.isabstract(presentation::Scrollable)


def test_presentation::scrollable_constructor_exists():
    assert callable(presentation::Scrollable.__init__)


def test_presentation::scrollable_constructor_args():
    sig = inspect.signature(presentation::Scrollable.__init__)
    params = list(sig.parameters.keys())
    assert "group1" in params, "Missing parameter 'group1'"
    assert "clientArea" in params, "Missing parameter 'clientArea'"

def test_presentation::scrollable_has_group1():
    assert hasattr(presentation::Scrollable, "group1")
    descriptor = None
    for klass in presentation::Scrollable.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::scrollable_has_clientArea():
    assert hasattr(presentation::Scrollable, "clientArea")
    descriptor = None
    for klass in presentation::Scrollable.__mro__:
        if "clientArea" in klass.__dict__:
            descriptor = klass.__dict__["clientArea"]
            break
    assert isinstance(descriptor, property)



def test_presentation::sash_is_not_abstract():
    assert not inspect.isabstract(presentation::Sash)


def test_presentation::sash_constructor_exists():
    assert callable(presentation::Sash.__init__)


def test_presentation::sash_constructor_args():
    sig = inspect.signature(presentation::Sash.__init__)
    params = list(sig.parameters.keys())



def test_presentation::sashform_is_not_abstract():
    assert not inspect.isabstract(presentation::SashForm)


def test_presentation::sashform_constructor_exists():
    assert callable(presentation::SashForm.__init__)


def test_presentation::sashform_constructor_args():
    sig = inspect.signature(presentation::SashForm.__init__)
    params = list(sig.parameters.keys())
    assert "weights" in params, "Missing parameter 'weights'"
    assert "sashWidth1" in params, "Missing parameter 'sashWidth1'"
    assert "sASHWIDTH" in params, "Missing parameter 'sASHWIDTH'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "group3" in params, "Missing parameter 'group3'"

def test_presentation::sashform_has_weights():
    assert hasattr(presentation::SashForm, "weights")
    descriptor = None
    for klass in presentation::SashForm.__mro__:
        if "weights" in klass.__dict__:
            descriptor = klass.__dict__["weights"]
            break
    assert isinstance(descriptor, property)

def test_presentation::sashform_has_sashWidth1():
    assert hasattr(presentation::SashForm, "sashWidth1")
    descriptor = None
    for klass in presentation::SashForm.__mro__:
        if "sashWidth1" in klass.__dict__:
            descriptor = klass.__dict__["sashWidth1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::sashform_has_sASHWIDTH():
    assert hasattr(presentation::SashForm, "sASHWIDTH")
    descriptor = None
    for klass in presentation::SashForm.__mro__:
        if "sASHWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["sASHWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_presentation::sashform_has_orientation():
    assert hasattr(presentation::SashForm, "orientation")
    descriptor = None
    for klass in presentation::SashForm.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_presentation::sashform_has_group3():
    assert hasattr(presentation::SashForm, "group3")
    descriptor = None
    for klass in presentation::SashForm.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_presentation::rowlayout_is_not_abstract():
    assert not inspect.isabstract(presentation::RowLayout)


def test_presentation::rowlayout_constructor_exists():
    assert callable(presentation::RowLayout.__init__)


def test_presentation::rowlayout_constructor_args():
    sig = inspect.signature(presentation::RowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "pack" in params, "Missing parameter 'pack'"
    assert "center" in params, "Missing parameter 'center'"
    assert "marginRight" in params, "Missing parameter 'marginRight'"
    assert "wrap" in params, "Missing parameter 'wrap'"
    assert "marginLeft" in params, "Missing parameter 'marginLeft'"
    assert "justify" in params, "Missing parameter 'justify'"
    assert "marginTop" in params, "Missing parameter 'marginTop'"
    assert "marginBottom" in params, "Missing parameter 'marginBottom'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "type" in params, "Missing parameter 'type'"
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "fill" in params, "Missing parameter 'fill'"

def test_presentation::rowlayout_has_pack():
    assert hasattr(presentation::RowLayout, "pack")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "pack" in klass.__dict__:
            descriptor = klass.__dict__["pack"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_center():
    assert hasattr(presentation::RowLayout, "center")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "center" in klass.__dict__:
            descriptor = klass.__dict__["center"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginRight():
    assert hasattr(presentation::RowLayout, "marginRight")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginRight" in klass.__dict__:
            descriptor = klass.__dict__["marginRight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_wrap():
    assert hasattr(presentation::RowLayout, "wrap")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "wrap" in klass.__dict__:
            descriptor = klass.__dict__["wrap"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginLeft():
    assert hasattr(presentation::RowLayout, "marginLeft")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginLeft" in klass.__dict__:
            descriptor = klass.__dict__["marginLeft"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_justify():
    assert hasattr(presentation::RowLayout, "justify")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "justify" in klass.__dict__:
            descriptor = klass.__dict__["justify"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginTop():
    assert hasattr(presentation::RowLayout, "marginTop")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginTop" in klass.__dict__:
            descriptor = klass.__dict__["marginTop"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginBottom():
    assert hasattr(presentation::RowLayout, "marginBottom")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginBottom" in klass.__dict__:
            descriptor = klass.__dict__["marginBottom"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginWidth():
    assert hasattr(presentation::RowLayout, "marginWidth")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_type():
    assert hasattr(presentation::RowLayout, "type")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_spacing():
    assert hasattr(presentation::RowLayout, "spacing")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_marginHeight():
    assert hasattr(presentation::RowLayout, "marginHeight")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowlayout_has_fill():
    assert hasattr(presentation::RowLayout, "fill")
    descriptor = None
    for klass in presentation::RowLayout.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)



def test_presentation::rowdata_is_not_abstract():
    assert not inspect.isabstract(presentation::RowData)


def test_presentation::rowdata_constructor_exists():
    assert callable(presentation::RowData.__init__)


def test_presentation::rowdata_constructor_args():
    sig = inspect.signature(presentation::RowData.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "exclude" in params, "Missing parameter 'exclude'"

def test_presentation::rowdata_has_mixed():
    assert hasattr(presentation::RowData, "mixed")
    descriptor = None
    for klass in presentation::RowData.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowdata_has_height():
    assert hasattr(presentation::RowData, "height")
    descriptor = None
    for klass in presentation::RowData.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowdata_has_width():
    assert hasattr(presentation::RowData, "width")
    descriptor = None
    for klass in presentation::RowData.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_presentation::rowdata_has_exclude():
    assert hasattr(presentation::RowData, "exclude")
    descriptor = None
    for klass in presentation::RowData.__mro__:
        if "exclude" in klass.__dict__:
            descriptor = klass.__dict__["exclude"]
            break
    assert isinstance(descriptor, property)



def test_presentation::resource_is_not_abstract():
    assert not inspect.isabstract(presentation::Resource)


def test_presentation::resource_constructor_exists():
    assert callable(presentation::Resource.__init__)


def test_presentation::resource_constructor_args():
    sig = inspect.signature(presentation::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_presentation::resource_has_mixed():
    assert hasattr(presentation::Resource, "mixed")
    descriptor = None
    for klass in presentation::Resource.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_presentation::progressbar_is_not_abstract():
    assert not inspect.isabstract(presentation::ProgressBar)


def test_presentation::progressbar_constructor_exists():
    assert callable(presentation::ProgressBar.__init__)


def test_presentation::progressbar_constructor_args():
    sig = inspect.signature(presentation::ProgressBar.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "selection" in params, "Missing parameter 'selection'"

def test_presentation::progressbar_has_state():
    assert hasattr(presentation::ProgressBar, "state")
    descriptor = None
    for klass in presentation::ProgressBar.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_presentation::progressbar_has_minimum():
    assert hasattr(presentation::ProgressBar, "minimum")
    descriptor = None
    for klass in presentation::ProgressBar.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::progressbar_has_maximum():
    assert hasattr(presentation::ProgressBar, "maximum")
    descriptor = None
    for klass in presentation::ProgressBar.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_presentation::progressbar_has_selection():
    assert hasattr(presentation::ProgressBar, "selection")
    descriptor = None
    for klass in presentation::ProgressBar.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)



def test_abstractdataprovider_is_not_abstract():
    assert not inspect.isabstract(AbstractDataProvider)


def test_abstractdataprovider_constructor_exists():
    assert callable(AbstractDataProvider.__init__)


def test_abstractdataprovider_constructor_args():
    sig = inspect.signature(AbstractDataProvider.__init__)
    params = list(sig.parameters.keys())



def test_presentation::objectdataprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::ObjectDataProvider)


def test_presentation::objectdataprovider_constructor_exists():
    assert callable(presentation::ObjectDataProvider.__init__)


def test_presentation::objectdataprovider_constructor_args():
    sig = inspect.signature(presentation::ObjectDataProvider.__init__)
    params = list(sig.parameters.keys())
    assert "group1" in params, "Missing parameter 'group1'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_presentation::objectdataprovider_has_group1():
    assert hasattr(presentation::ObjectDataProvider, "group1")
    descriptor = None
    for klass in presentation::ObjectDataProvider.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_presentation::objectdataprovider_has_methodName():
    assert hasattr(presentation::ObjectDataProvider, "methodName")
    descriptor = None
    for klass in presentation::ObjectDataProvider.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_presentation::xmldataprovider_is_not_abstract():
    assert not inspect.isabstract(presentation::XMLDataProvider)


def test_presentation::xmldataprovider_constructor_exists():
    assert callable(presentation::XMLDataProvider.__init__)


def test_presentation::xmldataprovider_constructor_args():
    sig = inspect.signature(presentation::XMLDataProvider.__init__)
    params = list(sig.parameters.keys())
    assert "xPath" in params, "Missing parameter 'xPath'"
    assert "group1" in params, "Missing parameter 'group1'"

def test_presentation::xmldataprovider_has_xPath():
    assert hasattr(presentation::XMLDataProvider, "xPath")
    descriptor = None
    for klass in presentation::XMLDataProvider.__mro__:
        if "xPath" in klass.__dict__:
            descriptor = klass.__dict__["xPath"]
            break
    assert isinstance(descriptor, property)

def test_presentation::xmldataprovider_has_group1():
    assert hasattr(presentation::XMLDataProvider, "group1")
    descriptor = None
    for klass in presentation::XMLDataProvider.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
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
Dialog_strategy = st.builds(
    Dialog,
)
presentation::MessageBox_strategy = st.builds(
    presentation::MessageBox,
    message=
        safe_text
)
presentation::Observable_strategy = st.builds(
    presentation::Observable,
    mixed=
        safe_text
)
presentation::Listener_strategy = st.builds(
    presentation::Listener,
    mixed=
        safe_text
)
presentation::ISelection_strategy = st.builds(
    presentation::ISelection,
    mixed=
        safe_text
)
presentation::TextStyle_strategy = st.builds(
    presentation::TextStyle,
    mixed=
        safe_text
)
presentation::IElementComparer_strategy = st.builds(
    presentation::IElementComparer,
    mixed=
        safe_text
)
presentation::GridData_strategy = st.builds(
    presentation::GridData,
    exclude=
        safe_text,
    horizontalIndent=
        safe_text,
    mixed=
        safe_text,
    verticalAlignment=
        safe_text,
    grabExcessVerticalSpace=
        safe_text,
    minimumHeight=
        safe_text,
    horizontalAlignment=
        safe_text,
    horizontalSpan=
        safe_text,
    minimumWidth=
        safe_text,
    heightHint=
        safe_text,
    verticalIndent=
        safe_text,
    verticalSpan=
        safe_text,
    grabExcessHorizontalSpace=
        safe_text,
    widthHint=
        safe_text
)
presentation::FormAttachment_strategy = st.builds(
    presentation::FormAttachment,
    mixed=
        safe_text,
    alignment=
        safe_text,
    numerator=
        safe_text,
    group=
        safe_text,
    offset=
        safe_text,
    denominator=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
presentation::FormLayout_strategy = st.builds(
    presentation::FormLayout,
    marginLeft=
        safe_text,
    marginHeight=
        safe_text,
    spacing=
        safe_text,
    marginBottom=
        safe_text,
    marginRight=
        safe_text,
    marginTop=
        safe_text,
    marginWidth=
        safe_text
)
presentation::GridLayout_strategy = st.builds(
    presentation::GridLayout,
    marginLeft=
        safe_text,
    makeColumnsEqualWidth=
        safe_text,
    numColumns=
        safe_text,
    marginBottom=
        safe_text,
    marginWidth=
        safe_text,
    marginTop=
        safe_text,
    marginRight=
        safe_text,
    verticalSpacing=
        safe_text,
    marginHeight=
        safe_text,
    horizontalSpacing=
        safe_text
)
presentation::FillLayout_strategy = st.builds(
    presentation::FillLayout,
    marginHeight=
        safe_text,
    type=
        safe_text,
    spacing=
        safe_text,
    marginWidth=
        safe_text
)
presentation::FormData_strategy = st.builds(
    presentation::FormData,
    height=
        safe_text,
    width=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text
)
DocumentObject_strategy = st.builds(
    DocumentObject,
)
presentation::Element_strategy = st.builds(
    presentation::Element,
)
presentation::Window_strategy = st.builds(
    presentation::Window,
    blockOnOpen=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text
)
presentation::DocumentRoot_strategy = st.builds(
    presentation::DocumentRoot,
    mixed=
        safe_text
)
Observable_strategy = st.builds(
    Observable,
)
presentation::DocumentObject_strategy = st.builds(
    presentation::DocumentObject,
)
presentation::Document_strategy = st.builds(
    presentation::Document,
    mixed=
        safe_text
)
presentation::DialogTray_strategy = st.builds(
    presentation::DialogTray,
    mixed=
        safe_text
)
presentation::IDialogBlockedHandler_strategy = st.builds(
    presentation::IDialogBlockedHandler,
    mixed=
        safe_text
)
Window_strategy = st.builds(
    Window,
)
presentation::Dialog_strategy = st.builds(
    presentation::Dialog,
    group1=
        safe_text
)
presentation::EStringToStringMapEntry_strategy = st.builds(
    presentation::EStringToStringMapEntry,
)
presentation::DefaultCellModifier_strategy = st.builds(
    presentation::DefaultCellModifier,
    mixed=
        safe_text
)
presentation::DefaultLabelProvider_strategy = st.builds(
    presentation::DefaultLabelProvider,
    mixed=
        safe_text
)
Resource_strategy = st.builds(
    Resource,
)
presentation::RGB_strategy = st.builds(
    presentation::RGB,
    mixed=
        safe_text
)
Item_strategy = st.builds(
    Item,
)
presentation::CTabItem_strategy = st.builds(
    presentation::CTabItem,
    group=
        safe_text,
    showClose=
        safe_text,
    bounds=
        safe_text,
    disabledImage=
        safe_text,
    toolTipText=
        safe_text,
    font=
        safe_text
)
presentation::ExpandItem_strategy = st.builds(
    presentation::ExpandItem,
    expanded=
        safe_text,
    group=
        safe_text,
    height=
        safe_text
)
presentation::MenuItem_strategy = st.builds(
    presentation::MenuItem,
    selection=
        safe_text,
    accelerator=
        safe_text,
    group=
        safe_text,
    enabled=
        safe_text
)
presentation::CoolItem_strategy = st.builds(
    presentation::CoolItem,
    bounds=
        safe_text,
    group=
        safe_text,
    size=
        safe_text,
    preferredSize=
        safe_text,
    minimumSize=
        safe_text
)
presentation::ControlEditor_strategy = st.builds(
    presentation::ControlEditor,
    mixed=
        safe_text,
    horizontalAlignment=
        safe_text,
    minimumHeight=
        safe_text,
    group=
        safe_text,
    verticalAlignment=
        safe_text,
    grabHorizontal=
        safe_text,
    grabVertical=
        safe_text,
    minimumWidth=
        safe_text
)
presentation::Cursor_strategy = st.builds(
    presentation::Cursor,
)
presentation::IContentProvider_strategy = st.builds(
    presentation::IContentProvider,
    mixed=
        safe_text
)
Viewer_strategy = st.builds(
    Viewer,
)
presentation::ContentViewer_strategy = st.builds(
    presentation::ContentViewer,
    group1=
        safe_text
)
presentation::Layout_strategy = st.builds(
    presentation::Layout,
    mixed=
        safe_text
)
Scrollable_strategy = st.builds(
    Scrollable,
)
presentation::List_strategy = st.builds(
    presentation::List,
    selection=
        safe_text,
    selectionIndices=
        safe_text,
    items=
        safe_text,
    topIndex=
        safe_text,
    group2=
        safe_text
)
presentation::Composite_strategy = st.builds(
    presentation::Composite,
    group2=
        safe_text,
    backgroundMode=
        safe_text,
    layoutDeferred=
        safe_text
)
AbstractListViewer_strategy = st.builds(
    AbstractListViewer,
)
presentation::ListViewer_strategy = st.builds(
    presentation::ListViewer,
    group3=
        safe_text
)
presentation::ComboViewer_strategy = st.builds(
    presentation::ComboViewer,
)
presentation::IBaseLabelProvider_strategy = st.builds(
    presentation::IBaseLabelProvider,
    mixed=
        safe_text
)
presentation::IStructuredContentProvider_strategy = st.builds(
    presentation::IStructuredContentProvider,
    mixed=
        safe_text
)
AbstractComboBoxCellEditor_strategy = st.builds(
    AbstractComboBoxCellEditor,
)
presentation::ComboBoxViewerCellEditor_strategy = st.builds(
    presentation::ComboBoxViewerCellEditor,
    group1=
        safe_text
)
presentation::ComboBoxCellEditor_strategy = st.builds(
    presentation::ComboBoxCellEditor,
)
presentation::ICellModifier_strategy = st.builds(
    presentation::ICellModifier,
    mixed=
        safe_text
)
presentation::ColumnViewerEditor_strategy = st.builds(
    presentation::ColumnViewerEditor,
    mixed=
        safe_text
)
DialogCellEditor_strategy = st.builds(
    DialogCellEditor,
)
presentation::ColorCellEditor_strategy = st.builds(
    presentation::ColorCellEditor,
)
presentation::Class_strategy = st.builds(
    presentation::Class,
    mixed=
        safe_text
)
Canvas_strategy = st.builds(
    Canvas,
)
presentation::Decorations_strategy = st.builds(
    presentation::Decorations,
    text=
        safe_text,
    image=
        safe_text,
    images=
        safe_text,
    maximized=
        safe_text,
    minimized=
        safe_text,
    group4=
        safe_text
)
presentation::CLabel_strategy = st.builds(
    presentation::CLabel,
    alignment=
        safe_text,
    text=
        safe_text,
    image=
        safe_text
)
TreeViewer_strategy = st.builds(
    TreeViewer,
)
presentation::CheckboxTreeViewer_strategy = st.builds(
    presentation::CheckboxTreeViewer,
    allChecked=
        safe_text,
    group6=
        safe_text
)
presentation::Collection_strategy = st.builds(
    presentation::Collection,
    mixed=
        safe_text
)
presentation::ICheckStateProvider_strategy = st.builds(
    presentation::ICheckStateProvider,
    mixed=
        safe_text
)
TableViewer_strategy = st.builds(
    TableViewer,
)
presentation::CheckboxTableViewer_strategy = st.builds(
    presentation::CheckboxTableViewer,
    group5=
        safe_text,
    allGrayed=
        safe_text,
    allChecked=
        safe_text
)
presentation::LayoutData_strategy = st.builds(
    presentation::LayoutData,
    mixed=
        safe_text
)
presentation::ICellEditorValidator_strategy = st.builds(
    presentation::ICellEditorValidator,
    mixed=
        safe_text
)
presentation::TableItem_strategy = st.builds(
    presentation::TableItem,
    group=
        safe_text,
    texts=
        safe_text,
    checked=
        safe_text,
    imageIndent=
        safe_text,
    grayed=
        safe_text
)
presentation::Cell_strategy = st.builds(
    presentation::Cell,
    image=
        safe_text,
    text=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text
)
presentation::CellEditor_strategy = st.builds(
    presentation::CellEditor,
    errorMessage=
        safe_text,
    style=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
Widget_strategy = st.builds(
    Widget,
)
presentation::Item_strategy = st.builds(
    presentation::Item,
    text=
        safe_text,
    image=
        safe_text
)
presentation::Menu_strategy = st.builds(
    presentation::Menu,
    group=
        safe_text,
    handle=
        safe_text,
    visible=
        safe_text,
    enabled=
        safe_text
)
presentation::Control_strategy = st.builds(
    presentation::Control,
    group=
        safe_text,
    backgroundImage=
        safe_text,
    size=
        safe_text,
    visible=
        safe_text,
    location=
        safe_text,
    font=
        safe_text,
    background=
        safe_text,
    handle=
        safe_text,
    capture=
        safe_text,
    enabled=
        safe_text,
    foreground=
        safe_text,
    bounds=
        safe_text,
    toolTipText=
        safe_text,
    redraw=
        safe_text,
    dragDetect=
        safe_text
)
presentation::Caret_strategy = st.builds(
    presentation::Caret,
    size=
        safe_text,
    bounds=
        safe_text,
    location=
        safe_text,
    font=
        safe_text,
    visible=
        safe_text,
    image=
        safe_text,
    group=
        safe_text
)
presentation::IME_strategy = st.builds(
    presentation::IME,
    ranges=
        safe_text,
    text=
        safe_text,
    group=
        safe_text,
    compositionOffset=
        safe_text
)
presentation::ICommand_strategy = st.builds(
    presentation::ICommand,
    mixed=
        safe_text
)
Control_strategy = st.builds(
    Control,
)
presentation::Link_strategy = st.builds(
    presentation::Link,
    text=
        safe_text
)
presentation::Label_strategy = st.builds(
    presentation::Label,
    image=
        safe_text,
    alignment=
        safe_text,
    text=
        safe_text
)
presentation::Button_strategy = st.builds(
    presentation::Button,
    selection=
        safe_text,
    group1=
        safe_text,
    grayed=
        safe_text,
    image=
        safe_text,
    alignment=
        safe_text,
    text=
        safe_text
)
Composite_strategy = st.builds(
    Composite,
)
presentation::CTabFolder_strategy = st.builds(
    presentation::CTabFolder,
    group3=
        safe_text,
    mINTABWIDTH=
        safe_text,
    minimized=
        safe_text,
    mRUVisible=
        safe_text,
    tabPosition=
        safe_text,
    marginWidth=
        safe_text,
    borderVisible=
        safe_text,
    single=
        safe_text,
    maximizeVisible=
        safe_text,
    maximized=
        safe_text,
    minimizeVisible=
        safe_text,
    selectionForeground=
        safe_text,
    unselectedImageVisible=
        safe_text,
    unselectedCloseVisible=
        safe_text,
    tabHeight=
        safe_text,
    selectionBackground=
        safe_text,
    minimumCharacters=
        safe_text,
    simple=
        safe_text,
    marginHeight=
        safe_text
)
presentation::Combo_strategy = st.builds(
    presentation::Combo,
    text=
        safe_text,
    group3=
        safe_text,
    listVisible=
        safe_text,
    visibleItemCount=
        safe_text,
    items=
        safe_text,
    textLimit=
        safe_text,
    selection=
        safe_text,
    orientation=
        safe_text
)
presentation::Group_strategy = st.builds(
    presentation::Group,
    text=
        safe_text
)
presentation::CCombo_strategy = st.builds(
    presentation::CCombo,
    selection=
        safe_text,
    editable=
        safe_text,
    visibleItemCount=
        safe_text,
    listVisible=
        safe_text,
    text=
        safe_text,
    items=
        safe_text,
    group3=
        safe_text,
    textLimit=
        safe_text
)
presentation::ExpandBar_strategy = st.builds(
    presentation::ExpandBar,
    group3=
        safe_text,
    spacing=
        safe_text
)
presentation::DateTime_strategy = st.builds(
    presentation::DateTime,
    minutes=
        safe_text,
    seconds=
        safe_text,
    day=
        safe_text,
    hours=
        safe_text,
    month=
        safe_text,
    year=
        safe_text
)
presentation::Canvas_strategy = st.builds(
    presentation::Canvas,
    mixed1=
        safe_text,
    group3=
        safe_text
)
presentation::CoolBar_strategy = st.builds(
    presentation::CoolBar,
    locked=
        safe_text,
    itemOrder=
        safe_text,
    itemSizes=
        safe_text,
    group3=
        safe_text,
    wrapIndices=
        safe_text
)
presentation::Browser_strategy = st.builds(
    presentation::Browser,
    url=
        safe_text,
    group3=
        safe_text,
    browserType=
        safe_text,
    text=
        safe_text
)
presentation::Binding_strategy = st.builds(
    presentation::Binding,
    elementName=
        safe_text,
    xPath=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text,
    path=
        safe_text
)
presentation::Accessible_strategy = st.builds(
    presentation::Accessible,
    mixed=
        safe_text
)
presentation::EObject_strategy = st.builds(
    presentation::EObject,
)
presentation::TreePath_strategy = st.builds(
    presentation::TreePath,
    mixed=
        safe_text
)
presentation::Widget_strategy = st.builds(
    presentation::Widget,
    mouseMoveEvent=
        safe_text,
    activateEvent=
        safe_text,
    mouseUpEvent=
        safe_text,
    hideEvent=
        safe_text,
    showEvent=
        safe_text,
    focusInEvent=
        safe_text,
    mouseDownEvent=
        safe_text,
    style=
        safe_text,
    mouseWheelEvent=
        safe_text,
    mouseEnterEvent=
        safe_text,
    hardKeyDownEvent=
        safe_text,
    modifyEvent=
        safe_text,
    deactivateEvent=
        safe_text,
    keyDownEvent=
        safe_text,
    moveEvent=
        safe_text,
    keyUpEvent=
        safe_text,
    helpEvent=
        safe_text,
    verifyEvent=
        safe_text,
    disposeEvent=
        safe_text,
    armEvent=
        safe_text,
    mouseHoverEvent=
        safe_text,
    measureItemEvent=
        safe_text,
    mouseExitEvent=
        safe_text,
    traverseEvent=
        safe_text,
    collapseEvent=
        safe_text,
    setDataEvent=
        safe_text,
    dataContext=
        safe_text,
    resizeEvent=
        safe_text,
    menuDetectEvent=
        safe_text,
    deiconifyEvent=
        safe_text,
    defaultSelectionEvent=
        safe_text,
    closeEvent=
        safe_text,
    mouseDoubleClickEvent=
        safe_text,
    selectionEvent=
        safe_text,
    iconifyEvent=
        safe_text,
    hardKeyUpEvent=
        safe_text,
    dragDetectEvent=
        safe_text,
    mixed=
        safe_text,
    imeCompositionEvent=
        safe_text,
    paintEvent=
        safe_text,
    focusOutEvent=
        safe_text,
    expandEvent=
        safe_text,
    eraseItemEvent=
        safe_text,
    paintItemEvent=
        safe_text
)
ColumnViewer_strategy = st.builds(
    ColumnViewer,
)
presentation::AbstractTreeViewer_strategy = st.builds(
    presentation::AbstractTreeViewer,
    autoExpandLevel=
        safe_text,
    group4=
        safe_text
)
presentation::AbstractTableViewer_strategy = st.builds(
    presentation::AbstractTableViewer,
    itemCount=
        safe_text
)
StructuredViewer_strategy = st.builds(
    StructuredViewer,
)
presentation::ColumnViewer_strategy = st.builds(
    presentation::ColumnViewer,
    group3=
        safe_text
)
presentation::AbstractListViewer_strategy = st.builds(
    presentation::AbstractListViewer,
)
presentation::IBindingContext_strategy = st.builds(
    presentation::IBindingContext,
    mixed=
        safe_text
)
presentation::AbstractDataProvider_strategy = st.builds(
    presentation::AbstractDataProvider,
    group=
        safe_text,
    mixed=
        safe_text,
    key=
        safe_text
)
CellEditor_strategy = st.builds(
    CellEditor,
)
presentation::DialogCellEditor_strategy = st.builds(
    presentation::DialogCellEditor,
)
presentation::CheckboxCellEditor_strategy = st.builds(
    presentation::CheckboxCellEditor,
)
presentation::AbstractComboBoxCellEditor_strategy = st.builds(
    presentation::AbstractComboBoxCellEditor,
    activationStyle=
        safe_text
)
presentation::WindowManager_strategy = st.builds(
    presentation::WindowManager,
    mixed=
        safe_text
)
ViewerComparator_strategy = st.builds(
    ViewerComparator,
)
presentation::ViewerColumn_strategy = st.builds(
    presentation::ViewerColumn,
    mixed=
        safe_text
)
presentation::Viewer_strategy = st.builds(
    presentation::Viewer,
    group=
        safe_text,
    mixed=
        safe_text
)
presentation::URL_strategy = st.builds(
    presentation::URL,
    mixed=
        safe_text
)
presentation::TreeItem_strategy = st.builds(
    presentation::TreeItem,
    grayed=
        safe_text,
    checked=
        safe_text,
    group=
        safe_text,
    itemCount=
        safe_text,
    expanded=
        safe_text,
    texts=
        safe_text,
    handle=
        safe_text
)
presentation::TreeColumn_strategy = st.builds(
    presentation::TreeColumn,
    width=
        safe_text,
    toolTipText=
        safe_text,
    group=
        safe_text,
    alignment=
        safe_text,
    resizable=
        safe_text,
    moveable=
        safe_text
)
presentation::Tree_strategy = st.builds(
    presentation::Tree,
    columnOrder=
        safe_text,
    group3=
        safe_text,
    itemCount=
        safe_text,
    sortDirection=
        safe_text,
    linesVisible=
        safe_text,
    headerVisible=
        safe_text
)
presentation::TrayDialog_strategy = st.builds(
    presentation::TrayDialog,
    group2=
        safe_text,
    helpAvailable=
        safe_text
)
presentation::TrayItem_strategy = st.builds(
    presentation::TrayItem,
)
presentation::Tray_strategy = st.builds(
    presentation::Tray,
    group=
        safe_text
)
presentation::Tracker_strategy = st.builds(
    presentation::Tracker,
    rectangles=
        safe_text,
    group=
        safe_text,
    stippled=
        safe_text
)
presentation::ToolTip_strategy = st.builds(
    presentation::ToolTip,
    autoHide=
        safe_text,
    message=
        safe_text,
    text=
        safe_text,
    group=
        safe_text,
    visible=
        safe_text
)
presentation::ToolItem_strategy = st.builds(
    presentation::ToolItem,
    enabled=
        safe_text,
    group=
        safe_text,
    hotImage=
        safe_text,
    toolTipText=
        safe_text,
    disabledImage=
        safe_text,
    selection=
        safe_text,
    width=
        safe_text,
    bounds=
        safe_text
)
presentation::ToolBar_strategy = st.builds(
    presentation::ToolBar,
    group3=
        safe_text
)
TrayDialog_strategy = st.builds(
    TrayDialog,
)
presentation::TitleAreaDialog_strategy = st.builds(
    presentation::TitleAreaDialog,
    titleImage=
        safe_text,
    message=
        safe_text,
    errorMessage=
        safe_text,
    title=
        safe_text,
    group3=
        safe_text
)
presentation::TextCellEditor_strategy = st.builds(
    presentation::TextCellEditor,
)
presentation::Text_strategy = st.builds(
    presentation::Text,
    textLimit=
        safe_text,
    orientation=
        safe_text,
    editable=
        safe_text,
    topIndex=
        safe_text,
    echoChar=
        safe_text,
    doubleClickEnabled=
        safe_text,
    selectionText=
        safe_text,
    text=
        safe_text,
    caretLocation=
        safe_text,
    lineDelimiter=
        safe_text,
    tabs=
        safe_text,
    selection=
        safe_text,
    message=
        safe_text
)
AbstractTableViewer_strategy = st.builds(
    AbstractTableViewer,
)
presentation::TableViewer_strategy = st.builds(
    presentation::TableViewer,
    group4=
        safe_text
)
AbstractTreeViewer_strategy = st.builds(
    AbstractTreeViewer,
)
presentation::TreeViewer_strategy = st.builds(
    presentation::TreeViewer,
    group5=
        safe_text
)
presentation::TableTreeViewer_strategy = st.builds(
    presentation::TableTreeViewer,
    group5=
        safe_text
)
presentation::TableTree_strategy = st.builds(
    presentation::TableTree,
)
ViewerColumn_strategy = st.builds(
    ViewerColumn,
)
presentation::TableViewerColumn_strategy = st.builds(
    presentation::TableViewerColumn,
    group=
        safe_text,
    width=
        safe_text,
    text=
        safe_text
)
ControlEditor_strategy = st.builds(
    ControlEditor,
)
presentation::TableEditor_strategy = st.builds(
    presentation::TableEditor,
    dynamic=
        safe_text,
    column=
        safe_text,
    group1=
        safe_text
)
presentation::TableColumn_strategy = st.builds(
    presentation::TableColumn,
    alignment=
        safe_text,
    width=
        safe_text,
    resizable=
        safe_text,
    moveable=
        safe_text,
    toolTipText=
        safe_text,
    group=
        safe_text
)
presentation::Table_strategy = st.builds(
    presentation::Table,
    topIndex=
        safe_text,
    sortDirection=
        safe_text,
    group3=
        safe_text,
    selectionIndices=
        safe_text,
    columnOrder=
        safe_text,
    linesVisible=
        safe_text,
    itemCount=
        safe_text,
    headerVisible=
        safe_text
)
presentation::TabFolder_strategy = st.builds(
    presentation::TabFolder,
    group3=
        safe_text
)
TextStyle_strategy = st.builds(
    TextStyle,
)
presentation::TabItem_strategy = st.builds(
    presentation::TabItem,
    group=
        safe_text,
    toolTipText=
        safe_text,
    bounds=
        safe_text
)
presentation::StyledTextContent_strategy = st.builds(
    presentation::StyledTextContent,
    mixed=
        safe_text
)
presentation::StyleRange_strategy = st.builds(
    presentation::StyleRange,
)
presentation::StyledText_strategy = st.builds(
    presentation::StyledText,
    caretOffset=
        safe_text,
    selectionRanges=
        safe_text,
    horizontalIndex=
        safe_text,
    bidiColoring=
        safe_text,
    topIndex=
        safe_text,
    topPixel=
        safe_text,
    editable=
        safe_text,
    ranges=
        safe_text,
    textLimit=
        safe_text,
    text=
        safe_text,
    tabs=
        safe_text,
    selection=
        safe_text,
    selectionText=
        safe_text,
    doubleClickEnabled=
        safe_text,
    selectionForeground=
        safe_text,
    horizontalPixel=
        safe_text,
    lineDelimiter=
        safe_text,
    blockSelection=
        safe_text,
    indent=
        safe_text,
    wordWrap=
        safe_text,
    alignment=
        safe_text,
    selectionBackground=
        safe_text,
    lineSpacing=
        safe_text,
    group4=
        safe_text,
    orientation=
        safe_text,
    justify=
        safe_text
)
presentation::ViewerSorter_strategy = st.builds(
    presentation::ViewerSorter,
)
presentation::ViewerComparator_strategy = st.builds(
    presentation::ViewerComparator,
    mixed=
        safe_text
)
ContentViewer_strategy = st.builds(
    ContentViewer,
)
presentation::StructuredViewer_strategy = st.builds(
    presentation::StructuredViewer,
    useHashlookup=
        safe_text,
    group2=
        safe_text
)
presentation::StackLayout_strategy = st.builds(
    presentation::StackLayout,
    marginHeight=
        safe_text,
    group=
        safe_text,
    marginWidth=
        safe_text
)
presentation::ViewerFilter_strategy = st.builds(
    presentation::ViewerFilter,
    mixed=
        safe_text
)
presentation::Spinner_strategy = st.builds(
    presentation::Spinner,
    selection=
        safe_text,
    pageIncrement=
        safe_text,
    increment=
        safe_text,
    maximum=
        safe_text,
    textLimit=
        safe_text,
    minimum=
        safe_text,
    text=
        safe_text,
    digits=
        safe_text
)
Decorations_strategy = st.builds(
    Decorations,
)
presentation::Shell_strategy = st.builds(
    presentation::Shell,
    alpha=
        safe_text,
    minimumSize=
        safe_text,
    imeInputMode=
        safe_text,
    fullScreen=
        safe_text,
    group5=
        safe_text
)
presentation::Slider_strategy = st.builds(
    presentation::Slider,
    pageIncrement=
        safe_text,
    increment=
        safe_text,
    selection=
        safe_text,
    thumb=
        safe_text,
    minimum=
        safe_text,
    maximum=
        safe_text
)
presentation::ScrollBar_strategy = st.builds(
    presentation::ScrollBar,
    thumb=
        safe_text,
    size=
        safe_text,
    enabled=
        safe_text,
    increment=
        safe_text,
    group=
        safe_text,
    visible=
        safe_text,
    selection=
        safe_text,
    minimum=
        safe_text,
    pageIncrement=
        safe_text,
    maximum=
        safe_text
)
presentation::Scale_strategy = st.builds(
    presentation::Scale,
    maximum=
        safe_text,
    selection=
        safe_text,
    increment=
        safe_text,
    minimum=
        safe_text,
    pageIncrement=
        safe_text
)
presentation::Scrollable_strategy = st.builds(
    presentation::Scrollable,
    group1=
        safe_text,
    clientArea=
        safe_text
)
presentation::Sash_strategy = st.builds(
    presentation::Sash,
)
presentation::SashForm_strategy = st.builds(
    presentation::SashForm,
    weights=
        safe_text,
    sashWidth1=
        safe_text,
    sASHWIDTH=
        safe_text,
    orientation=
        safe_text,
    group3=
        safe_text
)
presentation::RowLayout_strategy = st.builds(
    presentation::RowLayout,
    pack=
        safe_text,
    center=
        safe_text,
    marginRight=
        safe_text,
    wrap=
        safe_text,
    marginLeft=
        safe_text,
    justify=
        safe_text,
    marginTop=
        safe_text,
    marginBottom=
        safe_text,
    marginWidth=
        safe_text,
    type=
        safe_text,
    spacing=
        safe_text,
    marginHeight=
        safe_text,
    fill=
        safe_text
)
presentation::RowData_strategy = st.builds(
    presentation::RowData,
    mixed=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    exclude=
        safe_text
)
presentation::Resource_strategy = st.builds(
    presentation::Resource,
    mixed=
        safe_text
)
presentation::ProgressBar_strategy = st.builds(
    presentation::ProgressBar,
    state=
        safe_text,
    minimum=
        safe_text,
    maximum=
        safe_text,
    selection=
        safe_text
)
AbstractDataProvider_strategy = st.builds(
    AbstractDataProvider,
)
presentation::ObjectDataProvider_strategy = st.builds(
    presentation::ObjectDataProvider,
    group1=
        safe_text,
    methodName=
        safe_text
)
presentation::XMLDataProvider_strategy = st.builds(
    presentation::XMLDataProvider,
    xPath=
        safe_text,
    group1=
        safe_text
)

@given(instance=Dialog_strategy)
@settings(max_examples=50)
def test_dialog_instantiation(instance):
    assert isinstance(instance, Dialog)

@given(instance=presentation::MessageBox_strategy)
@settings(max_examples=50)
def test_presentation::messagebox_instantiation(instance):
    assert isinstance(instance, presentation::MessageBox)

@given(instance=presentation::MessageBox_strategy)
def test_presentation::messagebox_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=presentation::MessageBox_strategy)
def test_presentation::messagebox_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=presentation::Observable_strategy)
@settings(max_examples=50)
def test_presentation::observable_instantiation(instance):
    assert isinstance(instance, presentation::Observable)

@given(instance=presentation::Observable_strategy)
def test_presentation::observable_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Observable_strategy)
def test_presentation::observable_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Listener_strategy)
@settings(max_examples=50)
def test_presentation::listener_instantiation(instance):
    assert isinstance(instance, presentation::Listener)

@given(instance=presentation::Listener_strategy)
def test_presentation::listener_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Listener_strategy)
def test_presentation::listener_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ISelection_strategy)
@settings(max_examples=50)
def test_presentation::iselection_instantiation(instance):
    assert isinstance(instance, presentation::ISelection)

@given(instance=presentation::ISelection_strategy)
def test_presentation::iselection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ISelection_strategy)
def test_presentation::iselection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::TextStyle_strategy)
@settings(max_examples=50)
def test_presentation::textstyle_instantiation(instance):
    assert isinstance(instance, presentation::TextStyle)

@given(instance=presentation::TextStyle_strategy)
def test_presentation::textstyle_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::TextStyle_strategy)
def test_presentation::textstyle_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::IElementComparer_strategy)
@settings(max_examples=50)
def test_presentation::ielementcomparer_instantiation(instance):
    assert isinstance(instance, presentation::IElementComparer)

@given(instance=presentation::IElementComparer_strategy)
def test_presentation::ielementcomparer_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IElementComparer_strategy)
def test_presentation::ielementcomparer_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::GridData_strategy)
@settings(max_examples=50)
def test_presentation::griddata_instantiation(instance):
    assert isinstance(instance, presentation::GridData)

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_exclude_type(instance):
    assert isinstance(instance.exclude, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_exclude_setter(instance):
    original = instance.exclude
    instance.exclude = original
    assert instance.exclude == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalIndent_type(instance):
    assert isinstance(instance.horizontalIndent, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_grabExcessVerticalSpace_type(instance):
    assert isinstance(instance.grabExcessVerticalSpace, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_minimumHeight_type(instance):
    assert isinstance(instance.minimumHeight, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_minimumHeight_setter(instance):
    original = instance.minimumHeight
    instance.minimumHeight = original
    assert instance.minimumHeight == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalSpan_type(instance):
    assert isinstance(instance.horizontalSpan, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_minimumWidth_type(instance):
    assert isinstance(instance.minimumWidth, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_minimumWidth_setter(instance):
    original = instance.minimumWidth
    instance.minimumWidth = original
    assert instance.minimumWidth == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_heightHint_type(instance):
    assert isinstance(instance.heightHint, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_heightHint_setter(instance):
    original = instance.heightHint
    instance.heightHint = original
    assert instance.heightHint == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalIndent_type(instance):
    assert isinstance(instance.verticalIndent, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalIndent_setter(instance):
    original = instance.verticalIndent
    instance.verticalIndent = original
    assert instance.verticalIndent == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalSpan_type(instance):
    assert isinstance(instance.verticalSpan, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_grabExcessHorizontalSpace_type(instance):
    assert isinstance(instance.grabExcessHorizontalSpace, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original

@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_widthHint_type(instance):
    assert isinstance(instance.widthHint, str)


@given(instance=presentation::GridData_strategy)
def test_presentation::griddata_widthHint_setter(instance):
    original = instance.widthHint
    instance.widthHint = original
    assert instance.widthHint == original

@given(instance=presentation::FormAttachment_strategy)
@settings(max_examples=50)
def test_presentation::formattachment_instantiation(instance):
    assert isinstance(instance, presentation::FormAttachment)

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_numerator_type(instance):
    assert isinstance(instance.numerator, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_numerator_setter(instance):
    original = instance.numerator
    instance.numerator = original
    assert instance.numerator == original

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_denominator_type(instance):
    assert isinstance(instance.denominator, str)


@given(instance=presentation::FormAttachment_strategy)
def test_presentation::formattachment_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=presentation::FormLayout_strategy)
@settings(max_examples=50)
def test_presentation::formlayout_instantiation(instance):
    assert isinstance(instance, presentation::FormLayout)

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginLeft_type(instance):
    assert isinstance(instance.marginLeft, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginLeft_setter(instance):
    original = instance.marginLeft
    instance.marginLeft = original
    assert instance.marginLeft == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_spacing_type(instance):
    assert isinstance(instance.spacing, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginBottom_type(instance):
    assert isinstance(instance.marginBottom, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginBottom_setter(instance):
    original = instance.marginBottom
    instance.marginBottom = original
    assert instance.marginBottom == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginRight_type(instance):
    assert isinstance(instance.marginRight, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginRight_setter(instance):
    original = instance.marginRight
    instance.marginRight = original
    assert instance.marginRight == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginTop_type(instance):
    assert isinstance(instance.marginTop, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginTop_setter(instance):
    original = instance.marginTop
    instance.marginTop = original
    assert instance.marginTop == original

@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::FormLayout_strategy)
def test_presentation::formlayout_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::GridLayout_strategy)
@settings(max_examples=50)
def test_presentation::gridlayout_instantiation(instance):
    assert isinstance(instance, presentation::GridLayout)

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginLeft_type(instance):
    assert isinstance(instance.marginLeft, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginLeft_setter(instance):
    original = instance.marginLeft
    instance.marginLeft = original
    assert instance.marginLeft == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_makeColumnsEqualWidth_type(instance):
    assert isinstance(instance.makeColumnsEqualWidth, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_makeColumnsEqualWidth_setter(instance):
    original = instance.makeColumnsEqualWidth
    instance.makeColumnsEqualWidth = original
    assert instance.makeColumnsEqualWidth == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_numColumns_type(instance):
    assert isinstance(instance.numColumns, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginBottom_type(instance):
    assert isinstance(instance.marginBottom, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginBottom_setter(instance):
    original = instance.marginBottom
    instance.marginBottom = original
    assert instance.marginBottom == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginTop_type(instance):
    assert isinstance(instance.marginTop, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginTop_setter(instance):
    original = instance.marginTop
    instance.marginTop = original
    assert instance.marginTop == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginRight_type(instance):
    assert isinstance(instance.marginRight, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginRight_setter(instance):
    original = instance.marginRight
    instance.marginRight = original
    assert instance.marginRight == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_verticalSpacing_type(instance):
    assert isinstance(instance.verticalSpacing, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_horizontalSpacing_type(instance):
    assert isinstance(instance.horizontalSpacing, str)


@given(instance=presentation::GridLayout_strategy)
def test_presentation::gridlayout_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original

@given(instance=presentation::FillLayout_strategy)
@settings(max_examples=50)
def test_presentation::filllayout_instantiation(instance):
    assert isinstance(instance, presentation::FillLayout)

@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_spacing_type(instance):
    assert isinstance(instance.spacing, str)


@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::FillLayout_strategy)
def test_presentation::filllayout_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::FormData_strategy)
@settings(max_examples=50)
def test_presentation::formdata_instantiation(instance):
    assert isinstance(instance, presentation::FormData)

@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::FormData_strategy)
def test_presentation::formdata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=DocumentObject_strategy)
@settings(max_examples=50)
def test_documentobject_instantiation(instance):
    assert isinstance(instance, DocumentObject)

@given(instance=presentation::Element_strategy)
@settings(max_examples=50)
def test_presentation::element_instantiation(instance):
    assert isinstance(instance, presentation::Element)

@given(instance=presentation::Window_strategy)
@settings(max_examples=50)
def test_presentation::window_instantiation(instance):
    assert isinstance(instance, presentation::Window)

@given(instance=presentation::Window_strategy)
def test_presentation::window_blockOnOpen_type(instance):
    assert isinstance(instance.blockOnOpen, str)


@given(instance=presentation::Window_strategy)
def test_presentation::window_blockOnOpen_setter(instance):
    original = instance.blockOnOpen
    instance.blockOnOpen = original
    assert instance.blockOnOpen == original

@given(instance=presentation::Window_strategy)
def test_presentation::window_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Window_strategy)
def test_presentation::window_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Window_strategy)
def test_presentation::window_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Window_strategy)
def test_presentation::window_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::DocumentRoot_strategy)
@settings(max_examples=50)
def test_presentation::documentroot_instantiation(instance):
    assert isinstance(instance, presentation::DocumentRoot)

@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DocumentRoot_strategy)
def test_presentation::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Observable_strategy)
@settings(max_examples=50)
def test_observable_instantiation(instance):
    assert isinstance(instance, Observable)

@given(instance=presentation::DocumentObject_strategy)
@settings(max_examples=50)
def test_presentation::documentobject_instantiation(instance):
    assert isinstance(instance, presentation::DocumentObject)

@given(instance=presentation::Document_strategy)
@settings(max_examples=50)
def test_presentation::document_instantiation(instance):
    assert isinstance(instance, presentation::Document)

@given(instance=presentation::Document_strategy)
def test_presentation::document_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Document_strategy)
def test_presentation::document_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::DialogTray_strategy)
@settings(max_examples=50)
def test_presentation::dialogtray_instantiation(instance):
    assert isinstance(instance, presentation::DialogTray)

@given(instance=presentation::DialogTray_strategy)
def test_presentation::dialogtray_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DialogTray_strategy)
def test_presentation::dialogtray_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::IDialogBlockedHandler_strategy)
@settings(max_examples=50)
def test_presentation::idialogblockedhandler_instantiation(instance):
    assert isinstance(instance, presentation::IDialogBlockedHandler)

@given(instance=presentation::IDialogBlockedHandler_strategy)
def test_presentation::idialogblockedhandler_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IDialogBlockedHandler_strategy)
def test_presentation::idialogblockedhandler_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Window_strategy)
@settings(max_examples=50)
def test_window_instantiation(instance):
    assert isinstance(instance, Window)

@given(instance=presentation::Dialog_strategy)
@settings(max_examples=50)
def test_presentation::dialog_instantiation(instance):
    assert isinstance(instance, presentation::Dialog)

@given(instance=presentation::Dialog_strategy)
def test_presentation::dialog_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::Dialog_strategy)
def test_presentation::dialog_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_presentation::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, presentation::EStringToStringMapEntry)

@given(instance=presentation::DefaultCellModifier_strategy)
@settings(max_examples=50)
def test_presentation::defaultcellmodifier_instantiation(instance):
    assert isinstance(instance, presentation::DefaultCellModifier)

@given(instance=presentation::DefaultCellModifier_strategy)
def test_presentation::defaultcellmodifier_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DefaultCellModifier_strategy)
def test_presentation::defaultcellmodifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::DefaultLabelProvider_strategy)
@settings(max_examples=50)
def test_presentation::defaultlabelprovider_instantiation(instance):
    assert isinstance(instance, presentation::DefaultLabelProvider)

@given(instance=presentation::DefaultLabelProvider_strategy)
def test_presentation::defaultlabelprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::DefaultLabelProvider_strategy)
def test_presentation::defaultlabelprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=presentation::RGB_strategy)
@settings(max_examples=50)
def test_presentation::rgb_instantiation(instance):
    assert isinstance(instance, presentation::RGB)

@given(instance=presentation::RGB_strategy)
def test_presentation::rgb_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::RGB_strategy)
def test_presentation::rgb_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=presentation::CTabItem_strategy)
@settings(max_examples=50)
def test_presentation::ctabitem_instantiation(instance):
    assert isinstance(instance, presentation::CTabItem)

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_showClose_type(instance):
    assert isinstance(instance.showClose, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_showClose_setter(instance):
    original = instance.showClose
    instance.showClose = original
    assert instance.showClose == original

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_disabledImage_type(instance):
    assert isinstance(instance.disabledImage, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_disabledImage_setter(instance):
    original = instance.disabledImage
    instance.disabledImage = original
    assert instance.disabledImage == original

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_font_type(instance):
    assert isinstance(instance.font, str)


@given(instance=presentation::CTabItem_strategy)
def test_presentation::ctabitem_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original

@given(instance=presentation::ExpandItem_strategy)
@settings(max_examples=50)
def test_presentation::expanditem_instantiation(instance):
    assert isinstance(instance, presentation::ExpandItem)

@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_expanded_type(instance):
    assert isinstance(instance.expanded, str)


@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_expanded_setter(instance):
    original = instance.expanded
    instance.expanded = original
    assert instance.expanded == original

@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=presentation::ExpandItem_strategy)
def test_presentation::expanditem_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=presentation::MenuItem_strategy)
@settings(max_examples=50)
def test_presentation::menuitem_instantiation(instance):
    assert isinstance(instance, presentation::MenuItem)

@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_accelerator_type(instance):
    assert isinstance(instance.accelerator, str)


@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_accelerator_setter(instance):
    original = instance.accelerator
    instance.accelerator = original
    assert instance.accelerator == original

@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=presentation::MenuItem_strategy)
def test_presentation::menuitem_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=presentation::CoolItem_strategy)
@settings(max_examples=50)
def test_presentation::coolitem_instantiation(instance):
    assert isinstance(instance, presentation::CoolItem)

@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_preferredSize_type(instance):
    assert isinstance(instance.preferredSize, str)


@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_preferredSize_setter(instance):
    original = instance.preferredSize
    instance.preferredSize = original
    assert instance.preferredSize == original

@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_minimumSize_type(instance):
    assert isinstance(instance.minimumSize, str)


@given(instance=presentation::CoolItem_strategy)
def test_presentation::coolitem_minimumSize_setter(instance):
    original = instance.minimumSize
    instance.minimumSize = original
    assert instance.minimumSize == original

@given(instance=presentation::ControlEditor_strategy)
@settings(max_examples=50)
def test_presentation::controleditor_instantiation(instance):
    assert isinstance(instance, presentation::ControlEditor)

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_minimumHeight_type(instance):
    assert isinstance(instance.minimumHeight, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_minimumHeight_setter(instance):
    original = instance.minimumHeight
    instance.minimumHeight = original
    assert instance.minimumHeight == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_grabHorizontal_type(instance):
    assert isinstance(instance.grabHorizontal, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_grabHorizontal_setter(instance):
    original = instance.grabHorizontal
    instance.grabHorizontal = original
    assert instance.grabHorizontal == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_grabVertical_type(instance):
    assert isinstance(instance.grabVertical, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_grabVertical_setter(instance):
    original = instance.grabVertical
    instance.grabVertical = original
    assert instance.grabVertical == original

@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_minimumWidth_type(instance):
    assert isinstance(instance.minimumWidth, str)


@given(instance=presentation::ControlEditor_strategy)
def test_presentation::controleditor_minimumWidth_setter(instance):
    original = instance.minimumWidth
    instance.minimumWidth = original
    assert instance.minimumWidth == original

@given(instance=presentation::Cursor_strategy)
@settings(max_examples=50)
def test_presentation::cursor_instantiation(instance):
    assert isinstance(instance, presentation::Cursor)

@given(instance=presentation::IContentProvider_strategy)
@settings(max_examples=50)
def test_presentation::icontentprovider_instantiation(instance):
    assert isinstance(instance, presentation::IContentProvider)

@given(instance=presentation::IContentProvider_strategy)
def test_presentation::icontentprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IContentProvider_strategy)
def test_presentation::icontentprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Viewer_strategy)
@settings(max_examples=50)
def test_viewer_instantiation(instance):
    assert isinstance(instance, Viewer)

@given(instance=presentation::ContentViewer_strategy)
@settings(max_examples=50)
def test_presentation::contentviewer_instantiation(instance):
    assert isinstance(instance, presentation::ContentViewer)

@given(instance=presentation::ContentViewer_strategy)
def test_presentation::contentviewer_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::ContentViewer_strategy)
def test_presentation::contentviewer_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::Layout_strategy)
@settings(max_examples=50)
def test_presentation::layout_instantiation(instance):
    assert isinstance(instance, presentation::Layout)

@given(instance=presentation::Layout_strategy)
def test_presentation::layout_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Layout_strategy)
def test_presentation::layout_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Scrollable_strategy)
@settings(max_examples=50)
def test_scrollable_instantiation(instance):
    assert isinstance(instance, Scrollable)

@given(instance=presentation::List_strategy)
@settings(max_examples=50)
def test_presentation::list_instantiation(instance):
    assert isinstance(instance, presentation::List)

@given(instance=presentation::List_strategy)
def test_presentation::list_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::List_strategy)
def test_presentation::list_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::List_strategy)
def test_presentation::list_selectionIndices_type(instance):
    assert isinstance(instance.selectionIndices, str)


@given(instance=presentation::List_strategy)
def test_presentation::list_selectionIndices_setter(instance):
    original = instance.selectionIndices
    instance.selectionIndices = original
    assert instance.selectionIndices == original

@given(instance=presentation::List_strategy)
def test_presentation::list_items_type(instance):
    assert isinstance(instance.items, str)


@given(instance=presentation::List_strategy)
def test_presentation::list_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original

@given(instance=presentation::List_strategy)
def test_presentation::list_topIndex_type(instance):
    assert isinstance(instance.topIndex, str)


@given(instance=presentation::List_strategy)
def test_presentation::list_topIndex_setter(instance):
    original = instance.topIndex
    instance.topIndex = original
    assert instance.topIndex == original

@given(instance=presentation::List_strategy)
def test_presentation::list_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=presentation::List_strategy)
def test_presentation::list_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=presentation::Composite_strategy)
@settings(max_examples=50)
def test_presentation::composite_instantiation(instance):
    assert isinstance(instance, presentation::Composite)

@given(instance=presentation::Composite_strategy)
def test_presentation::composite_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=presentation::Composite_strategy)
def test_presentation::composite_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=presentation::Composite_strategy)
def test_presentation::composite_backgroundMode_type(instance):
    assert isinstance(instance.backgroundMode, str)


@given(instance=presentation::Composite_strategy)
def test_presentation::composite_backgroundMode_setter(instance):
    original = instance.backgroundMode
    instance.backgroundMode = original
    assert instance.backgroundMode == original

@given(instance=presentation::Composite_strategy)
def test_presentation::composite_layoutDeferred_type(instance):
    assert isinstance(instance.layoutDeferred, str)


@given(instance=presentation::Composite_strategy)
def test_presentation::composite_layoutDeferred_setter(instance):
    original = instance.layoutDeferred
    instance.layoutDeferred = original
    assert instance.layoutDeferred == original

@given(instance=AbstractListViewer_strategy)
@settings(max_examples=50)
def test_abstractlistviewer_instantiation(instance):
    assert isinstance(instance, AbstractListViewer)

@given(instance=presentation::ListViewer_strategy)
@settings(max_examples=50)
def test_presentation::listviewer_instantiation(instance):
    assert isinstance(instance, presentation::ListViewer)

@given(instance=presentation::ListViewer_strategy)
def test_presentation::listviewer_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::ListViewer_strategy)
def test_presentation::listviewer_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::ComboViewer_strategy)
@settings(max_examples=50)
def test_presentation::comboviewer_instantiation(instance):
    assert isinstance(instance, presentation::ComboViewer)

@given(instance=presentation::IBaseLabelProvider_strategy)
@settings(max_examples=50)
def test_presentation::ibaselabelprovider_instantiation(instance):
    assert isinstance(instance, presentation::IBaseLabelProvider)

@given(instance=presentation::IBaseLabelProvider_strategy)
def test_presentation::ibaselabelprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IBaseLabelProvider_strategy)
def test_presentation::ibaselabelprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::IStructuredContentProvider_strategy)
@settings(max_examples=50)
def test_presentation::istructuredcontentprovider_instantiation(instance):
    assert isinstance(instance, presentation::IStructuredContentProvider)

@given(instance=presentation::IStructuredContentProvider_strategy)
def test_presentation::istructuredcontentprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IStructuredContentProvider_strategy)
def test_presentation::istructuredcontentprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=AbstractComboBoxCellEditor_strategy)
@settings(max_examples=50)
def test_abstractcomboboxcelleditor_instantiation(instance):
    assert isinstance(instance, AbstractComboBoxCellEditor)

@given(instance=presentation::ComboBoxViewerCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::comboboxviewercelleditor_instantiation(instance):
    assert isinstance(instance, presentation::ComboBoxViewerCellEditor)

@given(instance=presentation::ComboBoxViewerCellEditor_strategy)
def test_presentation::comboboxviewercelleditor_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::ComboBoxViewerCellEditor_strategy)
def test_presentation::comboboxviewercelleditor_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::ComboBoxCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::comboboxcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::ComboBoxCellEditor)

@given(instance=presentation::ICellModifier_strategy)
@settings(max_examples=50)
def test_presentation::icellmodifier_instantiation(instance):
    assert isinstance(instance, presentation::ICellModifier)

@given(instance=presentation::ICellModifier_strategy)
def test_presentation::icellmodifier_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ICellModifier_strategy)
def test_presentation::icellmodifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ColumnViewerEditor_strategy)
@settings(max_examples=50)
def test_presentation::columnviewereditor_instantiation(instance):
    assert isinstance(instance, presentation::ColumnViewerEditor)

@given(instance=presentation::ColumnViewerEditor_strategy)
def test_presentation::columnviewereditor_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ColumnViewerEditor_strategy)
def test_presentation::columnviewereditor_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=DialogCellEditor_strategy)
@settings(max_examples=50)
def test_dialogcelleditor_instantiation(instance):
    assert isinstance(instance, DialogCellEditor)

@given(instance=presentation::ColorCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::colorcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::ColorCellEditor)

@given(instance=presentation::Class_strategy)
@settings(max_examples=50)
def test_presentation::class_instantiation(instance):
    assert isinstance(instance, presentation::Class)

@given(instance=presentation::Class_strategy)
def test_presentation::class_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Class_strategy)
def test_presentation::class_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=presentation::Decorations_strategy)
@settings(max_examples=50)
def test_presentation::decorations_instantiation(instance):
    assert isinstance(instance, presentation::Decorations)

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_images_type(instance):
    assert isinstance(instance.images, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_images_setter(instance):
    original = instance.images
    instance.images = original
    assert instance.images == original

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_maximized_type(instance):
    assert isinstance(instance.maximized, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_maximized_setter(instance):
    original = instance.maximized
    instance.maximized = original
    assert instance.maximized == original

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_minimized_type(instance):
    assert isinstance(instance.minimized, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_minimized_setter(instance):
    original = instance.minimized
    instance.minimized = original
    assert instance.minimized == original

@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=presentation::Decorations_strategy)
def test_presentation::decorations_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=presentation::CLabel_strategy)
@settings(max_examples=50)
def test_presentation::clabel_instantiation(instance):
    assert isinstance(instance, presentation::CLabel)

@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::CLabel_strategy)
def test_presentation::clabel_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=TreeViewer_strategy)
@settings(max_examples=50)
def test_treeviewer_instantiation(instance):
    assert isinstance(instance, TreeViewer)

@given(instance=presentation::CheckboxTreeViewer_strategy)
@settings(max_examples=50)
def test_presentation::checkboxtreeviewer_instantiation(instance):
    assert isinstance(instance, presentation::CheckboxTreeViewer)

@given(instance=presentation::CheckboxTreeViewer_strategy)
def test_presentation::checkboxtreeviewer_allChecked_type(instance):
    assert isinstance(instance.allChecked, str)


@given(instance=presentation::CheckboxTreeViewer_strategy)
def test_presentation::checkboxtreeviewer_allChecked_setter(instance):
    original = instance.allChecked
    instance.allChecked = original
    assert instance.allChecked == original

@given(instance=presentation::CheckboxTreeViewer_strategy)
def test_presentation::checkboxtreeviewer_group6_type(instance):
    assert isinstance(instance.group6, str)


@given(instance=presentation::CheckboxTreeViewer_strategy)
def test_presentation::checkboxtreeviewer_group6_setter(instance):
    original = instance.group6
    instance.group6 = original
    assert instance.group6 == original

@given(instance=presentation::Collection_strategy)
@settings(max_examples=50)
def test_presentation::collection_instantiation(instance):
    assert isinstance(instance, presentation::Collection)

@given(instance=presentation::Collection_strategy)
def test_presentation::collection_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Collection_strategy)
def test_presentation::collection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ICheckStateProvider_strategy)
@settings(max_examples=50)
def test_presentation::icheckstateprovider_instantiation(instance):
    assert isinstance(instance, presentation::ICheckStateProvider)

@given(instance=presentation::ICheckStateProvider_strategy)
def test_presentation::icheckstateprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ICheckStateProvider_strategy)
def test_presentation::icheckstateprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=TableViewer_strategy)
@settings(max_examples=50)
def test_tableviewer_instantiation(instance):
    assert isinstance(instance, TableViewer)

@given(instance=presentation::CheckboxTableViewer_strategy)
@settings(max_examples=50)
def test_presentation::checkboxtableviewer_instantiation(instance):
    assert isinstance(instance, presentation::CheckboxTableViewer)

@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_group5_type(instance):
    assert isinstance(instance.group5, str)


@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_group5_setter(instance):
    original = instance.group5
    instance.group5 = original
    assert instance.group5 == original

@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_allGrayed_type(instance):
    assert isinstance(instance.allGrayed, str)


@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_allGrayed_setter(instance):
    original = instance.allGrayed
    instance.allGrayed = original
    assert instance.allGrayed == original

@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_allChecked_type(instance):
    assert isinstance(instance.allChecked, str)


@given(instance=presentation::CheckboxTableViewer_strategy)
def test_presentation::checkboxtableviewer_allChecked_setter(instance):
    original = instance.allChecked
    instance.allChecked = original
    assert instance.allChecked == original

@given(instance=presentation::LayoutData_strategy)
@settings(max_examples=50)
def test_presentation::layoutdata_instantiation(instance):
    assert isinstance(instance, presentation::LayoutData)

@given(instance=presentation::LayoutData_strategy)
def test_presentation::layoutdata_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::LayoutData_strategy)
def test_presentation::layoutdata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ICellEditorValidator_strategy)
@settings(max_examples=50)
def test_presentation::icelleditorvalidator_instantiation(instance):
    assert isinstance(instance, presentation::ICellEditorValidator)

@given(instance=presentation::ICellEditorValidator_strategy)
def test_presentation::icelleditorvalidator_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ICellEditorValidator_strategy)
def test_presentation::icelleditorvalidator_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::TableItem_strategy)
@settings(max_examples=50)
def test_presentation::tableitem_instantiation(instance):
    assert isinstance(instance, presentation::TableItem)

@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_texts_type(instance):
    assert isinstance(instance.texts, str)


@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_texts_setter(instance):
    original = instance.texts
    instance.texts = original
    assert instance.texts == original

@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_checked_type(instance):
    assert isinstance(instance.checked, str)


@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_imageIndent_type(instance):
    assert isinstance(instance.imageIndent, str)


@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_imageIndent_setter(instance):
    original = instance.imageIndent
    instance.imageIndent = original
    assert instance.imageIndent == original

@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_grayed_type(instance):
    assert isinstance(instance.grayed, str)


@given(instance=presentation::TableItem_strategy)
def test_presentation::tableitem_grayed_setter(instance):
    original = instance.grayed
    instance.grayed = original
    assert instance.grayed == original

@given(instance=presentation::Cell_strategy)
@settings(max_examples=50)
def test_presentation::cell_instantiation(instance):
    assert isinstance(instance, presentation::Cell)

@given(instance=presentation::Cell_strategy)
def test_presentation::cell_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Cell_strategy)
def test_presentation::cell_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Cell_strategy)
def test_presentation::cell_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Cell_strategy)
def test_presentation::cell_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Cell_strategy)
def test_presentation::cell_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Cell_strategy)
def test_presentation::cell_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Cell_strategy)
def test_presentation::cell_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Cell_strategy)
def test_presentation::cell_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::CellEditor_strategy)
@settings(max_examples=50)
def test_presentation::celleditor_instantiation(instance):
    assert isinstance(instance, presentation::CellEditor)

@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_errorMessage_type(instance):
    assert isinstance(instance.errorMessage, str)


@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_errorMessage_setter(instance):
    original = instance.errorMessage
    instance.errorMessage = original
    assert instance.errorMessage == original

@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::CellEditor_strategy)
def test_presentation::celleditor_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Widget_strategy)
@settings(max_examples=50)
def test_widget_instantiation(instance):
    assert isinstance(instance, Widget)

@given(instance=presentation::Item_strategy)
@settings(max_examples=50)
def test_presentation::item_instantiation(instance):
    assert isinstance(instance, presentation::Item)

@given(instance=presentation::Item_strategy)
def test_presentation::item_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Item_strategy)
def test_presentation::item_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Item_strategy)
def test_presentation::item_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Item_strategy)
def test_presentation::item_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Menu_strategy)
@settings(max_examples=50)
def test_presentation::menu_instantiation(instance):
    assert isinstance(instance, presentation::Menu)

@given(instance=presentation::Menu_strategy)
def test_presentation::menu_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Menu_strategy)
def test_presentation::menu_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Menu_strategy)
def test_presentation::menu_handle_type(instance):
    assert isinstance(instance.handle, str)


@given(instance=presentation::Menu_strategy)
def test_presentation::menu_handle_setter(instance):
    original = instance.handle
    instance.handle = original
    assert instance.handle == original

@given(instance=presentation::Menu_strategy)
def test_presentation::menu_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=presentation::Menu_strategy)
def test_presentation::menu_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=presentation::Menu_strategy)
def test_presentation::menu_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=presentation::Menu_strategy)
def test_presentation::menu_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=presentation::Control_strategy)
@settings(max_examples=50)
def test_presentation::control_instantiation(instance):
    assert isinstance(instance, presentation::Control)

@given(instance=presentation::Control_strategy)
def test_presentation::control_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_backgroundImage_type(instance):
    assert isinstance(instance.backgroundImage, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_backgroundImage_setter(instance):
    original = instance.backgroundImage
    instance.backgroundImage = original
    assert instance.backgroundImage == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_font_type(instance):
    assert isinstance(instance.font, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_handle_type(instance):
    assert isinstance(instance.handle, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_handle_setter(instance):
    original = instance.handle
    instance.handle = original
    assert instance.handle == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_capture_type(instance):
    assert isinstance(instance.capture, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_capture_setter(instance):
    original = instance.capture
    instance.capture = original
    assert instance.capture == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_foreground_type(instance):
    assert isinstance(instance.foreground, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_foreground_setter(instance):
    original = instance.foreground
    instance.foreground = original
    assert instance.foreground == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_redraw_type(instance):
    assert isinstance(instance.redraw, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_redraw_setter(instance):
    original = instance.redraw
    instance.redraw = original
    assert instance.redraw == original

@given(instance=presentation::Control_strategy)
def test_presentation::control_dragDetect_type(instance):
    assert isinstance(instance.dragDetect, str)


@given(instance=presentation::Control_strategy)
def test_presentation::control_dragDetect_setter(instance):
    original = instance.dragDetect
    instance.dragDetect = original
    assert instance.dragDetect == original

@given(instance=presentation::Caret_strategy)
@settings(max_examples=50)
def test_presentation::caret_instantiation(instance):
    assert isinstance(instance, presentation::Caret)

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_font_type(instance):
    assert isinstance(instance.font, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Caret_strategy)
def test_presentation::caret_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Caret_strategy)
def test_presentation::caret_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::IME_strategy)
@settings(max_examples=50)
def test_presentation::ime_instantiation(instance):
    assert isinstance(instance, presentation::IME)

@given(instance=presentation::IME_strategy)
def test_presentation::ime_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=presentation::IME_strategy)
def test_presentation::ime_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=presentation::IME_strategy)
def test_presentation::ime_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::IME_strategy)
def test_presentation::ime_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::IME_strategy)
def test_presentation::ime_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::IME_strategy)
def test_presentation::ime_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::IME_strategy)
def test_presentation::ime_compositionOffset_type(instance):
    assert isinstance(instance.compositionOffset, str)


@given(instance=presentation::IME_strategy)
def test_presentation::ime_compositionOffset_setter(instance):
    original = instance.compositionOffset
    instance.compositionOffset = original
    assert instance.compositionOffset == original

@given(instance=presentation::ICommand_strategy)
@settings(max_examples=50)
def test_presentation::icommand_instantiation(instance):
    assert isinstance(instance, presentation::ICommand)

@given(instance=presentation::ICommand_strategy)
def test_presentation::icommand_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ICommand_strategy)
def test_presentation::icommand_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=presentation::Link_strategy)
@settings(max_examples=50)
def test_presentation::link_instantiation(instance):
    assert isinstance(instance, presentation::Link)

@given(instance=presentation::Link_strategy)
def test_presentation::link_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Link_strategy)
def test_presentation::link_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Label_strategy)
@settings(max_examples=50)
def test_presentation::label_instantiation(instance):
    assert isinstance(instance, presentation::Label)

@given(instance=presentation::Label_strategy)
def test_presentation::label_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Label_strategy)
def test_presentation::label_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Label_strategy)
def test_presentation::label_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::Label_strategy)
def test_presentation::label_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::Label_strategy)
def test_presentation::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Label_strategy)
def test_presentation::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Button_strategy)
@settings(max_examples=50)
def test_presentation::button_instantiation(instance):
    assert isinstance(instance, presentation::Button)

@given(instance=presentation::Button_strategy)
def test_presentation::button_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Button_strategy)
def test_presentation::button_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::Button_strategy)
def test_presentation::button_grayed_type(instance):
    assert isinstance(instance.grayed, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_grayed_setter(instance):
    original = instance.grayed
    instance.grayed = original
    assert instance.grayed == original

@given(instance=presentation::Button_strategy)
def test_presentation::button_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=presentation::Button_strategy)
def test_presentation::button_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::Button_strategy)
def test_presentation::button_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Button_strategy)
def test_presentation::button_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Composite_strategy)
@settings(max_examples=50)
def test_composite_instantiation(instance):
    assert isinstance(instance, Composite)

@given(instance=presentation::CTabFolder_strategy)
@settings(max_examples=50)
def test_presentation::ctabfolder_instantiation(instance):
    assert isinstance(instance, presentation::CTabFolder)

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_mINTABWIDTH_type(instance):
    assert isinstance(instance.mINTABWIDTH, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_mINTABWIDTH_setter(instance):
    original = instance.mINTABWIDTH
    instance.mINTABWIDTH = original
    assert instance.mINTABWIDTH == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimized_type(instance):
    assert isinstance(instance.minimized, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimized_setter(instance):
    original = instance.minimized
    instance.minimized = original
    assert instance.minimized == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_mRUVisible_type(instance):
    assert isinstance(instance.mRUVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_mRUVisible_setter(instance):
    original = instance.mRUVisible
    instance.mRUVisible = original
    assert instance.mRUVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_tabPosition_type(instance):
    assert isinstance(instance.tabPosition, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_tabPosition_setter(instance):
    original = instance.tabPosition
    instance.tabPosition = original
    assert instance.tabPosition == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_borderVisible_type(instance):
    assert isinstance(instance.borderVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_borderVisible_setter(instance):
    original = instance.borderVisible
    instance.borderVisible = original
    assert instance.borderVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_single_type(instance):
    assert isinstance(instance.single, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_maximizeVisible_type(instance):
    assert isinstance(instance.maximizeVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_maximizeVisible_setter(instance):
    original = instance.maximizeVisible
    instance.maximizeVisible = original
    assert instance.maximizeVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_maximized_type(instance):
    assert isinstance(instance.maximized, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_maximized_setter(instance):
    original = instance.maximized
    instance.maximized = original
    assert instance.maximized == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimizeVisible_type(instance):
    assert isinstance(instance.minimizeVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimizeVisible_setter(instance):
    original = instance.minimizeVisible
    instance.minimizeVisible = original
    assert instance.minimizeVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_selectionForeground_type(instance):
    assert isinstance(instance.selectionForeground, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_selectionForeground_setter(instance):
    original = instance.selectionForeground
    instance.selectionForeground = original
    assert instance.selectionForeground == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_unselectedImageVisible_type(instance):
    assert isinstance(instance.unselectedImageVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_unselectedImageVisible_setter(instance):
    original = instance.unselectedImageVisible
    instance.unselectedImageVisible = original
    assert instance.unselectedImageVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_unselectedCloseVisible_type(instance):
    assert isinstance(instance.unselectedCloseVisible, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_unselectedCloseVisible_setter(instance):
    original = instance.unselectedCloseVisible
    instance.unselectedCloseVisible = original
    assert instance.unselectedCloseVisible == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_tabHeight_type(instance):
    assert isinstance(instance.tabHeight, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_tabHeight_setter(instance):
    original = instance.tabHeight
    instance.tabHeight = original
    assert instance.tabHeight == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_selectionBackground_type(instance):
    assert isinstance(instance.selectionBackground, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_selectionBackground_setter(instance):
    original = instance.selectionBackground
    instance.selectionBackground = original
    assert instance.selectionBackground == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimumCharacters_type(instance):
    assert isinstance(instance.minimumCharacters, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_minimumCharacters_setter(instance):
    original = instance.minimumCharacters
    instance.minimumCharacters = original
    assert instance.minimumCharacters == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_simple_type(instance):
    assert isinstance(instance.simple, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_simple_setter(instance):
    original = instance.simple
    instance.simple = original
    assert instance.simple == original

@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::CTabFolder_strategy)
def test_presentation::ctabfolder_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::Combo_strategy)
@settings(max_examples=50)
def test_presentation::combo_instantiation(instance):
    assert isinstance(instance, presentation::Combo)

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_listVisible_type(instance):
    assert isinstance(instance.listVisible, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_listVisible_setter(instance):
    original = instance.listVisible
    instance.listVisible = original
    assert instance.listVisible == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_visibleItemCount_type(instance):
    assert isinstance(instance.visibleItemCount, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_visibleItemCount_setter(instance):
    original = instance.visibleItemCount
    instance.visibleItemCount = original
    assert instance.visibleItemCount == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_items_type(instance):
    assert isinstance(instance.items, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_textLimit_type(instance):
    assert isinstance(instance.textLimit, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_textLimit_setter(instance):
    original = instance.textLimit
    instance.textLimit = original
    assert instance.textLimit == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Combo_strategy)
def test_presentation::combo_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=presentation::Combo_strategy)
def test_presentation::combo_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=presentation::Group_strategy)
@settings(max_examples=50)
def test_presentation::group_instantiation(instance):
    assert isinstance(instance, presentation::Group)

@given(instance=presentation::Group_strategy)
def test_presentation::group_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Group_strategy)
def test_presentation::group_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::CCombo_strategy)
@settings(max_examples=50)
def test_presentation::ccombo_instantiation(instance):
    assert isinstance(instance, presentation::CCombo)

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_editable_type(instance):
    assert isinstance(instance.editable, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_visibleItemCount_type(instance):
    assert isinstance(instance.visibleItemCount, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_visibleItemCount_setter(instance):
    original = instance.visibleItemCount
    instance.visibleItemCount = original
    assert instance.visibleItemCount == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_listVisible_type(instance):
    assert isinstance(instance.listVisible, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_listVisible_setter(instance):
    original = instance.listVisible
    instance.listVisible = original
    assert instance.listVisible == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_items_type(instance):
    assert isinstance(instance.items, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_textLimit_type(instance):
    assert isinstance(instance.textLimit, str)


@given(instance=presentation::CCombo_strategy)
def test_presentation::ccombo_textLimit_setter(instance):
    original = instance.textLimit
    instance.textLimit = original
    assert instance.textLimit == original

@given(instance=presentation::ExpandBar_strategy)
@settings(max_examples=50)
def test_presentation::expandbar_instantiation(instance):
    assert isinstance(instance, presentation::ExpandBar)

@given(instance=presentation::ExpandBar_strategy)
def test_presentation::expandbar_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::ExpandBar_strategy)
def test_presentation::expandbar_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::ExpandBar_strategy)
def test_presentation::expandbar_spacing_type(instance):
    assert isinstance(instance.spacing, str)


@given(instance=presentation::ExpandBar_strategy)
def test_presentation::expandbar_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=presentation::DateTime_strategy)
@settings(max_examples=50)
def test_presentation::datetime_instantiation(instance):
    assert isinstance(instance, presentation::DateTime)

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_minutes_type(instance):
    assert isinstance(instance.minutes, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_seconds_type(instance):
    assert isinstance(instance.seconds, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_seconds_setter(instance):
    original = instance.seconds
    instance.seconds = original
    assert instance.seconds == original

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_hours_type(instance):
    assert isinstance(instance.hours, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=presentation::DateTime_strategy)
def test_presentation::datetime_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=presentation::Canvas_strategy)
@settings(max_examples=50)
def test_presentation::canvas_instantiation(instance):
    assert isinstance(instance, presentation::Canvas)

@given(instance=presentation::Canvas_strategy)
def test_presentation::canvas_mixed1_type(instance):
    assert isinstance(instance.mixed1, str)


@given(instance=presentation::Canvas_strategy)
def test_presentation::canvas_mixed1_setter(instance):
    original = instance.mixed1
    instance.mixed1 = original
    assert instance.mixed1 == original

@given(instance=presentation::Canvas_strategy)
def test_presentation::canvas_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::Canvas_strategy)
def test_presentation::canvas_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::CoolBar_strategy)
@settings(max_examples=50)
def test_presentation::coolbar_instantiation(instance):
    assert isinstance(instance, presentation::CoolBar)

@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_locked_type(instance):
    assert isinstance(instance.locked, str)


@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original

@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_itemOrder_type(instance):
    assert isinstance(instance.itemOrder, str)


@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_itemOrder_setter(instance):
    original = instance.itemOrder
    instance.itemOrder = original
    assert instance.itemOrder == original

@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_itemSizes_type(instance):
    assert isinstance(instance.itemSizes, str)


@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_itemSizes_setter(instance):
    original = instance.itemSizes
    instance.itemSizes = original
    assert instance.itemSizes == original

@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_wrapIndices_type(instance):
    assert isinstance(instance.wrapIndices, str)


@given(instance=presentation::CoolBar_strategy)
def test_presentation::coolbar_wrapIndices_setter(instance):
    original = instance.wrapIndices
    instance.wrapIndices = original
    assert instance.wrapIndices == original

@given(instance=presentation::Browser_strategy)
@settings(max_examples=50)
def test_presentation::browser_instantiation(instance):
    assert isinstance(instance, presentation::Browser)

@given(instance=presentation::Browser_strategy)
def test_presentation::browser_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=presentation::Browser_strategy)
def test_presentation::browser_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=presentation::Browser_strategy)
def test_presentation::browser_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::Browser_strategy)
def test_presentation::browser_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::Browser_strategy)
def test_presentation::browser_browserType_type(instance):
    assert isinstance(instance.browserType, str)


@given(instance=presentation::Browser_strategy)
def test_presentation::browser_browserType_setter(instance):
    original = instance.browserType
    instance.browserType = original
    assert instance.browserType == original

@given(instance=presentation::Browser_strategy)
def test_presentation::browser_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Browser_strategy)
def test_presentation::browser_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Binding_strategy)
@settings(max_examples=50)
def test_presentation::binding_instantiation(instance):
    assert isinstance(instance, presentation::Binding)

@given(instance=presentation::Binding_strategy)
def test_presentation::binding_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=presentation::Binding_strategy)
def test_presentation::binding_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=presentation::Binding_strategy)
def test_presentation::binding_xPath_type(instance):
    assert isinstance(instance.xPath, str)


@given(instance=presentation::Binding_strategy)
def test_presentation::binding_xPath_setter(instance):
    original = instance.xPath
    instance.xPath = original
    assert instance.xPath == original

@given(instance=presentation::Binding_strategy)
def test_presentation::binding_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Binding_strategy)
def test_presentation::binding_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Binding_strategy)
def test_presentation::binding_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Binding_strategy)
def test_presentation::binding_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Binding_strategy)
def test_presentation::binding_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=presentation::Binding_strategy)
def test_presentation::binding_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=presentation::Accessible_strategy)
@settings(max_examples=50)
def test_presentation::accessible_instantiation(instance):
    assert isinstance(instance, presentation::Accessible)

@given(instance=presentation::Accessible_strategy)
def test_presentation::accessible_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Accessible_strategy)
def test_presentation::accessible_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::EObject_strategy)
@settings(max_examples=50)
def test_presentation::eobject_instantiation(instance):
    assert isinstance(instance, presentation::EObject)

@given(instance=presentation::TreePath_strategy)
@settings(max_examples=50)
def test_presentation::treepath_instantiation(instance):
    assert isinstance(instance, presentation::TreePath)

@given(instance=presentation::TreePath_strategy)
def test_presentation::treepath_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::TreePath_strategy)
def test_presentation::treepath_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Widget_strategy)
@settings(max_examples=50)
def test_presentation::widget_instantiation(instance):
    assert isinstance(instance, presentation::Widget)

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseMoveEvent_type(instance):
    assert isinstance(instance.mouseMoveEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseMoveEvent_setter(instance):
    original = instance.mouseMoveEvent
    instance.mouseMoveEvent = original
    assert instance.mouseMoveEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_activateEvent_type(instance):
    assert isinstance(instance.activateEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_activateEvent_setter(instance):
    original = instance.activateEvent
    instance.activateEvent = original
    assert instance.activateEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseUpEvent_type(instance):
    assert isinstance(instance.mouseUpEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseUpEvent_setter(instance):
    original = instance.mouseUpEvent
    instance.mouseUpEvent = original
    assert instance.mouseUpEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hideEvent_type(instance):
    assert isinstance(instance.hideEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hideEvent_setter(instance):
    original = instance.hideEvent
    instance.hideEvent = original
    assert instance.hideEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_showEvent_type(instance):
    assert isinstance(instance.showEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_showEvent_setter(instance):
    original = instance.showEvent
    instance.showEvent = original
    assert instance.showEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_focusInEvent_type(instance):
    assert isinstance(instance.focusInEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_focusInEvent_setter(instance):
    original = instance.focusInEvent
    instance.focusInEvent = original
    assert instance.focusInEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseDownEvent_type(instance):
    assert isinstance(instance.mouseDownEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseDownEvent_setter(instance):
    original = instance.mouseDownEvent
    instance.mouseDownEvent = original
    assert instance.mouseDownEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseWheelEvent_type(instance):
    assert isinstance(instance.mouseWheelEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseWheelEvent_setter(instance):
    original = instance.mouseWheelEvent
    instance.mouseWheelEvent = original
    assert instance.mouseWheelEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseEnterEvent_type(instance):
    assert isinstance(instance.mouseEnterEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseEnterEvent_setter(instance):
    original = instance.mouseEnterEvent
    instance.mouseEnterEvent = original
    assert instance.mouseEnterEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hardKeyDownEvent_type(instance):
    assert isinstance(instance.hardKeyDownEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hardKeyDownEvent_setter(instance):
    original = instance.hardKeyDownEvent
    instance.hardKeyDownEvent = original
    assert instance.hardKeyDownEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_modifyEvent_type(instance):
    assert isinstance(instance.modifyEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_modifyEvent_setter(instance):
    original = instance.modifyEvent
    instance.modifyEvent = original
    assert instance.modifyEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_deactivateEvent_type(instance):
    assert isinstance(instance.deactivateEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_deactivateEvent_setter(instance):
    original = instance.deactivateEvent
    instance.deactivateEvent = original
    assert instance.deactivateEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_keyDownEvent_type(instance):
    assert isinstance(instance.keyDownEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_keyDownEvent_setter(instance):
    original = instance.keyDownEvent
    instance.keyDownEvent = original
    assert instance.keyDownEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_moveEvent_type(instance):
    assert isinstance(instance.moveEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_moveEvent_setter(instance):
    original = instance.moveEvent
    instance.moveEvent = original
    assert instance.moveEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_keyUpEvent_type(instance):
    assert isinstance(instance.keyUpEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_keyUpEvent_setter(instance):
    original = instance.keyUpEvent
    instance.keyUpEvent = original
    assert instance.keyUpEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_helpEvent_type(instance):
    assert isinstance(instance.helpEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_helpEvent_setter(instance):
    original = instance.helpEvent
    instance.helpEvent = original
    assert instance.helpEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_verifyEvent_type(instance):
    assert isinstance(instance.verifyEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_verifyEvent_setter(instance):
    original = instance.verifyEvent
    instance.verifyEvent = original
    assert instance.verifyEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_disposeEvent_type(instance):
    assert isinstance(instance.disposeEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_disposeEvent_setter(instance):
    original = instance.disposeEvent
    instance.disposeEvent = original
    assert instance.disposeEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_armEvent_type(instance):
    assert isinstance(instance.armEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_armEvent_setter(instance):
    original = instance.armEvent
    instance.armEvent = original
    assert instance.armEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseHoverEvent_type(instance):
    assert isinstance(instance.mouseHoverEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseHoverEvent_setter(instance):
    original = instance.mouseHoverEvent
    instance.mouseHoverEvent = original
    assert instance.mouseHoverEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_measureItemEvent_type(instance):
    assert isinstance(instance.measureItemEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_measureItemEvent_setter(instance):
    original = instance.measureItemEvent
    instance.measureItemEvent = original
    assert instance.measureItemEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseExitEvent_type(instance):
    assert isinstance(instance.mouseExitEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseExitEvent_setter(instance):
    original = instance.mouseExitEvent
    instance.mouseExitEvent = original
    assert instance.mouseExitEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_traverseEvent_type(instance):
    assert isinstance(instance.traverseEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_traverseEvent_setter(instance):
    original = instance.traverseEvent
    instance.traverseEvent = original
    assert instance.traverseEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_collapseEvent_type(instance):
    assert isinstance(instance.collapseEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_collapseEvent_setter(instance):
    original = instance.collapseEvent
    instance.collapseEvent = original
    assert instance.collapseEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_setDataEvent_type(instance):
    assert isinstance(instance.setDataEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_setDataEvent_setter(instance):
    original = instance.setDataEvent
    instance.setDataEvent = original
    assert instance.setDataEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_dataContext_type(instance):
    assert isinstance(instance.dataContext, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_dataContext_setter(instance):
    original = instance.dataContext
    instance.dataContext = original
    assert instance.dataContext == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_resizeEvent_type(instance):
    assert isinstance(instance.resizeEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_resizeEvent_setter(instance):
    original = instance.resizeEvent
    instance.resizeEvent = original
    assert instance.resizeEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_menuDetectEvent_type(instance):
    assert isinstance(instance.menuDetectEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_menuDetectEvent_setter(instance):
    original = instance.menuDetectEvent
    instance.menuDetectEvent = original
    assert instance.menuDetectEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_deiconifyEvent_type(instance):
    assert isinstance(instance.deiconifyEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_deiconifyEvent_setter(instance):
    original = instance.deiconifyEvent
    instance.deiconifyEvent = original
    assert instance.deiconifyEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_defaultSelectionEvent_type(instance):
    assert isinstance(instance.defaultSelectionEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_defaultSelectionEvent_setter(instance):
    original = instance.defaultSelectionEvent
    instance.defaultSelectionEvent = original
    assert instance.defaultSelectionEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_closeEvent_type(instance):
    assert isinstance(instance.closeEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_closeEvent_setter(instance):
    original = instance.closeEvent
    instance.closeEvent = original
    assert instance.closeEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseDoubleClickEvent_type(instance):
    assert isinstance(instance.mouseDoubleClickEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mouseDoubleClickEvent_setter(instance):
    original = instance.mouseDoubleClickEvent
    instance.mouseDoubleClickEvent = original
    assert instance.mouseDoubleClickEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_selectionEvent_type(instance):
    assert isinstance(instance.selectionEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_selectionEvent_setter(instance):
    original = instance.selectionEvent
    instance.selectionEvent = original
    assert instance.selectionEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_iconifyEvent_type(instance):
    assert isinstance(instance.iconifyEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_iconifyEvent_setter(instance):
    original = instance.iconifyEvent
    instance.iconifyEvent = original
    assert instance.iconifyEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hardKeyUpEvent_type(instance):
    assert isinstance(instance.hardKeyUpEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_hardKeyUpEvent_setter(instance):
    original = instance.hardKeyUpEvent
    instance.hardKeyUpEvent = original
    assert instance.hardKeyUpEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_dragDetectEvent_type(instance):
    assert isinstance(instance.dragDetectEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_dragDetectEvent_setter(instance):
    original = instance.dragDetectEvent
    instance.dragDetectEvent = original
    assert instance.dragDetectEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_imeCompositionEvent_type(instance):
    assert isinstance(instance.imeCompositionEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_imeCompositionEvent_setter(instance):
    original = instance.imeCompositionEvent
    instance.imeCompositionEvent = original
    assert instance.imeCompositionEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_paintEvent_type(instance):
    assert isinstance(instance.paintEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_paintEvent_setter(instance):
    original = instance.paintEvent
    instance.paintEvent = original
    assert instance.paintEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_focusOutEvent_type(instance):
    assert isinstance(instance.focusOutEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_focusOutEvent_setter(instance):
    original = instance.focusOutEvent
    instance.focusOutEvent = original
    assert instance.focusOutEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_expandEvent_type(instance):
    assert isinstance(instance.expandEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_expandEvent_setter(instance):
    original = instance.expandEvent
    instance.expandEvent = original
    assert instance.expandEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_eraseItemEvent_type(instance):
    assert isinstance(instance.eraseItemEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_eraseItemEvent_setter(instance):
    original = instance.eraseItemEvent
    instance.eraseItemEvent = original
    assert instance.eraseItemEvent == original

@given(instance=presentation::Widget_strategy)
def test_presentation::widget_paintItemEvent_type(instance):
    assert isinstance(instance.paintItemEvent, str)


@given(instance=presentation::Widget_strategy)
def test_presentation::widget_paintItemEvent_setter(instance):
    original = instance.paintItemEvent
    instance.paintItemEvent = original
    assert instance.paintItemEvent == original

@given(instance=ColumnViewer_strategy)
@settings(max_examples=50)
def test_columnviewer_instantiation(instance):
    assert isinstance(instance, ColumnViewer)

@given(instance=presentation::AbstractTreeViewer_strategy)
@settings(max_examples=50)
def test_presentation::abstracttreeviewer_instantiation(instance):
    assert isinstance(instance, presentation::AbstractTreeViewer)

@given(instance=presentation::AbstractTreeViewer_strategy)
def test_presentation::abstracttreeviewer_autoExpandLevel_type(instance):
    assert isinstance(instance.autoExpandLevel, str)


@given(instance=presentation::AbstractTreeViewer_strategy)
def test_presentation::abstracttreeviewer_autoExpandLevel_setter(instance):
    original = instance.autoExpandLevel
    instance.autoExpandLevel = original
    assert instance.autoExpandLevel == original

@given(instance=presentation::AbstractTreeViewer_strategy)
def test_presentation::abstracttreeviewer_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=presentation::AbstractTreeViewer_strategy)
def test_presentation::abstracttreeviewer_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=presentation::AbstractTableViewer_strategy)
@settings(max_examples=50)
def test_presentation::abstracttableviewer_instantiation(instance):
    assert isinstance(instance, presentation::AbstractTableViewer)

@given(instance=presentation::AbstractTableViewer_strategy)
def test_presentation::abstracttableviewer_itemCount_type(instance):
    assert isinstance(instance.itemCount, str)


@given(instance=presentation::AbstractTableViewer_strategy)
def test_presentation::abstracttableviewer_itemCount_setter(instance):
    original = instance.itemCount
    instance.itemCount = original
    assert instance.itemCount == original

@given(instance=StructuredViewer_strategy)
@settings(max_examples=50)
def test_structuredviewer_instantiation(instance):
    assert isinstance(instance, StructuredViewer)

@given(instance=presentation::ColumnViewer_strategy)
@settings(max_examples=50)
def test_presentation::columnviewer_instantiation(instance):
    assert isinstance(instance, presentation::ColumnViewer)

@given(instance=presentation::ColumnViewer_strategy)
def test_presentation::columnviewer_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::ColumnViewer_strategy)
def test_presentation::columnviewer_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::AbstractListViewer_strategy)
@settings(max_examples=50)
def test_presentation::abstractlistviewer_instantiation(instance):
    assert isinstance(instance, presentation::AbstractListViewer)

@given(instance=presentation::IBindingContext_strategy)
@settings(max_examples=50)
def test_presentation::ibindingcontext_instantiation(instance):
    assert isinstance(instance, presentation::IBindingContext)

@given(instance=presentation::IBindingContext_strategy)
def test_presentation::ibindingcontext_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::IBindingContext_strategy)
def test_presentation::ibindingcontext_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::AbstractDataProvider_strategy)
@settings(max_examples=50)
def test_presentation::abstractdataprovider_instantiation(instance):
    assert isinstance(instance, presentation::AbstractDataProvider)

@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=presentation::AbstractDataProvider_strategy)
def test_presentation::abstractdataprovider_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=CellEditor_strategy)
@settings(max_examples=50)
def test_celleditor_instantiation(instance):
    assert isinstance(instance, CellEditor)

@given(instance=presentation::DialogCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::dialogcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::DialogCellEditor)

@given(instance=presentation::CheckboxCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::checkboxcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::CheckboxCellEditor)

@given(instance=presentation::AbstractComboBoxCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::abstractcomboboxcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::AbstractComboBoxCellEditor)

@given(instance=presentation::AbstractComboBoxCellEditor_strategy)
def test_presentation::abstractcomboboxcelleditor_activationStyle_type(instance):
    assert isinstance(instance.activationStyle, str)


@given(instance=presentation::AbstractComboBoxCellEditor_strategy)
def test_presentation::abstractcomboboxcelleditor_activationStyle_setter(instance):
    original = instance.activationStyle
    instance.activationStyle = original
    assert instance.activationStyle == original

@given(instance=presentation::WindowManager_strategy)
@settings(max_examples=50)
def test_presentation::windowmanager_instantiation(instance):
    assert isinstance(instance, presentation::WindowManager)

@given(instance=presentation::WindowManager_strategy)
def test_presentation::windowmanager_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::WindowManager_strategy)
def test_presentation::windowmanager_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=ViewerComparator_strategy)
@settings(max_examples=50)
def test_viewercomparator_instantiation(instance):
    assert isinstance(instance, ViewerComparator)

@given(instance=presentation::ViewerColumn_strategy)
@settings(max_examples=50)
def test_presentation::viewercolumn_instantiation(instance):
    assert isinstance(instance, presentation::ViewerColumn)

@given(instance=presentation::ViewerColumn_strategy)
def test_presentation::viewercolumn_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ViewerColumn_strategy)
def test_presentation::viewercolumn_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Viewer_strategy)
@settings(max_examples=50)
def test_presentation::viewer_instantiation(instance):
    assert isinstance(instance, presentation::Viewer)

@given(instance=presentation::Viewer_strategy)
def test_presentation::viewer_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Viewer_strategy)
def test_presentation::viewer_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Viewer_strategy)
def test_presentation::viewer_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Viewer_strategy)
def test_presentation::viewer_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::URL_strategy)
@settings(max_examples=50)
def test_presentation::url_instantiation(instance):
    assert isinstance(instance, presentation::URL)

@given(instance=presentation::URL_strategy)
def test_presentation::url_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::URL_strategy)
def test_presentation::url_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::TreeItem_strategy)
@settings(max_examples=50)
def test_presentation::treeitem_instantiation(instance):
    assert isinstance(instance, presentation::TreeItem)

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_grayed_type(instance):
    assert isinstance(instance.grayed, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_grayed_setter(instance):
    original = instance.grayed
    instance.grayed = original
    assert instance.grayed == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_checked_type(instance):
    assert isinstance(instance.checked, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_itemCount_type(instance):
    assert isinstance(instance.itemCount, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_itemCount_setter(instance):
    original = instance.itemCount
    instance.itemCount = original
    assert instance.itemCount == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_expanded_type(instance):
    assert isinstance(instance.expanded, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_expanded_setter(instance):
    original = instance.expanded
    instance.expanded = original
    assert instance.expanded == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_texts_type(instance):
    assert isinstance(instance.texts, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_texts_setter(instance):
    original = instance.texts
    instance.texts = original
    assert instance.texts == original

@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_handle_type(instance):
    assert isinstance(instance.handle, str)


@given(instance=presentation::TreeItem_strategy)
def test_presentation::treeitem_handle_setter(instance):
    original = instance.handle
    instance.handle = original
    assert instance.handle == original

@given(instance=presentation::TreeColumn_strategy)
@settings(max_examples=50)
def test_presentation::treecolumn_instantiation(instance):
    assert isinstance(instance, presentation::TreeColumn)

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_resizable_type(instance):
    assert isinstance(instance.resizable, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_moveable_type(instance):
    assert isinstance(instance.moveable, str)


@given(instance=presentation::TreeColumn_strategy)
def test_presentation::treecolumn_moveable_setter(instance):
    original = instance.moveable
    instance.moveable = original
    assert instance.moveable == original

@given(instance=presentation::Tree_strategy)
@settings(max_examples=50)
def test_presentation::tree_instantiation(instance):
    assert isinstance(instance, presentation::Tree)

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_columnOrder_type(instance):
    assert isinstance(instance.columnOrder, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_columnOrder_setter(instance):
    original = instance.columnOrder
    instance.columnOrder = original
    assert instance.columnOrder == original

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_itemCount_type(instance):
    assert isinstance(instance.itemCount, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_itemCount_setter(instance):
    original = instance.itemCount
    instance.itemCount = original
    assert instance.itemCount == original

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_sortDirection_type(instance):
    assert isinstance(instance.sortDirection, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_sortDirection_setter(instance):
    original = instance.sortDirection
    instance.sortDirection = original
    assert instance.sortDirection == original

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_linesVisible_type(instance):
    assert isinstance(instance.linesVisible, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_linesVisible_setter(instance):
    original = instance.linesVisible
    instance.linesVisible = original
    assert instance.linesVisible == original

@given(instance=presentation::Tree_strategy)
def test_presentation::tree_headerVisible_type(instance):
    assert isinstance(instance.headerVisible, str)


@given(instance=presentation::Tree_strategy)
def test_presentation::tree_headerVisible_setter(instance):
    original = instance.headerVisible
    instance.headerVisible = original
    assert instance.headerVisible == original

@given(instance=presentation::TrayDialog_strategy)
@settings(max_examples=50)
def test_presentation::traydialog_instantiation(instance):
    assert isinstance(instance, presentation::TrayDialog)

@given(instance=presentation::TrayDialog_strategy)
def test_presentation::traydialog_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=presentation::TrayDialog_strategy)
def test_presentation::traydialog_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=presentation::TrayDialog_strategy)
def test_presentation::traydialog_helpAvailable_type(instance):
    assert isinstance(instance.helpAvailable, str)


@given(instance=presentation::TrayDialog_strategy)
def test_presentation::traydialog_helpAvailable_setter(instance):
    original = instance.helpAvailable
    instance.helpAvailable = original
    assert instance.helpAvailable == original

@given(instance=presentation::TrayItem_strategy)
@settings(max_examples=50)
def test_presentation::trayitem_instantiation(instance):
    assert isinstance(instance, presentation::TrayItem)

@given(instance=presentation::Tray_strategy)
@settings(max_examples=50)
def test_presentation::tray_instantiation(instance):
    assert isinstance(instance, presentation::Tray)

@given(instance=presentation::Tray_strategy)
def test_presentation::tray_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Tray_strategy)
def test_presentation::tray_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Tracker_strategy)
@settings(max_examples=50)
def test_presentation::tracker_instantiation(instance):
    assert isinstance(instance, presentation::Tracker)

@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_rectangles_type(instance):
    assert isinstance(instance.rectangles, str)


@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_rectangles_setter(instance):
    original = instance.rectangles
    instance.rectangles = original
    assert instance.rectangles == original

@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_stippled_type(instance):
    assert isinstance(instance.stippled, str)


@given(instance=presentation::Tracker_strategy)
def test_presentation::tracker_stippled_setter(instance):
    original = instance.stippled
    instance.stippled = original
    assert instance.stippled == original

@given(instance=presentation::ToolTip_strategy)
@settings(max_examples=50)
def test_presentation::tooltip_instantiation(instance):
    assert isinstance(instance, presentation::ToolTip)

@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_autoHide_type(instance):
    assert isinstance(instance.autoHide, str)


@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_autoHide_setter(instance):
    original = instance.autoHide
    instance.autoHide = original
    assert instance.autoHide == original

@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=presentation::ToolTip_strategy)
def test_presentation::tooltip_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=presentation::ToolItem_strategy)
@settings(max_examples=50)
def test_presentation::toolitem_instantiation(instance):
    assert isinstance(instance, presentation::ToolItem)

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_hotImage_type(instance):
    assert isinstance(instance.hotImage, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_hotImage_setter(instance):
    original = instance.hotImage
    instance.hotImage = original
    assert instance.hotImage == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_disabledImage_type(instance):
    assert isinstance(instance.disabledImage, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_disabledImage_setter(instance):
    original = instance.disabledImage
    instance.disabledImage = original
    assert instance.disabledImage == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::ToolItem_strategy)
def test_presentation::toolitem_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::ToolBar_strategy)
@settings(max_examples=50)
def test_presentation::toolbar_instantiation(instance):
    assert isinstance(instance, presentation::ToolBar)

@given(instance=presentation::ToolBar_strategy)
def test_presentation::toolbar_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::ToolBar_strategy)
def test_presentation::toolbar_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=TrayDialog_strategy)
@settings(max_examples=50)
def test_traydialog_instantiation(instance):
    assert isinstance(instance, TrayDialog)

@given(instance=presentation::TitleAreaDialog_strategy)
@settings(max_examples=50)
def test_presentation::titleareadialog_instantiation(instance):
    assert isinstance(instance, presentation::TitleAreaDialog)

@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_titleImage_type(instance):
    assert isinstance(instance.titleImage, str)


@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_titleImage_setter(instance):
    original = instance.titleImage
    instance.titleImage = original
    assert instance.titleImage == original

@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_errorMessage_type(instance):
    assert isinstance(instance.errorMessage, str)


@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_errorMessage_setter(instance):
    original = instance.errorMessage
    instance.errorMessage = original
    assert instance.errorMessage == original

@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::TitleAreaDialog_strategy)
def test_presentation::titleareadialog_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::TextCellEditor_strategy)
@settings(max_examples=50)
def test_presentation::textcelleditor_instantiation(instance):
    assert isinstance(instance, presentation::TextCellEditor)

@given(instance=presentation::Text_strategy)
@settings(max_examples=50)
def test_presentation::text_instantiation(instance):
    assert isinstance(instance, presentation::Text)

@given(instance=presentation::Text_strategy)
def test_presentation::text_textLimit_type(instance):
    assert isinstance(instance.textLimit, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_textLimit_setter(instance):
    original = instance.textLimit
    instance.textLimit = original
    assert instance.textLimit == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_editable_type(instance):
    assert isinstance(instance.editable, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_topIndex_type(instance):
    assert isinstance(instance.topIndex, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_topIndex_setter(instance):
    original = instance.topIndex
    instance.topIndex = original
    assert instance.topIndex == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_echoChar_type(instance):
    assert isinstance(instance.echoChar, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_echoChar_setter(instance):
    original = instance.echoChar
    instance.echoChar = original
    assert instance.echoChar == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_doubleClickEnabled_type(instance):
    assert isinstance(instance.doubleClickEnabled, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_doubleClickEnabled_setter(instance):
    original = instance.doubleClickEnabled
    instance.doubleClickEnabled = original
    assert instance.doubleClickEnabled == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_selectionText_type(instance):
    assert isinstance(instance.selectionText, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_selectionText_setter(instance):
    original = instance.selectionText
    instance.selectionText = original
    assert instance.selectionText == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_caretLocation_type(instance):
    assert isinstance(instance.caretLocation, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_caretLocation_setter(instance):
    original = instance.caretLocation
    instance.caretLocation = original
    assert instance.caretLocation == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_lineDelimiter_type(instance):
    assert isinstance(instance.lineDelimiter, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_lineDelimiter_setter(instance):
    original = instance.lineDelimiter
    instance.lineDelimiter = original
    assert instance.lineDelimiter == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_tabs_type(instance):
    assert isinstance(instance.tabs, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_tabs_setter(instance):
    original = instance.tabs
    instance.tabs = original
    assert instance.tabs == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Text_strategy)
def test_presentation::text_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=presentation::Text_strategy)
def test_presentation::text_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=AbstractTableViewer_strategy)
@settings(max_examples=50)
def test_abstracttableviewer_instantiation(instance):
    assert isinstance(instance, AbstractTableViewer)

@given(instance=presentation::TableViewer_strategy)
@settings(max_examples=50)
def test_presentation::tableviewer_instantiation(instance):
    assert isinstance(instance, presentation::TableViewer)

@given(instance=presentation::TableViewer_strategy)
def test_presentation::tableviewer_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=presentation::TableViewer_strategy)
def test_presentation::tableviewer_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=AbstractTreeViewer_strategy)
@settings(max_examples=50)
def test_abstracttreeviewer_instantiation(instance):
    assert isinstance(instance, AbstractTreeViewer)

@given(instance=presentation::TreeViewer_strategy)
@settings(max_examples=50)
def test_presentation::treeviewer_instantiation(instance):
    assert isinstance(instance, presentation::TreeViewer)

@given(instance=presentation::TreeViewer_strategy)
def test_presentation::treeviewer_group5_type(instance):
    assert isinstance(instance.group5, str)


@given(instance=presentation::TreeViewer_strategy)
def test_presentation::treeviewer_group5_setter(instance):
    original = instance.group5
    instance.group5 = original
    assert instance.group5 == original

@given(instance=presentation::TableTreeViewer_strategy)
@settings(max_examples=50)
def test_presentation::tabletreeviewer_instantiation(instance):
    assert isinstance(instance, presentation::TableTreeViewer)

@given(instance=presentation::TableTreeViewer_strategy)
def test_presentation::tabletreeviewer_group5_type(instance):
    assert isinstance(instance.group5, str)


@given(instance=presentation::TableTreeViewer_strategy)
def test_presentation::tabletreeviewer_group5_setter(instance):
    original = instance.group5
    instance.group5 = original
    assert instance.group5 == original

@given(instance=presentation::TableTree_strategy)
@settings(max_examples=50)
def test_presentation::tabletree_instantiation(instance):
    assert isinstance(instance, presentation::TableTree)

@given(instance=ViewerColumn_strategy)
@settings(max_examples=50)
def test_viewercolumn_instantiation(instance):
    assert isinstance(instance, ViewerColumn)

@given(instance=presentation::TableViewerColumn_strategy)
@settings(max_examples=50)
def test_presentation::tableviewercolumn_instantiation(instance):
    assert isinstance(instance, presentation::TableViewerColumn)

@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::TableViewerColumn_strategy)
def test_presentation::tableviewercolumn_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ControlEditor_strategy)
@settings(max_examples=50)
def test_controleditor_instantiation(instance):
    assert isinstance(instance, ControlEditor)

@given(instance=presentation::TableEditor_strategy)
@settings(max_examples=50)
def test_presentation::tableeditor_instantiation(instance):
    assert isinstance(instance, presentation::TableEditor)

@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_dynamic_type(instance):
    assert isinstance(instance.dynamic, str)


@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original

@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::TableEditor_strategy)
def test_presentation::tableeditor_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::TableColumn_strategy)
@settings(max_examples=50)
def test_presentation::tablecolumn_instantiation(instance):
    assert isinstance(instance, presentation::TableColumn)

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_resizable_type(instance):
    assert isinstance(instance.resizable, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_moveable_type(instance):
    assert isinstance(instance.moveable, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_moveable_setter(instance):
    original = instance.moveable
    instance.moveable = original
    assert instance.moveable == original

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TableColumn_strategy)
def test_presentation::tablecolumn_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::Table_strategy)
@settings(max_examples=50)
def test_presentation::table_instantiation(instance):
    assert isinstance(instance, presentation::Table)

@given(instance=presentation::Table_strategy)
def test_presentation::table_topIndex_type(instance):
    assert isinstance(instance.topIndex, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_topIndex_setter(instance):
    original = instance.topIndex
    instance.topIndex = original
    assert instance.topIndex == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_sortDirection_type(instance):
    assert isinstance(instance.sortDirection, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_sortDirection_setter(instance):
    original = instance.sortDirection
    instance.sortDirection = original
    assert instance.sortDirection == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_selectionIndices_type(instance):
    assert isinstance(instance.selectionIndices, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_selectionIndices_setter(instance):
    original = instance.selectionIndices
    instance.selectionIndices = original
    assert instance.selectionIndices == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_columnOrder_type(instance):
    assert isinstance(instance.columnOrder, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_columnOrder_setter(instance):
    original = instance.columnOrder
    instance.columnOrder = original
    assert instance.columnOrder == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_linesVisible_type(instance):
    assert isinstance(instance.linesVisible, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_linesVisible_setter(instance):
    original = instance.linesVisible
    instance.linesVisible = original
    assert instance.linesVisible == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_itemCount_type(instance):
    assert isinstance(instance.itemCount, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_itemCount_setter(instance):
    original = instance.itemCount
    instance.itemCount = original
    assert instance.itemCount == original

@given(instance=presentation::Table_strategy)
def test_presentation::table_headerVisible_type(instance):
    assert isinstance(instance.headerVisible, str)


@given(instance=presentation::Table_strategy)
def test_presentation::table_headerVisible_setter(instance):
    original = instance.headerVisible
    instance.headerVisible = original
    assert instance.headerVisible == original

@given(instance=presentation::TabFolder_strategy)
@settings(max_examples=50)
def test_presentation::tabfolder_instantiation(instance):
    assert isinstance(instance, presentation::TabFolder)

@given(instance=presentation::TabFolder_strategy)
def test_presentation::tabfolder_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::TabFolder_strategy)
def test_presentation::tabfolder_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=TextStyle_strategy)
@settings(max_examples=50)
def test_textstyle_instantiation(instance):
    assert isinstance(instance, TextStyle)

@given(instance=presentation::TabItem_strategy)
@settings(max_examples=50)
def test_presentation::tabitem_instantiation(instance):
    assert isinstance(instance, presentation::TabItem)

@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_toolTipText_type(instance):
    assert isinstance(instance.toolTipText, str)


@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_toolTipText_setter(instance):
    original = instance.toolTipText
    instance.toolTipText = original
    assert instance.toolTipText == original

@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_bounds_type(instance):
    assert isinstance(instance.bounds, str)


@given(instance=presentation::TabItem_strategy)
def test_presentation::tabitem_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=presentation::StyledTextContent_strategy)
@settings(max_examples=50)
def test_presentation::styledtextcontent_instantiation(instance):
    assert isinstance(instance, presentation::StyledTextContent)

@given(instance=presentation::StyledTextContent_strategy)
def test_presentation::styledtextcontent_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::StyledTextContent_strategy)
def test_presentation::styledtextcontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::StyleRange_strategy)
@settings(max_examples=50)
def test_presentation::stylerange_instantiation(instance):
    assert isinstance(instance, presentation::StyleRange)

@given(instance=presentation::StyledText_strategy)
@settings(max_examples=50)
def test_presentation::styledtext_instantiation(instance):
    assert isinstance(instance, presentation::StyledText)

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_caretOffset_type(instance):
    assert isinstance(instance.caretOffset, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_caretOffset_setter(instance):
    original = instance.caretOffset
    instance.caretOffset = original
    assert instance.caretOffset == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionRanges_type(instance):
    assert isinstance(instance.selectionRanges, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionRanges_setter(instance):
    original = instance.selectionRanges
    instance.selectionRanges = original
    assert instance.selectionRanges == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_horizontalIndex_type(instance):
    assert isinstance(instance.horizontalIndex, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_horizontalIndex_setter(instance):
    original = instance.horizontalIndex
    instance.horizontalIndex = original
    assert instance.horizontalIndex == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_bidiColoring_type(instance):
    assert isinstance(instance.bidiColoring, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_bidiColoring_setter(instance):
    original = instance.bidiColoring
    instance.bidiColoring = original
    assert instance.bidiColoring == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_topIndex_type(instance):
    assert isinstance(instance.topIndex, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_topIndex_setter(instance):
    original = instance.topIndex
    instance.topIndex = original
    assert instance.topIndex == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_topPixel_type(instance):
    assert isinstance(instance.topPixel, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_topPixel_setter(instance):
    original = instance.topPixel
    instance.topPixel = original
    assert instance.topPixel == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_editable_type(instance):
    assert isinstance(instance.editable, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_textLimit_type(instance):
    assert isinstance(instance.textLimit, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_textLimit_setter(instance):
    original = instance.textLimit
    instance.textLimit = original
    assert instance.textLimit == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_tabs_type(instance):
    assert isinstance(instance.tabs, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_tabs_setter(instance):
    original = instance.tabs
    instance.tabs = original
    assert instance.tabs == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionText_type(instance):
    assert isinstance(instance.selectionText, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionText_setter(instance):
    original = instance.selectionText
    instance.selectionText = original
    assert instance.selectionText == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_doubleClickEnabled_type(instance):
    assert isinstance(instance.doubleClickEnabled, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_doubleClickEnabled_setter(instance):
    original = instance.doubleClickEnabled
    instance.doubleClickEnabled = original
    assert instance.doubleClickEnabled == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionForeground_type(instance):
    assert isinstance(instance.selectionForeground, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionForeground_setter(instance):
    original = instance.selectionForeground
    instance.selectionForeground = original
    assert instance.selectionForeground == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_horizontalPixel_type(instance):
    assert isinstance(instance.horizontalPixel, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_horizontalPixel_setter(instance):
    original = instance.horizontalPixel
    instance.horizontalPixel = original
    assert instance.horizontalPixel == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_lineDelimiter_type(instance):
    assert isinstance(instance.lineDelimiter, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_lineDelimiter_setter(instance):
    original = instance.lineDelimiter
    instance.lineDelimiter = original
    assert instance.lineDelimiter == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_blockSelection_type(instance):
    assert isinstance(instance.blockSelection, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_blockSelection_setter(instance):
    original = instance.blockSelection
    instance.blockSelection = original
    assert instance.blockSelection == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_indent_type(instance):
    assert isinstance(instance.indent, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_indent_setter(instance):
    original = instance.indent
    instance.indent = original
    assert instance.indent == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_wordWrap_type(instance):
    assert isinstance(instance.wordWrap, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_wordWrap_setter(instance):
    original = instance.wordWrap
    instance.wordWrap = original
    assert instance.wordWrap == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionBackground_type(instance):
    assert isinstance(instance.selectionBackground, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_selectionBackground_setter(instance):
    original = instance.selectionBackground
    instance.selectionBackground = original
    assert instance.selectionBackground == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_lineSpacing_type(instance):
    assert isinstance(instance.lineSpacing, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_lineSpacing_setter(instance):
    original = instance.lineSpacing
    instance.lineSpacing = original
    assert instance.lineSpacing == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_justify_type(instance):
    assert isinstance(instance.justify, str)


@given(instance=presentation::StyledText_strategy)
def test_presentation::styledtext_justify_setter(instance):
    original = instance.justify
    instance.justify = original
    assert instance.justify == original

@given(instance=presentation::ViewerSorter_strategy)
@settings(max_examples=50)
def test_presentation::viewersorter_instantiation(instance):
    assert isinstance(instance, presentation::ViewerSorter)

@given(instance=presentation::ViewerComparator_strategy)
@settings(max_examples=50)
def test_presentation::viewercomparator_instantiation(instance):
    assert isinstance(instance, presentation::ViewerComparator)

@given(instance=presentation::ViewerComparator_strategy)
def test_presentation::viewercomparator_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ViewerComparator_strategy)
def test_presentation::viewercomparator_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=ContentViewer_strategy)
@settings(max_examples=50)
def test_contentviewer_instantiation(instance):
    assert isinstance(instance, ContentViewer)

@given(instance=presentation::StructuredViewer_strategy)
@settings(max_examples=50)
def test_presentation::structuredviewer_instantiation(instance):
    assert isinstance(instance, presentation::StructuredViewer)

@given(instance=presentation::StructuredViewer_strategy)
def test_presentation::structuredviewer_useHashlookup_type(instance):
    assert isinstance(instance.useHashlookup, str)


@given(instance=presentation::StructuredViewer_strategy)
def test_presentation::structuredviewer_useHashlookup_setter(instance):
    original = instance.useHashlookup
    instance.useHashlookup = original
    assert instance.useHashlookup == original

@given(instance=presentation::StructuredViewer_strategy)
def test_presentation::structuredviewer_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=presentation::StructuredViewer_strategy)
def test_presentation::structuredviewer_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=presentation::StackLayout_strategy)
@settings(max_examples=50)
def test_presentation::stacklayout_instantiation(instance):
    assert isinstance(instance, presentation::StackLayout)

@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::StackLayout_strategy)
def test_presentation::stacklayout_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::ViewerFilter_strategy)
@settings(max_examples=50)
def test_presentation::viewerfilter_instantiation(instance):
    assert isinstance(instance, presentation::ViewerFilter)

@given(instance=presentation::ViewerFilter_strategy)
def test_presentation::viewerfilter_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::ViewerFilter_strategy)
def test_presentation::viewerfilter_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::Spinner_strategy)
@settings(max_examples=50)
def test_presentation::spinner_instantiation(instance):
    assert isinstance(instance, presentation::Spinner)

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_pageIncrement_type(instance):
    assert isinstance(instance.pageIncrement, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_pageIncrement_setter(instance):
    original = instance.pageIncrement
    instance.pageIncrement = original
    assert instance.pageIncrement == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_textLimit_type(instance):
    assert isinstance(instance.textLimit, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_textLimit_setter(instance):
    original = instance.textLimit
    instance.textLimit = original
    assert instance.textLimit == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_digits_type(instance):
    assert isinstance(instance.digits, str)


@given(instance=presentation::Spinner_strategy)
def test_presentation::spinner_digits_setter(instance):
    original = instance.digits
    instance.digits = original
    assert instance.digits == original

@given(instance=Decorations_strategy)
@settings(max_examples=50)
def test_decorations_instantiation(instance):
    assert isinstance(instance, Decorations)

@given(instance=presentation::Shell_strategy)
@settings(max_examples=50)
def test_presentation::shell_instantiation(instance):
    assert isinstance(instance, presentation::Shell)

@given(instance=presentation::Shell_strategy)
def test_presentation::shell_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=presentation::Shell_strategy)
def test_presentation::shell_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=presentation::Shell_strategy)
def test_presentation::shell_minimumSize_type(instance):
    assert isinstance(instance.minimumSize, str)


@given(instance=presentation::Shell_strategy)
def test_presentation::shell_minimumSize_setter(instance):
    original = instance.minimumSize
    instance.minimumSize = original
    assert instance.minimumSize == original

@given(instance=presentation::Shell_strategy)
def test_presentation::shell_imeInputMode_type(instance):
    assert isinstance(instance.imeInputMode, str)


@given(instance=presentation::Shell_strategy)
def test_presentation::shell_imeInputMode_setter(instance):
    original = instance.imeInputMode
    instance.imeInputMode = original
    assert instance.imeInputMode == original

@given(instance=presentation::Shell_strategy)
def test_presentation::shell_fullScreen_type(instance):
    assert isinstance(instance.fullScreen, str)


@given(instance=presentation::Shell_strategy)
def test_presentation::shell_fullScreen_setter(instance):
    original = instance.fullScreen
    instance.fullScreen = original
    assert instance.fullScreen == original

@given(instance=presentation::Shell_strategy)
def test_presentation::shell_group5_type(instance):
    assert isinstance(instance.group5, str)


@given(instance=presentation::Shell_strategy)
def test_presentation::shell_group5_setter(instance):
    original = instance.group5
    instance.group5 = original
    assert instance.group5 == original

@given(instance=presentation::Slider_strategy)
@settings(max_examples=50)
def test_presentation::slider_instantiation(instance):
    assert isinstance(instance, presentation::Slider)

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_pageIncrement_type(instance):
    assert isinstance(instance.pageIncrement, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_pageIncrement_setter(instance):
    original = instance.pageIncrement
    instance.pageIncrement = original
    assert instance.pageIncrement == original

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_thumb_type(instance):
    assert isinstance(instance.thumb, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_thumb_setter(instance):
    original = instance.thumb
    instance.thumb = original
    assert instance.thumb == original

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=presentation::Slider_strategy)
def test_presentation::slider_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=presentation::Slider_strategy)
def test_presentation::slider_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=presentation::ScrollBar_strategy)
@settings(max_examples=50)
def test_presentation::scrollbar_instantiation(instance):
    assert isinstance(instance, presentation::ScrollBar)

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_thumb_type(instance):
    assert isinstance(instance.thumb, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_thumb_setter(instance):
    original = instance.thumb
    instance.thumb = original
    assert instance.thumb == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_enabled_type(instance):
    assert isinstance(instance.enabled, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_pageIncrement_type(instance):
    assert isinstance(instance.pageIncrement, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_pageIncrement_setter(instance):
    original = instance.pageIncrement
    instance.pageIncrement = original
    assert instance.pageIncrement == original

@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=presentation::ScrollBar_strategy)
def test_presentation::scrollbar_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=presentation::Scale_strategy)
@settings(max_examples=50)
def test_presentation::scale_instantiation(instance):
    assert isinstance(instance, presentation::Scale)

@given(instance=presentation::Scale_strategy)
def test_presentation::scale_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=presentation::Scale_strategy)
def test_presentation::scale_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=presentation::Scale_strategy)
def test_presentation::scale_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::Scale_strategy)
def test_presentation::scale_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=presentation::Scale_strategy)
def test_presentation::scale_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=presentation::Scale_strategy)
def test_presentation::scale_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=presentation::Scale_strategy)
def test_presentation::scale_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=presentation::Scale_strategy)
def test_presentation::scale_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=presentation::Scale_strategy)
def test_presentation::scale_pageIncrement_type(instance):
    assert isinstance(instance.pageIncrement, str)


@given(instance=presentation::Scale_strategy)
def test_presentation::scale_pageIncrement_setter(instance):
    original = instance.pageIncrement
    instance.pageIncrement = original
    assert instance.pageIncrement == original

@given(instance=presentation::Scrollable_strategy)
@settings(max_examples=50)
def test_presentation::scrollable_instantiation(instance):
    assert isinstance(instance, presentation::Scrollable)

@given(instance=presentation::Scrollable_strategy)
def test_presentation::scrollable_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::Scrollable_strategy)
def test_presentation::scrollable_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::Scrollable_strategy)
def test_presentation::scrollable_clientArea_type(instance):
    assert isinstance(instance.clientArea, str)


@given(instance=presentation::Scrollable_strategy)
def test_presentation::scrollable_clientArea_setter(instance):
    original = instance.clientArea
    instance.clientArea = original
    assert instance.clientArea == original

@given(instance=presentation::Sash_strategy)
@settings(max_examples=50)
def test_presentation::sash_instantiation(instance):
    assert isinstance(instance, presentation::Sash)

@given(instance=presentation::SashForm_strategy)
@settings(max_examples=50)
def test_presentation::sashform_instantiation(instance):
    assert isinstance(instance, presentation::SashForm)

@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_weights_type(instance):
    assert isinstance(instance.weights, str)


@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_weights_setter(instance):
    original = instance.weights
    instance.weights = original
    assert instance.weights == original

@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_sashWidth1_type(instance):
    assert isinstance(instance.sashWidth1, str)


@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_sashWidth1_setter(instance):
    original = instance.sashWidth1
    instance.sashWidth1 = original
    assert instance.sashWidth1 == original

@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_sASHWIDTH_type(instance):
    assert isinstance(instance.sASHWIDTH, str)


@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_sASHWIDTH_setter(instance):
    original = instance.sASHWIDTH
    instance.sASHWIDTH = original
    assert instance.sASHWIDTH == original

@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=presentation::SashForm_strategy)
def test_presentation::sashform_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=presentation::RowLayout_strategy)
@settings(max_examples=50)
def test_presentation::rowlayout_instantiation(instance):
    assert isinstance(instance, presentation::RowLayout)

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_pack_type(instance):
    assert isinstance(instance.pack, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_pack_setter(instance):
    original = instance.pack
    instance.pack = original
    assert instance.pack == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_center_type(instance):
    assert isinstance(instance.center, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_center_setter(instance):
    original = instance.center
    instance.center = original
    assert instance.center == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginRight_type(instance):
    assert isinstance(instance.marginRight, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginRight_setter(instance):
    original = instance.marginRight
    instance.marginRight = original
    assert instance.marginRight == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_wrap_type(instance):
    assert isinstance(instance.wrap, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_wrap_setter(instance):
    original = instance.wrap
    instance.wrap = original
    assert instance.wrap == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginLeft_type(instance):
    assert isinstance(instance.marginLeft, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginLeft_setter(instance):
    original = instance.marginLeft
    instance.marginLeft = original
    assert instance.marginLeft == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_justify_type(instance):
    assert isinstance(instance.justify, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_justify_setter(instance):
    original = instance.justify
    instance.justify = original
    assert instance.justify == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginTop_type(instance):
    assert isinstance(instance.marginTop, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginTop_setter(instance):
    original = instance.marginTop
    instance.marginTop = original
    assert instance.marginTop == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginBottom_type(instance):
    assert isinstance(instance.marginBottom, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginBottom_setter(instance):
    original = instance.marginBottom
    instance.marginBottom = original
    assert instance.marginBottom == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_spacing_type(instance):
    assert isinstance(instance.spacing, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_fill_type(instance):
    assert isinstance(instance.fill, str)


@given(instance=presentation::RowLayout_strategy)
def test_presentation::rowlayout_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=presentation::RowData_strategy)
@settings(max_examples=50)
def test_presentation::rowdata_instantiation(instance):
    assert isinstance(instance, presentation::RowData)

@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_exclude_type(instance):
    assert isinstance(instance.exclude, str)


@given(instance=presentation::RowData_strategy)
def test_presentation::rowdata_exclude_setter(instance):
    original = instance.exclude
    instance.exclude = original
    assert instance.exclude == original

@given(instance=presentation::Resource_strategy)
@settings(max_examples=50)
def test_presentation::resource_instantiation(instance):
    assert isinstance(instance, presentation::Resource)

@given(instance=presentation::Resource_strategy)
def test_presentation::resource_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=presentation::Resource_strategy)
def test_presentation::resource_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=presentation::ProgressBar_strategy)
@settings(max_examples=50)
def test_presentation::progressbar_instantiation(instance):
    assert isinstance(instance, presentation::ProgressBar)

@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=presentation::ProgressBar_strategy)
def test_presentation::progressbar_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=AbstractDataProvider_strategy)
@settings(max_examples=50)
def test_abstractdataprovider_instantiation(instance):
    assert isinstance(instance, AbstractDataProvider)

@given(instance=presentation::ObjectDataProvider_strategy)
@settings(max_examples=50)
def test_presentation::objectdataprovider_instantiation(instance):
    assert isinstance(instance, presentation::ObjectDataProvider)

@given(instance=presentation::ObjectDataProvider_strategy)
def test_presentation::objectdataprovider_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::ObjectDataProvider_strategy)
def test_presentation::objectdataprovider_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=presentation::ObjectDataProvider_strategy)
def test_presentation::objectdataprovider_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=presentation::ObjectDataProvider_strategy)
def test_presentation::objectdataprovider_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=presentation::XMLDataProvider_strategy)
@settings(max_examples=50)
def test_presentation::xmldataprovider_instantiation(instance):
    assert isinstance(instance, presentation::XMLDataProvider)

@given(instance=presentation::XMLDataProvider_strategy)
def test_presentation::xmldataprovider_xPath_type(instance):
    assert isinstance(instance.xPath, str)


@given(instance=presentation::XMLDataProvider_strategy)
def test_presentation::xmldataprovider_xPath_setter(instance):
    original = instance.xPath
    instance.xPath = original
    assert instance.xPath == original

@given(instance=presentation::XMLDataProvider_strategy)
def test_presentation::xmldataprovider_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=presentation::XMLDataProvider_strategy)
def test_presentation::xmldataprovider_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original
