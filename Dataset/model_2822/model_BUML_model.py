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
TextAlignment: Enumeration = Enumeration(
    name="TextAlignment",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Center"),
			EnumerationLiteral(name="Right")
    }
)

IconSize: Enumeration = Enumeration(
    name="IconSize",
    literals={
            EnumerationLiteral(name="Small"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Large"),
			EnumerationLiteral(name="XLarge"),
			EnumerationLiteral(name="XXL"),
			EnumerationLiteral(name="Custom")
    }
)

ResizeMode: Enumeration = Enumeration(
    name="ResizeMode",
    literals={
            EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="Horizontal"),
			EnumerationLiteral(name="Vertical"),
			EnumerationLiteral(name="None")
    }
)

State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Disabled"),
			EnumerationLiteral(name="Selected"),
			EnumerationLiteral(name="Focused")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="Top"),
			EnumerationLiteral(name="Bottom"),
			EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right"),
			EnumerationLiteral(name="TopLeft"),
			EnumerationLiteral(name="TopRight"),
			EnumerationLiteral(name="BottomLeft"),
			EnumerationLiteral(name="BottomRight")
    }
)

BorderStyle: Enumeration = Enumeration(
    name="BorderStyle",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Solid"),
			EnumerationLiteral(name="SolidRounded"),
			EnumerationLiteral(name="DashedRounded")
    }
)

ButtonStyle: Enumeration = Enumeration(
    name="ButtonStyle",
    literals={
            EnumerationLiteral(name="PointLeft"),
			EnumerationLiteral(name="Square"),
			EnumerationLiteral(name="Round"),
			EnumerationLiteral(name="PointRight")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="Solid"),
			EnumerationLiteral(name="Dotted"),
			EnumerationLiteral(name="Dashed")
    }
)

ChartType: Enumeration = Enumeration(
    name="ChartType",
    literals={
            EnumerationLiteral(name="Pie"),
			EnumerationLiteral(name="Line"),
			EnumerationLiteral(name="Bar"),
			EnumerationLiteral(name="Column")
    }
)

Theme: Enumeration = Enumeration(
    name="Theme",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Clean"),
			EnumerationLiteral(name="Sketch")
    }
)

ShapeType: Enumeration = Enumeration(
    name="ShapeType",
    literals={
            EnumerationLiteral(name="Ellipse"),
			EnumerationLiteral(name="Rectangle"),
			EnumerationLiteral(name="RoundedRectangle"),
			EnumerationLiteral(name="RoundRectangle"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="Star"),
			EnumerationLiteral(name="Parallelogram"),
			EnumerationLiteral(name="Triangle"),
			EnumerationLiteral(name="RightTriangle")
    }
)

Rotation90: Enumeration = Enumeration(
    name="Rotation90",
    literals={
            EnumerationLiteral(name="_0"),
			EnumerationLiteral(name="_90"),
			EnumerationLiteral(name="_180"),
			EnumerationLiteral(name="_270")
    }
)

# Classes
model_Screen = Class(name="model::Screen")
WidgetContainer = Class(name="WidgetContainer")
NoteSupport = Class(name="NoteSupport")
model_ScreenRuler = Class(name="model::ScreenRuler")
model_ScreenFont = Class(name="model::ScreenFont")
model_RulerGuide = Class(name="model::RulerGuide")
model_Widget = Class(name="model::Widget", is_abstract=True)
model_WidgetContainer = Class(name="model::WidgetContainer", is_abstract=True)
model_WidgetDescriptor = Class(name="model::WidgetDescriptor")
model_Button = Class(name="model::Button")
Widget = Class(name="Widget")
StateSupport = Class(name="StateSupport")
ColorBackgroundSupport = Class(name="ColorBackgroundSupport")
FontSupport = Class(name="FontSupport")
IconSupport = Class(name="IconSupport")
LinkSupport = Class(name="LinkSupport")
TextAlignmentSupport = Class(name="TextAlignmentSupport")
SkinSupport = Class(name="SkinSupport")
model_Checkbox = Class(name="model::Checkbox")
BooleanSelectionSupport = Class(name="BooleanSelectionSupport")
model_Combo = Class(name="model::Combo")
ColorBorderSupport = Class(name="ColorBorderSupport")
ColorAlphaSupport = Class(name="ColorAlphaSupport")
ItemSupport = Class(name="ItemSupport")
model_Placeholder = Class(name="model::Placeholder")
model_RadioButton = Class(name="model::RadioButton")
model_TextField = Class(name="model::TextField")
model_Spinner = Class(name="model::Spinner")
model_Window = Class(name="model::Window")
VerticalScrollbarSupport = Class(name="VerticalScrollbarSupport")
model_Browser = Class(name="model::Browser")
model_Label = Class(name="model::Label")
ColorForegroundSupport = Class(name="ColorForegroundSupport")
IconPositionSupport = Class(name="IconPositionSupport")
RotationSupport = Class(name="RotationSupport")
TextLinksSupport = Class(name="TextLinksSupport")
model_Link = Class(name="model::Link")
model_Area = Class(name="model::Area")
model_Panel = Class(name="model::Panel")
BorderStyleSupport = Class(name="BorderStyleSupport")
model_Group = Class(name="model::Group")
model_List = Class(name="model::List")
SelectionSupport = Class(name="SelectionSupport")
BorderSupport = Class(name="BorderSupport")
ListSupport = Class(name="ListSupport")
ColorAlternativeSupport = Class(name="ColorAlternativeSupport")
model_Popup = Class(name="model::Popup")
model_Menu = Class(name="model::Menu")
model_Table = Class(name="model::Table")
model_Text = Class(name="model::Text")
LineHeightSupport = Class(name="LineHeightSupport")
model_Icon = Class(name="model::Icon")
model_TextArea = Class(name="model::TextArea")
model_HScrollbar = Class(name="model::HScrollbar")
ValueSupport = Class(name="ValueSupport")
model_VScrollbar = Class(name="model::VScrollbar")
model_HLine = Class(name="model::HLine")
LineStyleSupport = Class(name="LineStyleSupport")
model_VLine = Class(name="model::VLine")
model_HSlider = Class(name="model::HSlider")
model_VSlider = Class(name="model::VSlider")
model_Tabs = Class(name="model::Tabs")
model_Tree = Class(name="model::Tree")
model_Font = Class(name="model::Font")
model_WidgetGroup = Class(name="model::WidgetGroup")
NameSupport = Class(name="NameSupport")
model_Master = Class(name="model::Master")
model_Image = Class(name="model::Image")
FlipSupport = Class(name="FlipSupport")
model_FontSupport = Class(name="model::FontSupport", is_abstract=True)
model_ColorForegroundSupport = Class(name="model::ColorForegroundSupport", is_abstract=True)
model_ColorBackgroundSupport = Class(name="model::ColorBackgroundSupport", is_abstract=True)
model_ColorBorderSupport = Class(name="model::ColorBorderSupport", is_abstract=True)
Overrides = Class(name="Overrides")
model_TextAlignmentSupport = Class(name="model::TextAlignmentSupport", is_abstract=True)
model_BooleanSelectionSupport = Class(name="model::BooleanSelectionSupport", is_abstract=True)
model_Note = Class(name="model::Note")
AnnotationSupport = Class(name="AnnotationSupport")
model_ProgressBar = Class(name="model::ProgressBar")
model_Callout = Class(name="model::Callout")
model_SearchField = Class(name="model::SearchField")
model_ColorAlphaSupport = Class(name="model::ColorAlphaSupport", is_abstract=True)
model_SelectionSupport = Class(name="model::SelectionSupport", is_abstract=True)
model_ScratchOut = Class(name="model::ScratchOut")
model_BorderSupport = Class(name="model::BorderSupport", is_abstract=True)
model_StateSupport = Class(name="model::StateSupport", is_abstract=True)
model_Breadcrumbs = Class(name="model::Breadcrumbs")
model_LinkBar = Class(name="model::LinkBar")
model_Tooltip = Class(name="model::Tooltip")
model_DateField = Class(name="model::DateField")
model_VideoPlayer = Class(name="model::VideoPlayer")
model_Map = Class(name="model::Map")
model_CoverFlow = Class(name="model::CoverFlow")
model_TabbedPane = Class(name="model::TabbedPane")
model_IconSupport = Class(name="model::IconSupport", is_abstract=True)
model_Accordion = Class(name="model::Accordion")
model_VerticalScrollbarSupport = Class(name="model::VerticalScrollbarSupport", is_abstract=True)
model_ValueSupport = Class(name="model::ValueSupport", is_abstract=True)
model_ColorPicker = Class(name="model::ColorPicker")
model_Arrow = Class(name="model::Arrow")
model_CurlyBrace = Class(name="model::CurlyBrace")
model_HSplitter = Class(name="model::HSplitter")
model_VSplitter = Class(name="model::VSplitter")
model_Circle = Class(name="model::Circle")
model_Rectangle = Class(name="model::Rectangle")
model_IconPositionSupport = Class(name="model::IconPositionSupport", is_abstract=True)
model_ButtonBar = Class(name="model::ButtonBar")
model_BorderStyleSupport = Class(name="model::BorderStyleSupport", is_abstract=True)
model_ColorAlternativeSupport = Class(name="model::ColorAlternativeSupport", is_abstract=True)
model_Chart = Class(name="model::Chart")
model_LineStyleSupport = Class(name="model::LineStyleSupport", is_abstract=True)
model_CrossOut = Class(name="model::CrossOut")
model_RotationSupport = Class(name="model::RotationSupport", is_abstract=True)
model_Item = Class(name="model::Item")
model_FlipSupport = Class(name="model::FlipSupport", is_abstract=True)
model_ItemSupport = Class(name="model::ItemSupport", is_abstract=True)
model_LinkSupport = Class(name="model::LinkSupport", is_abstract=True)
model_Hotspot = Class(name="model::Hotspot")
model_ListSupport = Class(name="model::ListSupport", is_abstract=True)
model_NameSupport = Class(name="model::NameSupport", is_abstract=True)
model_SVGImage = Class(name="model::SVGImage")
model_Alert = Class(name="model::Alert")
model_SkinSupport = Class(name="model::SkinSupport", is_abstract=True)
model_Shape = Class(name="model::Shape")
model_AnnotationSupport = Class(name="model::AnnotationSupport", is_abstract=True)
model_TextLinksSupport = Class(name="model::TextLinksSupport", is_abstract=True)
model_NoteSupport = Class(name="model::NoteSupport", is_abstract=True)
model_story_Storyboard = Class(name="model::story::Storyboard")
Panel = Class(name="Panel")
model_story_Panel = Class(name="model::story::Panel")
story_model_Screen = Class(name="story::model::Screen")
Storyboard = Class(name="Storyboard")
model_overrides_Overrides = Class(name="model::overrides::Overrides")
WidgetContainerOverrides = Class(name="WidgetContainerOverrides")
WidgetOverrides = Class(name="WidgetOverrides")
model_Switch = Class(name="model::Switch")
model_LineHeightSupport = Class(name="model::LineHeightSupport", is_abstract=True)
model_VButtonBar = Class(name="model::VButtonBar")
StringToStringMap = Class(name="StringToStringMap")
FontOverrides = Class(name="FontOverrides")
ItemOverrides = Class(name="ItemOverrides")
Operation = Class(name="Operation")
model_overrides_FontOverrides = Class(name="model::overrides::FontOverrides")
model_overrides_ItemOverrides = Class(name="model::overrides::ItemOverrides")
Reference = Class(name="Reference")
model_overrides_WidgetOverrides = Class(name="model::overrides::WidgetOverrides")
overrides_WidgetContainerOverrides = Class(name="overrides::WidgetContainerOverrides")
overrides_Reference = Class(name="overrides::Reference")
model_overrides_WidgetContainerOverrides = Class(name="model::overrides::WidgetContainerOverrides", is_abstract=True)
model_overrides_StringToStringMap = Class(name="model::overrides::StringToStringMap")
model_overrides_Operation = Class(name="model::overrides::Operation", is_abstract=True)
model_overrides_Move = Class(name="model::overrides::Move")
overrides_Operation = Class(name="overrides::Operation")
model_overrides_Delete = Class(name="model::overrides::Delete")
model_overrides_Insert = Class(name="model::overrides::Insert")
overrides_model_EObject = Class(name="overrides::model::EObject")
model_overrides_Reference = Class(name="model::overrides::Reference", is_abstract=True)

