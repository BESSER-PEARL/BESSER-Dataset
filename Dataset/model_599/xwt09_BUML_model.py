####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
presentation_AbstractComboBoxCellEditor = Class(name="presentation::AbstractComboBoxCellEditor", is_abstract=True)
CellEditor = Class(name="CellEditor")
presentation_AbstractDataProvider = Class(name="presentation::AbstractDataProvider", is_abstract=True)
presentation_AbstractListViewer = Class(name="presentation::AbstractListViewer", is_abstract=True)
StructuredViewer = Class(name="StructuredViewer")
presentation_AbstractTableViewer = Class(name="presentation::AbstractTableViewer", is_abstract=True)
ColumnViewer = Class(name="ColumnViewer")
presentation_AbstractTreeViewer = Class(name="presentation::AbstractTreeViewer", is_abstract=True)
presentation_IBindingContext = Class(name="presentation::IBindingContext", is_abstract=True)
presentation_TreePath = Class(name="presentation::TreePath")
presentation_EObject = Class(name="presentation::EObject")
presentation_Widget = Class(name="presentation::Widget", is_abstract=True)
presentation_Accessible = Class(name="presentation::Accessible")
presentation_Binding = Class(name="presentation::Binding")
presentation_Button = Class(name="presentation::Button")
Control = Class(name="Control")
presentation_ICommand = Class(name="presentation::ICommand", is_abstract=True)
presentation_Canvas = Class(name="presentation::Canvas")
presentation_Browser = Class(name="presentation::Browser")
Composite = Class(name="Composite")
Widget = Class(name="Widget")
presentation_IME = Class(name="presentation::IME")
presentation_Caret = Class(name="presentation::Caret")
presentation_CCombo = Class(name="presentation::CCombo")
presentation_CellEditor = Class(name="presentation::CellEditor", is_abstract=True)
presentation_ICellEditorValidator = Class(name="presentation::ICellEditorValidator", is_abstract=True)
presentation_LayoutData = Class(name="presentation::LayoutData")
presentation_Cell = Class(name="presentation::Cell")
presentation_TableItem = Class(name="presentation::TableItem")
presentation_CheckboxCellEditor = Class(name="presentation::CheckboxCellEditor")
presentation_CheckboxTableViewer = Class(name="presentation::CheckboxTableViewer")
TableViewer = Class(name="TableViewer")
presentation_ICheckStateProvider = Class(name="presentation::ICheckStateProvider", is_abstract=True)
presentation_Control = Class(name="presentation::Control", is_abstract=True)
presentation_CheckboxTreeViewer = Class(name="presentation::CheckboxTreeViewer")
TreeViewer = Class(name="TreeViewer")
presentation_CLabel = Class(name="presentation::CLabel")
Canvas = Class(name="Canvas")
presentation_Class = Class(name="presentation::Class")
presentation_ColumnViewer = Class(name="presentation::ColumnViewer", is_abstract=True)
presentation_ColumnViewerEditor = Class(name="presentation::ColumnViewerEditor", is_abstract=True)
presentation_ICellModifier = Class(name="presentation::ICellModifier", is_abstract=True)
presentation_Collection = Class(name="presentation::Collection", is_abstract=True)
presentation_ColorCellEditor = Class(name="presentation::ColorCellEditor")
DialogCellEditor = Class(name="DialogCellEditor")
presentation_Combo = Class(name="presentation::Combo")
presentation_ComboBoxCellEditor = Class(name="presentation::ComboBoxCellEditor")
AbstractComboBoxCellEditor = Class(name="AbstractComboBoxCellEditor")
presentation_ComboBoxViewerCellEditor = Class(name="presentation::ComboBoxViewerCellEditor")
presentation_ComboViewer = Class(name="presentation::ComboViewer")
AbstractListViewer = Class(name="AbstractListViewer")
presentation_Composite = Class(name="presentation::Composite")
Scrollable = Class(name="Scrollable")
presentation_IStructuredContentProvider = Class(name="presentation::IStructuredContentProvider", is_abstract=True)
presentation_IBaseLabelProvider = Class(name="presentation::IBaseLabelProvider", is_abstract=True)
presentation_ContentViewer = Class(name="presentation::ContentViewer", is_abstract=True)
Viewer = Class(name="Viewer")
presentation_IContentProvider = Class(name="presentation::IContentProvider", is_abstract=True)
presentation_Layout = Class(name="presentation::Layout", is_abstract=True)
presentation_Menu = Class(name="presentation::Menu")
presentation_Cursor = Class(name="presentation::Cursor")
presentation_ControlEditor = Class(name="presentation::ControlEditor")
presentation_CoolBar = Class(name="presentation::CoolBar")
presentation_CoolItem = Class(name="presentation::CoolItem")
Item = Class(name="Item")
presentation_CTabFolder = Class(name="presentation::CTabFolder")
presentation_RGB = Class(name="presentation::RGB")
presentation_CTabItem = Class(name="presentation::CTabItem")
presentation_DateTime = Class(name="presentation::DateTime")
Resource = Class(name="Resource")
presentation_Decorations = Class(name="presentation::Decorations")
presentation_Dialog = Class(name="presentation::Dialog", is_abstract=True)
Window = Class(name="Window")
presentation_IDialogBlockedHandler = Class(name="presentation::IDialogBlockedHandler", is_abstract=True)
presentation_DefaultCellModifier = Class(name="presentation::DefaultCellModifier")
presentation_DefaultLabelProvider = Class(name="presentation::DefaultLabelProvider")
presentation_Document = Class(name="presentation::Document", is_abstract=True)
presentation_DocumentObject = Class(name="presentation::DocumentObject")
Observable = Class(name="Observable")
presentation_DocumentRoot = Class(name="presentation::DocumentRoot")
presentation_EStringToStringMapEntry = Class(name="presentation::EStringToStringMapEntry")
presentation_DialogCellEditor = Class(name="presentation::DialogCellEditor", is_abstract=True)
presentation_DialogTray = Class(name="presentation::DialogTray", is_abstract=True)
presentation_Window = Class(name="presentation::Window", is_abstract=True)
presentation_Element = Class(name="presentation::Element")
DocumentObject = Class(name="DocumentObject")
presentation_ExpandBar = Class(name="presentation::ExpandBar")
presentation_ExpandItem = Class(name="presentation::ExpandItem")
presentation_FormAttachment = Class(name="presentation::FormAttachment")
presentation_FillLayout = Class(name="presentation::FillLayout")
Layout = Class(name="Layout")
presentation_FormData = Class(name="presentation::FormData")
presentation_FormLayout = Class(name="presentation::FormLayout")
presentation_GridData = Class(name="presentation::GridData")
presentation_GridLayout = Class(name="presentation::GridLayout")
presentation_Group = Class(name="presentation::Group")
presentation_IElementComparer = Class(name="presentation::IElementComparer", is_abstract=True)
presentation_TextStyle = Class(name="presentation::TextStyle")
presentation_Item = Class(name="presentation::Item", is_abstract=True)
presentation_ISelection = Class(name="presentation::ISelection", is_abstract=True)
presentation_Label = Class(name="presentation::Label")
presentation_List = Class(name="presentation::List")
presentation_Link = Class(name="presentation::Link")
presentation_ListViewer = Class(name="presentation::ListViewer")
presentation_Listener = Class(name="presentation::Listener", is_abstract=True)
presentation_MenuItem = Class(name="presentation::MenuItem")
presentation_MessageBox = Class(name="presentation::MessageBox")
Dialog = Class(name="Dialog")
presentation_ObjectDataProvider = Class(name="presentation::ObjectDataProvider")
AbstractDataProvider = Class(name="AbstractDataProvider")
presentation_Observable = Class(name="presentation::Observable")
presentation_Resource = Class(name="presentation::Resource", is_abstract=True)
presentation_ProgressBar = Class(name="presentation::ProgressBar")
presentation_RowData = Class(name="presentation::RowData")
presentation_RowLayout = Class(name="presentation::RowLayout")
presentation_Scale = Class(name="presentation::Scale")
presentation_Sash = Class(name="presentation::Sash")
presentation_SashForm = Class(name="presentation::SashForm")
presentation_Scrollable = Class(name="presentation::Scrollable", is_abstract=True)
presentation_ScrollBar = Class(name="presentation::ScrollBar")
presentation_Shell = Class(name="presentation::Shell")
Decorations = Class(name="Decorations")
presentation_Slider = Class(name="presentation::Slider")
presentation_Spinner = Class(name="presentation::Spinner")
presentation_StructuredViewer = Class(name="presentation::StructuredViewer", is_abstract=True)
ContentViewer = Class(name="ContentViewer")
presentation_ViewerComparator = Class(name="presentation::ViewerComparator")
presentation_StackLayout = Class(name="presentation::StackLayout")
presentation_ViewerSorter = Class(name="presentation::ViewerSorter")
presentation_StyledText = Class(name="presentation::StyledText")
presentation_ViewerFilter = Class(name="presentation::ViewerFilter", is_abstract=True)
presentation_StyledTextContent = Class(name="presentation::StyledTextContent", is_abstract=True)
presentation_StyleRange = Class(name="presentation::StyleRange")
presentation_TabFolder = Class(name="presentation::TabFolder")
presentation_TabItem = Class(name="presentation::TabItem")
TextStyle = Class(name="TextStyle")
presentation_TableColumn = Class(name="presentation::TableColumn")
presentation_Table = Class(name="presentation::Table")
presentation_TableEditor = Class(name="presentation::TableEditor")
ControlEditor = Class(name="ControlEditor")
presentation_TableViewer = Class(name="presentation::TableViewer")
AbstractTableViewer = Class(name="AbstractTableViewer")
presentation_TableTree = Class(name="presentation::TableTree")
presentation_TableTreeViewer = Class(name="presentation::TableTreeViewer")
AbstractTreeViewer = Class(name="AbstractTreeViewer")
presentation_TableViewerColumn = Class(name="presentation::TableViewerColumn")
ViewerColumn = Class(name="ViewerColumn")
presentation_Text = Class(name="presentation::Text")
presentation_ToolBar = Class(name="presentation::ToolBar")
presentation_TextCellEditor = Class(name="presentation::TextCellEditor")
presentation_TitleAreaDialog = Class(name="presentation::TitleAreaDialog")
TrayDialog = Class(name="TrayDialog")
presentation_ToolItem = Class(name="presentation::ToolItem")
presentation_Tray = Class(name="presentation::Tray")
presentation_ToolTip = Class(name="presentation::ToolTip")
presentation_Tracker = Class(name="presentation::Tracker")
presentation_Tree = Class(name="presentation::Tree")
presentation_TrayItem = Class(name="presentation::TrayItem")
presentation_TrayDialog = Class(name="presentation::TrayDialog", is_abstract=True)
presentation_TreeColumn = Class(name="presentation::TreeColumn")
presentation_TreeItem = Class(name="presentation::TreeItem")
presentation_TreeViewer = Class(name="presentation::TreeViewer")
presentation_ViewerColumn = Class(name="presentation::ViewerColumn", is_abstract=True)
presentation_URL = Class(name="presentation::URL")
presentation_Viewer = Class(name="presentation::Viewer", is_abstract=True)
ViewerComparator = Class(name="ViewerComparator")
presentation_WindowManager = Class(name="presentation::WindowManager")
presentation_XMLDataProvider = Class(name="presentation::XMLDataProvider")

# presentation_AbstractComboBoxCellEditor class attributes and methods
presentation_AbstractComboBoxCellEditor_activationStyle: Property = Property(name="activationStyle", type=StringType)
presentation_AbstractComboBoxCellEditor.attributes={presentation_AbstractComboBoxCellEditor_activationStyle}

# CellEditor class attributes and methods

# presentation_AbstractDataProvider class attributes and methods
presentation_AbstractDataProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_AbstractDataProvider_key: Property = Property(name="key", type=StringType)
presentation_AbstractDataProvider_group: Property = Property(name="group", type=StringType)
presentation_AbstractDataProvider.attributes={presentation_AbstractDataProvider_mixed, presentation_AbstractDataProvider_key, presentation_AbstractDataProvider_group}

# presentation_AbstractListViewer class attributes and methods

# StructuredViewer class attributes and methods

# presentation_AbstractTableViewer class attributes and methods
presentation_AbstractTableViewer_itemCount: Property = Property(name="itemCount", type=StringType)
presentation_AbstractTableViewer.attributes={presentation_AbstractTableViewer_itemCount}

# ColumnViewer class attributes and methods

# presentation_AbstractTreeViewer class attributes and methods
presentation_AbstractTreeViewer_group4: Property = Property(name="group4", type=StringType)
presentation_AbstractTreeViewer_autoExpandLevel: Property = Property(name="autoExpandLevel", type=StringType)
presentation_AbstractTreeViewer.attributes={presentation_AbstractTreeViewer_group4, presentation_AbstractTreeViewer_autoExpandLevel}

# presentation_IBindingContext class attributes and methods
presentation_IBindingContext_mixed: Property = Property(name="mixed", type=StringType)
presentation_IBindingContext.attributes={presentation_IBindingContext_mixed}

# presentation_TreePath class attributes and methods
presentation_TreePath_mixed: Property = Property(name="mixed", type=StringType)
presentation_TreePath.attributes={presentation_TreePath_mixed}

# presentation_EObject class attributes and methods

