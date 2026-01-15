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

# Enumerations
ProgressState: Enumeration = Enumeration(
    name="ProgressState",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="PAUSED"),
			EnumerationLiteral(name="ERROR")
    }
)

FontStyle: Enumeration = Enumeration(
    name="FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="ITALIC")
    }
)

SystemColors: Enumeration = Enumeration(
    name="SystemColors",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE")
    }
)

BorderStyle: Enumeration = Enumeration(
    name="BorderStyle",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="BORDER")
    }
)

ButtonStyle: Enumeration = Enumeration(
    name="ButtonStyle",
    literals={
            EnumerationLiteral(name="TOGGLE"),
			EnumerationLiteral(name="PUSH"),
			EnumerationLiteral(name="RADIO"),
			EnumerationLiteral(name="CHECK"),
			EnumerationLiteral(name="ARROW")
    }
)

FormAttachmentAlignment: Enumeration = Enumeration(
    name="FormAttachmentAlignment",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="BOTTOM"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="CENTER")
    }
)

MenuStyle: Enumeration = Enumeration(
    name="MenuStyle",
    literals={
            EnumerationLiteral(name="POP_UP"),
			EnumerationLiteral(name="DROP_DOWN")
    }
)

ArrowStyle: Enumeration = Enumeration(
    name="ArrowStyle",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

TextOrientationStyle: Enumeration = Enumeration(
    name="TextOrientationStyle",
    literals={
            EnumerationLiteral(name="LEFT_TO_RIGHT"),
			EnumerationLiteral(name="RIGHT_TO_LEFT")
    }
)

OrientationStyle: Enumeration = Enumeration(
    name="OrientationStyle",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL")
    }
)

HorizontalAlignmentStyle: Enumeration = Enumeration(
    name="HorizontalAlignmentStyle",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="FILL")
    }
)

VerticalAlignmentStyle: Enumeration = Enumeration(
    name="VerticalAlignmentStyle",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="BOTTOM"),
			EnumerationLiteral(name="FILL")
    }
)

MultiplicityStyle: Enumeration = Enumeration(
    name="MultiplicityStyle",
    literals={
            EnumerationLiteral(name="SINGLE"),
			EnumerationLiteral(name="MULTI")
    }
)

ComboStyle: Enumeration = Enumeration(
    name="ComboStyle",
    literals={
            EnumerationLiteral(name="DROP_DOWN"),
			EnumerationLiteral(name="READ_ONLY"),
			EnumerationLiteral(name="SIMPLE")
    }
)

ModalStyle: Enumeration = Enumeration(
    name="ModalStyle",
    literals={
            EnumerationLiteral(name="SYSTEM_MODAL"),
			EnumerationLiteral(name="APPLICATION_MODAL"),
			EnumerationLiteral(name="PRIMARY_MODAL")
    }
)

MenuItemStyle: Enumeration = Enumeration(
    name="MenuItemStyle",
    literals={
            EnumerationLiteral(name="RADIO"),
			EnumerationLiteral(name="SEPARATOR"),
			EnumerationLiteral(name="PUSH"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="CHECK")
    }
)

TrimStyle: Enumeration = Enumeration(
    name="TrimStyle",
    literals={
            EnumerationLiteral(name="NOT_TRIM"),
			EnumerationLiteral(name="SHELL_TRIM"),
			EnumerationLiteral(name="DIALOG_TRIM")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="CUSTOM"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="SOLID")
    }
)

CapStyle: Enumeration = Enumeration(
    name="CapStyle",
    literals={
            EnumerationLiteral(name="FLAT"),
			EnumerationLiteral(name="ROUND"),
			EnumerationLiteral(name="SQUARE")
    }
)

JoinStyle: Enumeration = Enumeration(
    name="JoinStyle",
    literals={
            EnumerationLiteral(name="MITER"),
			EnumerationLiteral(name="ROUND"),
			EnumerationLiteral(name="BEVEL")
    }
)

SortDirection: Enumeration = Enumeration(
    name="SortDirection",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN")
    }
)

