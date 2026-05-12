from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class stylesheets_Theme:

    def __init__(self, id: str, label: str, icon: str, stylesheets_Theme3: set["stylesheets_StyleSheet"] = None, stylesheets_Theme: "stylesheets_WorkspaceThemes" = None):
        self.id = id
        self.label = label
        self.icon = icon
        self.stylesheets_Theme3 = stylesheets_Theme3 if stylesheets_Theme3 is not None else set()
        self.stylesheets_Theme = stylesheets_Theme
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def stylesheets_Theme(self):
        return self.__stylesheets_Theme

    @stylesheets_Theme.setter
    def stylesheets_Theme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stylesheets_Theme__stylesheets_Theme", None)
        self.__stylesheets_Theme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stylesheets_WorkspaceThemes"):
                opp_val = getattr(old_value, "stylesheets_WorkspaceThemes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stylesheets_WorkspaceThemes"):
                opp_val = getattr(value, "stylesheets_WorkspaceThemes", None)
                if opp_val is None:
                    setattr(value, "stylesheets_WorkspaceThemes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stylesheets_Theme3(self):
        return self.__stylesheets_Theme3

    @stylesheets_Theme3.setter
    def stylesheets_Theme3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stylesheets_Theme__stylesheets_Theme3", None)
        self.__stylesheets_Theme3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stylesheets_StyleSheet4"):
                    opp_val = getattr(item, "stylesheets_StyleSheet4", None)
                    
                    if opp_val == self:
                        setattr(item, "stylesheets_StyleSheet4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stylesheets_StyleSheet4"):
                    opp_val = getattr(item, "stylesheets_StyleSheet4", None)
                    
                    setattr(item, "stylesheets_StyleSheet4", self)
                    

class stylesheets_StyleSheet(ABC):

    pass
class EModelElement:

    pass
class stylesheets_WorkspaceThemes(EModelElement):

    pass
class stylesheets_ModelStyleSheets(EModelElement):

    pass
class StyleSheet:

    pass
class stylesheets_EmbeddedStyleSheet(StyleSheet):

    def __init__(self, label: str, content: str):
        self.label = label
        self.content = content
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class stylesheets_StyleSheetReference(StyleSheet):

    def __init__(self, path: str):
        self.path = path
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

