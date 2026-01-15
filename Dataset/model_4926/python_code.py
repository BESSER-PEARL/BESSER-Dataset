from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class bootstrap_Widget(ABC):

    def __init__(self, title: str, widgets: "bootstrap_Section" = None, Widget: "bootstrap_Section" = None):
        self.title = title
        self.widgets = widgets
        self.Widget = Widget
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Widget(self):
        return self.__Widget

    @Widget.setter
    def Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Widget__Widget", None)
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

    @property
    def widgets(self):
        return self.__widgets

    @widgets.setter
    def widgets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Widget__widgets", None)
        self.__widgets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Section11"):
                opp_val = getattr(old_value, "Section11", None)
                if opp_val == self:
                    setattr(old_value, "Section11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Section11"):
                opp_val = getattr(value, "Section11", None)
                setattr(value, "Section11", self)

class FormWidget:

    pass
class bootstrap_Spinner(FormWidget):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class bootstrap_CheckBox(FormWidget):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class bootstrap_TextArea(FormWidget):

    pass
class bootstrap_FormWidget(ABC):

    def __init__(self, label: str, FormWidget: "bootstrap_Form" = None, formWidgets: "bootstrap_Form" = None):
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
        old_value = getattr(self, f"_bootstrap_FormWidget__formWidgets", None)
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
        old_value = getattr(self, f"_bootstrap_FormWidget__FormWidget", None)
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
class bootstrap_Video(Widget):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class bootstrap_Text(Widget):

    def __init__(self, columnNumber: int):
        self.columnNumber = columnNumber
        
    @property
    def columnNumber(self) -> int:
        return self.__columnNumber

    @columnNumber.setter
    def columnNumber(self, columnNumber: int):
        self.__columnNumber = columnNumber

class bootstrap_Gallery(Widget):

    def __init__(self, imagesPath: str):
        self.imagesPath = imagesPath
        
    @property
    def imagesPath(self) -> str:
        return self.__imagesPath

    @imagesPath.setter
    def imagesPath(self, imagesPath: str):
        self.__imagesPath = imagesPath

class bootstrap_ImagesBlock(Widget):

    def __init__(self, imagesPath: str):
        self.imagesPath = imagesPath
        
    @property
    def imagesPath(self) -> str:
        return self.__imagesPath

    @imagesPath.setter
    def imagesPath(self, imagesPath: str):
        self.__imagesPath = imagesPath

class bootstrap_Table(Widget):

    def __init__(self, columnNames: str, rowNames: str, striped: bool, bordered: bool):
        self.columnNames = columnNames
        self.rowNames = rowNames
        self.striped = striped
        self.bordered = bordered
        
    @property
    def rowNames(self) -> str:
        return self.__rowNames

    @rowNames.setter
    def rowNames(self, rowNames: str):
        self.__rowNames = rowNames

    @property
    def bordered(self) -> bool:
        return self.__bordered

    @bordered.setter
    def bordered(self, bordered: bool):
        self.__bordered = bordered

    @property
    def columnNames(self) -> str:
        return self.__columnNames

    @columnNames.setter
    def columnNames(self, columnNames: str):
        self.__columnNames = columnNames

    @property
    def striped(self) -> bool:
        return self.__striped

    @striped.setter
    def striped(self, striped: bool):
        self.__striped = striped

class bootstrap_Form(Widget):

    pass
class bootstrap_Section:

    def __init__(self, title: str, description: str, Section11: "bootstrap_Widget" = None, Section: "bootstrap_Page" = None, section: set["bootstrap_Widget"] = None, sections: "bootstrap_Page" = None):
        self.title = title
        self.description = description
        self.Section11 = Section11
        self.Section = Section
        self.section = section if section is not None else set()
        self.sections = sections
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Section(self):
        return self.__Section

    @Section.setter
    def Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Section__Section", None)
        self.__Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page"):
                opp_val = getattr(old_value, "page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page"):
                opp_val = getattr(value, "page", None)
                if opp_val is None:
                    setattr(value, "page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Section__section", None)
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
                    

    @property
    def sections(self):
        return self.__sections

    @sections.setter
    def sections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Section__sections", None)
        self.__sections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page9"):
                opp_val = getattr(old_value, "Page9", None)
                if opp_val == self:
                    setattr(old_value, "Page9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page9"):
                opp_val = getattr(value, "Page9", None)
                setattr(value, "Page9", self)

    @property
    def Section11(self):
        return self.__Section11

    @Section11.setter
    def Section11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Section__Section11", None)
        self.__Section11 = value
        
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