# Classes
swt_Widget = Class(name="swt::Widget", is_abstract=True)
swt_LayoutData = Class(name="swt::LayoutData", is_abstract=True)
swt_Control = Class(name="swt::Control", is_abstract=True)
Widget = Class(name="Widget")
swt_Color = Class(name="swt::Color", is_abstract=True)
swt_Font = Class(name="swt::Font")
swt_AbstractComposite = Class(name="swt::AbstractComposite", is_abstract=True)
Control = Class(name="Control")
swt_Layout = Class(name="swt::Layout", is_abstract=True)
swt_Composite = Class(name="swt::Composite")
swt_Group = Class(name="swt::Group")
Composite = Class(name="Composite")
swt_Canvas = Class(name="swt::Canvas")
swt_Decorations = Class(name="swt::Decorations", is_abstract=True)
Canvas = Class(name="Canvas")
swt_MenuBar = Class(name="swt::MenuBar")
swt_Shell = Class(name="swt::Shell")
Decorations = Class(name="Decorations")
swt_Button = Class(name="swt::Button")
swt_AbstractMenu = Class(name="swt::AbstractMenu", is_abstract=True)
swt_MenuItem = Class(name="swt::MenuItem")
swt_Menu = Class(name="swt::Menu")
AbstractMenu = Class(name="AbstractMenu")
swt_Labeled = Class(name="swt::Labeled", is_abstract=True)
swt_Item = Class(name="swt::Item", is_abstract=True)
Labeled = Class(name="Labeled")
Item = Class(name="Item")
swt_ToolBar = Class(name="swt::ToolBar")
swt_ToolItem = Class(name="swt::ToolItem")
swt_CoolBar = Class(name="swt::CoolBar")
swt_CoolItem = Class(name="swt::CoolItem")
swt_Label = Class(name="swt::Label")
swt_Separator = Class(name="swt::Separator")
swt_Text = Class(name="swt::Text")
swt_PasswordText = Class(name="swt::PasswordText")
Text = Class(name="Text")
swt_SearchText = Class(name="swt::SearchText")
swt_IntervalControl = Class(name="swt::IntervalControl", is_abstract=True)
swt_IntervalSelector = Class(name="swt::IntervalSelector", is_abstract=True)
IntervalControl = Class(name="IntervalControl")
swt_Slider = Class(name="swt::Slider")
IntervalSelector = Class(name="IntervalSelector")
swt_Spinner = Class(name="swt::Spinner")
swt_ProgressBar = Class(name="swt::ProgressBar")
swt_Combo = Class(name="swt::Combo")
swt_DateTime = Class(name="swt::DateTime")
swt_TabFolder = Class(name="swt::TabFolder")
swt_Browser = Class(name="swt::Browser")
swt_AbstractList = Class(name="swt::AbstractList", is_abstract=True)
swt_List = Class(name="swt::List")
AbstractList = Class(name="AbstractList")
swt_TabItem = Class(name="swt::TabItem")
swt_FillLayout = Class(name="swt::FillLayout")
swt_SystemColor = Class(name="swt::SystemColor")
Color = Class(name="Color")
swt_RGBColor = Class(name="swt::RGBColor")
swt_RowData = Class(name="swt::RowData")
LayoutData = Class(name="LayoutData")
swt_RowLayout = Class(name="swt::RowLayout")
swt_GridData = Class(name="swt::GridData")
swt_GridLayout = Class(name="swt::GridLayout")
swt_FormLayout = Class(name="swt::FormLayout")
swt_FormData = Class(name="swt::FormData")
swt_FormAttachment = Class(name="swt::FormAttachment")
swt_TreeColumn = Class(name="swt::TreeColumn")
swt_LineAttributes = Class(name="swt::LineAttributes")
swt_Tree = Class(name="swt::Tree")
swt_TreeViewer = Class(name="swt::TreeViewer")
swt_Viewer = Class(name="swt::Viewer", is_abstract=True)

# swt_Widget class attributes and methods
swt_Widget_style: Property = Property(name="style", type=IntegerType)
swt_Widget.attributes={swt_Widget_style}

# swt_LayoutData class attributes and methods

# swt_Control class attributes and methods
swt_Control_borderStyle: Property = Property(name="borderStyle", type=StringType)
swt_Control_textOrientationStyle: Property = Property(name="textOrientationStyle", type=StringType)
swt_Control_enabled: Property = Property(name="enabled", type=BooleanType)
swt_Control_visible: Property = Property(name="visible", type=BooleanType)
swt_Control_touchEnabled: Property = Property(name="touchEnabled", type=BooleanType)
swt_Control_toolTipText: Property = Property(name="toolTipText", type=StringType)
swt_Control_size: Property = Property(name="size", type=StringType)
swt_Control.attributes={swt_Control_toolTipText, swt_Control_borderStyle, swt_Control_touchEnabled, swt_Control_textOrientationStyle, swt_Control_enabled, swt_Control_visible, swt_Control_size}

# Widget class attributes and methods

# swt_Color class attributes and methods

# swt_Font class attributes and methods
swt_Font_name: Property = Property(name="name", type=StringType)
swt_Font_style: Property = Property(name="style", type=IntegerType)
swt_Font_height: Property = Property(name="height", type=IntegerType)
swt_Font.attributes={swt_Font_name, swt_Font_style, swt_Font_height}

# swt_AbstractComposite class attributes and methods

# Control class attributes and methods

# swt_Layout class attributes and methods

# swt_Composite class attributes and methods

# swt_Group class attributes and methods
swt_Group_text: Property = Property(name="text", type=StringType)
swt_Group.attributes={swt_Group_text}

# Composite class attributes and methods

# swt_Canvas class attributes and methods

# swt_Decorations class attributes and methods
swt_Decorations_maximized: Property = Property(name="maximized", type=BooleanType)
swt_Decorations_minimized: Property = Property(name="minimized", type=BooleanType)
swt_Decorations.attributes={swt_Decorations_minimized, swt_Decorations_maximized}

# Canvas class attributes and methods

# swt_MenuBar class attributes and methods

# swt_Shell class attributes and methods
swt_Shell_modalStyle: Property = Property(name="modalStyle", type=StringType)
swt_Shell_trimStyle: Property = Property(name="trimStyle", type=StringType)
swt_Shell_fullScreen: Property = Property(name="fullScreen", type=BooleanType)
swt_Shell_alpha: Property = Property(name="alpha", type=IntegerType)
swt_Shell.attributes={swt_Shell_alpha, swt_Shell_fullScreen, swt_Shell_modalStyle, swt_Shell_trimStyle}

