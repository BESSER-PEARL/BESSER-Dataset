from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class viewers_ViewerInputs:

    pass
class viewers_TreeViewerElement:

    def __init__(self, label: str, viewers_TreeViewerElement: "viewers_TreeViewerInput" = None, viewers_TreeViewerElement5: "viewers_TreeViewerElement" = None, viewers_TreeViewerElement3: set["viewers_TreeViewerElement"] = None):
        self.label = label
        self.viewers_TreeViewerElement = viewers_TreeViewerElement
        self.viewers_TreeViewerElement5 = viewers_TreeViewerElement5
        self.viewers_TreeViewerElement3 = viewers_TreeViewerElement3 if viewers_TreeViewerElement3 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def viewers_TreeViewerElement(self):
        return self.__viewers_TreeViewerElement

    @viewers_TreeViewerElement.setter
    def viewers_TreeViewerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewers_TreeViewerElement__viewers_TreeViewerElement", None)
        self.__viewers_TreeViewerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewers_TreeViewerInput"):
                opp_val = getattr(old_value, "viewers_TreeViewerInput", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewers_TreeViewerInput"):
                opp_val = getattr(value, "viewers_TreeViewerInput", None)
                if opp_val is None:
                    setattr(value, "viewers_TreeViewerInput", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewers_TreeViewerElement3(self):
        return self.__viewers_TreeViewerElement3

    @viewers_TreeViewerElement3.setter
    def viewers_TreeViewerElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewers_TreeViewerElement__viewers_TreeViewerElement3", None)
        self.__viewers_TreeViewerElement3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewers_TreeViewerElement5"):
                    opp_val = getattr(item, "viewers_TreeViewerElement5", None)
                    
                    if opp_val == self:
                        setattr(item, "viewers_TreeViewerElement5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewers_TreeViewerElement5"):
                    opp_val = getattr(item, "viewers_TreeViewerElement5", None)
                    
                    setattr(item, "viewers_TreeViewerElement5", self)
                    

    @property
    def viewers_TreeViewerElement5(self):
        return self.__viewers_TreeViewerElement5

    @viewers_TreeViewerElement5.setter
    def viewers_TreeViewerElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewers_TreeViewerElement__viewers_TreeViewerElement5", None)
        self.__viewers_TreeViewerElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewers_TreeViewerElement3"):
                opp_val = getattr(old_value, "viewers_TreeViewerElement3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewers_TreeViewerElement3"):
                opp_val = getattr(value, "viewers_TreeViewerElement3", None)
                if opp_val is None:
                    setattr(value, "viewers_TreeViewerElement3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewers_TreeViewerInput:

    pass
class viewers_TableViewerElement:

    def __init__(self, name: str, label: str, viewers_TableViewerElement: "viewers_TableViewerInput" = None):
        self.name = name
        self.label = label
        self.viewers_TableViewerElement = viewers_TableViewerElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def viewers_TableViewerElement(self):
        return self.__viewers_TableViewerElement

    @viewers_TableViewerElement.setter
    def viewers_TableViewerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewers_TableViewerElement__viewers_TableViewerElement", None)
        self.__viewers_TableViewerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewers_TableViewerInput"):
                opp_val = getattr(old_value, "viewers_TableViewerInput", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewers_TableViewerInput"):
                opp_val = getattr(value, "viewers_TableViewerInput", None)
                if opp_val is None:
                    setattr(value, "viewers_TableViewerInput", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewers_TableViewerInput:

    pass
class viewers_ListViewerElement:

    def __init__(self, label: str, viewers_ListViewerElement: "viewers_ListViewerInput" = None):
        self.label = label
        self.viewers_ListViewerElement = viewers_ListViewerElement
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def viewers_ListViewerElement(self):
        return self.__viewers_ListViewerElement

    @viewers_ListViewerElement.setter
    def viewers_ListViewerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewers_ListViewerElement__viewers_ListViewerElement", None)
        self.__viewers_ListViewerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewers_ListViewerInput"):
                opp_val = getattr(old_value, "viewers_ListViewerInput", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewers_ListViewerInput"):
                opp_val = getattr(value, "viewers_ListViewerInput", None)
                if opp_val is None:
                    setattr(value, "viewers_ListViewerInput", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewers_ListViewerInput:

    pass