class bootstrap_MainPage:

    def __init__(self, title: str, description: str, MainPage: "bootstrap_Site" = None, mainPage: "bootstrap_Site" = None):
        self.title = title
        self.description = description
        self.MainPage = MainPage
        self.mainPage = mainPage
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def mainPage(self):
        return self.__mainPage

    @mainPage.setter
    def mainPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_MainPage__mainPage", None)
        self.__mainPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Site6"):
                opp_val = getattr(old_value, "Site6", None)
                if opp_val == self:
                    setattr(old_value, "Site6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Site6"):
                opp_val = getattr(value, "Site6", None)
                setattr(value, "Site6", self)

    @property
    def MainPage(self):
        return self.__MainPage

    @MainPage.setter
    def MainPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_MainPage__MainPage", None)
        self.__MainPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "site2"):
                opp_val = getattr(old_value, "site2", None)
                if opp_val == self:
                    setattr(old_value, "site2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "site2"):
                opp_val = getattr(value, "site2", None)
                setattr(value, "site2", self)

class bootstrap_Page:

    def __init__(self, title: str, description: str, name: str, Page: "bootstrap_Site" = None, page: set["bootstrap_Section"] = None, pages: "bootstrap_Site" = None, Page9: "bootstrap_Section" = None):
        self.title = title
        self.description = description
        self.name = name
        self.Page = Page
        self.page = page if page is not None else set()
        self.pages = pages
        self.Page9 = Page9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "site"):
                opp_val = getattr(old_value, "site", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "site"):
                opp_val = getattr(value, "site", None)
                if opp_val is None:
                    setattr(value, "site", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Page__page", None)
        self.__page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Section"):
                    opp_val = getattr(item, "Section", None)
                    
                    if opp_val == self:
                        setattr(item, "Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Section"):
                    opp_val = getattr(item, "Section", None)
                    
                    setattr(item, "Section", self)
                    

    @property
    def Page9(self):
        return self.__Page9

    @Page9.setter
    def Page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Page__Page9", None)
        self.__Page9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sections"):
                opp_val = getattr(old_value, "sections", None)
                if opp_val == self:
                    setattr(old_value, "sections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sections"):
                opp_val = getattr(value, "sections", None)
                setattr(value, "sections", self)

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Site"):
                opp_val = getattr(old_value, "Site", None)
                if opp_val == self:
                    setattr(old_value, "Site", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Site"):
                opp_val = getattr(value, "Site", None)
                setattr(value, "Site", self)

class bootstrap_Site:

    def __init__(self, title: str, site: set["bootstrap_Page"] = None, site2: "bootstrap_MainPage" = None, Site: "bootstrap_Page" = None, Site6: "bootstrap_MainPage" = None):
        self.title = title
        self.site = site if site is not None else set()
        self.site2 = site2
        self.Site = Site
        self.Site6 = Site6
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Site6(self):
        return self.__Site6

    @Site6.setter
    def Site6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Site__Site6", None)
        self.__Site6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mainPage"):
                opp_val = getattr(old_value, "mainPage", None)
                if opp_val == self:
                    setattr(old_value, "mainPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mainPage"):
                opp_val = getattr(value, "mainPage", None)
                setattr(value, "mainPage", self)

    @property
    def site2(self):
        return self.__site2

    @site2.setter
    def site2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Site__site2", None)
        self.__site2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MainPage"):
                opp_val = getattr(old_value, "MainPage", None)
                if opp_val == self:
                    setattr(old_value, "MainPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MainPage"):
                opp_val = getattr(value, "MainPage", None)
                setattr(value, "MainPage", self)

    @property
    def Site(self):
        return self.__Site

    @Site.setter
    def Site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Site__Site", None)
        self.__Site = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages"):
                opp_val = getattr(old_value, "pages", None)
                if opp_val == self:
                    setattr(old_value, "pages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages"):
                opp_val = getattr(value, "pages", None)
                setattr(value, "pages", self)

    @property
    def site(self):
        return self.__site

    @site.setter
    def site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bootstrap_Site__site", None)
        self.__site = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    if opp_val == self:
                        setattr(item, "Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    setattr(item, "Page", self)
                    
