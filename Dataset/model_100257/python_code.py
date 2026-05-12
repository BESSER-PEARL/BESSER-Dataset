from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class HorizontalAlign(Enum):
    right = "right"
class ViewType(Enum):
    thumb = "thumb"


############################################
# Definition of Classes
############################################

class AnyText:

    pass
class wikiML_AbstractFormattedInlineContent(AnyText):

    pass
class HyperLink:

    pass
class wikiML_External(HyperLink):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class wikiML_Internal(HyperLink):

    pass
class AbstractUnformattedInlineContent:

    pass
class wikiML_HyperLink(AbstractUnformattedInlineContent):

    pass
class AbstractFormattedInlineContent:

    pass
class wikiML_ItalicBold(AbstractFormattedInlineContent):

    pass
class wikiML_Italic(AbstractFormattedInlineContent):

    pass
class wikiML_Bold(AbstractFormattedInlineContent):

    pass
class wikiML_Text(AbstractUnformattedInlineContent):

    def __init__(self, name: str, wikiML_Text: "wikiML_Category" = None, wikiML_Text39: "wikiML_Internal" = None):
        self.name = name
        self.wikiML_Text = wikiML_Text
        self.wikiML_Text39 = wikiML_Text39
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def wikiML_Text39(self):
        return self.__wikiML_Text39

    @wikiML_Text39.setter
    def wikiML_Text39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Text__wikiML_Text39", None)
        self.__wikiML_Text39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_Internal38"):
                opp_val = getattr(old_value, "wikiML_Internal38", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_Internal38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_Internal38"):
                opp_val = getattr(value, "wikiML_Internal38", None)
                setattr(value, "wikiML_Internal38", self)

    @property
    def wikiML_Text(self):
        return self.__wikiML_Text

    @wikiML_Text.setter
    def wikiML_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Text__wikiML_Text", None)
        self.__wikiML_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_Category"):
                opp_val = getattr(old_value, "wikiML_Category", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_Category"):
                opp_val = getattr(value, "wikiML_Category", None)
                setattr(value, "wikiML_Category", self)

class wikiML_AbstractUnformattedInlineContent(AnyText):

    pass
class wikiML_UnorderListItem:

    def __init__(self, level: str, wikiML_UnorderListItem: "wikiML_UnorderedList" = None, wikiML_UnorderListItem14: "wikiML_AnyTextSequence" = None):
        self.level = level
        self.wikiML_UnorderListItem = wikiML_UnorderListItem
        self.wikiML_UnorderListItem14 = wikiML_UnorderListItem14
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def wikiML_UnorderListItem14(self):
        return self.__wikiML_UnorderListItem14

    @wikiML_UnorderListItem14.setter
    def wikiML_UnorderListItem14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_UnorderListItem__wikiML_UnorderListItem14", None)
        self.__wikiML_UnorderListItem14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_AnyTextSequence15"):
                opp_val = getattr(old_value, "wikiML_AnyTextSequence15", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_AnyTextSequence15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_AnyTextSequence15"):
                opp_val = getattr(value, "wikiML_AnyTextSequence15", None)
                setattr(value, "wikiML_AnyTextSequence15", self)

    @property
    def wikiML_UnorderListItem(self):
        return self.__wikiML_UnorderListItem

    @wikiML_UnorderListItem.setter
    def wikiML_UnorderListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_UnorderListItem__wikiML_UnorderListItem", None)
        self.__wikiML_UnorderListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_UnorderedList"):
                opp_val = getattr(old_value, "wikiML_UnorderedList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_UnorderedList"):
                opp_val = getattr(value, "wikiML_UnorderedList", None)
                if opp_val is None:
                    setattr(value, "wikiML_UnorderedList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wikiML_OrderListItem:

    pass
class Template:

    pass
class wikiML_QuoteTemplate(Template):

    pass
class wikiML_MainTemplate(Template):

    pass
class wikiML_AboutTemplate(Template):

    pass
class wikiML_AnyTextSequence:

    pass
class ParagraphTypes:

    pass
class wikiML_AnyText(ParagraphTypes):

    pass
class wikiML_Image(ParagraphTypes):

    def __init__(self, name: str, type: str, hAlign: str, wikiML_Image: "wikiML_AbstractUnformattedInlineContent" = None, wikiML_Image21: "wikiML_AnyTextSequence" = None):
        self.name = name
        self.type = type
        self.hAlign = hAlign
        self.wikiML_Image = wikiML_Image
        self.wikiML_Image21 = wikiML_Image21
        
        pass
    @property
    def hAlign(self):
        return self.__hAlign

    @hAlign.setter
    def hAlign(self, hAlign: str):
        self.__hAlign = hAlign


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def wikiML_Image21(self):
        return self.__wikiML_Image21

    @wikiML_Image21.setter
    def wikiML_Image21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Image__wikiML_Image21", None)
        self.__wikiML_Image21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_AnyTextSequence22"):
                opp_val = getattr(old_value, "wikiML_AnyTextSequence22", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_AnyTextSequence22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_AnyTextSequence22"):
                opp_val = getattr(value, "wikiML_AnyTextSequence22", None)
                setattr(value, "wikiML_AnyTextSequence22", self)

    @property
    def wikiML_Image(self):
        return self.__wikiML_Image

    @wikiML_Image.setter
    def wikiML_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Image__wikiML_Image", None)
        self.__wikiML_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_AbstractUnformattedInlineContent"):
                opp_val = getattr(old_value, "wikiML_AbstractUnformattedInlineContent", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_AbstractUnformattedInlineContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_AbstractUnformattedInlineContent"):
                opp_val = getattr(value, "wikiML_AbstractUnformattedInlineContent", None)
                setattr(value, "wikiML_AbstractUnformattedInlineContent", self)

class wikiML_Heading5(ParagraphTypes):

    pass
class wikiML_Paragraph(ParagraphTypes):

    def __init__(self, paragraph: str, wikiML_Paragraph: "wikiML_OrderedList" = None, wikiML_Paragraph12: "wikiML_UnorderedList" = None):
        self.paragraph = paragraph
        self.wikiML_Paragraph = wikiML_Paragraph
        self.wikiML_Paragraph12 = wikiML_Paragraph12
        
        pass
    @property
    def paragraph(self):
        return self.__paragraph

    @paragraph.setter
    def paragraph(self, paragraph: str):
        self.__paragraph = paragraph


    @property
    def wikiML_Paragraph12(self):
        return self.__wikiML_Paragraph12

    @wikiML_Paragraph12.setter
    def wikiML_Paragraph12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Paragraph__wikiML_Paragraph12", None)
        self.__wikiML_Paragraph12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_UnorderedList11"):
                opp_val = getattr(old_value, "wikiML_UnorderedList11", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_UnorderedList11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_UnorderedList11"):
                opp_val = getattr(value, "wikiML_UnorderedList11", None)
                setattr(value, "wikiML_UnorderedList11", self)

    @property
    def wikiML_Paragraph(self):
        return self.__wikiML_Paragraph

    @wikiML_Paragraph.setter
    def wikiML_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Paragraph__wikiML_Paragraph", None)
        self.__wikiML_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_OrderedList8"):
                opp_val = getattr(old_value, "wikiML_OrderedList8", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_OrderedList8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_OrderedList8"):
                opp_val = getattr(value, "wikiML_OrderedList8", None)
                setattr(value, "wikiML_OrderedList8", self)

class wikiML_Category(ParagraphTypes):

    def __init__(self, value: str, wikiML_Category: "wikiML_Text" = None):
        self.value = value
        self.wikiML_Category = wikiML_Category
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def wikiML_Category(self):
        return self.__wikiML_Category

    @wikiML_Category.setter
    def wikiML_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_Category__wikiML_Category", None)
        self.__wikiML_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_Text"):
                opp_val = getattr(old_value, "wikiML_Text", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_Text", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_Text"):
                opp_val = getattr(value, "wikiML_Text", None)
                setattr(value, "wikiML_Text", self)

class wikiML_Template(ParagraphTypes):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class wikiML_Heading4(ParagraphTypes):

    pass
class wikiML_Heading3(ParagraphTypes):

    pass
class wikiML_OrderedList(ParagraphTypes):

    pass
class wikiML_Heading2(ParagraphTypes):

    pass
class wikiML_UnorderedList(ParagraphTypes):

    pass
class wikiML_BlockQuote(ParagraphTypes):

    pass
class wikiML_ParagraphTypes:

    pass
class wikiML_WikiPage:

    def __init__(self, name: str, wikiML_WikiPage: set["wikiML_ParagraphTypes"] = None, wikiML_WikiPage36: "wikiML_Internal" = None):
        self.name = name
        self.wikiML_WikiPage = wikiML_WikiPage if wikiML_WikiPage is not None else set()
        self.wikiML_WikiPage36 = wikiML_WikiPage36
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def wikiML_WikiPage(self):
        return self.__wikiML_WikiPage

    @wikiML_WikiPage.setter
    def wikiML_WikiPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_WikiPage__wikiML_WikiPage", None)
        self.__wikiML_WikiPage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wikiML_ParagraphTypes"):
                    opp_val = getattr(item, "wikiML_ParagraphTypes", None)
                    
                    if opp_val == self:
                        setattr(item, "wikiML_ParagraphTypes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wikiML_ParagraphTypes"):
                    opp_val = getattr(item, "wikiML_ParagraphTypes", None)
                    
                    setattr(item, "wikiML_ParagraphTypes", self)
                    

    @property
    def wikiML_WikiPage36(self):
        return self.__wikiML_WikiPage36

    @wikiML_WikiPage36.setter
    def wikiML_WikiPage36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wikiML_WikiPage__wikiML_WikiPage36", None)
        self.__wikiML_WikiPage36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wikiML_Internal"):
                opp_val = getattr(old_value, "wikiML_Internal", None)
                if opp_val == self:
                    setattr(old_value, "wikiML_Internal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wikiML_Internal"):
                opp_val = getattr(value, "wikiML_Internal", None)
                setattr(value, "wikiML_Internal", self)