# presentation_Widget class attributes and methods
presentation_Widget_closeEvent: Property = Property(name="closeEvent", type=StringType)
presentation_Widget_collapseEvent: Property = Property(name="collapseEvent", type=StringType)
presentation_Widget_dataContext: Property = Property(name="dataContext", type=StringType)
presentation_Widget_deactivateEvent: Property = Property(name="deactivateEvent", type=StringType)
presentation_Widget_defaultSelectionEvent: Property = Property(name="defaultSelectionEvent", type=StringType)
presentation_Widget_deiconifyEvent: Property = Property(name="deiconifyEvent", type=StringType)
presentation_Widget_disposeEvent: Property = Property(name="disposeEvent", type=StringType)
presentation_Widget_dragDetectEvent: Property = Property(name="dragDetectEvent", type=StringType)
presentation_Widget_eraseItemEvent: Property = Property(name="eraseItemEvent", type=StringType)
presentation_Widget_mixed: Property = Property(name="mixed", type=StringType)
presentation_Widget_activateEvent: Property = Property(name="activateEvent", type=StringType)
presentation_Widget_armEvent: Property = Property(name="armEvent", type=StringType)
presentation_Widget_hideEvent: Property = Property(name="hideEvent", type=StringType)
presentation_Widget_iconifyEvent: Property = Property(name="iconifyEvent", type=StringType)
presentation_Widget_imeCompositionEvent: Property = Property(name="imeCompositionEvent", type=StringType)
presentation_Widget_keyDownEvent: Property = Property(name="keyDownEvent", type=StringType)
presentation_Widget_keyUpEvent: Property = Property(name="keyUpEvent", type=StringType)
presentation_Widget_measureItemEvent: Property = Property(name="measureItemEvent", type=StringType)
presentation_Widget_menuDetectEvent: Property = Property(name="menuDetectEvent", type=StringType)
presentation_Widget_expandEvent: Property = Property(name="expandEvent", type=StringType)
presentation_Widget_focusInEvent: Property = Property(name="focusInEvent", type=StringType)
presentation_Widget_focusOutEvent: Property = Property(name="focusOutEvent", type=StringType)
presentation_Widget_hardKeyDownEvent: Property = Property(name="hardKeyDownEvent", type=StringType)
presentation_Widget_hardKeyUpEvent: Property = Property(name="hardKeyUpEvent", type=StringType)
presentation_Widget_helpEvent: Property = Property(name="helpEvent", type=StringType)
presentation_Widget_mouseEnterEvent: Property = Property(name="mouseEnterEvent", type=StringType)
presentation_Widget_mouseExitEvent: Property = Property(name="mouseExitEvent", type=StringType)
presentation_Widget_mouseHoverEvent: Property = Property(name="mouseHoverEvent", type=StringType)
presentation_Widget_mouseMoveEvent: Property = Property(name="mouseMoveEvent", type=StringType)
presentation_Widget_mouseUpEvent: Property = Property(name="mouseUpEvent", type=StringType)
presentation_Widget_mouseWheelEvent: Property = Property(name="mouseWheelEvent", type=StringType)
presentation_Widget_moveEvent: Property = Property(name="moveEvent", type=StringType)
presentation_Widget_modifyEvent: Property = Property(name="modifyEvent", type=StringType)
presentation_Widget_mouseDoubleClickEvent: Property = Property(name="mouseDoubleClickEvent", type=StringType)
presentation_Widget_mouseDownEvent: Property = Property(name="mouseDownEvent", type=StringType)
presentation_Widget_showEvent: Property = Property(name="showEvent", type=StringType)
presentation_Widget_style: Property = Property(name="style", type=StringType)
presentation_Widget_traverseEvent: Property = Property(name="traverseEvent", type=StringType)
presentation_Widget_verifyEvent: Property = Property(name="verifyEvent", type=StringType)
presentation_Widget_paintEvent: Property = Property(name="paintEvent", type=StringType)
presentation_Widget_paintItemEvent: Property = Property(name="paintItemEvent", type=StringType)
presentation_Widget_resizeEvent: Property = Property(name="resizeEvent", type=StringType)
presentation_Widget_selectionEvent: Property = Property(name="selectionEvent", type=StringType)
presentation_Widget_setDataEvent: Property = Property(name="setDataEvent", type=StringType)
presentation_Widget.attributes={presentation_Widget_paintEvent, presentation_Widget_iconifyEvent, presentation_Widget_collapseEvent, presentation_Widget_eraseItemEvent, presentation_Widget_expandEvent, presentation_Widget_paintItemEvent, presentation_Widget_focusOutEvent, presentation_Widget_traverseEvent, presentation_Widget_menuDetectEvent, presentation_Widget_style, presentation_Widget_selectionEvent, presentation_Widget_defaultSelectionEvent, presentation_Widget_resizeEvent, presentation_Widget_deiconifyEvent, presentation_Widget_dataContext, presentation_Widget_keyDownEvent, presentation_Widget_moveEvent, presentation_Widget_focusInEvent, presentation_Widget_deactivateEvent, presentation_Widget_closeEvent, presentation_Widget_mixed, presentation_Widget_mouseEnterEvent, presentation_Widget_mouseHoverEvent, presentation_Widget_imeCompositionEvent, presentation_Widget_mouseUpEvent, presentation_Widget_helpEvent, presentation_Widget_mouseWheelEvent, presentation_Widget_showEvent, presentation_Widget_armEvent, presentation_Widget_mouseMoveEvent, presentation_Widget_activateEvent, presentation_Widget_keyUpEvent, presentation_Widget_mouseDoubleClickEvent, presentation_Widget_hardKeyUpEvent, presentation_Widget_dragDetectEvent, presentation_Widget_verifyEvent, presentation_Widget_hardKeyDownEvent, presentation_Widget_mouseDownEvent, presentation_Widget_hideEvent, presentation_Widget_mouseExitEvent, presentation_Widget_measureItemEvent, presentation_Widget_modifyEvent, presentation_Widget_disposeEvent, presentation_Widget_setDataEvent}

# presentation_Accessible class attributes and methods
presentation_Accessible_mixed: Property = Property(name="mixed", type=StringType)
presentation_Accessible.attributes={presentation_Accessible_mixed}

# presentation_Binding class attributes and methods
presentation_Binding_group: Property = Property(name="group", type=StringType)
presentation_Binding_elementName: Property = Property(name="elementName", type=StringType)
presentation_Binding_path: Property = Property(name="path", type=StringType)
presentation_Binding_xPath: Property = Property(name="xPath", type=StringType)
presentation_Binding_mixed: Property = Property(name="mixed", type=StringType)
presentation_Binding.attributes={presentation_Binding_xPath, presentation_Binding_path, presentation_Binding_group, presentation_Binding_elementName, presentation_Binding_mixed}

# presentation_Button class attributes and methods
presentation_Button_group1: Property = Property(name="group1", type=StringType)
presentation_Button_alignment: Property = Property(name="alignment", type=StringType)
presentation_Button_grayed: Property = Property(name="grayed", type=StringType)
presentation_Button_image: Property = Property(name="image", type=StringType)
presentation_Button_selection: Property = Property(name="selection", type=StringType)
presentation_Button_text: Property = Property(name="text", type=StringType)
presentation_Button.attributes={presentation_Button_alignment, presentation_Button_selection, presentation_Button_image, presentation_Button_text, presentation_Button_group1, presentation_Button_grayed}

# Control class attributes and methods

# presentation_ICommand class attributes and methods
presentation_ICommand_mixed: Property = Property(name="mixed", type=StringType)
presentation_ICommand.attributes={presentation_ICommand_mixed}

# presentation_Canvas class attributes and methods
presentation_Canvas_mixed1: Property = Property(name="mixed1", type=StringType)
presentation_Canvas_group3: Property = Property(name="group3", type=StringType)
presentation_Canvas.attributes={presentation_Canvas_mixed1, presentation_Canvas_group3}

# presentation_Browser class attributes and methods
presentation_Browser_text: Property = Property(name="text", type=StringType)
presentation_Browser_url: Property = Property(name="url", type=StringType)
presentation_Browser_group3: Property = Property(name="group3", type=StringType)
presentation_Browser_browserType: Property = Property(name="browserType", type=StringType)
presentation_Browser.attributes={presentation_Browser_text, presentation_Browser_browserType, presentation_Browser_url, presentation_Browser_group3}

# Composite class attributes and methods

# Widget class attributes and methods

# presentation_IME class attributes and methods
presentation_IME_ranges: Property = Property(name="ranges", type=StringType)
presentation_IME_compositionOffset: Property = Property(name="compositionOffset", type=StringType)
presentation_IME_text: Property = Property(name="text", type=StringType)
presentation_IME_group: Property = Property(name="group", type=StringType)
presentation_IME.attributes={presentation_IME_ranges, presentation_IME_text, presentation_IME_group, presentation_IME_compositionOffset}

# presentation_Caret class attributes and methods
presentation_Caret_group: Property = Property(name="group", type=StringType)
presentation_Caret_bounds: Property = Property(name="bounds", type=StringType)
presentation_Caret_font: Property = Property(name="font", type=StringType)
presentation_Caret_image: Property = Property(name="image", type=StringType)
presentation_Caret_location: Property = Property(name="location", type=StringType)
presentation_Caret_size: Property = Property(name="size", type=StringType)
presentation_Caret_visible: Property = Property(name="visible", type=StringType)
presentation_Caret.attributes={presentation_Caret_visible, presentation_Caret_image, presentation_Caret_font, presentation_Caret_bounds, presentation_Caret_size, presentation_Caret_group, presentation_Caret_location}

# presentation_CCombo class attributes and methods
presentation_CCombo_items: Property = Property(name="items", type=StringType)
presentation_CCombo_editable: Property = Property(name="editable", type=StringType)
presentation_CCombo_listVisible: Property = Property(name="listVisible", type=StringType)
presentation_CCombo_selection: Property = Property(name="selection", type=StringType)
presentation_CCombo_text: Property = Property(name="text", type=StringType)
presentation_CCombo_textLimit: Property = Property(name="textLimit", type=StringType)
presentation_CCombo_visibleItemCount: Property = Property(name="visibleItemCount", type=StringType)
presentation_CCombo_group3: Property = Property(name="group3", type=StringType)
presentation_CCombo.attributes={presentation_CCombo_group3, presentation_CCombo_selection, presentation_CCombo_visibleItemCount, presentation_CCombo_listVisible, presentation_CCombo_editable, presentation_CCombo_textLimit, presentation_CCombo_items, presentation_CCombo_text}

# presentation_CellEditor class attributes and methods
presentation_CellEditor_mixed: Property = Property(name="mixed", type=StringType)
presentation_CellEditor_group: Property = Property(name="group", type=StringType)
presentation_CellEditor_errorMessage: Property = Property(name="errorMessage", type=StringType)
presentation_CellEditor_style: Property = Property(name="style", type=StringType)
presentation_CellEditor.attributes={presentation_CellEditor_mixed, presentation_CellEditor_style, presentation_CellEditor_group, presentation_CellEditor_errorMessage}

# presentation_ICellEditorValidator class attributes and methods
presentation_ICellEditorValidator_mixed: Property = Property(name="mixed", type=StringType)
presentation_ICellEditorValidator.attributes={presentation_ICellEditorValidator_mixed}

# presentation_LayoutData class attributes and methods
presentation_LayoutData_mixed: Property = Property(name="mixed", type=StringType)
presentation_LayoutData.attributes={presentation_LayoutData_mixed}

# presentation_Cell class attributes and methods
presentation_Cell_image: Property = Property(name="image", type=StringType)
presentation_Cell_text: Property = Property(name="text", type=StringType)
presentation_Cell_mixed: Property = Property(name="mixed", type=StringType)
presentation_Cell_group: Property = Property(name="group", type=StringType)
presentation_Cell.attributes={presentation_Cell_mixed, presentation_Cell_image, presentation_Cell_text, presentation_Cell_group}

# presentation_TableItem class attributes and methods
presentation_TableItem_group: Property = Property(name="group", type=StringType)
presentation_TableItem_texts: Property = Property(name="texts", type=StringType)
presentation_TableItem_checked: Property = Property(name="checked", type=StringType)
presentation_TableItem_grayed: Property = Property(name="grayed", type=StringType)
presentation_TableItem_imageIndent: Property = Property(name="imageIndent", type=StringType)
presentation_TableItem.attributes={presentation_TableItem_grayed, presentation_TableItem_imageIndent, presentation_TableItem_checked, presentation_TableItem_texts, presentation_TableItem_group}

# presentation_CheckboxCellEditor class attributes and methods

# presentation_CheckboxTableViewer class attributes and methods
presentation_CheckboxTableViewer_group5: Property = Property(name="group5", type=StringType)
presentation_CheckboxTableViewer_allGrayed: Property = Property(name="allGrayed", type=StringType)
presentation_CheckboxTableViewer_allChecked: Property = Property(name="allChecked", type=StringType)
presentation_CheckboxTableViewer.attributes={presentation_CheckboxTableViewer_allGrayed, presentation_CheckboxTableViewer_group5, presentation_CheckboxTableViewer_allChecked}

# TableViewer class attributes and methods

# presentation_ICheckStateProvider class attributes and methods
presentation_ICheckStateProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_ICheckStateProvider.attributes={presentation_ICheckStateProvider_mixed}

# presentation_Control class attributes and methods
presentation_Control_group: Property = Property(name="group", type=StringType)
presentation_Control_backgroundImage: Property = Property(name="backgroundImage", type=StringType)
presentation_Control_bounds: Property = Property(name="bounds", type=StringType)
presentation_Control_capture: Property = Property(name="capture", type=StringType)
presentation_Control_dragDetect: Property = Property(name="dragDetect", type=StringType)
presentation_Control_enabled: Property = Property(name="enabled", type=StringType)
presentation_Control_background: Property = Property(name="background", type=StringType)
presentation_Control_handle: Property = Property(name="handle", type=StringType)
presentation_Control_location: Property = Property(name="location", type=StringType)
presentation_Control_redraw: Property = Property(name="redraw", type=StringType)
presentation_Control_size: Property = Property(name="size", type=StringType)
presentation_Control_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_Control_visible: Property = Property(name="visible", type=StringType)
presentation_Control_font: Property = Property(name="font", type=StringType)
presentation_Control_foreground: Property = Property(name="foreground", type=StringType)
presentation_Control.attributes={presentation_Control_font, presentation_Control_dragDetect, presentation_Control_redraw, presentation_Control_enabled, presentation_Control_background, presentation_Control_group, presentation_Control_foreground, presentation_Control_size, presentation_Control_bounds, presentation_Control_toolTipText, presentation_Control_visible, presentation_Control_capture, presentation_Control_location, presentation_Control_handle, presentation_Control_backgroundImage}

# presentation_CheckboxTreeViewer class attributes and methods
presentation_CheckboxTreeViewer_group6: Property = Property(name="group6", type=StringType)
presentation_CheckboxTreeViewer_allChecked: Property = Property(name="allChecked", type=StringType)
presentation_CheckboxTreeViewer.attributes={presentation_CheckboxTreeViewer_group6, presentation_CheckboxTreeViewer_allChecked}

# TreeViewer class attributes and methods

# presentation_CLabel class attributes and methods
presentation_CLabel_alignment: Property = Property(name="alignment", type=StringType)
presentation_CLabel_image: Property = Property(name="image", type=StringType)
presentation_CLabel_text: Property = Property(name="text", type=StringType)
presentation_CLabel.attributes={presentation_CLabel_text, presentation_CLabel_image, presentation_CLabel_alignment}

# Canvas class attributes and methods

# presentation_Class class attributes and methods
presentation_Class_mixed: Property = Property(name="mixed", type=StringType)
presentation_Class.attributes={presentation_Class_mixed}

# presentation_ColumnViewer class attributes and methods
presentation_ColumnViewer_group3: Property = Property(name="group3", type=StringType)
presentation_ColumnViewer.attributes={presentation_ColumnViewer_group3}

# presentation_ColumnViewerEditor class attributes and methods
presentation_ColumnViewerEditor_mixed: Property = Property(name="mixed", type=StringType)
presentation_ColumnViewerEditor.attributes={presentation_ColumnViewerEditor_mixed}

# presentation_ICellModifier class attributes and methods
presentation_ICellModifier_mixed: Property = Property(name="mixed", type=StringType)
presentation_ICellModifier.attributes={presentation_ICellModifier_mixed}

# presentation_Collection class attributes and methods
presentation_Collection_mixed: Property = Property(name="mixed", type=StringType)
presentation_Collection.attributes={presentation_Collection_mixed}

# presentation_ColorCellEditor class attributes and methods

# DialogCellEditor class attributes and methods

# presentation_Combo class attributes and methods
presentation_Combo_group3: Property = Property(name="group3", type=StringType)
presentation_Combo_items: Property = Property(name="items", type=StringType)
presentation_Combo_listVisible: Property = Property(name="listVisible", type=StringType)
presentation_Combo_visibleItemCount: Property = Property(name="visibleItemCount", type=StringType)
presentation_Combo_orientation: Property = Property(name="orientation", type=StringType)
presentation_Combo_selection: Property = Property(name="selection", type=StringType)
presentation_Combo_text: Property = Property(name="text", type=StringType)
presentation_Combo_textLimit: Property = Property(name="textLimit", type=StringType)
presentation_Combo.attributes={presentation_Combo_listVisible, presentation_Combo_selection, presentation_Combo_group3, presentation_Combo_text, presentation_Combo_items, presentation_Combo_orientation, presentation_Combo_visibleItemCount, presentation_Combo_textLimit}

