from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FormWidget:

    pass
class webapp_Spinner(FormWidget):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class webapp_TextArea(FormWidget):

    pass
class webapp_CheckBox(FormWidget):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class webapp_Section:

    def __init__(self, title: str, description: str, section: set["webapp_Widget"] = None, sections: "webapp_StaticView" = None, Section38: "webapp_Widget" = None, Section: "webapp_StaticView" = None):
        self.title = title
        self.description = description
        self.section = section if section is not None else set()
        self.sections = sections
        self.Section38 = Section38
        self.Section = Section
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Section(self):
        return self.__Section

    @Section.setter
    def Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Section__Section", None)
        self.__Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view"):
                opp_val = getattr(old_value, "view", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view"):
                opp_val = getattr(value, "view", None)
                if opp_val is None:
                    setattr(value, "view", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sections(self):
        return self.__sections

    @sections.setter
    def sections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Section__sections", None)
        self.__sections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticView"):
                opp_val = getattr(old_value, "StaticView", None)
                if opp_val == self:
                    setattr(old_value, "StaticView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticView"):
                opp_val = getattr(value, "StaticView", None)
                setattr(value, "StaticView", self)

    @property
    def Section38(self):
        return self.__Section38

    @Section38.setter
    def Section38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Section__Section38", None)
        self.__Section38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "widgets"):
                opp_val = getattr(old_value, "widgets", None)
                if opp_val == self:
                    setattr(old_value, "widgets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "widgets"):
                opp_val = getattr(value, "widgets", None)
                setattr(value, "widgets", self)

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Section__section", None)
        self.__section = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Widget"):
                    opp_val = getattr(item, "Widget", None)
                    
                    if opp_val == self:
                        setattr(item, "Widget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Widget"):
                    opp_val = getattr(item, "Widget", None)
                    
                    setattr(item, "Widget", self)
                    

class AbstractView:

    pass
class webapp_StaticView(AbstractView):

    pass
class webapp_ModelView(AbstractView):

    pass
class webapp_FormWidget(ABC):

    def __init__(self, label: str, FormWidget: "webapp_Form" = None, formWidgets: "webapp_Form" = None):
        self.label = label
        self.FormWidget = FormWidget
        self.formWidgets = formWidgets
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def formWidgets(self):
        return self.__formWidgets

    @formWidgets.setter
    def formWidgets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_FormWidget__formWidgets", None)
        self.__formWidgets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Form"):
                opp_val = getattr(old_value, "Form", None)
                if opp_val == self:
                    setattr(old_value, "Form", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Form"):
                opp_val = getattr(value, "Form", None)
                setattr(value, "Form", self)

    @property
    def FormWidget(self):
        return self.__FormWidget

    @FormWidget.setter
    def FormWidget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_FormWidget__FormWidget", None)
        self.__FormWidget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form"):
                opp_val = getattr(old_value, "form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form"):
                opp_val = getattr(value, "form", None)
                if opp_val is None:
                    setattr(value, "form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Widget:

    pass
class webapp_ImagesBlock(Widget):

    def __init__(self, imagesPath: str):
        self.imagesPath = imagesPath
        
    @property
    def imagesPath(self) -> str:
        return self.__imagesPath

    @imagesPath.setter
    def imagesPath(self, imagesPath: str):
        self.__imagesPath = imagesPath

class webapp_Video(Widget):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class webapp_Text(Widget):

    def __init__(self, columnNumber: int):
        self.columnNumber = columnNumber
        
    @property
    def columnNumber(self) -> int:
        return self.__columnNumber

    @columnNumber.setter
    def columnNumber(self, columnNumber: int):
        self.__columnNumber = columnNumber

class webapp_Gallery(Widget):

    def __init__(self, imagesPath: str):
        self.imagesPath = imagesPath
        
    @property
    def imagesPath(self) -> str:
        return self.__imagesPath

    @imagesPath.setter
    def imagesPath(self, imagesPath: str):
        self.__imagesPath = imagesPath

class webapp_Table(Widget):

    def __init__(self, columnNames: str, rowNames: str, striped: bool, bordered: bool):
        self.columnNames = columnNames
        self.rowNames = rowNames
        self.striped = striped
        self.bordered = bordered
        
    @property
    def bordered(self) -> bool:
        return self.__bordered

    @bordered.setter
    def bordered(self, bordered: bool):
        self.__bordered = bordered

    @property
    def striped(self) -> bool:
        return self.__striped

    @striped.setter
    def striped(self, striped: bool):
        self.__striped = striped

    @property
    def columnNames(self) -> str:
        return self.__columnNames

    @columnNames.setter
    def columnNames(self, columnNames: str):
        self.__columnNames = columnNames

    @property
    def rowNames(self) -> str:
        return self.__rowNames

    @rowNames.setter
    def rowNames(self, rowNames: str):
        self.__rowNames = rowNames

class webapp_Form(Widget):

    pass
class webapp_Widget(ABC):

    def __init__(self, title: str, Widget: "webapp_Section" = None, widgets: "webapp_Section" = None):
        self.title = title
        self.Widget = Widget
        self.widgets = widgets
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def widgets(self):
        return self.__widgets

    @widgets.setter
    def widgets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Widget__widgets", None)
        self.__widgets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Section38"):
                opp_val = getattr(old_value, "Section38", None)
                if opp_val == self:
                    setattr(old_value, "Section38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Section38"):
                opp_val = getattr(value, "Section38", None)
                setattr(value, "Section38", self)

    @property
    def Widget(self):
        return self.__Widget

    @Widget.setter
    def Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Widget__Widget", None)
        self.__Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "section"):
                opp_val = getattr(old_value, "section", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "section"):
                opp_val = getattr(value, "section", None)
                if opp_val is None:
                    setattr(value, "section", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_RouterMapping:

    def __init__(self, path: str, webapp_RouterMapping: "webapp_Router" = None, webapp_RouterMapping26: "webapp_AbstractView" = None):
        self.path = path
        self.webapp_RouterMapping = webapp_RouterMapping
        self.webapp_RouterMapping26 = webapp_RouterMapping26
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def webapp_RouterMapping26(self):
        return self.__webapp_RouterMapping26

    @webapp_RouterMapping26.setter
    def webapp_RouterMapping26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_RouterMapping__webapp_RouterMapping26", None)
        self.__webapp_RouterMapping26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_AbstractView"):
                opp_val = getattr(old_value, "webapp_AbstractView", None)
                if opp_val == self:
                    setattr(old_value, "webapp_AbstractView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_AbstractView"):
                opp_val = getattr(value, "webapp_AbstractView", None)
                setattr(value, "webapp_AbstractView", self)

    @property
    def webapp_RouterMapping(self):
        return self.__webapp_RouterMapping

    @webapp_RouterMapping.setter
    def webapp_RouterMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_RouterMapping__webapp_RouterMapping", None)
        self.__webapp_RouterMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Router"):
                opp_val = getattr(old_value, "webapp_Router", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Router"):
                opp_val = getattr(value, "webapp_Router", None)
                if opp_val is None:
                    setattr(value, "webapp_Router", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class webapp_Operation(NamedElement):

    pass
class webapp_Model(NamedElement):

    pass
class webapp_Attribute(NamedElement):

    def __init__(self, defaultValue: str, webapp_Attribute: "webapp_Model" = None):
        self.defaultValue = defaultValue
        self.webapp_Attribute = webapp_Attribute
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def webapp_Attribute(self):
        return self.__webapp_Attribute

    @webapp_Attribute.setter
    def webapp_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute", None)
        self.__webapp_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model"):
                opp_val = getattr(old_value, "webapp_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model"):
                opp_val = getattr(value, "webapp_Model", None)
                if opp_val is None:
                    setattr(value, "webapp_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Parameter(NamedElement):

    pass
class webapp_AbstractView(NamedElement):

    def __init__(self, description: str, AbstractView: "webapp_Application" = None, webapp_AbstractView: "webapp_RouterMapping" = None, webapp_AbstractView28: set["webapp_Operation"] = None, views: "webapp_Application" = None):
        self.description = description
        self.AbstractView = AbstractView
        self.webapp_AbstractView = webapp_AbstractView
        self.webapp_AbstractView28 = webapp_AbstractView28 if webapp_AbstractView28 is not None else set()
        self.views = views
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_AbstractView__views", None)
        self.__views = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application31"):
                opp_val = getattr(old_value, "Application31", None)
                if opp_val == self:
                    setattr(old_value, "Application31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application31"):
                opp_val = getattr(value, "Application31", None)
                setattr(value, "Application31", self)

    @property
    def AbstractView(self):
        return self.__AbstractView

    @AbstractView.setter
    def AbstractView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_AbstractView__AbstractView", None)
        self.__AbstractView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application4"):
                opp_val = getattr(old_value, "application4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application4"):
                opp_val = getattr(value, "application4", None)
                if opp_val is None:
                    setattr(value, "application4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_AbstractView28(self):
        return self.__webapp_AbstractView28

    @webapp_AbstractView28.setter
    def webapp_AbstractView28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_AbstractView__webapp_AbstractView28", None)
        self.__webapp_AbstractView28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Operation29"):
                    opp_val = getattr(item, "webapp_Operation29", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Operation29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Operation29"):
                    opp_val = getattr(item, "webapp_Operation29", None)
                    
                    setattr(item, "webapp_Operation29", self)
                    

    @property
    def webapp_AbstractView(self):
        return self.__webapp_AbstractView

    @webapp_AbstractView.setter
    def webapp_AbstractView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_AbstractView__webapp_AbstractView", None)
        self.__webapp_AbstractView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_RouterMapping26"):
                opp_val = getattr(old_value, "webapp_RouterMapping26", None)
                if opp_val == self:
                    setattr(old_value, "webapp_RouterMapping26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_RouterMapping26"):
                opp_val = getattr(value, "webapp_RouterMapping26", None)
                setattr(value, "webapp_RouterMapping26", self)

class webapp_Router(NamedElement):

    pass
class webapp_Reference(NamedElement):

    pass
class webapp_Collection(NamedElement):

    pass
class webapp_Application(NamedElement):

    pass
class webapp_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
