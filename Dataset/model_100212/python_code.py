from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class documentation_TableRow:

    def __init__(self, rowCells: str, documentation_TableRow: "documentation_Table" = None):
        self.rowCells = rowCells
        self.documentation_TableRow = documentation_TableRow
        
        pass
    @property
    def rowCells(self):
        return self.__rowCells

    @rowCells.setter
    def rowCells(self, rowCells: str):
        self.__rowCells = rowCells


    @property
    def documentation_TableRow(self):
        return self.__documentation_TableRow

    @documentation_TableRow.setter
    def documentation_TableRow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_TableRow__documentation_TableRow", None)
        self.__documentation_TableRow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_Table7"):
                opp_val = getattr(old_value, "documentation_Table7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_Table7"):
                opp_val = getattr(value, "documentation_Table7", None)
                if opp_val is None:
                    setattr(value, "documentation_Table7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class documentation_TableHeader:

    def __init__(self, headerCells: str, documentation_TableHeader: "documentation_Table" = None):
        self.headerCells = headerCells
        self.documentation_TableHeader = documentation_TableHeader
        
        pass
    @property
    def headerCells(self):
        return self.__headerCells

    @headerCells.setter
    def headerCells(self, headerCells: str):
        self.__headerCells = headerCells


    @property
    def documentation_TableHeader(self):
        return self.__documentation_TableHeader

    @documentation_TableHeader.setter
    def documentation_TableHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_TableHeader__documentation_TableHeader", None)
        self.__documentation_TableHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_Table"):
                opp_val = getattr(old_value, "documentation_Table", None)
                if opp_val == self:
                    setattr(old_value, "documentation_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_Table"):
                opp_val = getattr(value, "documentation_Table", None)
                setattr(value, "documentation_Table", self)

class documentation_NamedElement(ABC):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class documentation_Fragment(ABC):

    pass
class documentation_TextFragmentContainer(ABC):

    pass
class documentation_Documentation:

    def __init__(self, title: str, documentation_Documentation: set["documentation_Section"] = None, documentation_Documentation2: set["documentation_TermEntry"] = None):
        self.title = title
        self.documentation_Documentation = documentation_Documentation if documentation_Documentation is not None else set()
        self.documentation_Documentation2 = documentation_Documentation2 if documentation_Documentation2 is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def documentation_Documentation(self):
        return self.__documentation_Documentation

    @documentation_Documentation.setter
    def documentation_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_Documentation__documentation_Documentation", None)
        self.__documentation_Documentation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentation_Section"):
                    opp_val = getattr(item, "documentation_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "documentation_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentation_Section"):
                    opp_val = getattr(item, "documentation_Section", None)
                    
                    setattr(item, "documentation_Section", self)
                    

    @property
    def documentation_Documentation2(self):
        return self.__documentation_Documentation2

    @documentation_Documentation2.setter
    def documentation_Documentation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_Documentation__documentation_Documentation2", None)
        self.__documentation_Documentation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentation_TermEntry"):
                    opp_val = getattr(item, "documentation_TermEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "documentation_TermEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentation_TermEntry"):
                    opp_val = getattr(item, "documentation_TermEntry", None)
                    
                    setattr(item, "documentation_TermEntry", self)
                    

class Fragment:

    pass
class documentation_Table(Fragment):

    pass
class documentation_Line(Fragment):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class documentation_List(Fragment):

    pass
class NamedElement:

    pass
class documentation_Image(Fragment, NamedElement):

    def __init__(self, width: str, originalSource: str):
        self.width = width
        self.originalSource = originalSource
        
        pass
    @property
    def originalSource(self):
        return self.__originalSource

    @originalSource.setter
    def originalSource(self, originalSource: str):
        self.__originalSource = originalSource


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


class documentation_TermEntry(NamedElement):

    def __init__(self, description: str, documentation_TermEntry: "documentation_Documentation" = None):
        self.description = description
        self.documentation_TermEntry = documentation_TermEntry
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def documentation_TermEntry(self):
        return self.__documentation_TermEntry

    @documentation_TermEntry.setter
    def documentation_TermEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_TermEntry__documentation_TermEntry", None)
        self.__documentation_TermEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_Documentation2"):
                opp_val = getattr(old_value, "documentation_Documentation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_Documentation2"):
                opp_val = getattr(value, "documentation_Documentation2", None)
                if opp_val is None:
                    setattr(value, "documentation_Documentation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class documentation_XML(Fragment, NamedElement):

    def __init__(self, contextClassName: str, resource: str):
        self.contextClassName = contextClassName
        self.resource = resource
        
        pass
    @property
    def contextClassName(self):
        return self.__contextClassName

    @contextClassName.setter
    def contextClassName(self, contextClassName: str):
        self.__contextClassName = contextClassName


    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource


class TextFragmentContainer:

    pass
class documentation_Subsection(Fragment, NamedElement, TextFragmentContainer):

    pass
class documentation_Subsubsection(Fragment, NamedElement, TextFragmentContainer):

    pass
class documentation_ListItem(TextFragmentContainer):

    def __init__(self, text: str, documentation_ListItem: "documentation_List" = None):
        self.text = text
        self.documentation_ListItem = documentation_ListItem
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def documentation_ListItem(self):
        return self.__documentation_ListItem

    @documentation_ListItem.setter
    def documentation_ListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_ListItem__documentation_ListItem", None)
        self.__documentation_ListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_List"):
                opp_val = getattr(old_value, "documentation_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_List"):
                opp_val = getattr(value, "documentation_List", None)
                if opp_val is None:
                    setattr(value, "documentation_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class documentation_Section(NamedElement, TextFragmentContainer):

    pass
class documentation_Paragraph(Fragment, TextFragmentContainer):

    pass