# presentation_ComboBoxCellEditor class attributes and methods

# AbstractComboBoxCellEditor class attributes and methods

# presentation_ComboBoxViewerCellEditor class attributes and methods
presentation_ComboBoxViewerCellEditor_group1: Property = Property(name="group1", type=StringType)
presentation_ComboBoxViewerCellEditor.attributes={presentation_ComboBoxViewerCellEditor_group1}

# presentation_ComboViewer class attributes and methods

# AbstractListViewer class attributes and methods

# presentation_Composite class attributes and methods
presentation_Composite_group2: Property = Property(name="group2", type=StringType)
presentation_Composite_backgroundMode: Property = Property(name="backgroundMode", type=StringType)
presentation_Composite_layoutDeferred: Property = Property(name="layoutDeferred", type=StringType)
presentation_Composite.attributes={presentation_Composite_layoutDeferred, presentation_Composite_group2, presentation_Composite_backgroundMode}

# Scrollable class attributes and methods

# presentation_IStructuredContentProvider class attributes and methods
presentation_IStructuredContentProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_IStructuredContentProvider.attributes={presentation_IStructuredContentProvider_mixed}

# presentation_IBaseLabelProvider class attributes and methods
presentation_IBaseLabelProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_IBaseLabelProvider.attributes={presentation_IBaseLabelProvider_mixed}

# presentation_ContentViewer class attributes and methods
presentation_ContentViewer_group1: Property = Property(name="group1", type=StringType)
presentation_ContentViewer.attributes={presentation_ContentViewer_group1}

# Viewer class attributes and methods

# presentation_IContentProvider class attributes and methods
presentation_IContentProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_IContentProvider.attributes={presentation_IContentProvider_mixed}

# presentation_Layout class attributes and methods
presentation_Layout_mixed: Property = Property(name="mixed", type=StringType)
presentation_Layout.attributes={presentation_Layout_mixed}

# presentation_Menu class attributes and methods
presentation_Menu_group: Property = Property(name="group", type=StringType)
presentation_Menu_enabled: Property = Property(name="enabled", type=StringType)
presentation_Menu_handle: Property = Property(name="handle", type=StringType)
presentation_Menu_visible: Property = Property(name="visible", type=StringType)
presentation_Menu.attributes={presentation_Menu_group, presentation_Menu_handle, presentation_Menu_enabled, presentation_Menu_visible}

# presentation_Cursor class attributes and methods

# presentation_ControlEditor class attributes and methods
presentation_ControlEditor_group: Property = Property(name="group", type=StringType)
presentation_ControlEditor_grabHorizontal: Property = Property(name="grabHorizontal", type=StringType)
presentation_ControlEditor_grabVertical: Property = Property(name="grabVertical", type=StringType)
presentation_ControlEditor_mixed: Property = Property(name="mixed", type=StringType)
presentation_ControlEditor_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
presentation_ControlEditor_minimumHeight: Property = Property(name="minimumHeight", type=StringType)
presentation_ControlEditor_minimumWidth: Property = Property(name="minimumWidth", type=StringType)
presentation_ControlEditor_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
presentation_ControlEditor.attributes={presentation_ControlEditor_verticalAlignment, presentation_ControlEditor_group, presentation_ControlEditor_minimumWidth, presentation_ControlEditor_horizontalAlignment, presentation_ControlEditor_grabHorizontal, presentation_ControlEditor_mixed, presentation_ControlEditor_minimumHeight, presentation_ControlEditor_grabVertical}

# presentation_CoolBar class attributes and methods
presentation_CoolBar_group3: Property = Property(name="group3", type=StringType)
presentation_CoolBar_itemOrder: Property = Property(name="itemOrder", type=StringType)
presentation_CoolBar_wrapIndices: Property = Property(name="wrapIndices", type=StringType)
presentation_CoolBar_itemSizes: Property = Property(name="itemSizes", type=StringType)
presentation_CoolBar_locked: Property = Property(name="locked", type=StringType)
presentation_CoolBar.attributes={presentation_CoolBar_locked, presentation_CoolBar_itemOrder, presentation_CoolBar_group3, presentation_CoolBar_itemSizes, presentation_CoolBar_wrapIndices}

# presentation_CoolItem class attributes and methods
presentation_CoolItem_group: Property = Property(name="group", type=StringType)
presentation_CoolItem_preferredSize: Property = Property(name="preferredSize", type=StringType)
presentation_CoolItem_size: Property = Property(name="size", type=StringType)
presentation_CoolItem_bounds: Property = Property(name="bounds", type=StringType)
presentation_CoolItem_minimumSize: Property = Property(name="minimumSize", type=StringType)
presentation_CoolItem.attributes={presentation_CoolItem_group, presentation_CoolItem_preferredSize, presentation_CoolItem_bounds, presentation_CoolItem_size, presentation_CoolItem_minimumSize}

# Item class attributes and methods

# presentation_CTabFolder class attributes and methods
presentation_CTabFolder_group3: Property = Property(name="group3", type=StringType)
presentation_CTabFolder_borderVisible: Property = Property(name="borderVisible", type=StringType)
presentation_CTabFolder_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_CTabFolder_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_CTabFolder_minimized: Property = Property(name="minimized", type=StringType)
presentation_CTabFolder_minimizeVisible: Property = Property(name="minimizeVisible", type=StringType)
presentation_CTabFolder_minimumCharacters: Property = Property(name="minimumCharacters", type=StringType)
presentation_CTabFolder_maximized: Property = Property(name="maximized", type=StringType)
presentation_CTabFolder_maximizeVisible: Property = Property(name="maximizeVisible", type=StringType)
presentation_CTabFolder_mINTABWIDTH: Property = Property(name="mINTABWIDTH", type=StringType)
presentation_CTabFolder_selectionForeground: Property = Property(name="selectionForeground", type=StringType)
presentation_CTabFolder_simple: Property = Property(name="simple", type=StringType)
presentation_CTabFolder_single: Property = Property(name="single", type=StringType)
presentation_CTabFolder_tabHeight: Property = Property(name="tabHeight", type=StringType)
presentation_CTabFolder_tabPosition: Property = Property(name="tabPosition", type=StringType)
presentation_CTabFolder_mRUVisible: Property = Property(name="mRUVisible", type=StringType)
presentation_CTabFolder_selectionBackground: Property = Property(name="selectionBackground", type=StringType)
presentation_CTabFolder_unselectedCloseVisible: Property = Property(name="unselectedCloseVisible", type=StringType)
presentation_CTabFolder_unselectedImageVisible: Property = Property(name="unselectedImageVisible", type=StringType)
presentation_CTabFolder.attributes={presentation_CTabFolder_simple, presentation_CTabFolder_tabPosition, presentation_CTabFolder_group3, presentation_CTabFolder_mRUVisible, presentation_CTabFolder_minimizeVisible, presentation_CTabFolder_borderVisible, presentation_CTabFolder_marginHeight, presentation_CTabFolder_minimized, presentation_CTabFolder_maximizeVisible, presentation_CTabFolder_mINTABWIDTH, presentation_CTabFolder_minimumCharacters, presentation_CTabFolder_single, presentation_CTabFolder_tabHeight, presentation_CTabFolder_marginWidth, presentation_CTabFolder_selectionBackground, presentation_CTabFolder_unselectedCloseVisible, presentation_CTabFolder_maximized, presentation_CTabFolder_unselectedImageVisible, presentation_CTabFolder_selectionForeground}

# presentation_RGB class attributes and methods
presentation_RGB_mixed: Property = Property(name="mixed", type=StringType)
presentation_RGB.attributes={presentation_RGB_mixed}

# presentation_CTabItem class attributes and methods
presentation_CTabItem_group: Property = Property(name="group", type=StringType)
presentation_CTabItem_bounds: Property = Property(name="bounds", type=StringType)
presentation_CTabItem_disabledImage: Property = Property(name="disabledImage", type=StringType)
presentation_CTabItem_font: Property = Property(name="font", type=StringType)
presentation_CTabItem_showClose: Property = Property(name="showClose", type=StringType)
presentation_CTabItem_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_CTabItem.attributes={presentation_CTabItem_bounds, presentation_CTabItem_font, presentation_CTabItem_toolTipText, presentation_CTabItem_showClose, presentation_CTabItem_group, presentation_CTabItem_disabledImage}

# presentation_DateTime class attributes and methods
presentation_DateTime_day: Property = Property(name="day", type=StringType)
presentation_DateTime_hours: Property = Property(name="hours", type=StringType)
presentation_DateTime_seconds: Property = Property(name="seconds", type=StringType)
presentation_DateTime_year: Property = Property(name="year", type=StringType)
presentation_DateTime_minutes: Property = Property(name="minutes", type=StringType)
presentation_DateTime_month: Property = Property(name="month", type=StringType)
presentation_DateTime.attributes={presentation_DateTime_month, presentation_DateTime_day, presentation_DateTime_year, presentation_DateTime_seconds, presentation_DateTime_hours, presentation_DateTime_minutes}

# Resource class attributes and methods

# presentation_Decorations class attributes and methods
presentation_Decorations_group4: Property = Property(name="group4", type=StringType)
presentation_Decorations_image: Property = Property(name="image", type=StringType)
presentation_Decorations_maximized: Property = Property(name="maximized", type=StringType)
presentation_Decorations_minimized: Property = Property(name="minimized", type=StringType)
presentation_Decorations_text: Property = Property(name="text", type=StringType)
presentation_Decorations_images: Property = Property(name="images", type=StringType)
presentation_Decorations.attributes={presentation_Decorations_maximized, presentation_Decorations_group4, presentation_Decorations_image, presentation_Decorations_text, presentation_Decorations_images, presentation_Decorations_minimized}

# presentation_Dialog class attributes and methods
presentation_Dialog_group1: Property = Property(name="group1", type=StringType)
presentation_Dialog.attributes={presentation_Dialog_group1}

# Window class attributes and methods

# presentation_IDialogBlockedHandler class attributes and methods
presentation_IDialogBlockedHandler_mixed: Property = Property(name="mixed", type=StringType)
presentation_IDialogBlockedHandler.attributes={presentation_IDialogBlockedHandler_mixed}

# presentation_DefaultCellModifier class attributes and methods
presentation_DefaultCellModifier_mixed: Property = Property(name="mixed", type=StringType)
presentation_DefaultCellModifier.attributes={presentation_DefaultCellModifier_mixed}

# presentation_DefaultLabelProvider class attributes and methods
presentation_DefaultLabelProvider_mixed: Property = Property(name="mixed", type=StringType)
presentation_DefaultLabelProvider.attributes={presentation_DefaultLabelProvider_mixed}

# presentation_Document class attributes and methods
presentation_Document_mixed: Property = Property(name="mixed", type=StringType)
presentation_Document.attributes={presentation_Document_mixed}

# presentation_DocumentObject class attributes and methods

# Observable class attributes and methods

# presentation_DocumentRoot class attributes and methods
presentation_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
presentation_DocumentRoot.attributes={presentation_DocumentRoot_mixed}

# presentation_EStringToStringMapEntry class attributes and methods

# presentation_DialogCellEditor class attributes and methods

# presentation_DialogTray class attributes and methods
presentation_DialogTray_mixed: Property = Property(name="mixed", type=StringType)
presentation_DialogTray.attributes={presentation_DialogTray_mixed}

# presentation_Window class attributes and methods
presentation_Window_mixed: Property = Property(name="mixed", type=StringType)
presentation_Window_group: Property = Property(name="group", type=StringType)
presentation_Window_blockOnOpen: Property = Property(name="blockOnOpen", type=StringType)
presentation_Window.attributes={presentation_Window_mixed, presentation_Window_group, presentation_Window_blockOnOpen}

# presentation_Element class attributes and methods

# DocumentObject class attributes and methods

# presentation_ExpandBar class attributes and methods
presentation_ExpandBar_spacing: Property = Property(name="spacing", type=StringType)
presentation_ExpandBar_group3: Property = Property(name="group3", type=StringType)
presentation_ExpandBar.attributes={presentation_ExpandBar_spacing, presentation_ExpandBar_group3}

# presentation_ExpandItem class attributes and methods
presentation_ExpandItem_group: Property = Property(name="group", type=StringType)
presentation_ExpandItem_expanded: Property = Property(name="expanded", type=StringType)
presentation_ExpandItem_height: Property = Property(name="height", type=StringType)
presentation_ExpandItem.attributes={presentation_ExpandItem_height, presentation_ExpandItem_expanded, presentation_ExpandItem_group}

# presentation_FormAttachment class attributes and methods
presentation_FormAttachment_alignment: Property = Property(name="alignment", type=StringType)
presentation_FormAttachment_denominator: Property = Property(name="denominator", type=StringType)
presentation_FormAttachment_numerator: Property = Property(name="numerator", type=StringType)
presentation_FormAttachment_offset: Property = Property(name="offset", type=StringType)
presentation_FormAttachment_mixed: Property = Property(name="mixed", type=StringType)
presentation_FormAttachment_group: Property = Property(name="group", type=StringType)
presentation_FormAttachment.attributes={presentation_FormAttachment_group, presentation_FormAttachment_mixed, presentation_FormAttachment_offset, presentation_FormAttachment_denominator, presentation_FormAttachment_alignment, presentation_FormAttachment_numerator}

# presentation_FillLayout class attributes and methods
presentation_FillLayout_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_FillLayout_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_FillLayout_spacing: Property = Property(name="spacing", type=StringType)
presentation_FillLayout_type: Property = Property(name="type", type=StringType)
presentation_FillLayout.attributes={presentation_FillLayout_marginWidth, presentation_FillLayout_type, presentation_FillLayout_marginHeight, presentation_FillLayout_spacing}

# Layout class attributes and methods

# presentation_FormData class attributes and methods
presentation_FormData_mixed: Property = Property(name="mixed", type=StringType)
presentation_FormData_group: Property = Property(name="group", type=StringType)
presentation_FormData_height: Property = Property(name="height", type=StringType)
presentation_FormData_width: Property = Property(name="width", type=StringType)
presentation_FormData.attributes={presentation_FormData_width, presentation_FormData_height, presentation_FormData_mixed, presentation_FormData_group}

# presentation_FormLayout class attributes and methods
presentation_FormLayout_marginBottom: Property = Property(name="marginBottom", type=StringType)
presentation_FormLayout_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_FormLayout_marginTop: Property = Property(name="marginTop", type=StringType)
presentation_FormLayout_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_FormLayout_spacing: Property = Property(name="spacing", type=StringType)
presentation_FormLayout_marginLeft: Property = Property(name="marginLeft", type=StringType)
presentation_FormLayout_marginRight: Property = Property(name="marginRight", type=StringType)
presentation_FormLayout.attributes={presentation_FormLayout_marginHeight, presentation_FormLayout_marginLeft, presentation_FormLayout_spacing, presentation_FormLayout_marginRight, presentation_FormLayout_marginWidth, presentation_FormLayout_marginTop, presentation_FormLayout_marginBottom}