# Decorations class attributes and methods

# swt_Button class attributes and methods
swt_Button_buttonStyle: Property = Property(name="buttonStyle", type=StringType)
swt_Button_arrowStyle: Property = Property(name="arrowStyle", type=StringType)
swt_Button_selection: Property = Property(name="selection", type=BooleanType)
swt_Button.attributes={swt_Button_arrowStyle, swt_Button_selection, swt_Button_buttonStyle}

# swt_AbstractMenu class attributes and methods
swt_AbstractMenu_textOrientationStyle: Property = Property(name="textOrientationStyle", type=StringType)
swt_AbstractMenu_enabled: Property = Property(name="enabled", type=BooleanType)
swt_AbstractMenu_visible: Property = Property(name="visible", type=BooleanType)
swt_AbstractMenu.attributes={swt_AbstractMenu_textOrientationStyle, swt_AbstractMenu_enabled, swt_AbstractMenu_visible}

# swt_MenuItem class attributes and methods
swt_MenuItem_menuItemStyle: Property = Property(name="menuItemStyle", type=StringType)
swt_MenuItem_ID: Property = Property(name="ID", type=IntegerType)
swt_MenuItem_accelerator: Property = Property(name="accelerator", type=IntegerType)
swt_MenuItem_enabled: Property = Property(name="enabled", type=BooleanType)
swt_MenuItem_selection: Property = Property(name="selection", type=BooleanType)
swt_MenuItem.attributes={swt_MenuItem_menuItemStyle, swt_MenuItem_selection, swt_MenuItem_enabled, swt_MenuItem_accelerator, swt_MenuItem_ID}

# swt_Menu class attributes and methods
swt_Menu_menuStyle: Property = Property(name="menuStyle", type=StringType)
swt_Menu.attributes={swt_Menu_menuStyle}

# AbstractMenu class attributes and methods

# swt_Labeled class attributes and methods
swt_Labeled_text: Property = Property(name="text", type=StringType)
swt_Labeled_image: Property = Property(name="image", type=StringType)
swt_Labeled.attributes={swt_Labeled_text, swt_Labeled_image}

# swt_Item class attributes and methods

# Labeled class attributes and methods

# Item class attributes and methods

# swt_ToolBar class attributes and methods
swt_ToolBar_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_ToolBar.attributes={swt_ToolBar_orientationStyle}

# swt_ToolItem class attributes and methods
swt_ToolItem_enabled: Property = Property(name="enabled", type=BooleanType)
swt_ToolItem_hotImage: Property = Property(name="hotImage", type=StringType)
swt_ToolItem_toolTipText: Property = Property(name="toolTipText", type=StringType)
swt_ToolItem_selection: Property = Property(name="selection", type=BooleanType)
swt_ToolItem.attributes={swt_ToolItem_toolTipText, swt_ToolItem_hotImage, swt_ToolItem_enabled, swt_ToolItem_selection}

# swt_CoolBar class attributes and methods
swt_CoolBar_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_CoolBar.attributes={swt_CoolBar_orientationStyle}

# swt_CoolItem class attributes and methods
swt_CoolItem_minimumSize: Property = Property(name="minimumSize", type=StringType)
swt_CoolItem_preferredSize: Property = Property(name="preferredSize", type=StringType)
swt_CoolItem_size: Property = Property(name="size", type=StringType)
swt_CoolItem.attributes={swt_CoolItem_size, swt_CoolItem_preferredSize, swt_CoolItem_minimumSize}

# swt_Label class attributes and methods

# swt_Separator class attributes and methods
swt_Separator_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_Separator.attributes={swt_Separator_orientationStyle}

# swt_Text class attributes and methods
swt_Text_multiplicityStyle: Property = Property(name="multiplicityStyle", type=StringType)
swt_Text_text: Property = Property(name="text", type=StringType)
swt_Text_selection: Property = Property(name="selection", type=StringType)
swt_Text_editable: Property = Property(name="editable", type=BooleanType)
swt_Text_echoChar: Property = Property(name="echoChar", type=StringType)
swt_Text_tabs: Property = Property(name="tabs", type=IntegerType)
swt_Text_textLimit: Property = Property(name="textLimit", type=IntegerType)
swt_Text_topIndex: Property = Property(name="topIndex", type=IntegerType)
swt_Text_message: Property = Property(name="message", type=StringType)
swt_Text.attributes={swt_Text_message, swt_Text_tabs, swt_Text_multiplicityStyle, swt_Text_textLimit, swt_Text_topIndex, swt_Text_selection, swt_Text_text, swt_Text_editable, swt_Text_echoChar}

# swt_PasswordText class attributes and methods

# Text class attributes and methods

# swt_SearchText class attributes and methods

# swt_IntervalControl class attributes and methods
swt_IntervalControl_minimum: Property = Property(name="minimum", type=IntegerType)
swt_IntervalControl_maximum: Property = Property(name="maximum", type=IntegerType)
swt_IntervalControl_selection: Property = Property(name="selection", type=IntegerType)
swt_IntervalControl.attributes={swt_IntervalControl_maximum, swt_IntervalControl_minimum, swt_IntervalControl_selection}

