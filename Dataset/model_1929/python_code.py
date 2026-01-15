from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Docbook_VarListEntryType:

    def __init__(self, spacing: str, termlength: str, Docbook_VarListEntryType: "Docbook_VariableListType" = None, Docbook_VarListEntryType440: set["Docbook_TermType"] = None, Docbook_VarListEntryType443: "Docbook_ListitemType" = None):
        self.spacing = spacing
        self.termlength = termlength
        self.Docbook_VarListEntryType = Docbook_VarListEntryType
        self.Docbook_VarListEntryType440 = Docbook_VarListEntryType440 if Docbook_VarListEntryType440 is not None else set()
        self.Docbook_VarListEntryType443 = Docbook_VarListEntryType443
        
    @property
    def termlength(self) -> str:
        return self.__termlength

    @termlength.setter
    def termlength(self, termlength: str):
        self.__termlength = termlength

    @property
    def spacing(self) -> str:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: str):
        self.__spacing = spacing

    @property
    def Docbook_VarListEntryType(self):
        return self.__Docbook_VarListEntryType

    @Docbook_VarListEntryType.setter
    def Docbook_VarListEntryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_VarListEntryType__Docbook_VarListEntryType", None)
        self.__Docbook_VarListEntryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_VariableListType438"):
                opp_val = getattr(old_value, "Docbook_VariableListType438", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_VariableListType438"):
                opp_val = getattr(value, "Docbook_VariableListType438", None)
                if opp_val is None:
                    setattr(value, "Docbook_VariableListType438", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_VarListEntryType440(self):
        return self.__Docbook_VarListEntryType440

    @Docbook_VarListEntryType440.setter
    def Docbook_VarListEntryType440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_VarListEntryType__Docbook_VarListEntryType440", None)
        self.__Docbook_VarListEntryType440 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TermType441"):
                    opp_val = getattr(item, "Docbook_TermType441", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TermType441", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TermType441"):
                    opp_val = getattr(item, "Docbook_TermType441", None)
                    
                    setattr(item, "Docbook_TermType441", self)
                    

    @property
    def Docbook_VarListEntryType443(self):
        return self.__Docbook_VarListEntryType443

    @Docbook_VarListEntryType443.setter
    def Docbook_VarListEntryType443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_VarListEntryType__Docbook_VarListEntryType443", None)
        self.__Docbook_VarListEntryType443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ListitemType444"):
                opp_val = getattr(old_value, "Docbook_ListitemType444", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ListitemType444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ListitemType444"):
                opp_val = getattr(value, "Docbook_ListitemType444", None)
                setattr(value, "Docbook_ListitemType444", self)

class Docbook_TermType:

    def __init__(self, mixed: str, Docbook_TermType: set["Docbook_EmphasisType"] = None, Docbook_TermType402: set["Docbook_OptionType"] = None, Docbook_TermType405: set["Docbook_FileNameType"] = None, Docbook_TermType408: set["Docbook_EnvarType"] = None, Docbook_TermType441: "Docbook_VarListEntryType" = None):
        self.mixed = mixed
        self.Docbook_TermType = Docbook_TermType if Docbook_TermType is not None else set()
        self.Docbook_TermType402 = Docbook_TermType402 if Docbook_TermType402 is not None else set()
        self.Docbook_TermType405 = Docbook_TermType405 if Docbook_TermType405 is not None else set()
        self.Docbook_TermType408 = Docbook_TermType408 if Docbook_TermType408 is not None else set()
        self.Docbook_TermType441 = Docbook_TermType441
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_TermType408(self):
        return self.__Docbook_TermType408

    @Docbook_TermType408.setter
    def Docbook_TermType408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TermType__Docbook_TermType408", None)
        self.__Docbook_TermType408 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EnvarType409"):
                    opp_val = getattr(item, "Docbook_EnvarType409", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EnvarType409", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EnvarType409"):
                    opp_val = getattr(item, "Docbook_EnvarType409", None)
                    
                    setattr(item, "Docbook_EnvarType409", self)
                    

    @property
    def Docbook_TermType(self):
        return self.__Docbook_TermType

    @Docbook_TermType.setter
    def Docbook_TermType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TermType__Docbook_TermType", None)
        self.__Docbook_TermType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType400"):
                    opp_val = getattr(item, "Docbook_EmphasisType400", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType400"):
                    opp_val = getattr(item, "Docbook_EmphasisType400", None)
                    
                    setattr(item, "Docbook_EmphasisType400", self)
                    

    @property
    def Docbook_TermType441(self):
        return self.__Docbook_TermType441

    @Docbook_TermType441.setter
    def Docbook_TermType441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TermType__Docbook_TermType441", None)
        self.__Docbook_TermType441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_VarListEntryType440"):
                opp_val = getattr(old_value, "Docbook_VarListEntryType440", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_VarListEntryType440"):
                opp_val = getattr(value, "Docbook_VarListEntryType440", None)
                if opp_val is None:
                    setattr(value, "Docbook_VarListEntryType440", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TermType402(self):
        return self.__Docbook_TermType402

    @Docbook_TermType402.setter
    def Docbook_TermType402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TermType__Docbook_TermType402", None)
        self.__Docbook_TermType402 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OptionType403"):
                    opp_val = getattr(item, "Docbook_OptionType403", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OptionType403", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OptionType403"):
                    opp_val = getattr(item, "Docbook_OptionType403", None)
                    
                    setattr(item, "Docbook_OptionType403", self)
                    

    @property
    def Docbook_TermType405(self):
        return self.__Docbook_TermType405

    @Docbook_TermType405.setter
    def Docbook_TermType405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TermType__Docbook_TermType405", None)
        self.__Docbook_TermType405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FileNameType406"):
                    opp_val = getattr(item, "Docbook_FileNameType406", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FileNameType406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FileNameType406"):
                    opp_val = getattr(item, "Docbook_FileNameType406", None)
                    
                    setattr(item, "Docbook_FileNameType406", self)
                    

class Docbook_SegType:

    def __init__(self, group: str, mixed: str, errorcode: str, errortext: str, Docbook_SegType: "Docbook_SegListItemType" = None):
        self.group = group
        self.mixed = mixed
        self.errorcode = errorcode
        self.errortext = errortext
        self.Docbook_SegType = Docbook_SegType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def errorcode(self) -> str:
        return self.__errorcode

    @errorcode.setter
    def errorcode(self, errorcode: str):
        self.__errorcode = errorcode

    @property
    def errortext(self) -> str:
        return self.__errortext

    @errortext.setter
    def errortext(self, errortext: str):
        self.__errortext = errortext

    @property
    def Docbook_SegType(self):
        return self.__Docbook_SegType

    @Docbook_SegType.setter
    def Docbook_SegType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SegType__Docbook_SegType", None)
        self.__Docbook_SegType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SegListItemType"):
                opp_val = getattr(old_value, "Docbook_SegListItemType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SegListItemType"):
                opp_val = getattr(value, "Docbook_SegListItemType", None)
                if opp_val is None:
                    setattr(value, "Docbook_SegListItemType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_SegListItemType:

    pass
class Docbook_RevnumberType:

    def __init__(self, mixed: str, Docbook_RevnumberType: "Docbook_RevisionType" = None, Docbook_RevnumberType333: set["Docbook_UlinkType"] = None):
        self.mixed = mixed
        self.Docbook_RevnumberType = Docbook_RevnumberType
        self.Docbook_RevnumberType333 = Docbook_RevnumberType333 if Docbook_RevnumberType333 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_RevnumberType(self):
        return self.__Docbook_RevnumberType

    @Docbook_RevnumberType.setter
    def Docbook_RevnumberType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RevnumberType__Docbook_RevnumberType", None)
        self.__Docbook_RevnumberType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevisionType324"):
                opp_val = getattr(old_value, "Docbook_RevisionType324", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevisionType324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevisionType324"):
                opp_val = getattr(value, "Docbook_RevisionType324", None)
                setattr(value, "Docbook_RevisionType324", self)

    @property
    def Docbook_RevnumberType333(self):
        return self.__Docbook_RevnumberType333

    @Docbook_RevnumberType333.setter
    def Docbook_RevnumberType333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RevnumberType__Docbook_RevnumberType333", None)
        self.__Docbook_RevnumberType333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType334"):
                    opp_val = getattr(item, "Docbook_UlinkType334", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType334"):
                    opp_val = getattr(item, "Docbook_UlinkType334", None)
                    
                    setattr(item, "Docbook_UlinkType334", self)
                    

class Docbook_RevdescriptionType:

    def __init__(self, mixed: str, Docbook_RevdescriptionType: set["Docbook_ParaType"] = None, Docbook_RevdescriptionType331: "Docbook_RevisionType" = None):
        self.mixed = mixed
        self.Docbook_RevdescriptionType = Docbook_RevdescriptionType if Docbook_RevdescriptionType is not None else set()
        self.Docbook_RevdescriptionType331 = Docbook_RevdescriptionType331
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_RevdescriptionType331(self):
        return self.__Docbook_RevdescriptionType331

    @Docbook_RevdescriptionType331.setter
    def Docbook_RevdescriptionType331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RevdescriptionType__Docbook_RevdescriptionType331", None)
        self.__Docbook_RevdescriptionType331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevisionType330"):
                opp_val = getattr(old_value, "Docbook_RevisionType330", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevisionType330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevisionType330"):
                opp_val = getattr(value, "Docbook_RevisionType330", None)
                setattr(value, "Docbook_RevisionType330", self)

    @property
    def Docbook_RevdescriptionType(self):
        return self.__Docbook_RevdescriptionType

    @Docbook_RevdescriptionType.setter
    def Docbook_RevdescriptionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RevdescriptionType__Docbook_RevdescriptionType", None)
        self.__Docbook_RevdescriptionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType320"):
                    opp_val = getattr(item, "Docbook_ParaType320", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType320"):
                    opp_val = getattr(item, "Docbook_ParaType320", None)
                    
                    setattr(item, "Docbook_ParaType320", self)
                    

class Docbook_RevisionType:

    pass
class Docbook_SegmentedListType:

    def __init__(self, group: str, segtitle: str, Docbook_SegmentedListType: "Docbook_RefSect1Type" = None, Docbook_SegmentedListType385: set["Docbook_SegListItemType"] = None):
        self.group = group
        self.segtitle = segtitle
        self.Docbook_SegmentedListType = Docbook_SegmentedListType
        self.Docbook_SegmentedListType385 = Docbook_SegmentedListType385 if Docbook_SegmentedListType385 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def segtitle(self) -> str:
        return self.__segtitle

    @segtitle.setter
    def segtitle(self, segtitle: str):
        self.__segtitle = segtitle

    @property
    def Docbook_SegmentedListType385(self):
        return self.__Docbook_SegmentedListType385

    @Docbook_SegmentedListType385.setter
    def Docbook_SegmentedListType385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SegmentedListType__Docbook_SegmentedListType385", None)
        self.__Docbook_SegmentedListType385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_SegListItemType386"):
                    opp_val = getattr(item, "Docbook_SegListItemType386", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_SegListItemType386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_SegListItemType386"):
                    opp_val = getattr(item, "Docbook_SegListItemType386", None)
                    
                    setattr(item, "Docbook_SegListItemType386", self)
                    

    @property
    def Docbook_SegmentedListType(self):
        return self.__Docbook_SegmentedListType

    @Docbook_SegmentedListType.setter
    def Docbook_SegmentedListType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SegmentedListType__Docbook_SegmentedListType", None)
        self.__Docbook_SegmentedListType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefSect1Type312"):
                opp_val = getattr(old_value, "Docbook_RefSect1Type312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefSect1Type312"):
                opp_val = getattr(value, "Docbook_RefSect1Type312", None)
                if opp_val is None:
                    setattr(value, "Docbook_RefSect1Type312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_RefEntryTitleType:

    def __init__(self, mixed: str, Docbook_RefEntryTitleType: "Docbook_RefMetaType" = None):
        self.mixed = mixed
        self.Docbook_RefEntryTitleType = Docbook_RefEntryTitleType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_RefEntryTitleType(self):
        return self.__Docbook_RefEntryTitleType

    @Docbook_RefEntryTitleType.setter
    def Docbook_RefEntryTitleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryTitleType__Docbook_RefEntryTitleType", None)
        self.__Docbook_RefEntryTitleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefMetaType301"):
                opp_val = getattr(old_value, "Docbook_RefMetaType301", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefMetaType301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefMetaType301"):
                opp_val = getattr(value, "Docbook_RefMetaType301", None)
                setattr(value, "Docbook_RefMetaType301", self)

class Docbook_RefEntryType:

    def __init__(self, version: str, Docbook_RefEntryType284: "Docbook_RefMetaType" = None, Docbook_RefEntryType286: "Docbook_RefNameDivType" = None, Docbook_RefEntryType288: "Docbook_RefSynopsisDivType" = None, Docbook_RefEntryType290: set["Docbook_RefSect1Type"] = None, Docbook_RefEntryType: "Docbook_InfoType" = None, Docbook_RefEntryType299: "Docbook_ReferenceType" = None):
        self.version = version
        self.Docbook_RefEntryType284 = Docbook_RefEntryType284
        self.Docbook_RefEntryType286 = Docbook_RefEntryType286
        self.Docbook_RefEntryType288 = Docbook_RefEntryType288
        self.Docbook_RefEntryType290 = Docbook_RefEntryType290 if Docbook_RefEntryType290 is not None else set()
        self.Docbook_RefEntryType = Docbook_RefEntryType
        self.Docbook_RefEntryType299 = Docbook_RefEntryType299
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def Docbook_RefEntryType284(self):
        return self.__Docbook_RefEntryType284

    @Docbook_RefEntryType284.setter
    def Docbook_RefEntryType284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType284", None)
        self.__Docbook_RefEntryType284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefMetaType"):
                opp_val = getattr(old_value, "Docbook_RefMetaType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefMetaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefMetaType"):
                opp_val = getattr(value, "Docbook_RefMetaType", None)
                setattr(value, "Docbook_RefMetaType", self)

    @property
    def Docbook_RefEntryType299(self):
        return self.__Docbook_RefEntryType299

    @Docbook_RefEntryType299.setter
    def Docbook_RefEntryType299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType299", None)
        self.__Docbook_RefEntryType299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ReferenceType298"):
                opp_val = getattr(old_value, "Docbook_ReferenceType298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ReferenceType298"):
                opp_val = getattr(value, "Docbook_ReferenceType298", None)
                if opp_val is None:
                    setattr(value, "Docbook_ReferenceType298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_RefEntryType(self):
        return self.__Docbook_RefEntryType

    @Docbook_RefEntryType.setter
    def Docbook_RefEntryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType", None)
        self.__Docbook_RefEntryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType282"):
                opp_val = getattr(old_value, "Docbook_InfoType282", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType282"):
                opp_val = getattr(value, "Docbook_InfoType282", None)
                setattr(value, "Docbook_InfoType282", self)

    @property
    def Docbook_RefEntryType286(self):
        return self.__Docbook_RefEntryType286

    @Docbook_RefEntryType286.setter
    def Docbook_RefEntryType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType286", None)
        self.__Docbook_RefEntryType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefNameDivType"):
                opp_val = getattr(old_value, "Docbook_RefNameDivType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefNameDivType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefNameDivType"):
                opp_val = getattr(value, "Docbook_RefNameDivType", None)
                setattr(value, "Docbook_RefNameDivType", self)

    @property
    def Docbook_RefEntryType288(self):
        return self.__Docbook_RefEntryType288

    @Docbook_RefEntryType288.setter
    def Docbook_RefEntryType288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType288", None)
        self.__Docbook_RefEntryType288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefSynopsisDivType"):
                opp_val = getattr(old_value, "Docbook_RefSynopsisDivType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefSynopsisDivType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefSynopsisDivType"):
                opp_val = getattr(value, "Docbook_RefSynopsisDivType", None)
                setattr(value, "Docbook_RefSynopsisDivType", self)

    @property
    def Docbook_RefEntryType290(self):
        return self.__Docbook_RefEntryType290

    @Docbook_RefEntryType290.setter
    def Docbook_RefEntryType290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefEntryType__Docbook_RefEntryType290", None)
        self.__Docbook_RefEntryType290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_RefSect1Type"):
                    opp_val = getattr(item, "Docbook_RefSect1Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_RefSect1Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_RefSect1Type"):
                    opp_val = getattr(item, "Docbook_RefSect1Type", None)
                    
                    setattr(item, "Docbook_RefSect1Type", self)
                    

class Docbook_RefSect1Type:

    def __init__(self, group: str, id: str, Docbook_RefSect1Type: "Docbook_RefEntryType" = None, Docbook_RefSect1Type303: "Docbook_TitleType" = None, Docbook_RefSect1Type306: set["Docbook_ParaType"] = None, Docbook_RefSect1Type309: set["Docbook_VariableListType"] = None, Docbook_RefSect1Type312: set["Docbook_SegmentedListType"] = None):
        self.group = group
        self.id = id
        self.Docbook_RefSect1Type = Docbook_RefSect1Type
        self.Docbook_RefSect1Type303 = Docbook_RefSect1Type303
        self.Docbook_RefSect1Type306 = Docbook_RefSect1Type306 if Docbook_RefSect1Type306 is not None else set()
        self.Docbook_RefSect1Type309 = Docbook_RefSect1Type309 if Docbook_RefSect1Type309 is not None else set()
        self.Docbook_RefSect1Type312 = Docbook_RefSect1Type312 if Docbook_RefSect1Type312 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def Docbook_RefSect1Type306(self):
        return self.__Docbook_RefSect1Type306

    @Docbook_RefSect1Type306.setter
    def Docbook_RefSect1Type306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefSect1Type__Docbook_RefSect1Type306", None)
        self.__Docbook_RefSect1Type306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType307"):
                    opp_val = getattr(item, "Docbook_ParaType307", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType307"):
                    opp_val = getattr(item, "Docbook_ParaType307", None)
                    
                    setattr(item, "Docbook_ParaType307", self)
                    

    @property
    def Docbook_RefSect1Type303(self):
        return self.__Docbook_RefSect1Type303

    @Docbook_RefSect1Type303.setter
    def Docbook_RefSect1Type303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefSect1Type__Docbook_RefSect1Type303", None)
        self.__Docbook_RefSect1Type303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType304"):
                opp_val = getattr(old_value, "Docbook_TitleType304", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType304"):
                opp_val = getattr(value, "Docbook_TitleType304", None)
                setattr(value, "Docbook_TitleType304", self)

    @property
    def Docbook_RefSect1Type312(self):
        return self.__Docbook_RefSect1Type312

    @Docbook_RefSect1Type312.setter
    def Docbook_RefSect1Type312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefSect1Type__Docbook_RefSect1Type312", None)
        self.__Docbook_RefSect1Type312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_SegmentedListType"):
                    opp_val = getattr(item, "Docbook_SegmentedListType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_SegmentedListType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_SegmentedListType"):
                    opp_val = getattr(item, "Docbook_SegmentedListType", None)
                    
                    setattr(item, "Docbook_SegmentedListType", self)
                    

    @property
    def Docbook_RefSect1Type309(self):
        return self.__Docbook_RefSect1Type309

    @Docbook_RefSect1Type309.setter
    def Docbook_RefSect1Type309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefSect1Type__Docbook_RefSect1Type309", None)
        self.__Docbook_RefSect1Type309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_VariableListType310"):
                    opp_val = getattr(item, "Docbook_VariableListType310", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_VariableListType310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_VariableListType310"):
                    opp_val = getattr(item, "Docbook_VariableListType310", None)
                    
                    setattr(item, "Docbook_VariableListType310", self)
                    

    @property
    def Docbook_RefSect1Type(self):
        return self.__Docbook_RefSect1Type

    @Docbook_RefSect1Type.setter
    def Docbook_RefSect1Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefSect1Type__Docbook_RefSect1Type", None)
        self.__Docbook_RefSect1Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefEntryType290"):
                opp_val = getattr(old_value, "Docbook_RefEntryType290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefEntryType290"):
                opp_val = getattr(value, "Docbook_RefEntryType290", None)
                if opp_val is None:
                    setattr(value, "Docbook_RefEntryType290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_RefSynopsisDivType:

    pass
class Docbook_RefNameDivType:

    def __init__(self, refname: str, refpurpose: str, refclass: str, Docbook_RefNameDivType: "Docbook_RefEntryType" = None):
        self.refname = refname
        self.refpurpose = refpurpose
        self.refclass = refclass
        self.Docbook_RefNameDivType = Docbook_RefNameDivType
        
    @property
    def refname(self) -> str:
        return self.__refname

    @refname.setter
    def refname(self, refname: str):
        self.__refname = refname

    @property
    def refpurpose(self) -> str:
        return self.__refpurpose

    @refpurpose.setter
    def refpurpose(self, refpurpose: str):
        self.__refpurpose = refpurpose

    @property
    def refclass(self) -> str:
        return self.__refclass

    @refclass.setter
    def refclass(self, refclass: str):
        self.__refclass = refclass

    @property
    def Docbook_RefNameDivType(self):
        return self.__Docbook_RefNameDivType

    @Docbook_RefNameDivType.setter
    def Docbook_RefNameDivType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefNameDivType__Docbook_RefNameDivType", None)
        self.__Docbook_RefNameDivType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefEntryType286"):
                opp_val = getattr(old_value, "Docbook_RefEntryType286", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefEntryType286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefEntryType286"):
                opp_val = getattr(value, "Docbook_RefEntryType286", None)
                setattr(value, "Docbook_RefEntryType286", self)

class Docbook_RefMetaType:

    def __init__(self, manvolnum: str, Docbook_RefMetaType: "Docbook_RefEntryType" = None, Docbook_RefMetaType301: "Docbook_RefEntryTitleType" = None):
        self.manvolnum = manvolnum
        self.Docbook_RefMetaType = Docbook_RefMetaType
        self.Docbook_RefMetaType301 = Docbook_RefMetaType301
        
    @property
    def manvolnum(self) -> str:
        return self.__manvolnum

    @manvolnum.setter
    def manvolnum(self, manvolnum: str):
        self.__manvolnum = manvolnum

    @property
    def Docbook_RefMetaType(self):
        return self.__Docbook_RefMetaType

    @Docbook_RefMetaType.setter
    def Docbook_RefMetaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefMetaType__Docbook_RefMetaType", None)
        self.__Docbook_RefMetaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefEntryType284"):
                opp_val = getattr(old_value, "Docbook_RefEntryType284", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefEntryType284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefEntryType284"):
                opp_val = getattr(value, "Docbook_RefEntryType284", None)
                setattr(value, "Docbook_RefEntryType284", self)

    @property
    def Docbook_RefMetaType301(self):
        return self.__Docbook_RefMetaType301

    @Docbook_RefMetaType301.setter
    def Docbook_RefMetaType301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_RefMetaType__Docbook_RefMetaType301", None)
        self.__Docbook_RefMetaType301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefEntryTitleType"):
                opp_val = getattr(old_value, "Docbook_RefEntryTitleType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefEntryTitleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefEntryTitleType"):
                opp_val = getattr(value, "Docbook_RefEntryTitleType", None)
                setattr(value, "Docbook_RefEntryTitleType", self)

class Docbook_VariableListType:

    pass
class Docbook_SurnameType:

    def __init__(self, mixed: str, Docbook_SurnameType: "Docbook_PersonnameType" = None):
        self.mixed = mixed
        self.Docbook_SurnameType = Docbook_SurnameType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_SurnameType(self):
        return self.__Docbook_SurnameType

    @Docbook_SurnameType.setter
    def Docbook_SurnameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SurnameType__Docbook_SurnameType", None)
        self.__Docbook_SurnameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PersonnameType259"):
                opp_val = getattr(old_value, "Docbook_PersonnameType259", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PersonnameType259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PersonnameType259"):
                opp_val = getattr(value, "Docbook_PersonnameType259", None)
                setattr(value, "Docbook_PersonnameType259", self)

class Docbook_ParameterType:

    def __init__(self, mixed: str, Docbook_ParameterType: "Docbook_ParamdefType" = None):
        self.mixed = mixed
        self.Docbook_ParameterType = Docbook_ParameterType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_ParameterType(self):
        return self.__Docbook_ParameterType

    @Docbook_ParameterType.setter
    def Docbook_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParameterType__Docbook_ParameterType", None)
        self.__Docbook_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParamdefType235"):
                opp_val = getattr(old_value, "Docbook_ParamdefType235", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ParamdefType235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParamdefType235"):
                opp_val = getattr(value, "Docbook_ParamdefType235", None)
                setattr(value, "Docbook_ParamdefType235", self)

class ItemizedlistType:

    pass
class Docbook_LegalNoticeType:

    def __init__(self, group: str, Docbook_LegalNoticeType: "Docbook_InfoType" = None, Docbook_LegalNoticeType202: "Docbook_TitleType" = None, Docbook_LegalNoticeType205: "Docbook_RevhistoryType" = None, Docbook_LegalNoticeType208: set["Docbook_ParaType"] = None, Docbook_LegalNoticeType211: set["Docbook_OrderedlistType"] = None):
        self.group = group
        self.Docbook_LegalNoticeType = Docbook_LegalNoticeType
        self.Docbook_LegalNoticeType202 = Docbook_LegalNoticeType202
        self.Docbook_LegalNoticeType205 = Docbook_LegalNoticeType205
        self.Docbook_LegalNoticeType208 = Docbook_LegalNoticeType208 if Docbook_LegalNoticeType208 is not None else set()
        self.Docbook_LegalNoticeType211 = Docbook_LegalNoticeType211 if Docbook_LegalNoticeType211 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def Docbook_LegalNoticeType208(self):
        return self.__Docbook_LegalNoticeType208

    @Docbook_LegalNoticeType208.setter
    def Docbook_LegalNoticeType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LegalNoticeType__Docbook_LegalNoticeType208", None)
        self.__Docbook_LegalNoticeType208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType209"):
                    opp_val = getattr(item, "Docbook_ParaType209", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType209"):
                    opp_val = getattr(item, "Docbook_ParaType209", None)
                    
                    setattr(item, "Docbook_ParaType209", self)
                    

    @property
    def Docbook_LegalNoticeType(self):
        return self.__Docbook_LegalNoticeType

    @Docbook_LegalNoticeType.setter
    def Docbook_LegalNoticeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LegalNoticeType__Docbook_LegalNoticeType", None)
        self.__Docbook_LegalNoticeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType197"):
                opp_val = getattr(old_value, "Docbook_InfoType197", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType197"):
                opp_val = getattr(value, "Docbook_InfoType197", None)
                setattr(value, "Docbook_InfoType197", self)

    @property
    def Docbook_LegalNoticeType202(self):
        return self.__Docbook_LegalNoticeType202

    @Docbook_LegalNoticeType202.setter
    def Docbook_LegalNoticeType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LegalNoticeType__Docbook_LegalNoticeType202", None)
        self.__Docbook_LegalNoticeType202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType203"):
                opp_val = getattr(old_value, "Docbook_TitleType203", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType203"):
                opp_val = getattr(value, "Docbook_TitleType203", None)
                setattr(value, "Docbook_TitleType203", self)

    @property
    def Docbook_LegalNoticeType211(self):
        return self.__Docbook_LegalNoticeType211

    @Docbook_LegalNoticeType211.setter
    def Docbook_LegalNoticeType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LegalNoticeType__Docbook_LegalNoticeType211", None)
        self.__Docbook_LegalNoticeType211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OrderedlistType212"):
                    opp_val = getattr(item, "Docbook_OrderedlistType212", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OrderedlistType212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OrderedlistType212"):
                    opp_val = getattr(item, "Docbook_OrderedlistType212", None)
                    
                    setattr(item, "Docbook_OrderedlistType212", self)
                    

    @property
    def Docbook_LegalNoticeType205(self):
        return self.__Docbook_LegalNoticeType205

    @Docbook_LegalNoticeType205.setter
    def Docbook_LegalNoticeType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LegalNoticeType__Docbook_LegalNoticeType205", None)
        self.__Docbook_LegalNoticeType205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevhistoryType206"):
                opp_val = getattr(old_value, "Docbook_RevhistoryType206", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevhistoryType206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevhistoryType206"):
                opp_val = getattr(value, "Docbook_RevhistoryType206", None)
                setattr(value, "Docbook_RevhistoryType206", self)

class Docbook_RevhistoryType:

    pass
class Docbook_SubtitleType:

    def __init__(self, mixed: str, group: str, Docbook_SubtitleType: "Docbook_InfoType" = None, Docbook_SubtitleType391: set["Docbook_PhraseType"] = None, Docbook_SubtitleType388: set["Docbook_EmphasisType"] = None):
        self.mixed = mixed
        self.group = group
        self.Docbook_SubtitleType = Docbook_SubtitleType
        self.Docbook_SubtitleType391 = Docbook_SubtitleType391 if Docbook_SubtitleType391 is not None else set()
        self.Docbook_SubtitleType388 = Docbook_SubtitleType388 if Docbook_SubtitleType388 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def Docbook_SubtitleType391(self):
        return self.__Docbook_SubtitleType391

    @Docbook_SubtitleType391.setter
    def Docbook_SubtitleType391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SubtitleType__Docbook_SubtitleType391", None)
        self.__Docbook_SubtitleType391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PhraseType392"):
                    opp_val = getattr(item, "Docbook_PhraseType392", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PhraseType392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PhraseType392"):
                    opp_val = getattr(item, "Docbook_PhraseType392", None)
                    
                    setattr(item, "Docbook_PhraseType392", self)
                    

    @property
    def Docbook_SubtitleType(self):
        return self.__Docbook_SubtitleType

    @Docbook_SubtitleType.setter
    def Docbook_SubtitleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SubtitleType__Docbook_SubtitleType", None)
        self.__Docbook_SubtitleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType179"):
                opp_val = getattr(old_value, "Docbook_InfoType179", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType179"):
                opp_val = getattr(value, "Docbook_InfoType179", None)
                setattr(value, "Docbook_InfoType179", self)

    @property
    def Docbook_SubtitleType388(self):
        return self.__Docbook_SubtitleType388

    @Docbook_SubtitleType388.setter
    def Docbook_SubtitleType388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SubtitleType__Docbook_SubtitleType388", None)
        self.__Docbook_SubtitleType388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType389"):
                    opp_val = getattr(item, "Docbook_EmphasisType389", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType389"):
                    opp_val = getattr(item, "Docbook_EmphasisType389", None)
                    
                    setattr(item, "Docbook_EmphasisType389", self)
                    

class Docbook_FuncsynopsisType:

    pass
class Docbook_FuncdefType:

    def __init__(self, mixed: str, Docbook_FuncdefType: "Docbook_FunctionType" = None, Docbook_FuncdefType155: "Docbook_FuncprototypeType" = None):
        self.mixed = mixed
        self.Docbook_FuncdefType = Docbook_FuncdefType
        self.Docbook_FuncdefType155 = Docbook_FuncdefType155
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_FuncdefType(self):
        return self.__Docbook_FuncdefType

    @Docbook_FuncdefType.setter
    def Docbook_FuncdefType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FuncdefType__Docbook_FuncdefType", None)
        self.__Docbook_FuncdefType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FunctionType"):
                opp_val = getattr(old_value, "Docbook_FunctionType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_FunctionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FunctionType"):
                opp_val = getattr(value, "Docbook_FunctionType", None)
                setattr(value, "Docbook_FunctionType", self)

    @property
    def Docbook_FuncdefType155(self):
        return self.__Docbook_FuncdefType155

    @Docbook_FuncdefType155.setter
    def Docbook_FuncdefType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FuncdefType__Docbook_FuncdefType155", None)
        self.__Docbook_FuncdefType155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FuncprototypeType"):
                opp_val = getattr(old_value, "Docbook_FuncprototypeType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_FuncprototypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FuncprototypeType"):
                opp_val = getattr(value, "Docbook_FuncprototypeType", None)
                setattr(value, "Docbook_FuncprototypeType", self)

class Docbook_ParamdefType:

    def __init__(self, mixed: str, Docbook_ParamdefType: "Docbook_FuncprototypeType" = None, Docbook_ParamdefType235: "Docbook_ParameterType" = None):
        self.mixed = mixed
        self.Docbook_ParamdefType = Docbook_ParamdefType
        self.Docbook_ParamdefType235 = Docbook_ParamdefType235
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_ParamdefType(self):
        return self.__Docbook_ParamdefType

    @Docbook_ParamdefType.setter
    def Docbook_ParamdefType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParamdefType__Docbook_ParamdefType", None)
        self.__Docbook_ParamdefType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FuncprototypeType157"):
                opp_val = getattr(old_value, "Docbook_FuncprototypeType157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FuncprototypeType157"):
                opp_val = getattr(value, "Docbook_FuncprototypeType157", None)
                if opp_val is None:
                    setattr(value, "Docbook_FuncprototypeType157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParamdefType235(self):
        return self.__Docbook_ParamdefType235

    @Docbook_ParamdefType235.setter
    def Docbook_ParamdefType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParamdefType__Docbook_ParamdefType235", None)
        self.__Docbook_ParamdefType235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParameterType"):
                opp_val = getattr(old_value, "Docbook_ParameterType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ParameterType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParameterType"):
                opp_val = getattr(value, "Docbook_ParameterType", None)
                setattr(value, "Docbook_ParameterType", self)

class Docbook_FuncprototypeType:

    pass
class Docbook_FunctionType:

    def __init__(self, mixed: str, Docbook_FunctionType: "Docbook_FuncdefType" = None):
        self.mixed = mixed
        self.Docbook_FunctionType = Docbook_FunctionType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_FunctionType(self):
        return self.__Docbook_FunctionType

    @Docbook_FunctionType.setter
    def Docbook_FunctionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FunctionType__Docbook_FunctionType", None)
        self.__Docbook_FunctionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FuncdefType"):
                opp_val = getattr(old_value, "Docbook_FuncdefType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_FuncdefType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FuncdefType"):
                opp_val = getattr(value, "Docbook_FuncdefType", None)
                setattr(value, "Docbook_FuncdefType", self)

class Docbook_FileNameType:

    def __init__(self, mixed: str, Docbook_FileNameType: set["Docbook_ReplaceableType"] = None, Docbook_FileNameType406: "Docbook_TermType" = None):
        self.mixed = mixed
        self.Docbook_FileNameType = Docbook_FileNameType if Docbook_FileNameType is not None else set()
        self.Docbook_FileNameType406 = Docbook_FileNameType406
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_FileNameType(self):
        return self.__Docbook_FileNameType

    @Docbook_FileNameType.setter
    def Docbook_FileNameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FileNameType__Docbook_FileNameType", None)
        self.__Docbook_FileNameType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ReplaceableType149"):
                    opp_val = getattr(item, "Docbook_ReplaceableType149", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ReplaceableType149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ReplaceableType149"):
                    opp_val = getattr(item, "Docbook_ReplaceableType149", None)
                    
                    setattr(item, "Docbook_ReplaceableType149", self)
                    

    @property
    def Docbook_FileNameType406(self):
        return self.__Docbook_FileNameType406

    @Docbook_FileNameType406.setter
    def Docbook_FileNameType406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FileNameType__Docbook_FileNameType406", None)
        self.__Docbook_FileNameType406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TermType405"):
                opp_val = getattr(old_value, "Docbook_TermType405", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TermType405"):
                opp_val = getattr(value, "Docbook_TermType405", None)
                if opp_val is None:
                    setattr(value, "Docbook_TermType405", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_FirstnameType:

    def __init__(self, mixed: str, Docbook_FirstnameType: "Docbook_PersonnameType" = None):
        self.mixed = mixed
        self.Docbook_FirstnameType = Docbook_FirstnameType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_FirstnameType(self):
        return self.__Docbook_FirstnameType

    @Docbook_FirstnameType.setter
    def Docbook_FirstnameType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FirstnameType__Docbook_FirstnameType", None)
        self.__Docbook_FirstnameType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PersonnameType257"):
                opp_val = getattr(old_value, "Docbook_PersonnameType257", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PersonnameType257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PersonnameType257"):
                opp_val = getattr(value, "Docbook_PersonnameType257", None)
                setattr(value, "Docbook_PersonnameType257", self)

class Docbook_ExampleType:

    def __init__(self, id: str, Docbook_ExampleType: "Docbook_TitleType" = None, Docbook_ExampleType140: "Docbook_ProgramlistingType" = None, Docbook_ExampleType379: "Docbook_SectionType" = None):
        self.id = id
        self.Docbook_ExampleType = Docbook_ExampleType
        self.Docbook_ExampleType140 = Docbook_ExampleType140
        self.Docbook_ExampleType379 = Docbook_ExampleType379
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Docbook_ExampleType379(self):
        return self.__Docbook_ExampleType379

    @Docbook_ExampleType379.setter
    def Docbook_ExampleType379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ExampleType__Docbook_ExampleType379", None)
        self.__Docbook_ExampleType379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType378"):
                opp_val = getattr(old_value, "Docbook_SectionType378", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_SectionType378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType378"):
                opp_val = getattr(value, "Docbook_SectionType378", None)
                setattr(value, "Docbook_SectionType378", self)

    @property
    def Docbook_ExampleType140(self):
        return self.__Docbook_ExampleType140

    @Docbook_ExampleType140.setter
    def Docbook_ExampleType140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ExampleType__Docbook_ExampleType140", None)
        self.__Docbook_ExampleType140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ProgramlistingType141"):
                opp_val = getattr(old_value, "Docbook_ProgramlistingType141", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ProgramlistingType141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ProgramlistingType141"):
                opp_val = getattr(value, "Docbook_ProgramlistingType141", None)
                setattr(value, "Docbook_ProgramlistingType141", self)

    @property
    def Docbook_ExampleType(self):
        return self.__Docbook_ExampleType

    @Docbook_ExampleType.setter
    def Docbook_ExampleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ExampleType__Docbook_ExampleType", None)
        self.__Docbook_ExampleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType138"):
                opp_val = getattr(old_value, "Docbook_TitleType138", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType138"):
                opp_val = getattr(value, "Docbook_TitleType138", None)
                setattr(value, "Docbook_TitleType138", self)

class Docbook_EnvarType:

    def __init__(self, mixed: str, Docbook_EnvarType: set["Docbook_ReplaceableType"] = None, Docbook_EnvarType409: "Docbook_TermType" = None):
        self.mixed = mixed
        self.Docbook_EnvarType = Docbook_EnvarType if Docbook_EnvarType is not None else set()
        self.Docbook_EnvarType409 = Docbook_EnvarType409
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_EnvarType409(self):
        return self.__Docbook_EnvarType409

    @Docbook_EnvarType409.setter
    def Docbook_EnvarType409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EnvarType__Docbook_EnvarType409", None)
        self.__Docbook_EnvarType409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TermType408"):
                opp_val = getattr(old_value, "Docbook_TermType408", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TermType408"):
                opp_val = getattr(value, "Docbook_TermType408", None)
                if opp_val is None:
                    setattr(value, "Docbook_TermType408", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EnvarType(self):
        return self.__Docbook_EnvarType

    @Docbook_EnvarType.setter
    def Docbook_EnvarType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EnvarType__Docbook_EnvarType", None)
        self.__Docbook_EnvarType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ReplaceableType136"):
                    opp_val = getattr(item, "Docbook_ReplaceableType136", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ReplaceableType136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ReplaceableType136"):
                    opp_val = getattr(item, "Docbook_ReplaceableType136", None)
                    
                    setattr(item, "Docbook_ReplaceableType136", self)
                    

class Docbook_UlinkType:

    def __init__(self, type: str, url: str, mixed: str, Docbook_UlinkType: "Docbook_DocumentRoot" = None, Docbook_UlinkType168: "Docbook_ImportantType" = None, Docbook_UlinkType227: "Docbook_NoteType" = None, Docbook_UlinkType233: "Docbook_OtheraddrType" = None, Docbook_UlinkType244: "Docbook_ParaType" = None, Docbook_UlinkType334: "Docbook_RevnumberType" = None, Docbook_UlinkType427: "Docbook_TipType" = None, Docbook_UlinkType435: set["Docbook_EmphasisType"] = None):
        self.type = type
        self.url = url
        self.mixed = mixed
        self.Docbook_UlinkType = Docbook_UlinkType
        self.Docbook_UlinkType168 = Docbook_UlinkType168
        self.Docbook_UlinkType227 = Docbook_UlinkType227
        self.Docbook_UlinkType233 = Docbook_UlinkType233
        self.Docbook_UlinkType244 = Docbook_UlinkType244
        self.Docbook_UlinkType334 = Docbook_UlinkType334
        self.Docbook_UlinkType427 = Docbook_UlinkType427
        self.Docbook_UlinkType435 = Docbook_UlinkType435 if Docbook_UlinkType435 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_UlinkType244(self):
        return self.__Docbook_UlinkType244

    @Docbook_UlinkType244.setter
    def Docbook_UlinkType244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType244", None)
        self.__Docbook_UlinkType244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType243"):
                opp_val = getattr(old_value, "Docbook_ParaType243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType243"):
                opp_val = getattr(value, "Docbook_ParaType243", None)
                if opp_val is None:
                    setattr(value, "Docbook_ParaType243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_UlinkType435(self):
        return self.__Docbook_UlinkType435

    @Docbook_UlinkType435.setter
    def Docbook_UlinkType435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType435", None)
        self.__Docbook_UlinkType435 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType436"):
                    opp_val = getattr(item, "Docbook_EmphasisType436", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType436", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType436"):
                    opp_val = getattr(item, "Docbook_EmphasisType436", None)
                    
                    setattr(item, "Docbook_EmphasisType436", self)
                    

    @property
    def Docbook_UlinkType(self):
        return self.__Docbook_UlinkType

    @Docbook_UlinkType.setter
    def Docbook_UlinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType", None)
        self.__Docbook_UlinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot122"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot122"):
                opp_val = getattr(value, "Docbook_DocumentRoot122", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_UlinkType233(self):
        return self.__Docbook_UlinkType233

    @Docbook_UlinkType233.setter
    def Docbook_UlinkType233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType233", None)
        self.__Docbook_UlinkType233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_OtheraddrType232"):
                opp_val = getattr(old_value, "Docbook_OtheraddrType232", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_OtheraddrType232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_OtheraddrType232"):
                opp_val = getattr(value, "Docbook_OtheraddrType232", None)
                setattr(value, "Docbook_OtheraddrType232", self)

    @property
    def Docbook_UlinkType427(self):
        return self.__Docbook_UlinkType427

    @Docbook_UlinkType427.setter
    def Docbook_UlinkType427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType427", None)
        self.__Docbook_UlinkType427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TipType426"):
                opp_val = getattr(old_value, "Docbook_TipType426", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TipType426"):
                opp_val = getattr(value, "Docbook_TipType426", None)
                if opp_val is None:
                    setattr(value, "Docbook_TipType426", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_UlinkType334(self):
        return self.__Docbook_UlinkType334

    @Docbook_UlinkType334.setter
    def Docbook_UlinkType334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType334", None)
        self.__Docbook_UlinkType334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevnumberType333"):
                opp_val = getattr(old_value, "Docbook_RevnumberType333", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevnumberType333"):
                opp_val = getattr(value, "Docbook_RevnumberType333", None)
                if opp_val is None:
                    setattr(value, "Docbook_RevnumberType333", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_UlinkType227(self):
        return self.__Docbook_UlinkType227

    @Docbook_UlinkType227.setter
    def Docbook_UlinkType227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType227", None)
        self.__Docbook_UlinkType227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_NoteType226"):
                opp_val = getattr(old_value, "Docbook_NoteType226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_NoteType226"):
                opp_val = getattr(value, "Docbook_NoteType226", None)
                if opp_val is None:
                    setattr(value, "Docbook_NoteType226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_UlinkType168(self):
        return self.__Docbook_UlinkType168

    @Docbook_UlinkType168.setter
    def Docbook_UlinkType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_UlinkType__Docbook_UlinkType168", None)
        self.__Docbook_UlinkType168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ImportantType167"):
                opp_val = getattr(old_value, "Docbook_ImportantType167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ImportantType167"):
                opp_val = getattr(value, "Docbook_ImportantType167", None)
                if opp_val is None:
                    setattr(value, "Docbook_ImportantType167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_TheadType:

    pass
class Docbook_TgroupType:

    def __init__(self, colseq: str, rowseq: str, cols: str, align: str, Docbook_TgroupType: "Docbook_DocumentRoot" = None, Docbook_TgroupType171: "Docbook_InformaltableType" = None, Docbook_TgroupType398: "Docbook_TableType" = None, Docbook_TgroupType414: set["Docbook_ColspecType"] = None, Docbook_TgroupType417: "Docbook_TheadType" = None, Docbook_TgroupType420: "Docbook_TbodyType" = None):
        self.colseq = colseq
        self.rowseq = rowseq
        self.cols = cols
        self.align = align
        self.Docbook_TgroupType = Docbook_TgroupType
        self.Docbook_TgroupType171 = Docbook_TgroupType171
        self.Docbook_TgroupType398 = Docbook_TgroupType398
        self.Docbook_TgroupType414 = Docbook_TgroupType414 if Docbook_TgroupType414 is not None else set()
        self.Docbook_TgroupType417 = Docbook_TgroupType417
        self.Docbook_TgroupType420 = Docbook_TgroupType420
        
    @property
    def cols(self) -> str:
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols

    @property
    def rowseq(self) -> str:
        return self.__rowseq

    @rowseq.setter
    def rowseq(self, rowseq: str):
        self.__rowseq = rowseq

    @property
    def colseq(self) -> str:
        return self.__colseq

    @colseq.setter
    def colseq(self, colseq: str):
        self.__colseq = colseq

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def Docbook_TgroupType398(self):
        return self.__Docbook_TgroupType398

    @Docbook_TgroupType398.setter
    def Docbook_TgroupType398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType398", None)
        self.__Docbook_TgroupType398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TableType397"):
                opp_val = getattr(old_value, "Docbook_TableType397", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TableType397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TableType397"):
                opp_val = getattr(value, "Docbook_TableType397", None)
                setattr(value, "Docbook_TableType397", self)

    @property
    def Docbook_TgroupType417(self):
        return self.__Docbook_TgroupType417

    @Docbook_TgroupType417.setter
    def Docbook_TgroupType417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType417", None)
        self.__Docbook_TgroupType417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TheadType418"):
                opp_val = getattr(old_value, "Docbook_TheadType418", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TheadType418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TheadType418"):
                opp_val = getattr(value, "Docbook_TheadType418", None)
                setattr(value, "Docbook_TheadType418", self)

    @property
    def Docbook_TgroupType171(self):
        return self.__Docbook_TgroupType171

    @Docbook_TgroupType171.setter
    def Docbook_TgroupType171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType171", None)
        self.__Docbook_TgroupType171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InformaltableType170"):
                opp_val = getattr(old_value, "Docbook_InformaltableType170", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InformaltableType170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InformaltableType170"):
                opp_val = getattr(value, "Docbook_InformaltableType170", None)
                setattr(value, "Docbook_InformaltableType170", self)

    @property
    def Docbook_TgroupType420(self):
        return self.__Docbook_TgroupType420

    @Docbook_TgroupType420.setter
    def Docbook_TgroupType420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType420", None)
        self.__Docbook_TgroupType420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TbodyType421"):
                opp_val = getattr(old_value, "Docbook_TbodyType421", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TbodyType421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TbodyType421"):
                opp_val = getattr(value, "Docbook_TbodyType421", None)
                setattr(value, "Docbook_TbodyType421", self)

    @property
    def Docbook_TgroupType(self):
        return self.__Docbook_TgroupType

    @Docbook_TgroupType.setter
    def Docbook_TgroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType", None)
        self.__Docbook_TgroupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot113"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot113"):
                opp_val = getattr(value, "Docbook_DocumentRoot113", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TgroupType414(self):
        return self.__Docbook_TgroupType414

    @Docbook_TgroupType414.setter
    def Docbook_TgroupType414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TgroupType__Docbook_TgroupType414", None)
        self.__Docbook_TgroupType414 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ColspecType415"):
                    opp_val = getattr(item, "Docbook_ColspecType415", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ColspecType415", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ColspecType415"):
                    opp_val = getattr(item, "Docbook_ColspecType415", None)
                    
                    setattr(item, "Docbook_ColspecType415", self)
                    

class Docbook_TipType:

    def __init__(self, mixed: str, Docbook_TipType: "Docbook_DocumentRoot" = None, Docbook_TipType271: "Docbook_PrefaceType" = None, Docbook_TipType373: "Docbook_SectionType" = None, Docbook_TipType426: set["Docbook_UlinkType"] = None):
        self.mixed = mixed
        self.Docbook_TipType = Docbook_TipType
        self.Docbook_TipType271 = Docbook_TipType271
        self.Docbook_TipType373 = Docbook_TipType373
        self.Docbook_TipType426 = Docbook_TipType426 if Docbook_TipType426 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_TipType(self):
        return self.__Docbook_TipType

    @Docbook_TipType.setter
    def Docbook_TipType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TipType__Docbook_TipType", None)
        self.__Docbook_TipType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot117"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot117"):
                opp_val = getattr(value, "Docbook_DocumentRoot117", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TipType271(self):
        return self.__Docbook_TipType271

    @Docbook_TipType271.setter
    def Docbook_TipType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TipType__Docbook_TipType271", None)
        self.__Docbook_TipType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PrefaceType270"):
                opp_val = getattr(old_value, "Docbook_PrefaceType270", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PrefaceType270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PrefaceType270"):
                opp_val = getattr(value, "Docbook_PrefaceType270", None)
                setattr(value, "Docbook_PrefaceType270", self)

    @property
    def Docbook_TipType426(self):
        return self.__Docbook_TipType426

    @Docbook_TipType426.setter
    def Docbook_TipType426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TipType__Docbook_TipType426", None)
        self.__Docbook_TipType426 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType427"):
                    opp_val = getattr(item, "Docbook_UlinkType427", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType427"):
                    opp_val = getattr(item, "Docbook_UlinkType427", None)
                    
                    setattr(item, "Docbook_UlinkType427", self)
                    

    @property
    def Docbook_TipType373(self):
        return self.__Docbook_TipType373

    @Docbook_TipType373.setter
    def Docbook_TipType373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TipType__Docbook_TipType373", None)
        self.__Docbook_TipType373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType372"):
                opp_val = getattr(old_value, "Docbook_SectionType372", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_SectionType372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType372"):
                opp_val = getattr(value, "Docbook_SectionType372", None)
                setattr(value, "Docbook_SectionType372", self)

class Docbook_TbodyType:

    pass
class Docbook_TableType:

    def __init__(self, id: str, Docbook_TableType: "Docbook_DocumentRoot" = None, Docbook_TableType370: "Docbook_SectionType" = None, Docbook_TableType394: "Docbook_TitleType" = None, Docbook_TableType397: "Docbook_TgroupType" = None):
        self.id = id
        self.Docbook_TableType = Docbook_TableType
        self.Docbook_TableType370 = Docbook_TableType370
        self.Docbook_TableType394 = Docbook_TableType394
        self.Docbook_TableType397 = Docbook_TableType397
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Docbook_TableType394(self):
        return self.__Docbook_TableType394

    @Docbook_TableType394.setter
    def Docbook_TableType394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TableType__Docbook_TableType394", None)
        self.__Docbook_TableType394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType395"):
                opp_val = getattr(old_value, "Docbook_TitleType395", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType395"):
                opp_val = getattr(value, "Docbook_TitleType395", None)
                setattr(value, "Docbook_TitleType395", self)

    @property
    def Docbook_TableType370(self):
        return self.__Docbook_TableType370

    @Docbook_TableType370.setter
    def Docbook_TableType370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TableType__Docbook_TableType370", None)
        self.__Docbook_TableType370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType369"):
                opp_val = getattr(old_value, "Docbook_SectionType369", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType369"):
                opp_val = getattr(value, "Docbook_SectionType369", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType369", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TableType(self):
        return self.__Docbook_TableType

    @Docbook_TableType.setter
    def Docbook_TableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TableType__Docbook_TableType", None)
        self.__Docbook_TableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot109"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot109"):
                opp_val = getattr(value, "Docbook_DocumentRoot109", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TableType397(self):
        return self.__Docbook_TableType397

    @Docbook_TableType397.setter
    def Docbook_TableType397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TableType__Docbook_TableType397", None)
        self.__Docbook_TableType397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TgroupType398"):
                opp_val = getattr(old_value, "Docbook_TgroupType398", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TgroupType398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TgroupType398"):
                opp_val = getattr(value, "Docbook_TgroupType398", None)
                setattr(value, "Docbook_TgroupType398", self)

class Docbook_PublisherType:

    def __init__(self, publishername: str, Docbook_PublisherType: "Docbook_DocumentRoot" = None, Docbook_PublisherType188: "Docbook_InfoType" = None, Docbook_PublisherType279: "Docbook_AddressType" = None):
        self.publishername = publishername
        self.Docbook_PublisherType = Docbook_PublisherType
        self.Docbook_PublisherType188 = Docbook_PublisherType188
        self.Docbook_PublisherType279 = Docbook_PublisherType279
        
    @property
    def publishername(self) -> str:
        return self.__publishername

    @publishername.setter
    def publishername(self, publishername: str):
        self.__publishername = publishername

    @property
    def Docbook_PublisherType188(self):
        return self.__Docbook_PublisherType188

    @Docbook_PublisherType188.setter
    def Docbook_PublisherType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PublisherType__Docbook_PublisherType188", None)
        self.__Docbook_PublisherType188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType187"):
                opp_val = getattr(old_value, "Docbook_InfoType187", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType187"):
                opp_val = getattr(value, "Docbook_InfoType187", None)
                setattr(value, "Docbook_InfoType187", self)

    @property
    def Docbook_PublisherType279(self):
        return self.__Docbook_PublisherType279

    @Docbook_PublisherType279.setter
    def Docbook_PublisherType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PublisherType__Docbook_PublisherType279", None)
        self.__Docbook_PublisherType279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_AddressType280"):
                opp_val = getattr(old_value, "Docbook_AddressType280", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_AddressType280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_AddressType280"):
                opp_val = getattr(value, "Docbook_AddressType280", None)
                setattr(value, "Docbook_AddressType280", self)

    @property
    def Docbook_PublisherType(self):
        return self.__Docbook_PublisherType

    @Docbook_PublisherType.setter
    def Docbook_PublisherType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PublisherType__Docbook_PublisherType", None)
        self.__Docbook_PublisherType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot102"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot102"):
                opp_val = getattr(value, "Docbook_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_RowType:

    pass
class Docbook_PhraseType:

    def __init__(self, id: str, Docbook_PhraseType: "Docbook_DocumentRoot" = None, Docbook_PhraseType277: "Docbook_ProgramlistingType" = None, Docbook_PhraseType392: "Docbook_SubtitleType" = None, Docbook_PhraseType433: "Docbook_TitleType" = None):
        self.id = id
        self.Docbook_PhraseType = Docbook_PhraseType
        self.Docbook_PhraseType277 = Docbook_PhraseType277
        self.Docbook_PhraseType392 = Docbook_PhraseType392
        self.Docbook_PhraseType433 = Docbook_PhraseType433
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Docbook_PhraseType(self):
        return self.__Docbook_PhraseType

    @Docbook_PhraseType.setter
    def Docbook_PhraseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PhraseType__Docbook_PhraseType", None)
        self.__Docbook_PhraseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot95"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot95"):
                opp_val = getattr(value, "Docbook_DocumentRoot95", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_PhraseType277(self):
        return self.__Docbook_PhraseType277

    @Docbook_PhraseType277.setter
    def Docbook_PhraseType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PhraseType__Docbook_PhraseType277", None)
        self.__Docbook_PhraseType277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ProgramlistingType276"):
                opp_val = getattr(old_value, "Docbook_ProgramlistingType276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ProgramlistingType276"):
                opp_val = getattr(value, "Docbook_ProgramlistingType276", None)
                if opp_val is None:
                    setattr(value, "Docbook_ProgramlistingType276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_PhraseType433(self):
        return self.__Docbook_PhraseType433

    @Docbook_PhraseType433.setter
    def Docbook_PhraseType433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PhraseType__Docbook_PhraseType433", None)
        self.__Docbook_PhraseType433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType432"):
                opp_val = getattr(old_value, "Docbook_TitleType432", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType432"):
                opp_val = getattr(value, "Docbook_TitleType432", None)
                if opp_val is None:
                    setattr(value, "Docbook_TitleType432", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_PhraseType392(self):
        return self.__Docbook_PhraseType392

    @Docbook_PhraseType392.setter
    def Docbook_PhraseType392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_PhraseType__Docbook_PhraseType392", None)
        self.__Docbook_PhraseType392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SubtitleType391"):
                opp_val = getattr(old_value, "Docbook_SubtitleType391", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SubtitleType391"):
                opp_val = getattr(value, "Docbook_SubtitleType391", None)
                if opp_val is None:
                    setattr(value, "Docbook_SubtitleType391", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_ProgramlistingType:

    def __init__(self, mixed: str, group: str, format: str, language: str, linenumbering: str, superscript: str, Docbook_ProgramlistingType: "Docbook_DocumentRoot" = None, Docbook_ProgramlistingType128: "Docbook_EntryType" = None, Docbook_ProgramlistingType141: "Docbook_ExampleType" = None, Docbook_ProgramlistingType273: set["Docbook_EmphasisType"] = None, Docbook_ProgramlistingType276: set["Docbook_PhraseType"] = None, Docbook_ProgramlistingType352: "Docbook_SectionType" = None):
        self.mixed = mixed
        self.group = group
        self.format = format
        self.language = language
        self.linenumbering = linenumbering
        self.superscript = superscript
        self.Docbook_ProgramlistingType = Docbook_ProgramlistingType
        self.Docbook_ProgramlistingType128 = Docbook_ProgramlistingType128
        self.Docbook_ProgramlistingType141 = Docbook_ProgramlistingType141
        self.Docbook_ProgramlistingType273 = Docbook_ProgramlistingType273 if Docbook_ProgramlistingType273 is not None else set()
        self.Docbook_ProgramlistingType276 = Docbook_ProgramlistingType276 if Docbook_ProgramlistingType276 is not None else set()
        self.Docbook_ProgramlistingType352 = Docbook_ProgramlistingType352
        
    @property
    def linenumbering(self) -> str:
        return self.__linenumbering

    @linenumbering.setter
    def linenumbering(self, linenumbering: str):
        self.__linenumbering = linenumbering

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def superscript(self) -> str:
        return self.__superscript

    @superscript.setter
    def superscript(self, superscript: str):
        self.__superscript = superscript

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def Docbook_ProgramlistingType(self):
        return self.__Docbook_ProgramlistingType

    @Docbook_ProgramlistingType.setter
    def Docbook_ProgramlistingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType", None)
        self.__Docbook_ProgramlistingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot100"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot100"):
                opp_val = getattr(value, "Docbook_DocumentRoot100", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ProgramlistingType141(self):
        return self.__Docbook_ProgramlistingType141

    @Docbook_ProgramlistingType141.setter
    def Docbook_ProgramlistingType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType141", None)
        self.__Docbook_ProgramlistingType141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ExampleType140"):
                opp_val = getattr(old_value, "Docbook_ExampleType140", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ExampleType140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ExampleType140"):
                opp_val = getattr(value, "Docbook_ExampleType140", None)
                setattr(value, "Docbook_ExampleType140", self)

    @property
    def Docbook_ProgramlistingType276(self):
        return self.__Docbook_ProgramlistingType276

    @Docbook_ProgramlistingType276.setter
    def Docbook_ProgramlistingType276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType276", None)
        self.__Docbook_ProgramlistingType276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PhraseType277"):
                    opp_val = getattr(item, "Docbook_PhraseType277", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PhraseType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PhraseType277"):
                    opp_val = getattr(item, "Docbook_PhraseType277", None)
                    
                    setattr(item, "Docbook_PhraseType277", self)
                    

    @property
    def Docbook_ProgramlistingType273(self):
        return self.__Docbook_ProgramlistingType273

    @Docbook_ProgramlistingType273.setter
    def Docbook_ProgramlistingType273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType273", None)
        self.__Docbook_ProgramlistingType273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType274"):
                    opp_val = getattr(item, "Docbook_EmphasisType274", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType274"):
                    opp_val = getattr(item, "Docbook_EmphasisType274", None)
                    
                    setattr(item, "Docbook_EmphasisType274", self)
                    

    @property
    def Docbook_ProgramlistingType352(self):
        return self.__Docbook_ProgramlistingType352

    @Docbook_ProgramlistingType352.setter
    def Docbook_ProgramlistingType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType352", None)
        self.__Docbook_ProgramlistingType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType351"):
                opp_val = getattr(old_value, "Docbook_SectionType351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType351"):
                opp_val = getattr(value, "Docbook_SectionType351", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ProgramlistingType128(self):
        return self.__Docbook_ProgramlistingType128

    @Docbook_ProgramlistingType128.setter
    def Docbook_ProgramlistingType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ProgramlistingType__Docbook_ProgramlistingType128", None)
        self.__Docbook_ProgramlistingType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_EntryType127"):
                opp_val = getattr(old_value, "Docbook_EntryType127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_EntryType127"):
                opp_val = getattr(value, "Docbook_EntryType127", None)
                if opp_val is None:
                    setattr(value, "Docbook_EntryType127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_OrderedlistType(ItemizedlistType):

    def __init__(self, inheritnum: str, continuation: str, Docbook_OrderedlistType: "Docbook_DocumentRoot" = None, Docbook_OrderedlistType212: "Docbook_LegalNoticeType" = None, Docbook_OrderedlistType367: "Docbook_SectionType" = None):
        self.inheritnum = inheritnum
        self.continuation = continuation
        self.Docbook_OrderedlistType = Docbook_OrderedlistType
        self.Docbook_OrderedlistType212 = Docbook_OrderedlistType212
        self.Docbook_OrderedlistType367 = Docbook_OrderedlistType367
        
    @property
    def continuation(self) -> str:
        return self.__continuation

    @continuation.setter
    def continuation(self, continuation: str):
        self.__continuation = continuation

    @property
    def inheritnum(self) -> str:
        return self.__inheritnum

    @inheritnum.setter
    def inheritnum(self, inheritnum: str):
        self.__inheritnum = inheritnum

    @property
    def Docbook_OrderedlistType367(self):
        return self.__Docbook_OrderedlistType367

    @Docbook_OrderedlistType367.setter
    def Docbook_OrderedlistType367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OrderedlistType__Docbook_OrderedlistType367", None)
        self.__Docbook_OrderedlistType367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType366"):
                opp_val = getattr(old_value, "Docbook_SectionType366", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType366"):
                opp_val = getattr(value, "Docbook_SectionType366", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType366", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_OrderedlistType212(self):
        return self.__Docbook_OrderedlistType212

    @Docbook_OrderedlistType212.setter
    def Docbook_OrderedlistType212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OrderedlistType__Docbook_OrderedlistType212", None)
        self.__Docbook_OrderedlistType212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_LegalNoticeType211"):
                opp_val = getattr(old_value, "Docbook_LegalNoticeType211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_LegalNoticeType211"):
                opp_val = getattr(value, "Docbook_LegalNoticeType211", None)
                if opp_val is None:
                    setattr(value, "Docbook_LegalNoticeType211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_OrderedlistType(self):
        return self.__Docbook_OrderedlistType

    @Docbook_OrderedlistType.setter
    def Docbook_OrderedlistType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OrderedlistType__Docbook_OrderedlistType", None)
        self.__Docbook_OrderedlistType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot87"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot87"):
                opp_val = getattr(value, "Docbook_DocumentRoot87", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_LinkType:

    def __init__(self, mixed: str, value: str, linkend: str, Docbook_LinkType: "Docbook_DocumentRoot" = None, Docbook_LinkType250: "Docbook_ParaType" = None):
        self.mixed = mixed
        self.value = value
        self.linkend = linkend
        self.Docbook_LinkType = Docbook_LinkType
        self.Docbook_LinkType250 = Docbook_LinkType250
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def linkend(self) -> str:
        return self.__linkend

    @linkend.setter
    def linkend(self, linkend: str):
        self.__linkend = linkend

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Docbook_LinkType(self):
        return self.__Docbook_LinkType

    @Docbook_LinkType.setter
    def Docbook_LinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LinkType__Docbook_LinkType", None)
        self.__Docbook_LinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot76"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot76"):
                opp_val = getattr(value, "Docbook_DocumentRoot76", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_LinkType250(self):
        return self.__Docbook_LinkType250

    @Docbook_LinkType250.setter
    def Docbook_LinkType250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LinkType__Docbook_LinkType250", None)
        self.__Docbook_LinkType250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType249"):
                opp_val = getattr(old_value, "Docbook_ParaType249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType249"):
                opp_val = getattr(value, "Docbook_ParaType249", None)
                if opp_val is None:
                    setattr(value, "Docbook_ParaType249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_MediaobjectType:

    pass
class Docbook_LiteralType:

    def __init__(self, value: str, moreinfo: str, Docbook_LiteralType: "Docbook_DocumentRoot" = None, Docbook_LiteralType224: "Docbook_NoteType" = None, Docbook_LiteralType241: "Docbook_ParaType" = None):
        self.value = value
        self.moreinfo = moreinfo
        self.Docbook_LiteralType = Docbook_LiteralType
        self.Docbook_LiteralType224 = Docbook_LiteralType224
        self.Docbook_LiteralType241 = Docbook_LiteralType241
        
    @property
    def moreinfo(self) -> str:
        return self.__moreinfo

    @moreinfo.setter
    def moreinfo(self, moreinfo: str):
        self.__moreinfo = moreinfo

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Docbook_LiteralType224(self):
        return self.__Docbook_LiteralType224

    @Docbook_LiteralType224.setter
    def Docbook_LiteralType224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LiteralType__Docbook_LiteralType224", None)
        self.__Docbook_LiteralType224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_NoteType223"):
                opp_val = getattr(old_value, "Docbook_NoteType223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_NoteType223"):
                opp_val = getattr(value, "Docbook_NoteType223", None)
                if opp_val is None:
                    setattr(value, "Docbook_NoteType223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_LiteralType(self):
        return self.__Docbook_LiteralType

    @Docbook_LiteralType.setter
    def Docbook_LiteralType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LiteralType__Docbook_LiteralType", None)
        self.__Docbook_LiteralType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot80"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot80"):
                opp_val = getattr(value, "Docbook_DocumentRoot80", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_LiteralType241(self):
        return self.__Docbook_LiteralType241

    @Docbook_LiteralType241.setter
    def Docbook_LiteralType241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_LiteralType__Docbook_LiteralType241", None)
        self.__Docbook_LiteralType241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType240"):
                opp_val = getattr(old_value, "Docbook_ParaType240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType240"):
                opp_val = getattr(value, "Docbook_ParaType240", None)
                if opp_val is None:
                    setattr(value, "Docbook_ParaType240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_ListitemType:

    pass
class Docbook_InformaltableType:

    pass
class Docbook_ImportantType:

    def __init__(self, mixed: str, group: str, Docbook_ImportantType: "Docbook_DocumentRoot" = None, Docbook_ImportantType164: set["Docbook_EmphasisType"] = None, Docbook_ImportantType167: set["Docbook_UlinkType"] = None, Docbook_ImportantType268: "Docbook_PrefaceType" = None):
        self.mixed = mixed
        self.group = group
        self.Docbook_ImportantType = Docbook_ImportantType
        self.Docbook_ImportantType164 = Docbook_ImportantType164 if Docbook_ImportantType164 is not None else set()
        self.Docbook_ImportantType167 = Docbook_ImportantType167 if Docbook_ImportantType167 is not None else set()
        self.Docbook_ImportantType268 = Docbook_ImportantType268
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_ImportantType(self):
        return self.__Docbook_ImportantType

    @Docbook_ImportantType.setter
    def Docbook_ImportantType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImportantType__Docbook_ImportantType", None)
        self.__Docbook_ImportantType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot68"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot68"):
                opp_val = getattr(value, "Docbook_DocumentRoot68", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ImportantType164(self):
        return self.__Docbook_ImportantType164

    @Docbook_ImportantType164.setter
    def Docbook_ImportantType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImportantType__Docbook_ImportantType164", None)
        self.__Docbook_ImportantType164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType165"):
                    opp_val = getattr(item, "Docbook_EmphasisType165", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType165"):
                    opp_val = getattr(item, "Docbook_EmphasisType165", None)
                    
                    setattr(item, "Docbook_EmphasisType165", self)
                    

    @property
    def Docbook_ImportantType268(self):
        return self.__Docbook_ImportantType268

    @Docbook_ImportantType268.setter
    def Docbook_ImportantType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImportantType__Docbook_ImportantType268", None)
        self.__Docbook_ImportantType268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PrefaceType267"):
                opp_val = getattr(old_value, "Docbook_PrefaceType267", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PrefaceType267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PrefaceType267"):
                opp_val = getattr(value, "Docbook_PrefaceType267", None)
                setattr(value, "Docbook_PrefaceType267", self)

    @property
    def Docbook_ImportantType167(self):
        return self.__Docbook_ImportantType167

    @Docbook_ImportantType167.setter
    def Docbook_ImportantType167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImportantType__Docbook_ImportantType167", None)
        self.__Docbook_ImportantType167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType168"):
                    opp_val = getattr(item, "Docbook_UlinkType168", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType168"):
                    opp_val = getattr(item, "Docbook_UlinkType168", None)
                    
                    setattr(item, "Docbook_UlinkType168", self)
                    

class Docbook_KeywordsetType:

    def __init__(self, keyword: str, Docbook_KeywordsetType: "Docbook_DocumentRoot" = None, Docbook_KeywordsetType182: "Docbook_InfoType" = None):
        self.keyword = keyword
        self.Docbook_KeywordsetType = Docbook_KeywordsetType
        self.Docbook_KeywordsetType182 = Docbook_KeywordsetType182
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def Docbook_KeywordsetType182(self):
        return self.__Docbook_KeywordsetType182

    @Docbook_KeywordsetType182.setter
    def Docbook_KeywordsetType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_KeywordsetType__Docbook_KeywordsetType182", None)
        self.__Docbook_KeywordsetType182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType181"):
                opp_val = getattr(old_value, "Docbook_InfoType181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType181"):
                opp_val = getattr(value, "Docbook_InfoType181", None)
                if opp_val is None:
                    setattr(value, "Docbook_InfoType181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_KeywordsetType(self):
        return self.__Docbook_KeywordsetType

    @Docbook_KeywordsetType.setter
    def Docbook_KeywordsetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_KeywordsetType__Docbook_KeywordsetType", None)
        self.__Docbook_KeywordsetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot74"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot74"):
                opp_val = getattr(value, "Docbook_DocumentRoot74", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_ItemizedlistType:

    pass
class Docbook_FigureType:

    def __init__(self, float: str, id: str, Docbook_FigureType: "Docbook_DocumentRoot" = None, Docbook_FigureType143: "Docbook_TitleType" = None, Docbook_FigureType146: "Docbook_MediaobjectType" = None, Docbook_FigureType361: "Docbook_SectionType" = None):
        self.float = float
        self.id = id
        self.Docbook_FigureType = Docbook_FigureType
        self.Docbook_FigureType143 = Docbook_FigureType143
        self.Docbook_FigureType146 = Docbook_FigureType146
        self.Docbook_FigureType361 = Docbook_FigureType361
        
    @property
    def float(self) -> str:
        return self.__float

    @float.setter
    def float(self, float: str):
        self.__float = float

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Docbook_FigureType143(self):
        return self.__Docbook_FigureType143

    @Docbook_FigureType143.setter
    def Docbook_FigureType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FigureType__Docbook_FigureType143", None)
        self.__Docbook_FigureType143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType144"):
                opp_val = getattr(old_value, "Docbook_TitleType144", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType144"):
                opp_val = getattr(value, "Docbook_TitleType144", None)
                setattr(value, "Docbook_TitleType144", self)

    @property
    def Docbook_FigureType361(self):
        return self.__Docbook_FigureType361

    @Docbook_FigureType361.setter
    def Docbook_FigureType361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FigureType__Docbook_FigureType361", None)
        self.__Docbook_FigureType361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType360"):
                opp_val = getattr(old_value, "Docbook_SectionType360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType360"):
                opp_val = getattr(value, "Docbook_SectionType360", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_FigureType146(self):
        return self.__Docbook_FigureType146

    @Docbook_FigureType146.setter
    def Docbook_FigureType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FigureType__Docbook_FigureType146", None)
        self.__Docbook_FigureType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_MediaobjectType147"):
                opp_val = getattr(old_value, "Docbook_MediaobjectType147", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_MediaobjectType147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_MediaobjectType147"):
                opp_val = getattr(value, "Docbook_MediaobjectType147", None)
                setattr(value, "Docbook_MediaobjectType147", self)

    @property
    def Docbook_FigureType(self):
        return self.__Docbook_FigureType

    @Docbook_FigureType.setter
    def Docbook_FigureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FigureType__Docbook_FigureType", None)
        self.__Docbook_FigureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot60"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot60"):
                opp_val = getattr(value, "Docbook_DocumentRoot60", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_ImageobjectType:

    pass
class Docbook_ImagedataType:

    def __init__(self, depth: str, fileref: str, width: str, align: str, scale: str, Docbook_ImagedataType: "Docbook_DocumentRoot" = None, Docbook_ImagedataType162: "Docbook_ImageobjectType" = None):
        self.depth = depth
        self.fileref = fileref
        self.width = width
        self.align = align
        self.scale = scale
        self.Docbook_ImagedataType = Docbook_ImagedataType
        self.Docbook_ImagedataType162 = Docbook_ImagedataType162
        
    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def fileref(self) -> str:
        return self.__fileref

    @fileref.setter
    def fileref(self, fileref: str):
        self.__fileref = fileref

    @property
    def Docbook_ImagedataType162(self):
        return self.__Docbook_ImagedataType162

    @Docbook_ImagedataType162.setter
    def Docbook_ImagedataType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImagedataType__Docbook_ImagedataType162", None)
        self.__Docbook_ImagedataType162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ImageobjectType161"):
                opp_val = getattr(old_value, "Docbook_ImageobjectType161", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ImageobjectType161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ImageobjectType161"):
                opp_val = getattr(value, "Docbook_ImageobjectType161", None)
                setattr(value, "Docbook_ImageobjectType161", self)

    @property
    def Docbook_ImagedataType(self):
        return self.__Docbook_ImagedataType

    @Docbook_ImagedataType.setter
    def Docbook_ImagedataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ImagedataType__Docbook_ImagedataType", None)
        self.__Docbook_ImagedataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot64"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot64"):
                opp_val = getattr(value, "Docbook_DocumentRoot64", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_FootnoteType:

    def __init__(self, id: str, Docbook_FootnoteType: "Docbook_DocumentRoot" = None, Docbook_FootnoteType151: "Docbook_ParaType" = None, Docbook_FootnoteType247: "Docbook_ParaType" = None):
        self.id = id
        self.Docbook_FootnoteType = Docbook_FootnoteType
        self.Docbook_FootnoteType151 = Docbook_FootnoteType151
        self.Docbook_FootnoteType247 = Docbook_FootnoteType247
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Docbook_FootnoteType151(self):
        return self.__Docbook_FootnoteType151

    @Docbook_FootnoteType151.setter
    def Docbook_FootnoteType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FootnoteType__Docbook_FootnoteType151", None)
        self.__Docbook_FootnoteType151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType152"):
                opp_val = getattr(old_value, "Docbook_ParaType152", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ParaType152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType152"):
                opp_val = getattr(value, "Docbook_ParaType152", None)
                setattr(value, "Docbook_ParaType152", self)

    @property
    def Docbook_FootnoteType247(self):
        return self.__Docbook_FootnoteType247

    @Docbook_FootnoteType247.setter
    def Docbook_FootnoteType247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FootnoteType__Docbook_FootnoteType247", None)
        self.__Docbook_FootnoteType247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType246"):
                opp_val = getattr(old_value, "Docbook_ParaType246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType246"):
                opp_val = getattr(value, "Docbook_ParaType246", None)
                if opp_val is None:
                    setattr(value, "Docbook_ParaType246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_FootnoteType(self):
        return self.__Docbook_FootnoteType

    @Docbook_FootnoteType.setter
    def Docbook_FootnoteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_FootnoteType__Docbook_FootnoteType", None)
        self.__Docbook_FootnoteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot62"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot62"):
                opp_val = getattr(value, "Docbook_DocumentRoot62", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_EntryType:

    def __init__(self, mixed: str, valign: str, align: str, morerows: str, nameend: str, namest: str, Docbook_EntryType: "Docbook_DocumentRoot" = None, Docbook_EntryType130: "Docbook_MediaobjectType" = None, Docbook_EntryType133: set["Docbook_ParaType"] = None, Docbook_EntryType127: set["Docbook_ProgramlistingType"] = None, Docbook_EntryType337: "Docbook_RowType" = None):
        self.mixed = mixed
        self.valign = valign
        self.align = align
        self.morerows = morerows
        self.nameend = nameend
        self.namest = namest
        self.Docbook_EntryType = Docbook_EntryType
        self.Docbook_EntryType130 = Docbook_EntryType130
        self.Docbook_EntryType133 = Docbook_EntryType133 if Docbook_EntryType133 is not None else set()
        self.Docbook_EntryType127 = Docbook_EntryType127 if Docbook_EntryType127 is not None else set()
        self.Docbook_EntryType337 = Docbook_EntryType337
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def nameend(self) -> str:
        return self.__nameend

    @nameend.setter
    def nameend(self, nameend: str):
        self.__nameend = nameend

    @property
    def namest(self) -> str:
        return self.__namest

    @namest.setter
    def namest(self, namest: str):
        self.__namest = namest

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def morerows(self) -> str:
        return self.__morerows

    @morerows.setter
    def morerows(self, morerows: str):
        self.__morerows = morerows

    @property
    def Docbook_EntryType(self):
        return self.__Docbook_EntryType

    @Docbook_EntryType.setter
    def Docbook_EntryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EntryType__Docbook_EntryType", None)
        self.__Docbook_EntryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot58"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot58"):
                opp_val = getattr(value, "Docbook_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EntryType127(self):
        return self.__Docbook_EntryType127

    @Docbook_EntryType127.setter
    def Docbook_EntryType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EntryType__Docbook_EntryType127", None)
        self.__Docbook_EntryType127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ProgramlistingType128"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType128", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ProgramlistingType128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ProgramlistingType128"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType128", None)
                    
                    setattr(item, "Docbook_ProgramlistingType128", self)
                    

    @property
    def Docbook_EntryType133(self):
        return self.__Docbook_EntryType133

    @Docbook_EntryType133.setter
    def Docbook_EntryType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EntryType__Docbook_EntryType133", None)
        self.__Docbook_EntryType133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType134"):
                    opp_val = getattr(item, "Docbook_ParaType134", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType134"):
                    opp_val = getattr(item, "Docbook_ParaType134", None)
                    
                    setattr(item, "Docbook_ParaType134", self)
                    

    @property
    def Docbook_EntryType337(self):
        return self.__Docbook_EntryType337

    @Docbook_EntryType337.setter
    def Docbook_EntryType337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EntryType__Docbook_EntryType337", None)
        self.__Docbook_EntryType337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RowType336"):
                opp_val = getattr(old_value, "Docbook_RowType336", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RowType336"):
                opp_val = getattr(value, "Docbook_RowType336", None)
                if opp_val is None:
                    setattr(value, "Docbook_RowType336", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EntryType130(self):
        return self.__Docbook_EntryType130

    @Docbook_EntryType130.setter
    def Docbook_EntryType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EntryType__Docbook_EntryType130", None)
        self.__Docbook_EntryType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_MediaobjectType131"):
                opp_val = getattr(old_value, "Docbook_MediaobjectType131", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_MediaobjectType131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_MediaobjectType131"):
                opp_val = getattr(value, "Docbook_MediaobjectType131", None)
                setattr(value, "Docbook_MediaobjectType131", self)

class Docbook_EmphasisType:

    def __init__(self, mixed: str, role: str, Docbook_EmphasisType: "Docbook_DocumentRoot" = None, Docbook_EmphasisType125: "Docbook_EmphasisType" = None, Docbook_EmphasisType123: set["Docbook_EmphasisType"] = None, Docbook_EmphasisType165: "Docbook_ImportantType" = None, Docbook_EmphasisType238: "Docbook_ParaType" = None, Docbook_EmphasisType274: "Docbook_ProgramlistingType" = None, Docbook_EmphasisType389: "Docbook_SubtitleType" = None, Docbook_EmphasisType400: "Docbook_TermType" = None, Docbook_EmphasisType430: "Docbook_TitleType" = None, Docbook_EmphasisType436: "Docbook_UlinkType" = None):
        self.mixed = mixed
        self.role = role
        self.Docbook_EmphasisType = Docbook_EmphasisType
        self.Docbook_EmphasisType125 = Docbook_EmphasisType125
        self.Docbook_EmphasisType123 = Docbook_EmphasisType123 if Docbook_EmphasisType123 is not None else set()
        self.Docbook_EmphasisType165 = Docbook_EmphasisType165
        self.Docbook_EmphasisType238 = Docbook_EmphasisType238
        self.Docbook_EmphasisType274 = Docbook_EmphasisType274
        self.Docbook_EmphasisType389 = Docbook_EmphasisType389
        self.Docbook_EmphasisType400 = Docbook_EmphasisType400
        self.Docbook_EmphasisType430 = Docbook_EmphasisType430
        self.Docbook_EmphasisType436 = Docbook_EmphasisType436
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_EmphasisType436(self):
        return self.__Docbook_EmphasisType436

    @Docbook_EmphasisType436.setter
    def Docbook_EmphasisType436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType436", None)
        self.__Docbook_EmphasisType436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_UlinkType435"):
                opp_val = getattr(old_value, "Docbook_UlinkType435", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_UlinkType435"):
                opp_val = getattr(value, "Docbook_UlinkType435", None)
                if opp_val is None:
                    setattr(value, "Docbook_UlinkType435", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType274(self):
        return self.__Docbook_EmphasisType274

    @Docbook_EmphasisType274.setter
    def Docbook_EmphasisType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType274", None)
        self.__Docbook_EmphasisType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ProgramlistingType273"):
                opp_val = getattr(old_value, "Docbook_ProgramlistingType273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ProgramlistingType273"):
                opp_val = getattr(value, "Docbook_ProgramlistingType273", None)
                if opp_val is None:
                    setattr(value, "Docbook_ProgramlistingType273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType430(self):
        return self.__Docbook_EmphasisType430

    @Docbook_EmphasisType430.setter
    def Docbook_EmphasisType430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType430", None)
        self.__Docbook_EmphasisType430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType429"):
                opp_val = getattr(old_value, "Docbook_TitleType429", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType429"):
                opp_val = getattr(value, "Docbook_TitleType429", None)
                if opp_val is None:
                    setattr(value, "Docbook_TitleType429", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType238(self):
        return self.__Docbook_EmphasisType238

    @Docbook_EmphasisType238.setter
    def Docbook_EmphasisType238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType238", None)
        self.__Docbook_EmphasisType238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ParaType237"):
                opp_val = getattr(old_value, "Docbook_ParaType237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ParaType237"):
                opp_val = getattr(value, "Docbook_ParaType237", None)
                if opp_val is None:
                    setattr(value, "Docbook_ParaType237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType165(self):
        return self.__Docbook_EmphasisType165

    @Docbook_EmphasisType165.setter
    def Docbook_EmphasisType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType165", None)
        self.__Docbook_EmphasisType165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ImportantType164"):
                opp_val = getattr(old_value, "Docbook_ImportantType164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ImportantType164"):
                opp_val = getattr(value, "Docbook_ImportantType164", None)
                if opp_val is None:
                    setattr(value, "Docbook_ImportantType164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType(self):
        return self.__Docbook_EmphasisType

    @Docbook_EmphasisType.setter
    def Docbook_EmphasisType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType", None)
        self.__Docbook_EmphasisType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot56"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot56"):
                opp_val = getattr(value, "Docbook_DocumentRoot56", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType125(self):
        return self.__Docbook_EmphasisType125

    @Docbook_EmphasisType125.setter
    def Docbook_EmphasisType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType125", None)
        self.__Docbook_EmphasisType125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_EmphasisType123"):
                opp_val = getattr(old_value, "Docbook_EmphasisType123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_EmphasisType123"):
                opp_val = getattr(value, "Docbook_EmphasisType123", None)
                if opp_val is None:
                    setattr(value, "Docbook_EmphasisType123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType389(self):
        return self.__Docbook_EmphasisType389

    @Docbook_EmphasisType389.setter
    def Docbook_EmphasisType389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType389", None)
        self.__Docbook_EmphasisType389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SubtitleType388"):
                opp_val = getattr(old_value, "Docbook_SubtitleType388", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SubtitleType388"):
                opp_val = getattr(value, "Docbook_SubtitleType388", None)
                if opp_val is None:
                    setattr(value, "Docbook_SubtitleType388", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_EmphasisType123(self):
        return self.__Docbook_EmphasisType123

    @Docbook_EmphasisType123.setter
    def Docbook_EmphasisType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType123", None)
        self.__Docbook_EmphasisType123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType125"):
                    opp_val = getattr(item, "Docbook_EmphasisType125", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType125"):
                    opp_val = getattr(item, "Docbook_EmphasisType125", None)
                    
                    setattr(item, "Docbook_EmphasisType125", self)
                    

    @property
    def Docbook_EmphasisType400(self):
        return self.__Docbook_EmphasisType400

    @Docbook_EmphasisType400.setter
    def Docbook_EmphasisType400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_EmphasisType__Docbook_EmphasisType400", None)
        self.__Docbook_EmphasisType400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TermType"):
                opp_val = getattr(old_value, "Docbook_TermType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TermType"):
                opp_val = getattr(value, "Docbook_TermType", None)
                if opp_val is None:
                    setattr(value, "Docbook_TermType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_DocumentRoot:

    def __init__(self, mixed: str, bibliomisc: str, confnum: str, caution: str, date: str, confsponsor: str, conftitle: str, firstname: str, keyword: str, pubdate: str, publishername: str, state: str, subtitle: str, superscript: str, warning: str, Docbook_DocumentRoot: set["Docbook_EStringToStringMapEntry"] = None, Docbook_DocumentRoot31: set["Docbook_EStringToStringMapEntry"] = None, Docbook_DocumentRoot43: set["Docbook_BookType"] = None, Docbook_DocumentRoot34: set["Docbook_AbstractType"] = None, Docbook_DocumentRoot37: set["Docbook_AddressType"] = None, Docbook_DocumentRoot40: set["Docbook_AuthorType"] = None, Docbook_DocumentRoot52: set["Docbook_ColspecType"] = None, Docbook_DocumentRoot54: set["Docbook_ConfgroupType"] = None, Docbook_DocumentRoot46: set["Docbook_InfoType"] = None, Docbook_DocumentRoot49: set["Docbook_ChapterType"] = None, Docbook_DocumentRoot56: set["Docbook_EmphasisType"] = None, Docbook_DocumentRoot58: set["Docbook_EntryType"] = None, Docbook_DocumentRoot62: set["Docbook_FootnoteType"] = None, Docbook_DocumentRoot64: set["Docbook_ImagedataType"] = None, Docbook_DocumentRoot66: set["Docbook_ImageobjectType"] = None, Docbook_DocumentRoot60: set["Docbook_FigureType"] = None, Docbook_DocumentRoot72: set["Docbook_ItemizedlistType"] = None, Docbook_DocumentRoot68: set["Docbook_ImportantType"] = None, Docbook_DocumentRoot70: set["Docbook_InformaltableType"] = None, Docbook_DocumentRoot78: set["Docbook_ListitemType"] = None, Docbook_DocumentRoot80: set["Docbook_LiteralType"] = None, Docbook_DocumentRoot82: set["Docbook_MediaobjectType"] = None, Docbook_DocumentRoot74: set["Docbook_KeywordsetType"] = None, Docbook_DocumentRoot76: set["Docbook_LinkType"] = None, Docbook_DocumentRoot87: set["Docbook_OrderedlistType"] = None, Docbook_DocumentRoot89: set["Docbook_OtheraddrType"] = None, Docbook_DocumentRoot84: set["Docbook_NoteType"] = None, Docbook_DocumentRoot97: set["Docbook_PrefaceType"] = None, Docbook_DocumentRoot100: set["Docbook_ProgramlistingType"] = None, Docbook_DocumentRoot92: set["Docbook_ParaType"] = None, Docbook_DocumentRoot95: set["Docbook_PhraseType"] = None, Docbook_DocumentRoot104: set["Docbook_RowType"] = None, Docbook_DocumentRoot106: set["Docbook_SectionType"] = None, Docbook_DocumentRoot102: set["Docbook_PublisherType"] = None, Docbook_DocumentRoot109: set["Docbook_TableType"] = None, Docbook_DocumentRoot111: set["Docbook_TbodyType"] = None, Docbook_DocumentRoot117: set["Docbook_TipType"] = None, Docbook_DocumentRoot119: set["Docbook_TitleType"] = None, Docbook_DocumentRoot113: set["Docbook_TgroupType"] = None, Docbook_DocumentRoot115: set["Docbook_TheadType"] = None, Docbook_DocumentRoot122: set["Docbook_UlinkType"] = None):
        self.mixed = mixed
        self.bibliomisc = bibliomisc
        self.confnum = confnum
        self.caution = caution
        self.date = date
        self.confsponsor = confsponsor
        self.conftitle = conftitle
        self.firstname = firstname
        self.keyword = keyword
        self.pubdate = pubdate
        self.publishername = publishername
        self.state = state
        self.subtitle = subtitle
        self.superscript = superscript
        self.warning = warning
        self.Docbook_DocumentRoot = Docbook_DocumentRoot if Docbook_DocumentRoot is not None else set()
        self.Docbook_DocumentRoot31 = Docbook_DocumentRoot31 if Docbook_DocumentRoot31 is not None else set()
        self.Docbook_DocumentRoot43 = Docbook_DocumentRoot43 if Docbook_DocumentRoot43 is not None else set()
        self.Docbook_DocumentRoot34 = Docbook_DocumentRoot34 if Docbook_DocumentRoot34 is not None else set()
        self.Docbook_DocumentRoot37 = Docbook_DocumentRoot37 if Docbook_DocumentRoot37 is not None else set()
        self.Docbook_DocumentRoot40 = Docbook_DocumentRoot40 if Docbook_DocumentRoot40 is not None else set()
        self.Docbook_DocumentRoot52 = Docbook_DocumentRoot52 if Docbook_DocumentRoot52 is not None else set()
        self.Docbook_DocumentRoot54 = Docbook_DocumentRoot54 if Docbook_DocumentRoot54 is not None else set()
        self.Docbook_DocumentRoot46 = Docbook_DocumentRoot46 if Docbook_DocumentRoot46 is not None else set()
        self.Docbook_DocumentRoot49 = Docbook_DocumentRoot49 if Docbook_DocumentRoot49 is not None else set()
        self.Docbook_DocumentRoot56 = Docbook_DocumentRoot56 if Docbook_DocumentRoot56 is not None else set()
        self.Docbook_DocumentRoot58 = Docbook_DocumentRoot58 if Docbook_DocumentRoot58 is not None else set()
        self.Docbook_DocumentRoot62 = Docbook_DocumentRoot62 if Docbook_DocumentRoot62 is not None else set()
        self.Docbook_DocumentRoot64 = Docbook_DocumentRoot64 if Docbook_DocumentRoot64 is not None else set()
        self.Docbook_DocumentRoot66 = Docbook_DocumentRoot66 if Docbook_DocumentRoot66 is not None else set()
        self.Docbook_DocumentRoot60 = Docbook_DocumentRoot60 if Docbook_DocumentRoot60 is not None else set()
        self.Docbook_DocumentRoot72 = Docbook_DocumentRoot72 if Docbook_DocumentRoot72 is not None else set()
        self.Docbook_DocumentRoot68 = Docbook_DocumentRoot68 if Docbook_DocumentRoot68 is not None else set()
        self.Docbook_DocumentRoot70 = Docbook_DocumentRoot70 if Docbook_DocumentRoot70 is not None else set()
        self.Docbook_DocumentRoot78 = Docbook_DocumentRoot78 if Docbook_DocumentRoot78 is not None else set()
        self.Docbook_DocumentRoot80 = Docbook_DocumentRoot80 if Docbook_DocumentRoot80 is not None else set()
        self.Docbook_DocumentRoot82 = Docbook_DocumentRoot82 if Docbook_DocumentRoot82 is not None else set()
        self.Docbook_DocumentRoot74 = Docbook_DocumentRoot74 if Docbook_DocumentRoot74 is not None else set()
        self.Docbook_DocumentRoot76 = Docbook_DocumentRoot76 if Docbook_DocumentRoot76 is not None else set()
        self.Docbook_DocumentRoot87 = Docbook_DocumentRoot87 if Docbook_DocumentRoot87 is not None else set()
        self.Docbook_DocumentRoot89 = Docbook_DocumentRoot89 if Docbook_DocumentRoot89 is not None else set()
        self.Docbook_DocumentRoot84 = Docbook_DocumentRoot84 if Docbook_DocumentRoot84 is not None else set()
        self.Docbook_DocumentRoot97 = Docbook_DocumentRoot97 if Docbook_DocumentRoot97 is not None else set()
        self.Docbook_DocumentRoot100 = Docbook_DocumentRoot100 if Docbook_DocumentRoot100 is not None else set()
        self.Docbook_DocumentRoot92 = Docbook_DocumentRoot92 if Docbook_DocumentRoot92 is not None else set()
        self.Docbook_DocumentRoot95 = Docbook_DocumentRoot95 if Docbook_DocumentRoot95 is not None else set()
        self.Docbook_DocumentRoot104 = Docbook_DocumentRoot104 if Docbook_DocumentRoot104 is not None else set()
        self.Docbook_DocumentRoot106 = Docbook_DocumentRoot106 if Docbook_DocumentRoot106 is not None else set()
        self.Docbook_DocumentRoot102 = Docbook_DocumentRoot102 if Docbook_DocumentRoot102 is not None else set()
        self.Docbook_DocumentRoot109 = Docbook_DocumentRoot109 if Docbook_DocumentRoot109 is not None else set()
        self.Docbook_DocumentRoot111 = Docbook_DocumentRoot111 if Docbook_DocumentRoot111 is not None else set()
        self.Docbook_DocumentRoot117 = Docbook_DocumentRoot117 if Docbook_DocumentRoot117 is not None else set()
        self.Docbook_DocumentRoot119 = Docbook_DocumentRoot119 if Docbook_DocumentRoot119 is not None else set()
        self.Docbook_DocumentRoot113 = Docbook_DocumentRoot113 if Docbook_DocumentRoot113 is not None else set()
        self.Docbook_DocumentRoot115 = Docbook_DocumentRoot115 if Docbook_DocumentRoot115 is not None else set()
        self.Docbook_DocumentRoot122 = Docbook_DocumentRoot122 if Docbook_DocumentRoot122 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def publishername(self) -> str:
        return self.__publishername

    @publishername.setter
    def publishername(self, publishername: str):
        self.__publishername = publishername

    @property
    def caution(self) -> str:
        return self.__caution

    @caution.setter
    def caution(self, caution: str):
        self.__caution = caution

    @property
    def subtitle(self) -> str:
        return self.__subtitle

    @subtitle.setter
    def subtitle(self, subtitle: str):
        self.__subtitle = subtitle

    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def superscript(self) -> str:
        return self.__superscript

    @superscript.setter
    def superscript(self, superscript: str):
        self.__superscript = superscript

    @property
    def confsponsor(self) -> str:
        return self.__confsponsor

    @confsponsor.setter
    def confsponsor(self, confsponsor: str):
        self.__confsponsor = confsponsor

    @property
    def pubdate(self) -> str:
        return self.__pubdate

    @pubdate.setter
    def pubdate(self, pubdate: str):
        self.__pubdate = pubdate

    @property
    def confnum(self) -> str:
        return self.__confnum

    @confnum.setter
    def confnum(self, confnum: str):
        self.__confnum = confnum

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def warning(self) -> str:
        return self.__warning

    @warning.setter
    def warning(self, warning: str):
        self.__warning = warning

    @property
    def bibliomisc(self) -> str:
        return self.__bibliomisc

    @bibliomisc.setter
    def bibliomisc(self, bibliomisc: str):
        self.__bibliomisc = bibliomisc

    @property
    def conftitle(self) -> str:
        return self.__conftitle

    @conftitle.setter
    def conftitle(self, conftitle: str):
        self.__conftitle = conftitle

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def Docbook_DocumentRoot49(self):
        return self.__Docbook_DocumentRoot49

    @Docbook_DocumentRoot49.setter
    def Docbook_DocumentRoot49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot49", None)
        self.__Docbook_DocumentRoot49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ChapterType50"):
                    opp_val = getattr(item, "Docbook_ChapterType50", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ChapterType50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ChapterType50"):
                    opp_val = getattr(item, "Docbook_ChapterType50", None)
                    
                    setattr(item, "Docbook_ChapterType50", self)
                    

    @property
    def Docbook_DocumentRoot87(self):
        return self.__Docbook_DocumentRoot87

    @Docbook_DocumentRoot87.setter
    def Docbook_DocumentRoot87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot87", None)
        self.__Docbook_DocumentRoot87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OrderedlistType"):
                    opp_val = getattr(item, "Docbook_OrderedlistType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OrderedlistType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OrderedlistType"):
                    opp_val = getattr(item, "Docbook_OrderedlistType", None)
                    
                    setattr(item, "Docbook_OrderedlistType", self)
                    

    @property
    def Docbook_DocumentRoot102(self):
        return self.__Docbook_DocumentRoot102

    @Docbook_DocumentRoot102.setter
    def Docbook_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot102", None)
        self.__Docbook_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PublisherType"):
                    opp_val = getattr(item, "Docbook_PublisherType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PublisherType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PublisherType"):
                    opp_val = getattr(item, "Docbook_PublisherType", None)
                    
                    setattr(item, "Docbook_PublisherType", self)
                    

    @property
    def Docbook_DocumentRoot117(self):
        return self.__Docbook_DocumentRoot117

    @Docbook_DocumentRoot117.setter
    def Docbook_DocumentRoot117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot117", None)
        self.__Docbook_DocumentRoot117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TipType"):
                    opp_val = getattr(item, "Docbook_TipType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TipType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TipType"):
                    opp_val = getattr(item, "Docbook_TipType", None)
                    
                    setattr(item, "Docbook_TipType", self)
                    

    @property
    def Docbook_DocumentRoot97(self):
        return self.__Docbook_DocumentRoot97

    @Docbook_DocumentRoot97.setter
    def Docbook_DocumentRoot97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot97", None)
        self.__Docbook_DocumentRoot97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PrefaceType98"):
                    opp_val = getattr(item, "Docbook_PrefaceType98", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PrefaceType98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PrefaceType98"):
                    opp_val = getattr(item, "Docbook_PrefaceType98", None)
                    
                    setattr(item, "Docbook_PrefaceType98", self)
                    

    @property
    def Docbook_DocumentRoot56(self):
        return self.__Docbook_DocumentRoot56

    @Docbook_DocumentRoot56.setter
    def Docbook_DocumentRoot56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot56", None)
        self.__Docbook_DocumentRoot56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType"):
                    opp_val = getattr(item, "Docbook_EmphasisType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType"):
                    opp_val = getattr(item, "Docbook_EmphasisType", None)
                    
                    setattr(item, "Docbook_EmphasisType", self)
                    

    @property
    def Docbook_DocumentRoot119(self):
        return self.__Docbook_DocumentRoot119

    @Docbook_DocumentRoot119.setter
    def Docbook_DocumentRoot119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot119", None)
        self.__Docbook_DocumentRoot119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TitleType120"):
                    opp_val = getattr(item, "Docbook_TitleType120", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TitleType120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TitleType120"):
                    opp_val = getattr(item, "Docbook_TitleType120", None)
                    
                    setattr(item, "Docbook_TitleType120", self)
                    

    @property
    def Docbook_DocumentRoot106(self):
        return self.__Docbook_DocumentRoot106

    @Docbook_DocumentRoot106.setter
    def Docbook_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot106", None)
        self.__Docbook_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_SectionType107"):
                    opp_val = getattr(item, "Docbook_SectionType107", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_SectionType107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_SectionType107"):
                    opp_val = getattr(item, "Docbook_SectionType107", None)
                    
                    setattr(item, "Docbook_SectionType107", self)
                    

    @property
    def Docbook_DocumentRoot(self):
        return self.__Docbook_DocumentRoot

    @Docbook_DocumentRoot.setter
    def Docbook_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot", None)
        self.__Docbook_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Docbook_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Docbook_EStringToStringMapEntry", None)
                    
                    setattr(item, "Docbook_EStringToStringMapEntry", self)
                    

    @property
    def Docbook_DocumentRoot40(self):
        return self.__Docbook_DocumentRoot40

    @Docbook_DocumentRoot40.setter
    def Docbook_DocumentRoot40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot40", None)
        self.__Docbook_DocumentRoot40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_AuthorType41"):
                    opp_val = getattr(item, "Docbook_AuthorType41", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_AuthorType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_AuthorType41"):
                    opp_val = getattr(item, "Docbook_AuthorType41", None)
                    
                    setattr(item, "Docbook_AuthorType41", self)
                    

    @property
    def Docbook_DocumentRoot115(self):
        return self.__Docbook_DocumentRoot115

    @Docbook_DocumentRoot115.setter
    def Docbook_DocumentRoot115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot115", None)
        self.__Docbook_DocumentRoot115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TheadType"):
                    opp_val = getattr(item, "Docbook_TheadType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TheadType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TheadType"):
                    opp_val = getattr(item, "Docbook_TheadType", None)
                    
                    setattr(item, "Docbook_TheadType", self)
                    

    @property
    def Docbook_DocumentRoot60(self):
        return self.__Docbook_DocumentRoot60

    @Docbook_DocumentRoot60.setter
    def Docbook_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot60", None)
        self.__Docbook_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FigureType"):
                    opp_val = getattr(item, "Docbook_FigureType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FigureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FigureType"):
                    opp_val = getattr(item, "Docbook_FigureType", None)
                    
                    setattr(item, "Docbook_FigureType", self)
                    

    @property
    def Docbook_DocumentRoot109(self):
        return self.__Docbook_DocumentRoot109

    @Docbook_DocumentRoot109.setter
    def Docbook_DocumentRoot109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot109", None)
        self.__Docbook_DocumentRoot109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TableType"):
                    opp_val = getattr(item, "Docbook_TableType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TableType"):
                    opp_val = getattr(item, "Docbook_TableType", None)
                    
                    setattr(item, "Docbook_TableType", self)
                    

    @property
    def Docbook_DocumentRoot82(self):
        return self.__Docbook_DocumentRoot82

    @Docbook_DocumentRoot82.setter
    def Docbook_DocumentRoot82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot82", None)
        self.__Docbook_DocumentRoot82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_MediaobjectType"):
                    opp_val = getattr(item, "Docbook_MediaobjectType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_MediaobjectType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_MediaobjectType"):
                    opp_val = getattr(item, "Docbook_MediaobjectType", None)
                    
                    setattr(item, "Docbook_MediaobjectType", self)
                    

    @property
    def Docbook_DocumentRoot78(self):
        return self.__Docbook_DocumentRoot78

    @Docbook_DocumentRoot78.setter
    def Docbook_DocumentRoot78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot78", None)
        self.__Docbook_DocumentRoot78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ListitemType"):
                    opp_val = getattr(item, "Docbook_ListitemType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ListitemType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ListitemType"):
                    opp_val = getattr(item, "Docbook_ListitemType", None)
                    
                    setattr(item, "Docbook_ListitemType", self)
                    

    @property
    def Docbook_DocumentRoot68(self):
        return self.__Docbook_DocumentRoot68

    @Docbook_DocumentRoot68.setter
    def Docbook_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot68", None)
        self.__Docbook_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ImportantType"):
                    opp_val = getattr(item, "Docbook_ImportantType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ImportantType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ImportantType"):
                    opp_val = getattr(item, "Docbook_ImportantType", None)
                    
                    setattr(item, "Docbook_ImportantType", self)
                    

    @property
    def Docbook_DocumentRoot74(self):
        return self.__Docbook_DocumentRoot74

    @Docbook_DocumentRoot74.setter
    def Docbook_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot74", None)
        self.__Docbook_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_KeywordsetType"):
                    opp_val = getattr(item, "Docbook_KeywordsetType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_KeywordsetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_KeywordsetType"):
                    opp_val = getattr(item, "Docbook_KeywordsetType", None)
                    
                    setattr(item, "Docbook_KeywordsetType", self)
                    

    @property
    def Docbook_DocumentRoot84(self):
        return self.__Docbook_DocumentRoot84

    @Docbook_DocumentRoot84.setter
    def Docbook_DocumentRoot84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot84", None)
        self.__Docbook_DocumentRoot84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_NoteType85"):
                    opp_val = getattr(item, "Docbook_NoteType85", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_NoteType85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_NoteType85"):
                    opp_val = getattr(item, "Docbook_NoteType85", None)
                    
                    setattr(item, "Docbook_NoteType85", self)
                    

    @property
    def Docbook_DocumentRoot31(self):
        return self.__Docbook_DocumentRoot31

    @Docbook_DocumentRoot31.setter
    def Docbook_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot31", None)
        self.__Docbook_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EStringToStringMapEntry32"):
                    opp_val = getattr(item, "Docbook_EStringToStringMapEntry32", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EStringToStringMapEntry32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EStringToStringMapEntry32"):
                    opp_val = getattr(item, "Docbook_EStringToStringMapEntry32", None)
                    
                    setattr(item, "Docbook_EStringToStringMapEntry32", self)
                    

    @property
    def Docbook_DocumentRoot70(self):
        return self.__Docbook_DocumentRoot70

    @Docbook_DocumentRoot70.setter
    def Docbook_DocumentRoot70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot70", None)
        self.__Docbook_DocumentRoot70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_InformaltableType"):
                    opp_val = getattr(item, "Docbook_InformaltableType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_InformaltableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_InformaltableType"):
                    opp_val = getattr(item, "Docbook_InformaltableType", None)
                    
                    setattr(item, "Docbook_InformaltableType", self)
                    

    @property
    def Docbook_DocumentRoot80(self):
        return self.__Docbook_DocumentRoot80

    @Docbook_DocumentRoot80.setter
    def Docbook_DocumentRoot80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot80", None)
        self.__Docbook_DocumentRoot80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_LiteralType"):
                    opp_val = getattr(item, "Docbook_LiteralType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_LiteralType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_LiteralType"):
                    opp_val = getattr(item, "Docbook_LiteralType", None)
                    
                    setattr(item, "Docbook_LiteralType", self)
                    

    @property
    def Docbook_DocumentRoot92(self):
        return self.__Docbook_DocumentRoot92

    @Docbook_DocumentRoot92.setter
    def Docbook_DocumentRoot92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot92", None)
        self.__Docbook_DocumentRoot92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType93"):
                    opp_val = getattr(item, "Docbook_ParaType93", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType93"):
                    opp_val = getattr(item, "Docbook_ParaType93", None)
                    
                    setattr(item, "Docbook_ParaType93", self)
                    

    @property
    def Docbook_DocumentRoot113(self):
        return self.__Docbook_DocumentRoot113

    @Docbook_DocumentRoot113.setter
    def Docbook_DocumentRoot113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot113", None)
        self.__Docbook_DocumentRoot113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TgroupType"):
                    opp_val = getattr(item, "Docbook_TgroupType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TgroupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TgroupType"):
                    opp_val = getattr(item, "Docbook_TgroupType", None)
                    
                    setattr(item, "Docbook_TgroupType", self)
                    

    @property
    def Docbook_DocumentRoot72(self):
        return self.__Docbook_DocumentRoot72

    @Docbook_DocumentRoot72.setter
    def Docbook_DocumentRoot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot72", None)
        self.__Docbook_DocumentRoot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ItemizedlistType"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ItemizedlistType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ItemizedlistType"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType", None)
                    
                    setattr(item, "Docbook_ItemizedlistType", self)
                    

    @property
    def Docbook_DocumentRoot64(self):
        return self.__Docbook_DocumentRoot64

    @Docbook_DocumentRoot64.setter
    def Docbook_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot64", None)
        self.__Docbook_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ImagedataType"):
                    opp_val = getattr(item, "Docbook_ImagedataType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ImagedataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ImagedataType"):
                    opp_val = getattr(item, "Docbook_ImagedataType", None)
                    
                    setattr(item, "Docbook_ImagedataType", self)
                    

    @property
    def Docbook_DocumentRoot76(self):
        return self.__Docbook_DocumentRoot76

    @Docbook_DocumentRoot76.setter
    def Docbook_DocumentRoot76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot76", None)
        self.__Docbook_DocumentRoot76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_LinkType"):
                    opp_val = getattr(item, "Docbook_LinkType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_LinkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_LinkType"):
                    opp_val = getattr(item, "Docbook_LinkType", None)
                    
                    setattr(item, "Docbook_LinkType", self)
                    

    @property
    def Docbook_DocumentRoot54(self):
        return self.__Docbook_DocumentRoot54

    @Docbook_DocumentRoot54.setter
    def Docbook_DocumentRoot54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot54", None)
        self.__Docbook_DocumentRoot54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ConfgroupType"):
                    opp_val = getattr(item, "Docbook_ConfgroupType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ConfgroupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ConfgroupType"):
                    opp_val = getattr(item, "Docbook_ConfgroupType", None)
                    
                    setattr(item, "Docbook_ConfgroupType", self)
                    

    @property
    def Docbook_DocumentRoot52(self):
        return self.__Docbook_DocumentRoot52

    @Docbook_DocumentRoot52.setter
    def Docbook_DocumentRoot52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot52", None)
        self.__Docbook_DocumentRoot52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ColspecType"):
                    opp_val = getattr(item, "Docbook_ColspecType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ColspecType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ColspecType"):
                    opp_val = getattr(item, "Docbook_ColspecType", None)
                    
                    setattr(item, "Docbook_ColspecType", self)
                    

    @property
    def Docbook_DocumentRoot58(self):
        return self.__Docbook_DocumentRoot58

    @Docbook_DocumentRoot58.setter
    def Docbook_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot58", None)
        self.__Docbook_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EntryType"):
                    opp_val = getattr(item, "Docbook_EntryType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EntryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EntryType"):
                    opp_val = getattr(item, "Docbook_EntryType", None)
                    
                    setattr(item, "Docbook_EntryType", self)
                    

    @property
    def Docbook_DocumentRoot89(self):
        return self.__Docbook_DocumentRoot89

    @Docbook_DocumentRoot89.setter
    def Docbook_DocumentRoot89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot89", None)
        self.__Docbook_DocumentRoot89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OtheraddrType90"):
                    opp_val = getattr(item, "Docbook_OtheraddrType90", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OtheraddrType90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OtheraddrType90"):
                    opp_val = getattr(item, "Docbook_OtheraddrType90", None)
                    
                    setattr(item, "Docbook_OtheraddrType90", self)
                    

    @property
    def Docbook_DocumentRoot43(self):
        return self.__Docbook_DocumentRoot43

    @Docbook_DocumentRoot43.setter
    def Docbook_DocumentRoot43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot43", None)
        self.__Docbook_DocumentRoot43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_BookType44"):
                    opp_val = getattr(item, "Docbook_BookType44", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_BookType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_BookType44"):
                    opp_val = getattr(item, "Docbook_BookType44", None)
                    
                    setattr(item, "Docbook_BookType44", self)
                    

    @property
    def Docbook_DocumentRoot111(self):
        return self.__Docbook_DocumentRoot111

    @Docbook_DocumentRoot111.setter
    def Docbook_DocumentRoot111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot111", None)
        self.__Docbook_DocumentRoot111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TbodyType"):
                    opp_val = getattr(item, "Docbook_TbodyType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TbodyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TbodyType"):
                    opp_val = getattr(item, "Docbook_TbodyType", None)
                    
                    setattr(item, "Docbook_TbodyType", self)
                    

    @property
    def Docbook_DocumentRoot100(self):
        return self.__Docbook_DocumentRoot100

    @Docbook_DocumentRoot100.setter
    def Docbook_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot100", None)
        self.__Docbook_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ProgramlistingType"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ProgramlistingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ProgramlistingType"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType", None)
                    
                    setattr(item, "Docbook_ProgramlistingType", self)
                    

    @property
    def Docbook_DocumentRoot62(self):
        return self.__Docbook_DocumentRoot62

    @Docbook_DocumentRoot62.setter
    def Docbook_DocumentRoot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot62", None)
        self.__Docbook_DocumentRoot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FootnoteType"):
                    opp_val = getattr(item, "Docbook_FootnoteType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FootnoteType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FootnoteType"):
                    opp_val = getattr(item, "Docbook_FootnoteType", None)
                    
                    setattr(item, "Docbook_FootnoteType", self)
                    

    @property
    def Docbook_DocumentRoot95(self):
        return self.__Docbook_DocumentRoot95

    @Docbook_DocumentRoot95.setter
    def Docbook_DocumentRoot95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot95", None)
        self.__Docbook_DocumentRoot95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PhraseType"):
                    opp_val = getattr(item, "Docbook_PhraseType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PhraseType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PhraseType"):
                    opp_val = getattr(item, "Docbook_PhraseType", None)
                    
                    setattr(item, "Docbook_PhraseType", self)
                    

    @property
    def Docbook_DocumentRoot37(self):
        return self.__Docbook_DocumentRoot37

    @Docbook_DocumentRoot37.setter
    def Docbook_DocumentRoot37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot37", None)
        self.__Docbook_DocumentRoot37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_AddressType38"):
                    opp_val = getattr(item, "Docbook_AddressType38", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_AddressType38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_AddressType38"):
                    opp_val = getattr(item, "Docbook_AddressType38", None)
                    
                    setattr(item, "Docbook_AddressType38", self)
                    

    @property
    def Docbook_DocumentRoot46(self):
        return self.__Docbook_DocumentRoot46

    @Docbook_DocumentRoot46.setter
    def Docbook_DocumentRoot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot46", None)
        self.__Docbook_DocumentRoot46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_InfoType47"):
                    opp_val = getattr(item, "Docbook_InfoType47", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_InfoType47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_InfoType47"):
                    opp_val = getattr(item, "Docbook_InfoType47", None)
                    
                    setattr(item, "Docbook_InfoType47", self)
                    

    @property
    def Docbook_DocumentRoot34(self):
        return self.__Docbook_DocumentRoot34

    @Docbook_DocumentRoot34.setter
    def Docbook_DocumentRoot34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot34", None)
        self.__Docbook_DocumentRoot34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_AbstractType35"):
                    opp_val = getattr(item, "Docbook_AbstractType35", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_AbstractType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_AbstractType35"):
                    opp_val = getattr(item, "Docbook_AbstractType35", None)
                    
                    setattr(item, "Docbook_AbstractType35", self)
                    

    @property
    def Docbook_DocumentRoot122(self):
        return self.__Docbook_DocumentRoot122

    @Docbook_DocumentRoot122.setter
    def Docbook_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot122", None)
        self.__Docbook_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType"):
                    opp_val = getattr(item, "Docbook_UlinkType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType"):
                    opp_val = getattr(item, "Docbook_UlinkType", None)
                    
                    setattr(item, "Docbook_UlinkType", self)
                    

    @property
    def Docbook_DocumentRoot66(self):
        return self.__Docbook_DocumentRoot66

    @Docbook_DocumentRoot66.setter
    def Docbook_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot66", None)
        self.__Docbook_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ImageobjectType"):
                    opp_val = getattr(item, "Docbook_ImageobjectType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ImageobjectType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ImageobjectType"):
                    opp_val = getattr(item, "Docbook_ImageobjectType", None)
                    
                    setattr(item, "Docbook_ImageobjectType", self)
                    

    @property
    def Docbook_DocumentRoot104(self):
        return self.__Docbook_DocumentRoot104

    @Docbook_DocumentRoot104.setter
    def Docbook_DocumentRoot104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DocumentRoot__Docbook_DocumentRoot104", None)
        self.__Docbook_DocumentRoot104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_RowType"):
                    opp_val = getattr(item, "Docbook_RowType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_RowType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_RowType"):
                    opp_val = getattr(item, "Docbook_RowType", None)
                    
                    setattr(item, "Docbook_RowType", self)
                    

class Docbook_DateType:

    def __init__(self, mixed: str, Docbook_DateType: "Docbook_RevisionType" = None):
        self.mixed = mixed
        self.Docbook_DateType = Docbook_DateType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_DateType(self):
        return self.__Docbook_DateType

    @Docbook_DateType.setter
    def Docbook_DateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_DateType__Docbook_DateType", None)
        self.__Docbook_DateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevisionType326"):
                opp_val = getattr(old_value, "Docbook_RevisionType326", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevisionType326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevisionType326"):
                opp_val = getattr(value, "Docbook_RevisionType326", None)
                setattr(value, "Docbook_RevisionType326", self)

class Docbook_EStringToStringMapEntry:

    pass
class Docbook_CopyrightType:

    def __init__(self, group: str, year: str, holder: str, Docbook_CopyrightType: "Docbook_InfoType" = None):
        self.group = group
        self.year = year
        self.holder = holder
        self.Docbook_CopyrightType = Docbook_CopyrightType
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def holder(self) -> str:
        return self.__holder

    @holder.setter
    def holder(self, holder: str):
        self.__holder = holder

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def Docbook_CopyrightType(self):
        return self.__Docbook_CopyrightType

    @Docbook_CopyrightType.setter
    def Docbook_CopyrightType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_CopyrightType__Docbook_CopyrightType", None)
        self.__Docbook_CopyrightType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType195"):
                opp_val = getattr(old_value, "Docbook_InfoType195", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType195"):
                opp_val = getattr(value, "Docbook_InfoType195", None)
                setattr(value, "Docbook_InfoType195", self)

class Docbook_CommandType:

    def __init__(self, mixed: str, Docbook_CommandType: "Docbook_CmdsynopsisType" = None):
        self.mixed = mixed
        self.Docbook_CommandType = Docbook_CommandType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_CommandType(self):
        return self.__Docbook_CommandType

    @Docbook_CommandType.setter
    def Docbook_CommandType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_CommandType__Docbook_CommandType", None)
        self.__Docbook_CommandType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_CmdsynopsisType"):
                opp_val = getattr(old_value, "Docbook_CmdsynopsisType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_CmdsynopsisType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_CmdsynopsisType"):
                opp_val = getattr(value, "Docbook_CmdsynopsisType", None)
                setattr(value, "Docbook_CmdsynopsisType", self)

class Docbook_CmdsynopsisType:

    pass
class Docbook_ConfgroupType:

    def __init__(self, conftitle: str, confnum: str, confsponsor: str, Docbook_ConfgroupType: "Docbook_DocumentRoot" = None, Docbook_ConfgroupType191: "Docbook_InfoType" = None):
        self.conftitle = conftitle
        self.confnum = confnum
        self.confsponsor = confsponsor
        self.Docbook_ConfgroupType = Docbook_ConfgroupType
        self.Docbook_ConfgroupType191 = Docbook_ConfgroupType191
        
    @property
    def conftitle(self) -> str:
        return self.__conftitle

    @conftitle.setter
    def conftitle(self, conftitle: str):
        self.__conftitle = conftitle

    @property
    def confsponsor(self) -> str:
        return self.__confsponsor

    @confsponsor.setter
    def confsponsor(self, confsponsor: str):
        self.__confsponsor = confsponsor

    @property
    def confnum(self) -> str:
        return self.__confnum

    @confnum.setter
    def confnum(self, confnum: str):
        self.__confnum = confnum

    @property
    def Docbook_ConfgroupType(self):
        return self.__Docbook_ConfgroupType

    @Docbook_ConfgroupType.setter
    def Docbook_ConfgroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ConfgroupType__Docbook_ConfgroupType", None)
        self.__Docbook_ConfgroupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot54"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot54"):
                opp_val = getattr(value, "Docbook_DocumentRoot54", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ConfgroupType191(self):
        return self.__Docbook_ConfgroupType191

    @Docbook_ConfgroupType191.setter
    def Docbook_ConfgroupType191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ConfgroupType__Docbook_ConfgroupType191", None)
        self.__Docbook_ConfgroupType191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType190"):
                opp_val = getattr(old_value, "Docbook_InfoType190", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType190"):
                opp_val = getattr(value, "Docbook_InfoType190", None)
                setattr(value, "Docbook_InfoType190", self)

class Docbook_TitleType:

    def __init__(self, group: str, mixed: str, Docbook_TitleType: "Docbook_ChapterType" = None, Docbook_TitleType120: "Docbook_DocumentRoot" = None, Docbook_TitleType144: "Docbook_FigureType" = None, Docbook_TitleType138: "Docbook_ExampleType" = None, Docbook_TitleType177: "Docbook_InfoType" = None, Docbook_TitleType203: "Docbook_LegalNoticeType" = None, Docbook_TitleType262: "Docbook_PrefaceType" = None, Docbook_TitleType296: "Docbook_ReferenceType" = None, Docbook_TitleType304: "Docbook_RefSect1Type" = None, Docbook_TitleType358: "Docbook_SectionType" = None, Docbook_TitleType395: "Docbook_TableType" = None, Docbook_TitleType429: set["Docbook_EmphasisType"] = None, Docbook_TitleType432: set["Docbook_PhraseType"] = None):
        self.group = group
        self.mixed = mixed
        self.Docbook_TitleType = Docbook_TitleType
        self.Docbook_TitleType120 = Docbook_TitleType120
        self.Docbook_TitleType144 = Docbook_TitleType144
        self.Docbook_TitleType138 = Docbook_TitleType138
        self.Docbook_TitleType177 = Docbook_TitleType177
        self.Docbook_TitleType203 = Docbook_TitleType203
        self.Docbook_TitleType262 = Docbook_TitleType262
        self.Docbook_TitleType296 = Docbook_TitleType296
        self.Docbook_TitleType304 = Docbook_TitleType304
        self.Docbook_TitleType358 = Docbook_TitleType358
        self.Docbook_TitleType395 = Docbook_TitleType395
        self.Docbook_TitleType429 = Docbook_TitleType429 if Docbook_TitleType429 is not None else set()
        self.Docbook_TitleType432 = Docbook_TitleType432 if Docbook_TitleType432 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_TitleType358(self):
        return self.__Docbook_TitleType358

    @Docbook_TitleType358.setter
    def Docbook_TitleType358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType358", None)
        self.__Docbook_TitleType358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType357"):
                opp_val = getattr(old_value, "Docbook_SectionType357", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType357"):
                opp_val = getattr(value, "Docbook_SectionType357", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType357", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TitleType177(self):
        return self.__Docbook_TitleType177

    @Docbook_TitleType177.setter
    def Docbook_TitleType177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType177", None)
        self.__Docbook_TitleType177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType176"):
                opp_val = getattr(old_value, "Docbook_InfoType176", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType176"):
                opp_val = getattr(value, "Docbook_InfoType176", None)
                setattr(value, "Docbook_InfoType176", self)

    @property
    def Docbook_TitleType432(self):
        return self.__Docbook_TitleType432

    @Docbook_TitleType432.setter
    def Docbook_TitleType432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType432", None)
        self.__Docbook_TitleType432 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_PhraseType433"):
                    opp_val = getattr(item, "Docbook_PhraseType433", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_PhraseType433", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_PhraseType433"):
                    opp_val = getattr(item, "Docbook_PhraseType433", None)
                    
                    setattr(item, "Docbook_PhraseType433", self)
                    

    @property
    def Docbook_TitleType429(self):
        return self.__Docbook_TitleType429

    @Docbook_TitleType429.setter
    def Docbook_TitleType429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType429", None)
        self.__Docbook_TitleType429 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType430"):
                    opp_val = getattr(item, "Docbook_EmphasisType430", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType430", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType430"):
                    opp_val = getattr(item, "Docbook_EmphasisType430", None)
                    
                    setattr(item, "Docbook_EmphasisType430", self)
                    

    @property
    def Docbook_TitleType296(self):
        return self.__Docbook_TitleType296

    @Docbook_TitleType296.setter
    def Docbook_TitleType296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType296", None)
        self.__Docbook_TitleType296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ReferenceType295"):
                opp_val = getattr(old_value, "Docbook_ReferenceType295", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ReferenceType295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ReferenceType295"):
                opp_val = getattr(value, "Docbook_ReferenceType295", None)
                setattr(value, "Docbook_ReferenceType295", self)

    @property
    def Docbook_TitleType304(self):
        return self.__Docbook_TitleType304

    @Docbook_TitleType304.setter
    def Docbook_TitleType304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType304", None)
        self.__Docbook_TitleType304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefSect1Type303"):
                opp_val = getattr(old_value, "Docbook_RefSect1Type303", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefSect1Type303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefSect1Type303"):
                opp_val = getattr(value, "Docbook_RefSect1Type303", None)
                setattr(value, "Docbook_RefSect1Type303", self)

    @property
    def Docbook_TitleType138(self):
        return self.__Docbook_TitleType138

    @Docbook_TitleType138.setter
    def Docbook_TitleType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType138", None)
        self.__Docbook_TitleType138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ExampleType"):
                opp_val = getattr(old_value, "Docbook_ExampleType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ExampleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ExampleType"):
                opp_val = getattr(value, "Docbook_ExampleType", None)
                setattr(value, "Docbook_ExampleType", self)

    @property
    def Docbook_TitleType203(self):
        return self.__Docbook_TitleType203

    @Docbook_TitleType203.setter
    def Docbook_TitleType203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType203", None)
        self.__Docbook_TitleType203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_LegalNoticeType202"):
                opp_val = getattr(old_value, "Docbook_LegalNoticeType202", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_LegalNoticeType202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_LegalNoticeType202"):
                opp_val = getattr(value, "Docbook_LegalNoticeType202", None)
                setattr(value, "Docbook_LegalNoticeType202", self)

    @property
    def Docbook_TitleType120(self):
        return self.__Docbook_TitleType120

    @Docbook_TitleType120.setter
    def Docbook_TitleType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType120", None)
        self.__Docbook_TitleType120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot119"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot119"):
                opp_val = getattr(value, "Docbook_DocumentRoot119", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_TitleType(self):
        return self.__Docbook_TitleType

    @Docbook_TitleType.setter
    def Docbook_TitleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType", None)
        self.__Docbook_TitleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ChapterType17"):
                opp_val = getattr(old_value, "Docbook_ChapterType17", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ChapterType17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ChapterType17"):
                opp_val = getattr(value, "Docbook_ChapterType17", None)
                setattr(value, "Docbook_ChapterType17", self)

    @property
    def Docbook_TitleType144(self):
        return self.__Docbook_TitleType144

    @Docbook_TitleType144.setter
    def Docbook_TitleType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType144", None)
        self.__Docbook_TitleType144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FigureType143"):
                opp_val = getattr(old_value, "Docbook_FigureType143", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_FigureType143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FigureType143"):
                opp_val = getattr(value, "Docbook_FigureType143", None)
                setattr(value, "Docbook_FigureType143", self)

    @property
    def Docbook_TitleType395(self):
        return self.__Docbook_TitleType395

    @Docbook_TitleType395.setter
    def Docbook_TitleType395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType395", None)
        self.__Docbook_TitleType395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TableType394"):
                opp_val = getattr(old_value, "Docbook_TableType394", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TableType394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TableType394"):
                opp_val = getattr(value, "Docbook_TableType394", None)
                setattr(value, "Docbook_TableType394", self)

    @property
    def Docbook_TitleType262(self):
        return self.__Docbook_TitleType262

    @Docbook_TitleType262.setter
    def Docbook_TitleType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_TitleType__Docbook_TitleType262", None)
        self.__Docbook_TitleType262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PrefaceType261"):
                opp_val = getattr(old_value, "Docbook_PrefaceType261", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PrefaceType261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PrefaceType261"):
                opp_val = getattr(value, "Docbook_PrefaceType261", None)
                setattr(value, "Docbook_PrefaceType261", self)

class Docbook_ColspecType:

    def __init__(self, colname: str, colwidth: str, Docbook_ColspecType: "Docbook_DocumentRoot" = None, Docbook_ColspecType415: "Docbook_TgroupType" = None):
        self.colname = colname
        self.colwidth = colwidth
        self.Docbook_ColspecType = Docbook_ColspecType
        self.Docbook_ColspecType415 = Docbook_ColspecType415
        
    @property
    def colname(self) -> str:
        return self.__colname

    @colname.setter
    def colname(self, colname: str):
        self.__colname = colname

    @property
    def colwidth(self) -> str:
        return self.__colwidth

    @colwidth.setter
    def colwidth(self, colwidth: str):
        self.__colwidth = colwidth

    @property
    def Docbook_ColspecType(self):
        return self.__Docbook_ColspecType

    @Docbook_ColspecType.setter
    def Docbook_ColspecType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ColspecType__Docbook_ColspecType", None)
        self.__Docbook_ColspecType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot52"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot52"):
                opp_val = getattr(value, "Docbook_DocumentRoot52", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ColspecType415(self):
        return self.__Docbook_ColspecType415

    @Docbook_ColspecType415.setter
    def Docbook_ColspecType415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ColspecType__Docbook_ColspecType415", None)
        self.__Docbook_ColspecType415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TgroupType414"):
                opp_val = getattr(old_value, "Docbook_TgroupType414", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TgroupType414"):
                opp_val = getattr(value, "Docbook_TgroupType414", None)
                if opp_val is None:
                    setattr(value, "Docbook_TgroupType414", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_SectionType:

    def __init__(self, group: str, caution: str, warning: str, annotations: str, Docbook_SectionType: "Docbook_ChapterType" = None, Docbook_SectionType107: "Docbook_DocumentRoot" = None, Docbook_SectionType342: set["Docbook_MediaobjectType"] = None, Docbook_SectionType339: set["Docbook_ItemizedlistType"] = None, Docbook_SectionType348: set["Docbook_ParaType"] = None, Docbook_SectionType345: set["Docbook_NoteType"] = None, Docbook_SectionType355: "Docbook_SectionType" = None, Docbook_SectionType353: set["Docbook_SectionType"] = None, Docbook_SectionType351: set["Docbook_ProgramlistingType"] = None, Docbook_SectionType363: set["Docbook_InformaltableType"] = None, Docbook_SectionType366: set["Docbook_OrderedlistType"] = None, Docbook_SectionType357: set["Docbook_TitleType"] = None, Docbook_SectionType360: set["Docbook_FigureType"] = None, Docbook_SectionType372: "Docbook_TipType" = None, Docbook_SectionType375: set["Docbook_FuncsynopsisType"] = None, Docbook_SectionType369: set["Docbook_TableType"] = None, Docbook_SectionType378: "Docbook_ExampleType" = None, Docbook_SectionType381: set["Docbook_CmdsynopsisType"] = None):
        self.group = group
        self.caution = caution
        self.warning = warning
        self.annotations = annotations
        self.Docbook_SectionType = Docbook_SectionType
        self.Docbook_SectionType107 = Docbook_SectionType107
        self.Docbook_SectionType342 = Docbook_SectionType342 if Docbook_SectionType342 is not None else set()
        self.Docbook_SectionType339 = Docbook_SectionType339 if Docbook_SectionType339 is not None else set()
        self.Docbook_SectionType348 = Docbook_SectionType348 if Docbook_SectionType348 is not None else set()
        self.Docbook_SectionType345 = Docbook_SectionType345 if Docbook_SectionType345 is not None else set()
        self.Docbook_SectionType355 = Docbook_SectionType355
        self.Docbook_SectionType353 = Docbook_SectionType353 if Docbook_SectionType353 is not None else set()
        self.Docbook_SectionType351 = Docbook_SectionType351 if Docbook_SectionType351 is not None else set()
        self.Docbook_SectionType363 = Docbook_SectionType363 if Docbook_SectionType363 is not None else set()
        self.Docbook_SectionType366 = Docbook_SectionType366 if Docbook_SectionType366 is not None else set()
        self.Docbook_SectionType357 = Docbook_SectionType357 if Docbook_SectionType357 is not None else set()
        self.Docbook_SectionType360 = Docbook_SectionType360 if Docbook_SectionType360 is not None else set()
        self.Docbook_SectionType372 = Docbook_SectionType372
        self.Docbook_SectionType375 = Docbook_SectionType375 if Docbook_SectionType375 is not None else set()
        self.Docbook_SectionType369 = Docbook_SectionType369 if Docbook_SectionType369 is not None else set()
        self.Docbook_SectionType378 = Docbook_SectionType378
        self.Docbook_SectionType381 = Docbook_SectionType381 if Docbook_SectionType381 is not None else set()
        
    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def caution(self) -> str:
        return self.__caution

    @caution.setter
    def caution(self, caution: str):
        self.__caution = caution

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def warning(self) -> str:
        return self.__warning

    @warning.setter
    def warning(self, warning: str):
        self.__warning = warning

    @property
    def Docbook_SectionType351(self):
        return self.__Docbook_SectionType351

    @Docbook_SectionType351.setter
    def Docbook_SectionType351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType351", None)
        self.__Docbook_SectionType351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ProgramlistingType352"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType352", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ProgramlistingType352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ProgramlistingType352"):
                    opp_val = getattr(item, "Docbook_ProgramlistingType352", None)
                    
                    setattr(item, "Docbook_ProgramlistingType352", self)
                    

    @property
    def Docbook_SectionType375(self):
        return self.__Docbook_SectionType375

    @Docbook_SectionType375.setter
    def Docbook_SectionType375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType375", None)
        self.__Docbook_SectionType375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FuncsynopsisType376"):
                    opp_val = getattr(item, "Docbook_FuncsynopsisType376", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FuncsynopsisType376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FuncsynopsisType376"):
                    opp_val = getattr(item, "Docbook_FuncsynopsisType376", None)
                    
                    setattr(item, "Docbook_FuncsynopsisType376", self)
                    

    @property
    def Docbook_SectionType348(self):
        return self.__Docbook_SectionType348

    @Docbook_SectionType348.setter
    def Docbook_SectionType348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType348", None)
        self.__Docbook_SectionType348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType349"):
                    opp_val = getattr(item, "Docbook_ParaType349", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType349"):
                    opp_val = getattr(item, "Docbook_ParaType349", None)
                    
                    setattr(item, "Docbook_ParaType349", self)
                    

    @property
    def Docbook_SectionType369(self):
        return self.__Docbook_SectionType369

    @Docbook_SectionType369.setter
    def Docbook_SectionType369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType369", None)
        self.__Docbook_SectionType369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TableType370"):
                    opp_val = getattr(item, "Docbook_TableType370", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TableType370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TableType370"):
                    opp_val = getattr(item, "Docbook_TableType370", None)
                    
                    setattr(item, "Docbook_TableType370", self)
                    

    @property
    def Docbook_SectionType357(self):
        return self.__Docbook_SectionType357

    @Docbook_SectionType357.setter
    def Docbook_SectionType357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType357", None)
        self.__Docbook_SectionType357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_TitleType358"):
                    opp_val = getattr(item, "Docbook_TitleType358", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_TitleType358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_TitleType358"):
                    opp_val = getattr(item, "Docbook_TitleType358", None)
                    
                    setattr(item, "Docbook_TitleType358", self)
                    

    @property
    def Docbook_SectionType372(self):
        return self.__Docbook_SectionType372

    @Docbook_SectionType372.setter
    def Docbook_SectionType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType372", None)
        self.__Docbook_SectionType372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TipType373"):
                opp_val = getattr(old_value, "Docbook_TipType373", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TipType373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TipType373"):
                opp_val = getattr(value, "Docbook_TipType373", None)
                setattr(value, "Docbook_TipType373", self)

    @property
    def Docbook_SectionType381(self):
        return self.__Docbook_SectionType381

    @Docbook_SectionType381.setter
    def Docbook_SectionType381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType381", None)
        self.__Docbook_SectionType381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_CmdsynopsisType382"):
                    opp_val = getattr(item, "Docbook_CmdsynopsisType382", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_CmdsynopsisType382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_CmdsynopsisType382"):
                    opp_val = getattr(item, "Docbook_CmdsynopsisType382", None)
                    
                    setattr(item, "Docbook_CmdsynopsisType382", self)
                    

    @property
    def Docbook_SectionType353(self):
        return self.__Docbook_SectionType353

    @Docbook_SectionType353.setter
    def Docbook_SectionType353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType353", None)
        self.__Docbook_SectionType353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_SectionType355"):
                    opp_val = getattr(item, "Docbook_SectionType355", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_SectionType355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_SectionType355"):
                    opp_val = getattr(item, "Docbook_SectionType355", None)
                    
                    setattr(item, "Docbook_SectionType355", self)
                    

    @property
    def Docbook_SectionType(self):
        return self.__Docbook_SectionType

    @Docbook_SectionType.setter
    def Docbook_SectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType", None)
        self.__Docbook_SectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ChapterType24"):
                opp_val = getattr(old_value, "Docbook_ChapterType24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ChapterType24"):
                opp_val = getattr(value, "Docbook_ChapterType24", None)
                if opp_val is None:
                    setattr(value, "Docbook_ChapterType24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_SectionType355(self):
        return self.__Docbook_SectionType355

    @Docbook_SectionType355.setter
    def Docbook_SectionType355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType355", None)
        self.__Docbook_SectionType355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType353"):
                opp_val = getattr(old_value, "Docbook_SectionType353", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType353"):
                opp_val = getattr(value, "Docbook_SectionType353", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType353", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_SectionType363(self):
        return self.__Docbook_SectionType363

    @Docbook_SectionType363.setter
    def Docbook_SectionType363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType363", None)
        self.__Docbook_SectionType363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_InformaltableType364"):
                    opp_val = getattr(item, "Docbook_InformaltableType364", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_InformaltableType364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_InformaltableType364"):
                    opp_val = getattr(item, "Docbook_InformaltableType364", None)
                    
                    setattr(item, "Docbook_InformaltableType364", self)
                    

    @property
    def Docbook_SectionType378(self):
        return self.__Docbook_SectionType378

    @Docbook_SectionType378.setter
    def Docbook_SectionType378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType378", None)
        self.__Docbook_SectionType378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ExampleType379"):
                opp_val = getattr(old_value, "Docbook_ExampleType379", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ExampleType379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ExampleType379"):
                opp_val = getattr(value, "Docbook_ExampleType379", None)
                setattr(value, "Docbook_ExampleType379", self)

    @property
    def Docbook_SectionType360(self):
        return self.__Docbook_SectionType360

    @Docbook_SectionType360.setter
    def Docbook_SectionType360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType360", None)
        self.__Docbook_SectionType360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FigureType361"):
                    opp_val = getattr(item, "Docbook_FigureType361", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FigureType361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FigureType361"):
                    opp_val = getattr(item, "Docbook_FigureType361", None)
                    
                    setattr(item, "Docbook_FigureType361", self)
                    

    @property
    def Docbook_SectionType366(self):
        return self.__Docbook_SectionType366

    @Docbook_SectionType366.setter
    def Docbook_SectionType366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType366", None)
        self.__Docbook_SectionType366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OrderedlistType367"):
                    opp_val = getattr(item, "Docbook_OrderedlistType367", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OrderedlistType367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OrderedlistType367"):
                    opp_val = getattr(item, "Docbook_OrderedlistType367", None)
                    
                    setattr(item, "Docbook_OrderedlistType367", self)
                    

    @property
    def Docbook_SectionType342(self):
        return self.__Docbook_SectionType342

    @Docbook_SectionType342.setter
    def Docbook_SectionType342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType342", None)
        self.__Docbook_SectionType342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_MediaobjectType343"):
                    opp_val = getattr(item, "Docbook_MediaobjectType343", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_MediaobjectType343", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_MediaobjectType343"):
                    opp_val = getattr(item, "Docbook_MediaobjectType343", None)
                    
                    setattr(item, "Docbook_MediaobjectType343", self)
                    

    @property
    def Docbook_SectionType107(self):
        return self.__Docbook_SectionType107

    @Docbook_SectionType107.setter
    def Docbook_SectionType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType107", None)
        self.__Docbook_SectionType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot106"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot106"):
                opp_val = getattr(value, "Docbook_DocumentRoot106", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_SectionType339(self):
        return self.__Docbook_SectionType339

    @Docbook_SectionType339.setter
    def Docbook_SectionType339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType339", None)
        self.__Docbook_SectionType339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ItemizedlistType340"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType340", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ItemizedlistType340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ItemizedlistType340"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType340", None)
                    
                    setattr(item, "Docbook_ItemizedlistType340", self)
                    

    @property
    def Docbook_SectionType345(self):
        return self.__Docbook_SectionType345

    @Docbook_SectionType345.setter
    def Docbook_SectionType345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_SectionType__Docbook_SectionType345", None)
        self.__Docbook_SectionType345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_NoteType346"):
                    opp_val = getattr(item, "Docbook_NoteType346", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_NoteType346", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_NoteType346"):
                    opp_val = getattr(item, "Docbook_NoteType346", None)
                    
                    setattr(item, "Docbook_NoteType346", self)
                    

class Docbook_NoteType:

    def __init__(self, group: str, mixed: str, Docbook_NoteType: "Docbook_ChapterType" = None, Docbook_NoteType85: "Docbook_DocumentRoot" = None, Docbook_NoteType223: set["Docbook_LiteralType"] = None, Docbook_NoteType226: set["Docbook_UlinkType"] = None, Docbook_NoteType346: "Docbook_SectionType" = None):
        self.group = group
        self.mixed = mixed
        self.Docbook_NoteType = Docbook_NoteType
        self.Docbook_NoteType85 = Docbook_NoteType85
        self.Docbook_NoteType223 = Docbook_NoteType223 if Docbook_NoteType223 is not None else set()
        self.Docbook_NoteType226 = Docbook_NoteType226 if Docbook_NoteType226 is not None else set()
        self.Docbook_NoteType346 = Docbook_NoteType346
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_NoteType226(self):
        return self.__Docbook_NoteType226

    @Docbook_NoteType226.setter
    def Docbook_NoteType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_NoteType__Docbook_NoteType226", None)
        self.__Docbook_NoteType226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType227"):
                    opp_val = getattr(item, "Docbook_UlinkType227", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType227"):
                    opp_val = getattr(item, "Docbook_UlinkType227", None)
                    
                    setattr(item, "Docbook_UlinkType227", self)
                    

    @property
    def Docbook_NoteType85(self):
        return self.__Docbook_NoteType85

    @Docbook_NoteType85.setter
    def Docbook_NoteType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_NoteType__Docbook_NoteType85", None)
        self.__Docbook_NoteType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot84"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot84"):
                opp_val = getattr(value, "Docbook_DocumentRoot84", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_NoteType346(self):
        return self.__Docbook_NoteType346

    @Docbook_NoteType346.setter
    def Docbook_NoteType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_NoteType__Docbook_NoteType346", None)
        self.__Docbook_NoteType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType345"):
                opp_val = getattr(old_value, "Docbook_SectionType345", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType345"):
                opp_val = getattr(value, "Docbook_SectionType345", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType345", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_NoteType223(self):
        return self.__Docbook_NoteType223

    @Docbook_NoteType223.setter
    def Docbook_NoteType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_NoteType__Docbook_NoteType223", None)
        self.__Docbook_NoteType223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_LiteralType224"):
                    opp_val = getattr(item, "Docbook_LiteralType224", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_LiteralType224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_LiteralType224"):
                    opp_val = getattr(item, "Docbook_LiteralType224", None)
                    
                    setattr(item, "Docbook_LiteralType224", self)
                    

    @property
    def Docbook_NoteType(self):
        return self.__Docbook_NoteType

    @Docbook_NoteType.setter
    def Docbook_NoteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_NoteType__Docbook_NoteType", None)
        self.__Docbook_NoteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ChapterType22"):
                opp_val = getattr(old_value, "Docbook_ChapterType22", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ChapterType22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ChapterType22"):
                opp_val = getattr(value, "Docbook_ChapterType22", None)
                setattr(value, "Docbook_ChapterType22", self)

class Docbook_ReferenceType:

    def __init__(self, version: str, Docbook_ReferenceType: "Docbook_BookType" = None, Docbook_ReferenceType292: "Docbook_InfoType" = None, Docbook_ReferenceType295: "Docbook_TitleType" = None, Docbook_ReferenceType298: set["Docbook_RefEntryType"] = None):
        self.version = version
        self.Docbook_ReferenceType = Docbook_ReferenceType
        self.Docbook_ReferenceType292 = Docbook_ReferenceType292
        self.Docbook_ReferenceType295 = Docbook_ReferenceType295
        self.Docbook_ReferenceType298 = Docbook_ReferenceType298 if Docbook_ReferenceType298 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def Docbook_ReferenceType295(self):
        return self.__Docbook_ReferenceType295

    @Docbook_ReferenceType295.setter
    def Docbook_ReferenceType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReferenceType__Docbook_ReferenceType295", None)
        self.__Docbook_ReferenceType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType296"):
                opp_val = getattr(old_value, "Docbook_TitleType296", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType296"):
                opp_val = getattr(value, "Docbook_TitleType296", None)
                setattr(value, "Docbook_TitleType296", self)

    @property
    def Docbook_ReferenceType(self):
        return self.__Docbook_ReferenceType

    @Docbook_ReferenceType.setter
    def Docbook_ReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReferenceType__Docbook_ReferenceType", None)
        self.__Docbook_ReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_BookType15"):
                opp_val = getattr(old_value, "Docbook_BookType15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_BookType15"):
                opp_val = getattr(value, "Docbook_BookType15", None)
                if opp_val is None:
                    setattr(value, "Docbook_BookType15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ReferenceType292(self):
        return self.__Docbook_ReferenceType292

    @Docbook_ReferenceType292.setter
    def Docbook_ReferenceType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReferenceType__Docbook_ReferenceType292", None)
        self.__Docbook_ReferenceType292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType293"):
                opp_val = getattr(old_value, "Docbook_InfoType293", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType293"):
                opp_val = getattr(value, "Docbook_InfoType293", None)
                setattr(value, "Docbook_InfoType293", self)

    @property
    def Docbook_ReferenceType298(self):
        return self.__Docbook_ReferenceType298

    @Docbook_ReferenceType298.setter
    def Docbook_ReferenceType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReferenceType__Docbook_ReferenceType298", None)
        self.__Docbook_ReferenceType298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_RefEntryType299"):
                    opp_val = getattr(item, "Docbook_RefEntryType299", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_RefEntryType299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_RefEntryType299"):
                    opp_val = getattr(item, "Docbook_RefEntryType299", None)
                    
                    setattr(item, "Docbook_RefEntryType299", self)
                    

class Docbook_ChapterType:

    def __init__(self, annotations: str, Docbook_ChapterType: "Docbook_BookType" = None, Docbook_ChapterType22: "Docbook_NoteType" = None, Docbook_ChapterType24: set["Docbook_SectionType"] = None, Docbook_ChapterType17: "Docbook_TitleType" = None, Docbook_ChapterType19: set["Docbook_ParaType"] = None, Docbook_ChapterType50: "Docbook_DocumentRoot" = None):
        self.annotations = annotations
        self.Docbook_ChapterType = Docbook_ChapterType
        self.Docbook_ChapterType22 = Docbook_ChapterType22
        self.Docbook_ChapterType24 = Docbook_ChapterType24 if Docbook_ChapterType24 is not None else set()
        self.Docbook_ChapterType17 = Docbook_ChapterType17
        self.Docbook_ChapterType19 = Docbook_ChapterType19 if Docbook_ChapterType19 is not None else set()
        self.Docbook_ChapterType50 = Docbook_ChapterType50
        
    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def Docbook_ChapterType50(self):
        return self.__Docbook_ChapterType50

    @Docbook_ChapterType50.setter
    def Docbook_ChapterType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType50", None)
        self.__Docbook_ChapterType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot49"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot49"):
                opp_val = getattr(value, "Docbook_DocumentRoot49", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ChapterType22(self):
        return self.__Docbook_ChapterType22

    @Docbook_ChapterType22.setter
    def Docbook_ChapterType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType22", None)
        self.__Docbook_ChapterType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_NoteType"):
                opp_val = getattr(old_value, "Docbook_NoteType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_NoteType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_NoteType"):
                opp_val = getattr(value, "Docbook_NoteType", None)
                setattr(value, "Docbook_NoteType", self)

    @property
    def Docbook_ChapterType19(self):
        return self.__Docbook_ChapterType19

    @Docbook_ChapterType19.setter
    def Docbook_ChapterType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType19", None)
        self.__Docbook_ChapterType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ParaType20"):
                    opp_val = getattr(item, "Docbook_ParaType20", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ParaType20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ParaType20"):
                    opp_val = getattr(item, "Docbook_ParaType20", None)
                    
                    setattr(item, "Docbook_ParaType20", self)
                    

    @property
    def Docbook_ChapterType17(self):
        return self.__Docbook_ChapterType17

    @Docbook_ChapterType17.setter
    def Docbook_ChapterType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType17", None)
        self.__Docbook_ChapterType17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType"):
                opp_val = getattr(old_value, "Docbook_TitleType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType"):
                opp_val = getattr(value, "Docbook_TitleType", None)
                setattr(value, "Docbook_TitleType", self)

    @property
    def Docbook_ChapterType24(self):
        return self.__Docbook_ChapterType24

    @Docbook_ChapterType24.setter
    def Docbook_ChapterType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType24", None)
        self.__Docbook_ChapterType24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_SectionType"):
                    opp_val = getattr(item, "Docbook_SectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_SectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_SectionType"):
                    opp_val = getattr(item, "Docbook_SectionType", None)
                    
                    setattr(item, "Docbook_SectionType", self)
                    

    @property
    def Docbook_ChapterType(self):
        return self.__Docbook_ChapterType

    @Docbook_ChapterType.setter
    def Docbook_ChapterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ChapterType__Docbook_ChapterType", None)
        self.__Docbook_ChapterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_BookType13"):
                opp_val = getattr(old_value, "Docbook_BookType13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_BookType13"):
                opp_val = getattr(value, "Docbook_BookType13", None)
                if opp_val is None:
                    setattr(value, "Docbook_BookType13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_PrefaceType:

    pass
class Docbook_BookType:

    def __init__(self, lang: str, version: str, label: str, Docbook_BookType: "Docbook_InfoType" = None, Docbook_BookType15: set["Docbook_ReferenceType"] = None, Docbook_BookType11: "Docbook_PrefaceType" = None, Docbook_BookType13: set["Docbook_ChapterType"] = None, Docbook_BookType44: "Docbook_DocumentRoot" = None):
        self.lang = lang
        self.version = version
        self.label = label
        self.Docbook_BookType = Docbook_BookType
        self.Docbook_BookType15 = Docbook_BookType15 if Docbook_BookType15 is not None else set()
        self.Docbook_BookType11 = Docbook_BookType11
        self.Docbook_BookType13 = Docbook_BookType13 if Docbook_BookType13 is not None else set()
        self.Docbook_BookType44 = Docbook_BookType44
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def Docbook_BookType(self):
        return self.__Docbook_BookType

    @Docbook_BookType.setter
    def Docbook_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_BookType__Docbook_BookType", None)
        self.__Docbook_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType"):
                opp_val = getattr(old_value, "Docbook_InfoType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_InfoType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType"):
                opp_val = getattr(value, "Docbook_InfoType", None)
                setattr(value, "Docbook_InfoType", self)

    @property
    def Docbook_BookType44(self):
        return self.__Docbook_BookType44

    @Docbook_BookType44.setter
    def Docbook_BookType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_BookType__Docbook_BookType44", None)
        self.__Docbook_BookType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot43"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot43"):
                opp_val = getattr(value, "Docbook_DocumentRoot43", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_BookType13(self):
        return self.__Docbook_BookType13

    @Docbook_BookType13.setter
    def Docbook_BookType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_BookType__Docbook_BookType13", None)
        self.__Docbook_BookType13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ChapterType"):
                    opp_val = getattr(item, "Docbook_ChapterType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ChapterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ChapterType"):
                    opp_val = getattr(item, "Docbook_ChapterType", None)
                    
                    setattr(item, "Docbook_ChapterType", self)
                    

    @property
    def Docbook_BookType15(self):
        return self.__Docbook_BookType15

    @Docbook_BookType15.setter
    def Docbook_BookType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_BookType__Docbook_BookType15", None)
        self.__Docbook_BookType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ReferenceType"):
                    opp_val = getattr(item, "Docbook_ReferenceType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ReferenceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ReferenceType"):
                    opp_val = getattr(item, "Docbook_ReferenceType", None)
                    
                    setattr(item, "Docbook_ReferenceType", self)
                    

    @property
    def Docbook_BookType11(self):
        return self.__Docbook_BookType11

    @Docbook_BookType11.setter
    def Docbook_BookType11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_BookType__Docbook_BookType11", None)
        self.__Docbook_BookType11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PrefaceType"):
                opp_val = getattr(old_value, "Docbook_PrefaceType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PrefaceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PrefaceType"):
                opp_val = getattr(value, "Docbook_PrefaceType", None)
                setattr(value, "Docbook_PrefaceType", self)

class Docbook_InfoType:

    def __init__(self, pubdate: str, bibliomisc: str, date: str, group: str, releaseinfo: str, productname: str, Docbook_InfoType: "Docbook_BookType" = None, Docbook_InfoType47: "Docbook_DocumentRoot" = None, Docbook_InfoType173: set["Docbook_AuthorType"] = None, Docbook_InfoType181: set["Docbook_KeywordsetType"] = None, Docbook_InfoType176: "Docbook_TitleType" = None, Docbook_InfoType179: "Docbook_SubtitleType" = None, Docbook_InfoType190: "Docbook_ConfgroupType" = None, Docbook_InfoType193: "Docbook_RevhistoryType" = None, Docbook_InfoType195: "Docbook_CopyrightType" = None, Docbook_InfoType184: "Docbook_AbstractType" = None, Docbook_InfoType187: "Docbook_PublisherType" = None, Docbook_InfoType197: "Docbook_LegalNoticeType" = None, Docbook_InfoType282: "Docbook_RefEntryType" = None, Docbook_InfoType293: "Docbook_ReferenceType" = None):
        self.pubdate = pubdate
        self.bibliomisc = bibliomisc
        self.date = date
        self.group = group
        self.releaseinfo = releaseinfo
        self.productname = productname
        self.Docbook_InfoType = Docbook_InfoType
        self.Docbook_InfoType47 = Docbook_InfoType47
        self.Docbook_InfoType173 = Docbook_InfoType173 if Docbook_InfoType173 is not None else set()
        self.Docbook_InfoType181 = Docbook_InfoType181 if Docbook_InfoType181 is not None else set()
        self.Docbook_InfoType176 = Docbook_InfoType176
        self.Docbook_InfoType179 = Docbook_InfoType179
        self.Docbook_InfoType190 = Docbook_InfoType190
        self.Docbook_InfoType193 = Docbook_InfoType193
        self.Docbook_InfoType195 = Docbook_InfoType195
        self.Docbook_InfoType184 = Docbook_InfoType184
        self.Docbook_InfoType187 = Docbook_InfoType187
        self.Docbook_InfoType197 = Docbook_InfoType197
        self.Docbook_InfoType282 = Docbook_InfoType282
        self.Docbook_InfoType293 = Docbook_InfoType293
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def releaseinfo(self) -> str:
        return self.__releaseinfo

    @releaseinfo.setter
    def releaseinfo(self, releaseinfo: str):
        self.__releaseinfo = releaseinfo

    @property
    def productname(self) -> str:
        return self.__productname

    @productname.setter
    def productname(self, productname: str):
        self.__productname = productname

    @property
    def pubdate(self) -> str:
        return self.__pubdate

    @pubdate.setter
    def pubdate(self, pubdate: str):
        self.__pubdate = pubdate

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def bibliomisc(self) -> str:
        return self.__bibliomisc

    @bibliomisc.setter
    def bibliomisc(self, bibliomisc: str):
        self.__bibliomisc = bibliomisc

    @property
    def Docbook_InfoType195(self):
        return self.__Docbook_InfoType195

    @Docbook_InfoType195.setter
    def Docbook_InfoType195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType195", None)
        self.__Docbook_InfoType195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_CopyrightType"):
                opp_val = getattr(old_value, "Docbook_CopyrightType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_CopyrightType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_CopyrightType"):
                opp_val = getattr(value, "Docbook_CopyrightType", None)
                setattr(value, "Docbook_CopyrightType", self)

    @property
    def Docbook_InfoType187(self):
        return self.__Docbook_InfoType187

    @Docbook_InfoType187.setter
    def Docbook_InfoType187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType187", None)
        self.__Docbook_InfoType187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PublisherType188"):
                opp_val = getattr(old_value, "Docbook_PublisherType188", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PublisherType188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PublisherType188"):
                opp_val = getattr(value, "Docbook_PublisherType188", None)
                setattr(value, "Docbook_PublisherType188", self)

    @property
    def Docbook_InfoType181(self):
        return self.__Docbook_InfoType181

    @Docbook_InfoType181.setter
    def Docbook_InfoType181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType181", None)
        self.__Docbook_InfoType181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_KeywordsetType182"):
                    opp_val = getattr(item, "Docbook_KeywordsetType182", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_KeywordsetType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_KeywordsetType182"):
                    opp_val = getattr(item, "Docbook_KeywordsetType182", None)
                    
                    setattr(item, "Docbook_KeywordsetType182", self)
                    

    @property
    def Docbook_InfoType176(self):
        return self.__Docbook_InfoType176

    @Docbook_InfoType176.setter
    def Docbook_InfoType176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType176", None)
        self.__Docbook_InfoType176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TitleType177"):
                opp_val = getattr(old_value, "Docbook_TitleType177", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_TitleType177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TitleType177"):
                opp_val = getattr(value, "Docbook_TitleType177", None)
                setattr(value, "Docbook_TitleType177", self)

    @property
    def Docbook_InfoType47(self):
        return self.__Docbook_InfoType47

    @Docbook_InfoType47.setter
    def Docbook_InfoType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType47", None)
        self.__Docbook_InfoType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot46"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot46"):
                opp_val = getattr(value, "Docbook_DocumentRoot46", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_InfoType179(self):
        return self.__Docbook_InfoType179

    @Docbook_InfoType179.setter
    def Docbook_InfoType179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType179", None)
        self.__Docbook_InfoType179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SubtitleType"):
                opp_val = getattr(old_value, "Docbook_SubtitleType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_SubtitleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SubtitleType"):
                opp_val = getattr(value, "Docbook_SubtitleType", None)
                setattr(value, "Docbook_SubtitleType", self)

    @property
    def Docbook_InfoType193(self):
        return self.__Docbook_InfoType193

    @Docbook_InfoType193.setter
    def Docbook_InfoType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType193", None)
        self.__Docbook_InfoType193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevhistoryType"):
                opp_val = getattr(old_value, "Docbook_RevhistoryType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevhistoryType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevhistoryType"):
                opp_val = getattr(value, "Docbook_RevhistoryType", None)
                setattr(value, "Docbook_RevhistoryType", self)

    @property
    def Docbook_InfoType282(self):
        return self.__Docbook_InfoType282

    @Docbook_InfoType282.setter
    def Docbook_InfoType282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType282", None)
        self.__Docbook_InfoType282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefEntryType"):
                opp_val = getattr(old_value, "Docbook_RefEntryType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RefEntryType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefEntryType"):
                opp_val = getattr(value, "Docbook_RefEntryType", None)
                setattr(value, "Docbook_RefEntryType", self)

    @property
    def Docbook_InfoType197(self):
        return self.__Docbook_InfoType197

    @Docbook_InfoType197.setter
    def Docbook_InfoType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType197", None)
        self.__Docbook_InfoType197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_LegalNoticeType"):
                opp_val = getattr(old_value, "Docbook_LegalNoticeType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_LegalNoticeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_LegalNoticeType"):
                opp_val = getattr(value, "Docbook_LegalNoticeType", None)
                setattr(value, "Docbook_LegalNoticeType", self)

    @property
    def Docbook_InfoType173(self):
        return self.__Docbook_InfoType173

    @Docbook_InfoType173.setter
    def Docbook_InfoType173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType173", None)
        self.__Docbook_InfoType173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_AuthorType174"):
                    opp_val = getattr(item, "Docbook_AuthorType174", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_AuthorType174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_AuthorType174"):
                    opp_val = getattr(item, "Docbook_AuthorType174", None)
                    
                    setattr(item, "Docbook_AuthorType174", self)
                    

    @property
    def Docbook_InfoType293(self):
        return self.__Docbook_InfoType293

    @Docbook_InfoType293.setter
    def Docbook_InfoType293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType293", None)
        self.__Docbook_InfoType293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ReferenceType292"):
                opp_val = getattr(old_value, "Docbook_ReferenceType292", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ReferenceType292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ReferenceType292"):
                opp_val = getattr(value, "Docbook_ReferenceType292", None)
                setattr(value, "Docbook_ReferenceType292", self)

    @property
    def Docbook_InfoType184(self):
        return self.__Docbook_InfoType184

    @Docbook_InfoType184.setter
    def Docbook_InfoType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType184", None)
        self.__Docbook_InfoType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_AbstractType185"):
                opp_val = getattr(old_value, "Docbook_AbstractType185", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_AbstractType185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_AbstractType185"):
                opp_val = getattr(value, "Docbook_AbstractType185", None)
                setattr(value, "Docbook_AbstractType185", self)

    @property
    def Docbook_InfoType(self):
        return self.__Docbook_InfoType

    @Docbook_InfoType.setter
    def Docbook_InfoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType", None)
        self.__Docbook_InfoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_BookType"):
                opp_val = getattr(old_value, "Docbook_BookType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_BookType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_BookType"):
                opp_val = getattr(value, "Docbook_BookType", None)
                setattr(value, "Docbook_BookType", self)

    @property
    def Docbook_InfoType190(self):
        return self.__Docbook_InfoType190

    @Docbook_InfoType190.setter
    def Docbook_InfoType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_InfoType__Docbook_InfoType190", None)
        self.__Docbook_InfoType190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ConfgroupType191"):
                opp_val = getattr(old_value, "Docbook_ConfgroupType191", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_ConfgroupType191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ConfgroupType191"):
                opp_val = getattr(value, "Docbook_ConfgroupType191", None)
                setattr(value, "Docbook_ConfgroupType191", self)

class Docbook_PersonnameType:

    pass
class Docbook_AuthorType:

    def __init__(self, contrib: str, Docbook_AuthorType: "Docbook_PersonnameType" = None, Docbook_AuthorType7: "Docbook_AddressType" = None, Docbook_AuthorType41: "Docbook_DocumentRoot" = None, Docbook_AuthorType174: "Docbook_InfoType" = None):
        self.contrib = contrib
        self.Docbook_AuthorType = Docbook_AuthorType
        self.Docbook_AuthorType7 = Docbook_AuthorType7
        self.Docbook_AuthorType41 = Docbook_AuthorType41
        self.Docbook_AuthorType174 = Docbook_AuthorType174
        
    @property
    def contrib(self) -> str:
        return self.__contrib

    @contrib.setter
    def contrib(self, contrib: str):
        self.__contrib = contrib

    @property
    def Docbook_AuthorType(self):
        return self.__Docbook_AuthorType

    @Docbook_AuthorType.setter
    def Docbook_AuthorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AuthorType__Docbook_AuthorType", None)
        self.__Docbook_AuthorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PersonnameType"):
                opp_val = getattr(old_value, "Docbook_PersonnameType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PersonnameType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PersonnameType"):
                opp_val = getattr(value, "Docbook_PersonnameType", None)
                setattr(value, "Docbook_PersonnameType", self)

    @property
    def Docbook_AuthorType7(self):
        return self.__Docbook_AuthorType7

    @Docbook_AuthorType7.setter
    def Docbook_AuthorType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AuthorType__Docbook_AuthorType7", None)
        self.__Docbook_AuthorType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_AddressType8"):
                opp_val = getattr(old_value, "Docbook_AddressType8", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_AddressType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_AddressType8"):
                opp_val = getattr(value, "Docbook_AddressType8", None)
                setattr(value, "Docbook_AddressType8", self)

    @property
    def Docbook_AuthorType41(self):
        return self.__Docbook_AuthorType41

    @Docbook_AuthorType41.setter
    def Docbook_AuthorType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AuthorType__Docbook_AuthorType41", None)
        self.__Docbook_AuthorType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot40"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot40"):
                opp_val = getattr(value, "Docbook_DocumentRoot40", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_AuthorType174(self):
        return self.__Docbook_AuthorType174

    @Docbook_AuthorType174.setter
    def Docbook_AuthorType174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AuthorType__Docbook_AuthorType174", None)
        self.__Docbook_AuthorType174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_InfoType173"):
                opp_val = getattr(old_value, "Docbook_InfoType173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_InfoType173"):
                opp_val = getattr(value, "Docbook_InfoType173", None)
                if opp_val is None:
                    setattr(value, "Docbook_InfoType173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_AuthorinitialsType:

    def __init__(self, mixed: str, Docbook_AuthorinitialsType: "Docbook_RevisionType" = None):
        self.mixed = mixed
        self.Docbook_AuthorinitialsType = Docbook_AuthorinitialsType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_AuthorinitialsType(self):
        return self.__Docbook_AuthorinitialsType

    @Docbook_AuthorinitialsType.setter
    def Docbook_AuthorinitialsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AuthorinitialsType__Docbook_AuthorinitialsType", None)
        self.__Docbook_AuthorinitialsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevisionType328"):
                opp_val = getattr(old_value, "Docbook_RevisionType328", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_RevisionType328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevisionType328"):
                opp_val = getattr(value, "Docbook_RevisionType328", None)
                setattr(value, "Docbook_RevisionType328", self)

class Docbook_OtheraddrType:

    pass
class Docbook_ReplaceableType:

    def __init__(self, mixed: str, Docbook_ReplaceableType: "Docbook_ArgType" = None, Docbook_ReplaceableType136: "Docbook_EnvarType" = None, Docbook_ReplaceableType149: "Docbook_FileNameType" = None, Docbook_ReplaceableType230: "Docbook_OptionType" = None):
        self.mixed = mixed
        self.Docbook_ReplaceableType = Docbook_ReplaceableType
        self.Docbook_ReplaceableType136 = Docbook_ReplaceableType136
        self.Docbook_ReplaceableType149 = Docbook_ReplaceableType149
        self.Docbook_ReplaceableType230 = Docbook_ReplaceableType230
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_ReplaceableType149(self):
        return self.__Docbook_ReplaceableType149

    @Docbook_ReplaceableType149.setter
    def Docbook_ReplaceableType149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReplaceableType__Docbook_ReplaceableType149", None)
        self.__Docbook_ReplaceableType149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FileNameType"):
                opp_val = getattr(old_value, "Docbook_FileNameType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FileNameType"):
                opp_val = getattr(value, "Docbook_FileNameType", None)
                if opp_val is None:
                    setattr(value, "Docbook_FileNameType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ReplaceableType230(self):
        return self.__Docbook_ReplaceableType230

    @Docbook_ReplaceableType230.setter
    def Docbook_ReplaceableType230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReplaceableType__Docbook_ReplaceableType230", None)
        self.__Docbook_ReplaceableType230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_OptionType229"):
                opp_val = getattr(old_value, "Docbook_OptionType229", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_OptionType229"):
                opp_val = getattr(value, "Docbook_OptionType229", None)
                if opp_val is None:
                    setattr(value, "Docbook_OptionType229", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ReplaceableType(self):
        return self.__Docbook_ReplaceableType

    @Docbook_ReplaceableType.setter
    def Docbook_ReplaceableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReplaceableType__Docbook_ReplaceableType", None)
        self.__Docbook_ReplaceableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ArgType4"):
                opp_val = getattr(old_value, "Docbook_ArgType4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ArgType4"):
                opp_val = getattr(value, "Docbook_ArgType4", None)
                if opp_val is None:
                    setattr(value, "Docbook_ArgType4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ReplaceableType136(self):
        return self.__Docbook_ReplaceableType136

    @Docbook_ReplaceableType136.setter
    def Docbook_ReplaceableType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ReplaceableType__Docbook_ReplaceableType136", None)
        self.__Docbook_ReplaceableType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_EnvarType"):
                opp_val = getattr(old_value, "Docbook_EnvarType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_EnvarType"):
                opp_val = getattr(value, "Docbook_EnvarType", None)
                if opp_val is None:
                    setattr(value, "Docbook_EnvarType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_OptionType:

    def __init__(self, mixed: str, Docbook_OptionType: "Docbook_ArgType" = None, Docbook_OptionType229: set["Docbook_ReplaceableType"] = None, Docbook_OptionType403: "Docbook_TermType" = None):
        self.mixed = mixed
        self.Docbook_OptionType = Docbook_OptionType
        self.Docbook_OptionType229 = Docbook_OptionType229 if Docbook_OptionType229 is not None else set()
        self.Docbook_OptionType403 = Docbook_OptionType403
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_OptionType(self):
        return self.__Docbook_OptionType

    @Docbook_OptionType.setter
    def Docbook_OptionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OptionType__Docbook_OptionType", None)
        self.__Docbook_OptionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ArgType"):
                opp_val = getattr(old_value, "Docbook_ArgType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ArgType"):
                opp_val = getattr(value, "Docbook_ArgType", None)
                if opp_val is None:
                    setattr(value, "Docbook_ArgType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_OptionType229(self):
        return self.__Docbook_OptionType229

    @Docbook_OptionType229.setter
    def Docbook_OptionType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OptionType__Docbook_OptionType229", None)
        self.__Docbook_OptionType229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ReplaceableType230"):
                    opp_val = getattr(item, "Docbook_ReplaceableType230", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ReplaceableType230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ReplaceableType230"):
                    opp_val = getattr(item, "Docbook_ReplaceableType230", None)
                    
                    setattr(item, "Docbook_ReplaceableType230", self)
                    

    @property
    def Docbook_OptionType403(self):
        return self.__Docbook_OptionType403

    @Docbook_OptionType403.setter
    def Docbook_OptionType403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_OptionType__Docbook_OptionType403", None)
        self.__Docbook_OptionType403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_TermType402"):
                opp_val = getattr(old_value, "Docbook_TermType402", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_TermType402"):
                opp_val = getattr(value, "Docbook_TermType402", None)
                if opp_val is None:
                    setattr(value, "Docbook_TermType402", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Docbook_ArgType:

    def __init__(self, mixed: str, choice: str, rep: str, Docbook_ArgType: set["Docbook_OptionType"] = None, Docbook_ArgType4: set["Docbook_ReplaceableType"] = None, Docbook_ArgType28: "Docbook_CmdsynopsisType" = None):
        self.mixed = mixed
        self.choice = choice
        self.rep = rep
        self.Docbook_ArgType = Docbook_ArgType if Docbook_ArgType is not None else set()
        self.Docbook_ArgType4 = Docbook_ArgType4 if Docbook_ArgType4 is not None else set()
        self.Docbook_ArgType28 = Docbook_ArgType28
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def choice(self) -> str:
        return self.__choice

    @choice.setter
    def choice(self, choice: str):
        self.__choice = choice

    @property
    def rep(self) -> str:
        return self.__rep

    @rep.setter
    def rep(self, rep: str):
        self.__rep = rep

    @property
    def Docbook_ArgType28(self):
        return self.__Docbook_ArgType28

    @Docbook_ArgType28.setter
    def Docbook_ArgType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ArgType__Docbook_ArgType28", None)
        self.__Docbook_ArgType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_CmdsynopsisType27"):
                opp_val = getattr(old_value, "Docbook_CmdsynopsisType27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_CmdsynopsisType27"):
                opp_val = getattr(value, "Docbook_CmdsynopsisType27", None)
                if opp_val is None:
                    setattr(value, "Docbook_CmdsynopsisType27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ArgType(self):
        return self.__Docbook_ArgType

    @Docbook_ArgType.setter
    def Docbook_ArgType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ArgType__Docbook_ArgType", None)
        self.__Docbook_ArgType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_OptionType"):
                    opp_val = getattr(item, "Docbook_OptionType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_OptionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_OptionType"):
                    opp_val = getattr(item, "Docbook_OptionType", None)
                    
                    setattr(item, "Docbook_OptionType", self)
                    

    @property
    def Docbook_ArgType4(self):
        return self.__Docbook_ArgType4

    @Docbook_ArgType4.setter
    def Docbook_ArgType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ArgType__Docbook_ArgType4", None)
        self.__Docbook_ArgType4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ReplaceableType"):
                    opp_val = getattr(item, "Docbook_ReplaceableType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ReplaceableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ReplaceableType"):
                    opp_val = getattr(item, "Docbook_ReplaceableType", None)
                    
                    setattr(item, "Docbook_ReplaceableType", self)
                    

class Docbook_AddressType:

    def __init__(self, state: str, email: str, format: str, Docbook_AddressType: "Docbook_OtheraddrType" = None, Docbook_AddressType8: "Docbook_AuthorType" = None, Docbook_AddressType38: "Docbook_DocumentRoot" = None, Docbook_AddressType280: "Docbook_PublisherType" = None):
        self.state = state
        self.email = email
        self.format = format
        self.Docbook_AddressType = Docbook_AddressType
        self.Docbook_AddressType8 = Docbook_AddressType8
        self.Docbook_AddressType38 = Docbook_AddressType38
        self.Docbook_AddressType280 = Docbook_AddressType280
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def Docbook_AddressType280(self):
        return self.__Docbook_AddressType280

    @Docbook_AddressType280.setter
    def Docbook_AddressType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AddressType__Docbook_AddressType280", None)
        self.__Docbook_AddressType280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PublisherType279"):
                opp_val = getattr(old_value, "Docbook_PublisherType279", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_PublisherType279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PublisherType279"):
                opp_val = getattr(value, "Docbook_PublisherType279", None)
                setattr(value, "Docbook_PublisherType279", self)

    @property
    def Docbook_AddressType(self):
        return self.__Docbook_AddressType

    @Docbook_AddressType.setter
    def Docbook_AddressType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AddressType__Docbook_AddressType", None)
        self.__Docbook_AddressType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_OtheraddrType"):
                opp_val = getattr(old_value, "Docbook_OtheraddrType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_OtheraddrType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_OtheraddrType"):
                opp_val = getattr(value, "Docbook_OtheraddrType", None)
                setattr(value, "Docbook_OtheraddrType", self)

    @property
    def Docbook_AddressType38(self):
        return self.__Docbook_AddressType38

    @Docbook_AddressType38.setter
    def Docbook_AddressType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AddressType__Docbook_AddressType38", None)
        self.__Docbook_AddressType38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot37"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot37"):
                opp_val = getattr(value, "Docbook_DocumentRoot37", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_AddressType8(self):
        return self.__Docbook_AddressType8

    @Docbook_AddressType8.setter
    def Docbook_AddressType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_AddressType__Docbook_AddressType8", None)
        self.__Docbook_AddressType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_AuthorType7"):
                opp_val = getattr(old_value, "Docbook_AuthorType7", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_AuthorType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_AuthorType7"):
                opp_val = getattr(value, "Docbook_AuthorType7", None)
                setattr(value, "Docbook_AuthorType7", self)

class Docbook_ParaType:

    def __init__(self, mixed: str, group: str, role: str, id: str, Docbook_ParaType: "Docbook_AbstractType" = None, Docbook_ParaType20: "Docbook_ChapterType" = None, Docbook_ParaType93: "Docbook_DocumentRoot" = None, Docbook_ParaType134: "Docbook_EntryType" = None, Docbook_ParaType152: "Docbook_FootnoteType" = None, Docbook_ParaType209: "Docbook_LegalNoticeType" = None, Docbook_ParaType215: "Docbook_ListitemType" = None, Docbook_ParaType237: set["Docbook_EmphasisType"] = None, Docbook_ParaType240: set["Docbook_LiteralType"] = None, Docbook_ParaType249: set["Docbook_LinkType"] = None, Docbook_ParaType243: set["Docbook_UlinkType"] = None, Docbook_ParaType246: set["Docbook_FootnoteType"] = None, Docbook_ParaType252: set["Docbook_ItemizedlistType"] = None, Docbook_ParaType255: set["Docbook_VariableListType"] = None, Docbook_ParaType265: "Docbook_PrefaceType" = None, Docbook_ParaType307: "Docbook_RefSect1Type" = None, Docbook_ParaType320: "Docbook_RevdescriptionType" = None, Docbook_ParaType349: "Docbook_SectionType" = None):
        self.mixed = mixed
        self.group = group
        self.role = role
        self.id = id
        self.Docbook_ParaType = Docbook_ParaType
        self.Docbook_ParaType20 = Docbook_ParaType20
        self.Docbook_ParaType93 = Docbook_ParaType93
        self.Docbook_ParaType134 = Docbook_ParaType134
        self.Docbook_ParaType152 = Docbook_ParaType152
        self.Docbook_ParaType209 = Docbook_ParaType209
        self.Docbook_ParaType215 = Docbook_ParaType215
        self.Docbook_ParaType237 = Docbook_ParaType237 if Docbook_ParaType237 is not None else set()
        self.Docbook_ParaType240 = Docbook_ParaType240 if Docbook_ParaType240 is not None else set()
        self.Docbook_ParaType249 = Docbook_ParaType249 if Docbook_ParaType249 is not None else set()
        self.Docbook_ParaType243 = Docbook_ParaType243 if Docbook_ParaType243 is not None else set()
        self.Docbook_ParaType246 = Docbook_ParaType246 if Docbook_ParaType246 is not None else set()
        self.Docbook_ParaType252 = Docbook_ParaType252 if Docbook_ParaType252 is not None else set()
        self.Docbook_ParaType255 = Docbook_ParaType255 if Docbook_ParaType255 is not None else set()
        self.Docbook_ParaType265 = Docbook_ParaType265
        self.Docbook_ParaType307 = Docbook_ParaType307
        self.Docbook_ParaType320 = Docbook_ParaType320
        self.Docbook_ParaType349 = Docbook_ParaType349
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Docbook_ParaType134(self):
        return self.__Docbook_ParaType134

    @Docbook_ParaType134.setter
    def Docbook_ParaType134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType134", None)
        self.__Docbook_ParaType134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_EntryType133"):
                opp_val = getattr(old_value, "Docbook_EntryType133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_EntryType133"):
                opp_val = getattr(value, "Docbook_EntryType133", None)
                if opp_val is None:
                    setattr(value, "Docbook_EntryType133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType243(self):
        return self.__Docbook_ParaType243

    @Docbook_ParaType243.setter
    def Docbook_ParaType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType243", None)
        self.__Docbook_ParaType243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_UlinkType244"):
                    opp_val = getattr(item, "Docbook_UlinkType244", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_UlinkType244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_UlinkType244"):
                    opp_val = getattr(item, "Docbook_UlinkType244", None)
                    
                    setattr(item, "Docbook_UlinkType244", self)
                    

    @property
    def Docbook_ParaType209(self):
        return self.__Docbook_ParaType209

    @Docbook_ParaType209.setter
    def Docbook_ParaType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType209", None)
        self.__Docbook_ParaType209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_LegalNoticeType208"):
                opp_val = getattr(old_value, "Docbook_LegalNoticeType208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_LegalNoticeType208"):
                opp_val = getattr(value, "Docbook_LegalNoticeType208", None)
                if opp_val is None:
                    setattr(value, "Docbook_LegalNoticeType208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType252(self):
        return self.__Docbook_ParaType252

    @Docbook_ParaType252.setter
    def Docbook_ParaType252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType252", None)
        self.__Docbook_ParaType252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_ItemizedlistType253"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType253", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_ItemizedlistType253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_ItemizedlistType253"):
                    opp_val = getattr(item, "Docbook_ItemizedlistType253", None)
                    
                    setattr(item, "Docbook_ItemizedlistType253", self)
                    

    @property
    def Docbook_ParaType349(self):
        return self.__Docbook_ParaType349

    @Docbook_ParaType349.setter
    def Docbook_ParaType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType349", None)
        self.__Docbook_ParaType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_SectionType348"):
                opp_val = getattr(old_value, "Docbook_SectionType348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_SectionType348"):
                opp_val = getattr(value, "Docbook_SectionType348", None)
                if opp_val is None:
                    setattr(value, "Docbook_SectionType348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType249(self):
        return self.__Docbook_ParaType249

    @Docbook_ParaType249.setter
    def Docbook_ParaType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType249", None)
        self.__Docbook_ParaType249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_LinkType250"):
                    opp_val = getattr(item, "Docbook_LinkType250", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_LinkType250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_LinkType250"):
                    opp_val = getattr(item, "Docbook_LinkType250", None)
                    
                    setattr(item, "Docbook_LinkType250", self)
                    

    @property
    def Docbook_ParaType152(self):
        return self.__Docbook_ParaType152

    @Docbook_ParaType152.setter
    def Docbook_ParaType152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType152", None)
        self.__Docbook_ParaType152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_FootnoteType151"):
                opp_val = getattr(old_value, "Docbook_FootnoteType151", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_FootnoteType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_FootnoteType151"):
                opp_val = getattr(value, "Docbook_FootnoteType151", None)
                setattr(value, "Docbook_FootnoteType151", self)

    @property
    def Docbook_ParaType265(self):
        return self.__Docbook_ParaType265

    @Docbook_ParaType265.setter
    def Docbook_ParaType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType265", None)
        self.__Docbook_ParaType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_PrefaceType264"):
                opp_val = getattr(old_value, "Docbook_PrefaceType264", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_PrefaceType264"):
                opp_val = getattr(value, "Docbook_PrefaceType264", None)
                if opp_val is None:
                    setattr(value, "Docbook_PrefaceType264", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType320(self):
        return self.__Docbook_ParaType320

    @Docbook_ParaType320.setter
    def Docbook_ParaType320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType320", None)
        self.__Docbook_ParaType320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RevdescriptionType"):
                opp_val = getattr(old_value, "Docbook_RevdescriptionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RevdescriptionType"):
                opp_val = getattr(value, "Docbook_RevdescriptionType", None)
                if opp_val is None:
                    setattr(value, "Docbook_RevdescriptionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType(self):
        return self.__Docbook_ParaType

    @Docbook_ParaType.setter
    def Docbook_ParaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType", None)
        self.__Docbook_ParaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_AbstractType"):
                opp_val = getattr(old_value, "Docbook_AbstractType", None)
                if opp_val == self:
                    setattr(old_value, "Docbook_AbstractType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_AbstractType"):
                opp_val = getattr(value, "Docbook_AbstractType", None)
                setattr(value, "Docbook_AbstractType", self)

    @property
    def Docbook_ParaType20(self):
        return self.__Docbook_ParaType20

    @Docbook_ParaType20.setter
    def Docbook_ParaType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType20", None)
        self.__Docbook_ParaType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ChapterType19"):
                opp_val = getattr(old_value, "Docbook_ChapterType19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ChapterType19"):
                opp_val = getattr(value, "Docbook_ChapterType19", None)
                if opp_val is None:
                    setattr(value, "Docbook_ChapterType19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType237(self):
        return self.__Docbook_ParaType237

    @Docbook_ParaType237.setter
    def Docbook_ParaType237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType237", None)
        self.__Docbook_ParaType237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_EmphasisType238"):
                    opp_val = getattr(item, "Docbook_EmphasisType238", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_EmphasisType238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_EmphasisType238"):
                    opp_val = getattr(item, "Docbook_EmphasisType238", None)
                    
                    setattr(item, "Docbook_EmphasisType238", self)
                    

    @property
    def Docbook_ParaType307(self):
        return self.__Docbook_ParaType307

    @Docbook_ParaType307.setter
    def Docbook_ParaType307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType307", None)
        self.__Docbook_ParaType307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_RefSect1Type306"):
                opp_val = getattr(old_value, "Docbook_RefSect1Type306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_RefSect1Type306"):
                opp_val = getattr(value, "Docbook_RefSect1Type306", None)
                if opp_val is None:
                    setattr(value, "Docbook_RefSect1Type306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType240(self):
        return self.__Docbook_ParaType240

    @Docbook_ParaType240.setter
    def Docbook_ParaType240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType240", None)
        self.__Docbook_ParaType240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_LiteralType241"):
                    opp_val = getattr(item, "Docbook_LiteralType241", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_LiteralType241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_LiteralType241"):
                    opp_val = getattr(item, "Docbook_LiteralType241", None)
                    
                    setattr(item, "Docbook_LiteralType241", self)
                    

    @property
    def Docbook_ParaType215(self):
        return self.__Docbook_ParaType215

    @Docbook_ParaType215.setter
    def Docbook_ParaType215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType215", None)
        self.__Docbook_ParaType215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_ListitemType214"):
                opp_val = getattr(old_value, "Docbook_ListitemType214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_ListitemType214"):
                opp_val = getattr(value, "Docbook_ListitemType214", None)
                if opp_val is None:
                    setattr(value, "Docbook_ListitemType214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType93(self):
        return self.__Docbook_ParaType93

    @Docbook_ParaType93.setter
    def Docbook_ParaType93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType93", None)
        self.__Docbook_ParaType93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Docbook_DocumentRoot92"):
                opp_val = getattr(old_value, "Docbook_DocumentRoot92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Docbook_DocumentRoot92"):
                opp_val = getattr(value, "Docbook_DocumentRoot92", None)
                if opp_val is None:
                    setattr(value, "Docbook_DocumentRoot92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Docbook_ParaType246(self):
        return self.__Docbook_ParaType246

    @Docbook_ParaType246.setter
    def Docbook_ParaType246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType246", None)
        self.__Docbook_ParaType246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_FootnoteType247"):
                    opp_val = getattr(item, "Docbook_FootnoteType247", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_FootnoteType247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_FootnoteType247"):
                    opp_val = getattr(item, "Docbook_FootnoteType247", None)
                    
                    setattr(item, "Docbook_FootnoteType247", self)
                    

    @property
    def Docbook_ParaType255(self):
        return self.__Docbook_ParaType255

    @Docbook_ParaType255.setter
    def Docbook_ParaType255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docbook_ParaType__Docbook_ParaType255", None)
        self.__Docbook_ParaType255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Docbook_VariableListType"):
                    opp_val = getattr(item, "Docbook_VariableListType", None)
                    
                    if opp_val == self:
                        setattr(item, "Docbook_VariableListType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Docbook_VariableListType"):
                    opp_val = getattr(item, "Docbook_VariableListType", None)
                    
                    setattr(item, "Docbook_VariableListType", self)
                    

class Docbook_AbstractType:

    pass