# presentation_GridData class attributes and methods
presentation_GridData_mixed: Property = Property(name="mixed", type=StringType)
presentation_GridData_grabExcessVerticalSpace: Property = Property(name="grabExcessVerticalSpace", type=StringType)
presentation_GridData_heightHint: Property = Property(name="heightHint", type=StringType)
presentation_GridData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
presentation_GridData_horizontalIndent: Property = Property(name="horizontalIndent", type=StringType)
presentation_GridData_horizontalSpan: Property = Property(name="horizontalSpan", type=StringType)
presentation_GridData_exclude: Property = Property(name="exclude", type=StringType)
presentation_GridData_grabExcessHorizontalSpace: Property = Property(name="grabExcessHorizontalSpace", type=StringType)
presentation_GridData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
presentation_GridData_verticalIndent: Property = Property(name="verticalIndent", type=StringType)
presentation_GridData_verticalSpan: Property = Property(name="verticalSpan", type=StringType)
presentation_GridData_widthHint: Property = Property(name="widthHint", type=StringType)
presentation_GridData_minimumHeight: Property = Property(name="minimumHeight", type=StringType)
presentation_GridData_minimumWidth: Property = Property(name="minimumWidth", type=StringType)
presentation_GridData.attributes={presentation_GridData_minimumHeight, presentation_GridData_verticalIndent, presentation_GridData_grabExcessVerticalSpace, presentation_GridData_exclude, presentation_GridData_heightHint, presentation_GridData_grabExcessHorizontalSpace, presentation_GridData_widthHint, presentation_GridData_mixed, presentation_GridData_horizontalSpan, presentation_GridData_verticalSpan, presentation_GridData_verticalAlignment, presentation_GridData_minimumWidth, presentation_GridData_horizontalIndent, presentation_GridData_horizontalAlignment}

# presentation_GridLayout class attributes and methods
presentation_GridLayout_marginBottom: Property = Property(name="marginBottom", type=StringType)
presentation_GridLayout_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_GridLayout_marginLeft: Property = Property(name="marginLeft", type=StringType)
presentation_GridLayout_marginRight: Property = Property(name="marginRight", type=StringType)
presentation_GridLayout_marginTop: Property = Property(name="marginTop", type=StringType)
presentation_GridLayout_horizontalSpacing: Property = Property(name="horizontalSpacing", type=StringType)
presentation_GridLayout_makeColumnsEqualWidth: Property = Property(name="makeColumnsEqualWidth", type=StringType)
presentation_GridLayout_verticalSpacing: Property = Property(name="verticalSpacing", type=StringType)
presentation_GridLayout_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_GridLayout_numColumns: Property = Property(name="numColumns", type=StringType)
presentation_GridLayout.attributes={presentation_GridLayout_marginWidth, presentation_GridLayout_marginHeight, presentation_GridLayout_verticalSpacing, presentation_GridLayout_numColumns, presentation_GridLayout_horizontalSpacing, presentation_GridLayout_marginLeft, presentation_GridLayout_makeColumnsEqualWidth, presentation_GridLayout_marginTop, presentation_GridLayout_marginRight, presentation_GridLayout_marginBottom}

# presentation_Group class attributes and methods
presentation_Group_text: Property = Property(name="text", type=StringType)
presentation_Group.attributes={presentation_Group_text}

# presentation_IElementComparer class attributes and methods
presentation_IElementComparer_mixed: Property = Property(name="mixed", type=StringType)
presentation_IElementComparer.attributes={presentation_IElementComparer_mixed}

# presentation_TextStyle class attributes and methods
presentation_TextStyle_mixed: Property = Property(name="mixed", type=StringType)
presentation_TextStyle.attributes={presentation_TextStyle_mixed}

# presentation_Item class attributes and methods
presentation_Item_image: Property = Property(name="image", type=StringType)
presentation_Item_text: Property = Property(name="text", type=StringType)
presentation_Item.attributes={presentation_Item_image, presentation_Item_text}

# presentation_ISelection class attributes and methods
presentation_ISelection_mixed: Property = Property(name="mixed", type=StringType)
presentation_ISelection.attributes={presentation_ISelection_mixed}

# presentation_Label class attributes and methods
presentation_Label_text: Property = Property(name="text", type=StringType)
presentation_Label_alignment: Property = Property(name="alignment", type=StringType)
presentation_Label_image: Property = Property(name="image", type=StringType)
presentation_Label.attributes={presentation_Label_image, presentation_Label_alignment, presentation_Label_text}

# presentation_List class attributes and methods
presentation_List_group2: Property = Property(name="group2", type=StringType)
presentation_List_items: Property = Property(name="items", type=StringType)
presentation_List_selection: Property = Property(name="selection", type=StringType)
presentation_List_selectionIndices: Property = Property(name="selectionIndices", type=StringType)
presentation_List_topIndex: Property = Property(name="topIndex", type=StringType)
presentation_List.attributes={presentation_List_items, presentation_List_group2, presentation_List_selection, presentation_List_topIndex, presentation_List_selectionIndices}

# presentation_Link class attributes and methods
presentation_Link_text: Property = Property(name="text", type=StringType)
presentation_Link.attributes={presentation_Link_text}

# presentation_ListViewer class attributes and methods
presentation_ListViewer_group3: Property = Property(name="group3", type=StringType)
presentation_ListViewer.attributes={presentation_ListViewer_group3}

# presentation_Listener class attributes and methods
presentation_Listener_mixed: Property = Property(name="mixed", type=StringType)
presentation_Listener.attributes={presentation_Listener_mixed}

# presentation_MenuItem class attributes and methods
presentation_MenuItem_group: Property = Property(name="group", type=StringType)
presentation_MenuItem_accelerator: Property = Property(name="accelerator", type=StringType)
presentation_MenuItem_enabled: Property = Property(name="enabled", type=StringType)
presentation_MenuItem_selection: Property = Property(name="selection", type=StringType)
presentation_MenuItem.attributes={presentation_MenuItem_selection, presentation_MenuItem_enabled, presentation_MenuItem_accelerator, presentation_MenuItem_group}

# presentation_MessageBox class attributes and methods
presentation_MessageBox_message: Property = Property(name="message", type=StringType)
presentation_MessageBox.attributes={presentation_MessageBox_message}

# Dialog class attributes and methods

# presentation_ObjectDataProvider class attributes and methods
presentation_ObjectDataProvider_group1: Property = Property(name="group1", type=StringType)
presentation_ObjectDataProvider_methodName: Property = Property(name="methodName", type=StringType)
presentation_ObjectDataProvider.attributes={presentation_ObjectDataProvider_methodName, presentation_ObjectDataProvider_group1}

# AbstractDataProvider class attributes and methods

# presentation_Observable class attributes and methods
presentation_Observable_mixed: Property = Property(name="mixed", type=StringType)
presentation_Observable.attributes={presentation_Observable_mixed}

# presentation_Resource class attributes and methods
presentation_Resource_mixed: Property = Property(name="mixed", type=StringType)
presentation_Resource.attributes={presentation_Resource_mixed}

# presentation_ProgressBar class attributes and methods
presentation_ProgressBar_minimum: Property = Property(name="minimum", type=StringType)
presentation_ProgressBar_selection: Property = Property(name="selection", type=StringType)
presentation_ProgressBar_state: Property = Property(name="state", type=StringType)
presentation_ProgressBar_maximum: Property = Property(name="maximum", type=StringType)
presentation_ProgressBar.attributes={presentation_ProgressBar_maximum, presentation_ProgressBar_state, presentation_ProgressBar_selection, presentation_ProgressBar_minimum}

# presentation_RowData class attributes and methods
presentation_RowData_mixed: Property = Property(name="mixed", type=StringType)
presentation_RowData_exclude: Property = Property(name="exclude", type=StringType)
presentation_RowData_height: Property = Property(name="height", type=StringType)
presentation_RowData_width: Property = Property(name="width", type=StringType)
presentation_RowData.attributes={presentation_RowData_exclude, presentation_RowData_height, presentation_RowData_mixed, presentation_RowData_width}

# presentation_RowLayout class attributes and methods
presentation_RowLayout_fill: Property = Property(name="fill", type=StringType)
presentation_RowLayout_justify: Property = Property(name="justify", type=StringType)
presentation_RowLayout_marginBottom: Property = Property(name="marginBottom", type=StringType)
presentation_RowLayout_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_RowLayout_marginLeft: Property = Property(name="marginLeft", type=StringType)
presentation_RowLayout_marginRight: Property = Property(name="marginRight", type=StringType)
presentation_RowLayout_marginTop: Property = Property(name="marginTop", type=StringType)
presentation_RowLayout_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_RowLayout_pack: Property = Property(name="pack", type=StringType)
presentation_RowLayout_spacing: Property = Property(name="spacing", type=StringType)
presentation_RowLayout_center: Property = Property(name="center", type=StringType)
presentation_RowLayout_type: Property = Property(name="type", type=StringType)
presentation_RowLayout_wrap: Property = Property(name="wrap", type=StringType)
presentation_RowLayout.attributes={presentation_RowLayout_justify, presentation_RowLayout_marginHeight, presentation_RowLayout_fill, presentation_RowLayout_center, presentation_RowLayout_marginTop, presentation_RowLayout_type, presentation_RowLayout_wrap, presentation_RowLayout_marginRight, presentation_RowLayout_marginBottom, presentation_RowLayout_marginWidth, presentation_RowLayout_marginLeft, presentation_RowLayout_spacing, presentation_RowLayout_pack}

# presentation_Scale class attributes and methods
presentation_Scale_increment: Property = Property(name="increment", type=StringType)
presentation_Scale_maximum: Property = Property(name="maximum", type=StringType)
presentation_Scale_minimum: Property = Property(name="minimum", type=StringType)
presentation_Scale_pageIncrement: Property = Property(name="pageIncrement", type=StringType)
presentation_Scale_selection: Property = Property(name="selection", type=StringType)
presentation_Scale.attributes={presentation_Scale_pageIncrement, presentation_Scale_increment, presentation_Scale_minimum, presentation_Scale_maximum, presentation_Scale_selection}

# presentation_Sash class attributes and methods

# presentation_SashForm class attributes and methods
presentation_SashForm_weights: Property = Property(name="weights", type=StringType)
presentation_SashForm_orientation: Property = Property(name="orientation", type=StringType)
presentation_SashForm_sASHWIDTH: Property = Property(name="sASHWIDTH", type=StringType)
presentation_SashForm_sashWidth1: Property = Property(name="sashWidth1", type=StringType)
presentation_SashForm_group3: Property = Property(name="group3", type=StringType)
presentation_SashForm.attributes={presentation_SashForm_sashWidth1, presentation_SashForm_weights, presentation_SashForm_sASHWIDTH, presentation_SashForm_group3, presentation_SashForm_orientation}

# presentation_Scrollable class attributes and methods
presentation_Scrollable_clientArea: Property = Property(name="clientArea", type=StringType)
presentation_Scrollable_group1: Property = Property(name="group1", type=StringType)
presentation_Scrollable.attributes={presentation_Scrollable_clientArea, presentation_Scrollable_group1}

# presentation_ScrollBar class attributes and methods
presentation_ScrollBar_group: Property = Property(name="group", type=StringType)
presentation_ScrollBar_enabled: Property = Property(name="enabled", type=StringType)
presentation_ScrollBar_increment: Property = Property(name="increment", type=StringType)
presentation_ScrollBar_maximum: Property = Property(name="maximum", type=StringType)
presentation_ScrollBar_minimum: Property = Property(name="minimum", type=StringType)
presentation_ScrollBar_thumb: Property = Property(name="thumb", type=StringType)
presentation_ScrollBar_visible: Property = Property(name="visible", type=StringType)
presentation_ScrollBar_pageIncrement: Property = Property(name="pageIncrement", type=StringType)
presentation_ScrollBar_selection: Property = Property(name="selection", type=StringType)
presentation_ScrollBar_size: Property = Property(name="size", type=StringType)
presentation_ScrollBar.attributes={presentation_ScrollBar_maximum, presentation_ScrollBar_increment, presentation_ScrollBar_minimum, presentation_ScrollBar_visible, presentation_ScrollBar_enabled, presentation_ScrollBar_thumb, presentation_ScrollBar_selection, presentation_ScrollBar_group, presentation_ScrollBar_pageIncrement, presentation_ScrollBar_size}

# presentation_Shell class attributes and methods
presentation_Shell_group5: Property = Property(name="group5", type=StringType)
presentation_Shell_imeInputMode: Property = Property(name="imeInputMode", type=StringType)
presentation_Shell_minimumSize: Property = Property(name="minimumSize", type=StringType)
presentation_Shell_alpha: Property = Property(name="alpha", type=StringType)
presentation_Shell_fullScreen: Property = Property(name="fullScreen", type=StringType)
presentation_Shell.attributes={presentation_Shell_group5, presentation_Shell_imeInputMode, presentation_Shell_fullScreen, presentation_Shell_minimumSize, presentation_Shell_alpha}

# Decorations class attributes and methods

# presentation_Slider class attributes and methods
presentation_Slider_increment: Property = Property(name="increment", type=StringType)
presentation_Slider_maximum: Property = Property(name="maximum", type=StringType)
presentation_Slider_minimum: Property = Property(name="minimum", type=StringType)
presentation_Slider_pageIncrement: Property = Property(name="pageIncrement", type=StringType)
presentation_Slider_selection: Property = Property(name="selection", type=StringType)
presentation_Slider_thumb: Property = Property(name="thumb", type=StringType)
presentation_Slider.attributes={presentation_Slider_maximum, presentation_Slider_pageIncrement, presentation_Slider_minimum, presentation_Slider_increment, presentation_Slider_selection, presentation_Slider_thumb}

# presentation_Spinner class attributes and methods
presentation_Spinner_digits: Property = Property(name="digits", type=StringType)
presentation_Spinner_increment: Property = Property(name="increment", type=StringType)
presentation_Spinner_maximum: Property = Property(name="maximum", type=StringType)
presentation_Spinner_minimum: Property = Property(name="minimum", type=StringType)
presentation_Spinner_pageIncrement: Property = Property(name="pageIncrement", type=StringType)
presentation_Spinner_selection: Property = Property(name="selection", type=StringType)
presentation_Spinner_text: Property = Property(name="text", type=StringType)
presentation_Spinner_textLimit: Property = Property(name="textLimit", type=StringType)
presentation_Spinner.attributes={presentation_Spinner_increment, presentation_Spinner_text, presentation_Spinner_maximum, presentation_Spinner_pageIncrement, presentation_Spinner_selection, presentation_Spinner_minimum, presentation_Spinner_digits, presentation_Spinner_textLimit}

# presentation_StructuredViewer class attributes and methods
presentation_StructuredViewer_group2: Property = Property(name="group2", type=StringType)
presentation_StructuredViewer_useHashlookup: Property = Property(name="useHashlookup", type=StringType)
presentation_StructuredViewer.attributes={presentation_StructuredViewer_group2, presentation_StructuredViewer_useHashlookup}

# ContentViewer class attributes and methods

# presentation_ViewerComparator class attributes and methods
presentation_ViewerComparator_mixed: Property = Property(name="mixed", type=StringType)
presentation_ViewerComparator.attributes={presentation_ViewerComparator_mixed}

# presentation_StackLayout class attributes and methods
presentation_StackLayout_marginHeight: Property = Property(name="marginHeight", type=StringType)
presentation_StackLayout_marginWidth: Property = Property(name="marginWidth", type=StringType)
presentation_StackLayout_group: Property = Property(name="group", type=StringType)
presentation_StackLayout.attributes={presentation_StackLayout_group, presentation_StackLayout_marginHeight, presentation_StackLayout_marginWidth}

# presentation_ViewerSorter class attributes and methods