# swt_IntervalSelector class attributes and methods
swt_IntervalSelector_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_IntervalSelector_increment: Property = Property(name="increment", type=IntegerType)
swt_IntervalSelector_pageIncrement: Property = Property(name="pageIncrement", type=IntegerType)
swt_IntervalSelector.attributes={swt_IntervalSelector_increment, swt_IntervalSelector_pageIncrement, swt_IntervalSelector_orientationStyle}

# IntervalControl class attributes and methods

# swt_Slider class attributes and methods
swt_Slider_thumb: Property = Property(name="thumb", type=IntegerType)
swt_Slider.attributes={swt_Slider_thumb}

# IntervalSelector class attributes and methods

# swt_Spinner class attributes and methods
swt_Spinner_digits: Property = Property(name="digits", type=IntegerType)
swt_Spinner_textLimit: Property = Property(name="textLimit", type=IntegerType)
swt_Spinner.attributes={swt_Spinner_textLimit, swt_Spinner_digits}

# swt_ProgressBar class attributes and methods
swt_ProgressBar_state: Property = Property(name="state", type=StringType)
swt_ProgressBar.attributes={swt_ProgressBar_state}

# swt_Combo class attributes and methods
swt_Combo_text: Property = Property(name="text", type=StringType)
swt_Combo_textLimit: Property = Property(name="textLimit", type=IntegerType)
swt_Combo.attributes={swt_Combo_textLimit, swt_Combo_text}

# swt_DateTime class attributes and methods
swt_DateTime_seconds: Property = Property(name="seconds", type=IntegerType)
swt_DateTime_minutes: Property = Property(name="minutes", type=IntegerType)
swt_DateTime_hours: Property = Property(name="hours", type=IntegerType)
swt_DateTime_day: Property = Property(name="day", type=IntegerType)
swt_DateTime_month: Property = Property(name="month", type=IntegerType)
swt_DateTime_year: Property = Property(name="year", type=IntegerType)
swt_DateTime.attributes={swt_DateTime_hours, swt_DateTime_minutes, swt_DateTime_month, swt_DateTime_year, swt_DateTime_seconds, swt_DateTime_day}

# swt_TabFolder class attributes and methods

# swt_Browser class attributes and methods
swt_Browser_javascriptEnabled: Property = Property(name="javascriptEnabled", type=BooleanType)
swt_Browser_text: Property = Property(name="text", type=StringType)
swt_Browser_url: Property = Property(name="url", type=StringType)
swt_Browser.attributes={swt_Browser_javascriptEnabled, swt_Browser_url, swt_Browser_text}

# swt_AbstractList class attributes and methods
swt_AbstractList_items: Property = Property(name="items", type=StringType)
swt_AbstractList_selectionIndex: Property = Property(name="selectionIndex", type=IntegerType)
swt_AbstractList.attributes={swt_AbstractList_selectionIndex, swt_AbstractList_items}

# swt_List class attributes and methods
swt_List_selectionIndices: Property = Property(name="selectionIndices", type=IntegerType)
swt_List_selection: Property = Property(name="selection", type=StringType)
swt_List_multiplicityStyle: Property = Property(name="multiplicityStyle", type=StringType)
swt_List.attributes={swt_List_selection, swt_List_multiplicityStyle, swt_List_selectionIndices}

# AbstractList class attributes and methods

# swt_TabItem class attributes and methods
swt_TabItem_toolTipText: Property = Property(name="toolTipText", type=StringType)
swt_TabItem.attributes={swt_TabItem_toolTipText}

# swt_FillLayout class attributes and methods
swt_FillLayout_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_FillLayout_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
swt_FillLayout_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
swt_FillLayout_spacing: Property = Property(name="spacing", type=IntegerType)
swt_FillLayout.attributes={swt_FillLayout_marginWidth, swt_FillLayout_marginHeight, swt_FillLayout_orientationStyle, swt_FillLayout_spacing}

# swt_SystemColor class attributes and methods
swt_SystemColor_color: Property = Property(name="color", type=StringType)
swt_SystemColor.attributes={swt_SystemColor_color}

# Color class attributes and methods

# swt_RGBColor class attributes and methods
swt_RGBColor_blue: Property = Property(name="blue", type=IntegerType)
swt_RGBColor_red: Property = Property(name="red", type=IntegerType)
swt_RGBColor_green: Property = Property(name="green", type=IntegerType)
swt_RGBColor.attributes={swt_RGBColor_green, swt_RGBColor_blue, swt_RGBColor_red}

# swt_RowData class attributes and methods
swt_RowData_width: Property = Property(name="width", type=IntegerType)
swt_RowData_height: Property = Property(name="height", type=IntegerType)
swt_RowData_exclude: Property = Property(name="exclude", type=BooleanType)
swt_RowData.attributes={swt_RowData_width, swt_RowData_height, swt_RowData_exclude}

# LayoutData class attributes and methods

