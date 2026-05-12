from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Unit(Enum):
    PERCENT = "PERCENT"
    PIXELS = "PIXELS"


############################################
# Definition of Classes
############################################

class documentation_TextContainer(ABC):

    pass
class documentation_Width:

    def __init__(self, width: str, unit: str, documentation_Width: "documentation_Image" = None):
        self.width = width
        self.unit = unit
        self.documentation_Width = documentation_Width
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def documentation_Width(self):
        return self.__documentation_Width

    @documentation_Width.setter
    def documentation_Width(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_Width__documentation_Width", None)
        self.__documentation_Width = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_Image"):
                opp_val = getattr(old_value, "documentation_Image", None)
                if opp_val == self:
                    setattr(old_value, "documentation_Image", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_Image"):
                opp_val = getattr(value, "documentation_Image", None)
                setattr(value, "documentation_Image", self)

class documentation_TableRow:

    pass
class documentation_TableHeader:

    pass
class documentation_TableCell:

    def __init__(self, content: str, span: int, documentation_TableCell: "documentation_TableHeader" = None, documentation_TableCell11: "documentation_TableRow" = None):
        self.content = content
        self.span = span
        self.documentation_TableCell = documentation_TableCell
        self.documentation_TableCell11 = documentation_TableCell11
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def span(self):
        return self.__span

    @span.setter
    def span(self, span: int):
        self.__span = span


    @property
    def documentation_TableCell(self):
        return self.__documentation_TableCell

    @documentation_TableCell.setter
    def documentation_TableCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_TableCell__documentation_TableCell", None)
        self.__documentation_TableCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_TableHeader8"):
                opp_val = getattr(old_value, "documentation_TableHeader8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_TableHeader8"):
                opp_val = getattr(value, "documentation_TableHeader8", None)
                if opp_val is None:
                    setattr(value, "documentation_TableHeader8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def documentation_TableCell11(self):
        return self.__documentation_TableCell11

    @documentation_TableCell11.setter
    def documentation_TableCell11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_TableCell__documentation_TableCell11", None)
        self.__documentation_TableCell11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_TableRow10"):
                opp_val = getattr(old_value, "documentation_TableRow10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_TableRow10"):
                opp_val = getattr(value, "documentation_TableRow10", None)
                if opp_val is None:
                    setattr(value, "documentation_TableRow10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class documentation_ListItem:

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

class documentation_NamedElement(ABC):

    def __init__(self, id: str, name: str, label: str):
        self.id = id
        self.name = name
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


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


class TextContainer:

    pass
class documentation_FragmentContainer(TextContainer):

    pass
class Fragment:

    pass
class documentation_Text(Fragment):

    def __init__(self, text: str, documentation_Text: "documentation_TextContainer" = None):
        self.text = text
        self.documentation_Text = documentation_Text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def documentation_Text(self):
        return self.__documentation_Text

    @documentation_Text.setter
    def documentation_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_Text__documentation_Text", None)
        self.__documentation_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_TextContainer"):
                opp_val = getattr(old_value, "documentation_TextContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_TextContainer"):
                opp_val = getattr(value, "documentation_TextContainer", None)
                if opp_val is None:
                    setattr(value, "documentation_TextContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class documentation_Table(Fragment):

    pass
class documentation_PageBreak(Fragment):

    pass
class documentation_Listing(Fragment, TextContainer):

    pass
class documentation_Paragraph(Fragment, TextContainer):

    pass
class NamedElement:

    pass
class documentation_XML(NamedElement, Fragment):

    def __init__(self, contextClassName: str, resource: str, content: str):
        self.contextClassName = contextClassName
        self.resource = resource
        self.content = content
        
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


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class documentation_Link(NamedElement, Fragment):

    def __init__(self, uri: str):
        self.uri = uri
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


class documentation_Image(NamedElement, Fragment):

    def __init__(self, originalSource: str, resource: str, contextClassName: str, documentation_Image: "documentation_Width" = None):
        self.originalSource = originalSource
        self.resource = resource
        self.contextClassName = contextClassName
        self.documentation_Image = documentation_Image
        
        pass
    @property
    def originalSource(self):
        return self.__originalSource

    @originalSource.setter
    def originalSource(self, originalSource: str):
        self.__originalSource = originalSource


    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource


    @property
    def contextClassName(self):
        return self.__contextClassName

    @contextClassName.setter
    def contextClassName(self, contextClassName: str):
        self.__contextClassName = contextClassName


    @property
    def documentation_Image(self):
        return self.__documentation_Image

    @documentation_Image.setter
    def documentation_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_documentation_Image__documentation_Image", None)
        self.__documentation_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation_Width"):
                opp_val = getattr(old_value, "documentation_Width", None)
                if opp_val == self:
                    setattr(old_value, "documentation_Width", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation_Width"):
                opp_val = getattr(value, "documentation_Width", None)
                setattr(value, "documentation_Width", self)

class FragmentContainer:

    pass
class documentation_Subsection(NamedElement, Fragment, FragmentContainer):

    pass
class documentation_Subsubsection(NamedElement, Fragment, FragmentContainer):

    pass
class documentation_List(Fragment):

    pass
class Text:

    pass
class documentation_Code(Text):

    pass
class documentation_Reference(NamedElement, Text):

    def __init__(self, referredLabel: str):
        self.referredLabel = referredLabel
        
        pass
    @property
    def referredLabel(self):
        return self.__referredLabel

    @referredLabel.setter
    def referredLabel(self, referredLabel: str):
        self.__referredLabel = referredLabel


class documentation_HtmlCode(Text):

    pass
class documentation_Line(Text):

    pass
class documentation_Fragment(ABC):

    pass
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

class documentation_Section(NamedElement, FragmentContainer):

    pass
class documentation_Documentation:

    def __init__(self, title: str, documentation_Documentation2: set["documentation_TermEntry"] = None, documentation_Documentation: set["documentation_Section"] = None):
        self.title = title
        self.documentation_Documentation2 = documentation_Documentation2 if documentation_Documentation2 is not None else set()
        self.documentation_Documentation = documentation_Documentation if documentation_Documentation is not None else set()
        
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
                    