# presentation_StyledText class attributes and methods
presentation_StyledText_group4: Property = Property(name="group4", type=StringType)
presentation_StyledText_ranges: Property = Property(name="ranges", type=StringType)
presentation_StyledText_selectionRanges: Property = Property(name="selectionRanges", type=StringType)
presentation_StyledText_alignment: Property = Property(name="alignment", type=StringType)
presentation_StyledText_bidiColoring: Property = Property(name="bidiColoring", type=StringType)
presentation_StyledText_blockSelection: Property = Property(name="blockSelection", type=StringType)
presentation_StyledText_caretOffset: Property = Property(name="caretOffset", type=StringType)
presentation_StyledText_doubleClickEnabled: Property = Property(name="doubleClickEnabled", type=StringType)
presentation_StyledText_lineSpacing: Property = Property(name="lineSpacing", type=StringType)
presentation_StyledText_orientation: Property = Property(name="orientation", type=StringType)
presentation_StyledText_selection: Property = Property(name="selection", type=StringType)
presentation_StyledText_selectionBackground: Property = Property(name="selectionBackground", type=StringType)
presentation_StyledText_selectionForeground: Property = Property(name="selectionForeground", type=StringType)
presentation_StyledText_editable: Property = Property(name="editable", type=StringType)
presentation_StyledText_horizontalIndex: Property = Property(name="horizontalIndex", type=StringType)
presentation_StyledText_horizontalPixel: Property = Property(name="horizontalPixel", type=StringType)
presentation_StyledText_indent: Property = Property(name="indent", type=StringType)
presentation_StyledText_justify: Property = Property(name="justify", type=StringType)
presentation_StyledText_lineDelimiter: Property = Property(name="lineDelimiter", type=StringType)
presentation_StyledText_selectionText: Property = Property(name="selectionText", type=StringType)
presentation_StyledText_tabs: Property = Property(name="tabs", type=StringType)
presentation_StyledText_text: Property = Property(name="text", type=StringType)
presentation_StyledText_textLimit: Property = Property(name="textLimit", type=StringType)
presentation_StyledText_topIndex: Property = Property(name="topIndex", type=StringType)
presentation_StyledText_topPixel: Property = Property(name="topPixel", type=StringType)
presentation_StyledText_wordWrap: Property = Property(name="wordWrap", type=StringType)
presentation_StyledText.attributes={presentation_StyledText_caretOffset, presentation_StyledText_editable, presentation_StyledText_blockSelection, presentation_StyledText_group4, presentation_StyledText_lineSpacing, presentation_StyledText_tabs, presentation_StyledText_selectionText, presentation_StyledText_selectionForeground, presentation_StyledText_selectionBackground, presentation_StyledText_horizontalPixel, presentation_StyledText_doubleClickEnabled, presentation_StyledText_lineDelimiter, presentation_StyledText_topPixel, presentation_StyledText_horizontalIndex, presentation_StyledText_wordWrap, presentation_StyledText_textLimit, presentation_StyledText_ranges, presentation_StyledText_orientation, presentation_StyledText_topIndex, presentation_StyledText_bidiColoring, presentation_StyledText_selectionRanges, presentation_StyledText_justify, presentation_StyledText_indent, presentation_StyledText_text, presentation_StyledText_selection, presentation_StyledText_alignment}

# presentation_ViewerFilter class attributes and methods
presentation_ViewerFilter_mixed: Property = Property(name="mixed", type=StringType)
presentation_ViewerFilter.attributes={presentation_ViewerFilter_mixed}

# presentation_StyledTextContent class attributes and methods
presentation_StyledTextContent_mixed: Property = Property(name="mixed", type=StringType)
presentation_StyledTextContent.attributes={presentation_StyledTextContent_mixed}

# presentation_StyleRange class attributes and methods

# presentation_TabFolder class attributes and methods
presentation_TabFolder_group3: Property = Property(name="group3", type=StringType)
presentation_TabFolder.attributes={presentation_TabFolder_group3}

# presentation_TabItem class attributes and methods
presentation_TabItem_group: Property = Property(name="group", type=StringType)
presentation_TabItem_bounds: Property = Property(name="bounds", type=StringType)
presentation_TabItem_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_TabItem.attributes={presentation_TabItem_group, presentation_TabItem_toolTipText, presentation_TabItem_bounds}

# TextStyle class attributes and methods

# presentation_TableColumn class attributes and methods
presentation_TableColumn_resizable: Property = Property(name="resizable", type=StringType)
presentation_TableColumn_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_TableColumn_width: Property = Property(name="width", type=StringType)
presentation_TableColumn_group: Property = Property(name="group", type=StringType)
presentation_TableColumn_alignment: Property = Property(name="alignment", type=StringType)
presentation_TableColumn_moveable: Property = Property(name="moveable", type=StringType)
presentation_TableColumn.attributes={presentation_TableColumn_group, presentation_TableColumn_alignment, presentation_TableColumn_resizable, presentation_TableColumn_toolTipText, presentation_TableColumn_moveable, presentation_TableColumn_width}

# presentation_Table class attributes and methods
presentation_Table_group3: Property = Property(name="group3", type=StringType)
presentation_Table_itemCount: Property = Property(name="itemCount", type=StringType)
presentation_Table_linesVisible: Property = Property(name="linesVisible", type=StringType)
presentation_Table_sortDirection: Property = Property(name="sortDirection", type=StringType)
presentation_Table_topIndex: Property = Property(name="topIndex", type=StringType)
presentation_Table_columnOrder: Property = Property(name="columnOrder", type=StringType)
presentation_Table_selectionIndices: Property = Property(name="selectionIndices", type=StringType)
presentation_Table_headerVisible: Property = Property(name="headerVisible", type=StringType)
presentation_Table.attributes={presentation_Table_linesVisible, presentation_Table_group3, presentation_Table_sortDirection, presentation_Table_selectionIndices, presentation_Table_columnOrder, presentation_Table_headerVisible, presentation_Table_itemCount, presentation_Table_topIndex}

# presentation_TableEditor class attributes and methods
presentation_TableEditor_group1: Property = Property(name="group1", type=StringType)
presentation_TableEditor_column: Property = Property(name="column", type=StringType)
presentation_TableEditor_dynamic: Property = Property(name="dynamic", type=StringType)
presentation_TableEditor.attributes={presentation_TableEditor_group1, presentation_TableEditor_column, presentation_TableEditor_dynamic}

# ControlEditor class attributes and methods

# presentation_TableViewer class attributes and methods
presentation_TableViewer_group4: Property = Property(name="group4", type=StringType)
presentation_TableViewer.attributes={presentation_TableViewer_group4}

# AbstractTableViewer class attributes and methods

# presentation_TableTree class attributes and methods

# presentation_TableTreeViewer class attributes and methods
presentation_TableTreeViewer_group5: Property = Property(name="group5", type=StringType)
presentation_TableTreeViewer.attributes={presentation_TableTreeViewer_group5}

# AbstractTreeViewer class attributes and methods

# presentation_TableViewerColumn class attributes and methods
presentation_TableViewerColumn_width: Property = Property(name="width", type=StringType)
presentation_TableViewerColumn_group: Property = Property(name="group", type=StringType)
presentation_TableViewerColumn_text: Property = Property(name="text", type=StringType)
presentation_TableViewerColumn.attributes={presentation_TableViewerColumn_text, presentation_TableViewerColumn_width, presentation_TableViewerColumn_group}

# ViewerColumn class attributes and methods

# presentation_Text class attributes and methods
presentation_Text_message: Property = Property(name="message", type=StringType)
presentation_Text_orientation: Property = Property(name="orientation", type=StringType)
presentation_Text_selection: Property = Property(name="selection", type=StringType)
presentation_Text_selectionText: Property = Property(name="selectionText", type=StringType)
presentation_Text_tabs: Property = Property(name="tabs", type=StringType)
presentation_Text_text: Property = Property(name="text", type=StringType)
presentation_Text_caretLocation: Property = Property(name="caretLocation", type=StringType)
presentation_Text_doubleClickEnabled: Property = Property(name="doubleClickEnabled", type=StringType)
presentation_Text_echoChar: Property = Property(name="echoChar", type=StringType)
presentation_Text_editable: Property = Property(name="editable", type=StringType)
presentation_Text_lineDelimiter: Property = Property(name="lineDelimiter", type=StringType)
presentation_Text_textLimit: Property = Property(name="textLimit", type=StringType)
presentation_Text_topIndex: Property = Property(name="topIndex", type=StringType)
presentation_Text.attributes={presentation_Text_selection, presentation_Text_caretLocation, presentation_Text_lineDelimiter, presentation_Text_message, presentation_Text_topIndex, presentation_Text_echoChar, presentation_Text_tabs, presentation_Text_editable, presentation_Text_selectionText, presentation_Text_doubleClickEnabled, presentation_Text_text, presentation_Text_textLimit, presentation_Text_orientation}

# presentation_ToolBar class attributes and methods
presentation_ToolBar_group3: Property = Property(name="group3", type=StringType)
presentation_ToolBar.attributes={presentation_ToolBar_group3}

# presentation_TextCellEditor class attributes and methods

# presentation_TitleAreaDialog class attributes and methods
presentation_TitleAreaDialog_errorMessage: Property = Property(name="errorMessage", type=StringType)
presentation_TitleAreaDialog_message: Property = Property(name="message", type=StringType)
presentation_TitleAreaDialog_title: Property = Property(name="title", type=StringType)
presentation_TitleAreaDialog_titleImage: Property = Property(name="titleImage", type=StringType)
presentation_TitleAreaDialog_group3: Property = Property(name="group3", type=StringType)
presentation_TitleAreaDialog.attributes={presentation_TitleAreaDialog_group3, presentation_TitleAreaDialog_errorMessage, presentation_TitleAreaDialog_titleImage, presentation_TitleAreaDialog_message, presentation_TitleAreaDialog_title}

# TrayDialog class attributes and methods

# presentation_ToolItem class attributes and methods
presentation_ToolItem_bounds: Property = Property(name="bounds", type=StringType)
presentation_ToolItem_disabledImage: Property = Property(name="disabledImage", type=StringType)
presentation_ToolItem_enabled: Property = Property(name="enabled", type=StringType)
presentation_ToolItem_hotImage: Property = Property(name="hotImage", type=StringType)
presentation_ToolItem_selection: Property = Property(name="selection", type=StringType)
presentation_ToolItem_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_ToolItem_width: Property = Property(name="width", type=StringType)
presentation_ToolItem_group: Property = Property(name="group", type=StringType)
presentation_ToolItem.attributes={presentation_ToolItem_enabled, presentation_ToolItem_width, presentation_ToolItem_selection, presentation_ToolItem_toolTipText, presentation_ToolItem_disabledImage, presentation_ToolItem_group, presentation_ToolItem_hotImage, presentation_ToolItem_bounds}

# presentation_Tray class attributes and methods
presentation_Tray_group: Property = Property(name="group", type=StringType)
presentation_Tray.attributes={presentation_Tray_group}

# presentation_ToolTip class attributes and methods
presentation_ToolTip_group: Property = Property(name="group", type=StringType)
presentation_ToolTip_autoHide: Property = Property(name="autoHide", type=StringType)
presentation_ToolTip_message: Property = Property(name="message", type=StringType)
presentation_ToolTip_text: Property = Property(name="text", type=StringType)
presentation_ToolTip_visible: Property = Property(name="visible", type=StringType)
presentation_ToolTip.attributes={presentation_ToolTip_message, presentation_ToolTip_text, presentation_ToolTip_autoHide, presentation_ToolTip_group, presentation_ToolTip_visible}

# presentation_Tracker class attributes and methods
presentation_Tracker_group: Property = Property(name="group", type=StringType)
presentation_Tracker_rectangles: Property = Property(name="rectangles", type=StringType)
presentation_Tracker_stippled: Property = Property(name="stippled", type=StringType)
presentation_Tracker.attributes={presentation_Tracker_rectangles, presentation_Tracker_stippled, presentation_Tracker_group}

# presentation_Tree class attributes and methods
presentation_Tree_group3: Property = Property(name="group3", type=StringType)
presentation_Tree_columnOrder: Property = Property(name="columnOrder", type=StringType)
presentation_Tree_headerVisible: Property = Property(name="headerVisible", type=StringType)
presentation_Tree_itemCount: Property = Property(name="itemCount", type=StringType)
presentation_Tree_linesVisible: Property = Property(name="linesVisible", type=StringType)
presentation_Tree_sortDirection: Property = Property(name="sortDirection", type=StringType)
presentation_Tree.attributes={presentation_Tree_itemCount, presentation_Tree_group3, presentation_Tree_sortDirection, presentation_Tree_columnOrder, presentation_Tree_linesVisible, presentation_Tree_headerVisible}

# presentation_TrayItem class attributes and methods

# presentation_TrayDialog class attributes and methods
presentation_TrayDialog_helpAvailable: Property = Property(name="helpAvailable", type=StringType)
presentation_TrayDialog_group2: Property = Property(name="group2", type=StringType)
presentation_TrayDialog.attributes={presentation_TrayDialog_helpAvailable, presentation_TrayDialog_group2}

# presentation_TreeColumn class attributes and methods
presentation_TreeColumn_group: Property = Property(name="group", type=StringType)
presentation_TreeColumn_toolTipText: Property = Property(name="toolTipText", type=StringType)
presentation_TreeColumn_width: Property = Property(name="width", type=StringType)
presentation_TreeColumn_alignment: Property = Property(name="alignment", type=StringType)
presentation_TreeColumn_moveable: Property = Property(name="moveable", type=StringType)
presentation_TreeColumn_resizable: Property = Property(name="resizable", type=StringType)
presentation_TreeColumn.attributes={presentation_TreeColumn_alignment, presentation_TreeColumn_group, presentation_TreeColumn_moveable, presentation_TreeColumn_toolTipText, presentation_TreeColumn_width, presentation_TreeColumn_resizable}

# presentation_TreeItem class attributes and methods
presentation_TreeItem_group: Property = Property(name="group", type=StringType)
presentation_TreeItem_checked: Property = Property(name="checked", type=StringType)
presentation_TreeItem_expanded: Property = Property(name="expanded", type=StringType)
presentation_TreeItem_grayed: Property = Property(name="grayed", type=StringType)
presentation_TreeItem_handle: Property = Property(name="handle", type=StringType)
presentation_TreeItem_itemCount: Property = Property(name="itemCount", type=StringType)
presentation_TreeItem_texts: Property = Property(name="texts", type=StringType)
presentation_TreeItem.attributes={presentation_TreeItem_group, presentation_TreeItem_checked, presentation_TreeItem_handle, presentation_TreeItem_itemCount, presentation_TreeItem_texts, presentation_TreeItem_grayed, presentation_TreeItem_expanded}

# presentation_TreeViewer class attributes and methods
presentation_TreeViewer_group5: Property = Property(name="group5", type=StringType)
presentation_TreeViewer.attributes={presentation_TreeViewer_group5}

# presentation_ViewerColumn class attributes and methods
presentation_ViewerColumn_mixed: Property = Property(name="mixed", type=StringType)
presentation_ViewerColumn.attributes={presentation_ViewerColumn_mixed}

# presentation_URL class attributes and methods
presentation_URL_mixed: Property = Property(name="mixed", type=StringType)
presentation_URL.attributes={presentation_URL_mixed}