# swt_RowLayout class attributes and methods
swt_RowLayout_justify: Property = Property(name="justify", type=BooleanType)
swt_RowLayout_marginLeft: Property = Property(name="marginLeft", type=IntegerType)
swt_RowLayout_marginTop: Property = Property(name="marginTop", type=IntegerType)
swt_RowLayout_marginRight: Property = Property(name="marginRight", type=IntegerType)
swt_RowLayout_marginBottom: Property = Property(name="marginBottom", type=IntegerType)
swt_RowLayout_orientationStyle: Property = Property(name="orientationStyle", type=StringType)
swt_RowLayout_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
swt_RowLayout_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
swt_RowLayout_spacing: Property = Property(name="spacing", type=IntegerType)
swt_RowLayout_wrap: Property = Property(name="wrap", type=BooleanType)
swt_RowLayout_pack: Property = Property(name="pack", type=BooleanType)
swt_RowLayout_fill: Property = Property(name="fill", type=BooleanType)
swt_RowLayout_center: Property = Property(name="center", type=BooleanType)
swt_RowLayout.attributes={swt_RowLayout_marginRight, swt_RowLayout_orientationStyle, swt_RowLayout_marginWidth, swt_RowLayout_marginBottom, swt_RowLayout_marginLeft, swt_RowLayout_center, swt_RowLayout_marginTop, swt_RowLayout_pack, swt_RowLayout_justify, swt_RowLayout_spacing, swt_RowLayout_marginHeight, swt_RowLayout_wrap, swt_RowLayout_fill}

# swt_GridData class attributes and methods
swt_GridData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
swt_GridData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
swt_GridData_widthHint: Property = Property(name="widthHint", type=IntegerType)
swt_GridData_heightHint: Property = Property(name="heightHint", type=IntegerType)
swt_GridData_horizontalIndent: Property = Property(name="horizontalIndent", type=IntegerType)
swt_GridData_verticalIndent: Property = Property(name="verticalIndent", type=IntegerType)
swt_GridData_horizontalSpan: Property = Property(name="horizontalSpan", type=IntegerType)
swt_GridData_verticalSpan: Property = Property(name="verticalSpan", type=IntegerType)
swt_GridData_grabExcessHorizontalSpace: Property = Property(name="grabExcessHorizontalSpace", type=BooleanType)
swt_GridData_grabExcessVerticalSpace: Property = Property(name="grabExcessVerticalSpace", type=BooleanType)
swt_GridData_minimumWidth: Property = Property(name="minimumWidth", type=IntegerType)
swt_GridData_minimumHeight: Property = Property(name="minimumHeight", type=IntegerType)
swt_GridData_exclude: Property = Property(name="exclude", type=BooleanType)
swt_GridData.attributes={swt_GridData_exclude, swt_GridData_minimumWidth, swt_GridData_verticalAlignment, swt_GridData_heightHint, swt_GridData_widthHint, swt_GridData_grabExcessHorizontalSpace, swt_GridData_horizontalSpan, swt_GridData_horizontalIndent, swt_GridData_grabExcessVerticalSpace, swt_GridData_verticalSpan, swt_GridData_minimumHeight, swt_GridData_horizontalAlignment, swt_GridData_verticalIndent}

# swt_GridLayout class attributes and methods
swt_GridLayout_numColumns: Property = Property(name="numColumns", type=IntegerType)
swt_GridLayout_makeColumnsEqualWidth: Property = Property(name="makeColumnsEqualWidth", type=BooleanType)
swt_GridLayout_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
swt_GridLayout_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
swt_GridLayout_marginLeft: Property = Property(name="marginLeft", type=IntegerType)
swt_GridLayout_marginTop: Property = Property(name="marginTop", type=IntegerType)
swt_GridLayout_marginRight: Property = Property(name="marginRight", type=IntegerType)
swt_GridLayout_marginBottom: Property = Property(name="marginBottom", type=IntegerType)
swt_GridLayout_horizontalSpacing: Property = Property(name="horizontalSpacing", type=IntegerType)
swt_GridLayout_verticalSpacing: Property = Property(name="verticalSpacing", type=IntegerType)
swt_GridLayout.attributes={swt_GridLayout_marginHeight, swt_GridLayout_makeColumnsEqualWidth, swt_GridLayout_marginLeft, swt_GridLayout_marginRight, swt_GridLayout_marginWidth, swt_GridLayout_numColumns, swt_GridLayout_verticalSpacing, swt_GridLayout_marginBottom, swt_GridLayout_horizontalSpacing, swt_GridLayout_marginTop}

# swt_FormLayout class attributes and methods
swt_FormLayout_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
swt_FormLayout_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
swt_FormLayout_spacing: Property = Property(name="spacing", type=IntegerType)
swt_FormLayout_marginLeft: Property = Property(name="marginLeft", type=IntegerType)
swt_FormLayout_marginTop: Property = Property(name="marginTop", type=IntegerType)
swt_FormLayout_marginRight: Property = Property(name="marginRight", type=IntegerType)
swt_FormLayout_marginBottom: Property = Property(name="marginBottom", type=IntegerType)
swt_FormLayout.attributes={swt_FormLayout_marginRight, swt_FormLayout_marginWidth, swt_FormLayout_marginTop, swt_FormLayout_marginBottom, swt_FormLayout_marginHeight, swt_FormLayout_marginLeft, swt_FormLayout_spacing}

