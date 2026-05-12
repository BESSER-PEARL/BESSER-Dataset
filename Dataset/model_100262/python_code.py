from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PageSummary:

    pass
class ObjectSummary:

    pass
class xwiki_LinkCollection:

    pass
class xwiki_Link:

    def __init__(self, href: str, hrefLang: str, rel: str, type: str, xwiki_Link: "xwiki_LinkCollection" = None):
        self.href = href
        self.hrefLang = hrefLang
        self.rel = rel
        self.type = type
        self.xwiki_Link = xwiki_Link
        
        pass
    @property
    def rel(self):
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def href(self):
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href


    @property
    def hrefLang(self):
        return self.__hrefLang

    @hrefLang.setter
    def hrefLang(self, hrefLang: str):
        self.__hrefLang = hrefLang


    @property
    def xwiki_Link(self):
        return self.__xwiki_Link

    @xwiki_Link.setter
    def xwiki_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Link__xwiki_Link", None)
        self.__xwiki_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_LinkCollection"):
                opp_val = getattr(old_value, "xwiki_LinkCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_LinkCollection"):
                opp_val = getattr(value, "xwiki_LinkCollection", None)
                if opp_val is None:
                    setattr(value, "xwiki_LinkCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Page(PageSummary):

    def __init__(self, content: str, language: str, majorVersion: str, minorVersion: str, created: str, creator: str, creatorName: str, modified: str, modifier: str, modifierName: str, comment: str, xwiki_Page: "xwiki_DocumentRoot" = None):
        self.content = content
        self.language = language
        self.majorVersion = majorVersion
        self.minorVersion = minorVersion
        self.created = created
        self.creator = creator
        self.creatorName = creatorName
        self.modified = modified
        self.modifier = modifier
        self.modifierName = modifierName
        self.comment = comment
        self.xwiki_Page = xwiki_Page
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def majorVersion(self):
        return self.__majorVersion

    @majorVersion.setter
    def majorVersion(self, majorVersion: str):
        self.__majorVersion = majorVersion


    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier


    @property
    def creatorName(self):
        return self.__creatorName

    @creatorName.setter
    def creatorName(self, creatorName: str):
        self.__creatorName = creatorName


    @property
    def modified(self):
        return self.__modified

    @modified.setter
    def modified(self, modified: str):
        self.__modified = modified


    @property
    def minorVersion(self):
        return self.__minorVersion

    @minorVersion.setter
    def minorVersion(self, minorVersion: str):
        self.__minorVersion = minorVersion


    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def modifierName(self):
        return self.__modifierName

    @modifierName.setter
    def modifierName(self, modifierName: str):
        self.__modifierName = modifierName


    @property
    def xwiki_Page(self):
        return self.__xwiki_Page

    @xwiki_Page.setter
    def xwiki_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Page__xwiki_Page", None)
        self.__xwiki_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot36"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot36"):
                opp_val = getattr(value, "xwiki_DocumentRoot36", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Object(ObjectSummary):

    pass
class xwiki_EStringToStringMapEntry:

    pass
class xwiki_DocumentRoot:

    def __init__(self, mixed: str, xwiki_DocumentRoot10: set["xwiki_Attachment"] = None, xwiki_DocumentRoot: set["xwiki_EStringToStringMapEntry"] = None, xwiki_DocumentRoot7: set["xwiki_EStringToStringMapEntry"] = None, xwiki_DocumentRoot13: set["xwiki_AttachmentsType"] = None, xwiki_DocumentRoot16: set["xwiki_Class"] = None, xwiki_DocumentRoot19: set["xwiki_ClassesType"] = None, xwiki_DocumentRoot22: set["xwiki_Comment"] = None, xwiki_DocumentRoot25: set["xwiki_CommentsType"] = None, xwiki_DocumentRoot28: set["xwiki_HistoryType"] = None, xwiki_DocumentRoot30: set["xwiki_Object"] = None, xwiki_DocumentRoot32: set["xwiki_ObjectsType"] = None, xwiki_DocumentRoot51: set["xwiki_SpacesType"] = None, xwiki_DocumentRoot34: set["xwiki_ObjectSummary"] = None, xwiki_DocumentRoot36: set["xwiki_Page"] = None, xwiki_DocumentRoot38: set["xwiki_PagesType"] = None, xwiki_DocumentRoot40: set["xwiki_PropertiesType"] = None, xwiki_DocumentRoot42: set["xwiki_Property"] = None, xwiki_DocumentRoot45: set["xwiki_SearchResult"] = None, xwiki_DocumentRoot47: set["xwiki_SearchResultsType"] = None, xwiki_DocumentRoot49: set["xwiki_Space"] = None, xwiki_DocumentRoot53: set["xwiki_Syntaxes"] = None, xwiki_DocumentRoot55: set["xwiki_Tag"] = None, xwiki_DocumentRoot57: set["xwiki_TagsType"] = None, xwiki_DocumentRoot59: set["xwiki_Translations"] = None, xwiki_DocumentRoot61: set["xwiki_Wiki"] = None, xwiki_DocumentRoot63: set["xwiki_WikisType"] = None, xwiki_DocumentRoot65: set["xwiki_XWiki"] = None):
        self.mixed = mixed
        self.xwiki_DocumentRoot10 = xwiki_DocumentRoot10 if xwiki_DocumentRoot10 is not None else set()
        self.xwiki_DocumentRoot = xwiki_DocumentRoot if xwiki_DocumentRoot is not None else set()
        self.xwiki_DocumentRoot7 = xwiki_DocumentRoot7 if xwiki_DocumentRoot7 is not None else set()
        self.xwiki_DocumentRoot13 = xwiki_DocumentRoot13 if xwiki_DocumentRoot13 is not None else set()
        self.xwiki_DocumentRoot16 = xwiki_DocumentRoot16 if xwiki_DocumentRoot16 is not None else set()
        self.xwiki_DocumentRoot19 = xwiki_DocumentRoot19 if xwiki_DocumentRoot19 is not None else set()
        self.xwiki_DocumentRoot22 = xwiki_DocumentRoot22 if xwiki_DocumentRoot22 is not None else set()
        self.xwiki_DocumentRoot25 = xwiki_DocumentRoot25 if xwiki_DocumentRoot25 is not None else set()
        self.xwiki_DocumentRoot28 = xwiki_DocumentRoot28 if xwiki_DocumentRoot28 is not None else set()
        self.xwiki_DocumentRoot30 = xwiki_DocumentRoot30 if xwiki_DocumentRoot30 is not None else set()
        self.xwiki_DocumentRoot32 = xwiki_DocumentRoot32 if xwiki_DocumentRoot32 is not None else set()
        self.xwiki_DocumentRoot51 = xwiki_DocumentRoot51 if xwiki_DocumentRoot51 is not None else set()
        self.xwiki_DocumentRoot34 = xwiki_DocumentRoot34 if xwiki_DocumentRoot34 is not None else set()
        self.xwiki_DocumentRoot36 = xwiki_DocumentRoot36 if xwiki_DocumentRoot36 is not None else set()
        self.xwiki_DocumentRoot38 = xwiki_DocumentRoot38 if xwiki_DocumentRoot38 is not None else set()
        self.xwiki_DocumentRoot40 = xwiki_DocumentRoot40 if xwiki_DocumentRoot40 is not None else set()
        self.xwiki_DocumentRoot42 = xwiki_DocumentRoot42 if xwiki_DocumentRoot42 is not None else set()
        self.xwiki_DocumentRoot45 = xwiki_DocumentRoot45 if xwiki_DocumentRoot45 is not None else set()
        self.xwiki_DocumentRoot47 = xwiki_DocumentRoot47 if xwiki_DocumentRoot47 is not None else set()
        self.xwiki_DocumentRoot49 = xwiki_DocumentRoot49 if xwiki_DocumentRoot49 is not None else set()
        self.xwiki_DocumentRoot53 = xwiki_DocumentRoot53 if xwiki_DocumentRoot53 is not None else set()
        self.xwiki_DocumentRoot55 = xwiki_DocumentRoot55 if xwiki_DocumentRoot55 is not None else set()
        self.xwiki_DocumentRoot57 = xwiki_DocumentRoot57 if xwiki_DocumentRoot57 is not None else set()
        self.xwiki_DocumentRoot59 = xwiki_DocumentRoot59 if xwiki_DocumentRoot59 is not None else set()
        self.xwiki_DocumentRoot61 = xwiki_DocumentRoot61 if xwiki_DocumentRoot61 is not None else set()
        self.xwiki_DocumentRoot63 = xwiki_DocumentRoot63 if xwiki_DocumentRoot63 is not None else set()
        self.xwiki_DocumentRoot65 = xwiki_DocumentRoot65 if xwiki_DocumentRoot65 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def xwiki_DocumentRoot40(self):
        return self.__xwiki_DocumentRoot40

    @xwiki_DocumentRoot40.setter
    def xwiki_DocumentRoot40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot40", None)
        self.__xwiki_DocumentRoot40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_PropertiesType"):
                    opp_val = getattr(item, "xwiki_PropertiesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_PropertiesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_PropertiesType"):
                    opp_val = getattr(item, "xwiki_PropertiesType", None)
                    
                    setattr(item, "xwiki_PropertiesType", self)
                    

    @property
    def xwiki_DocumentRoot45(self):
        return self.__xwiki_DocumentRoot45

    @xwiki_DocumentRoot45.setter
    def xwiki_DocumentRoot45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot45", None)
        self.__xwiki_DocumentRoot45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_SearchResult"):
                    opp_val = getattr(item, "xwiki_SearchResult", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_SearchResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_SearchResult"):
                    opp_val = getattr(item, "xwiki_SearchResult", None)
                    
                    setattr(item, "xwiki_SearchResult", self)
                    

    @property
    def xwiki_DocumentRoot25(self):
        return self.__xwiki_DocumentRoot25

    @xwiki_DocumentRoot25.setter
    def xwiki_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot25", None)
        self.__xwiki_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_CommentsType26"):
                    opp_val = getattr(item, "xwiki_CommentsType26", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_CommentsType26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_CommentsType26"):
                    opp_val = getattr(item, "xwiki_CommentsType26", None)
                    
                    setattr(item, "xwiki_CommentsType26", self)
                    

    @property
    def xwiki_DocumentRoot30(self):
        return self.__xwiki_DocumentRoot30

    @xwiki_DocumentRoot30.setter
    def xwiki_DocumentRoot30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot30", None)
        self.__xwiki_DocumentRoot30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Object"):
                    opp_val = getattr(item, "xwiki_Object", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Object", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Object"):
                    opp_val = getattr(item, "xwiki_Object", None)
                    
                    setattr(item, "xwiki_Object", self)
                    

    @property
    def xwiki_DocumentRoot28(self):
        return self.__xwiki_DocumentRoot28

    @xwiki_DocumentRoot28.setter
    def xwiki_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot28", None)
        self.__xwiki_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_HistoryType"):
                    opp_val = getattr(item, "xwiki_HistoryType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_HistoryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_HistoryType"):
                    opp_val = getattr(item, "xwiki_HistoryType", None)
                    
                    setattr(item, "xwiki_HistoryType", self)
                    

    @property
    def xwiki_DocumentRoot47(self):
        return self.__xwiki_DocumentRoot47

    @xwiki_DocumentRoot47.setter
    def xwiki_DocumentRoot47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot47", None)
        self.__xwiki_DocumentRoot47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_SearchResultsType"):
                    opp_val = getattr(item, "xwiki_SearchResultsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_SearchResultsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_SearchResultsType"):
                    opp_val = getattr(item, "xwiki_SearchResultsType", None)
                    
                    setattr(item, "xwiki_SearchResultsType", self)
                    

    @property
    def xwiki_DocumentRoot22(self):
        return self.__xwiki_DocumentRoot22

    @xwiki_DocumentRoot22.setter
    def xwiki_DocumentRoot22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot22", None)
        self.__xwiki_DocumentRoot22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Comment23"):
                    opp_val = getattr(item, "xwiki_Comment23", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Comment23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Comment23"):
                    opp_val = getattr(item, "xwiki_Comment23", None)
                    
                    setattr(item, "xwiki_Comment23", self)
                    

    @property
    def xwiki_DocumentRoot51(self):
        return self.__xwiki_DocumentRoot51

    @xwiki_DocumentRoot51.setter
    def xwiki_DocumentRoot51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot51", None)
        self.__xwiki_DocumentRoot51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_SpacesType"):
                    opp_val = getattr(item, "xwiki_SpacesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_SpacesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_SpacesType"):
                    opp_val = getattr(item, "xwiki_SpacesType", None)
                    
                    setattr(item, "xwiki_SpacesType", self)
                    

    @property
    def xwiki_DocumentRoot32(self):
        return self.__xwiki_DocumentRoot32

    @xwiki_DocumentRoot32.setter
    def xwiki_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot32", None)
        self.__xwiki_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_ObjectsType"):
                    opp_val = getattr(item, "xwiki_ObjectsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_ObjectsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_ObjectsType"):
                    opp_val = getattr(item, "xwiki_ObjectsType", None)
                    
                    setattr(item, "xwiki_ObjectsType", self)
                    

    @property
    def xwiki_DocumentRoot63(self):
        return self.__xwiki_DocumentRoot63

    @xwiki_DocumentRoot63.setter
    def xwiki_DocumentRoot63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot63", None)
        self.__xwiki_DocumentRoot63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_WikisType"):
                    opp_val = getattr(item, "xwiki_WikisType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_WikisType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_WikisType"):
                    opp_val = getattr(item, "xwiki_WikisType", None)
                    
                    setattr(item, "xwiki_WikisType", self)
                    

    @property
    def xwiki_DocumentRoot42(self):
        return self.__xwiki_DocumentRoot42

    @xwiki_DocumentRoot42.setter
    def xwiki_DocumentRoot42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot42", None)
        self.__xwiki_DocumentRoot42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Property43"):
                    opp_val = getattr(item, "xwiki_Property43", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Property43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Property43"):
                    opp_val = getattr(item, "xwiki_Property43", None)
                    
                    setattr(item, "xwiki_Property43", self)
                    

    @property
    def xwiki_DocumentRoot61(self):
        return self.__xwiki_DocumentRoot61

    @xwiki_DocumentRoot61.setter
    def xwiki_DocumentRoot61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot61", None)
        self.__xwiki_DocumentRoot61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Wiki"):
                    opp_val = getattr(item, "xwiki_Wiki", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Wiki", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Wiki"):
                    opp_val = getattr(item, "xwiki_Wiki", None)
                    
                    setattr(item, "xwiki_Wiki", self)
                    

    @property
    def xwiki_DocumentRoot19(self):
        return self.__xwiki_DocumentRoot19

    @xwiki_DocumentRoot19.setter
    def xwiki_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot19", None)
        self.__xwiki_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_ClassesType20"):
                    opp_val = getattr(item, "xwiki_ClassesType20", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_ClassesType20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_ClassesType20"):
                    opp_val = getattr(item, "xwiki_ClassesType20", None)
                    
                    setattr(item, "xwiki_ClassesType20", self)
                    

    @property
    def xwiki_DocumentRoot49(self):
        return self.__xwiki_DocumentRoot49

    @xwiki_DocumentRoot49.setter
    def xwiki_DocumentRoot49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot49", None)
        self.__xwiki_DocumentRoot49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Space"):
                    opp_val = getattr(item, "xwiki_Space", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Space", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Space"):
                    opp_val = getattr(item, "xwiki_Space", None)
                    
                    setattr(item, "xwiki_Space", self)
                    

    @property
    def xwiki_DocumentRoot7(self):
        return self.__xwiki_DocumentRoot7

    @xwiki_DocumentRoot7.setter
    def xwiki_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot7", None)
        self.__xwiki_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_EStringToStringMapEntry8"):
                    opp_val = getattr(item, "xwiki_EStringToStringMapEntry8", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_EStringToStringMapEntry8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_EStringToStringMapEntry8"):
                    opp_val = getattr(item, "xwiki_EStringToStringMapEntry8", None)
                    
                    setattr(item, "xwiki_EStringToStringMapEntry8", self)
                    

    @property
    def xwiki_DocumentRoot(self):
        return self.__xwiki_DocumentRoot

    @xwiki_DocumentRoot.setter
    def xwiki_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot", None)
        self.__xwiki_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xwiki_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xwiki_EStringToStringMapEntry", None)
                    
                    setattr(item, "xwiki_EStringToStringMapEntry", self)
                    

    @property
    def xwiki_DocumentRoot38(self):
        return self.__xwiki_DocumentRoot38

    @xwiki_DocumentRoot38.setter
    def xwiki_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot38", None)
        self.__xwiki_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_PagesType"):
                    opp_val = getattr(item, "xwiki_PagesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_PagesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_PagesType"):
                    opp_val = getattr(item, "xwiki_PagesType", None)
                    
                    setattr(item, "xwiki_PagesType", self)
                    

    @property
    def xwiki_DocumentRoot57(self):
        return self.__xwiki_DocumentRoot57

    @xwiki_DocumentRoot57.setter
    def xwiki_DocumentRoot57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot57", None)
        self.__xwiki_DocumentRoot57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_TagsType"):
                    opp_val = getattr(item, "xwiki_TagsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_TagsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_TagsType"):
                    opp_val = getattr(item, "xwiki_TagsType", None)
                    
                    setattr(item, "xwiki_TagsType", self)
                    

    @property
    def xwiki_DocumentRoot53(self):
        return self.__xwiki_DocumentRoot53

    @xwiki_DocumentRoot53.setter
    def xwiki_DocumentRoot53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot53", None)
        self.__xwiki_DocumentRoot53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Syntaxes"):
                    opp_val = getattr(item, "xwiki_Syntaxes", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Syntaxes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Syntaxes"):
                    opp_val = getattr(item, "xwiki_Syntaxes", None)
                    
                    setattr(item, "xwiki_Syntaxes", self)
                    

    @property
    def xwiki_DocumentRoot13(self):
        return self.__xwiki_DocumentRoot13

    @xwiki_DocumentRoot13.setter
    def xwiki_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot13", None)
        self.__xwiki_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_AttachmentsType14"):
                    opp_val = getattr(item, "xwiki_AttachmentsType14", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_AttachmentsType14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_AttachmentsType14"):
                    opp_val = getattr(item, "xwiki_AttachmentsType14", None)
                    
                    setattr(item, "xwiki_AttachmentsType14", self)
                    

    @property
    def xwiki_DocumentRoot36(self):
        return self.__xwiki_DocumentRoot36

    @xwiki_DocumentRoot36.setter
    def xwiki_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot36", None)
        self.__xwiki_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Page"):
                    opp_val = getattr(item, "xwiki_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Page"):
                    opp_val = getattr(item, "xwiki_Page", None)
                    
                    setattr(item, "xwiki_Page", self)
                    

    @property
    def xwiki_DocumentRoot65(self):
        return self.__xwiki_DocumentRoot65

    @xwiki_DocumentRoot65.setter
    def xwiki_DocumentRoot65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot65", None)
        self.__xwiki_DocumentRoot65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_XWiki"):
                    opp_val = getattr(item, "xwiki_XWiki", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_XWiki", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_XWiki"):
                    opp_val = getattr(item, "xwiki_XWiki", None)
                    
                    setattr(item, "xwiki_XWiki", self)
                    

    @property
    def xwiki_DocumentRoot34(self):
        return self.__xwiki_DocumentRoot34

    @xwiki_DocumentRoot34.setter
    def xwiki_DocumentRoot34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot34", None)
        self.__xwiki_DocumentRoot34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_ObjectSummary"):
                    opp_val = getattr(item, "xwiki_ObjectSummary", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_ObjectSummary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_ObjectSummary"):
                    opp_val = getattr(item, "xwiki_ObjectSummary", None)
                    
                    setattr(item, "xwiki_ObjectSummary", self)
                    

    @property
    def xwiki_DocumentRoot59(self):
        return self.__xwiki_DocumentRoot59

    @xwiki_DocumentRoot59.setter
    def xwiki_DocumentRoot59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot59", None)
        self.__xwiki_DocumentRoot59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Translations"):
                    opp_val = getattr(item, "xwiki_Translations", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Translations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Translations"):
                    opp_val = getattr(item, "xwiki_Translations", None)
                    
                    setattr(item, "xwiki_Translations", self)
                    

    @property
    def xwiki_DocumentRoot16(self):
        return self.__xwiki_DocumentRoot16

    @xwiki_DocumentRoot16.setter
    def xwiki_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot16", None)
        self.__xwiki_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Class17"):
                    opp_val = getattr(item, "xwiki_Class17", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Class17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Class17"):
                    opp_val = getattr(item, "xwiki_Class17", None)
                    
                    setattr(item, "xwiki_Class17", self)
                    

    @property
    def xwiki_DocumentRoot55(self):
        return self.__xwiki_DocumentRoot55

    @xwiki_DocumentRoot55.setter
    def xwiki_DocumentRoot55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot55", None)
        self.__xwiki_DocumentRoot55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Tag"):
                    opp_val = getattr(item, "xwiki_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Tag"):
                    opp_val = getattr(item, "xwiki_Tag", None)
                    
                    setattr(item, "xwiki_Tag", self)
                    

    @property
    def xwiki_DocumentRoot10(self):
        return self.__xwiki_DocumentRoot10

    @xwiki_DocumentRoot10.setter
    def xwiki_DocumentRoot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_DocumentRoot__xwiki_DocumentRoot10", None)
        self.__xwiki_DocumentRoot10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Attachment11"):
                    opp_val = getattr(item, "xwiki_Attachment11", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Attachment11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Attachment11"):
                    opp_val = getattr(item, "xwiki_Attachment11", None)
                    
                    setattr(item, "xwiki_Attachment11", self)
                    

class LinkCollection:

    pass
class xwiki_Property(LinkCollection):

    def __init__(self, value: str, name: str, type: str, xwiki_Property: "xwiki_Class" = None, xwiki_Property43: "xwiki_DocumentRoot" = None, xwiki_Property82: "xwiki_PropertiesType" = None, xwiki_Property84: set["xwiki_Attribute"] = None, xwiki_Property71: "xwiki_Object" = None):
        self.value = value
        self.name = name
        self.type = type
        self.xwiki_Property = xwiki_Property
        self.xwiki_Property43 = xwiki_Property43
        self.xwiki_Property82 = xwiki_Property82
        self.xwiki_Property84 = xwiki_Property84 if xwiki_Property84 is not None else set()
        self.xwiki_Property71 = xwiki_Property71
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xwiki_Property71(self):
        return self.__xwiki_Property71

    @xwiki_Property71.setter
    def xwiki_Property71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Property__xwiki_Property71", None)
        self.__xwiki_Property71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Object70"):
                opp_val = getattr(old_value, "xwiki_Object70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Object70"):
                opp_val = getattr(value, "xwiki_Object70", None)
                if opp_val is None:
                    setattr(value, "xwiki_Object70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Property43(self):
        return self.__xwiki_Property43

    @xwiki_Property43.setter
    def xwiki_Property43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Property__xwiki_Property43", None)
        self.__xwiki_Property43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot42"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot42"):
                opp_val = getattr(value, "xwiki_DocumentRoot42", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Property84(self):
        return self.__xwiki_Property84

    @xwiki_Property84.setter
    def xwiki_Property84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Property__xwiki_Property84", None)
        self.__xwiki_Property84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Attribute"):
                    opp_val = getattr(item, "xwiki_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Attribute"):
                    opp_val = getattr(item, "xwiki_Attribute", None)
                    
                    setattr(item, "xwiki_Attribute", self)
                    

    @property
    def xwiki_Property(self):
        return self.__xwiki_Property

    @xwiki_Property.setter
    def xwiki_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Property__xwiki_Property", None)
        self.__xwiki_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Class"):
                opp_val = getattr(old_value, "xwiki_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Class"):
                opp_val = getattr(value, "xwiki_Class", None)
                if opp_val is None:
                    setattr(value, "xwiki_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Property82(self):
        return self.__xwiki_Property82

    @xwiki_Property82.setter
    def xwiki_Property82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Property__xwiki_Property82", None)
        self.__xwiki_Property82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_PropertiesType81"):
                opp_val = getattr(old_value, "xwiki_PropertiesType81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_PropertiesType81"):
                opp_val = getattr(value, "xwiki_PropertiesType81", None)
                if opp_val is None:
                    setattr(value, "xwiki_PropertiesType81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Attribute(LinkCollection):

    def __init__(self, name: str, value: str, xwiki_Attribute: "xwiki_Property" = None):
        self.name = name
        self.value = value
        self.xwiki_Attribute = xwiki_Attribute
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xwiki_Attribute(self):
        return self.__xwiki_Attribute

    @xwiki_Attribute.setter
    def xwiki_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Attribute__xwiki_Attribute", None)
        self.__xwiki_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Property84"):
                opp_val = getattr(old_value, "xwiki_Property84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Property84"):
                opp_val = getattr(value, "xwiki_Property84", None)
                if opp_val is None:
                    setattr(value, "xwiki_Property84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_TagsType(LinkCollection):

    pass
class xwiki_Tag(LinkCollection):

    def __init__(self, name: str, xwiki_Tag96: "xwiki_TagsType" = None, xwiki_Tag: "xwiki_DocumentRoot" = None):
        self.name = name
        self.xwiki_Tag96 = xwiki_Tag96
        self.xwiki_Tag = xwiki_Tag
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xwiki_Tag96(self):
        return self.__xwiki_Tag96

    @xwiki_Tag96.setter
    def xwiki_Tag96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Tag__xwiki_Tag96", None)
        self.__xwiki_Tag96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_TagsType95"):
                opp_val = getattr(old_value, "xwiki_TagsType95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_TagsType95"):
                opp_val = getattr(value, "xwiki_TagsType95", None)
                if opp_val is None:
                    setattr(value, "xwiki_TagsType95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Tag(self):
        return self.__xwiki_Tag

    @xwiki_Tag.setter
    def xwiki_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Tag__xwiki_Tag", None)
        self.__xwiki_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot55"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot55"):
                opp_val = getattr(value, "xwiki_DocumentRoot55", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Translations(LinkCollection):

    def __init__(self, default: str, xwiki_Translations79: "xwiki_PageSummary" = None, xwiki_Translations98: set["xwiki_Translation"] = None, xwiki_Translations: "xwiki_DocumentRoot" = None):
        self.default = default
        self.xwiki_Translations79 = xwiki_Translations79
        self.xwiki_Translations98 = xwiki_Translations98 if xwiki_Translations98 is not None else set()
        self.xwiki_Translations = xwiki_Translations
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def xwiki_Translations(self):
        return self.__xwiki_Translations

    @xwiki_Translations.setter
    def xwiki_Translations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Translations__xwiki_Translations", None)
        self.__xwiki_Translations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot59"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot59"):
                opp_val = getattr(value, "xwiki_DocumentRoot59", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Translations79(self):
        return self.__xwiki_Translations79

    @xwiki_Translations79.setter
    def xwiki_Translations79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Translations__xwiki_Translations79", None)
        self.__xwiki_Translations79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_PageSummary78"):
                opp_val = getattr(old_value, "xwiki_PageSummary78", None)
                if opp_val == self:
                    setattr(old_value, "xwiki_PageSummary78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_PageSummary78"):
                opp_val = getattr(value, "xwiki_PageSummary78", None)
                setattr(value, "xwiki_PageSummary78", self)

    @property
    def xwiki_Translations98(self):
        return self.__xwiki_Translations98

    @xwiki_Translations98.setter
    def xwiki_Translations98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Translations__xwiki_Translations98", None)
        self.__xwiki_Translations98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Translation"):
                    opp_val = getattr(item, "xwiki_Translation", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Translation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Translation"):
                    opp_val = getattr(item, "xwiki_Translation", None)
                    
                    setattr(item, "xwiki_Translation", self)
                    

class xwiki_ObjectSummary(LinkCollection):

    def __init__(self, id: str, headline: str, guid: str, pageId: str, pageVersion: str, wiki: str, space: str, pageName: str, pageAuthor: str, pageAuthorName: str, className: str, number: str, xwiki_ObjectSummary: "xwiki_DocumentRoot" = None, xwiki_ObjectSummary74: "xwiki_ObjectsType" = None):
        self.id = id
        self.headline = headline
        self.guid = guid
        self.pageId = pageId
        self.pageVersion = pageVersion
        self.wiki = wiki
        self.space = space
        self.pageName = pageName
        self.pageAuthor = pageAuthor
        self.pageAuthorName = pageAuthorName
        self.className = className
        self.number = number
        self.xwiki_ObjectSummary = xwiki_ObjectSummary
        self.xwiki_ObjectSummary74 = xwiki_ObjectSummary74
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def pageAuthorName(self):
        return self.__pageAuthorName

    @pageAuthorName.setter
    def pageAuthorName(self, pageAuthorName: str):
        self.__pageAuthorName = pageAuthorName


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, wiki: str):
        self.__wiki = wiki


    @property
    def pageAuthor(self):
        return self.__pageAuthor

    @pageAuthor.setter
    def pageAuthor(self, pageAuthor: str):
        self.__pageAuthor = pageAuthor


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def pageVersion(self):
        return self.__pageVersion

    @pageVersion.setter
    def pageVersion(self, pageVersion: str):
        self.__pageVersion = pageVersion


    @property
    def pageId(self):
        return self.__pageId

    @pageId.setter
    def pageId(self, pageId: str):
        self.__pageId = pageId


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def pageName(self):
        return self.__pageName

    @pageName.setter
    def pageName(self, pageName: str):
        self.__pageName = pageName


    @property
    def headline(self):
        return self.__headline

    @headline.setter
    def headline(self, headline: str):
        self.__headline = headline


    @property
    def xwiki_ObjectSummary74(self):
        return self.__xwiki_ObjectSummary74

    @xwiki_ObjectSummary74.setter
    def xwiki_ObjectSummary74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_ObjectSummary__xwiki_ObjectSummary74", None)
        self.__xwiki_ObjectSummary74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_ObjectsType73"):
                opp_val = getattr(old_value, "xwiki_ObjectsType73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_ObjectsType73"):
                opp_val = getattr(value, "xwiki_ObjectsType73", None)
                if opp_val is None:
                    setattr(value, "xwiki_ObjectsType73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_ObjectSummary(self):
        return self.__xwiki_ObjectSummary

    @xwiki_ObjectSummary.setter
    def xwiki_ObjectSummary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_ObjectSummary__xwiki_ObjectSummary", None)
        self.__xwiki_ObjectSummary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot34"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot34"):
                opp_val = getattr(value, "xwiki_DocumentRoot34", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_WikisType(LinkCollection):

    pass
class xwiki_Class(LinkCollection):

    def __init__(self, id: str, name: str, xwiki_Class: set["xwiki_Property"] = None, xwiki_Class3: "xwiki_ClassesType" = None, xwiki_Class17: "xwiki_DocumentRoot" = None):
        self.id = id
        self.name = name
        self.xwiki_Class = xwiki_Class if xwiki_Class is not None else set()
        self.xwiki_Class3 = xwiki_Class3
        self.xwiki_Class17 = xwiki_Class17
        
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


    @property
    def xwiki_Class(self):
        return self.__xwiki_Class

    @xwiki_Class.setter
    def xwiki_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Class__xwiki_Class", None)
        self.__xwiki_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_Property"):
                    opp_val = getattr(item, "xwiki_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_Property"):
                    opp_val = getattr(item, "xwiki_Property", None)
                    
                    setattr(item, "xwiki_Property", self)
                    

    @property
    def xwiki_Class3(self):
        return self.__xwiki_Class3

    @xwiki_Class3.setter
    def xwiki_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Class__xwiki_Class3", None)
        self.__xwiki_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_ClassesType"):
                opp_val = getattr(old_value, "xwiki_ClassesType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_ClassesType"):
                opp_val = getattr(value, "xwiki_ClassesType", None)
                if opp_val is None:
                    setattr(value, "xwiki_ClassesType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Class17(self):
        return self.__xwiki_Class17

    @xwiki_Class17.setter
    def xwiki_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Class__xwiki_Class17", None)
        self.__xwiki_Class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot16"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot16"):
                opp_val = getattr(value, "xwiki_DocumentRoot16", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_XWiki(LinkCollection):

    def __init__(self, version: str, xwiki_XWiki103: "xwiki_Syntaxes" = None, xwiki_XWiki: "xwiki_DocumentRoot" = None):
        self.version = version
        self.xwiki_XWiki103 = xwiki_XWiki103
        self.xwiki_XWiki = xwiki_XWiki
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def xwiki_XWiki103(self):
        return self.__xwiki_XWiki103

    @xwiki_XWiki103.setter
    def xwiki_XWiki103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_XWiki__xwiki_XWiki103", None)
        self.__xwiki_XWiki103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Syntaxes104"):
                opp_val = getattr(old_value, "xwiki_Syntaxes104", None)
                if opp_val == self:
                    setattr(old_value, "xwiki_Syntaxes104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Syntaxes104"):
                opp_val = getattr(value, "xwiki_Syntaxes104", None)
                setattr(value, "xwiki_Syntaxes104", self)

    @property
    def xwiki_XWiki(self):
        return self.__xwiki_XWiki

    @xwiki_XWiki.setter
    def xwiki_XWiki(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_XWiki__xwiki_XWiki", None)
        self.__xwiki_XWiki = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot65"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot65"):
                opp_val = getattr(value, "xwiki_DocumentRoot65", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Wiki(LinkCollection):

    def __init__(self, id: str, name: str, description: str, owner: str, xwiki_Wiki101: "xwiki_WikisType" = None, xwiki_Wiki: "xwiki_DocumentRoot" = None):
        self.id = id
        self.name = name
        self.description = description
        self.owner = owner
        self.xwiki_Wiki101 = xwiki_Wiki101
        self.xwiki_Wiki = xwiki_Wiki
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def xwiki_Wiki101(self):
        return self.__xwiki_Wiki101

    @xwiki_Wiki101.setter
    def xwiki_Wiki101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Wiki__xwiki_Wiki101", None)
        self.__xwiki_Wiki101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_WikisType100"):
                opp_val = getattr(old_value, "xwiki_WikisType100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_WikisType100"):
                opp_val = getattr(value, "xwiki_WikisType100", None)
                if opp_val is None:
                    setattr(value, "xwiki_WikisType100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Wiki(self):
        return self.__xwiki_Wiki

    @xwiki_Wiki.setter
    def xwiki_Wiki(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Wiki__xwiki_Wiki", None)
        self.__xwiki_Wiki = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot61"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot61"):
                opp_val = getattr(value, "xwiki_DocumentRoot61", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_SearchResultsType(LinkCollection):

    def __init__(self, template: str, xwiki_SearchResultsType: "xwiki_DocumentRoot" = None, xwiki_SearchResultsType89: set["xwiki_SearchResult"] = None):
        self.template = template
        self.xwiki_SearchResultsType = xwiki_SearchResultsType
        self.xwiki_SearchResultsType89 = xwiki_SearchResultsType89 if xwiki_SearchResultsType89 is not None else set()
        
        pass
    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template


    @property
    def xwiki_SearchResultsType89(self):
        return self.__xwiki_SearchResultsType89

    @xwiki_SearchResultsType89.setter
    def xwiki_SearchResultsType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_SearchResultsType__xwiki_SearchResultsType89", None)
        self.__xwiki_SearchResultsType89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xwiki_SearchResult90"):
                    opp_val = getattr(item, "xwiki_SearchResult90", None)
                    
                    if opp_val == self:
                        setattr(item, "xwiki_SearchResult90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xwiki_SearchResult90"):
                    opp_val = getattr(item, "xwiki_SearchResult90", None)
                    
                    setattr(item, "xwiki_SearchResult90", self)
                    

    @property
    def xwiki_SearchResultsType(self):
        return self.__xwiki_SearchResultsType

    @xwiki_SearchResultsType.setter
    def xwiki_SearchResultsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_SearchResultsType__xwiki_SearchResultsType", None)
        self.__xwiki_SearchResultsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot47"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot47"):
                opp_val = getattr(value, "xwiki_DocumentRoot47", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_ClassesType(LinkCollection):

    pass
class xwiki_PropertiesType(LinkCollection):

    pass
class xwiki_PageSummary(LinkCollection):

    def __init__(self, version: str, id: str, fullName: str, wiki: str, space: str, name: str, title: str, parent: str, parentId: str, syntax: str, author: str, authorName: str, xwikiRelativeUrl: str, xwikiAbsoluteUrl: str, xwiki_PageSummary: "xwiki_PagesType" = None, xwiki_PageSummary78: "xwiki_Translations" = None):
        self.version = version
        self.id = id
        self.fullName = fullName
        self.wiki = wiki
        self.space = space
        self.name = name
        self.title = title
        self.parent = parent
        self.parentId = parentId
        self.syntax = syntax
        self.author = author
        self.authorName = authorName
        self.xwikiRelativeUrl = xwikiRelativeUrl
        self.xwikiAbsoluteUrl = xwikiAbsoluteUrl
        self.xwiki_PageSummary = xwiki_PageSummary
        self.xwiki_PageSummary78 = xwiki_PageSummary78
        
        pass
    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent: str):
        self.__parent = parent


    @property
    def parentId(self):
        return self.__parentId

    @parentId.setter
    def parentId(self, parentId: str):
        self.__parentId = parentId


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def authorName(self):
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName


    @property
    def fullName(self):
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def xwikiRelativeUrl(self):
        return self.__xwikiRelativeUrl

    @xwikiRelativeUrl.setter
    def xwikiRelativeUrl(self, xwikiRelativeUrl: str):
        self.__xwikiRelativeUrl = xwikiRelativeUrl


    @property
    def xwikiAbsoluteUrl(self):
        return self.__xwikiAbsoluteUrl

    @xwikiAbsoluteUrl.setter
    def xwikiAbsoluteUrl(self, xwikiAbsoluteUrl: str):
        self.__xwikiAbsoluteUrl = xwikiAbsoluteUrl


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, wiki: str):
        self.__wiki = wiki


    @property
    def syntax(self):
        return self.__syntax

    @syntax.setter
    def syntax(self, syntax: str):
        self.__syntax = syntax


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def xwiki_PageSummary78(self):
        return self.__xwiki_PageSummary78

    @xwiki_PageSummary78.setter
    def xwiki_PageSummary78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_PageSummary__xwiki_PageSummary78", None)
        self.__xwiki_PageSummary78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Translations79"):
                opp_val = getattr(old_value, "xwiki_Translations79", None)
                if opp_val == self:
                    setattr(old_value, "xwiki_Translations79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Translations79"):
                opp_val = getattr(value, "xwiki_Translations79", None)
                setattr(value, "xwiki_Translations79", self)

    @property
    def xwiki_PageSummary(self):
        return self.__xwiki_PageSummary

    @xwiki_PageSummary.setter
    def xwiki_PageSummary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_PageSummary__xwiki_PageSummary", None)
        self.__xwiki_PageSummary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_PagesType76"):
                opp_val = getattr(old_value, "xwiki_PagesType76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_PagesType76"):
                opp_val = getattr(value, "xwiki_PagesType76", None)
                if opp_val is None:
                    setattr(value, "xwiki_PagesType76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Space(LinkCollection):

    def __init__(self, xwikiAbsoluteUrl: str, id: str, wiki: str, name: str, home: str, xwikiRelativeUrl: str, xwiki_Space: "xwiki_DocumentRoot" = None, xwiki_Space93: "xwiki_SpacesType" = None):
        self.xwikiAbsoluteUrl = xwikiAbsoluteUrl
        self.id = id
        self.wiki = wiki
        self.name = name
        self.home = home
        self.xwikiRelativeUrl = xwikiRelativeUrl
        self.xwiki_Space = xwiki_Space
        self.xwiki_Space93 = xwiki_Space93
        
        pass
    @property
    def xwikiAbsoluteUrl(self):
        return self.__xwikiAbsoluteUrl

    @xwikiAbsoluteUrl.setter
    def xwikiAbsoluteUrl(self, xwikiAbsoluteUrl: str):
        self.__xwikiAbsoluteUrl = xwikiAbsoluteUrl


    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, wiki: str):
        self.__wiki = wiki


    @property
    def xwikiRelativeUrl(self):
        return self.__xwikiRelativeUrl

    @xwikiRelativeUrl.setter
    def xwikiRelativeUrl(self, xwikiRelativeUrl: str):
        self.__xwikiRelativeUrl = xwikiRelativeUrl


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def home(self):
        return self.__home

    @home.setter
    def home(self, home: str):
        self.__home = home


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def xwiki_Space(self):
        return self.__xwiki_Space

    @xwiki_Space.setter
    def xwiki_Space(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Space__xwiki_Space", None)
        self.__xwiki_Space = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot49"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot49"):
                opp_val = getattr(value, "xwiki_DocumentRoot49", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Space93(self):
        return self.__xwiki_Space93

    @xwiki_Space93.setter
    def xwiki_Space93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Space__xwiki_Space93", None)
        self.__xwiki_Space93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_SpacesType92"):
                opp_val = getattr(old_value, "xwiki_SpacesType92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_SpacesType92"):
                opp_val = getattr(value, "xwiki_SpacesType92", None)
                if opp_val is None:
                    setattr(value, "xwiki_SpacesType92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_Translation(LinkCollection):

    def __init__(self, language: str, xwiki_Translation: "xwiki_Translations" = None):
        self.language = language
        self.xwiki_Translation = xwiki_Translation
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def xwiki_Translation(self):
        return self.__xwiki_Translation

    @xwiki_Translation.setter
    def xwiki_Translation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Translation__xwiki_Translation", None)
        self.__xwiki_Translation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Translations98"):
                opp_val = getattr(old_value, "xwiki_Translations98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Translations98"):
                opp_val = getattr(value, "xwiki_Translations98", None)
                if opp_val is None:
                    setattr(value, "xwiki_Translations98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_SpacesType(LinkCollection):

    pass
class xwiki_PagesType(LinkCollection):

    pass
class xwiki_Syntaxes(LinkCollection):

    def __init__(self, syntax: str, xwiki_Syntaxes104: "xwiki_XWiki" = None, xwiki_Syntaxes: "xwiki_DocumentRoot" = None):
        self.syntax = syntax
        self.xwiki_Syntaxes104 = xwiki_Syntaxes104
        self.xwiki_Syntaxes = xwiki_Syntaxes
        
        pass
    @property
    def syntax(self):
        return self.__syntax

    @syntax.setter
    def syntax(self, syntax: str):
        self.__syntax = syntax


    @property
    def xwiki_Syntaxes(self):
        return self.__xwiki_Syntaxes

    @xwiki_Syntaxes.setter
    def xwiki_Syntaxes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Syntaxes__xwiki_Syntaxes", None)
        self.__xwiki_Syntaxes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot53"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot53"):
                opp_val = getattr(value, "xwiki_DocumentRoot53", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Syntaxes104(self):
        return self.__xwiki_Syntaxes104

    @xwiki_Syntaxes104.setter
    def xwiki_Syntaxes104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Syntaxes__xwiki_Syntaxes104", None)
        self.__xwiki_Syntaxes104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_XWiki103"):
                opp_val = getattr(old_value, "xwiki_XWiki103", None)
                if opp_val == self:
                    setattr(old_value, "xwiki_XWiki103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_XWiki103"):
                opp_val = getattr(value, "xwiki_XWiki103", None)
                setattr(value, "xwiki_XWiki103", self)

class xwiki_Comment(LinkCollection):

    def __init__(self, id: str, pageId: str, author: str, authorName: str, date: str, highlight: str, text: str, replyTo: str, xwiki_Comment: "xwiki_CommentsType" = None, xwiki_Comment23: "xwiki_DocumentRoot" = None):
        self.id = id
        self.pageId = pageId
        self.author = author
        self.authorName = authorName
        self.date = date
        self.highlight = highlight
        self.text = text
        self.replyTo = replyTo
        self.xwiki_Comment = xwiki_Comment
        self.xwiki_Comment23 = xwiki_Comment23
        
        pass
    @property
    def replyTo(self):
        return self.__replyTo

    @replyTo.setter
    def replyTo(self, replyTo: str):
        self.__replyTo = replyTo


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def highlight(self):
        return self.__highlight

    @highlight.setter
    def highlight(self, highlight: str):
        self.__highlight = highlight


    @property
    def authorName(self):
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def pageId(self):
        return self.__pageId

    @pageId.setter
    def pageId(self, pageId: str):
        self.__pageId = pageId


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


    @property
    def xwiki_Comment(self):
        return self.__xwiki_Comment

    @xwiki_Comment.setter
    def xwiki_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Comment__xwiki_Comment", None)
        self.__xwiki_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_CommentsType"):
                opp_val = getattr(old_value, "xwiki_CommentsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_CommentsType"):
                opp_val = getattr(value, "xwiki_CommentsType", None)
                if opp_val is None:
                    setattr(value, "xwiki_CommentsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Comment23(self):
        return self.__xwiki_Comment23

    @xwiki_Comment23.setter
    def xwiki_Comment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Comment__xwiki_Comment23", None)
        self.__xwiki_Comment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot22"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot22"):
                opp_val = getattr(value, "xwiki_DocumentRoot22", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_HistoryType(LinkCollection):

    pass
class xwiki_SearchResult(LinkCollection):

    def __init__(self, type: str, id: str, pageFullName: str, title: str, wiki: str, space: str, pageName: str, modified: str, author: str, authorName: str, version: str, language: str, className: str, objectNumber: str, filename: str, score: str, xwiki_SearchResult: "xwiki_DocumentRoot" = None, xwiki_SearchResult86: "xwiki_Object" = None, xwiki_SearchResult90: "xwiki_SearchResultsType" = None):
        self.type = type
        self.id = id
        self.pageFullName = pageFullName
        self.title = title
        self.wiki = wiki
        self.space = space
        self.pageName = pageName
        self.modified = modified
        self.author = author
        self.authorName = authorName
        self.version = version
        self.language = language
        self.className = className
        self.objectNumber = objectNumber
        self.filename = filename
        self.score = score
        self.xwiki_SearchResult = xwiki_SearchResult
        self.xwiki_SearchResult86 = xwiki_SearchResult86
        self.xwiki_SearchResult90 = xwiki_SearchResult90
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def pageName(self):
        return self.__pageName

    @pageName.setter
    def pageName(self, pageName: str):
        self.__pageName = pageName


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score: str):
        self.__score = score


    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, wiki: str):
        self.__wiki = wiki


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def modified(self):
        return self.__modified

    @modified.setter
    def modified(self, modified: str):
        self.__modified = modified


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def pageFullName(self):
        return self.__pageFullName

    @pageFullName.setter
    def pageFullName(self, pageFullName: str):
        self.__pageFullName = pageFullName


    @property
    def authorName(self):
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def objectNumber(self):
        return self.__objectNumber

    @objectNumber.setter
    def objectNumber(self, objectNumber: str):
        self.__objectNumber = objectNumber


    @property
    def xwiki_SearchResult86(self):
        return self.__xwiki_SearchResult86

    @xwiki_SearchResult86.setter
    def xwiki_SearchResult86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_SearchResult__xwiki_SearchResult86", None)
        self.__xwiki_SearchResult86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_Object87"):
                opp_val = getattr(old_value, "xwiki_Object87", None)
                if opp_val == self:
                    setattr(old_value, "xwiki_Object87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_Object87"):
                opp_val = getattr(value, "xwiki_Object87", None)
                setattr(value, "xwiki_Object87", self)

    @property
    def xwiki_SearchResult90(self):
        return self.__xwiki_SearchResult90

    @xwiki_SearchResult90.setter
    def xwiki_SearchResult90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_SearchResult__xwiki_SearchResult90", None)
        self.__xwiki_SearchResult90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_SearchResultsType89"):
                opp_val = getattr(old_value, "xwiki_SearchResultsType89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_SearchResultsType89"):
                opp_val = getattr(value, "xwiki_SearchResultsType89", None)
                if opp_val is None:
                    setattr(value, "xwiki_SearchResultsType89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_SearchResult(self):
        return self.__xwiki_SearchResult

    @xwiki_SearchResult.setter
    def xwiki_SearchResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_SearchResult__xwiki_SearchResult", None)
        self.__xwiki_SearchResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot45"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot45"):
                opp_val = getattr(value, "xwiki_DocumentRoot45", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_HistorySummary(LinkCollection):

    def __init__(self, pageId: str, wiki: str, space: str, name: str, version: str, majorVersion: str, minorVersion: str, modified: str, modifier: str, modifierName: str, language: str, comment: str, xwiki_HistorySummary: "xwiki_HistoryType" = None):
        self.pageId = pageId
        self.wiki = wiki
        self.space = space
        self.name = name
        self.version = version
        self.majorVersion = majorVersion
        self.minorVersion = minorVersion
        self.modified = modified
        self.modifier = modifier
        self.modifierName = modifierName
        self.language = language
        self.comment = comment
        self.xwiki_HistorySummary = xwiki_HistorySummary
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def minorVersion(self):
        return self.__minorVersion

    @minorVersion.setter
    def minorVersion(self, minorVersion: str):
        self.__minorVersion = minorVersion


    @property
    def modified(self):
        return self.__modified

    @modified.setter
    def modified(self, modified: str):
        self.__modified = modified


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier


    @property
    def wiki(self):
        return self.__wiki

    @wiki.setter
    def wiki(self, wiki: str):
        self.__wiki = wiki


    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def pageId(self):
        return self.__pageId

    @pageId.setter
    def pageId(self, pageId: str):
        self.__pageId = pageId


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def majorVersion(self):
        return self.__majorVersion

    @majorVersion.setter
    def majorVersion(self, majorVersion: str):
        self.__majorVersion = majorVersion


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def modifierName(self):
        return self.__modifierName

    @modifierName.setter
    def modifierName(self, modifierName: str):
        self.__modifierName = modifierName


    @property
    def xwiki_HistorySummary(self):
        return self.__xwiki_HistorySummary

    @xwiki_HistorySummary.setter
    def xwiki_HistorySummary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_HistorySummary__xwiki_HistorySummary", None)
        self.__xwiki_HistorySummary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_HistoryType67"):
                opp_val = getattr(old_value, "xwiki_HistoryType67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_HistoryType67"):
                opp_val = getattr(value, "xwiki_HistoryType67", None)
                if opp_val is None:
                    setattr(value, "xwiki_HistoryType67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xwiki_ObjectsType(LinkCollection):

    pass
class xwiki_AttachmentsType(LinkCollection):

    pass
class xwiki_CommentsType(LinkCollection):

    pass
class xwiki_Attachment(LinkCollection):

    def __init__(self, version: str, pageId: str, pageVersion: str, mimeType: str, author: str, authorName: str, date: str, xwikiRelativeUrl: str, xwikiAbsoluteUrl: str, id: str, name: str, size: str, xwiki_Attachment: "xwiki_AttachmentsType" = None, xwiki_Attachment11: "xwiki_DocumentRoot" = None):
        self.version = version
        self.pageId = pageId
        self.pageVersion = pageVersion
        self.mimeType = mimeType
        self.author = author
        self.authorName = authorName
        self.date = date
        self.xwikiRelativeUrl = xwikiRelativeUrl
        self.xwikiAbsoluteUrl = xwikiAbsoluteUrl
        self.id = id
        self.name = name
        self.size = size
        self.xwiki_Attachment = xwiki_Attachment
        self.xwiki_Attachment11 = xwiki_Attachment11
        
        pass
    @property
    def mimeType(self):
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType


    @property
    def authorName(self):
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def xwikiAbsoluteUrl(self):
        return self.__xwikiAbsoluteUrl

    @xwikiAbsoluteUrl.setter
    def xwikiAbsoluteUrl(self, xwikiAbsoluteUrl: str):
        self.__xwikiAbsoluteUrl = xwikiAbsoluteUrl


    @property
    def pageVersion(self):
        return self.__pageVersion

    @pageVersion.setter
    def pageVersion(self, pageVersion: str):
        self.__pageVersion = pageVersion


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def pageId(self):
        return self.__pageId

    @pageId.setter
    def pageId(self, pageId: str):
        self.__pageId = pageId


    @property
    def xwikiRelativeUrl(self):
        return self.__xwikiRelativeUrl

    @xwikiRelativeUrl.setter
    def xwikiRelativeUrl(self, xwikiRelativeUrl: str):
        self.__xwikiRelativeUrl = xwikiRelativeUrl


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def xwiki_Attachment11(self):
        return self.__xwiki_Attachment11

    @xwiki_Attachment11.setter
    def xwiki_Attachment11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Attachment__xwiki_Attachment11", None)
        self.__xwiki_Attachment11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_DocumentRoot10"):
                opp_val = getattr(old_value, "xwiki_DocumentRoot10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_DocumentRoot10"):
                opp_val = getattr(value, "xwiki_DocumentRoot10", None)
                if opp_val is None:
                    setattr(value, "xwiki_DocumentRoot10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xwiki_Attachment(self):
        return self.__xwiki_Attachment

    @xwiki_Attachment.setter
    def xwiki_Attachment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xwiki_Attachment__xwiki_Attachment", None)
        self.__xwiki_Attachment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xwiki_AttachmentsType"):
                opp_val = getattr(old_value, "xwiki_AttachmentsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xwiki_AttachmentsType"):
                opp_val = getattr(value, "xwiki_AttachmentsType", None)
                if opp_val is None:
                    setattr(value, "xwiki_AttachmentsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
