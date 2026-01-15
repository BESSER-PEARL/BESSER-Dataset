from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class docbook_EStringToStringMapEntry:

    pass
class docbook_DocumentRoot:

    def __init__(self, mixed: str, info: str, para: str, title: str, docbook_DocumentRoot: set["docbook_EStringToStringMapEntry"] = None, docbook_DocumentRoot5: set["docbook_EStringToStringMapEntry"] = None, docbook_DocumentRoot8: set["docbook_BookType"] = None, docbook_DocumentRoot11: set["docbook_ChapterType"] = None, docbook_DocumentRoot14: set["docbook_Sect1Type"] = None):
        self.mixed = mixed
        self.info = info
        self.para = para
        self.title = title
        self.docbook_DocumentRoot = docbook_DocumentRoot if docbook_DocumentRoot is not None else set()
        self.docbook_DocumentRoot5 = docbook_DocumentRoot5 if docbook_DocumentRoot5 is not None else set()
        self.docbook_DocumentRoot8 = docbook_DocumentRoot8 if docbook_DocumentRoot8 is not None else set()
        self.docbook_DocumentRoot11 = docbook_DocumentRoot11 if docbook_DocumentRoot11 is not None else set()
        self.docbook_DocumentRoot14 = docbook_DocumentRoot14 if docbook_DocumentRoot14 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def para(self) -> str:
        return self.__para

    @para.setter
    def para(self, para: str):
        self.__para = para

    @property
    def docbook_DocumentRoot8(self):
        return self.__docbook_DocumentRoot8

    @docbook_DocumentRoot8.setter
    def docbook_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_DocumentRoot__docbook_DocumentRoot8", None)
        self.__docbook_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_BookType9"):
                    opp_val = getattr(item, "docbook_BookType9", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_BookType9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_BookType9"):
                    opp_val = getattr(item, "docbook_BookType9", None)
                    
                    setattr(item, "docbook_BookType9", self)
                    

    @property
    def docbook_DocumentRoot5(self):
        return self.__docbook_DocumentRoot5

    @docbook_DocumentRoot5.setter
    def docbook_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_DocumentRoot__docbook_DocumentRoot5", None)
        self.__docbook_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "docbook_EStringToStringMapEntry6", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_EStringToStringMapEntry6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "docbook_EStringToStringMapEntry6", None)
                    
                    setattr(item, "docbook_EStringToStringMapEntry6", self)
                    

    @property
    def docbook_DocumentRoot(self):
        return self.__docbook_DocumentRoot

    @docbook_DocumentRoot.setter
    def docbook_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_DocumentRoot__docbook_DocumentRoot", None)
        self.__docbook_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_EStringToStringMapEntry"):
                    opp_val = getattr(item, "docbook_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_EStringToStringMapEntry"):
                    opp_val = getattr(item, "docbook_EStringToStringMapEntry", None)
                    
                    setattr(item, "docbook_EStringToStringMapEntry", self)
                    

    @property
    def docbook_DocumentRoot14(self):
        return self.__docbook_DocumentRoot14

    @docbook_DocumentRoot14.setter
    def docbook_DocumentRoot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_DocumentRoot__docbook_DocumentRoot14", None)
        self.__docbook_DocumentRoot14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_Sect1Type15"):
                    opp_val = getattr(item, "docbook_Sect1Type15", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_Sect1Type15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_Sect1Type15"):
                    opp_val = getattr(item, "docbook_Sect1Type15", None)
                    
                    setattr(item, "docbook_Sect1Type15", self)
                    

    @property
    def docbook_DocumentRoot11(self):
        return self.__docbook_DocumentRoot11

    @docbook_DocumentRoot11.setter
    def docbook_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_DocumentRoot__docbook_DocumentRoot11", None)
        self.__docbook_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_ChapterType12"):
                    opp_val = getattr(item, "docbook_ChapterType12", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_ChapterType12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_ChapterType12"):
                    opp_val = getattr(item, "docbook_ChapterType12", None)
                    
                    setattr(item, "docbook_ChapterType12", self)
                    

class docbook_Sect1Type:

    def __init__(self, mixed: str, title: str, para: str, docbook_Sect1Type: "docbook_ChapterType" = None, docbook_Sect1Type15: "docbook_DocumentRoot" = None):
        self.mixed = mixed
        self.title = title
        self.para = para
        self.docbook_Sect1Type = docbook_Sect1Type
        self.docbook_Sect1Type15 = docbook_Sect1Type15
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def para(self) -> str:
        return self.__para

    @para.setter
    def para(self, para: str):
        self.__para = para

    @property
    def docbook_Sect1Type15(self):
        return self.__docbook_Sect1Type15

    @docbook_Sect1Type15.setter
    def docbook_Sect1Type15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Sect1Type__docbook_Sect1Type15", None)
        self.__docbook_Sect1Type15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_DocumentRoot14"):
                opp_val = getattr(old_value, "docbook_DocumentRoot14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_DocumentRoot14"):
                opp_val = getattr(value, "docbook_DocumentRoot14", None)
                if opp_val is None:
                    setattr(value, "docbook_DocumentRoot14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docbook_Sect1Type(self):
        return self.__docbook_Sect1Type

    @docbook_Sect1Type.setter
    def docbook_Sect1Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Sect1Type__docbook_Sect1Type", None)
        self.__docbook_Sect1Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_ChapterType2"):
                opp_val = getattr(old_value, "docbook_ChapterType2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_ChapterType2"):
                opp_val = getattr(value, "docbook_ChapterType2", None)
                if opp_val is None:
                    setattr(value, "docbook_ChapterType2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class docbook_BookType:

    def __init__(self, title: str, info: str, docbook_BookType: set["docbook_ChapterType"] = None, docbook_BookType9: "docbook_DocumentRoot" = None):
        self.title = title
        self.info = info
        self.docbook_BookType = docbook_BookType if docbook_BookType is not None else set()
        self.docbook_BookType9 = docbook_BookType9
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def docbook_BookType(self):
        return self.__docbook_BookType

    @docbook_BookType.setter
    def docbook_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_BookType__docbook_BookType", None)
        self.__docbook_BookType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_ChapterType"):
                    opp_val = getattr(item, "docbook_ChapterType", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_ChapterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_ChapterType"):
                    opp_val = getattr(item, "docbook_ChapterType", None)
                    
                    setattr(item, "docbook_ChapterType", self)
                    

    @property
    def docbook_BookType9(self):
        return self.__docbook_BookType9

    @docbook_BookType9.setter
    def docbook_BookType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_BookType__docbook_BookType9", None)
        self.__docbook_BookType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_DocumentRoot8"):
                opp_val = getattr(old_value, "docbook_DocumentRoot8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_DocumentRoot8"):
                opp_val = getattr(value, "docbook_DocumentRoot8", None)
                if opp_val is None:
                    setattr(value, "docbook_DocumentRoot8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class docbook_ChapterType:

    def __init__(self, mixed: str, title: str, para: str, docbook_ChapterType: "docbook_BookType" = None, docbook_ChapterType2: set["docbook_Sect1Type"] = None, docbook_ChapterType12: "docbook_DocumentRoot" = None):
        self.mixed = mixed
        self.title = title
        self.para = para
        self.docbook_ChapterType = docbook_ChapterType
        self.docbook_ChapterType2 = docbook_ChapterType2 if docbook_ChapterType2 is not None else set()
        self.docbook_ChapterType12 = docbook_ChapterType12
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def para(self) -> str:
        return self.__para

    @para.setter
    def para(self, para: str):
        self.__para = para

    @property
    def docbook_ChapterType(self):
        return self.__docbook_ChapterType

    @docbook_ChapterType.setter
    def docbook_ChapterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_ChapterType__docbook_ChapterType", None)
        self.__docbook_ChapterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_BookType"):
                opp_val = getattr(old_value, "docbook_BookType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_BookType"):
                opp_val = getattr(value, "docbook_BookType", None)
                if opp_val is None:
                    setattr(value, "docbook_BookType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docbook_ChapterType12(self):
        return self.__docbook_ChapterType12

    @docbook_ChapterType12.setter
    def docbook_ChapterType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_ChapterType__docbook_ChapterType12", None)
        self.__docbook_ChapterType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_DocumentRoot11"):
                opp_val = getattr(old_value, "docbook_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_DocumentRoot11"):
                opp_val = getattr(value, "docbook_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "docbook_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def docbook_ChapterType2(self):
        return self.__docbook_ChapterType2

    @docbook_ChapterType2.setter
    def docbook_ChapterType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_ChapterType__docbook_ChapterType2", None)
        self.__docbook_ChapterType2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docbook_Sect1Type"):
                    opp_val = getattr(item, "docbook_Sect1Type", None)
                    
                    if opp_val == self:
                        setattr(item, "docbook_Sect1Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docbook_Sect1Type"):
                    opp_val = getattr(item, "docbook_Sect1Type", None)
                    
                    setattr(item, "docbook_Sect1Type", self)
                    