# swt_FormData class attributes and methods
swt_FormData_width: Property = Property(name="width", type=IntegerType)
swt_FormData_height: Property = Property(name="height", type=IntegerType)
swt_FormData.attributes={swt_FormData_height, swt_FormData_width}

# swt_FormAttachment class attributes and methods
swt_FormAttachment_alignment: Property = Property(name="alignment", type=StringType)
swt_FormAttachment_denominator: Property = Property(name="denominator", type=IntegerType)
swt_FormAttachment_numerator: Property = Property(name="numerator", type=IntegerType)
swt_FormAttachment_offset: Property = Property(name="offset", type=IntegerType)
swt_FormAttachment.attributes={swt_FormAttachment_numerator, swt_FormAttachment_offset, swt_FormAttachment_denominator, swt_FormAttachment_alignment}

# swt_TreeColumn class attributes and methods
swt_TreeColumn_toolTipText: Property = Property(name="toolTipText", type=StringType)
swt_TreeColumn_displayText: Property = Property(name="displayText", type=StringType)
swt_TreeColumn.attributes={swt_TreeColumn_toolTipText, swt_TreeColumn_displayText}

# swt_LineAttributes class attributes and methods
swt_LineAttributes_width: Property = Property(name="width", type=FloatType)
swt_LineAttributes_style: Property = Property(name="style", type=StringType)
swt_LineAttributes_cap: Property = Property(name="cap", type=StringType)
swt_LineAttributes_join: Property = Property(name="join", type=StringType)
swt_LineAttributes_dash: Property = Property(name="dash", type=FloatType)
swt_LineAttributes_dashOffset: Property = Property(name="dashOffset", type=FloatType)
swt_LineAttributes_miterLimit: Property = Property(name="miterLimit", type=FloatType)
swt_LineAttributes.attributes={swt_LineAttributes_miterLimit, swt_LineAttributes_style, swt_LineAttributes_cap, swt_LineAttributes_dash, swt_LineAttributes_width, swt_LineAttributes_dashOffset, swt_LineAttributes_join}

# swt_Tree class attributes and methods
swt_Tree_headerVisible: Property = Property(name="headerVisible", type=BooleanType)
swt_Tree_linesVisible: Property = Property(name="linesVisible", type=BooleanType)
swt_Tree_sortDirection: Property = Property(name="sortDirection", type=StringType)
swt_Tree.attributes={swt_Tree_headerVisible, swt_Tree_sortDirection, swt_Tree_linesVisible}

# swt_TreeViewer class attributes and methods

# swt_Viewer class attributes and methods
swt_Viewer_input: Property = Property(name="input", type=StringType)
swt_Viewer.attributes={swt_Viewer_input}