# presentation_Viewer class attributes and methods
presentation_Viewer_mixed: Property = Property(name="mixed", type=StringType)
presentation_Viewer_group: Property = Property(name="group", type=StringType)
presentation_Viewer.attributes={presentation_Viewer_mixed, presentation_Viewer_group}

# ViewerComparator class attributes and methods

# presentation_WindowManager class attributes and methods
presentation_WindowManager_mixed: Property = Property(name="mixed", type=StringType)
presentation_WindowManager.attributes={presentation_WindowManager_mixed}

# presentation_XMLDataProvider class attributes and methods
presentation_XMLDataProvider_xPath: Property = Property(name="xPath", type=StringType)
presentation_XMLDataProvider_group1: Property = Property(name="group1", type=StringType)
presentation_XMLDataProvider.attributes={presentation_XMLDataProvider_group1, presentation_XMLDataProvider_xPath}

# Relationships
bindingContext0: BinaryAssociation = BinaryAssociation(
    name="bindingContext0",
    ends={
        Property(name="presentation_IBindingContext", type=presentation_AbstractDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AbstractDataProvider", type=presentation_IBindingContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expandedTreePaths1: BinaryAssociation = BinaryAssociation(
    name="expandedTreePaths1",
    ends={
        Property(name="presentation_TreePath", type=presentation_AbstractTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AbstractTreeViewer", type=presentation_TreePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expandedElements2: BinaryAssociation = BinaryAssociation(
    name="expandedElements2",
    ends={
        Property(name="presentation_EObject", type=presentation_AbstractTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AbstractTreeViewer3", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visibleExpandedElements4: BinaryAssociation = BinaryAssociation(
    name="visibleExpandedElements4",
    ends={
        Property(name="presentation_EObject6", type=presentation_AbstractTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_AbstractTreeViewer5", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="presentation_EObject8", type=presentation_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Binding", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="presentation_EObject11", type=presentation_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Binding10", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control12: BinaryAssociation = BinaryAssociation(
    name="control12",
    ends={
        Property(name="presentation_Widget", type=presentation_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Binding13", type=presentation_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
command16: BinaryAssociation = BinaryAssociation(
    name="command16",
    ends={
        Property(name="presentation_ICommand", type=presentation_Button, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Button", type=presentation_ICommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
webBrowser14: BinaryAssociation = BinaryAssociation(
    name="webBrowser14",
    ends={
        Property(name="presentation_EObject15", type=presentation_Browser, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Browser", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="presentation_Canvas22", type=presentation_Caret, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Caret21", type=presentation_Canvas, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iME17: BinaryAssociation = BinaryAssociation(
    name="iME17",
    ends={
        Property(name="presentation_IME", type=presentation_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Canvas", type=presentation_IME, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caret18: BinaryAssociation = BinaryAssociation(
    name="caret18",
    ends={
        Property(name="presentation_Caret", type=presentation_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Canvas19", type=presentation_Caret, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validator24: BinaryAssociation = BinaryAssociation(
    name="validator24",
    ends={
        Property(name="presentation_ICellEditorValidator", type=presentation_CellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CellEditor", type=presentation_ICellEditorValidator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layoutData25: BinaryAssociation = BinaryAssociation(
    name="layoutData25",
    ends={
        Property(name="presentation_LayoutData", type=presentation_CellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CellEditor26", type=presentation_LayoutData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent23: BinaryAssociation = BinaryAssociation(
    name="parent23",
    ends={
        Property(name="presentation_TableItem", type=presentation_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Cell", type=presentation_TableItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grayedElements32: BinaryAssociation = BinaryAssociation(
    name="grayedElements32",
    ends={
        Property(name="presentation_EObject33", type=presentation_CheckboxTableViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTableViewer", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkStateProvider34: BinaryAssociation = BinaryAssociation(
    name="checkStateProvider34",
    ends={
        Property(name="presentation_ICheckStateProvider", type=presentation_CheckboxTableViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTableViewer35", type=presentation_ICheckStateProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkedElements36: BinaryAssociation = BinaryAssociation(
    name="checkedElements36",
    ends={
        Property(name="presentation_EObject38", type=presentation_CheckboxTableViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTableViewer37", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="presentation_EObject29", type=presentation_CellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CellEditor28", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control30: BinaryAssociation = BinaryAssociation(
    name="control30",
    ends={
        Property(name="presentation_Control", type=presentation_CellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CellEditor31", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grayedElements39: BinaryAssociation = BinaryAssociation(
    name="grayedElements39",
    ends={
        Property(name="presentation_EObject40", type=presentation_CheckboxTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTreeViewer", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkStateProvider41: BinaryAssociation = BinaryAssociation(
    name="checkStateProvider41",
    ends={
        Property(name="presentation_ICheckStateProvider43", type=presentation_CheckboxTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTreeViewer42", type=presentation_ICheckStateProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkedElements44: BinaryAssociation = BinaryAssociation(
    name="checkedElements44",
    ends={
        Property(name="presentation_EObject46", type=presentation_CheckboxTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CheckboxTreeViewer45", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnViewerEditor47: BinaryAssociation = BinaryAssociation(
    name="columnViewerEditor47",
    ends={
        Property(name="presentation_ColumnViewerEditor", type=presentation_ColumnViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ColumnViewer", type=presentation_ColumnViewerEditor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cellModifier48: BinaryAssociation = BinaryAssociation(
    name="cellModifier48",
    ends={
        Property(name="presentation_ICellModifier", type=presentation_ColumnViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ColumnViewer49", type=presentation_ICellModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cellEditors50: BinaryAssociation = BinaryAssociation(
    name="cellEditors50",
    ends={
        Property(name="presentation_CellEditor52", type=presentation_ColumnViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ColumnViewer51", type=presentation_CellEditor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnProperties53: BinaryAssociation = BinaryAssociation(
    name="columnProperties53",
    ends={
        Property(name="presentation_EObject55", type=presentation_ColumnViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ColumnViewer54", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input56: BinaryAssociation = BinaryAssociation(
    name="input56",
    ends={
        Property(name="presentation_EObject57", type=presentation_ComboBoxViewerCellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ComboBoxViewerCellEditor", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewer62: BinaryAssociation = BinaryAssociation(
    name="viewer62",
    ends={
        Property(name="presentation_ComboViewer", type=presentation_ComboBoxViewerCellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ComboBoxViewerCellEditor63", type=presentation_ComboViewer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contenProvider58: BinaryAssociation = BinaryAssociation(
    name="contenProvider58",
    ends={
        Property(name="presentation_IStructuredContentProvider", type=presentation_ComboBoxViewerCellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ComboBoxViewerCellEditor59", type=presentation_IStructuredContentProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelProvider60: BinaryAssociation = BinaryAssociation(
    name="labelProvider60",
    ends={
        Property(name="presentation_IBaseLabelProvider", type=presentation_ComboBoxViewerCellEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ComboBoxViewerCellEditor61", type=presentation_IBaseLabelProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout69: BinaryAssociation = BinaryAssociation(
    name="layout69",
    ends={
        Property(name="presentation_Composite70", type=presentation_Layout, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="presentation_Layout", type=presentation_Composite, multiplicity=Multiplicity(1, 1))
    }
)
contentProvider71: BinaryAssociation = BinaryAssociation(
    name="contentProvider71",
    ends={
        Property(name="presentation_IContentProvider", type=presentation_ContentViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ContentViewer", type=presentation_IContentProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tabList64: BinaryAssociation = BinaryAssociation(
    name="tabList64",
    ends={
        Property(name="presentation_Control65", type=presentation_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Composite", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children66: BinaryAssociation = BinaryAssociation(
    name="children66",
    ends={
        Property(name="presentation_Control68", type=presentation_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Composite67", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menu75: BinaryAssociation = BinaryAssociation(
    name="menu75",
    ends={
        Property(name="presentation_Menu", type=presentation_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Control76", type=presentation_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursor77: BinaryAssociation = BinaryAssociation(
    name="cursor77",
    ends={
        Property(name="presentation_Cursor", type=presentation_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Control78", type=presentation_Cursor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layoutData79: BinaryAssociation = BinaryAssociation(
    name="layoutData79",
    ends={
        Property(name="presentation_EObject81", type=presentation_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Control80", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelProvider72: BinaryAssociation = BinaryAssociation(
    name="labelProvider72",
    ends={
        Property(name="presentation_IBaseLabelProvider74", type=presentation_ContentViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ContentViewer73", type=presentation_IBaseLabelProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessible82: BinaryAssociation = BinaryAssociation(
    name="accessible82",
    ends={
        Property(name="presentation_Accessible", type=presentation_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Control83", type=presentation_Accessible, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editor84: BinaryAssociation = BinaryAssociation(
    name="editor84",
    ends={
        Property(name="presentation_Control85", type=presentation_ControlEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ControlEditor", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent87: BinaryAssociation = BinaryAssociation(
    name="parent87",
    ends={
        Property(name="presentation_CoolBar89", type=presentation_CoolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CoolItem88", type=presentation_CoolBar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control90: BinaryAssociation = BinaryAssociation(
    name="control90",
    ends={
        Property(name="presentation_Control92", type=presentation_CoolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CoolItem91", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items86: BinaryAssociation = BinaryAssociation(
    name="items86",
    ends={
        Property(name="presentation_CoolItem", type=presentation_CoolBar, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CoolBar", type=presentation_CoolItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topRight96: BinaryAssociation = BinaryAssociation(
    name="topRight96",
    ends={
        Property(name="presentation_Control98", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabFolder97", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderOutsideRGB99: BinaryAssociation = BinaryAssociation(
    name="borderOutsideRGB99",
    ends={
        Property(name="presentation_RGB101", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabFolder100", type=presentation_RGB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderInsideRGB93: BinaryAssociation = BinaryAssociation(
    name="borderInsideRGB93",
    ends={
        Property(name="presentation_RGB", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabFolder", type=presentation_RGB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items94: BinaryAssociation = BinaryAssociation(
    name="items94",
    ends={
        Property(name="presentation_CTabItem", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabFolder95", type=presentation_CTabItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderMiddleRGB105: BinaryAssociation = BinaryAssociation(
    name="borderMiddleRGB105",
    ends={
        Property(name="presentation_CTabFolder106", type=presentation_RGB, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="presentation_RGB107", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1))
    }
)
selection102: BinaryAssociation = BinaryAssociation(
    name="selection102",
    ends={
        Property(name="presentation_CTabItem104", type=presentation_CTabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabFolder103", type=presentation_CTabItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent108: BinaryAssociation = BinaryAssociation(
    name="parent108",
    ends={
        Property(name="presentation_CTabFolder110", type=presentation_CTabItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabItem109", type=presentation_CTabFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control111: BinaryAssociation = BinaryAssociation(
    name="control111",
    ends={
        Property(name="presentation_Control113", type=presentation_CTabItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_CTabItem112", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menuBar116: BinaryAssociation = BinaryAssociation(
    name="menuBar116",
    ends={
        Property(name="presentation_Menu118", type=presentation_Decorations, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Decorations117", type=presentation_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultButton114: BinaryAssociation = BinaryAssociation(
    name="defaultButton114",
    ends={
        Property(name="presentation_Button115", type=presentation_Decorations, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Decorations", type=presentation_Button, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buttonBar119: BinaryAssociation = BinaryAssociation(
    name="buttonBar119",
    ends={
        Property(name="presentation_Control120", type=presentation_Dialog, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Dialog", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedHandler121: BinaryAssociation = BinaryAssociation(
    name="blockedHandler121",
    ends={
        Property(name="presentation_IDialogBlockedHandler", type=presentation_Dialog, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Dialog122", type=presentation_IDialogBlockedHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap123: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap123",
    ends={
        Property(name="presentation_EStringToStringMapEntry", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot", type=presentation_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composite127: BinaryAssociation = BinaryAssociation(
    name="composite127",
    ends={
        Property(name="presentation_DocumentRoot128", type=presentation_Composite, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="presentation_Composite129", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
dialog130: BinaryAssociation = BinaryAssociation(
    name="dialog130",
    ends={
        Property(name="presentation_Window", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot131", type=presentation_Window, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation124: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation124",
    ends={
        Property(name="presentation_EStringToStringMapEntry126", type=presentation_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_DocumentRoot125", type=presentation_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent133: BinaryAssociation = BinaryAssociation(
    name="parent133",
    ends={
        Property(name="presentation_ExpandBar135", type=presentation_ExpandItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ExpandItem134", type=presentation_ExpandBar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control136: BinaryAssociation = BinaryAssociation(
    name="control136",
    ends={
        Property(name="presentation_Control138", type=presentation_ExpandItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ExpandItem137", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items132: BinaryAssociation = BinaryAssociation(
    name="items132",
    ends={
        Property(name="presentation_ExpandItem", type=presentation_ExpandBar, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ExpandBar", type=presentation_ExpandItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control139: BinaryAssociation = BinaryAssociation(
    name="control139",
    ends={
        Property(name="presentation_Control140", type=presentation_FormAttachment, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_FormAttachment", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottom141: BinaryAssociation = BinaryAssociation(
    name="bottom141",
    ends={
        Property(name="presentation_FormAttachment142", type=presentation_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_FormData", type=presentation_FormAttachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="presentation_FormAttachment145", type=presentation_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_FormData144", type=presentation_FormAttachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="presentation_FormAttachment148", type=presentation_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_FormData147", type=presentation_FormAttachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
top149: BinaryAssociation = BinaryAssociation(
    name="top149",
    ends={
        Property(name="presentation_FormAttachment151", type=presentation_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_FormData150", type=presentation_FormAttachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles152: BinaryAssociation = BinaryAssociation(
    name="styles152",
    ends={
        Property(name="presentation_TextStyle", type=presentation_IME, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_IME153", type=presentation_TextStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list154: BinaryAssociation = BinaryAssociation(
    name="list154",
    ends={
        Property(name="presentation_List", type=presentation_ListViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ListViewer", type=presentation_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultItem155: BinaryAssociation = BinaryAssociation(
    name="defaultItem155",
    ends={
        Property(name="presentation_MenuItem", type=presentation_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Menu156", type=presentation_MenuItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentItem157: BinaryAssociation = BinaryAssociation(
    name="parentItem157",
    ends={
        Property(name="presentation_MenuItem159", type=presentation_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Menu158", type=presentation_MenuItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items160: BinaryAssociation = BinaryAssociation(
    name="items160",
    ends={
        Property(name="presentation_MenuItem162", type=presentation_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Menu161", type=presentation_MenuItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent166: BinaryAssociation = BinaryAssociation(
    name="parent166",
    ends={
        Property(name="presentation_Decorations168", type=presentation_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Menu167", type=presentation_Decorations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentMenu164: BinaryAssociation = BinaryAssociation(
    name="parentMenu164",
    ends={
        Property(name="presentation_Menu165", type=presentation_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Menu163", type=presentation_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent169: BinaryAssociation = BinaryAssociation(
    name="parent169",
    ends={
        Property(name="presentation_MenuItem170", type=presentation_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="presentation_Menu171", type=presentation_MenuItem, multiplicity=Multiplicity(1, 1))
    }
)
command172: BinaryAssociation = BinaryAssociation(
    name="command172",
    ends={
        Property(name="presentation_ICommand174", type=presentation_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_MenuItem173", type=presentation_ICommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menu175: BinaryAssociation = BinaryAssociation(
    name="menu175",
    ends={
        Property(name="presentation_Menu177", type=presentation_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_MenuItem176", type=presentation_Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodParameters182: BinaryAssociation = BinaryAssociation(
    name="methodParameters182",
    ends={
        Property(name="presentation_List184", type=presentation_ObjectDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ObjectDataProvider183", type=presentation_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectType178: BinaryAssociation = BinaryAssociation(
    name="objectType178",
    ends={
        Property(name="presentation_Class", type=presentation_ObjectDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ObjectDataProvider", type=presentation_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectInstance179: BinaryAssociation = BinaryAssociation(
    name="objectInstance179",
    ends={
        Property(name="presentation_EObject181", type=presentation_ObjectDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ObjectDataProvider180", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maximizedControl185: BinaryAssociation = BinaryAssociation(
    name="maximizedControl185",
    ends={
        Property(name="presentation_Control186", type=presentation_SashForm, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_SashForm", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verticalBar188: BinaryAssociation = BinaryAssociation(
    name="verticalBar188",
    ends={
        Property(name="presentation_ScrollBar190", type=presentation_Scrollable, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Scrollable189", type=presentation_ScrollBar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent191: BinaryAssociation = BinaryAssociation(
    name="parent191",
    ends={
        Property(name="presentation_Scrollable193", type=presentation_ScrollBar, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ScrollBar192", type=presentation_Scrollable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
horizontalBar187: BinaryAssociation = BinaryAssociation(
    name="horizontalBar187",
    ends={
        Property(name="presentation_ScrollBar", type=presentation_Scrollable, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Scrollable", type=presentation_ScrollBar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shells195: BinaryAssociation = BinaryAssociation(
    name="shells195",
    ends={
        Property(name="presentation_Shell", type=presentation_Shell, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Shell194", type=presentation_Shell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topControl196: BinaryAssociation = BinaryAssociation(
    name="topControl196",
    ends={
        Property(name="presentation_Control197", type=presentation_StackLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StackLayout", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comparator198: BinaryAssociation = BinaryAssociation(
    name="comparator198",
    ends={
        Property(name="presentation_ViewerComparator", type=presentation_StructuredViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StructuredViewer", type=presentation_ViewerComparator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comparer199: BinaryAssociation = BinaryAssociation(
    name="comparer199",
    ends={
        Property(name="presentation_IElementComparer", type=presentation_StructuredViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StructuredViewer200", type=presentation_IElementComparer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sorter203: BinaryAssociation = BinaryAssociation(
    name="sorter203",
    ends={
        Property(name="presentation_ViewerSorter", type=presentation_StructuredViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StructuredViewer204", type=presentation_ViewerSorter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters201: BinaryAssociation = BinaryAssociation(
    name="filters201",
    ends={
        Property(name="presentation_ViewerFilter", type=presentation_StructuredViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StructuredViewer202", type=presentation_ViewerFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content209: BinaryAssociation = BinaryAssociation(
    name="content209",
    ends={
        Property(name="presentation_StyledTextContent", type=presentation_StyledText, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StyledText210", type=presentation_StyledTextContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleRanges205: BinaryAssociation = BinaryAssociation(
    name="styleRanges205",
    ends={
        Property(name="presentation_StyleRange", type=presentation_StyledText, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StyledText", type=presentation_StyleRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleRange206: BinaryAssociation = BinaryAssociation(
    name="styleRange206",
    ends={
        Property(name="presentation_StyleRange208", type=presentation_StyledText, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_StyledText207", type=presentation_StyleRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items211: BinaryAssociation = BinaryAssociation(
    name="items211",
    ends={
        Property(name="presentation_TabItem", type=presentation_TabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TabFolder", type=presentation_TabItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection212: BinaryAssociation = BinaryAssociation(
    name="selection212",
    ends={
        Property(name="presentation_TabItem214", type=presentation_TabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TabFolder213", type=presentation_TabItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortColumn221: BinaryAssociation = BinaryAssociation(
    name="sortColumn221",
    ends={
        Property(name="presentation_TableColumn", type=presentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Table", type=presentation_TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns222: BinaryAssociation = BinaryAssociation(
    name="columns222",
    ends={
        Property(name="presentation_TableColumn224", type=presentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Table223", type=presentation_TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent215: BinaryAssociation = BinaryAssociation(
    name="parent215",
    ends={
        Property(name="presentation_TabFolder217", type=presentation_TabItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TabItem216", type=presentation_TabFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control218: BinaryAssociation = BinaryAssociation(
    name="control218",
    ends={
        Property(name="presentation_Control220", type=presentation_TabItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TabItem219", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items225: BinaryAssociation = BinaryAssociation(
    name="items225",
    ends={
        Property(name="presentation_TableItem227", type=presentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Table226", type=presentation_TableItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection228: BinaryAssociation = BinaryAssociation(
    name="selection228",
    ends={
        Property(name="presentation_TableItem230", type=presentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Table229", type=presentation_TableItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editor231: BinaryAssociation = BinaryAssociation(
    name="editor231",
    ends={
        Property(name="presentation_Element", type=presentation_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableColumn232", type=presentation_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent233: BinaryAssociation = BinaryAssociation(
    name="parent233",
    ends={
        Property(name="presentation_Table235", type=presentation_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableColumn234", type=presentation_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cells238: BinaryAssociation = BinaryAssociation(
    name="cells238",
    ends={
        Property(name="presentation_Collection", type=presentation_TableItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableItem239", type=presentation_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent240: BinaryAssociation = BinaryAssociation(
    name="parent240",
    ends={
        Property(name="presentation_Table242", type=presentation_TableItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableItem241", type=presentation_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editors243: BinaryAssociation = BinaryAssociation(
    name="editors243",
    ends={
        Property(name="presentation_Collection245", type=presentation_TableItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableItem244", type=presentation_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item236: BinaryAssociation = BinaryAssociation(
    name="item236",
    ends={
        Property(name="presentation_TableItem237", type=presentation_TableEditor, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableEditor", type=presentation_TableItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableTree246: BinaryAssociation = BinaryAssociation(
    name="tableTree246",
    ends={
        Property(name="presentation_TableTree", type=presentation_TableTreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableTreeViewer", type=presentation_TableTree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table247: BinaryAssociation = BinaryAssociation(
    name="table247",
    ends={
        Property(name="presentation_Table248", type=presentation_TableViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableViewer", type=presentation_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column249: BinaryAssociation = BinaryAssociation(
    name="column249",
    ends={
        Property(name="presentation_TableColumn250", type=presentation_TableViewerColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TableViewerColumn", type=presentation_TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
titleAreaColor251: BinaryAssociation = BinaryAssociation(
    name="titleAreaColor251",
    ends={
        Property(name="presentation_RGB252", type=presentation_TitleAreaDialog, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TitleAreaDialog", type=presentation_RGB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items253: BinaryAssociation = BinaryAssociation(
    name="items253",
    ends={
        Property(name="presentation_ToolItem", type=presentation_ToolBar, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ToolBar", type=presentation_ToolItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control254: BinaryAssociation = BinaryAssociation(
    name="control254",
    ends={
        Property(name="presentation_Control256", type=presentation_ToolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ToolItem255", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent257: BinaryAssociation = BinaryAssociation(
    name="parent257",
    ends={
        Property(name="presentation_ToolBar259", type=presentation_ToolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ToolItem258", type=presentation_ToolBar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursor262: BinaryAssociation = BinaryAssociation(
    name="cursor262",
    ends={
        Property(name="presentation_Cursor263", type=presentation_Tracker, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tracker", type=presentation_Cursor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent260: BinaryAssociation = BinaryAssociation(
    name="parent260",
    ends={
        Property(name="presentation_Shell261", type=presentation_ToolTip, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_ToolTip", type=presentation_Shell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items264: BinaryAssociation = BinaryAssociation(
    name="items264",
    ends={
        Property(name="presentation_TrayItem", type=presentation_Tray, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tray", type=presentation_TrayItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tray265: BinaryAssociation = BinaryAssociation(
    name="tray265",
    ends={
        Property(name="presentation_DialogTray", type=presentation_TrayDialog, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TrayDialog", type=presentation_DialogTray, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topItem272: BinaryAssociation = BinaryAssociation(
    name="topItem272",
    ends={
        Property(name="presentation_TreeItem274", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree273", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items275: BinaryAssociation = BinaryAssociation(
    name="items275",
    ends={
        Property(name="presentation_TreeItem277", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree276", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection278: BinaryAssociation = BinaryAssociation(
    name="selection278",
    ends={
        Property(name="presentation_TreeItem280", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree279", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortColumn266: BinaryAssociation = BinaryAssociation(
    name="sortColumn266",
    ends={
        Property(name="presentation_TreeColumn", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree", type=presentation_TreeColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentItem267: BinaryAssociation = BinaryAssociation(
    name="parentItem267",
    ends={
        Property(name="presentation_TreeItem", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree268", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns269: BinaryAssociation = BinaryAssociation(
    name="columns269",
    ends={
        Property(name="presentation_TreeColumn271", type=presentation_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Tree270", type=presentation_TreeColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentItem285: BinaryAssociation = BinaryAssociation(
    name="parentItem285",
    ends={
        Property(name="presentation_TreeItem286", type=presentation_TreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TreeItem284", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent281: BinaryAssociation = BinaryAssociation(
    name="parent281",
    ends={
        Property(name="presentation_Tree283", type=presentation_TreeColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TreeColumn282", type=presentation_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items288: BinaryAssociation = BinaryAssociation(
    name="items288",
    ends={
        Property(name="presentation_TreeItem289", type=presentation_TreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TreeItem287", type=presentation_TreeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent290: BinaryAssociation = BinaryAssociation(
    name="parent290",
    ends={
        Property(name="presentation_Tree292", type=presentation_TreeItem, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TreeItem291", type=presentation_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input295: BinaryAssociation = BinaryAssociation(
    name="input295",
    ends={
        Property(name="presentation_EObject296", type=presentation_Viewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Viewer", type=presentation_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection297: BinaryAssociation = BinaryAssociation(
    name="selection297",
    ends={
        Property(name="presentation_ISelection", type=presentation_Viewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Viewer298", type=presentation_ISelection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control299: BinaryAssociation = BinaryAssociation(
    name="control299",
    ends={
        Property(name="presentation_Control301", type=presentation_Viewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Viewer300", type=presentation_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tree293: BinaryAssociation = BinaryAssociation(
    name="tree293",
    ends={
        Property(name="presentation_Tree294", type=presentation_TreeViewer, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_TreeViewer", type=presentation_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
document304: BinaryAssociation = BinaryAssociation(
    name="document304",
    ends={
        Property(name="presentation_Document", type=presentation_XMLDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_XMLDataProvider", type=presentation_Document, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source305: BinaryAssociation = BinaryAssociation(
    name="source305",
    ends={
        Property(name="presentation_URL", type=presentation_XMLDataProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_XMLDataProvider306", type=presentation_URL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
windowManager302: BinaryAssociation = BinaryAssociation(
    name="windowManager302",
    ends={
        Property(name="presentation_WindowManager", type=presentation_Window, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation_Window303", type=presentation_WindowManager, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_presentation_AbstractComboBoxCellEditor_CellEditor = Generalization(general=CellEditor, specific=presentation_AbstractComboBoxCellEditor)
gen_presentation_AbstractListViewer_StructuredViewer = Generalization(general=StructuredViewer, specific=presentation_AbstractListViewer)
gen_presentation_AbstractTableViewer_ColumnViewer = Generalization(general=ColumnViewer, specific=presentation_AbstractTableViewer)
gen_presentation_AbstractTreeViewer_ColumnViewer = Generalization(general=ColumnViewer, specific=presentation_AbstractTreeViewer)
gen_presentation_Button_Control = Generalization(general=Control, specific=presentation_Button)
gen_presentation_Canvas_Composite = Generalization(general=Composite, specific=presentation_Canvas)
gen_presentation_Browser_Composite = Generalization(general=Composite, specific=presentation_Browser)
gen_presentation_Caret_Widget = Generalization(general=Widget, specific=presentation_Caret)
gen_presentation_CCombo_Composite = Generalization(general=Composite, specific=presentation_CCombo)
gen_presentation_CheckboxCellEditor_CellEditor = Generalization(general=CellEditor, specific=presentation_CheckboxCellEditor)
gen_presentation_CheckboxTableViewer_TableViewer = Generalization(general=TableViewer, specific=presentation_CheckboxTableViewer)
gen_presentation_CheckboxTreeViewer_TreeViewer = Generalization(general=TreeViewer, specific=presentation_CheckboxTreeViewer)
gen_presentation_CLabel_Canvas = Generalization(general=Canvas, specific=presentation_CLabel)
gen_presentation_ColumnViewer_StructuredViewer = Generalization(general=StructuredViewer, specific=presentation_ColumnViewer)
gen_presentation_ColorCellEditor_DialogCellEditor = Generalization(general=DialogCellEditor, specific=presentation_ColorCellEditor)
gen_presentation_Combo_Composite = Generalization(general=Composite, specific=presentation_Combo)
gen_presentation_ComboBoxCellEditor_AbstractComboBoxCellEditor = Generalization(general=AbstractComboBoxCellEditor, specific=presentation_ComboBoxCellEditor)
gen_presentation_ComboBoxViewerCellEditor_AbstractComboBoxCellEditor = Generalization(general=AbstractComboBoxCellEditor, specific=presentation_ComboBoxViewerCellEditor)
gen_presentation_ComboViewer_AbstractListViewer = Generalization(general=AbstractListViewer, specific=presentation_ComboViewer)
gen_presentation_Composite_Scrollable = Generalization(general=Scrollable, specific=presentation_Composite)
gen_presentation_ContentViewer_Viewer = Generalization(general=Viewer, specific=presentation_ContentViewer)
gen_presentation_Control_Widget = Generalization(general=Widget, specific=presentation_Control)
gen_presentation_CoolBar_Composite = Generalization(general=Composite, specific=presentation_CoolBar)
gen_presentation_CoolItem_Item = Generalization(general=Item, specific=presentation_CoolItem)
gen_presentation_CTabFolder_Composite = Generalization(general=Composite, specific=presentation_CTabFolder)
gen_presentation_CTabItem_Item = Generalization(general=Item, specific=presentation_CTabItem)
gen_presentation_DateTime_Composite = Generalization(general=Composite, specific=presentation_DateTime)
gen_presentation_Cursor_Resource = Generalization(general=Resource, specific=presentation_Cursor)
gen_presentation_Decorations_Canvas = Generalization(general=Canvas, specific=presentation_Decorations)
gen_presentation_Dialog_Window = Generalization(general=Window, specific=presentation_Dialog)
gen_presentation_DocumentObject_Observable = Generalization(general=Observable, specific=presentation_DocumentObject)
gen_presentation_DialogCellEditor_CellEditor = Generalization(general=CellEditor, specific=presentation_DialogCellEditor)
gen_presentation_Element_DocumentObject = Generalization(general=DocumentObject, specific=presentation_Element)
gen_presentation_ExpandBar_Composite = Generalization(general=Composite, specific=presentation_ExpandBar)
gen_presentation_ExpandItem_Item = Generalization(general=Item, specific=presentation_ExpandItem)
gen_presentation_FillLayout_Layout = Generalization(general=Layout, specific=presentation_FillLayout)
gen_presentation_FormLayout_Layout = Generalization(general=Layout, specific=presentation_FormLayout)
gen_presentation_GridLayout_Layout = Generalization(general=Layout, specific=presentation_GridLayout)
gen_presentation_Group_Composite = Generalization(general=Composite, specific=presentation_Group)
gen_presentation_IME_Widget = Generalization(general=Widget, specific=presentation_IME)
gen_presentation_Item_Widget = Generalization(general=Widget, specific=presentation_Item)
gen_presentation_Label_Control = Generalization(general=Control, specific=presentation_Label)
gen_presentation_List_Scrollable = Generalization(general=Scrollable, specific=presentation_List)
gen_presentation_Link_Control = Generalization(general=Control, specific=presentation_Link)
gen_presentation_ListViewer_AbstractListViewer = Generalization(general=AbstractListViewer, specific=presentation_ListViewer)
gen_presentation_Menu_Widget = Generalization(general=Widget, specific=presentation_Menu)
gen_presentation_MenuItem_Item = Generalization(general=Item, specific=presentation_MenuItem)
gen_presentation_MessageBox_Dialog = Generalization(general=Dialog, specific=presentation_MessageBox)
gen_presentation_ObjectDataProvider_AbstractDataProvider = Generalization(general=AbstractDataProvider, specific=presentation_ObjectDataProvider)
gen_presentation_ProgressBar_Control = Generalization(general=Control, specific=presentation_ProgressBar)
gen_presentation_RowLayout_Layout = Generalization(general=Layout, specific=presentation_RowLayout)
gen_presentation_Scale_Control = Generalization(general=Control, specific=presentation_Scale)
gen_presentation_Sash_Control = Generalization(general=Control, specific=presentation_Sash)
gen_presentation_SashForm_Composite = Generalization(general=Composite, specific=presentation_SashForm)
gen_presentation_ScrollBar_Widget = Generalization(general=Widget, specific=presentation_ScrollBar)
gen_presentation_Scrollable_Control = Generalization(general=Control, specific=presentation_Scrollable)
gen_presentation_Shell_Decorations = Generalization(general=Decorations, specific=presentation_Shell)
gen_presentation_Slider_Control = Generalization(general=Control, specific=presentation_Slider)
gen_presentation_Spinner_Composite = Generalization(general=Composite, specific=presentation_Spinner)
gen_presentation_StructuredViewer_ContentViewer = Generalization(general=ContentViewer, specific=presentation_StructuredViewer)
gen_presentation_StackLayout_Layout = Generalization(general=Layout, specific=presentation_StackLayout)
gen_presentation_StyledText_Canvas = Generalization(general=Canvas, specific=presentation_StyledText)
gen_presentation_TabFolder_Composite = Generalization(general=Composite, specific=presentation_TabFolder)
gen_presentation_TabItem_Item = Generalization(general=Item, specific=presentation_TabItem)
gen_presentation_StyleRange_TextStyle = Generalization(general=TextStyle, specific=presentation_StyleRange)
gen_presentation_Table_Composite = Generalization(general=Composite, specific=presentation_Table)
gen_presentation_TableColumn_Item = Generalization(general=Item, specific=presentation_TableColumn)
gen_presentation_TableEditor_ControlEditor = Generalization(general=ControlEditor, specific=presentation_TableEditor)
gen_presentation_TableItem_Item = Generalization(general=Item, specific=presentation_TableItem)
gen_presentation_TableViewer_AbstractTableViewer = Generalization(general=AbstractTableViewer, specific=presentation_TableViewer)
gen_presentation_TableTree_Composite = Generalization(general=Composite, specific=presentation_TableTree)
gen_presentation_TableTreeViewer_AbstractTreeViewer = Generalization(general=AbstractTreeViewer, specific=presentation_TableTreeViewer)
gen_presentation_TableViewerColumn_ViewerColumn = Generalization(general=ViewerColumn, specific=presentation_TableViewerColumn)
gen_presentation_Text_Scrollable = Generalization(general=Scrollable, specific=presentation_Text)
gen_presentation_ToolBar_Composite = Generalization(general=Composite, specific=presentation_ToolBar)
gen_presentation_TextCellEditor_CellEditor = Generalization(general=CellEditor, specific=presentation_TextCellEditor)
gen_presentation_TitleAreaDialog_TrayDialog = Generalization(general=TrayDialog, specific=presentation_TitleAreaDialog)
gen_presentation_ToolItem_Item = Generalization(general=Item, specific=presentation_ToolItem)
gen_presentation_Tray_Widget = Generalization(general=Widget, specific=presentation_Tray)
gen_presentation_ToolTip_Widget = Generalization(general=Widget, specific=presentation_ToolTip)
gen_presentation_Tracker_Widget = Generalization(general=Widget, specific=presentation_Tracker)
gen_presentation_TrayItem_Item = Generalization(general=Item, specific=presentation_TrayItem)
gen_presentation_Tree_Composite = Generalization(general=Composite, specific=presentation_Tree)
gen_presentation_TrayDialog_Dialog = Generalization(general=Dialog, specific=presentation_TrayDialog)
gen_presentation_TreeColumn_Item = Generalization(general=Item, specific=presentation_TreeColumn)
gen_presentation_TreeItem_Item = Generalization(general=Item, specific=presentation_TreeItem)
gen_presentation_TreeViewer_AbstractTreeViewer = Generalization(general=AbstractTreeViewer, specific=presentation_TreeViewer)
gen_presentation_ViewerSorter_ViewerComparator = Generalization(general=ViewerComparator, specific=presentation_ViewerSorter)
gen_presentation_XMLDataProvider_AbstractDataProvider = Generalization(general=AbstractDataProvider, specific=presentation_XMLDataProvider)

# Domain Model
domain_model = DomainModel(
    name="presentation",
    types={presentation_AbstractComboBoxCellEditor, CellEditor, presentation_AbstractDataProvider, presentation_AbstractListViewer, StructuredViewer, presentation_AbstractTableViewer, ColumnViewer, presentation_AbstractTreeViewer, presentation_IBindingContext, presentation_TreePath, presentation_EObject, presentation_Widget, presentation_Accessible, presentation_Binding, presentation_Button, Control, presentation_ICommand, presentation_Canvas, presentation_Browser, Composite, Widget, presentation_IME, presentation_Caret, presentation_CCombo, presentation_CellEditor, presentation_ICellEditorValidator, presentation_LayoutData, presentation_Cell, presentation_TableItem, presentation_CheckboxCellEditor, presentation_CheckboxTableViewer, TableViewer, presentation_ICheckStateProvider, presentation_Control, presentation_CheckboxTreeViewer, TreeViewer, presentation_CLabel, Canvas, presentation_Class, presentation_ColumnViewer, presentation_ColumnViewerEditor, presentation_ICellModifier, presentation_Collection, presentation_ColorCellEditor, DialogCellEditor, presentation_Combo, presentation_ComboBoxCellEditor, AbstractComboBoxCellEditor, presentation_ComboBoxViewerCellEditor, presentation_ComboViewer, AbstractListViewer, presentation_Composite, Scrollable, presentation_IStructuredContentProvider, presentation_IBaseLabelProvider, presentation_ContentViewer, Viewer, presentation_IContentProvider, presentation_Layout, presentation_Menu, presentation_Cursor, presentation_ControlEditor, presentation_CoolBar, presentation_CoolItem, Item, presentation_CTabFolder, presentation_RGB, presentation_CTabItem, presentation_DateTime, Resource, presentation_Decorations, presentation_Dialog, Window, presentation_IDialogBlockedHandler, presentation_DefaultCellModifier, presentation_DefaultLabelProvider, presentation_Document, presentation_DocumentObject, Observable, presentation_DocumentRoot, presentation_EStringToStringMapEntry, presentation_DialogCellEditor, presentation_DialogTray, presentation_Window, presentation_Element, DocumentObject, presentation_ExpandBar, presentation_ExpandItem, presentation_FormAttachment, presentation_FillLayout, Layout, presentation_FormData, presentation_FormLayout, presentation_GridData, presentation_GridLayout, presentation_Group, presentation_IElementComparer, presentation_TextStyle, presentation_Item, presentation_ISelection, presentation_Label, presentation_List, presentation_Link, presentation_ListViewer, presentation_Listener, presentation_MenuItem, presentation_MessageBox, Dialog, presentation_ObjectDataProvider, AbstractDataProvider, presentation_Observable, presentation_Resource, presentation_ProgressBar, presentation_RowData, presentation_RowLayout, presentation_Scale, presentation_Sash, presentation_SashForm, presentation_Scrollable, presentation_ScrollBar, presentation_Shell, Decorations, presentation_Slider, presentation_Spinner, presentation_StructuredViewer, ContentViewer, presentation_ViewerComparator, presentation_StackLayout, presentation_ViewerSorter, presentation_StyledText, presentation_ViewerFilter, presentation_StyledTextContent, presentation_StyleRange, presentation_TabFolder, presentation_TabItem, TextStyle, presentation_TableColumn, presentation_Table, presentation_TableEditor, ControlEditor, presentation_TableViewer, AbstractTableViewer, presentation_TableTree, presentation_TableTreeViewer, AbstractTreeViewer, presentation_TableViewerColumn, ViewerColumn, presentation_Text, presentation_ToolBar, presentation_TextCellEditor, presentation_TitleAreaDialog, TrayDialog, presentation_ToolItem, presentation_Tray, presentation_ToolTip, presentation_Tracker, presentation_Tree, presentation_TrayItem, presentation_TrayDialog, presentation_TreeColumn, presentation_TreeItem, presentation_TreeViewer, presentation_ViewerColumn, presentation_URL, presentation_Viewer, ViewerComparator, presentation_WindowManager, presentation_XMLDataProvider},
    associations={bindingContext0, expandedTreePaths1, expandedElements2, visibleExpandedElements4, source7, value9, control12, command16, webBrowser14, parent20, iME17, caret18, validator24, layoutData25, parent23, grayedElements32, checkStateProvider34, checkedElements36, value27, control30, grayedElements39, checkStateProvider41, checkedElements44, columnViewerEditor47, cellModifier48, cellEditors50, columnProperties53, input56, viewer62, contenProvider58, labelProvider60, layout69, contentProvider71, tabList64, children66, menu75, cursor77, layoutData79, labelProvider72, accessible82, editor84, parent87, control90, items86, topRight96, borderOutsideRGB99, borderInsideRGB93, items94, borderMiddleRGB105, selection102, parent108, control111, menuBar116, defaultButton114, buttonBar119, blockedHandler121, xMLNSPrefixMap123, composite127, dialog130, xSISchemaLocation124, parent133, control136, items132, control139, bottom141, right143, left146, top149, styles152, list154, defaultItem155, parentItem157, items160, parent166, parentMenu164, parent169, command172, menu175, methodParameters182, objectType178, objectInstance179, maximizedControl185, verticalBar188, parent191, horizontalBar187, shells195, topControl196, comparator198, comparer199, sorter203, filters201, content209, styleRanges205, styleRange206, items211, selection212, sortColumn221, columns222, parent215, control218, items225, selection228, editor231, parent233, cells238, parent240, editors243, item236, tableTree246, table247, column249, titleAreaColor251, items253, control254, parent257, cursor262, parent260, items264, tray265, topItem272, items275, selection278, sortColumn266, parentItem267, columns269, parentItem285, parent281, items288, parent290, input295, selection297, control299, tree293, document304, source305, windowManager302},
    generalizations={gen_presentation_AbstractComboBoxCellEditor_CellEditor, gen_presentation_AbstractListViewer_StructuredViewer, gen_presentation_AbstractTableViewer_ColumnViewer, gen_presentation_AbstractTreeViewer_ColumnViewer, gen_presentation_Button_Control, gen_presentation_Canvas_Composite, gen_presentation_Browser_Composite, gen_presentation_Caret_Widget, gen_presentation_CCombo_Composite, gen_presentation_CheckboxCellEditor_CellEditor, gen_presentation_CheckboxTableViewer_TableViewer, gen_presentation_CheckboxTreeViewer_TreeViewer, gen_presentation_CLabel_Canvas, gen_presentation_ColumnViewer_StructuredViewer, gen_presentation_ColorCellEditor_DialogCellEditor, gen_presentation_Combo_Composite, gen_presentation_ComboBoxCellEditor_AbstractComboBoxCellEditor, gen_presentation_ComboBoxViewerCellEditor_AbstractComboBoxCellEditor, gen_presentation_ComboViewer_AbstractListViewer, gen_presentation_Composite_Scrollable, gen_presentation_ContentViewer_Viewer, gen_presentation_Control_Widget, gen_presentation_CoolBar_Composite, gen_presentation_CoolItem_Item, gen_presentation_CTabFolder_Composite, gen_presentation_CTabItem_Item, gen_presentation_DateTime_Composite, gen_presentation_Cursor_Resource, gen_presentation_Decorations_Canvas, gen_presentation_Dialog_Window, gen_presentation_DocumentObject_Observable, gen_presentation_DialogCellEditor_CellEditor, gen_presentation_Element_DocumentObject, gen_presentation_ExpandBar_Composite, gen_presentation_ExpandItem_Item, gen_presentation_FillLayout_Layout, gen_presentation_FormLayout_Layout, gen_presentation_GridLayout_Layout, gen_presentation_Group_Composite, gen_presentation_IME_Widget, gen_presentation_Item_Widget, gen_presentation_Label_Control, gen_presentation_List_Scrollable, gen_presentation_Link_Control, gen_presentation_ListViewer_AbstractListViewer, gen_presentation_Menu_Widget, gen_presentation_MenuItem_Item, gen_presentation_MessageBox_Dialog, gen_presentation_ObjectDataProvider_AbstractDataProvider, gen_presentation_ProgressBar_Control, gen_presentation_RowLayout_Layout, gen_presentation_Scale_Control, gen_presentation_Sash_Control, gen_presentation_SashForm_Composite, gen_presentation_ScrollBar_Widget, gen_presentation_Scrollable_Control, gen_presentation_Shell_Decorations, gen_presentation_Slider_Control, gen_presentation_Spinner_Composite, gen_presentation_StructuredViewer_ContentViewer, gen_presentation_StackLayout_Layout, gen_presentation_StyledText_Canvas, gen_presentation_TabFolder_Composite, gen_presentation_TabItem_Item, gen_presentation_StyleRange_TextStyle, gen_presentation_Table_Composite, gen_presentation_TableColumn_Item, gen_presentation_TableEditor_ControlEditor, gen_presentation_TableItem_Item, gen_presentation_TableViewer_AbstractTableViewer, gen_presentation_TableTree_Composite, gen_presentation_TableTreeViewer_AbstractTreeViewer, gen_presentation_TableViewerColumn_ViewerColumn, gen_presentation_Text_Scrollable, gen_presentation_ToolBar_Composite, gen_presentation_TextCellEditor_CellEditor, gen_presentation_TitleAreaDialog_TrayDialog, gen_presentation_ToolItem_Item, gen_presentation_Tray_Widget, gen_presentation_ToolTip_Widget, gen_presentation_Tracker_Widget, gen_presentation_TrayItem_Item, gen_presentation_Tree_Composite, gen_presentation_TrayDialog_Dialog, gen_presentation_TreeColumn_Item, gen_presentation_TreeItem_Item, gen_presentation_TreeViewer_AbstractTreeViewer, gen_presentation_ViewerSorter_ViewerComparator, gen_presentation_XMLDataProvider_AbstractDataProvider},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)