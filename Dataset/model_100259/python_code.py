from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class xdoc_GlossaryEntry:

    def __init__(self, name: str, alias: str, xdoc_GlossaryEntry: set["xdoc_TextOrMarkup"] = None, xdoc_GlossaryEntry67: "xdoc_Glossary" = None):
        self.name = name
        self.alias = alias
        self.xdoc_GlossaryEntry = xdoc_GlossaryEntry if xdoc_GlossaryEntry is not None else set()
        self.xdoc_GlossaryEntry67 = xdoc_GlossaryEntry67
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xdoc_GlossaryEntry(self):
        return self.__xdoc_GlossaryEntry

    @xdoc_GlossaryEntry.setter
    def xdoc_GlossaryEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_GlossaryEntry__xdoc_GlossaryEntry", None)
        self.__xdoc_GlossaryEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xdoc_TextOrMarkup64"):
                    opp_val = getattr(item, "xdoc_TextOrMarkup64", None)
                    
                    if opp_val == self:
                        setattr(item, "xdoc_TextOrMarkup64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xdoc_TextOrMarkup64"):
                    opp_val = getattr(item, "xdoc_TextOrMarkup64", None)
                    
                    setattr(item, "xdoc_TextOrMarkup64", self)
                    

    @property
    def xdoc_GlossaryEntry67(self):
        return self.__xdoc_GlossaryEntry67

    @xdoc_GlossaryEntry67.setter
    def xdoc_GlossaryEntry67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_GlossaryEntry__xdoc_GlossaryEntry67", None)
        self.__xdoc_GlossaryEntry67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xdoc_Glossary66"):
                opp_val = getattr(old_value, "xdoc_Glossary66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xdoc_Glossary66"):
                opp_val = getattr(value, "xdoc_Glossary66", None)
                if opp_val is None:
                    setattr(value, "xdoc_Glossary66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xdoc_MarkupInCode:

    pass
class xdoc_Code:

    def __init__(self, contents: str):
        self.contents = contents
        
        pass
    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents


class Part:

    pass
class xdoc_PartRef(Part):

    pass
class xdoc_JvmDeclaredType:

    pass
class xdoc_ImageProxy:

    pass
class MarkupInCode:

    pass
class xdoc_Item:

    pass
class Identifiable:

    pass
class xdoc_TableData:

    pass
class xdoc_TableRow:

    pass
class MarkUp:

    pass
class xdoc_UnorderedList(MarkUp):

    pass
class xdoc_Anchor(Identifiable, MarkupInCode, MarkUp):

    pass
class xdoc_OrderedList(MarkUp):

    pass
class xdoc_ImageRef(MarkUp):

    def __init__(self, name: str, path: str, clazz: str, style: str, caption: str, xdoc_ImageRef: "xdoc_ImageProxy" = None):
        self.name = name
        self.path = path
        self.clazz = clazz
        self.style = style
        self.caption = caption
        self.xdoc_ImageRef = xdoc_ImageRef
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def caption(self):
        return self.__caption

    @caption.setter
    def caption(self, caption: str):
        self.__caption = caption


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def clazz(self):
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz


    @property
    def xdoc_ImageRef(self):
        return self.__xdoc_ImageRef

    @xdoc_ImageRef.setter
    def xdoc_ImageRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_ImageRef__xdoc_ImageRef", None)
        self.__xdoc_ImageRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xdoc_ImageProxy"):
                opp_val = getattr(old_value, "xdoc_ImageProxy", None)
                if opp_val == self:
                    setattr(old_value, "xdoc_ImageProxy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xdoc_ImageProxy"):
                opp_val = getattr(value, "xdoc_ImageProxy", None)
                setattr(value, "xdoc_ImageProxy", self)

class xdoc_Link(MarkUp):

    def __init__(self, url: str, text: str):
        self.url = url
        self.text = text
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class xdoc_CodeRef(MarkUp):

    pass
class xdoc_CodeBlock(MarkUp):

    pass
class xdoc_Ref(MarkupInCode, MarkUp):

    pass
class xdoc_Todo(MarkupInCode, MarkUp):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class xdoc_Emphasize(MarkupInCode, MarkUp):

    pass
class xdoc_Table(MarkUp):

    pass
class xdoc_MarkUp:

    pass
class xdoc_TextPart:

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class xdoc_EObject:

    pass
class xdoc_Identifiable:

    def __init__(self, name: str, xdoc_Identifiable: "xdoc_Ref" = None):
        self.name = name
        self.xdoc_Identifiable = xdoc_Identifiable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xdoc_Identifiable(self):
        return self.__xdoc_Identifiable

    @xdoc_Identifiable.setter
    def xdoc_Identifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_Identifiable__xdoc_Identifiable", None)
        self.__xdoc_Identifiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xdoc_Ref"):
                opp_val = getattr(old_value, "xdoc_Ref", None)
                if opp_val == self:
                    setattr(old_value, "xdoc_Ref", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xdoc_Ref"):
                opp_val = getattr(value, "xdoc_Ref", None)
                setattr(value, "xdoc_Ref", self)

class Chapter:

    pass
class xdoc_ChapterRef(Chapter):

    pass
class Section2:

    pass
class xdoc_Section2Ref(Section2):

    pass
class Section:

    pass
class xdoc_SectionRef(Section):

    pass
class xdoc_AbstractSection(Identifiable):

    pass
class xdoc_XdocFile:

    pass
class xdoc_Glossary:

    pass
class xdoc_LangDef:

    def __init__(self, keywords: str, name: str, xdoc_LangDef: "xdoc_Document" = None, xdoc_LangDef62: "xdoc_CodeBlock" = None):
        self.keywords = keywords
        self.name = name
        self.xdoc_LangDef = xdoc_LangDef
        self.xdoc_LangDef62 = xdoc_LangDef62
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def xdoc_LangDef(self):
        return self.__xdoc_LangDef

    @xdoc_LangDef.setter
    def xdoc_LangDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_LangDef__xdoc_LangDef", None)
        self.__xdoc_LangDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xdoc_Document8"):
                opp_val = getattr(old_value, "xdoc_Document8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xdoc_Document8"):
                opp_val = getattr(value, "xdoc_Document8", None)
                if opp_val is None:
                    setattr(value, "xdoc_Document8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xdoc_LangDef62(self):
        return self.__xdoc_LangDef62

    @xdoc_LangDef62.setter
    def xdoc_LangDef62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xdoc_LangDef__xdoc_LangDef62", None)
        self.__xdoc_LangDef62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xdoc_CodeBlock61"):
                opp_val = getattr(old_value, "xdoc_CodeBlock61", None)
                if opp_val == self:
                    setattr(old_value, "xdoc_CodeBlock61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xdoc_CodeBlock61"):
                opp_val = getattr(value, "xdoc_CodeBlock61", None)
                setattr(value, "xdoc_CodeBlock61", self)

class xdoc_TextOrMarkup:

    pass
class AbstractSection:

    pass
class xdoc_Section4(AbstractSection):

    pass
class xdoc_Section(AbstractSection):

    pass
class xdoc_Section3(AbstractSection):

    pass
class xdoc_Section2(AbstractSection):

    pass
class xdoc_Part(AbstractSection):

    pass
class xdoc_Chapter(AbstractSection):

    pass
class xdoc_Document(AbstractSection):

    pass