# Relationships
layoutData0: BinaryAssociation = BinaryAssociation(
    name="layoutData0",
    ends={
        Property(name="swt_LayoutData", type=swt_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Control", type=swt_LayoutData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
background1: BinaryAssociation = BinaryAssociation(
    name="background1",
    ends={
        Property(name="swt_Color", type=swt_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Control2", type=swt_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font3: BinaryAssociation = BinaryAssociation(
    name="font3",
    ends={
        Property(name="swt_Font", type=swt_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Control4", type=swt_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
menuBar5: BinaryAssociation = BinaryAssociation(
    name="menuBar5",
    ends={
        Property(name="MenuBar", type=swt_Decorations, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=swt_MenuBar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultButton6: BinaryAssociation = BinaryAssociation(
    name="defaultButton6",
    ends={
        Property(name="swt_Button", type=swt_Shell, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Shell", type=swt_Button, multiplicity=Multiplicity(0, 1))
    }
)
items7: BinaryAssociation = BinaryAssociation(
    name="items7",
    ends={
        Property(name="swt_MenuItem", type=swt_AbstractMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_AbstractMenu", type=swt_MenuItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentItem8: BinaryAssociation = BinaryAssociation(
    name="parentItem8",
    ends={
        Property(name="MenuItem", type=swt_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu", type=swt_MenuItem, multiplicity=Multiplicity(0, 1))
    }
)
parent9: BinaryAssociation = BinaryAssociation(
    name="parent9",
    ends={
        Property(name="Decorations", type=swt_MenuBar, multiplicity=Multiplicity(1, 1)),
        Property(name="menuBar", type=swt_Decorations, multiplicity=Multiplicity(0, 1))
    }
)
menu10: BinaryAssociation = BinaryAssociation(
    name="menu10",
    ends={
        Property(name="Menu", type=swt_MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="parentItem", type=swt_Menu, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items11: BinaryAssociation = BinaryAssociation(
    name="items11",
    ends={
        Property(name="ToolItem", type=swt_ToolBar, multiplicity=Multiplicity(1, 1)),
        Property(name="parent12", type=swt_ToolItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent13: BinaryAssociation = BinaryAssociation(
    name="parent13",
    ends={
        Property(name="ToolBar", type=swt_ToolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=swt_ToolBar, multiplicity=Multiplicity(0, 1))
    }
)
items14: BinaryAssociation = BinaryAssociation(
    name="items14",
    ends={
        Property(name="CoolItem", type=swt_CoolBar, multiplicity=Multiplicity(1, 1)),
        Property(name="parent15", type=swt_CoolItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent16: BinaryAssociation = BinaryAssociation(
    name="parent16",
    ends={
        Property(name="CoolBar", type=swt_CoolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="items17", type=swt_CoolBar, multiplicity=Multiplicity(0, 1))
    }
)
control18: BinaryAssociation = BinaryAssociation(
    name="control18",
    ends={
        Property(name="swt_Control19", type=swt_CoolItem, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_CoolItem", type=swt_Control, multiplicity=Multiplicity(0, 1))
    }
)
items20: BinaryAssociation = BinaryAssociation(
    name="items20",
    ends={
        Property(name="swt_TabItem", type=swt_TabFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_TabFolder", type=swt_TabItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
control21: BinaryAssociation = BinaryAssociation(
    name="control21",
    ends={
        Property(name="swt_Control23", type=swt_TabItem, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_TabItem22", type=swt_Control, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left24: BinaryAssociation = BinaryAssociation(
    name="left24",
    ends={
        Property(name="swt_FormAttachment", type=swt_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_FormData", type=swt_FormAttachment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
top25: BinaryAssociation = BinaryAssociation(
    name="top25",
    ends={
        Property(name="swt_FormAttachment27", type=swt_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_FormData26", type=swt_FormAttachment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="swt_FormAttachment30", type=swt_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_FormData29", type=swt_FormAttachment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottom31: BinaryAssociation = BinaryAssociation(
    name="bottom31",
    ends={
        Property(name="swt_FormAttachment33", type=swt_FormData, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_FormData32", type=swt_FormAttachment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
control34: BinaryAssociation = BinaryAssociation(
    name="control34",
    ends={
        Property(name="swt_Control36", type=swt_FormAttachment, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_FormAttachment35", type=swt_Control, multiplicity=Multiplicity(0, 1))
    }
)
columns37: BinaryAssociation = BinaryAssociation(
    name="columns37",
    ends={
        Property(name="swt_TreeColumn", type=swt_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Tree", type=swt_TreeColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortColumn38: BinaryAssociation = BinaryAssociation(
    name="sortColumn38",
    ends={
        Property(name="swt_TreeColumn40", type=swt_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Tree39", type=swt_TreeColumn, multiplicity=Multiplicity(0, 1))
    }
)
viewer41: BinaryAssociation = BinaryAssociation(
    name="viewer41",
    ends={
        Property(name="swt_TreeViewer", type=swt_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="swt_Tree42", type=swt_TreeViewer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_swt_Control_Widget = Generalization(general=Widget, specific=swt_Control)
gen_swt_AbstractComposite_Control = Generalization(general=Control, specific=swt_AbstractComposite)
gen_swt_Group_Composite = Generalization(general=Composite, specific=swt_Group)
gen_swt_Canvas_Composite = Generalization(general=Composite, specific=swt_Canvas)
gen_swt_Decorations_Canvas = Generalization(general=Canvas, specific=swt_Decorations)
gen_swt_Shell_Decorations = Generalization(general=Decorations, specific=swt_Shell)
gen_swt_MenuItem_Item = Generalization(general=Item, specific=swt_MenuItem)
gen_swt_AbstractMenu_Widget = Generalization(general=Widget, specific=swt_AbstractMenu)
gen_swt_Menu_AbstractMenu = Generalization(general=AbstractMenu, specific=swt_Menu)
gen_swt_MenuBar_AbstractMenu = Generalization(general=AbstractMenu, specific=swt_MenuBar)
gen_swt_Item_Widget = Generalization(general=Widget, specific=swt_Item)
gen_swt_Item_Labeled = Generalization(general=Labeled, specific=swt_Item)
gen_swt_ToolBar_Control = Generalization(general=Control, specific=swt_ToolBar)
gen_swt_ToolItem_Item = Generalization(general=Item, specific=swt_ToolItem)
gen_swt_CoolItem_Item = Generalization(general=Item, specific=swt_CoolItem)
gen_swt_Label_Control = Generalization(general=Control, specific=swt_Label)
gen_swt_Label_Labeled = Generalization(general=Labeled, specific=swt_Label)
gen_swt_Separator_Control = Generalization(general=Control, specific=swt_Separator)
gen_swt_Button_Control = Generalization(general=Control, specific=swt_Button)
gen_swt_Button_Labeled = Generalization(general=Labeled, specific=swt_Button)
gen_swt_Text_Control = Generalization(general=Control, specific=swt_Text)
gen_swt_PasswordText_Text = Generalization(general=Text, specific=swt_PasswordText)
gen_swt_SearchText_Text = Generalization(general=Text, specific=swt_SearchText)
gen_swt_IntervalControl_Control = Generalization(general=Control, specific=swt_IntervalControl)
gen_swt_IntervalSelector_IntervalControl = Generalization(general=IntervalControl, specific=swt_IntervalSelector)
gen_swt_Slider_IntervalSelector = Generalization(general=IntervalSelector, specific=swt_Slider)
gen_swt_Spinner_IntervalSelector = Generalization(general=IntervalSelector, specific=swt_Spinner)
gen_swt_ProgressBar_IntervalControl = Generalization(general=IntervalControl, specific=swt_ProgressBar)
gen_swt_Combo_AbstractList = Generalization(general=AbstractList, specific=swt_Combo)
gen_swt_DateTime_Control = Generalization(general=Control, specific=swt_DateTime)
gen_swt_TabFolder_Control = Generalization(general=Control, specific=swt_TabFolder)
gen_swt_Browser_Control = Generalization(general=Control, specific=swt_Browser)
gen_swt_AbstractList_Control = Generalization(general=Control, specific=swt_AbstractList)
gen_swt_List_AbstractList = Generalization(general=AbstractList, specific=swt_List)
gen_swt_TabItem_Item = Generalization(general=Item, specific=swt_TabItem)
gen_swt_SystemColor_Color = Generalization(general=Color, specific=swt_SystemColor)
gen_swt_RGBColor_Color = Generalization(general=Color, specific=swt_RGBColor)
gen_swt_RowData_LayoutData = Generalization(general=LayoutData, specific=swt_RowData)
gen_swt_GridData_LayoutData = Generalization(general=LayoutData, specific=swt_GridData)
gen_swt_FormData_LayoutData = Generalization(general=LayoutData, specific=swt_FormData)
gen_swt_TreeColumn_Item = Generalization(general=Item, specific=swt_TreeColumn)
gen_swt_Tree_Control = Generalization(general=Control, specific=swt_Tree)

# Domain Model
domain_model = DomainModel(
    name="swt",
    types={swt_Widget, swt_LayoutData, swt_Control, Widget, swt_Color, swt_Font, swt_AbstractComposite, Control, swt_Layout, swt_Composite, swt_Group, Composite, swt_Canvas, swt_Decorations, Canvas, swt_MenuBar, swt_Shell, Decorations, swt_Button, swt_AbstractMenu, swt_MenuItem, swt_Menu, AbstractMenu, swt_Labeled, swt_Item, Labeled, Item, swt_ToolBar, swt_ToolItem, swt_CoolBar, swt_CoolItem, swt_Label, swt_Separator, swt_Text, swt_PasswordText, Text, swt_SearchText, swt_IntervalControl, swt_IntervalSelector, IntervalControl, swt_Slider, IntervalSelector, swt_Spinner, swt_ProgressBar, swt_Combo, swt_DateTime, swt_TabFolder, swt_Browser, swt_AbstractList, swt_List, AbstractList, swt_TabItem, swt_FillLayout, swt_SystemColor, Color, swt_RGBColor, swt_RowData, LayoutData, swt_RowLayout, swt_GridData, swt_GridLayout, swt_FormLayout, swt_FormData, swt_FormAttachment, swt_TreeColumn, swt_LineAttributes, swt_Tree, swt_TreeViewer, swt_Viewer, ProgressState, FontStyle, SystemColors, BorderStyle, ButtonStyle, FormAttachmentAlignment, MenuStyle, ArrowStyle, TextOrientationStyle, OrientationStyle, HorizontalAlignmentStyle, VerticalAlignmentStyle, MultiplicityStyle, ComboStyle, ModalStyle, MenuItemStyle, TrimStyle, LineStyle, CapStyle, JoinStyle, SortDirection},
    associations={layoutData0, background1, font3, menuBar5, defaultButton6, items7, parentItem8, parent9, menu10, items11, parent13, items14, parent16, control18, items20, control21, left24, top25, right28, bottom31, control34, columns37, sortColumn38, viewer41},
    generalizations={gen_swt_Control_Widget, gen_swt_AbstractComposite_Control, gen_swt_Group_Composite, gen_swt_Canvas_Composite, gen_swt_Decorations_Canvas, gen_swt_Shell_Decorations, gen_swt_MenuItem_Item, gen_swt_AbstractMenu_Widget, gen_swt_Menu_AbstractMenu, gen_swt_MenuBar_AbstractMenu, gen_swt_Item_Widget, gen_swt_Item_Labeled, gen_swt_ToolBar_Control, gen_swt_ToolItem_Item, gen_swt_CoolItem_Item, gen_swt_Label_Control, gen_swt_Label_Labeled, gen_swt_Separator_Control, gen_swt_Button_Control, gen_swt_Button_Labeled, gen_swt_Text_Control, gen_swt_PasswordText_Text, gen_swt_SearchText_Text, gen_swt_IntervalControl_Control, gen_swt_IntervalSelector_IntervalControl, gen_swt_Slider_IntervalSelector, gen_swt_Spinner_IntervalSelector, gen_swt_ProgressBar_IntervalControl, gen_swt_Combo_AbstractList, gen_swt_DateTime_Control, gen_swt_TabFolder_Control, gen_swt_Browser_Control, gen_swt_AbstractList_Control, gen_swt_List_AbstractList, gen_swt_TabItem_Item, gen_swt_SystemColor_Color, gen_swt_RGBColor_Color, gen_swt_RowData_LayoutData, gen_swt_GridData_LayoutData, gen_swt_FormData_LayoutData, gen_swt_TreeColumn_Item, gen_swt_Tree_Control},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)