# model_Screen class attributes and methods
model_Screen_name: Property = Property(name="name", type=StringType)
model_Screen_theme: Property = Property(name="theme", type=StringType)
model_Screen_minVersion: Property = Property(name="minVersion", type=StringType)
model_Screen.attributes={model_Screen_minVersion, model_Screen_name, model_Screen_theme}

# WidgetContainer class attributes and methods

# NoteSupport class attributes and methods

# model_ScreenRuler class attributes and methods

# model_ScreenFont class attributes and methods
model_ScreenFont_name: Property = Property(name="name", type=StringType)
model_ScreenFont_size: Property = Property(name="size", type=StringType)
model_ScreenFont_bold: Property = Property(name="bold", type=BooleanType)
model_ScreenFont_italic: Property = Property(name="italic", type=BooleanType)
model_ScreenFont_available: Property = Property(name="available", type=StringType)
model_ScreenFont.attributes={model_ScreenFont_size, model_ScreenFont_italic, model_ScreenFont_bold, model_ScreenFont_available, model_ScreenFont_name}

# model_RulerGuide class attributes and methods
model_RulerGuide_position: Property = Property(name="position", type=IntegerType)
model_RulerGuide.attributes={model_RulerGuide_position}

# model_Widget class attributes and methods
model_Widget_id: Property = Property(name="id", type=StringType)
model_Widget_height: Property = Property(name="height", type=IntegerType)
model_Widget_text: Property = Property(name="text", type=StringType)
model_Widget_locked: Property = Property(name="locked", type=BooleanType)
model_Widget_measuredWidth: Property = Property(name="measuredWidth", type=IntegerType)
model_Widget_measuredHeight: Property = Property(name="measuredHeight", type=IntegerType)
model_Widget_customId: Property = Property(name="customId", type=StringType)
model_Widget_customData: Property = Property(name="customData", type=StringType)
model_Widget_annotation: Property = Property(name="annotation", type=BooleanType)
model_Widget_layoutParams: Property = Property(name="layoutParams", type=StringType)
model_Widget_x: Property = Property(name="x", type=IntegerType)
model_Widget_y: Property = Property(name="y", type=IntegerType)
model_Widget_width: Property = Property(name="width", type=IntegerType)
model_Widget.attributes={model_Widget_measuredWidth, model_Widget_width, model_Widget_customId, model_Widget_x, model_Widget_customData, model_Widget_id, model_Widget_measuredHeight, model_Widget_locked, model_Widget_text, model_Widget_annotation, model_Widget_layoutParams, model_Widget_y, model_Widget_height}

# model_WidgetContainer class attributes and methods

# model_WidgetDescriptor class attributes and methods
model_WidgetDescriptor_textWrappable: Property = Property(name="textWrappable", type=BooleanType)
model_WidgetDescriptor_textLines: Property = Property(name="textLines", type=IntegerType)
model_WidgetDescriptor_textCentered: Property = Property(name="textCentered", type=BooleanType)
model_WidgetDescriptor_typeName: Property = Property(name="typeName", type=StringType)
model_WidgetDescriptor_resizeMode: Property = Property(name="resizeMode", type=StringType)
model_WidgetDescriptor_textEditable: Property = Property(name="textEditable", type=BooleanType)
model_WidgetDescriptor.attributes={model_WidgetDescriptor_resizeMode, model_WidgetDescriptor_textLines, model_WidgetDescriptor_textWrappable, model_WidgetDescriptor_typeName, model_WidgetDescriptor_textCentered, model_WidgetDescriptor_textEditable}

# model_Button class attributes and methods
model_Button_style: Property = Property(name="style", type=StringType)
model_Button.attributes={model_Button_style}

# Widget class attributes and methods

# StateSupport class attributes and methods

# ColorBackgroundSupport class attributes and methods

# FontSupport class attributes and methods

# IconSupport class attributes and methods

# LinkSupport class attributes and methods

# TextAlignmentSupport class attributes and methods

# SkinSupport class attributes and methods

# model_Checkbox class attributes and methods

# BooleanSelectionSupport class attributes and methods

# model_Combo class attributes and methods

# ColorBorderSupport class attributes and methods

# ColorAlphaSupport class attributes and methods

# ItemSupport class attributes and methods

# model_Placeholder class attributes and methods

# model_RadioButton class attributes and methods

# model_TextField class attributes and methods

# model_Spinner class attributes and methods

# model_Window class attributes and methods
model_Window_closeButton: Property = Property(name="closeButton", type=BooleanType)
model_Window_minimizeButton: Property = Property(name="minimizeButton", type=BooleanType)
model_Window_maximizeButton: Property = Property(name="maximizeButton", type=BooleanType)
model_Window.attributes={model_Window_maximizeButton, model_Window_closeButton, model_Window_minimizeButton}

# VerticalScrollbarSupport class attributes and methods

# model_Browser class attributes and methods

# model_Label class attributes and methods

# ColorForegroundSupport class attributes and methods

# IconPositionSupport class attributes and methods

# RotationSupport class attributes and methods

# TextLinksSupport class attributes and methods

# model_Link class attributes and methods

# model_Area class attributes and methods

# model_Panel class attributes and methods

# BorderStyleSupport class attributes and methods

# model_Group class attributes and methods

# model_List class attributes and methods
model_List_header: Property = Property(name="header", type=BooleanType)
model_List.attributes={model_List_header}

# SelectionSupport class attributes and methods

# BorderSupport class attributes and methods

# ListSupport class attributes and methods

# ColorAlternativeSupport class attributes and methods

# model_Popup class attributes and methods

# model_Menu class attributes and methods

# model_Table class attributes and methods
model_Table_verticalLines: Property = Property(name="verticalLines", type=BooleanType)
model_Table_header: Property = Property(name="header", type=BooleanType)
model_Table.attributes={model_Table_verticalLines, model_Table_header}

# model_Text class attributes and methods
model_Text_dummyText: Property = Property(name="dummyText", type=BooleanType)
model_Text.attributes={model_Text_dummyText}

# LineHeightSupport class attributes and methods

# model_Icon class attributes and methods

# model_TextArea class attributes and methods

# model_HScrollbar class attributes and methods

# ValueSupport class attributes and methods

# model_VScrollbar class attributes and methods

# model_HLine class attributes and methods

# LineStyleSupport class attributes and methods

# model_VLine class attributes and methods

# model_HSlider class attributes and methods

# model_VSlider class attributes and methods

# model_Tabs class attributes and methods

# model_Tree class attributes and methods

# model_Font class attributes and methods
model_Font_size: Property = Property(name="size", type=StringType)
model_Font_bold: Property = Property(name="bold", type=StringType)
model_Font_italic: Property = Property(name="italic", type=StringType)
model_Font_underline: Property = Property(name="underline", type=StringType)
model_Font.attributes={model_Font_underline, model_Font_size, model_Font_bold, model_Font_italic}

# model_WidgetGroup class attributes and methods

# NameSupport class attributes and methods

# model_Master class attributes and methods
model_Master_dimmed: Property = Property(name="dimmed", type=BooleanType)
model_Master_m_getSourceWidget: Method = Method(name="getSourceWidget", parameters={Parameter(name='widget')}, type=Widget)
model_Master.attributes={model_Master_dimmed}
model_Master.methods={model_Master_m_getSourceWidget}

# model_Image class attributes and methods
model_Image_src: Property = Property(name="src", type=StringType)
model_Image_grayscale: Property = Property(name="grayscale", type=BooleanType)
model_Image.attributes={model_Image_src, model_Image_grayscale}

# FlipSupport class attributes and methods

# model_FontSupport class attributes and methods

# model_ColorForegroundSupport class attributes and methods
model_ColorForegroundSupport_foreground: Property = Property(name="foreground", type=StringType)
model_ColorForegroundSupport.attributes={model_ColorForegroundSupport_foreground}

# model_ColorBackgroundSupport class attributes and methods
model_ColorBackgroundSupport_background: Property = Property(name="background", type=StringType)
model_ColorBackgroundSupport.attributes={model_ColorBackgroundSupport_background}

# model_ColorBorderSupport class attributes and methods
model_ColorBorderSupport_borderColor: Property = Property(name="borderColor", type=StringType)
model_ColorBorderSupport.attributes={model_ColorBorderSupport_borderColor}

# Overrides class attributes and methods

# model_TextAlignmentSupport class attributes and methods
model_TextAlignmentSupport_textAlignment: Property = Property(name="textAlignment", type=StringType)
model_TextAlignmentSupport.attributes={model_TextAlignmentSupport_textAlignment}

# model_BooleanSelectionSupport class attributes and methods
model_BooleanSelectionSupport_selected: Property = Property(name="selected", type=BooleanType)
model_BooleanSelectionSupport.attributes={model_BooleanSelectionSupport_selected}

# model_Note class attributes and methods

# AnnotationSupport class attributes and methods

# model_ProgressBar class attributes and methods

# model_Callout class attributes and methods

# model_SearchField class attributes and methods

# model_ColorAlphaSupport class attributes and methods
model_ColorAlphaSupport_alpha: Property = Property(name="alpha", type=IntegerType)
model_ColorAlphaSupport.attributes={model_ColorAlphaSupport_alpha}

# model_SelectionSupport class attributes and methods
model_SelectionSupport_selection: Property = Property(name="selection", type=StringType)
model_SelectionSupport.attributes={model_SelectionSupport_selection}

# model_ScratchOut class attributes and methods

# model_BorderSupport class attributes and methods
model_BorderSupport_border: Property = Property(name="border", type=BooleanType)
model_BorderSupport.attributes={model_BorderSupport_border}

# model_StateSupport class attributes and methods
model_StateSupport_state: Property = Property(name="state", type=StringType)
model_StateSupport_m_isValidState: Method = Method(name="isValidState", parameters={Parameter(name='state')}, type=BooleanType)
model_StateSupport.attributes={model_StateSupport_state}
model_StateSupport.methods={model_StateSupport_m_isValidState}

# model_Breadcrumbs class attributes and methods

# model_LinkBar class attributes and methods

# model_Tooltip class attributes and methods
model_Tooltip_position: Property = Property(name="position", type=StringType)
model_Tooltip.attributes={model_Tooltip_position}

# model_DateField class attributes and methods

# model_VideoPlayer class attributes and methods

# model_Map class attributes and methods

# model_CoverFlow class attributes and methods

# model_TabbedPane class attributes and methods
model_TabbedPane_position: Property = Property(name="position", type=StringType)
model_TabbedPane.attributes={model_TabbedPane_position}

# model_IconSupport class attributes and methods
model_IconSupport_icon: Property = Property(name="icon", type=StringType)
model_IconSupport_iconRotation: Property = Property(name="iconRotation", type=StringType)
model_IconSupport.attributes={model_IconSupport_icon, model_IconSupport_iconRotation}

# model_Accordion class attributes and methods

# model_VerticalScrollbarSupport class attributes and methods
model_VerticalScrollbarSupport_verticalScrollbar: Property = Property(name="verticalScrollbar", type=BooleanType)
model_VerticalScrollbarSupport.attributes={model_VerticalScrollbarSupport_verticalScrollbar}

# model_ValueSupport class attributes and methods
model_ValueSupport_value: Property = Property(name="value", type=IntegerType)
model_ValueSupport.attributes={model_ValueSupport_value}

# model_ColorPicker class attributes and methods

# model_Arrow class attributes and methods
model_Arrow_left: Property = Property(name="left", type=BooleanType)
model_Arrow_right: Property = Property(name="right", type=BooleanType)
model_Arrow_direction: Property = Property(name="direction", type=StringType)
model_Arrow.attributes={model_Arrow_direction, model_Arrow_left, model_Arrow_right}

# model_CurlyBrace class attributes and methods
model_CurlyBrace_position: Property = Property(name="position", type=StringType)
model_CurlyBrace.attributes={model_CurlyBrace_position}

# model_HSplitter class attributes and methods

# model_VSplitter class attributes and methods

# model_Circle class attributes and methods

# model_Rectangle class attributes and methods

# model_IconPositionSupport class attributes and methods
model_IconPositionSupport_iconPosition: Property = Property(name="iconPosition", type=StringType)
model_IconPositionSupport.attributes={model_IconPositionSupport_iconPosition}

# model_ButtonBar class attributes and methods

# model_BorderStyleSupport class attributes and methods
model_BorderStyleSupport_border: Property = Property(name="border", type=StringType)
model_BorderStyleSupport.attributes={model_BorderStyleSupport_border}

# model_ColorAlternativeSupport class attributes and methods
model_ColorAlternativeSupport_alternative: Property = Property(name="alternative", type=StringType)
model_ColorAlternativeSupport.attributes={model_ColorAlternativeSupport_alternative}

# model_Chart class attributes and methods
model_Chart_chartType: Property = Property(name="chartType", type=StringType)
model_Chart.attributes={model_Chart_chartType}

# model_LineStyleSupport class attributes and methods
model_LineStyleSupport_lineStyle: Property = Property(name="lineStyle", type=StringType)
model_LineStyleSupport.attributes={model_LineStyleSupport_lineStyle}

# model_CrossOut class attributes and methods

# model_RotationSupport class attributes and methods
model_RotationSupport_rotation: Property = Property(name="rotation", type=StringType)
model_RotationSupport.attributes={model_RotationSupport_rotation}

# model_Item class attributes and methods
model_Item_x: Property = Property(name="x", type=IntegerType)
model_Item_y: Property = Property(name="y", type=IntegerType)
model_Item_width: Property = Property(name="width", type=IntegerType)
model_Item_height: Property = Property(name="height", type=IntegerType)
model_Item_text: Property = Property(name="text", type=StringType)
model_Item.attributes={model_Item_y, model_Item_width, model_Item_x, model_Item_text, model_Item_height}

# model_FlipSupport class attributes and methods
model_FlipSupport_hFlip: Property = Property(name="hFlip", type=BooleanType)
model_FlipSupport_vFlip: Property = Property(name="vFlip", type=BooleanType)
model_FlipSupport.attributes={model_FlipSupport_vFlip, model_FlipSupport_hFlip}

# model_ItemSupport class attributes and methods

# model_LinkSupport class attributes and methods
model_LinkSupport_link: Property = Property(name="link", type=StringType)
model_LinkSupport.attributes={model_LinkSupport_link}

# model_Hotspot class attributes and methods

# model_ListSupport class attributes and methods
model_ListSupport_rowHeight: Property = Property(name="rowHeight", type=IntegerType)
model_ListSupport_horizontalLines: Property = Property(name="horizontalLines", type=BooleanType)
model_ListSupport.attributes={model_ListSupport_rowHeight, model_ListSupport_horizontalLines}

# model_NameSupport class attributes and methods
model_NameSupport_name: Property = Property(name="name", type=StringType)
model_NameSupport.attributes={model_NameSupport_name}

# model_SVGImage class attributes and methods
model_SVGImage_src: Property = Property(name="src", type=StringType)
model_SVGImage.attributes={model_SVGImage_src}

# model_Alert class attributes and methods

# model_SkinSupport class attributes and methods
model_SkinSupport_skin: Property = Property(name="skin", type=StringType)
model_SkinSupport.attributes={model_SkinSupport_skin}

# model_Shape class attributes and methods
model_Shape_shapeType: Property = Property(name="shapeType", type=StringType)
model_Shape_m_isRotatable: Method = Method(name="isRotatable", parameters={}, type=BooleanType)
model_Shape.attributes={model_Shape_shapeType}
model_Shape.methods={model_Shape_m_isRotatable}

# model_AnnotationSupport class attributes and methods

# model_TextLinksSupport class attributes and methods

# model_NoteSupport class attributes and methods
model_NoteSupport_note: Property = Property(name="note", type=StringType)
model_NoteSupport.attributes={model_NoteSupport_note}

# model_story_Storyboard class attributes and methods

# Panel class attributes and methods

# model_story_Panel class attributes and methods
model_story_Panel_id: Property = Property(name="id", type=StringType)
model_story_Panel_x: Property = Property(name="x", type=IntegerType)
model_story_Panel_y: Property = Property(name="y", type=IntegerType)
model_story_Panel.attributes={model_story_Panel_y, model_story_Panel_x, model_story_Panel_id}

# story_model_Screen class attributes and methods

# Storyboard class attributes and methods

# model_overrides_Overrides class attributes and methods

# WidgetContainerOverrides class attributes and methods

# WidgetOverrides class attributes and methods

# model_Switch class attributes and methods

# model_LineHeightSupport class attributes and methods
model_LineHeightSupport_lineHeight: Property = Property(name="lineHeight", type=StringType)
model_LineHeightSupport.attributes={model_LineHeightSupport_lineHeight}

# model_VButtonBar class attributes and methods

# StringToStringMap class attributes and methods

# FontOverrides class attributes and methods

# ItemOverrides class attributes and methods

# Operation class attributes and methods

# model_overrides_FontOverrides class attributes and methods
model_overrides_FontOverrides_size: Property = Property(name="size", type=StringType)
model_overrides_FontOverrides_bold: Property = Property(name="bold", type=StringType)
model_overrides_FontOverrides_italic: Property = Property(name="italic", type=StringType)
model_overrides_FontOverrides_underline: Property = Property(name="underline", type=StringType)
model_overrides_FontOverrides.attributes={model_overrides_FontOverrides_size, model_overrides_FontOverrides_bold, model_overrides_FontOverrides_underline, model_overrides_FontOverrides_italic}

# model_overrides_ItemOverrides class attributes and methods
model_overrides_ItemOverrides_text: Property = Property(name="text", type=StringType)
model_overrides_ItemOverrides_link: Property = Property(name="link", type=StringType)
model_overrides_ItemOverrides_noLink: Property = Property(name="noLink", type=BooleanType)
model_overrides_ItemOverrides.attributes={model_overrides_ItemOverrides_link, model_overrides_ItemOverrides_text, model_overrides_ItemOverrides_noLink}

# Reference class attributes and methods

# model_overrides_WidgetOverrides class attributes and methods
model_overrides_WidgetOverrides_src: Property = Property(name="src", type=StringType)
model_overrides_WidgetOverrides_x: Property = Property(name="x", type=StringType)
model_overrides_WidgetOverrides_y: Property = Property(name="y", type=StringType)
model_overrides_WidgetOverrides_width: Property = Property(name="width", type=StringType)
model_overrides_WidgetOverrides_height: Property = Property(name="height", type=StringType)
model_overrides_WidgetOverrides_text: Property = Property(name="text", type=StringType)
model_overrides_WidgetOverrides_noText: Property = Property(name="noText", type=BooleanType)
model_overrides_WidgetOverrides_link: Property = Property(name="link", type=StringType)
model_overrides_WidgetOverrides_noLink: Property = Property(name="noLink", type=BooleanType)
model_overrides_WidgetOverrides.attributes={model_overrides_WidgetOverrides_src, model_overrides_WidgetOverrides_width, model_overrides_WidgetOverrides_link, model_overrides_WidgetOverrides_noText, model_overrides_WidgetOverrides_text, model_overrides_WidgetOverrides_height, model_overrides_WidgetOverrides_y, model_overrides_WidgetOverrides_noLink, model_overrides_WidgetOverrides_x}

# overrides_WidgetContainerOverrides class attributes and methods

# overrides_Reference class attributes and methods

# model_overrides_WidgetContainerOverrides class attributes and methods

# model_overrides_StringToStringMap class attributes and methods
model_overrides_StringToStringMap_key: Property = Property(name="key", type=StringType)
model_overrides_StringToStringMap_value: Property = Property(name="value", type=StringType)
model_overrides_StringToStringMap.attributes={model_overrides_StringToStringMap_value, model_overrides_StringToStringMap_key}

# model_overrides_Operation class attributes and methods

# model_overrides_Move class attributes and methods
model_overrides_Move_newIndex: Property = Property(name="newIndex", type=IntegerType)
model_overrides_Move.attributes={model_overrides_Move_newIndex}

# overrides_Operation class attributes and methods

# model_overrides_Delete class attributes and methods

# model_overrides_Insert class attributes and methods
model_overrides_Insert_newIndex: Property = Property(name="newIndex", type=IntegerType)
model_overrides_Insert.attributes={model_overrides_Insert_newIndex}

# overrides_model_EObject class attributes and methods

# model_overrides_Reference class attributes and methods
model_overrides_Reference_ref: Property = Property(name="ref", type=StringType)
model_overrides_Reference.attributes={model_overrides_Reference_ref}

# Relationships
hRuler0: BinaryAssociation = BinaryAssociation(
    name="hRuler0",
    ends={
        Property(name="model_ScreenRuler", type=model_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Screen", type=model_ScreenRuler, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vRuler1: BinaryAssociation = BinaryAssociation(
    name="vRuler1",
    ends={
        Property(name="model_ScreenRuler3", type=model_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Screen2", type=model_ScreenRuler, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
font4: BinaryAssociation = BinaryAssociation(
    name="font4",
    ends={
        Property(name="model_ScreenFont", type=model_Screen, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Screen5", type=model_ScreenFont, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guides6: BinaryAssociation = BinaryAssociation(
    name="guides6",
    ends={
        Property(name="model_RulerGuide", type=model_ScreenRuler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ScreenRuler7", type=model_RulerGuide, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor9: BinaryAssociation = BinaryAssociation(
    name="descriptor9",
    ends={
        Property(name="model_WidgetDescriptor", type=model_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Widget", type=model_WidgetDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
container8: BinaryAssociation = BinaryAssociation(
    name="container8",
    ends={
        Property(name="WidgetContainer", type=model_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="widgets", type=model_WidgetContainer, multiplicity=Multiplicity(0, 1))
    }
)
widgets10: BinaryAssociation = BinaryAssociation(
    name="widgets10",
    ends={
        Property(name="Widget", type=model_WidgetContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=model_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance14: BinaryAssociation = BinaryAssociation(
    name="instance14",
    ends={
        Property(name="model_WidgetContainer16", type=model_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Master15", type=model_WidgetContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font17: BinaryAssociation = BinaryAssociation(
    name="font17",
    ends={
        Property(name="model_Font", type=model_FontSupport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FontSupport", type=model_Font, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
screen11: BinaryAssociation = BinaryAssociation(
    name="screen11",
    ends={
        Property(name="model_WidgetContainer", type=model_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Master", type=model_WidgetContainer, multiplicity=Multiplicity(0, 1))
    }
)
overrides12: BinaryAssociation = BinaryAssociation(
    name="overrides12",
    ends={
        Property(name="Overrides", type=model_Master, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Master13", type=Overrides, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="model_Item", type=model_ItemSupport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ItemSupport", type=model_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
panels19: BinaryAssociation = BinaryAssociation(
    name="panels19",
    ends={
        Property(name="Panel", type=model_story_Storyboard, multiplicity=Multiplicity(1, 1)),
        Property(name="model_story_Storyboard", type=Panel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screen20: BinaryAssociation = BinaryAssociation(
    name="screen20",
    ends={
        Property(name="story_model_Screen", type=model_story_Panel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_story_Panel", type=story_model_Screen, multiplicity=Multiplicity(0, 1))
    }
)
story21: BinaryAssociation = BinaryAssociation(
    name="story21",
    ends={
        Property(name="Storyboard", type=model_story_Panel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_story_Panel22", type=Storyboard, multiplicity=Multiplicity(0, 1))
    }
)
attributes24: BinaryAssociation = BinaryAssociation(
    name="attributes24",
    ends={
        Property(name="StringToStringMap", type=model_overrides_WidgetOverrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_WidgetOverrides", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
font25: BinaryAssociation = BinaryAssociation(
    name="font25",
    ends={
        Property(name="FontOverrides", type=model_overrides_WidgetOverrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_WidgetOverrides26", type=FontOverrides, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items27: BinaryAssociation = BinaryAssociation(
    name="items27",
    ends={
        Property(name="ItemOverrides", type=model_overrides_WidgetOverrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_WidgetOverrides28", type=ItemOverrides, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemChanges29: BinaryAssociation = BinaryAssociation(
    name="itemChanges29",
    ends={
        Property(name="Operation", type=model_overrides_WidgetOverrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_WidgetOverrides30", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
widgets23: BinaryAssociation = BinaryAssociation(
    name="widgets23",
    ends={
        Property(name="WidgetOverrides", type=model_overrides_Overrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_Overrides", type=WidgetOverrides, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
widgetChanges32: BinaryAssociation = BinaryAssociation(
    name="widgetChanges32",
    ends={
        Property(name="Operation33", type=model_overrides_WidgetContainerOverrides, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_WidgetContainerOverrides", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object31: BinaryAssociation = BinaryAssociation(
    name="object31",
    ends={
        Property(name="overrides_model_EObject", type=model_overrides_Insert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_overrides_Insert", type=overrides_model_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_Screen_WidgetContainer = Generalization(general=WidgetContainer, specific=model_Screen)
gen_model_Screen_NoteSupport = Generalization(general=NoteSupport, specific=model_Screen)
gen_model_Widget_NoteSupport = Generalization(general=NoteSupport, specific=model_Widget)
gen_model_Button_Widget = Generalization(general=Widget, specific=model_Button)
gen_model_Button_StateSupport = Generalization(general=StateSupport, specific=model_Button)
gen_model_Button_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Button)
gen_model_Button_FontSupport = Generalization(general=FontSupport, specific=model_Button)
gen_model_Button_IconSupport = Generalization(general=IconSupport, specific=model_Button)
gen_model_Button_LinkSupport = Generalization(general=LinkSupport, specific=model_Button)
gen_model_Button_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Button)
gen_model_Button_SkinSupport = Generalization(general=SkinSupport, specific=model_Button)
gen_model_Checkbox_Widget = Generalization(general=Widget, specific=model_Checkbox)
gen_model_Checkbox_BooleanSelectionSupport = Generalization(general=BooleanSelectionSupport, specific=model_Checkbox)
gen_model_Checkbox_StateSupport = Generalization(general=StateSupport, specific=model_Checkbox)
gen_model_Checkbox_LinkSupport = Generalization(general=LinkSupport, specific=model_Checkbox)
gen_model_Checkbox_FontSupport = Generalization(general=FontSupport, specific=model_Checkbox)
gen_model_Checkbox_SkinSupport = Generalization(general=SkinSupport, specific=model_Checkbox)
gen_model_Combo_Widget = Generalization(general=Widget, specific=model_Combo)
gen_model_Combo_StateSupport = Generalization(general=StateSupport, specific=model_Combo)
gen_model_Combo_FontSupport = Generalization(general=FontSupport, specific=model_Combo)
gen_model_Combo_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_Combo)
gen_model_Combo_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Combo)
gen_model_Combo_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Combo)
gen_model_Combo_LinkSupport = Generalization(general=LinkSupport, specific=model_Combo)
gen_model_Combo_ItemSupport = Generalization(general=ItemSupport, specific=model_Combo)
gen_model_Link_Widget = Generalization(general=Widget, specific=model_Link)
gen_model_Link_FontSupport = Generalization(general=FontSupport, specific=model_Link)
gen_model_Link_StateSupport = Generalization(general=StateSupport, specific=model_Link)
gen_model_Link_LinkSupport = Generalization(general=LinkSupport, specific=model_Link)
gen_model_Link_SkinSupport = Generalization(general=SkinSupport, specific=model_Link)
gen_model_Placeholder_Widget = Generalization(general=Widget, specific=model_Placeholder)
gen_model_Placeholder_LinkSupport = Generalization(general=LinkSupport, specific=model_Placeholder)
gen_model_Placeholder_SkinSupport = Generalization(general=SkinSupport, specific=model_Placeholder)
gen_model_RadioButton_Widget = Generalization(general=Widget, specific=model_RadioButton)
gen_model_RadioButton_BooleanSelectionSupport = Generalization(general=BooleanSelectionSupport, specific=model_RadioButton)
gen_model_RadioButton_StateSupport = Generalization(general=StateSupport, specific=model_RadioButton)
gen_model_RadioButton_LinkSupport = Generalization(general=LinkSupport, specific=model_RadioButton)
gen_model_RadioButton_FontSupport = Generalization(general=FontSupport, specific=model_RadioButton)
gen_model_RadioButton_SkinSupport = Generalization(general=SkinSupport, specific=model_RadioButton)
gen_model_TextField_Widget = Generalization(general=Widget, specific=model_TextField)
gen_model_TextField_StateSupport = Generalization(general=StateSupport, specific=model_TextField)
gen_model_TextField_FontSupport = Generalization(general=FontSupport, specific=model_TextField)
gen_model_TextField_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_TextField)
gen_model_TextField_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_TextField)
gen_model_TextField_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_TextField)
gen_model_TextField_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_TextField)
gen_model_TextField_SkinSupport = Generalization(general=SkinSupport, specific=model_TextField)
gen_model_Spinner_Widget = Generalization(general=Widget, specific=model_Spinner)
gen_model_Spinner_StateSupport = Generalization(general=StateSupport, specific=model_Spinner)
gen_model_Spinner_FontSupport = Generalization(general=FontSupport, specific=model_Spinner)
gen_model_Spinner_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_Spinner)
gen_model_Spinner_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Spinner)
gen_model_Spinner_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Spinner)
gen_model_Spinner_SkinSupport = Generalization(general=SkinSupport, specific=model_Spinner)
gen_model_Window_Widget = Generalization(general=Widget, specific=model_Window)
gen_model_Window_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Window)
gen_model_Window_SkinSupport = Generalization(general=SkinSupport, specific=model_Window)
gen_model_Window_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Window)
gen_model_Window_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Window)
gen_model_Browser_Widget = Generalization(general=Widget, specific=model_Browser)
gen_model_Browser_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Browser)
gen_model_Browser_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Browser)
gen_model_Browser_SkinSupport = Generalization(general=SkinSupport, specific=model_Browser)
gen_model_Browser_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Browser)
gen_model_Combo_SkinSupport = Generalization(general=SkinSupport, specific=model_Combo)
gen_model_Label_Widget = Generalization(general=Widget, specific=model_Label)
gen_model_Label_FontSupport = Generalization(general=FontSupport, specific=model_Label)
gen_model_Label_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Label)
gen_model_Label_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Label)
gen_model_Label_StateSupport = Generalization(general=StateSupport, specific=model_Label)
gen_model_Label_IconSupport = Generalization(general=IconSupport, specific=model_Label)
gen_model_Label_IconPositionSupport = Generalization(general=IconPositionSupport, specific=model_Label)
gen_model_Label_LinkSupport = Generalization(general=LinkSupport, specific=model_Label)
gen_model_Label_RotationSupport = Generalization(general=RotationSupport, specific=model_Label)
gen_model_Label_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_Label)
gen_model_Area_Widget = Generalization(general=Widget, specific=model_Area)
gen_model_Panel_Widget = Generalization(general=Widget, specific=model_Panel)
gen_model_Panel_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Panel)
gen_model_Panel_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Panel)
gen_model_Panel_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Panel)
gen_model_Panel_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Panel)
gen_model_Panel_BorderStyleSupport = Generalization(general=BorderStyleSupport, specific=model_Panel)
gen_model_Panel_LinkSupport = Generalization(general=LinkSupport, specific=model_Panel)
gen_model_Panel_SkinSupport = Generalization(general=SkinSupport, specific=model_Panel)
gen_model_Group_Widget = Generalization(general=Widget, specific=model_Group)
gen_model_Group_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Group)
gen_model_Group_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Group)
gen_model_Group_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Group)
gen_model_Group_FontSupport = Generalization(general=FontSupport, specific=model_Group)
gen_model_Group_SkinSupport = Generalization(general=SkinSupport, specific=model_Group)
gen_model_List_Widget = Generalization(general=Widget, specific=model_List)
gen_model_List_SelectionSupport = Generalization(general=SelectionSupport, specific=model_List)
gen_model_List_BorderSupport = Generalization(general=BorderSupport, specific=model_List)
gen_model_List_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_List)
gen_model_List_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_List)
gen_model_List_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_List)
gen_model_List_ListSupport = Generalization(general=ListSupport, specific=model_List)
gen_model_List_FontSupport = Generalization(general=FontSupport, specific=model_List)
gen_model_List_ItemSupport = Generalization(general=ItemSupport, specific=model_List)
gen_model_List_ColorAlternativeSupport = Generalization(general=ColorAlternativeSupport, specific=model_List)
gen_model_Popup_Widget = Generalization(general=Widget, specific=model_Popup)
gen_model_Popup_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Popup)
gen_model_Popup_ItemSupport = Generalization(general=ItemSupport, specific=model_Popup)
gen_model_Menu_Widget = Generalization(general=Widget, specific=model_Menu)
gen_model_Menu_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Menu)
gen_model_Menu_IconSupport = Generalization(general=IconSupport, specific=model_Menu)
gen_model_Menu_ItemSupport = Generalization(general=ItemSupport, specific=model_Menu)
gen_model_Menu_SkinSupport = Generalization(general=SkinSupport, specific=model_Menu)
gen_model_Table_Widget = Generalization(general=Widget, specific=model_Table)
gen_model_Table_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Table)
gen_model_Table_BorderSupport = Generalization(general=BorderSupport, specific=model_Table)
gen_model_Table_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Table)
gen_model_Table_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Table)
gen_model_Table_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Table)
gen_model_Table_ListSupport = Generalization(general=ListSupport, specific=model_Table)
gen_model_Table_FontSupport = Generalization(general=FontSupport, specific=model_Table)
gen_model_Table_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Table)
gen_model_Table_ColorAlternativeSupport = Generalization(general=ColorAlternativeSupport, specific=model_Table)
gen_model_Table_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_Table)
gen_model_Browser_FontSupport = Generalization(general=FontSupport, specific=model_Browser)
gen_model_Text_Widget = Generalization(general=Widget, specific=model_Text)
gen_model_Text_FontSupport = Generalization(general=FontSupport, specific=model_Text)
gen_model_Text_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Text)
gen_model_Text_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Text)
gen_model_Text_LinkSupport = Generalization(general=LinkSupport, specific=model_Text)
gen_model_Text_LineHeightSupport = Generalization(general=LineHeightSupport, specific=model_Text)
gen_model_Text_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_Text)
gen_model_Tree_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Tree)
gen_model_Tree_ItemSupport = Generalization(general=ItemSupport, specific=model_Tree)
gen_model_Tree_FontSupport = Generalization(general=FontSupport, specific=model_Tree)
gen_model_Icon_Widget = Generalization(general=Widget, specific=model_Icon)
gen_model_Icon_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Icon)
gen_model_Icon_IconSupport = Generalization(general=IconSupport, specific=model_Icon)
gen_model_Icon_LinkSupport = Generalization(general=LinkSupport, specific=model_Icon)
gen_model_TextArea_Widget = Generalization(general=Widget, specific=model_TextArea)
gen_model_TextArea_StateSupport = Generalization(general=StateSupport, specific=model_TextArea)
gen_model_TextArea_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_TextArea)
gen_model_TextArea_FontSupport = Generalization(general=FontSupport, specific=model_TextArea)
gen_model_TextArea_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_TextArea)
gen_model_TextArea_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_TextArea)
gen_model_TextArea_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_TextArea)
gen_model_TextArea_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_TextArea)
gen_model_TextArea_SkinSupport = Generalization(general=SkinSupport, specific=model_TextArea)
gen_model_TextArea_LineHeightSupport = Generalization(general=LineHeightSupport, specific=model_TextArea)
gen_model_TextArea_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_TextArea)
gen_model_HScrollbar_Widget = Generalization(general=Widget, specific=model_HScrollbar)
gen_model_HScrollbar_ValueSupport = Generalization(general=ValueSupport, specific=model_HScrollbar)
gen_model_HScrollbar_SkinSupport = Generalization(general=SkinSupport, specific=model_HScrollbar)
gen_model_VScrollbar_Widget = Generalization(general=Widget, specific=model_VScrollbar)
gen_model_VScrollbar_ValueSupport = Generalization(general=ValueSupport, specific=model_VScrollbar)
gen_model_VScrollbar_SkinSupport = Generalization(general=SkinSupport, specific=model_VScrollbar)
gen_model_HLine_Widget = Generalization(general=Widget, specific=model_HLine)
gen_model_HLine_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_HLine)
gen_model_HLine_LineStyleSupport = Generalization(general=LineStyleSupport, specific=model_HLine)
gen_model_HLine_SkinSupport = Generalization(general=SkinSupport, specific=model_HLine)
gen_model_VLine_Widget = Generalization(general=Widget, specific=model_VLine)
gen_model_VLine_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_VLine)
gen_model_VLine_LineStyleSupport = Generalization(general=LineStyleSupport, specific=model_VLine)
gen_model_VLine_SkinSupport = Generalization(general=SkinSupport, specific=model_VLine)
gen_model_HSlider_Widget = Generalization(general=Widget, specific=model_HSlider)
gen_model_HSlider_ValueSupport = Generalization(general=ValueSupport, specific=model_HSlider)
gen_model_HSlider_StateSupport = Generalization(general=StateSupport, specific=model_HSlider)
gen_model_HSlider_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_HSlider)
gen_model_HSlider_SkinSupport = Generalization(general=SkinSupport, specific=model_HSlider)
gen_model_VSlider_Widget = Generalization(general=Widget, specific=model_VSlider)
gen_model_VSlider_ValueSupport = Generalization(general=ValueSupport, specific=model_VSlider)
gen_model_VSlider_StateSupport = Generalization(general=StateSupport, specific=model_VSlider)
gen_model_VSlider_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_VSlider)
gen_model_VSlider_SkinSupport = Generalization(general=SkinSupport, specific=model_VSlider)
gen_model_Tabs_Widget = Generalization(general=Widget, specific=model_Tabs)
gen_model_Tabs_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Tabs)
gen_model_Tabs_ItemSupport = Generalization(general=ItemSupport, specific=model_Tabs)
gen_model_Tabs_FontSupport = Generalization(general=FontSupport, specific=model_Tabs)
gen_model_Tabs_SkinSupport = Generalization(general=SkinSupport, specific=model_Tabs)
gen_model_Tree_Widget = Generalization(general=Widget, specific=model_Tree)
gen_model_Tree_BorderSupport = Generalization(general=BorderSupport, specific=model_Tree)
gen_model_Tree_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Tree)
gen_model_Tree_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Tree)
gen_model_Tree_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Tree)
gen_model_WidgetGroup_Widget = Generalization(general=Widget, specific=model_WidgetGroup)
gen_model_WidgetGroup_WidgetContainer = Generalization(general=WidgetContainer, specific=model_WidgetGroup)
gen_model_WidgetGroup_LinkSupport = Generalization(general=LinkSupport, specific=model_WidgetGroup)
gen_model_WidgetGroup_NameSupport = Generalization(general=NameSupport, specific=model_WidgetGroup)
gen_model_Master_Widget = Generalization(general=Widget, specific=model_Master)
gen_model_Master_LinkSupport = Generalization(general=LinkSupport, specific=model_Master)
gen_model_Image_Widget = Generalization(general=Widget, specific=model_Image)
gen_model_Image_LinkSupport = Generalization(general=LinkSupport, specific=model_Image)
gen_model_Image_RotationSupport = Generalization(general=RotationSupport, specific=model_Image)
gen_model_Image_FlipSupport = Generalization(general=FlipSupport, specific=model_Image)
gen_model_Image_BorderSupport = Generalization(general=BorderSupport, specific=model_Image)
gen_model_Note_Widget = Generalization(general=Widget, specific=model_Note)
gen_model_Note_FontSupport = Generalization(general=FontSupport, specific=model_Note)
gen_model_Note_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Note)
gen_model_Note_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Note)
gen_model_Note_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Note)
gen_model_Note_LinkSupport = Generalization(general=LinkSupport, specific=model_Note)
gen_model_Note_SkinSupport = Generalization(general=SkinSupport, specific=model_Note)
gen_model_Note_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_Note)
gen_model_Note_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_Note)
gen_model_ProgressBar_Widget = Generalization(general=Widget, specific=model_ProgressBar)
gen_model_ProgressBar_ValueSupport = Generalization(general=ValueSupport, specific=model_ProgressBar)
gen_model_ProgressBar_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_ProgressBar)
gen_model_ProgressBar_SkinSupport = Generalization(general=SkinSupport, specific=model_ProgressBar)
gen_model_Callout_Widget = Generalization(general=Widget, specific=model_Callout)
gen_model_Callout_FontSupport = Generalization(general=FontSupport, specific=model_Callout)
gen_model_Callout_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Callout)
gen_model_Callout_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Callout)
gen_model_Callout_LinkSupport = Generalization(general=LinkSupport, specific=model_Callout)
gen_model_Callout_SkinSupport = Generalization(general=SkinSupport, specific=model_Callout)
gen_model_Callout_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_Callout)
gen_model_SearchField_Widget = Generalization(general=Widget, specific=model_SearchField)
gen_model_SearchField_FontSupport = Generalization(general=FontSupport, specific=model_SearchField)
gen_model_SearchField_StateSupport = Generalization(general=StateSupport, specific=model_SearchField)
gen_model_SearchField_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_SearchField)
gen_model_SearchField_LinkSupport = Generalization(general=LinkSupport, specific=model_SearchField)
gen_model_SearchField_SkinSupport = Generalization(general=SkinSupport, specific=model_SearchField)
gen_model_Tooltip_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_Tooltip)
gen_model_ScratchOut_Widget = Generalization(general=Widget, specific=model_ScratchOut)
gen_model_ScratchOut_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_ScratchOut)
gen_model_ScratchOut_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_ScratchOut)
gen_model_ScratchOut_SkinSupport = Generalization(general=SkinSupport, specific=model_ScratchOut)
gen_model_ScratchOut_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_ScratchOut)
gen_model_Breadcrumbs_Widget = Generalization(general=Widget, specific=model_Breadcrumbs)
gen_model_Breadcrumbs_FontSupport = Generalization(general=FontSupport, specific=model_Breadcrumbs)
gen_model_Breadcrumbs_ItemSupport = Generalization(general=ItemSupport, specific=model_Breadcrumbs)
gen_model_Breadcrumbs_SkinSupport = Generalization(general=SkinSupport, specific=model_Breadcrumbs)
gen_model_LinkBar_Widget = Generalization(general=Widget, specific=model_LinkBar)
gen_model_LinkBar_FontSupport = Generalization(general=FontSupport, specific=model_LinkBar)
gen_model_LinkBar_SelectionSupport = Generalization(general=SelectionSupport, specific=model_LinkBar)
gen_model_LinkBar_ItemSupport = Generalization(general=ItemSupport, specific=model_LinkBar)
gen_model_LinkBar_SkinSupport = Generalization(general=SkinSupport, specific=model_LinkBar)
gen_model_Tooltip_Widget = Generalization(general=Widget, specific=model_Tooltip)
gen_model_Tooltip_FontSupport = Generalization(general=FontSupport, specific=model_Tooltip)
gen_model_Tooltip_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Tooltip)
gen_model_Tooltip_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Tooltip)
gen_model_Tooltip_SkinSupport = Generalization(general=SkinSupport, specific=model_Tooltip)
gen_model_DateField_Widget = Generalization(general=Widget, specific=model_DateField)
gen_model_DateField_StateSupport = Generalization(general=StateSupport, specific=model_DateField)
gen_model_DateField_ColorBorderSupport = Generalization(general=ColorBorderSupport, specific=model_DateField)
gen_model_DateField_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_DateField)
gen_model_DateField_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_DateField)
gen_model_DateField_SkinSupport = Generalization(general=SkinSupport, specific=model_DateField)
gen_model_VideoPlayer_Widget = Generalization(general=Widget, specific=model_VideoPlayer)
gen_model_VideoPlayer_SkinSupport = Generalization(general=SkinSupport, specific=model_VideoPlayer)
gen_model_Map_Widget = Generalization(general=Widget, specific=model_Map)
gen_model_Map_SkinSupport = Generalization(general=SkinSupport, specific=model_Map)
gen_model_CoverFlow_Widget = Generalization(general=Widget, specific=model_CoverFlow)
gen_model_CoverFlow_SkinSupport = Generalization(general=SkinSupport, specific=model_CoverFlow)
gen_model_TabbedPane_Widget = Generalization(general=Widget, specific=model_TabbedPane)
gen_model_TabbedPane_SelectionSupport = Generalization(general=SelectionSupport, specific=model_TabbedPane)
gen_model_TabbedPane_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_TabbedPane)
gen_model_TabbedPane_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_TabbedPane)
gen_model_TabbedPane_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_TabbedPane)
gen_model_TabbedPane_ItemSupport = Generalization(general=ItemSupport, specific=model_TabbedPane)
gen_model_TabbedPane_FontSupport = Generalization(general=FontSupport, specific=model_TabbedPane)
gen_model_TabbedPane_SkinSupport = Generalization(general=SkinSupport, specific=model_TabbedPane)
gen_model_Accordion_Widget = Generalization(general=Widget, specific=model_Accordion)
gen_model_Accordion_SelectionSupport = Generalization(general=SelectionSupport, specific=model_Accordion)
gen_model_Accordion_VerticalScrollbarSupport = Generalization(general=VerticalScrollbarSupport, specific=model_Accordion)
gen_model_Accordion_ItemSupport = Generalization(general=ItemSupport, specific=model_Accordion)
gen_model_Accordion_FontSupport = Generalization(general=FontSupport, specific=model_Accordion)
gen_model_VerticalScrollbarSupport_ValueSupport = Generalization(general=ValueSupport, specific=model_VerticalScrollbarSupport)
gen_model_VSplitter_SkinSupport = Generalization(general=SkinSupport, specific=model_VSplitter)
gen_model_ColorPicker_Widget = Generalization(general=Widget, specific=model_ColorPicker)
gen_model_ColorPicker_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_ColorPicker)
gen_model_ColorPicker_SkinSupport = Generalization(general=SkinSupport, specific=model_ColorPicker)
gen_model_Arrow_Widget = Generalization(general=Widget, specific=model_Arrow)
gen_model_Arrow_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Arrow)
gen_model_Arrow_LineStyleSupport = Generalization(general=LineStyleSupport, specific=model_Arrow)
gen_model_Arrow_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_Arrow)
gen_model_CurlyBrace_Widget = Generalization(general=Widget, specific=model_CurlyBrace)
gen_model_CurlyBrace_FontSupport = Generalization(general=FontSupport, specific=model_CurlyBrace)
gen_model_CurlyBrace_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_CurlyBrace)
gen_model_CurlyBrace_SkinSupport = Generalization(general=SkinSupport, specific=model_CurlyBrace)
gen_model_CurlyBrace_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_CurlyBrace)
gen_model_CurlyBrace_TextLinksSupport = Generalization(general=TextLinksSupport, specific=model_CurlyBrace)
gen_model_HSplitter_Widget = Generalization(general=Widget, specific=model_HSplitter)
gen_model_HSplitter_SkinSupport = Generalization(general=SkinSupport, specific=model_HSplitter)
gen_model_VSplitter_Widget = Generalization(general=Widget, specific=model_VSplitter)
gen_model_Circle_Widget = Generalization(general=Widget, specific=model_Circle)
gen_model_Circle_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Circle)
gen_model_Circle_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Circle)
gen_model_Circle_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Circle)
gen_model_Circle_BorderSupport = Generalization(general=BorderSupport, specific=model_Circle)
gen_model_Circle_IconSupport = Generalization(general=IconSupport, specific=model_Circle)
gen_model_Circle_IconPositionSupport = Generalization(general=IconPositionSupport, specific=model_Circle)
gen_model_Circle_FontSupport = Generalization(general=FontSupport, specific=model_Circle)
gen_model_Circle_LinkSupport = Generalization(general=LinkSupport, specific=model_Circle)
gen_model_Circle_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Circle)
gen_model_Circle_LineStyleSupport = Generalization(general=LineStyleSupport, specific=model_Circle)
gen_model_Rectangle_Widget = Generalization(general=Widget, specific=model_Rectangle)
gen_model_Rectangle_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Rectangle)
gen_model_Rectangle_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Rectangle)
gen_model_Rectangle_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Rectangle)
gen_model_Rectangle_BorderStyleSupport = Generalization(general=BorderStyleSupport, specific=model_Rectangle)
gen_model_Rectangle_IconSupport = Generalization(general=IconSupport, specific=model_Rectangle)
gen_model_Rectangle_IconPositionSupport = Generalization(general=IconPositionSupport, specific=model_Rectangle)
gen_model_Rectangle_FontSupport = Generalization(general=FontSupport, specific=model_Rectangle)
gen_model_Rectangle_LinkSupport = Generalization(general=LinkSupport, specific=model_Rectangle)
gen_model_Rectangle_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Rectangle)
gen_model_IconPositionSupport_IconSupport = Generalization(general=IconSupport, specific=model_IconPositionSupport)
gen_model_ButtonBar_Widget = Generalization(general=Widget, specific=model_ButtonBar)
gen_model_ButtonBar_SelectionSupport = Generalization(general=SelectionSupport, specific=model_ButtonBar)
gen_model_ButtonBar_FontSupport = Generalization(general=FontSupport, specific=model_ButtonBar)
gen_model_ButtonBar_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_ButtonBar)
gen_model_ButtonBar_ItemSupport = Generalization(general=ItemSupport, specific=model_ButtonBar)
gen_model_ButtonBar_SkinSupport = Generalization(general=SkinSupport, specific=model_ButtonBar)
gen_model_Chart_Widget = Generalization(general=Widget, specific=model_Chart)
gen_model_Chart_SkinSupport = Generalization(general=SkinSupport, specific=model_Chart)
gen_model_CrossOut_Widget = Generalization(general=Widget, specific=model_CrossOut)
gen_model_CrossOut_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_CrossOut)
gen_model_CrossOut_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_CrossOut)
gen_model_CrossOut_SkinSupport = Generalization(general=SkinSupport, specific=model_CrossOut)
gen_model_CrossOut_AnnotationSupport = Generalization(general=AnnotationSupport, specific=model_CrossOut)
gen_model_Item_LinkSupport = Generalization(general=LinkSupport, specific=model_Item)
gen_model_Hotspot_Widget = Generalization(general=Widget, specific=model_Hotspot)
gen_model_Hotspot_LinkSupport = Generalization(general=LinkSupport, specific=model_Hotspot)
gen_model_Shape_IconPositionSupport = Generalization(general=IconPositionSupport, specific=model_Shape)
gen_model_Shape_FontSupport = Generalization(general=FontSupport, specific=model_Shape)
gen_model_Shape_LinkSupport = Generalization(general=LinkSupport, specific=model_Shape)
gen_model_Shape_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_Shape)
gen_model_Shape_LineStyleSupport = Generalization(general=LineStyleSupport, specific=model_Shape)
gen_model_Shape_SkinSupport = Generalization(general=SkinSupport, specific=model_Shape)
gen_model_Shape_RotationSupport = Generalization(general=RotationSupport, specific=model_Shape)
gen_model_SVGImage_Widget = Generalization(general=Widget, specific=model_SVGImage)
gen_model_SVGImage_LinkSupport = Generalization(general=LinkSupport, specific=model_SVGImage)
gen_model_SVGImage_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_SVGImage)
gen_model_Alert_Widget = Generalization(general=Widget, specific=model_Alert)
gen_model_Alert_IconSupport = Generalization(general=IconSupport, specific=model_Alert)
gen_model_SVGImage_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_SVGImage)
gen_model_Alert_ItemSupport = Generalization(general=ItemSupport, specific=model_Alert)
gen_model_Alert_FontSupport = Generalization(general=FontSupport, specific=model_Alert)
gen_model_SVGImage_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_SVGImage)
gen_model_Alert_SkinSupport = Generalization(general=SkinSupport, specific=model_Alert)
gen_model_SVGImage_RotationSupport = Generalization(general=RotationSupport, specific=model_SVGImage)
gen_model_SVGImage_FlipSupport = Generalization(general=FlipSupport, specific=model_SVGImage)
gen_model_Shape_Widget = Generalization(general=Widget, specific=model_Shape)
gen_model_Shape_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Shape)
gen_model_Shape_ColorAlphaSupport = Generalization(general=ColorAlphaSupport, specific=model_Shape)
gen_model_Shape_ColorForegroundSupport = Generalization(general=ColorForegroundSupport, specific=model_Shape)
gen_model_Shape_BorderSupport = Generalization(general=BorderSupport, specific=model_Shape)
gen_model_Shape_IconSupport = Generalization(general=IconSupport, specific=model_Shape)
gen_model_TextLinksSupport_ItemSupport = Generalization(general=ItemSupport, specific=model_TextLinksSupport)
gen_model_overrides_Overrides_WidgetContainerOverrides = Generalization(general=WidgetContainerOverrides, specific=model_overrides_Overrides)
gen_model_Switch_Widget = Generalization(general=Widget, specific=model_Switch)
gen_model_Switch_BooleanSelectionSupport = Generalization(general=BooleanSelectionSupport, specific=model_Switch)
gen_model_Switch_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_Switch)
gen_model_Switch_FontSupport = Generalization(general=FontSupport, specific=model_Switch)
gen_model_Switch_LinkSupport = Generalization(general=LinkSupport, specific=model_Switch)
gen_model_Switch_StateSupport = Generalization(general=StateSupport, specific=model_Switch)
gen_model_Switch_SkinSupport = Generalization(general=SkinSupport, specific=model_Switch)
gen_model_VButtonBar_Widget = Generalization(general=Widget, specific=model_VButtonBar)
gen_model_VButtonBar_SelectionSupport = Generalization(general=SelectionSupport, specific=model_VButtonBar)
gen_model_VButtonBar_FontSupport = Generalization(general=FontSupport, specific=model_VButtonBar)
gen_model_VButtonBar_TextAlignmentSupport = Generalization(general=TextAlignmentSupport, specific=model_VButtonBar)
gen_model_VButtonBar_ColorBackgroundSupport = Generalization(general=ColorBackgroundSupport, specific=model_VButtonBar)
gen_model_VButtonBar_ItemSupport = Generalization(general=ItemSupport, specific=model_VButtonBar)
gen_model_VButtonBar_SkinSupport = Generalization(general=SkinSupport, specific=model_VButtonBar)
gen_model_overrides_ItemOverrides_Reference = Generalization(general=Reference, specific=model_overrides_ItemOverrides)
gen_model_overrides_WidgetOverrides_overrides_WidgetContainerOverrides = Generalization(general=overrides_WidgetContainerOverrides, specific=model_overrides_WidgetOverrides)
gen_model_overrides_WidgetOverrides_overrides_Reference = Generalization(general=overrides_Reference, specific=model_overrides_WidgetOverrides)
gen_model_overrides_Move_overrides_Operation = Generalization(general=overrides_Operation, specific=model_overrides_Move)
gen_model_overrides_Move_overrides_Reference = Generalization(general=overrides_Reference, specific=model_overrides_Move)
gen_model_overrides_Delete_overrides_Operation = Generalization(general=overrides_Operation, specific=model_overrides_Delete)
gen_model_overrides_Delete_overrides_Reference = Generalization(general=overrides_Reference, specific=model_overrides_Delete)
gen_model_overrides_Insert_Operation = Generalization(general=Operation, specific=model_overrides_Insert)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Screen, WidgetContainer, NoteSupport, model_ScreenRuler, model_ScreenFont, model_RulerGuide, model_Widget, model_WidgetContainer, model_WidgetDescriptor, model_Button, Widget, StateSupport, ColorBackgroundSupport, FontSupport, IconSupport, LinkSupport, TextAlignmentSupport, SkinSupport, model_Checkbox, BooleanSelectionSupport, model_Combo, ColorBorderSupport, ColorAlphaSupport, ItemSupport, model_Placeholder, model_RadioButton, model_TextField, model_Spinner, model_Window, VerticalScrollbarSupport, model_Browser, model_Label, ColorForegroundSupport, IconPositionSupport, RotationSupport, TextLinksSupport, model_Link, model_Area, model_Panel, BorderStyleSupport, model_Group, model_List, SelectionSupport, BorderSupport, ListSupport, ColorAlternativeSupport, model_Popup, model_Menu, model_Table, model_Text, LineHeightSupport, model_Icon, model_TextArea, model_HScrollbar, ValueSupport, model_VScrollbar, model_HLine, LineStyleSupport, model_VLine, model_HSlider, model_VSlider, model_Tabs, model_Tree, model_Font, model_WidgetGroup, NameSupport, model_Master, model_Image, FlipSupport, model_FontSupport, model_ColorForegroundSupport, model_ColorBackgroundSupport, model_ColorBorderSupport, Overrides, model_TextAlignmentSupport, model_BooleanSelectionSupport, model_Note, AnnotationSupport, model_ProgressBar, model_Callout, model_SearchField, model_ColorAlphaSupport, model_SelectionSupport, model_ScratchOut, model_BorderSupport, model_StateSupport, model_Breadcrumbs, model_LinkBar, model_Tooltip, model_DateField, model_VideoPlayer, model_Map, model_CoverFlow, model_TabbedPane, model_IconSupport, model_Accordion, model_VerticalScrollbarSupport, model_ValueSupport, model_ColorPicker, model_Arrow, model_CurlyBrace, model_HSplitter, model_VSplitter, model_Circle, model_Rectangle, model_IconPositionSupport, model_ButtonBar, model_BorderStyleSupport, model_ColorAlternativeSupport, model_Chart, model_LineStyleSupport, model_CrossOut, model_RotationSupport, model_Item, model_FlipSupport, model_ItemSupport, model_LinkSupport, model_Hotspot, model_ListSupport, model_NameSupport, model_SVGImage, model_Alert, model_SkinSupport, model_Shape, model_AnnotationSupport, model_TextLinksSupport, model_NoteSupport, model_story_Storyboard, Panel, model_story_Panel, story_model_Screen, Storyboard, model_overrides_Overrides, WidgetContainerOverrides, WidgetOverrides, model_Switch, model_LineHeightSupport, model_VButtonBar, StringToStringMap, FontOverrides, ItemOverrides, Operation, model_overrides_FontOverrides, model_overrides_ItemOverrides, Reference, model_overrides_WidgetOverrides, overrides_WidgetContainerOverrides, overrides_Reference, model_overrides_WidgetContainerOverrides, model_overrides_StringToStringMap, model_overrides_Operation, model_overrides_Move, overrides_Operation, model_overrides_Delete, model_overrides_Insert, overrides_model_EObject, model_overrides_Reference, TextAlignment, IconSize, ResizeMode, State, Position, BorderStyle, ButtonStyle, LineStyle, ChartType, Theme, ShapeType, Rotation90},
    associations={hRuler0, vRuler1, font4, guides6, descriptor9, container8, widgets10, instance14, font17, screen11, overrides12, items18, panels19, screen20, story21, attributes24, font25, items27, itemChanges29, widgets23, widgetChanges32, object31},
    generalizations={gen_model_Screen_WidgetContainer, gen_model_Screen_NoteSupport, gen_model_Widget_NoteSupport, gen_model_Button_Widget, gen_model_Button_StateSupport, gen_model_Button_ColorBackgroundSupport, gen_model_Button_FontSupport, gen_model_Button_IconSupport, gen_model_Button_LinkSupport, gen_model_Button_TextAlignmentSupport, gen_model_Button_SkinSupport, gen_model_Checkbox_Widget, gen_model_Checkbox_BooleanSelectionSupport, gen_model_Checkbox_StateSupport, gen_model_Checkbox_LinkSupport, gen_model_Checkbox_FontSupport, gen_model_Checkbox_SkinSupport, gen_model_Combo_Widget, gen_model_Combo_StateSupport, gen_model_Combo_FontSupport, gen_model_Combo_ColorBorderSupport, gen_model_Combo_ColorBackgroundSupport, gen_model_Combo_ColorAlphaSupport, gen_model_Combo_LinkSupport, gen_model_Combo_ItemSupport, gen_model_Link_Widget, gen_model_Link_FontSupport, gen_model_Link_StateSupport, gen_model_Link_LinkSupport, gen_model_Link_SkinSupport, gen_model_Placeholder_Widget, gen_model_Placeholder_LinkSupport, gen_model_Placeholder_SkinSupport, gen_model_RadioButton_Widget, gen_model_RadioButton_BooleanSelectionSupport, gen_model_RadioButton_StateSupport, gen_model_RadioButton_LinkSupport, gen_model_RadioButton_FontSupport, gen_model_RadioButton_SkinSupport, gen_model_TextField_Widget, gen_model_TextField_StateSupport, gen_model_TextField_FontSupport, gen_model_TextField_TextAlignmentSupport, gen_model_TextField_ColorBackgroundSupport, gen_model_TextField_ColorAlphaSupport, gen_model_TextField_ColorBorderSupport, gen_model_TextField_SkinSupport, gen_model_Spinner_Widget, gen_model_Spinner_StateSupport, gen_model_Spinner_FontSupport, gen_model_Spinner_ColorBorderSupport, gen_model_Spinner_ColorBackgroundSupport, gen_model_Spinner_ColorAlphaSupport, gen_model_Spinner_SkinSupport, gen_model_Window_Widget, gen_model_Window_VerticalScrollbarSupport, gen_model_Window_SkinSupport, gen_model_Window_ColorBackgroundSupport, gen_model_Window_ColorAlphaSupport, gen_model_Browser_Widget, gen_model_Browser_VerticalScrollbarSupport, gen_model_Browser_ColorBackgroundSupport, gen_model_Browser_SkinSupport, gen_model_Browser_ColorAlphaSupport, gen_model_Combo_SkinSupport, gen_model_Label_Widget, gen_model_Label_FontSupport, gen_model_Label_TextAlignmentSupport, gen_model_Label_ColorForegroundSupport, gen_model_Label_StateSupport, gen_model_Label_IconSupport, gen_model_Label_IconPositionSupport, gen_model_Label_LinkSupport, gen_model_Label_RotationSupport, gen_model_Label_TextLinksSupport, gen_model_Area_Widget, gen_model_Panel_Widget, gen_model_Panel_ColorBackgroundSupport, gen_model_Panel_ColorAlphaSupport, gen_model_Panel_VerticalScrollbarSupport, gen_model_Panel_ColorForegroundSupport, gen_model_Panel_BorderStyleSupport, gen_model_Panel_LinkSupport, gen_model_Panel_SkinSupport, gen_model_Group_Widget, gen_model_Group_VerticalScrollbarSupport, gen_model_Group_ColorBackgroundSupport, gen_model_Group_ColorAlphaSupport, gen_model_Group_FontSupport, gen_model_Group_SkinSupport, gen_model_List_Widget, gen_model_List_SelectionSupport, gen_model_List_BorderSupport, gen_model_List_VerticalScrollbarSupport, gen_model_List_ColorBackgroundSupport, gen_model_List_ColorAlphaSupport, gen_model_List_ListSupport, gen_model_List_FontSupport, gen_model_List_ItemSupport, gen_model_List_ColorAlternativeSupport, gen_model_Popup_Widget, gen_model_Popup_SelectionSupport, gen_model_Popup_ItemSupport, gen_model_Menu_Widget, gen_model_Menu_SelectionSupport, gen_model_Menu_IconSupport, gen_model_Menu_ItemSupport, gen_model_Menu_SkinSupport, gen_model_Table_Widget, gen_model_Table_SelectionSupport, gen_model_Table_BorderSupport, gen_model_Table_VerticalScrollbarSupport, gen_model_Table_ColorBackgroundSupport, gen_model_Table_ColorAlphaSupport, gen_model_Table_ListSupport, gen_model_Table_FontSupport, gen_model_Table_TextAlignmentSupport, gen_model_Table_ColorAlternativeSupport, gen_model_Table_TextLinksSupport, gen_model_Browser_FontSupport, gen_model_Text_Widget, gen_model_Text_FontSupport, gen_model_Text_TextAlignmentSupport, gen_model_Text_ColorForegroundSupport, gen_model_Text_LinkSupport, gen_model_Text_LineHeightSupport, gen_model_Text_TextLinksSupport, gen_model_Tree_SelectionSupport, gen_model_Tree_ItemSupport, gen_model_Tree_FontSupport, gen_model_Icon_Widget, gen_model_Icon_ColorForegroundSupport, gen_model_Icon_IconSupport, gen_model_Icon_LinkSupport, gen_model_TextArea_Widget, gen_model_TextArea_StateSupport, gen_model_TextArea_VerticalScrollbarSupport, gen_model_TextArea_FontSupport, gen_model_TextArea_TextAlignmentSupport, gen_model_TextArea_ColorBackgroundSupport, gen_model_TextArea_ColorAlphaSupport, gen_model_TextArea_ColorBorderSupport, gen_model_TextArea_SkinSupport, gen_model_TextArea_LineHeightSupport, gen_model_TextArea_TextLinksSupport, gen_model_HScrollbar_Widget, gen_model_HScrollbar_ValueSupport, gen_model_HScrollbar_SkinSupport, gen_model_VScrollbar_Widget, gen_model_VScrollbar_ValueSupport, gen_model_VScrollbar_SkinSupport, gen_model_HLine_Widget, gen_model_HLine_ColorForegroundSupport, gen_model_HLine_LineStyleSupport, gen_model_HLine_SkinSupport, gen_model_VLine_Widget, gen_model_VLine_ColorForegroundSupport, gen_model_VLine_LineStyleSupport, gen_model_VLine_SkinSupport, gen_model_HSlider_Widget, gen_model_HSlider_ValueSupport, gen_model_HSlider_StateSupport, gen_model_HSlider_ColorBackgroundSupport, gen_model_HSlider_SkinSupport, gen_model_VSlider_Widget, gen_model_VSlider_ValueSupport, gen_model_VSlider_StateSupport, gen_model_VSlider_ColorBackgroundSupport, gen_model_VSlider_SkinSupport, gen_model_Tabs_Widget, gen_model_Tabs_SelectionSupport, gen_model_Tabs_ItemSupport, gen_model_Tabs_FontSupport, gen_model_Tabs_SkinSupport, gen_model_Tree_Widget, gen_model_Tree_BorderSupport, gen_model_Tree_VerticalScrollbarSupport, gen_model_Tree_ColorBackgroundSupport, gen_model_Tree_ColorAlphaSupport, gen_model_WidgetGroup_Widget, gen_model_WidgetGroup_WidgetContainer, gen_model_WidgetGroup_LinkSupport, gen_model_WidgetGroup_NameSupport, gen_model_Master_Widget, gen_model_Master_LinkSupport, gen_model_Image_Widget, gen_model_Image_LinkSupport, gen_model_Image_RotationSupport, gen_model_Image_FlipSupport, gen_model_Image_BorderSupport, gen_model_Note_Widget, gen_model_Note_FontSupport, gen_model_Note_TextAlignmentSupport, gen_model_Note_ColorBackgroundSupport, gen_model_Note_ColorAlphaSupport, gen_model_Note_LinkSupport, gen_model_Note_SkinSupport, gen_model_Note_AnnotationSupport, gen_model_Note_TextLinksSupport, gen_model_ProgressBar_Widget, gen_model_ProgressBar_ValueSupport, gen_model_ProgressBar_ColorBackgroundSupport, gen_model_ProgressBar_SkinSupport, gen_model_Callout_Widget, gen_model_Callout_FontSupport, gen_model_Callout_ColorBackgroundSupport, gen_model_Callout_ColorAlphaSupport, gen_model_Callout_LinkSupport, gen_model_Callout_SkinSupport, gen_model_Callout_AnnotationSupport, gen_model_SearchField_Widget, gen_model_SearchField_FontSupport, gen_model_SearchField_StateSupport, gen_model_SearchField_ColorBorderSupport, gen_model_SearchField_LinkSupport, gen_model_SearchField_SkinSupport, gen_model_Tooltip_TextLinksSupport, gen_model_ScratchOut_Widget, gen_model_ScratchOut_ColorForegroundSupport, gen_model_ScratchOut_ColorAlphaSupport, gen_model_ScratchOut_SkinSupport, gen_model_ScratchOut_AnnotationSupport, gen_model_Breadcrumbs_Widget, gen_model_Breadcrumbs_FontSupport, gen_model_Breadcrumbs_ItemSupport, gen_model_Breadcrumbs_SkinSupport, gen_model_LinkBar_Widget, gen_model_LinkBar_FontSupport, gen_model_LinkBar_SelectionSupport, gen_model_LinkBar_ItemSupport, gen_model_LinkBar_SkinSupport, gen_model_Tooltip_Widget, gen_model_Tooltip_FontSupport, gen_model_Tooltip_TextAlignmentSupport, gen_model_Tooltip_ColorBackgroundSupport, gen_model_Tooltip_SkinSupport, gen_model_DateField_Widget, gen_model_DateField_StateSupport, gen_model_DateField_ColorBorderSupport, gen_model_DateField_ColorBackgroundSupport, gen_model_DateField_ColorAlphaSupport, gen_model_DateField_SkinSupport, gen_model_VideoPlayer_Widget, gen_model_VideoPlayer_SkinSupport, gen_model_Map_Widget, gen_model_Map_SkinSupport, gen_model_CoverFlow_Widget, gen_model_CoverFlow_SkinSupport, gen_model_TabbedPane_Widget, gen_model_TabbedPane_SelectionSupport, gen_model_TabbedPane_VerticalScrollbarSupport, gen_model_TabbedPane_ColorBackgroundSupport, gen_model_TabbedPane_ColorAlphaSupport, gen_model_TabbedPane_ItemSupport, gen_model_TabbedPane_FontSupport, gen_model_TabbedPane_SkinSupport, gen_model_Accordion_Widget, gen_model_Accordion_SelectionSupport, gen_model_Accordion_VerticalScrollbarSupport, gen_model_Accordion_ItemSupport, gen_model_Accordion_FontSupport, gen_model_VerticalScrollbarSupport_ValueSupport, gen_model_VSplitter_SkinSupport, gen_model_ColorPicker_Widget, gen_model_ColorPicker_ColorBackgroundSupport, gen_model_ColorPicker_SkinSupport, gen_model_Arrow_Widget, gen_model_Arrow_ColorForegroundSupport, gen_model_Arrow_LineStyleSupport, gen_model_Arrow_AnnotationSupport, gen_model_CurlyBrace_Widget, gen_model_CurlyBrace_FontSupport, gen_model_CurlyBrace_ColorForegroundSupport, gen_model_CurlyBrace_SkinSupport, gen_model_CurlyBrace_AnnotationSupport, gen_model_CurlyBrace_TextLinksSupport, gen_model_HSplitter_Widget, gen_model_HSplitter_SkinSupport, gen_model_VSplitter_Widget, gen_model_Circle_Widget, gen_model_Circle_ColorBackgroundSupport, gen_model_Circle_ColorAlphaSupport, gen_model_Circle_ColorForegroundSupport, gen_model_Circle_BorderSupport, gen_model_Circle_IconSupport, gen_model_Circle_IconPositionSupport, gen_model_Circle_FontSupport, gen_model_Circle_LinkSupport, gen_model_Circle_TextAlignmentSupport, gen_model_Circle_LineStyleSupport, gen_model_Rectangle_Widget, gen_model_Rectangle_ColorBackgroundSupport, gen_model_Rectangle_ColorAlphaSupport, gen_model_Rectangle_ColorForegroundSupport, gen_model_Rectangle_BorderStyleSupport, gen_model_Rectangle_IconSupport, gen_model_Rectangle_IconPositionSupport, gen_model_Rectangle_FontSupport, gen_model_Rectangle_LinkSupport, gen_model_Rectangle_TextAlignmentSupport, gen_model_IconPositionSupport_IconSupport, gen_model_ButtonBar_Widget, gen_model_ButtonBar_SelectionSupport, gen_model_ButtonBar_FontSupport, gen_model_ButtonBar_ColorBackgroundSupport, gen_model_ButtonBar_ItemSupport, gen_model_ButtonBar_SkinSupport, gen_model_Chart_Widget, gen_model_Chart_SkinSupport, gen_model_CrossOut_Widget, gen_model_CrossOut_ColorForegroundSupport, gen_model_CrossOut_ColorAlphaSupport, gen_model_CrossOut_SkinSupport, gen_model_CrossOut_AnnotationSupport, gen_model_Item_LinkSupport, gen_model_Hotspot_Widget, gen_model_Hotspot_LinkSupport, gen_model_Shape_IconPositionSupport, gen_model_Shape_FontSupport, gen_model_Shape_LinkSupport, gen_model_Shape_TextAlignmentSupport, gen_model_Shape_LineStyleSupport, gen_model_Shape_SkinSupport, gen_model_Shape_RotationSupport, gen_model_SVGImage_Widget, gen_model_SVGImage_LinkSupport, gen_model_SVGImage_ColorBackgroundSupport, gen_model_Alert_Widget, gen_model_Alert_IconSupport, gen_model_SVGImage_ColorForegroundSupport, gen_model_Alert_ItemSupport, gen_model_Alert_FontSupport, gen_model_SVGImage_ColorAlphaSupport, gen_model_Alert_SkinSupport, gen_model_SVGImage_RotationSupport, gen_model_SVGImage_FlipSupport, gen_model_Shape_Widget, gen_model_Shape_ColorBackgroundSupport, gen_model_Shape_ColorAlphaSupport, gen_model_Shape_ColorForegroundSupport, gen_model_Shape_BorderSupport, gen_model_Shape_IconSupport, gen_model_TextLinksSupport_ItemSupport, gen_model_overrides_Overrides_WidgetContainerOverrides, gen_model_Switch_Widget, gen_model_Switch_BooleanSelectionSupport, gen_model_Switch_ColorBackgroundSupport, gen_model_Switch_FontSupport, gen_model_Switch_LinkSupport, gen_model_Switch_StateSupport, gen_model_Switch_SkinSupport, gen_model_VButtonBar_Widget, gen_model_VButtonBar_SelectionSupport, gen_model_VButtonBar_FontSupport, gen_model_VButtonBar_TextAlignmentSupport, gen_model_VButtonBar_ColorBackgroundSupport, gen_model_VButtonBar_ItemSupport, gen_model_VButtonBar_SkinSupport, gen_model_overrides_ItemOverrides_Reference, gen_model_overrides_WidgetOverrides_overrides_WidgetContainerOverrides, gen_model_overrides_WidgetOverrides_overrides_Reference, gen_model_overrides_Move_overrides_Operation, gen_model_overrides_Move_overrides_Reference, gen_model_overrides_Delete_overrides_Operation, gen_model_overrides_Delete_overrides_Reference, gen_model_overrides_Insert_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)