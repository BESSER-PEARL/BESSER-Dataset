from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Shape(Enum):
    rect = "rect"
    circle = "circle"
    poly = "poly"
    default = "default"
class TRules(Enum):
    none = "none"
    groups = "groups"
    rows = "rows"
    all = "all"
    cols = "cols"
class NohrefType(Enum):
    nohref = "nohref"
class ValignType(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"
    baseline = "baseline"
class IsmapType(Enum):
    ismap = "ismap"
class DirType1(Enum):
    rtl = "rtl"
    ltr = "ltr"
class Scope(Enum):
    row = "row"
    col = "col"
    rowgroup = "rowgroup"
    colgroup = "colgroup"
class TFrame(Enum):
    void = "void"
    above = "above"
    below = "below"
    hsides = "hsides"
    lhs = "lhs"
    rhs = "rhs"
    vsides = "vsides"
    box = "box"
    border = "border"
class DirType(Enum):
    ltr = "ltr"
    rtl = "rtl"
class AlignType(Enum):
    left = "left"
    center = "center"
    right = "right"
    justify = "justify"
    char = "char"


############################################
# Definition of Classes
############################################

class PreContent:

    pass
class xhtml_PreContent:

    def __init__(self, mixed: str, group: str, xhtml_PreContent481: set["xhtml_TtType"] = None, xhtml_PreContent484: set["xhtml_IType"] = None, xhtml_PreContent487: set["xhtml_BType"] = None, xhtml_PreContent490: set["xhtml_BigType"] = None, xhtml_PreContent493: set["xhtml_SmallType"] = None, xhtml_PreContent496: set["xhtml_EmType"] = None, xhtml_PreContent499: set["xhtml_StrongType"] = None, xhtml_PreContent502: set["xhtml_DfnType"] = None, xhtml_PreContent: set["xhtml_AType"] = None, xhtml_PreContent508: set["xhtml_QType"] = None, xhtml_PreContent511: set["xhtml_SampType"] = None, xhtml_PreContent514: set["xhtml_KbdType"] = None, xhtml_PreContent517: set["xhtml_VarType"] = None, xhtml_PreContent520: set["xhtml_CiteType"] = None, xhtml_PreContent523: set["xhtml_AbbrType"] = None, xhtml_PreContent526: set["xhtml_AcronymType"] = None, xhtml_PreContent529: set["xhtml_SubType"] = None, xhtml_PreContent505: set["xhtml_CodeType"] = None, xhtml_PreContent535: set["xhtml_BrType"] = None, xhtml_PreContent538: set["xhtml_SpanType"] = None, xhtml_PreContent541: set["xhtml_BdoType"] = None, xhtml_PreContent544: set["xhtml_MapType"] = None, xhtml_PreContent532: set["xhtml_SupType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_PreContent481 = xhtml_PreContent481 if xhtml_PreContent481 is not None else set()
        self.xhtml_PreContent484 = xhtml_PreContent484 if xhtml_PreContent484 is not None else set()
        self.xhtml_PreContent487 = xhtml_PreContent487 if xhtml_PreContent487 is not None else set()
        self.xhtml_PreContent490 = xhtml_PreContent490 if xhtml_PreContent490 is not None else set()
        self.xhtml_PreContent493 = xhtml_PreContent493 if xhtml_PreContent493 is not None else set()
        self.xhtml_PreContent496 = xhtml_PreContent496 if xhtml_PreContent496 is not None else set()
        self.xhtml_PreContent499 = xhtml_PreContent499 if xhtml_PreContent499 is not None else set()
        self.xhtml_PreContent502 = xhtml_PreContent502 if xhtml_PreContent502 is not None else set()
        self.xhtml_PreContent = xhtml_PreContent if xhtml_PreContent is not None else set()
        self.xhtml_PreContent508 = xhtml_PreContent508 if xhtml_PreContent508 is not None else set()
        self.xhtml_PreContent511 = xhtml_PreContent511 if xhtml_PreContent511 is not None else set()
        self.xhtml_PreContent514 = xhtml_PreContent514 if xhtml_PreContent514 is not None else set()
        self.xhtml_PreContent517 = xhtml_PreContent517 if xhtml_PreContent517 is not None else set()
        self.xhtml_PreContent520 = xhtml_PreContent520 if xhtml_PreContent520 is not None else set()
        self.xhtml_PreContent523 = xhtml_PreContent523 if xhtml_PreContent523 is not None else set()
        self.xhtml_PreContent526 = xhtml_PreContent526 if xhtml_PreContent526 is not None else set()
        self.xhtml_PreContent529 = xhtml_PreContent529 if xhtml_PreContent529 is not None else set()
        self.xhtml_PreContent505 = xhtml_PreContent505 if xhtml_PreContent505 is not None else set()
        self.xhtml_PreContent535 = xhtml_PreContent535 if xhtml_PreContent535 is not None else set()
        self.xhtml_PreContent538 = xhtml_PreContent538 if xhtml_PreContent538 is not None else set()
        self.xhtml_PreContent541 = xhtml_PreContent541 if xhtml_PreContent541 is not None else set()
        self.xhtml_PreContent544 = xhtml_PreContent544 if xhtml_PreContent544 is not None else set()
        self.xhtml_PreContent532 = xhtml_PreContent532 if xhtml_PreContent532 is not None else set()
        
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
    def xhtml_PreContent529(self):
        return self.__xhtml_PreContent529

    @xhtml_PreContent529.setter
    def xhtml_PreContent529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent529", None)
        self.__xhtml_PreContent529 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType530"):
                    opp_val = getattr(item, "xhtml_SubType530", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType530", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType530"):
                    opp_val = getattr(item, "xhtml_SubType530", None)
                    
                    setattr(item, "xhtml_SubType530", self)
                    

    @property
    def xhtml_PreContent511(self):
        return self.__xhtml_PreContent511

    @xhtml_PreContent511.setter
    def xhtml_PreContent511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent511", None)
        self.__xhtml_PreContent511 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType512"):
                    opp_val = getattr(item, "xhtml_SampType512", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType512", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType512"):
                    opp_val = getattr(item, "xhtml_SampType512", None)
                    
                    setattr(item, "xhtml_SampType512", self)
                    

    @property
    def xhtml_PreContent(self):
        return self.__xhtml_PreContent

    @xhtml_PreContent.setter
    def xhtml_PreContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent", None)
        self.__xhtml_PreContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType479"):
                    opp_val = getattr(item, "xhtml_AType479", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType479", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType479"):
                    opp_val = getattr(item, "xhtml_AType479", None)
                    
                    setattr(item, "xhtml_AType479", self)
                    

    @property
    def xhtml_PreContent526(self):
        return self.__xhtml_PreContent526

    @xhtml_PreContent526.setter
    def xhtml_PreContent526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent526", None)
        self.__xhtml_PreContent526 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType527"):
                    opp_val = getattr(item, "xhtml_AcronymType527", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType527", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType527"):
                    opp_val = getattr(item, "xhtml_AcronymType527", None)
                    
                    setattr(item, "xhtml_AcronymType527", self)
                    

    @property
    def xhtml_PreContent487(self):
        return self.__xhtml_PreContent487

    @xhtml_PreContent487.setter
    def xhtml_PreContent487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent487", None)
        self.__xhtml_PreContent487 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType488"):
                    opp_val = getattr(item, "xhtml_BType488", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType488", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType488"):
                    opp_val = getattr(item, "xhtml_BType488", None)
                    
                    setattr(item, "xhtml_BType488", self)
                    

    @property
    def xhtml_PreContent514(self):
        return self.__xhtml_PreContent514

    @xhtml_PreContent514.setter
    def xhtml_PreContent514(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent514", None)
        self.__xhtml_PreContent514 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType515"):
                    opp_val = getattr(item, "xhtml_KbdType515", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType515", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType515"):
                    opp_val = getattr(item, "xhtml_KbdType515", None)
                    
                    setattr(item, "xhtml_KbdType515", self)
                    

    @property
    def xhtml_PreContent520(self):
        return self.__xhtml_PreContent520

    @xhtml_PreContent520.setter
    def xhtml_PreContent520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent520", None)
        self.__xhtml_PreContent520 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType521"):
                    opp_val = getattr(item, "xhtml_CiteType521", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType521", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType521"):
                    opp_val = getattr(item, "xhtml_CiteType521", None)
                    
                    setattr(item, "xhtml_CiteType521", self)
                    

    @property
    def xhtml_PreContent502(self):
        return self.__xhtml_PreContent502

    @xhtml_PreContent502.setter
    def xhtml_PreContent502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent502", None)
        self.__xhtml_PreContent502 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType503"):
                    opp_val = getattr(item, "xhtml_DfnType503", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType503", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType503"):
                    opp_val = getattr(item, "xhtml_DfnType503", None)
                    
                    setattr(item, "xhtml_DfnType503", self)
                    

    @property
    def xhtml_PreContent523(self):
        return self.__xhtml_PreContent523

    @xhtml_PreContent523.setter
    def xhtml_PreContent523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent523", None)
        self.__xhtml_PreContent523 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType524"):
                    opp_val = getattr(item, "xhtml_AbbrType524", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType524", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType524"):
                    opp_val = getattr(item, "xhtml_AbbrType524", None)
                    
                    setattr(item, "xhtml_AbbrType524", self)
                    

    @property
    def xhtml_PreContent538(self):
        return self.__xhtml_PreContent538

    @xhtml_PreContent538.setter
    def xhtml_PreContent538(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent538", None)
        self.__xhtml_PreContent538 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType539"):
                    opp_val = getattr(item, "xhtml_SpanType539", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType539", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType539"):
                    opp_val = getattr(item, "xhtml_SpanType539", None)
                    
                    setattr(item, "xhtml_SpanType539", self)
                    

    @property
    def xhtml_PreContent541(self):
        return self.__xhtml_PreContent541

    @xhtml_PreContent541.setter
    def xhtml_PreContent541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent541", None)
        self.__xhtml_PreContent541 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BdoType542"):
                    opp_val = getattr(item, "xhtml_BdoType542", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BdoType542", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BdoType542"):
                    opp_val = getattr(item, "xhtml_BdoType542", None)
                    
                    setattr(item, "xhtml_BdoType542", self)
                    

    @property
    def xhtml_PreContent496(self):
        return self.__xhtml_PreContent496

    @xhtml_PreContent496.setter
    def xhtml_PreContent496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent496", None)
        self.__xhtml_PreContent496 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType497"):
                    opp_val = getattr(item, "xhtml_EmType497", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType497", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType497"):
                    opp_val = getattr(item, "xhtml_EmType497", None)
                    
                    setattr(item, "xhtml_EmType497", self)
                    

    @property
    def xhtml_PreContent535(self):
        return self.__xhtml_PreContent535

    @xhtml_PreContent535.setter
    def xhtml_PreContent535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent535", None)
        self.__xhtml_PreContent535 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType536"):
                    opp_val = getattr(item, "xhtml_BrType536", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType536", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType536"):
                    opp_val = getattr(item, "xhtml_BrType536", None)
                    
                    setattr(item, "xhtml_BrType536", self)
                    

    @property
    def xhtml_PreContent484(self):
        return self.__xhtml_PreContent484

    @xhtml_PreContent484.setter
    def xhtml_PreContent484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent484", None)
        self.__xhtml_PreContent484 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType485"):
                    opp_val = getattr(item, "xhtml_IType485", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType485", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType485"):
                    opp_val = getattr(item, "xhtml_IType485", None)
                    
                    setattr(item, "xhtml_IType485", self)
                    

    @property
    def xhtml_PreContent493(self):
        return self.__xhtml_PreContent493

    @xhtml_PreContent493.setter
    def xhtml_PreContent493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent493", None)
        self.__xhtml_PreContent493 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType494"):
                    opp_val = getattr(item, "xhtml_SmallType494", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType494", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType494"):
                    opp_val = getattr(item, "xhtml_SmallType494", None)
                    
                    setattr(item, "xhtml_SmallType494", self)
                    

    @property
    def xhtml_PreContent505(self):
        return self.__xhtml_PreContent505

    @xhtml_PreContent505.setter
    def xhtml_PreContent505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent505", None)
        self.__xhtml_PreContent505 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType506"):
                    opp_val = getattr(item, "xhtml_CodeType506", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType506", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType506"):
                    opp_val = getattr(item, "xhtml_CodeType506", None)
                    
                    setattr(item, "xhtml_CodeType506", self)
                    

    @property
    def xhtml_PreContent544(self):
        return self.__xhtml_PreContent544

    @xhtml_PreContent544.setter
    def xhtml_PreContent544(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent544", None)
        self.__xhtml_PreContent544 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_MapType545"):
                    opp_val = getattr(item, "xhtml_MapType545", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_MapType545", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_MapType545"):
                    opp_val = getattr(item, "xhtml_MapType545", None)
                    
                    setattr(item, "xhtml_MapType545", self)
                    

    @property
    def xhtml_PreContent532(self):
        return self.__xhtml_PreContent532

    @xhtml_PreContent532.setter
    def xhtml_PreContent532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent532", None)
        self.__xhtml_PreContent532 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType533"):
                    opp_val = getattr(item, "xhtml_SupType533", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType533", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType533"):
                    opp_val = getattr(item, "xhtml_SupType533", None)
                    
                    setattr(item, "xhtml_SupType533", self)
                    

    @property
    def xhtml_PreContent481(self):
        return self.__xhtml_PreContent481

    @xhtml_PreContent481.setter
    def xhtml_PreContent481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent481", None)
        self.__xhtml_PreContent481 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType482"):
                    opp_val = getattr(item, "xhtml_TtType482", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType482", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType482"):
                    opp_val = getattr(item, "xhtml_TtType482", None)
                    
                    setattr(item, "xhtml_TtType482", self)
                    

    @property
    def xhtml_PreContent490(self):
        return self.__xhtml_PreContent490

    @xhtml_PreContent490.setter
    def xhtml_PreContent490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent490", None)
        self.__xhtml_PreContent490 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType491"):
                    opp_val = getattr(item, "xhtml_BigType491", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType491", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType491"):
                    opp_val = getattr(item, "xhtml_BigType491", None)
                    
                    setattr(item, "xhtml_BigType491", self)
                    

    @property
    def xhtml_PreContent499(self):
        return self.__xhtml_PreContent499

    @xhtml_PreContent499.setter
    def xhtml_PreContent499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent499", None)
        self.__xhtml_PreContent499 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType500"):
                    opp_val = getattr(item, "xhtml_StrongType500", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType500", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType500"):
                    opp_val = getattr(item, "xhtml_StrongType500", None)
                    
                    setattr(item, "xhtml_StrongType500", self)
                    

    @property
    def xhtml_PreContent508(self):
        return self.__xhtml_PreContent508

    @xhtml_PreContent508.setter
    def xhtml_PreContent508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent508", None)
        self.__xhtml_PreContent508 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType509"):
                    opp_val = getattr(item, "xhtml_QType509", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType509", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType509"):
                    opp_val = getattr(item, "xhtml_QType509", None)
                    
                    setattr(item, "xhtml_QType509", self)
                    

    @property
    def xhtml_PreContent517(self):
        return self.__xhtml_PreContent517

    @xhtml_PreContent517.setter
    def xhtml_PreContent517(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent517", None)
        self.__xhtml_PreContent517 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType518"):
                    opp_val = getattr(item, "xhtml_VarType518", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType518", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType518"):
                    opp_val = getattr(item, "xhtml_VarType518", None)
                    
                    setattr(item, "xhtml_VarType518", self)
                    

class xhtml_Inline:

    def __init__(self, mixed: str, inline: str, xhtml_Inline: set["xhtml_AType"] = None, xhtml_Inline356: set["xhtml_BrType"] = None, xhtml_Inline368: set["xhtml_ImgType"] = None, xhtml_Inline371: set["xhtml_TtType"] = None, xhtml_Inline374: set["xhtml_IType"] = None, xhtml_Inline377: set["xhtml_BType"] = None, xhtml_Inline359: set["xhtml_SpanType"] = None, xhtml_Inline362: set["xhtml_BdoType"] = None, xhtml_Inline365: set["xhtml_MapType"] = None, xhtml_Inline392: set["xhtml_DfnType"] = None, xhtml_Inline380: set["xhtml_BigType"] = None, xhtml_Inline395: set["xhtml_CodeType"] = None, xhtml_Inline383: set["xhtml_SmallType"] = None, xhtml_Inline398: set["xhtml_QType"] = None, xhtml_Inline386: set["xhtml_EmType"] = None, xhtml_Inline401: set["xhtml_SampType"] = None, xhtml_Inline389: set["xhtml_StrongType"] = None, xhtml_Inline404: set["xhtml_KbdType"] = None, xhtml_Inline407: set["xhtml_VarType"] = None, xhtml_Inline410: set["xhtml_CiteType"] = None, xhtml_Inline413: set["xhtml_AbbrType"] = None, xhtml_Inline416: set["xhtml_AcronymType"] = None, xhtml_Inline419: set["xhtml_SubType"] = None, xhtml_Inline422: set["xhtml_SupType"] = None):
        self.mixed = mixed
        self.inline = inline
        self.xhtml_Inline = xhtml_Inline if xhtml_Inline is not None else set()
        self.xhtml_Inline356 = xhtml_Inline356 if xhtml_Inline356 is not None else set()
        self.xhtml_Inline368 = xhtml_Inline368 if xhtml_Inline368 is not None else set()
        self.xhtml_Inline371 = xhtml_Inline371 if xhtml_Inline371 is not None else set()
        self.xhtml_Inline374 = xhtml_Inline374 if xhtml_Inline374 is not None else set()
        self.xhtml_Inline377 = xhtml_Inline377 if xhtml_Inline377 is not None else set()
        self.xhtml_Inline359 = xhtml_Inline359 if xhtml_Inline359 is not None else set()
        self.xhtml_Inline362 = xhtml_Inline362 if xhtml_Inline362 is not None else set()
        self.xhtml_Inline365 = xhtml_Inline365 if xhtml_Inline365 is not None else set()
        self.xhtml_Inline392 = xhtml_Inline392 if xhtml_Inline392 is not None else set()
        self.xhtml_Inline380 = xhtml_Inline380 if xhtml_Inline380 is not None else set()
        self.xhtml_Inline395 = xhtml_Inline395 if xhtml_Inline395 is not None else set()
        self.xhtml_Inline383 = xhtml_Inline383 if xhtml_Inline383 is not None else set()
        self.xhtml_Inline398 = xhtml_Inline398 if xhtml_Inline398 is not None else set()
        self.xhtml_Inline386 = xhtml_Inline386 if xhtml_Inline386 is not None else set()
        self.xhtml_Inline401 = xhtml_Inline401 if xhtml_Inline401 is not None else set()
        self.xhtml_Inline389 = xhtml_Inline389 if xhtml_Inline389 is not None else set()
        self.xhtml_Inline404 = xhtml_Inline404 if xhtml_Inline404 is not None else set()
        self.xhtml_Inline407 = xhtml_Inline407 if xhtml_Inline407 is not None else set()
        self.xhtml_Inline410 = xhtml_Inline410 if xhtml_Inline410 is not None else set()
        self.xhtml_Inline413 = xhtml_Inline413 if xhtml_Inline413 is not None else set()
        self.xhtml_Inline416 = xhtml_Inline416 if xhtml_Inline416 is not None else set()
        self.xhtml_Inline419 = xhtml_Inline419 if xhtml_Inline419 is not None else set()
        self.xhtml_Inline422 = xhtml_Inline422 if xhtml_Inline422 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def inline(self) -> str:
        return self.__inline

    @inline.setter
    def inline(self, inline: str):
        self.__inline = inline

    @property
    def xhtml_Inline401(self):
        return self.__xhtml_Inline401

    @xhtml_Inline401.setter
    def xhtml_Inline401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline401", None)
        self.__xhtml_Inline401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType402"):
                    opp_val = getattr(item, "xhtml_SampType402", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType402"):
                    opp_val = getattr(item, "xhtml_SampType402", None)
                    
                    setattr(item, "xhtml_SampType402", self)
                    

    @property
    def xhtml_Inline386(self):
        return self.__xhtml_Inline386

    @xhtml_Inline386.setter
    def xhtml_Inline386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline386", None)
        self.__xhtml_Inline386 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType387"):
                    opp_val = getattr(item, "xhtml_EmType387", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType387", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType387"):
                    opp_val = getattr(item, "xhtml_EmType387", None)
                    
                    setattr(item, "xhtml_EmType387", self)
                    

    @property
    def xhtml_Inline383(self):
        return self.__xhtml_Inline383

    @xhtml_Inline383.setter
    def xhtml_Inline383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline383", None)
        self.__xhtml_Inline383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType384"):
                    opp_val = getattr(item, "xhtml_SmallType384", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType384"):
                    opp_val = getattr(item, "xhtml_SmallType384", None)
                    
                    setattr(item, "xhtml_SmallType384", self)
                    

    @property
    def xhtml_Inline395(self):
        return self.__xhtml_Inline395

    @xhtml_Inline395.setter
    def xhtml_Inline395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline395", None)
        self.__xhtml_Inline395 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType396"):
                    opp_val = getattr(item, "xhtml_CodeType396", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType396", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType396"):
                    opp_val = getattr(item, "xhtml_CodeType396", None)
                    
                    setattr(item, "xhtml_CodeType396", self)
                    

    @property
    def xhtml_Inline371(self):
        return self.__xhtml_Inline371

    @xhtml_Inline371.setter
    def xhtml_Inline371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline371", None)
        self.__xhtml_Inline371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType372"):
                    opp_val = getattr(item, "xhtml_TtType372", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType372"):
                    opp_val = getattr(item, "xhtml_TtType372", None)
                    
                    setattr(item, "xhtml_TtType372", self)
                    

    @property
    def xhtml_Inline362(self):
        return self.__xhtml_Inline362

    @xhtml_Inline362.setter
    def xhtml_Inline362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline362", None)
        self.__xhtml_Inline362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BdoType363"):
                    opp_val = getattr(item, "xhtml_BdoType363", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BdoType363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BdoType363"):
                    opp_val = getattr(item, "xhtml_BdoType363", None)
                    
                    setattr(item, "xhtml_BdoType363", self)
                    

    @property
    def xhtml_Inline(self):
        return self.__xhtml_Inline

    @xhtml_Inline.setter
    def xhtml_Inline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline", None)
        self.__xhtml_Inline = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType354"):
                    opp_val = getattr(item, "xhtml_AType354", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType354", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType354"):
                    opp_val = getattr(item, "xhtml_AType354", None)
                    
                    setattr(item, "xhtml_AType354", self)
                    

    @property
    def xhtml_Inline377(self):
        return self.__xhtml_Inline377

    @xhtml_Inline377.setter
    def xhtml_Inline377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline377", None)
        self.__xhtml_Inline377 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType378"):
                    opp_val = getattr(item, "xhtml_BType378", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType378", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType378"):
                    opp_val = getattr(item, "xhtml_BType378", None)
                    
                    setattr(item, "xhtml_BType378", self)
                    

    @property
    def xhtml_Inline374(self):
        return self.__xhtml_Inline374

    @xhtml_Inline374.setter
    def xhtml_Inline374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline374", None)
        self.__xhtml_Inline374 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType375"):
                    opp_val = getattr(item, "xhtml_IType375", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType375", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType375"):
                    opp_val = getattr(item, "xhtml_IType375", None)
                    
                    setattr(item, "xhtml_IType375", self)
                    

    @property
    def xhtml_Inline365(self):
        return self.__xhtml_Inline365

    @xhtml_Inline365.setter
    def xhtml_Inline365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline365", None)
        self.__xhtml_Inline365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_MapType366"):
                    opp_val = getattr(item, "xhtml_MapType366", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_MapType366", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_MapType366"):
                    opp_val = getattr(item, "xhtml_MapType366", None)
                    
                    setattr(item, "xhtml_MapType366", self)
                    

    @property
    def xhtml_Inline413(self):
        return self.__xhtml_Inline413

    @xhtml_Inline413.setter
    def xhtml_Inline413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline413", None)
        self.__xhtml_Inline413 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType414"):
                    opp_val = getattr(item, "xhtml_AbbrType414", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType414", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType414"):
                    opp_val = getattr(item, "xhtml_AbbrType414", None)
                    
                    setattr(item, "xhtml_AbbrType414", self)
                    

    @property
    def xhtml_Inline380(self):
        return self.__xhtml_Inline380

    @xhtml_Inline380.setter
    def xhtml_Inline380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline380", None)
        self.__xhtml_Inline380 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType381"):
                    opp_val = getattr(item, "xhtml_BigType381", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType381", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType381"):
                    opp_val = getattr(item, "xhtml_BigType381", None)
                    
                    setattr(item, "xhtml_BigType381", self)
                    

    @property
    def xhtml_Inline419(self):
        return self.__xhtml_Inline419

    @xhtml_Inline419.setter
    def xhtml_Inline419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline419", None)
        self.__xhtml_Inline419 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType420"):
                    opp_val = getattr(item, "xhtml_SubType420", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType420", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType420"):
                    opp_val = getattr(item, "xhtml_SubType420", None)
                    
                    setattr(item, "xhtml_SubType420", self)
                    

    @property
    def xhtml_Inline392(self):
        return self.__xhtml_Inline392

    @xhtml_Inline392.setter
    def xhtml_Inline392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline392", None)
        self.__xhtml_Inline392 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType393"):
                    opp_val = getattr(item, "xhtml_DfnType393", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType393", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType393"):
                    opp_val = getattr(item, "xhtml_DfnType393", None)
                    
                    setattr(item, "xhtml_DfnType393", self)
                    

    @property
    def xhtml_Inline407(self):
        return self.__xhtml_Inline407

    @xhtml_Inline407.setter
    def xhtml_Inline407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline407", None)
        self.__xhtml_Inline407 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType408"):
                    opp_val = getattr(item, "xhtml_VarType408", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType408", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType408"):
                    opp_val = getattr(item, "xhtml_VarType408", None)
                    
                    setattr(item, "xhtml_VarType408", self)
                    

    @property
    def xhtml_Inline404(self):
        return self.__xhtml_Inline404

    @xhtml_Inline404.setter
    def xhtml_Inline404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline404", None)
        self.__xhtml_Inline404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType405"):
                    opp_val = getattr(item, "xhtml_KbdType405", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType405"):
                    opp_val = getattr(item, "xhtml_KbdType405", None)
                    
                    setattr(item, "xhtml_KbdType405", self)
                    

    @property
    def xhtml_Inline422(self):
        return self.__xhtml_Inline422

    @xhtml_Inline422.setter
    def xhtml_Inline422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline422", None)
        self.__xhtml_Inline422 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType423"):
                    opp_val = getattr(item, "xhtml_SupType423", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType423", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType423"):
                    opp_val = getattr(item, "xhtml_SupType423", None)
                    
                    setattr(item, "xhtml_SupType423", self)
                    

    @property
    def xhtml_Inline389(self):
        return self.__xhtml_Inline389

    @xhtml_Inline389.setter
    def xhtml_Inline389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline389", None)
        self.__xhtml_Inline389 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType390"):
                    opp_val = getattr(item, "xhtml_StrongType390", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType390", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType390"):
                    opp_val = getattr(item, "xhtml_StrongType390", None)
                    
                    setattr(item, "xhtml_StrongType390", self)
                    

    @property
    def xhtml_Inline398(self):
        return self.__xhtml_Inline398

    @xhtml_Inline398.setter
    def xhtml_Inline398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline398", None)
        self.__xhtml_Inline398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType399"):
                    opp_val = getattr(item, "xhtml_QType399", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType399"):
                    opp_val = getattr(item, "xhtml_QType399", None)
                    
                    setattr(item, "xhtml_QType399", self)
                    

    @property
    def xhtml_Inline356(self):
        return self.__xhtml_Inline356

    @xhtml_Inline356.setter
    def xhtml_Inline356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline356", None)
        self.__xhtml_Inline356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType357"):
                    opp_val = getattr(item, "xhtml_BrType357", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType357"):
                    opp_val = getattr(item, "xhtml_BrType357", None)
                    
                    setattr(item, "xhtml_BrType357", self)
                    

    @property
    def xhtml_Inline410(self):
        return self.__xhtml_Inline410

    @xhtml_Inline410.setter
    def xhtml_Inline410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline410", None)
        self.__xhtml_Inline410 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType411"):
                    opp_val = getattr(item, "xhtml_CiteType411", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType411", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType411"):
                    opp_val = getattr(item, "xhtml_CiteType411", None)
                    
                    setattr(item, "xhtml_CiteType411", self)
                    

    @property
    def xhtml_Inline368(self):
        return self.__xhtml_Inline368

    @xhtml_Inline368.setter
    def xhtml_Inline368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline368", None)
        self.__xhtml_Inline368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType369"):
                    opp_val = getattr(item, "xhtml_ImgType369", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType369", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType369"):
                    opp_val = getattr(item, "xhtml_ImgType369", None)
                    
                    setattr(item, "xhtml_ImgType369", self)
                    

    @property
    def xhtml_Inline359(self):
        return self.__xhtml_Inline359

    @xhtml_Inline359.setter
    def xhtml_Inline359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline359", None)
        self.__xhtml_Inline359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType360"):
                    opp_val = getattr(item, "xhtml_SpanType360", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType360"):
                    opp_val = getattr(item, "xhtml_SpanType360", None)
                    
                    setattr(item, "xhtml_SpanType360", self)
                    

    @property
    def xhtml_Inline416(self):
        return self.__xhtml_Inline416

    @xhtml_Inline416.setter
    def xhtml_Inline416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline416", None)
        self.__xhtml_Inline416 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType417"):
                    opp_val = getattr(item, "xhtml_AcronymType417", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType417", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType417"):
                    opp_val = getattr(item, "xhtml_AcronymType417", None)
                    
                    setattr(item, "xhtml_AcronymType417", self)
                    

class xhtml_Flow:

    def __init__(self, mixed: str, group: str, xhtml_Flow249: set["xhtml_H5Type"] = None, xhtml_Flow252: set["xhtml_H6Type"] = None, xhtml_Flow255: set["xhtml_DivType"] = None, xhtml_Flow: set["xhtml_PType"] = None, xhtml_Flow237: set["xhtml_H1Type"] = None, xhtml_Flow240: set["xhtml_H2Type"] = None, xhtml_Flow243: set["xhtml_H3Type"] = None, xhtml_Flow246: set["xhtml_H4Type"] = None, xhtml_Flow270: set["xhtml_HrType"] = None, xhtml_Flow273: set["xhtml_BlockquoteType"] = None, xhtml_Flow276: set["xhtml_AddressType"] = None, xhtml_Flow258: set["xhtml_UlType"] = None, xhtml_Flow261: set["xhtml_OlType"] = None, xhtml_Flow264: set["xhtml_DlType"] = None, xhtml_Flow267: set["xhtml_PreType"] = None, xhtml_Flow297: set["xhtml_ImgType"] = None, xhtml_Flow300: set["xhtml_TtType"] = None, xhtml_Flow303: set["xhtml_IType"] = None, xhtml_Flow279: set["xhtml_TableType"] = None, xhtml_Flow282: set["xhtml_AType"] = None, xhtml_Flow285: set["xhtml_BrType"] = None, xhtml_Flow288: set["xhtml_SpanType"] = None, xhtml_Flow291: set["xhtml_BdoType"] = None, xhtml_Flow294: set["xhtml_MapType"] = None, xhtml_Flow321: set["xhtml_DfnType"] = None, xhtml_Flow324: set["xhtml_CodeType"] = None, xhtml_Flow327: set["xhtml_QType"] = None, xhtml_Flow306: set["xhtml_BType"] = None, xhtml_Flow309: set["xhtml_BigType"] = None, xhtml_Flow312: set["xhtml_SmallType"] = None, xhtml_Flow315: set["xhtml_EmType"] = None, xhtml_Flow318: set["xhtml_StrongType"] = None, xhtml_Flow345: set["xhtml_AcronymType"] = None, xhtml_Flow348: set["xhtml_SubType"] = None, xhtml_Flow351: set["xhtml_SupType"] = None, xhtml_Flow330: set["xhtml_SampType"] = None, xhtml_Flow333: set["xhtml_KbdType"] = None, xhtml_Flow336: set["xhtml_VarType"] = None, xhtml_Flow339: set["xhtml_CiteType"] = None, xhtml_Flow342: set["xhtml_AbbrType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_Flow249 = xhtml_Flow249 if xhtml_Flow249 is not None else set()
        self.xhtml_Flow252 = xhtml_Flow252 if xhtml_Flow252 is not None else set()
        self.xhtml_Flow255 = xhtml_Flow255 if xhtml_Flow255 is not None else set()
        self.xhtml_Flow = xhtml_Flow if xhtml_Flow is not None else set()
        self.xhtml_Flow237 = xhtml_Flow237 if xhtml_Flow237 is not None else set()
        self.xhtml_Flow240 = xhtml_Flow240 if xhtml_Flow240 is not None else set()
        self.xhtml_Flow243 = xhtml_Flow243 if xhtml_Flow243 is not None else set()
        self.xhtml_Flow246 = xhtml_Flow246 if xhtml_Flow246 is not None else set()
        self.xhtml_Flow270 = xhtml_Flow270 if xhtml_Flow270 is not None else set()
        self.xhtml_Flow273 = xhtml_Flow273 if xhtml_Flow273 is not None else set()
        self.xhtml_Flow276 = xhtml_Flow276 if xhtml_Flow276 is not None else set()
        self.xhtml_Flow258 = xhtml_Flow258 if xhtml_Flow258 is not None else set()
        self.xhtml_Flow261 = xhtml_Flow261 if xhtml_Flow261 is not None else set()
        self.xhtml_Flow264 = xhtml_Flow264 if xhtml_Flow264 is not None else set()
        self.xhtml_Flow267 = xhtml_Flow267 if xhtml_Flow267 is not None else set()
        self.xhtml_Flow297 = xhtml_Flow297 if xhtml_Flow297 is not None else set()
        self.xhtml_Flow300 = xhtml_Flow300 if xhtml_Flow300 is not None else set()
        self.xhtml_Flow303 = xhtml_Flow303 if xhtml_Flow303 is not None else set()
        self.xhtml_Flow279 = xhtml_Flow279 if xhtml_Flow279 is not None else set()
        self.xhtml_Flow282 = xhtml_Flow282 if xhtml_Flow282 is not None else set()
        self.xhtml_Flow285 = xhtml_Flow285 if xhtml_Flow285 is not None else set()
        self.xhtml_Flow288 = xhtml_Flow288 if xhtml_Flow288 is not None else set()
        self.xhtml_Flow291 = xhtml_Flow291 if xhtml_Flow291 is not None else set()
        self.xhtml_Flow294 = xhtml_Flow294 if xhtml_Flow294 is not None else set()
        self.xhtml_Flow321 = xhtml_Flow321 if xhtml_Flow321 is not None else set()
        self.xhtml_Flow324 = xhtml_Flow324 if xhtml_Flow324 is not None else set()
        self.xhtml_Flow327 = xhtml_Flow327 if xhtml_Flow327 is not None else set()
        self.xhtml_Flow306 = xhtml_Flow306 if xhtml_Flow306 is not None else set()
        self.xhtml_Flow309 = xhtml_Flow309 if xhtml_Flow309 is not None else set()
        self.xhtml_Flow312 = xhtml_Flow312 if xhtml_Flow312 is not None else set()
        self.xhtml_Flow315 = xhtml_Flow315 if xhtml_Flow315 is not None else set()
        self.xhtml_Flow318 = xhtml_Flow318 if xhtml_Flow318 is not None else set()
        self.xhtml_Flow345 = xhtml_Flow345 if xhtml_Flow345 is not None else set()
        self.xhtml_Flow348 = xhtml_Flow348 if xhtml_Flow348 is not None else set()
        self.xhtml_Flow351 = xhtml_Flow351 if xhtml_Flow351 is not None else set()
        self.xhtml_Flow330 = xhtml_Flow330 if xhtml_Flow330 is not None else set()
        self.xhtml_Flow333 = xhtml_Flow333 if xhtml_Flow333 is not None else set()
        self.xhtml_Flow336 = xhtml_Flow336 if xhtml_Flow336 is not None else set()
        self.xhtml_Flow339 = xhtml_Flow339 if xhtml_Flow339 is not None else set()
        self.xhtml_Flow342 = xhtml_Flow342 if xhtml_Flow342 is not None else set()
        
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
    def xhtml_Flow279(self):
        return self.__xhtml_Flow279

    @xhtml_Flow279.setter
    def xhtml_Flow279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow279", None)
        self.__xhtml_Flow279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType280"):
                    opp_val = getattr(item, "xhtml_TableType280", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType280"):
                    opp_val = getattr(item, "xhtml_TableType280", None)
                    
                    setattr(item, "xhtml_TableType280", self)
                    

    @property
    def xhtml_Flow294(self):
        return self.__xhtml_Flow294

    @xhtml_Flow294.setter
    def xhtml_Flow294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow294", None)
        self.__xhtml_Flow294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_MapType295"):
                    opp_val = getattr(item, "xhtml_MapType295", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_MapType295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_MapType295"):
                    opp_val = getattr(item, "xhtml_MapType295", None)
                    
                    setattr(item, "xhtml_MapType295", self)
                    

    @property
    def xhtml_Flow285(self):
        return self.__xhtml_Flow285

    @xhtml_Flow285.setter
    def xhtml_Flow285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow285", None)
        self.__xhtml_Flow285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType286"):
                    opp_val = getattr(item, "xhtml_BrType286", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType286"):
                    opp_val = getattr(item, "xhtml_BrType286", None)
                    
                    setattr(item, "xhtml_BrType286", self)
                    

    @property
    def xhtml_Flow264(self):
        return self.__xhtml_Flow264

    @xhtml_Flow264.setter
    def xhtml_Flow264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow264", None)
        self.__xhtml_Flow264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType265"):
                    opp_val = getattr(item, "xhtml_DlType265", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType265"):
                    opp_val = getattr(item, "xhtml_DlType265", None)
                    
                    setattr(item, "xhtml_DlType265", self)
                    

    @property
    def xhtml_Flow267(self):
        return self.__xhtml_Flow267

    @xhtml_Flow267.setter
    def xhtml_Flow267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow267", None)
        self.__xhtml_Flow267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType268"):
                    opp_val = getattr(item, "xhtml_PreType268", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType268"):
                    opp_val = getattr(item, "xhtml_PreType268", None)
                    
                    setattr(item, "xhtml_PreType268", self)
                    

    @property
    def xhtml_Flow276(self):
        return self.__xhtml_Flow276

    @xhtml_Flow276.setter
    def xhtml_Flow276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow276", None)
        self.__xhtml_Flow276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType277"):
                    opp_val = getattr(item, "xhtml_AddressType277", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType277"):
                    opp_val = getattr(item, "xhtml_AddressType277", None)
                    
                    setattr(item, "xhtml_AddressType277", self)
                    

    @property
    def xhtml_Flow246(self):
        return self.__xhtml_Flow246

    @xhtml_Flow246.setter
    def xhtml_Flow246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow246", None)
        self.__xhtml_Flow246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type247"):
                    opp_val = getattr(item, "xhtml_H4Type247", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type247"):
                    opp_val = getattr(item, "xhtml_H4Type247", None)
                    
                    setattr(item, "xhtml_H4Type247", self)
                    

    @property
    def xhtml_Flow288(self):
        return self.__xhtml_Flow288

    @xhtml_Flow288.setter
    def xhtml_Flow288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow288", None)
        self.__xhtml_Flow288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType289"):
                    opp_val = getattr(item, "xhtml_SpanType289", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType289"):
                    opp_val = getattr(item, "xhtml_SpanType289", None)
                    
                    setattr(item, "xhtml_SpanType289", self)
                    

    @property
    def xhtml_Flow249(self):
        return self.__xhtml_Flow249

    @xhtml_Flow249.setter
    def xhtml_Flow249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow249", None)
        self.__xhtml_Flow249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type250"):
                    opp_val = getattr(item, "xhtml_H5Type250", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type250"):
                    opp_val = getattr(item, "xhtml_H5Type250", None)
                    
                    setattr(item, "xhtml_H5Type250", self)
                    

    @property
    def xhtml_Flow306(self):
        return self.__xhtml_Flow306

    @xhtml_Flow306.setter
    def xhtml_Flow306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow306", None)
        self.__xhtml_Flow306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType307"):
                    opp_val = getattr(item, "xhtml_BType307", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType307"):
                    opp_val = getattr(item, "xhtml_BType307", None)
                    
                    setattr(item, "xhtml_BType307", self)
                    

    @property
    def xhtml_Flow327(self):
        return self.__xhtml_Flow327

    @xhtml_Flow327.setter
    def xhtml_Flow327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow327", None)
        self.__xhtml_Flow327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType328"):
                    opp_val = getattr(item, "xhtml_QType328", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType328"):
                    opp_val = getattr(item, "xhtml_QType328", None)
                    
                    setattr(item, "xhtml_QType328", self)
                    

    @property
    def xhtml_Flow339(self):
        return self.__xhtml_Flow339

    @xhtml_Flow339.setter
    def xhtml_Flow339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow339", None)
        self.__xhtml_Flow339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType340"):
                    opp_val = getattr(item, "xhtml_CiteType340", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType340"):
                    opp_val = getattr(item, "xhtml_CiteType340", None)
                    
                    setattr(item, "xhtml_CiteType340", self)
                    

    @property
    def xhtml_Flow309(self):
        return self.__xhtml_Flow309

    @xhtml_Flow309.setter
    def xhtml_Flow309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow309", None)
        self.__xhtml_Flow309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType310"):
                    opp_val = getattr(item, "xhtml_BigType310", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType310"):
                    opp_val = getattr(item, "xhtml_BigType310", None)
                    
                    setattr(item, "xhtml_BigType310", self)
                    

    @property
    def xhtml_Flow318(self):
        return self.__xhtml_Flow318

    @xhtml_Flow318.setter
    def xhtml_Flow318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow318", None)
        self.__xhtml_Flow318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType319"):
                    opp_val = getattr(item, "xhtml_StrongType319", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType319"):
                    opp_val = getattr(item, "xhtml_StrongType319", None)
                    
                    setattr(item, "xhtml_StrongType319", self)
                    

    @property
    def xhtml_Flow297(self):
        return self.__xhtml_Flow297

    @xhtml_Flow297.setter
    def xhtml_Flow297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow297", None)
        self.__xhtml_Flow297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType298"):
                    opp_val = getattr(item, "xhtml_ImgType298", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType298"):
                    opp_val = getattr(item, "xhtml_ImgType298", None)
                    
                    setattr(item, "xhtml_ImgType298", self)
                    

    @property
    def xhtml_Flow300(self):
        return self.__xhtml_Flow300

    @xhtml_Flow300.setter
    def xhtml_Flow300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow300", None)
        self.__xhtml_Flow300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType301"):
                    opp_val = getattr(item, "xhtml_TtType301", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType301"):
                    opp_val = getattr(item, "xhtml_TtType301", None)
                    
                    setattr(item, "xhtml_TtType301", self)
                    

    @property
    def xhtml_Flow303(self):
        return self.__xhtml_Flow303

    @xhtml_Flow303.setter
    def xhtml_Flow303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow303", None)
        self.__xhtml_Flow303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType304"):
                    opp_val = getattr(item, "xhtml_IType304", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType304"):
                    opp_val = getattr(item, "xhtml_IType304", None)
                    
                    setattr(item, "xhtml_IType304", self)
                    

    @property
    def xhtml_Flow282(self):
        return self.__xhtml_Flow282

    @xhtml_Flow282.setter
    def xhtml_Flow282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow282", None)
        self.__xhtml_Flow282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType283"):
                    opp_val = getattr(item, "xhtml_AType283", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType283"):
                    opp_val = getattr(item, "xhtml_AType283", None)
                    
                    setattr(item, "xhtml_AType283", self)
                    

    @property
    def xhtml_Flow312(self):
        return self.__xhtml_Flow312

    @xhtml_Flow312.setter
    def xhtml_Flow312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow312", None)
        self.__xhtml_Flow312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType313"):
                    opp_val = getattr(item, "xhtml_SmallType313", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType313"):
                    opp_val = getattr(item, "xhtml_SmallType313", None)
                    
                    setattr(item, "xhtml_SmallType313", self)
                    

    @property
    def xhtml_Flow324(self):
        return self.__xhtml_Flow324

    @xhtml_Flow324.setter
    def xhtml_Flow324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow324", None)
        self.__xhtml_Flow324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType325"):
                    opp_val = getattr(item, "xhtml_CodeType325", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType325"):
                    opp_val = getattr(item, "xhtml_CodeType325", None)
                    
                    setattr(item, "xhtml_CodeType325", self)
                    

    @property
    def xhtml_Flow336(self):
        return self.__xhtml_Flow336

    @xhtml_Flow336.setter
    def xhtml_Flow336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow336", None)
        self.__xhtml_Flow336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType337"):
                    opp_val = getattr(item, "xhtml_VarType337", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType337"):
                    opp_val = getattr(item, "xhtml_VarType337", None)
                    
                    setattr(item, "xhtml_VarType337", self)
                    

    @property
    def xhtml_Flow342(self):
        return self.__xhtml_Flow342

    @xhtml_Flow342.setter
    def xhtml_Flow342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow342", None)
        self.__xhtml_Flow342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType343"):
                    opp_val = getattr(item, "xhtml_AbbrType343", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType343", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType343"):
                    opp_val = getattr(item, "xhtml_AbbrType343", None)
                    
                    setattr(item, "xhtml_AbbrType343", self)
                    

    @property
    def xhtml_Flow351(self):
        return self.__xhtml_Flow351

    @xhtml_Flow351.setter
    def xhtml_Flow351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow351", None)
        self.__xhtml_Flow351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType352"):
                    opp_val = getattr(item, "xhtml_SupType352", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType352"):
                    opp_val = getattr(item, "xhtml_SupType352", None)
                    
                    setattr(item, "xhtml_SupType352", self)
                    

    @property
    def xhtml_Flow243(self):
        return self.__xhtml_Flow243

    @xhtml_Flow243.setter
    def xhtml_Flow243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow243", None)
        self.__xhtml_Flow243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type244"):
                    opp_val = getattr(item, "xhtml_H3Type244", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type244"):
                    opp_val = getattr(item, "xhtml_H3Type244", None)
                    
                    setattr(item, "xhtml_H3Type244", self)
                    

    @property
    def xhtml_Flow240(self):
        return self.__xhtml_Flow240

    @xhtml_Flow240.setter
    def xhtml_Flow240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow240", None)
        self.__xhtml_Flow240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type241"):
                    opp_val = getattr(item, "xhtml_H2Type241", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type241"):
                    opp_val = getattr(item, "xhtml_H2Type241", None)
                    
                    setattr(item, "xhtml_H2Type241", self)
                    

    @property
    def xhtml_Flow270(self):
        return self.__xhtml_Flow270

    @xhtml_Flow270.setter
    def xhtml_Flow270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow270", None)
        self.__xhtml_Flow270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType271"):
                    opp_val = getattr(item, "xhtml_HrType271", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType271"):
                    opp_val = getattr(item, "xhtml_HrType271", None)
                    
                    setattr(item, "xhtml_HrType271", self)
                    

    @property
    def xhtml_Flow237(self):
        return self.__xhtml_Flow237

    @xhtml_Flow237.setter
    def xhtml_Flow237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow237", None)
        self.__xhtml_Flow237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type238"):
                    opp_val = getattr(item, "xhtml_H1Type238", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type238"):
                    opp_val = getattr(item, "xhtml_H1Type238", None)
                    
                    setattr(item, "xhtml_H1Type238", self)
                    

    @property
    def xhtml_Flow348(self):
        return self.__xhtml_Flow348

    @xhtml_Flow348.setter
    def xhtml_Flow348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow348", None)
        self.__xhtml_Flow348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType349"):
                    opp_val = getattr(item, "xhtml_SubType349", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType349"):
                    opp_val = getattr(item, "xhtml_SubType349", None)
                    
                    setattr(item, "xhtml_SubType349", self)
                    

    @property
    def xhtml_Flow261(self):
        return self.__xhtml_Flow261

    @xhtml_Flow261.setter
    def xhtml_Flow261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow261", None)
        self.__xhtml_Flow261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType262"):
                    opp_val = getattr(item, "xhtml_OlType262", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType262"):
                    opp_val = getattr(item, "xhtml_OlType262", None)
                    
                    setattr(item, "xhtml_OlType262", self)
                    

    @property
    def xhtml_Flow258(self):
        return self.__xhtml_Flow258

    @xhtml_Flow258.setter
    def xhtml_Flow258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow258", None)
        self.__xhtml_Flow258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType259"):
                    opp_val = getattr(item, "xhtml_UlType259", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType259"):
                    opp_val = getattr(item, "xhtml_UlType259", None)
                    
                    setattr(item, "xhtml_UlType259", self)
                    

    @property
    def xhtml_Flow(self):
        return self.__xhtml_Flow

    @xhtml_Flow.setter
    def xhtml_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow", None)
        self.__xhtml_Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType235"):
                    opp_val = getattr(item, "xhtml_PType235", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType235"):
                    opp_val = getattr(item, "xhtml_PType235", None)
                    
                    setattr(item, "xhtml_PType235", self)
                    

    @property
    def xhtml_Flow330(self):
        return self.__xhtml_Flow330

    @xhtml_Flow330.setter
    def xhtml_Flow330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow330", None)
        self.__xhtml_Flow330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType331"):
                    opp_val = getattr(item, "xhtml_SampType331", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType331"):
                    opp_val = getattr(item, "xhtml_SampType331", None)
                    
                    setattr(item, "xhtml_SampType331", self)
                    

    @property
    def xhtml_Flow252(self):
        return self.__xhtml_Flow252

    @xhtml_Flow252.setter
    def xhtml_Flow252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow252", None)
        self.__xhtml_Flow252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type253"):
                    opp_val = getattr(item, "xhtml_H6Type253", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type253"):
                    opp_val = getattr(item, "xhtml_H6Type253", None)
                    
                    setattr(item, "xhtml_H6Type253", self)
                    

    @property
    def xhtml_Flow255(self):
        return self.__xhtml_Flow255

    @xhtml_Flow255.setter
    def xhtml_Flow255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow255", None)
        self.__xhtml_Flow255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType256"):
                    opp_val = getattr(item, "xhtml_DivType256", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType256"):
                    opp_val = getattr(item, "xhtml_DivType256", None)
                    
                    setattr(item, "xhtml_DivType256", self)
                    

    @property
    def xhtml_Flow333(self):
        return self.__xhtml_Flow333

    @xhtml_Flow333.setter
    def xhtml_Flow333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow333", None)
        self.__xhtml_Flow333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType334"):
                    opp_val = getattr(item, "xhtml_KbdType334", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType334"):
                    opp_val = getattr(item, "xhtml_KbdType334", None)
                    
                    setattr(item, "xhtml_KbdType334", self)
                    

    @property
    def xhtml_Flow273(self):
        return self.__xhtml_Flow273

    @xhtml_Flow273.setter
    def xhtml_Flow273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow273", None)
        self.__xhtml_Flow273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType274"):
                    opp_val = getattr(item, "xhtml_BlockquoteType274", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType274"):
                    opp_val = getattr(item, "xhtml_BlockquoteType274", None)
                    
                    setattr(item, "xhtml_BlockquoteType274", self)
                    

    @property
    def xhtml_Flow291(self):
        return self.__xhtml_Flow291

    @xhtml_Flow291.setter
    def xhtml_Flow291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow291", None)
        self.__xhtml_Flow291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BdoType292"):
                    opp_val = getattr(item, "xhtml_BdoType292", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BdoType292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BdoType292"):
                    opp_val = getattr(item, "xhtml_BdoType292", None)
                    
                    setattr(item, "xhtml_BdoType292", self)
                    

    @property
    def xhtml_Flow345(self):
        return self.__xhtml_Flow345

    @xhtml_Flow345.setter
    def xhtml_Flow345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow345", None)
        self.__xhtml_Flow345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType346"):
                    opp_val = getattr(item, "xhtml_AcronymType346", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType346", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType346"):
                    opp_val = getattr(item, "xhtml_AcronymType346", None)
                    
                    setattr(item, "xhtml_AcronymType346", self)
                    

    @property
    def xhtml_Flow321(self):
        return self.__xhtml_Flow321

    @xhtml_Flow321.setter
    def xhtml_Flow321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow321", None)
        self.__xhtml_Flow321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType322"):
                    opp_val = getattr(item, "xhtml_DfnType322", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType322"):
                    opp_val = getattr(item, "xhtml_DfnType322", None)
                    
                    setattr(item, "xhtml_DfnType322", self)
                    

    @property
    def xhtml_Flow315(self):
        return self.__xhtml_Flow315

    @xhtml_Flow315.setter
    def xhtml_Flow315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow315", None)
        self.__xhtml_Flow315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType316"):
                    opp_val = getattr(item, "xhtml_EmType316", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType316"):
                    opp_val = getattr(item, "xhtml_EmType316", None)
                    
                    setattr(item, "xhtml_EmType316", self)
                    

class xhtml_TrType:

    def __init__(self, group: str, align: str, char: str, charoff: str, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, valign: str, xhtml_TrType: "xhtml_DocumentRoot" = None, xhtml_TrType566: "xhtml_TableType" = None, xhtml_TrType569: "xhtml_TbodyType" = None, xhtml_TrType572: "xhtml_TfootType" = None, xhtml_TrType575: "xhtml_TheadType" = None, xhtml_TrType577: set["xhtml_ThType"] = None, xhtml_TrType580: set["xhtml_TdType"] = None):
        self.group = group
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TrType = xhtml_TrType
        self.xhtml_TrType566 = xhtml_TrType566
        self.xhtml_TrType569 = xhtml_TrType569
        self.xhtml_TrType572 = xhtml_TrType572
        self.xhtml_TrType575 = xhtml_TrType575
        self.xhtml_TrType577 = xhtml_TrType577 if xhtml_TrType577 is not None else set()
        self.xhtml_TrType580 = xhtml_TrType580 if xhtml_TrType580 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_TrType(self):
        return self.__xhtml_TrType

    @xhtml_TrType.setter
    def xhtml_TrType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType", None)
        self.__xhtml_TrType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot224"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot224"):
                opp_val = getattr(value, "xhtml_DocumentRoot224", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType572(self):
        return self.__xhtml_TrType572

    @xhtml_TrType572.setter
    def xhtml_TrType572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType572", None)
        self.__xhtml_TrType572 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TfootType571"):
                opp_val = getattr(old_value, "xhtml_TfootType571", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TfootType571"):
                opp_val = getattr(value, "xhtml_TfootType571", None)
                if opp_val is None:
                    setattr(value, "xhtml_TfootType571", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType575(self):
        return self.__xhtml_TrType575

    @xhtml_TrType575.setter
    def xhtml_TrType575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType575", None)
        self.__xhtml_TrType575 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TheadType574"):
                opp_val = getattr(old_value, "xhtml_TheadType574", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TheadType574"):
                opp_val = getattr(value, "xhtml_TheadType574", None)
                if opp_val is None:
                    setattr(value, "xhtml_TheadType574", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType569(self):
        return self.__xhtml_TrType569

    @xhtml_TrType569.setter
    def xhtml_TrType569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType569", None)
        self.__xhtml_TrType569 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TbodyType568"):
                opp_val = getattr(old_value, "xhtml_TbodyType568", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TbodyType568"):
                opp_val = getattr(value, "xhtml_TbodyType568", None)
                if opp_val is None:
                    setattr(value, "xhtml_TbodyType568", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType566(self):
        return self.__xhtml_TrType566

    @xhtml_TrType566.setter
    def xhtml_TrType566(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType566", None)
        self.__xhtml_TrType566 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType565"):
                opp_val = getattr(old_value, "xhtml_TableType565", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType565"):
                opp_val = getattr(value, "xhtml_TableType565", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType565", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType580(self):
        return self.__xhtml_TrType580

    @xhtml_TrType580.setter
    def xhtml_TrType580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType580", None)
        self.__xhtml_TrType580 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TdType581"):
                    opp_val = getattr(item, "xhtml_TdType581", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TdType581", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TdType581"):
                    opp_val = getattr(item, "xhtml_TdType581", None)
                    
                    setattr(item, "xhtml_TdType581", self)
                    

    @property
    def xhtml_TrType577(self):
        return self.__xhtml_TrType577

    @xhtml_TrType577.setter
    def xhtml_TrType577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType577", None)
        self.__xhtml_TrType577 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ThType578"):
                    opp_val = getattr(item, "xhtml_ThType578", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ThType578", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ThType578"):
                    opp_val = getattr(item, "xhtml_ThType578", None)
                    
                    setattr(item, "xhtml_ThType578", self)
                    

class xhtml_TheadType:

    def __init__(self, align: str, charoff: str, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, valign: str, char: str, xhtml_TheadType: "xhtml_DocumentRoot" = None, xhtml_TheadType557: "xhtml_TableType" = None, xhtml_TheadType574: set["xhtml_TrType"] = None):
        self.align = align
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.valign = valign
        self.char = char
        self.xhtml_TheadType = xhtml_TheadType
        self.xhtml_TheadType557 = xhtml_TheadType557
        self.xhtml_TheadType574 = xhtml_TheadType574 if xhtml_TheadType574 is not None else set()
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_TheadType574(self):
        return self.__xhtml_TheadType574

    @xhtml_TheadType574.setter
    def xhtml_TheadType574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TheadType__xhtml_TheadType574", None)
        self.__xhtml_TheadType574 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType575"):
                    opp_val = getattr(item, "xhtml_TrType575", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType575", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType575"):
                    opp_val = getattr(item, "xhtml_TrType575", None)
                    
                    setattr(item, "xhtml_TrType575", self)
                    

    @property
    def xhtml_TheadType(self):
        return self.__xhtml_TheadType

    @xhtml_TheadType.setter
    def xhtml_TheadType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TheadType__xhtml_TheadType", None)
        self.__xhtml_TheadType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot222"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot222"):
                opp_val = getattr(value, "xhtml_DocumentRoot222", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TheadType557(self):
        return self.__xhtml_TheadType557

    @xhtml_TheadType557.setter
    def xhtml_TheadType557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TheadType__xhtml_TheadType557", None)
        self.__xhtml_TheadType557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType556"):
                opp_val = getattr(old_value, "xhtml_TableType556", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType556", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType556"):
                opp_val = getattr(value, "xhtml_TableType556", None)
                setattr(value, "xhtml_TableType556", self)

class xhtml_TfootType:

    def __init__(self, align: str, charoff: str, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, valign: str, char: str, xhtml_TfootType: "xhtml_DocumentRoot" = None, xhtml_TfootType560: "xhtml_TableType" = None, xhtml_TfootType571: set["xhtml_TrType"] = None):
        self.align = align
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.valign = valign
        self.char = char
        self.xhtml_TfootType = xhtml_TfootType
        self.xhtml_TfootType560 = xhtml_TfootType560
        self.xhtml_TfootType571 = xhtml_TfootType571 if xhtml_TfootType571 is not None else set()
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def xhtml_TfootType(self):
        return self.__xhtml_TfootType

    @xhtml_TfootType.setter
    def xhtml_TfootType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TfootType__xhtml_TfootType", None)
        self.__xhtml_TfootType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot218"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot218"):
                opp_val = getattr(value, "xhtml_DocumentRoot218", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TfootType560(self):
        return self.__xhtml_TfootType560

    @xhtml_TfootType560.setter
    def xhtml_TfootType560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TfootType__xhtml_TfootType560", None)
        self.__xhtml_TfootType560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType559"):
                opp_val = getattr(old_value, "xhtml_TableType559", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType559"):
                opp_val = getattr(value, "xhtml_TableType559", None)
                setattr(value, "xhtml_TableType559", self)

    @property
    def xhtml_TfootType571(self):
        return self.__xhtml_TfootType571

    @xhtml_TfootType571.setter
    def xhtml_TfootType571(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TfootType__xhtml_TfootType571", None)
        self.__xhtml_TfootType571 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType572"):
                    opp_val = getattr(item, "xhtml_TrType572", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType572", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType572"):
                    opp_val = getattr(item, "xhtml_TrType572", None)
                    
                    setattr(item, "xhtml_TrType572", self)
                    

class xhtml_TbodyType:

    def __init__(self, align: str, char: str, charoff: str, class: str, id: str, lang: str, lang1: str, style: str, title: str, valign: str, dir: str, xhtml_TbodyType: "xhtml_DocumentRoot" = None, xhtml_TbodyType563: "xhtml_TableType" = None, xhtml_TbodyType568: set["xhtml_TrType"] = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.valign = valign
        self.dir = dir
        self.xhtml_TbodyType = xhtml_TbodyType
        self.xhtml_TbodyType563 = xhtml_TbodyType563
        self.xhtml_TbodyType568 = xhtml_TbodyType568 if xhtml_TbodyType568 is not None else set()
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def xhtml_TbodyType(self):
        return self.__xhtml_TbodyType

    @xhtml_TbodyType.setter
    def xhtml_TbodyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TbodyType__xhtml_TbodyType", None)
        self.__xhtml_TbodyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot214"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot214"):
                opp_val = getattr(value, "xhtml_DocumentRoot214", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TbodyType568(self):
        return self.__xhtml_TbodyType568

    @xhtml_TbodyType568.setter
    def xhtml_TbodyType568(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TbodyType__xhtml_TbodyType568", None)
        self.__xhtml_TbodyType568 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType569"):
                    opp_val = getattr(item, "xhtml_TrType569", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType569", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType569"):
                    opp_val = getattr(item, "xhtml_TrType569", None)
                    
                    setattr(item, "xhtml_TrType569", self)
                    

    @property
    def xhtml_TbodyType563(self):
        return self.__xhtml_TbodyType563

    @xhtml_TbodyType563.setter
    def xhtml_TbodyType563(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TbodyType__xhtml_TbodyType563", None)
        self.__xhtml_TbodyType563 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType562"):
                opp_val = getattr(old_value, "xhtml_TableType562", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType562"):
                opp_val = getattr(value, "xhtml_TableType562", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType562", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_EStringToStringMapEntry:

    pass
class xhtml_DocumentRoot:

    def __init__(self, mixed: str, xhtml_DocumentRoot97: set["xhtml_AreaType"] = None, xhtml_DocumentRoot99: set["xhtml_BType"] = None, xhtml_DocumentRoot102: set["xhtml_BdoType"] = None, xhtml_DocumentRoot105: set["xhtml_BigType"] = None, xhtml_DocumentRoot: set["xhtml_EStringToStringMapEntry"] = None, xhtml_DocumentRoot83: set["xhtml_EStringToStringMapEntry"] = None, xhtml_DocumentRoot86: set["xhtml_AType"] = None, xhtml_DocumentRoot88: set["xhtml_AbbrType"] = None, xhtml_DocumentRoot91: set["xhtml_AcronymType"] = None, xhtml_DocumentRoot94: set["xhtml_AddressType"] = None, xhtml_DocumentRoot122: set["xhtml_ColType"] = None, xhtml_DocumentRoot125: set["xhtml_ColgroupType"] = None, xhtml_DocumentRoot128: set["xhtml_DdType"] = None, xhtml_DocumentRoot131: set["xhtml_DfnType"] = None, xhtml_DocumentRoot108: set["xhtml_BlockquoteType"] = None, xhtml_DocumentRoot111: set["xhtml_BrType"] = None, xhtml_DocumentRoot114: set["xhtml_CaptionType"] = None, xhtml_DocumentRoot116: set["xhtml_CiteType"] = None, xhtml_DocumentRoot119: set["xhtml_CodeType"] = None, xhtml_DocumentRoot149: set["xhtml_H2Type"] = None, xhtml_DocumentRoot152: set["xhtml_H3Type"] = None, xhtml_DocumentRoot155: set["xhtml_H4Type"] = None, xhtml_DocumentRoot158: set["xhtml_H5Type"] = None, xhtml_DocumentRoot134: set["xhtml_DivType"] = None, xhtml_DocumentRoot137: set["xhtml_DlType"] = None, xhtml_DocumentRoot140: set["xhtml_DtType"] = None, xhtml_DocumentRoot143: set["xhtml_EmType"] = None, xhtml_DocumentRoot146: set["xhtml_H1Type"] = None, xhtml_DocumentRoot167: set["xhtml_IType"] = None, xhtml_DocumentRoot170: set["xhtml_ImgType"] = None, xhtml_DocumentRoot173: set["xhtml_KbdType"] = None, xhtml_DocumentRoot176: set["xhtml_LiType"] = None, xhtml_DocumentRoot161: set["xhtml_H6Type"] = None, xhtml_DocumentRoot164: set["xhtml_HrType"] = None, xhtml_DocumentRoot193: set["xhtml_SampType"] = None, xhtml_DocumentRoot196: set["xhtml_SmallType"] = None, xhtml_DocumentRoot199: set["xhtml_SpanType"] = None, xhtml_DocumentRoot202: set["xhtml_StrongType"] = None, xhtml_DocumentRoot178: set["xhtml_MapType"] = None, xhtml_DocumentRoot181: set["xhtml_OlType"] = None, xhtml_DocumentRoot184: set["xhtml_PType"] = None, xhtml_DocumentRoot187: set["xhtml_PreType"] = None, xhtml_DocumentRoot190: set["xhtml_QType"] = None, xhtml_DocumentRoot211: set["xhtml_TableType"] = None, xhtml_DocumentRoot214: set["xhtml_TbodyType"] = None, xhtml_DocumentRoot216: set["xhtml_TdType"] = None, xhtml_DocumentRoot205: set["xhtml_SubType"] = None, xhtml_DocumentRoot208: set["xhtml_SupType"] = None, xhtml_DocumentRoot229: set["xhtml_UlType"] = None, xhtml_DocumentRoot232: set["xhtml_VarType"] = None, xhtml_DocumentRoot218: set["xhtml_TfootType"] = None, xhtml_DocumentRoot220: set["xhtml_ThType"] = None, xhtml_DocumentRoot222: set["xhtml_TheadType"] = None, xhtml_DocumentRoot224: set["xhtml_TrType"] = None, xhtml_DocumentRoot226: set["xhtml_TtType"] = None):
        self.mixed = mixed
        self.xhtml_DocumentRoot97 = xhtml_DocumentRoot97 if xhtml_DocumentRoot97 is not None else set()
        self.xhtml_DocumentRoot99 = xhtml_DocumentRoot99 if xhtml_DocumentRoot99 is not None else set()
        self.xhtml_DocumentRoot102 = xhtml_DocumentRoot102 if xhtml_DocumentRoot102 is not None else set()
        self.xhtml_DocumentRoot105 = xhtml_DocumentRoot105 if xhtml_DocumentRoot105 is not None else set()
        self.xhtml_DocumentRoot = xhtml_DocumentRoot if xhtml_DocumentRoot is not None else set()
        self.xhtml_DocumentRoot83 = xhtml_DocumentRoot83 if xhtml_DocumentRoot83 is not None else set()
        self.xhtml_DocumentRoot86 = xhtml_DocumentRoot86 if xhtml_DocumentRoot86 is not None else set()
        self.xhtml_DocumentRoot88 = xhtml_DocumentRoot88 if xhtml_DocumentRoot88 is not None else set()
        self.xhtml_DocumentRoot91 = xhtml_DocumentRoot91 if xhtml_DocumentRoot91 is not None else set()
        self.xhtml_DocumentRoot94 = xhtml_DocumentRoot94 if xhtml_DocumentRoot94 is not None else set()
        self.xhtml_DocumentRoot122 = xhtml_DocumentRoot122 if xhtml_DocumentRoot122 is not None else set()
        self.xhtml_DocumentRoot125 = xhtml_DocumentRoot125 if xhtml_DocumentRoot125 is not None else set()
        self.xhtml_DocumentRoot128 = xhtml_DocumentRoot128 if xhtml_DocumentRoot128 is not None else set()
        self.xhtml_DocumentRoot131 = xhtml_DocumentRoot131 if xhtml_DocumentRoot131 is not None else set()
        self.xhtml_DocumentRoot108 = xhtml_DocumentRoot108 if xhtml_DocumentRoot108 is not None else set()
        self.xhtml_DocumentRoot111 = xhtml_DocumentRoot111 if xhtml_DocumentRoot111 is not None else set()
        self.xhtml_DocumentRoot114 = xhtml_DocumentRoot114 if xhtml_DocumentRoot114 is not None else set()
        self.xhtml_DocumentRoot116 = xhtml_DocumentRoot116 if xhtml_DocumentRoot116 is not None else set()
        self.xhtml_DocumentRoot119 = xhtml_DocumentRoot119 if xhtml_DocumentRoot119 is not None else set()
        self.xhtml_DocumentRoot149 = xhtml_DocumentRoot149 if xhtml_DocumentRoot149 is not None else set()
        self.xhtml_DocumentRoot152 = xhtml_DocumentRoot152 if xhtml_DocumentRoot152 is not None else set()
        self.xhtml_DocumentRoot155 = xhtml_DocumentRoot155 if xhtml_DocumentRoot155 is not None else set()
        self.xhtml_DocumentRoot158 = xhtml_DocumentRoot158 if xhtml_DocumentRoot158 is not None else set()
        self.xhtml_DocumentRoot134 = xhtml_DocumentRoot134 if xhtml_DocumentRoot134 is not None else set()
        self.xhtml_DocumentRoot137 = xhtml_DocumentRoot137 if xhtml_DocumentRoot137 is not None else set()
        self.xhtml_DocumentRoot140 = xhtml_DocumentRoot140 if xhtml_DocumentRoot140 is not None else set()
        self.xhtml_DocumentRoot143 = xhtml_DocumentRoot143 if xhtml_DocumentRoot143 is not None else set()
        self.xhtml_DocumentRoot146 = xhtml_DocumentRoot146 if xhtml_DocumentRoot146 is not None else set()
        self.xhtml_DocumentRoot167 = xhtml_DocumentRoot167 if xhtml_DocumentRoot167 is not None else set()
        self.xhtml_DocumentRoot170 = xhtml_DocumentRoot170 if xhtml_DocumentRoot170 is not None else set()
        self.xhtml_DocumentRoot173 = xhtml_DocumentRoot173 if xhtml_DocumentRoot173 is not None else set()
        self.xhtml_DocumentRoot176 = xhtml_DocumentRoot176 if xhtml_DocumentRoot176 is not None else set()
        self.xhtml_DocumentRoot161 = xhtml_DocumentRoot161 if xhtml_DocumentRoot161 is not None else set()
        self.xhtml_DocumentRoot164 = xhtml_DocumentRoot164 if xhtml_DocumentRoot164 is not None else set()
        self.xhtml_DocumentRoot193 = xhtml_DocumentRoot193 if xhtml_DocumentRoot193 is not None else set()
        self.xhtml_DocumentRoot196 = xhtml_DocumentRoot196 if xhtml_DocumentRoot196 is not None else set()
        self.xhtml_DocumentRoot199 = xhtml_DocumentRoot199 if xhtml_DocumentRoot199 is not None else set()
        self.xhtml_DocumentRoot202 = xhtml_DocumentRoot202 if xhtml_DocumentRoot202 is not None else set()
        self.xhtml_DocumentRoot178 = xhtml_DocumentRoot178 if xhtml_DocumentRoot178 is not None else set()
        self.xhtml_DocumentRoot181 = xhtml_DocumentRoot181 if xhtml_DocumentRoot181 is not None else set()
        self.xhtml_DocumentRoot184 = xhtml_DocumentRoot184 if xhtml_DocumentRoot184 is not None else set()
        self.xhtml_DocumentRoot187 = xhtml_DocumentRoot187 if xhtml_DocumentRoot187 is not None else set()
        self.xhtml_DocumentRoot190 = xhtml_DocumentRoot190 if xhtml_DocumentRoot190 is not None else set()
        self.xhtml_DocumentRoot211 = xhtml_DocumentRoot211 if xhtml_DocumentRoot211 is not None else set()
        self.xhtml_DocumentRoot214 = xhtml_DocumentRoot214 if xhtml_DocumentRoot214 is not None else set()
        self.xhtml_DocumentRoot216 = xhtml_DocumentRoot216 if xhtml_DocumentRoot216 is not None else set()
        self.xhtml_DocumentRoot205 = xhtml_DocumentRoot205 if xhtml_DocumentRoot205 is not None else set()
        self.xhtml_DocumentRoot208 = xhtml_DocumentRoot208 if xhtml_DocumentRoot208 is not None else set()
        self.xhtml_DocumentRoot229 = xhtml_DocumentRoot229 if xhtml_DocumentRoot229 is not None else set()
        self.xhtml_DocumentRoot232 = xhtml_DocumentRoot232 if xhtml_DocumentRoot232 is not None else set()
        self.xhtml_DocumentRoot218 = xhtml_DocumentRoot218 if xhtml_DocumentRoot218 is not None else set()
        self.xhtml_DocumentRoot220 = xhtml_DocumentRoot220 if xhtml_DocumentRoot220 is not None else set()
        self.xhtml_DocumentRoot222 = xhtml_DocumentRoot222 if xhtml_DocumentRoot222 is not None else set()
        self.xhtml_DocumentRoot224 = xhtml_DocumentRoot224 if xhtml_DocumentRoot224 is not None else set()
        self.xhtml_DocumentRoot226 = xhtml_DocumentRoot226 if xhtml_DocumentRoot226 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xhtml_DocumentRoot178(self):
        return self.__xhtml_DocumentRoot178

    @xhtml_DocumentRoot178.setter
    def xhtml_DocumentRoot178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot178", None)
        self.__xhtml_DocumentRoot178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_MapType179"):
                    opp_val = getattr(item, "xhtml_MapType179", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_MapType179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_MapType179"):
                    opp_val = getattr(item, "xhtml_MapType179", None)
                    
                    setattr(item, "xhtml_MapType179", self)
                    

    @property
    def xhtml_DocumentRoot190(self):
        return self.__xhtml_DocumentRoot190

    @xhtml_DocumentRoot190.setter
    def xhtml_DocumentRoot190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot190", None)
        self.__xhtml_DocumentRoot190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType191"):
                    opp_val = getattr(item, "xhtml_QType191", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType191"):
                    opp_val = getattr(item, "xhtml_QType191", None)
                    
                    setattr(item, "xhtml_QType191", self)
                    

    @property
    def xhtml_DocumentRoot161(self):
        return self.__xhtml_DocumentRoot161

    @xhtml_DocumentRoot161.setter
    def xhtml_DocumentRoot161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot161", None)
        self.__xhtml_DocumentRoot161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type162"):
                    opp_val = getattr(item, "xhtml_H6Type162", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type162"):
                    opp_val = getattr(item, "xhtml_H6Type162", None)
                    
                    setattr(item, "xhtml_H6Type162", self)
                    

    @property
    def xhtml_DocumentRoot105(self):
        return self.__xhtml_DocumentRoot105

    @xhtml_DocumentRoot105.setter
    def xhtml_DocumentRoot105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot105", None)
        self.__xhtml_DocumentRoot105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType106"):
                    opp_val = getattr(item, "xhtml_BigType106", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType106"):
                    opp_val = getattr(item, "xhtml_BigType106", None)
                    
                    setattr(item, "xhtml_BigType106", self)
                    

    @property
    def xhtml_DocumentRoot184(self):
        return self.__xhtml_DocumentRoot184

    @xhtml_DocumentRoot184.setter
    def xhtml_DocumentRoot184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot184", None)
        self.__xhtml_DocumentRoot184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType185"):
                    opp_val = getattr(item, "xhtml_PType185", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType185"):
                    opp_val = getattr(item, "xhtml_PType185", None)
                    
                    setattr(item, "xhtml_PType185", self)
                    

    @property
    def xhtml_DocumentRoot173(self):
        return self.__xhtml_DocumentRoot173

    @xhtml_DocumentRoot173.setter
    def xhtml_DocumentRoot173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot173", None)
        self.__xhtml_DocumentRoot173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType174"):
                    opp_val = getattr(item, "xhtml_KbdType174", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType174"):
                    opp_val = getattr(item, "xhtml_KbdType174", None)
                    
                    setattr(item, "xhtml_KbdType174", self)
                    

    @property
    def xhtml_DocumentRoot149(self):
        return self.__xhtml_DocumentRoot149

    @xhtml_DocumentRoot149.setter
    def xhtml_DocumentRoot149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot149", None)
        self.__xhtml_DocumentRoot149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type150"):
                    opp_val = getattr(item, "xhtml_H2Type150", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type150"):
                    opp_val = getattr(item, "xhtml_H2Type150", None)
                    
                    setattr(item, "xhtml_H2Type150", self)
                    

    @property
    def xhtml_DocumentRoot216(self):
        return self.__xhtml_DocumentRoot216

    @xhtml_DocumentRoot216.setter
    def xhtml_DocumentRoot216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot216", None)
        self.__xhtml_DocumentRoot216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TdType"):
                    opp_val = getattr(item, "xhtml_TdType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TdType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TdType"):
                    opp_val = getattr(item, "xhtml_TdType", None)
                    
                    setattr(item, "xhtml_TdType", self)
                    

    @property
    def xhtml_DocumentRoot111(self):
        return self.__xhtml_DocumentRoot111

    @xhtml_DocumentRoot111.setter
    def xhtml_DocumentRoot111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot111", None)
        self.__xhtml_DocumentRoot111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType112"):
                    opp_val = getattr(item, "xhtml_BrType112", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType112"):
                    opp_val = getattr(item, "xhtml_BrType112", None)
                    
                    setattr(item, "xhtml_BrType112", self)
                    

    @property
    def xhtml_DocumentRoot202(self):
        return self.__xhtml_DocumentRoot202

    @xhtml_DocumentRoot202.setter
    def xhtml_DocumentRoot202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot202", None)
        self.__xhtml_DocumentRoot202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType203"):
                    opp_val = getattr(item, "xhtml_StrongType203", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType203"):
                    opp_val = getattr(item, "xhtml_StrongType203", None)
                    
                    setattr(item, "xhtml_StrongType203", self)
                    

    @property
    def xhtml_DocumentRoot119(self):
        return self.__xhtml_DocumentRoot119

    @xhtml_DocumentRoot119.setter
    def xhtml_DocumentRoot119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot119", None)
        self.__xhtml_DocumentRoot119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType120"):
                    opp_val = getattr(item, "xhtml_CodeType120", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType120"):
                    opp_val = getattr(item, "xhtml_CodeType120", None)
                    
                    setattr(item, "xhtml_CodeType120", self)
                    

    @property
    def xhtml_DocumentRoot158(self):
        return self.__xhtml_DocumentRoot158

    @xhtml_DocumentRoot158.setter
    def xhtml_DocumentRoot158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot158", None)
        self.__xhtml_DocumentRoot158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type159"):
                    opp_val = getattr(item, "xhtml_H5Type159", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type159"):
                    opp_val = getattr(item, "xhtml_H5Type159", None)
                    
                    setattr(item, "xhtml_H5Type159", self)
                    

    @property
    def xhtml_DocumentRoot218(self):
        return self.__xhtml_DocumentRoot218

    @xhtml_DocumentRoot218.setter
    def xhtml_DocumentRoot218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot218", None)
        self.__xhtml_DocumentRoot218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TfootType"):
                    opp_val = getattr(item, "xhtml_TfootType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TfootType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TfootType"):
                    opp_val = getattr(item, "xhtml_TfootType", None)
                    
                    setattr(item, "xhtml_TfootType", self)
                    

    @property
    def xhtml_DocumentRoot164(self):
        return self.__xhtml_DocumentRoot164

    @xhtml_DocumentRoot164.setter
    def xhtml_DocumentRoot164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot164", None)
        self.__xhtml_DocumentRoot164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType165"):
                    opp_val = getattr(item, "xhtml_HrType165", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType165"):
                    opp_val = getattr(item, "xhtml_HrType165", None)
                    
                    setattr(item, "xhtml_HrType165", self)
                    

    @property
    def xhtml_DocumentRoot224(self):
        return self.__xhtml_DocumentRoot224

    @xhtml_DocumentRoot224.setter
    def xhtml_DocumentRoot224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot224", None)
        self.__xhtml_DocumentRoot224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType"):
                    opp_val = getattr(item, "xhtml_TrType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType"):
                    opp_val = getattr(item, "xhtml_TrType", None)
                    
                    setattr(item, "xhtml_TrType", self)
                    

    @property
    def xhtml_DocumentRoot83(self):
        return self.__xhtml_DocumentRoot83

    @xhtml_DocumentRoot83.setter
    def xhtml_DocumentRoot83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot83", None)
        self.__xhtml_DocumentRoot83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EStringToStringMapEntry84"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry84", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EStringToStringMapEntry84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EStringToStringMapEntry84"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry84", None)
                    
                    setattr(item, "xhtml_EStringToStringMapEntry84", self)
                    

    @property
    def xhtml_DocumentRoot232(self):
        return self.__xhtml_DocumentRoot232

    @xhtml_DocumentRoot232.setter
    def xhtml_DocumentRoot232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot232", None)
        self.__xhtml_DocumentRoot232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType233"):
                    opp_val = getattr(item, "xhtml_VarType233", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType233", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType233"):
                    opp_val = getattr(item, "xhtml_VarType233", None)
                    
                    setattr(item, "xhtml_VarType233", self)
                    

    @property
    def xhtml_DocumentRoot97(self):
        return self.__xhtml_DocumentRoot97

    @xhtml_DocumentRoot97.setter
    def xhtml_DocumentRoot97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot97", None)
        self.__xhtml_DocumentRoot97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AreaType"):
                    opp_val = getattr(item, "xhtml_AreaType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AreaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AreaType"):
                    opp_val = getattr(item, "xhtml_AreaType", None)
                    
                    setattr(item, "xhtml_AreaType", self)
                    

    @property
    def xhtml_DocumentRoot108(self):
        return self.__xhtml_DocumentRoot108

    @xhtml_DocumentRoot108.setter
    def xhtml_DocumentRoot108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot108", None)
        self.__xhtml_DocumentRoot108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType109"):
                    opp_val = getattr(item, "xhtml_BlockquoteType109", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType109"):
                    opp_val = getattr(item, "xhtml_BlockquoteType109", None)
                    
                    setattr(item, "xhtml_BlockquoteType109", self)
                    

    @property
    def xhtml_DocumentRoot131(self):
        return self.__xhtml_DocumentRoot131

    @xhtml_DocumentRoot131.setter
    def xhtml_DocumentRoot131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot131", None)
        self.__xhtml_DocumentRoot131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType132"):
                    opp_val = getattr(item, "xhtml_DfnType132", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType132"):
                    opp_val = getattr(item, "xhtml_DfnType132", None)
                    
                    setattr(item, "xhtml_DfnType132", self)
                    

    @property
    def xhtml_DocumentRoot91(self):
        return self.__xhtml_DocumentRoot91

    @xhtml_DocumentRoot91.setter
    def xhtml_DocumentRoot91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot91", None)
        self.__xhtml_DocumentRoot91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType92"):
                    opp_val = getattr(item, "xhtml_AcronymType92", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType92"):
                    opp_val = getattr(item, "xhtml_AcronymType92", None)
                    
                    setattr(item, "xhtml_AcronymType92", self)
                    

    @property
    def xhtml_DocumentRoot226(self):
        return self.__xhtml_DocumentRoot226

    @xhtml_DocumentRoot226.setter
    def xhtml_DocumentRoot226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot226", None)
        self.__xhtml_DocumentRoot226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType227"):
                    opp_val = getattr(item, "xhtml_TtType227", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType227"):
                    opp_val = getattr(item, "xhtml_TtType227", None)
                    
                    setattr(item, "xhtml_TtType227", self)
                    

    @property
    def xhtml_DocumentRoot143(self):
        return self.__xhtml_DocumentRoot143

    @xhtml_DocumentRoot143.setter
    def xhtml_DocumentRoot143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot143", None)
        self.__xhtml_DocumentRoot143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType144"):
                    opp_val = getattr(item, "xhtml_EmType144", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType144"):
                    opp_val = getattr(item, "xhtml_EmType144", None)
                    
                    setattr(item, "xhtml_EmType144", self)
                    

    @property
    def xhtml_DocumentRoot146(self):
        return self.__xhtml_DocumentRoot146

    @xhtml_DocumentRoot146.setter
    def xhtml_DocumentRoot146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot146", None)
        self.__xhtml_DocumentRoot146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type147"):
                    opp_val = getattr(item, "xhtml_H1Type147", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type147"):
                    opp_val = getattr(item, "xhtml_H1Type147", None)
                    
                    setattr(item, "xhtml_H1Type147", self)
                    

    @property
    def xhtml_DocumentRoot176(self):
        return self.__xhtml_DocumentRoot176

    @xhtml_DocumentRoot176.setter
    def xhtml_DocumentRoot176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot176", None)
        self.__xhtml_DocumentRoot176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_LiType"):
                    opp_val = getattr(item, "xhtml_LiType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_LiType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_LiType"):
                    opp_val = getattr(item, "xhtml_LiType", None)
                    
                    setattr(item, "xhtml_LiType", self)
                    

    @property
    def xhtml_DocumentRoot222(self):
        return self.__xhtml_DocumentRoot222

    @xhtml_DocumentRoot222.setter
    def xhtml_DocumentRoot222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot222", None)
        self.__xhtml_DocumentRoot222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TheadType"):
                    opp_val = getattr(item, "xhtml_TheadType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TheadType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TheadType"):
                    opp_val = getattr(item, "xhtml_TheadType", None)
                    
                    setattr(item, "xhtml_TheadType", self)
                    

    @property
    def xhtml_DocumentRoot187(self):
        return self.__xhtml_DocumentRoot187

    @xhtml_DocumentRoot187.setter
    def xhtml_DocumentRoot187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot187", None)
        self.__xhtml_DocumentRoot187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType188"):
                    opp_val = getattr(item, "xhtml_PreType188", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType188"):
                    opp_val = getattr(item, "xhtml_PreType188", None)
                    
                    setattr(item, "xhtml_PreType188", self)
                    

    @property
    def xhtml_DocumentRoot88(self):
        return self.__xhtml_DocumentRoot88

    @xhtml_DocumentRoot88.setter
    def xhtml_DocumentRoot88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot88", None)
        self.__xhtml_DocumentRoot88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType89"):
                    opp_val = getattr(item, "xhtml_AbbrType89", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType89"):
                    opp_val = getattr(item, "xhtml_AbbrType89", None)
                    
                    setattr(item, "xhtml_AbbrType89", self)
                    

    @property
    def xhtml_DocumentRoot122(self):
        return self.__xhtml_DocumentRoot122

    @xhtml_DocumentRoot122.setter
    def xhtml_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot122", None)
        self.__xhtml_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColType123"):
                    opp_val = getattr(item, "xhtml_ColType123", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColType123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColType123"):
                    opp_val = getattr(item, "xhtml_ColType123", None)
                    
                    setattr(item, "xhtml_ColType123", self)
                    

    @property
    def xhtml_DocumentRoot205(self):
        return self.__xhtml_DocumentRoot205

    @xhtml_DocumentRoot205.setter
    def xhtml_DocumentRoot205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot205", None)
        self.__xhtml_DocumentRoot205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType206"):
                    opp_val = getattr(item, "xhtml_SubType206", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType206"):
                    opp_val = getattr(item, "xhtml_SubType206", None)
                    
                    setattr(item, "xhtml_SubType206", self)
                    

    @property
    def xhtml_DocumentRoot208(self):
        return self.__xhtml_DocumentRoot208

    @xhtml_DocumentRoot208.setter
    def xhtml_DocumentRoot208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot208", None)
        self.__xhtml_DocumentRoot208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType209"):
                    opp_val = getattr(item, "xhtml_SupType209", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType209"):
                    opp_val = getattr(item, "xhtml_SupType209", None)
                    
                    setattr(item, "xhtml_SupType209", self)
                    

    @property
    def xhtml_DocumentRoot94(self):
        return self.__xhtml_DocumentRoot94

    @xhtml_DocumentRoot94.setter
    def xhtml_DocumentRoot94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot94", None)
        self.__xhtml_DocumentRoot94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType95"):
                    opp_val = getattr(item, "xhtml_AddressType95", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType95"):
                    opp_val = getattr(item, "xhtml_AddressType95", None)
                    
                    setattr(item, "xhtml_AddressType95", self)
                    

    @property
    def xhtml_DocumentRoot152(self):
        return self.__xhtml_DocumentRoot152

    @xhtml_DocumentRoot152.setter
    def xhtml_DocumentRoot152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot152", None)
        self.__xhtml_DocumentRoot152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type153"):
                    opp_val = getattr(item, "xhtml_H3Type153", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type153"):
                    opp_val = getattr(item, "xhtml_H3Type153", None)
                    
                    setattr(item, "xhtml_H3Type153", self)
                    

    @property
    def xhtml_DocumentRoot199(self):
        return self.__xhtml_DocumentRoot199

    @xhtml_DocumentRoot199.setter
    def xhtml_DocumentRoot199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot199", None)
        self.__xhtml_DocumentRoot199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType200"):
                    opp_val = getattr(item, "xhtml_SpanType200", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType200"):
                    opp_val = getattr(item, "xhtml_SpanType200", None)
                    
                    setattr(item, "xhtml_SpanType200", self)
                    

    @property
    def xhtml_DocumentRoot220(self):
        return self.__xhtml_DocumentRoot220

    @xhtml_DocumentRoot220.setter
    def xhtml_DocumentRoot220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot220", None)
        self.__xhtml_DocumentRoot220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ThType"):
                    opp_val = getattr(item, "xhtml_ThType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ThType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ThType"):
                    opp_val = getattr(item, "xhtml_ThType", None)
                    
                    setattr(item, "xhtml_ThType", self)
                    

    @property
    def xhtml_DocumentRoot114(self):
        return self.__xhtml_DocumentRoot114

    @xhtml_DocumentRoot114.setter
    def xhtml_DocumentRoot114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot114", None)
        self.__xhtml_DocumentRoot114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CaptionType"):
                    opp_val = getattr(item, "xhtml_CaptionType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CaptionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CaptionType"):
                    opp_val = getattr(item, "xhtml_CaptionType", None)
                    
                    setattr(item, "xhtml_CaptionType", self)
                    

    @property
    def xhtml_DocumentRoot214(self):
        return self.__xhtml_DocumentRoot214

    @xhtml_DocumentRoot214.setter
    def xhtml_DocumentRoot214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot214", None)
        self.__xhtml_DocumentRoot214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TbodyType"):
                    opp_val = getattr(item, "xhtml_TbodyType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TbodyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TbodyType"):
                    opp_val = getattr(item, "xhtml_TbodyType", None)
                    
                    setattr(item, "xhtml_TbodyType", self)
                    

    @property
    def xhtml_DocumentRoot102(self):
        return self.__xhtml_DocumentRoot102

    @xhtml_DocumentRoot102.setter
    def xhtml_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot102", None)
        self.__xhtml_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BdoType103"):
                    opp_val = getattr(item, "xhtml_BdoType103", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BdoType103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BdoType103"):
                    opp_val = getattr(item, "xhtml_BdoType103", None)
                    
                    setattr(item, "xhtml_BdoType103", self)
                    

    @property
    def xhtml_DocumentRoot137(self):
        return self.__xhtml_DocumentRoot137

    @xhtml_DocumentRoot137.setter
    def xhtml_DocumentRoot137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot137", None)
        self.__xhtml_DocumentRoot137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType138"):
                    opp_val = getattr(item, "xhtml_DlType138", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType138"):
                    opp_val = getattr(item, "xhtml_DlType138", None)
                    
                    setattr(item, "xhtml_DlType138", self)
                    

    @property
    def xhtml_DocumentRoot86(self):
        return self.__xhtml_DocumentRoot86

    @xhtml_DocumentRoot86.setter
    def xhtml_DocumentRoot86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot86", None)
        self.__xhtml_DocumentRoot86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType"):
                    opp_val = getattr(item, "xhtml_AType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType"):
                    opp_val = getattr(item, "xhtml_AType", None)
                    
                    setattr(item, "xhtml_AType", self)
                    

    @property
    def xhtml_DocumentRoot155(self):
        return self.__xhtml_DocumentRoot155

    @xhtml_DocumentRoot155.setter
    def xhtml_DocumentRoot155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot155", None)
        self.__xhtml_DocumentRoot155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type156"):
                    opp_val = getattr(item, "xhtml_H4Type156", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type156"):
                    opp_val = getattr(item, "xhtml_H4Type156", None)
                    
                    setattr(item, "xhtml_H4Type156", self)
                    

    @property
    def xhtml_DocumentRoot125(self):
        return self.__xhtml_DocumentRoot125

    @xhtml_DocumentRoot125.setter
    def xhtml_DocumentRoot125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot125", None)
        self.__xhtml_DocumentRoot125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColgroupType126"):
                    opp_val = getattr(item, "xhtml_ColgroupType126", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColgroupType126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColgroupType126"):
                    opp_val = getattr(item, "xhtml_ColgroupType126", None)
                    
                    setattr(item, "xhtml_ColgroupType126", self)
                    

    @property
    def xhtml_DocumentRoot211(self):
        return self.__xhtml_DocumentRoot211

    @xhtml_DocumentRoot211.setter
    def xhtml_DocumentRoot211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot211", None)
        self.__xhtml_DocumentRoot211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType212"):
                    opp_val = getattr(item, "xhtml_TableType212", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType212"):
                    opp_val = getattr(item, "xhtml_TableType212", None)
                    
                    setattr(item, "xhtml_TableType212", self)
                    

    @property
    def xhtml_DocumentRoot181(self):
        return self.__xhtml_DocumentRoot181

    @xhtml_DocumentRoot181.setter
    def xhtml_DocumentRoot181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot181", None)
        self.__xhtml_DocumentRoot181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType182"):
                    opp_val = getattr(item, "xhtml_OlType182", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType182"):
                    opp_val = getattr(item, "xhtml_OlType182", None)
                    
                    setattr(item, "xhtml_OlType182", self)
                    

    @property
    def xhtml_DocumentRoot128(self):
        return self.__xhtml_DocumentRoot128

    @xhtml_DocumentRoot128.setter
    def xhtml_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot128", None)
        self.__xhtml_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DdType129"):
                    opp_val = getattr(item, "xhtml_DdType129", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DdType129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DdType129"):
                    opp_val = getattr(item, "xhtml_DdType129", None)
                    
                    setattr(item, "xhtml_DdType129", self)
                    

    @property
    def xhtml_DocumentRoot(self):
        return self.__xhtml_DocumentRoot

    @xhtml_DocumentRoot.setter
    def xhtml_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot", None)
        self.__xhtml_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry", None)
                    
                    setattr(item, "xhtml_EStringToStringMapEntry", self)
                    

    @property
    def xhtml_DocumentRoot167(self):
        return self.__xhtml_DocumentRoot167

    @xhtml_DocumentRoot167.setter
    def xhtml_DocumentRoot167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot167", None)
        self.__xhtml_DocumentRoot167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType168"):
                    opp_val = getattr(item, "xhtml_IType168", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType168"):
                    opp_val = getattr(item, "xhtml_IType168", None)
                    
                    setattr(item, "xhtml_IType168", self)
                    

    @property
    def xhtml_DocumentRoot116(self):
        return self.__xhtml_DocumentRoot116

    @xhtml_DocumentRoot116.setter
    def xhtml_DocumentRoot116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot116", None)
        self.__xhtml_DocumentRoot116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType117"):
                    opp_val = getattr(item, "xhtml_CiteType117", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType117"):
                    opp_val = getattr(item, "xhtml_CiteType117", None)
                    
                    setattr(item, "xhtml_CiteType117", self)
                    

    @property
    def xhtml_DocumentRoot134(self):
        return self.__xhtml_DocumentRoot134

    @xhtml_DocumentRoot134.setter
    def xhtml_DocumentRoot134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot134", None)
        self.__xhtml_DocumentRoot134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType135"):
                    opp_val = getattr(item, "xhtml_DivType135", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType135"):
                    opp_val = getattr(item, "xhtml_DivType135", None)
                    
                    setattr(item, "xhtml_DivType135", self)
                    

    @property
    def xhtml_DocumentRoot229(self):
        return self.__xhtml_DocumentRoot229

    @xhtml_DocumentRoot229.setter
    def xhtml_DocumentRoot229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot229", None)
        self.__xhtml_DocumentRoot229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType230"):
                    opp_val = getattr(item, "xhtml_UlType230", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType230"):
                    opp_val = getattr(item, "xhtml_UlType230", None)
                    
                    setattr(item, "xhtml_UlType230", self)
                    

    @property
    def xhtml_DocumentRoot140(self):
        return self.__xhtml_DocumentRoot140

    @xhtml_DocumentRoot140.setter
    def xhtml_DocumentRoot140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot140", None)
        self.__xhtml_DocumentRoot140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DtType141"):
                    opp_val = getattr(item, "xhtml_DtType141", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DtType141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DtType141"):
                    opp_val = getattr(item, "xhtml_DtType141", None)
                    
                    setattr(item, "xhtml_DtType141", self)
                    

    @property
    def xhtml_DocumentRoot99(self):
        return self.__xhtml_DocumentRoot99

    @xhtml_DocumentRoot99.setter
    def xhtml_DocumentRoot99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot99", None)
        self.__xhtml_DocumentRoot99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType100"):
                    opp_val = getattr(item, "xhtml_BType100", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType100"):
                    opp_val = getattr(item, "xhtml_BType100", None)
                    
                    setattr(item, "xhtml_BType100", self)
                    

    @property
    def xhtml_DocumentRoot193(self):
        return self.__xhtml_DocumentRoot193

    @xhtml_DocumentRoot193.setter
    def xhtml_DocumentRoot193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot193", None)
        self.__xhtml_DocumentRoot193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType194"):
                    opp_val = getattr(item, "xhtml_SampType194", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType194"):
                    opp_val = getattr(item, "xhtml_SampType194", None)
                    
                    setattr(item, "xhtml_SampType194", self)
                    

    @property
    def xhtml_DocumentRoot196(self):
        return self.__xhtml_DocumentRoot196

    @xhtml_DocumentRoot196.setter
    def xhtml_DocumentRoot196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot196", None)
        self.__xhtml_DocumentRoot196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType197"):
                    opp_val = getattr(item, "xhtml_SmallType197", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType197"):
                    opp_val = getattr(item, "xhtml_SmallType197", None)
                    
                    setattr(item, "xhtml_SmallType197", self)
                    

    @property
    def xhtml_DocumentRoot170(self):
        return self.__xhtml_DocumentRoot170

    @xhtml_DocumentRoot170.setter
    def xhtml_DocumentRoot170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot170", None)
        self.__xhtml_DocumentRoot170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType171"):
                    opp_val = getattr(item, "xhtml_ImgType171", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType171"):
                    opp_val = getattr(item, "xhtml_ImgType171", None)
                    
                    setattr(item, "xhtml_ImgType171", self)
                    

class Flow:

    pass
class xhtml_LiType(Flow):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_LiType: "xhtml_DocumentRoot" = None, xhtml_LiType477: "xhtml_OlType" = None, xhtml_LiType584: "xhtml_UlType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_LiType = xhtml_LiType
        self.xhtml_LiType477 = xhtml_LiType477
        self.xhtml_LiType584 = xhtml_LiType584
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_LiType584(self):
        return self.__xhtml_LiType584

    @xhtml_LiType584.setter
    def xhtml_LiType584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_LiType__xhtml_LiType584", None)
        self.__xhtml_LiType584 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_UlType583"):
                opp_val = getattr(old_value, "xhtml_UlType583", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_UlType583"):
                opp_val = getattr(value, "xhtml_UlType583", None)
                if opp_val is None:
                    setattr(value, "xhtml_UlType583", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_LiType477(self):
        return self.__xhtml_LiType477

    @xhtml_LiType477.setter
    def xhtml_LiType477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_LiType__xhtml_LiType477", None)
        self.__xhtml_LiType477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_OlType476"):
                opp_val = getattr(old_value, "xhtml_OlType476", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_OlType476"):
                opp_val = getattr(value, "xhtml_OlType476", None)
                if opp_val is None:
                    setattr(value, "xhtml_OlType476", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_LiType(self):
        return self.__xhtml_LiType

    @xhtml_LiType.setter
    def xhtml_LiType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_LiType__xhtml_LiType", None)
        self.__xhtml_LiType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot176"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot176"):
                opp_val = getattr(value, "xhtml_DocumentRoot176", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ThType(Flow):

    def __init__(self, abbr1: str, align: str, axis: str, char: str, charoff: str, class: str, dir: str, headers: str, id: str, lang: str, lang1: str, rowspan: str, scope: str, style: str, title: str, valign: str, colspan: str, xhtml_ThType: "xhtml_DocumentRoot" = None, xhtml_ThType578: "xhtml_TrType" = None):
        self.abbr1 = abbr1
        self.align = align
        self.axis = axis
        self.char = char
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.headers = headers
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.rowspan = rowspan
        self.scope = scope
        self.style = style
        self.title = title
        self.valign = valign
        self.colspan = colspan
        self.xhtml_ThType = xhtml_ThType
        self.xhtml_ThType578 = xhtml_ThType578
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def abbr1(self) -> str:
        return self.__abbr1

    @abbr1.setter
    def abbr1(self, abbr1: str):
        self.__abbr1 = abbr1

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def headers(self) -> str:
        return self.__headers

    @headers.setter
    def headers(self, headers: str):
        self.__headers = headers

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def axis(self) -> str:
        return self.__axis

    @axis.setter
    def axis(self, axis: str):
        self.__axis = axis

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def xhtml_ThType(self):
        return self.__xhtml_ThType

    @xhtml_ThType.setter
    def xhtml_ThType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ThType__xhtml_ThType", None)
        self.__xhtml_ThType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot220"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot220"):
                opp_val = getattr(value, "xhtml_DocumentRoot220", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ThType578(self):
        return self.__xhtml_ThType578

    @xhtml_ThType578.setter
    def xhtml_ThType578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ThType__xhtml_ThType578", None)
        self.__xhtml_ThType578 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TrType577"):
                opp_val = getattr(old_value, "xhtml_TrType577", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TrType577"):
                opp_val = getattr(value, "xhtml_TrType577", None)
                if opp_val is None:
                    setattr(value, "xhtml_TrType577", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TdType(Flow):

    def __init__(self, abbr1: str, align: str, axis: str, char: str, charoff: str, class: str, colspan: str, dir: str, headers: str, id: str, lang: str, lang1: str, rowspan: str, scope: str, style: str, title: str, valign: str, xhtml_TdType: "xhtml_DocumentRoot" = None, xhtml_TdType581: "xhtml_TrType" = None):
        self.abbr1 = abbr1
        self.align = align
        self.axis = axis
        self.char = char
        self.charoff = charoff
        self.class = class
        self.colspan = colspan
        self.dir = dir
        self.headers = headers
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.rowspan = rowspan
        self.scope = scope
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TdType = xhtml_TdType
        self.xhtml_TdType581 = xhtml_TdType581
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def abbr1(self) -> str:
        return self.__abbr1

    @abbr1.setter
    def abbr1(self, abbr1: str):
        self.__abbr1 = abbr1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def headers(self) -> str:
        return self.__headers

    @headers.setter
    def headers(self, headers: str):
        self.__headers = headers

    @property
    def axis(self) -> str:
        return self.__axis

    @axis.setter
    def axis(self, axis: str):
        self.__axis = axis

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_TdType581(self):
        return self.__xhtml_TdType581

    @xhtml_TdType581.setter
    def xhtml_TdType581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TdType__xhtml_TdType581", None)
        self.__xhtml_TdType581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TrType580"):
                opp_val = getattr(old_value, "xhtml_TrType580", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TrType580"):
                opp_val = getattr(value, "xhtml_TrType580", None)
                if opp_val is None:
                    setattr(value, "xhtml_TrType580", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TdType(self):
        return self.__xhtml_TdType

    @xhtml_TdType.setter
    def xhtml_TdType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TdType__xhtml_TdType", None)
        self.__xhtml_TdType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot216"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot216"):
                opp_val = getattr(value, "xhtml_DocumentRoot216", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DdType(Flow):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_DdType: "xhtml_DlType" = None, xhtml_DdType129: "xhtml_DocumentRoot" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_DdType = xhtml_DdType
        self.xhtml_DdType129 = xhtml_DdType129
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_DdType(self):
        return self.__xhtml_DdType

    @xhtml_DdType.setter
    def xhtml_DdType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DdType__xhtml_DdType", None)
        self.__xhtml_DdType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DlType80"):
                opp_val = getattr(old_value, "xhtml_DlType80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DlType80"):
                opp_val = getattr(value, "xhtml_DlType80", None)
                if opp_val is None:
                    setattr(value, "xhtml_DlType80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DdType129(self):
        return self.__xhtml_DdType129

    @xhtml_DdType129.setter
    def xhtml_DdType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DdType__xhtml_DdType129", None)
        self.__xhtml_DdType129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot128"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot128"):
                opp_val = getattr(value, "xhtml_DocumentRoot128", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ColType:

    def __init__(self, align: str, char: str, charoff: str, class: str, dir: str, id: str, lang: str, lang1: str, span: str, style: str, title: str, valign: str, width: str, xhtml_ColType: "xhtml_ColgroupType" = None, xhtml_ColType123: "xhtml_DocumentRoot" = None, xhtml_ColType551: "xhtml_TableType" = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.span = span
        self.style = style
        self.title = title
        self.valign = valign
        self.width = width
        self.xhtml_ColType = xhtml_ColType
        self.xhtml_ColType123 = xhtml_ColType123
        self.xhtml_ColType551 = xhtml_ColType551
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_ColType551(self):
        return self.__xhtml_ColType551

    @xhtml_ColType551.setter
    def xhtml_ColType551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColType__xhtml_ColType551", None)
        self.__xhtml_ColType551 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType550"):
                opp_val = getattr(old_value, "xhtml_TableType550", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType550"):
                opp_val = getattr(value, "xhtml_TableType550", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType550", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ColType(self):
        return self.__xhtml_ColType

    @xhtml_ColType.setter
    def xhtml_ColType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColType__xhtml_ColType", None)
        self.__xhtml_ColType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ColgroupType"):
                opp_val = getattr(old_value, "xhtml_ColgroupType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ColgroupType"):
                opp_val = getattr(value, "xhtml_ColgroupType", None)
                if opp_val is None:
                    setattr(value, "xhtml_ColgroupType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ColType123(self):
        return self.__xhtml_ColType123

    @xhtml_ColType123.setter
    def xhtml_ColType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColType__xhtml_ColType123", None)
        self.__xhtml_ColType123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot122"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot122"):
                opp_val = getattr(value, "xhtml_DocumentRoot122", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ColgroupType:

    def __init__(self, align: str, width: str, char: str, charoff: str, class: str, dir: str, id: str, lang: str, lang1: str, span: str, style: str, title: str, valign: str, xhtml_ColgroupType: set["xhtml_ColType"] = None, xhtml_ColgroupType126: "xhtml_DocumentRoot" = None, xhtml_ColgroupType554: "xhtml_TableType" = None):
        self.align = align
        self.width = width
        self.char = char
        self.charoff = charoff
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.span = span
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_ColgroupType = xhtml_ColgroupType if xhtml_ColgroupType is not None else set()
        self.xhtml_ColgroupType126 = xhtml_ColgroupType126
        self.xhtml_ColgroupType554 = xhtml_ColgroupType554
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_ColgroupType(self):
        return self.__xhtml_ColgroupType

    @xhtml_ColgroupType.setter
    def xhtml_ColgroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColgroupType__xhtml_ColgroupType", None)
        self.__xhtml_ColgroupType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColType"):
                    opp_val = getattr(item, "xhtml_ColType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColType"):
                    opp_val = getattr(item, "xhtml_ColType", None)
                    
                    setattr(item, "xhtml_ColType", self)
                    

    @property
    def xhtml_ColgroupType126(self):
        return self.__xhtml_ColgroupType126

    @xhtml_ColgroupType126.setter
    def xhtml_ColgroupType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColgroupType__xhtml_ColgroupType126", None)
        self.__xhtml_ColgroupType126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot125"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot125"):
                opp_val = getattr(value, "xhtml_DocumentRoot125", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ColgroupType554(self):
        return self.__xhtml_ColgroupType554

    @xhtml_ColgroupType554.setter
    def xhtml_ColgroupType554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColgroupType__xhtml_ColgroupType554", None)
        self.__xhtml_ColgroupType554 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType553"):
                opp_val = getattr(old_value, "xhtml_TableType553", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType553"):
                opp_val = getattr(value, "xhtml_TableType553", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType553", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Block:

    pass
class xhtml_TableType:

    def __init__(self, border: str, cellpadding: str, cellspacing: str, class: str, dir: str, id: str, lang: str, lang1: str, rules: str, style: str, summary: str, title: str, width: str, frame: str, xhtml_TableType: "xhtml_Block" = None, xhtml_TableType212: "xhtml_DocumentRoot" = None, xhtml_TableType280: "xhtml_Flow" = None, xhtml_TableType471: "xhtml_MapType" = None, xhtml_TableType547: "xhtml_CaptionType" = None, xhtml_TableType550: set["xhtml_ColType"] = None, xhtml_TableType553: set["xhtml_ColgroupType"] = None, xhtml_TableType556: "xhtml_TheadType" = None, xhtml_TableType559: "xhtml_TfootType" = None, xhtml_TableType562: set["xhtml_TbodyType"] = None, xhtml_TableType565: set["xhtml_TrType"] = None):
        self.border = border
        self.cellpadding = cellpadding
        self.cellspacing = cellspacing
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.rules = rules
        self.style = style
        self.summary = summary
        self.title = title
        self.width = width
        self.frame = frame
        self.xhtml_TableType = xhtml_TableType
        self.xhtml_TableType212 = xhtml_TableType212
        self.xhtml_TableType280 = xhtml_TableType280
        self.xhtml_TableType471 = xhtml_TableType471
        self.xhtml_TableType547 = xhtml_TableType547
        self.xhtml_TableType550 = xhtml_TableType550 if xhtml_TableType550 is not None else set()
        self.xhtml_TableType553 = xhtml_TableType553 if xhtml_TableType553 is not None else set()
        self.xhtml_TableType556 = xhtml_TableType556
        self.xhtml_TableType559 = xhtml_TableType559
        self.xhtml_TableType562 = xhtml_TableType562 if xhtml_TableType562 is not None else set()
        self.xhtml_TableType565 = xhtml_TableType565 if xhtml_TableType565 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def frame(self) -> str:
        return self.__frame

    @frame.setter
    def frame(self, frame: str):
        self.__frame = frame

    @property
    def cellpadding(self) -> str:
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def xhtml_TableType559(self):
        return self.__xhtml_TableType559

    @xhtml_TableType559.setter
    def xhtml_TableType559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType559", None)
        self.__xhtml_TableType559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TfootType560"):
                opp_val = getattr(old_value, "xhtml_TfootType560", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TfootType560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TfootType560"):
                opp_val = getattr(value, "xhtml_TfootType560", None)
                setattr(value, "xhtml_TfootType560", self)

    @property
    def xhtml_TableType550(self):
        return self.__xhtml_TableType550

    @xhtml_TableType550.setter
    def xhtml_TableType550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType550", None)
        self.__xhtml_TableType550 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColType551"):
                    opp_val = getattr(item, "xhtml_ColType551", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColType551", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColType551"):
                    opp_val = getattr(item, "xhtml_ColType551", None)
                    
                    setattr(item, "xhtml_ColType551", self)
                    

    @property
    def xhtml_TableType562(self):
        return self.__xhtml_TableType562

    @xhtml_TableType562.setter
    def xhtml_TableType562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType562", None)
        self.__xhtml_TableType562 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TbodyType563"):
                    opp_val = getattr(item, "xhtml_TbodyType563", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TbodyType563", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TbodyType563"):
                    opp_val = getattr(item, "xhtml_TbodyType563", None)
                    
                    setattr(item, "xhtml_TbodyType563", self)
                    

    @property
    def xhtml_TableType565(self):
        return self.__xhtml_TableType565

    @xhtml_TableType565.setter
    def xhtml_TableType565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType565", None)
        self.__xhtml_TableType565 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType566"):
                    opp_val = getattr(item, "xhtml_TrType566", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType566", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType566"):
                    opp_val = getattr(item, "xhtml_TrType566", None)
                    
                    setattr(item, "xhtml_TrType566", self)
                    

    @property
    def xhtml_TableType212(self):
        return self.__xhtml_TableType212

    @xhtml_TableType212.setter
    def xhtml_TableType212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType212", None)
        self.__xhtml_TableType212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot211"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot211"):
                opp_val = getattr(value, "xhtml_DocumentRoot211", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType471(self):
        return self.__xhtml_TableType471

    @xhtml_TableType471.setter
    def xhtml_TableType471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType471", None)
        self.__xhtml_TableType471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType470"):
                opp_val = getattr(old_value, "xhtml_MapType470", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType470"):
                opp_val = getattr(value, "xhtml_MapType470", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType470", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType547(self):
        return self.__xhtml_TableType547

    @xhtml_TableType547.setter
    def xhtml_TableType547(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType547", None)
        self.__xhtml_TableType547 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_CaptionType548"):
                opp_val = getattr(old_value, "xhtml_CaptionType548", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_CaptionType548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_CaptionType548"):
                opp_val = getattr(value, "xhtml_CaptionType548", None)
                setattr(value, "xhtml_CaptionType548", self)

    @property
    def xhtml_TableType556(self):
        return self.__xhtml_TableType556

    @xhtml_TableType556.setter
    def xhtml_TableType556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType556", None)
        self.__xhtml_TableType556 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TheadType557"):
                opp_val = getattr(old_value, "xhtml_TheadType557", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TheadType557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TheadType557"):
                opp_val = getattr(value, "xhtml_TheadType557", None)
                setattr(value, "xhtml_TheadType557", self)

    @property
    def xhtml_TableType553(self):
        return self.__xhtml_TableType553

    @xhtml_TableType553.setter
    def xhtml_TableType553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType553", None)
        self.__xhtml_TableType553 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColgroupType554"):
                    opp_val = getattr(item, "xhtml_ColgroupType554", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColgroupType554", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColgroupType554"):
                    opp_val = getattr(item, "xhtml_ColgroupType554", None)
                    
                    setattr(item, "xhtml_ColgroupType554", self)
                    

    @property
    def xhtml_TableType(self):
        return self.__xhtml_TableType

    @xhtml_TableType.setter
    def xhtml_TableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType", None)
        self.__xhtml_TableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block75"):
                opp_val = getattr(old_value, "xhtml_Block75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block75"):
                opp_val = getattr(value, "xhtml_Block75", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType280(self):
        return self.__xhtml_TableType280

    @xhtml_TableType280.setter
    def xhtml_TableType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType280", None)
        self.__xhtml_TableType280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow279"):
                opp_val = getattr(old_value, "xhtml_Flow279", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow279"):
                opp_val = getattr(value, "xhtml_Flow279", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow279", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_PreType(PreContent):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, space: str, style: str, title: str, xhtml_PreType: "xhtml_Block" = None, xhtml_PreType188: "xhtml_DocumentRoot" = None, xhtml_PreType268: "xhtml_Flow" = None, xhtml_PreType459: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.space = space
        self.style = style
        self.title = title
        self.xhtml_PreType = xhtml_PreType
        self.xhtml_PreType188 = xhtml_PreType188
        self.xhtml_PreType268 = xhtml_PreType268
        self.xhtml_PreType459 = xhtml_PreType459
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def space(self) -> str:
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_PreType459(self):
        return self.__xhtml_PreType459

    @xhtml_PreType459.setter
    def xhtml_PreType459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType459", None)
        self.__xhtml_PreType459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType458"):
                opp_val = getattr(old_value, "xhtml_MapType458", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType458"):
                opp_val = getattr(value, "xhtml_MapType458", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType458", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType268(self):
        return self.__xhtml_PreType268

    @xhtml_PreType268.setter
    def xhtml_PreType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType268", None)
        self.__xhtml_PreType268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow267"):
                opp_val = getattr(old_value, "xhtml_Flow267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow267"):
                opp_val = getattr(value, "xhtml_Flow267", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType(self):
        return self.__xhtml_PreType

    @xhtml_PreType.setter
    def xhtml_PreType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType", None)
        self.__xhtml_PreType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block67"):
                opp_val = getattr(old_value, "xhtml_Block67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block67"):
                opp_val = getattr(value, "xhtml_Block67", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType188(self):
        return self.__xhtml_PreType188

    @xhtml_PreType188.setter
    def xhtml_PreType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType188", None)
        self.__xhtml_PreType188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot187"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot187"):
                opp_val = getattr(value, "xhtml_DocumentRoot187", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DlType:

    def __init__(self, dir: str, id: str, lang: str, lang1: str, style: str, title: str, group: str, class: str, xhtml_DlType: "xhtml_Block" = None, xhtml_DlType78: set["xhtml_DtType"] = None, xhtml_DlType80: set["xhtml_DdType"] = None, xhtml_DlType138: "xhtml_DocumentRoot" = None, xhtml_DlType265: "xhtml_Flow" = None, xhtml_DlType456: "xhtml_MapType" = None):
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.group = group
        self.class = class
        self.xhtml_DlType = xhtml_DlType
        self.xhtml_DlType78 = xhtml_DlType78 if xhtml_DlType78 is not None else set()
        self.xhtml_DlType80 = xhtml_DlType80 if xhtml_DlType80 is not None else set()
        self.xhtml_DlType138 = xhtml_DlType138
        self.xhtml_DlType265 = xhtml_DlType265
        self.xhtml_DlType456 = xhtml_DlType456
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_DlType78(self):
        return self.__xhtml_DlType78

    @xhtml_DlType78.setter
    def xhtml_DlType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType78", None)
        self.__xhtml_DlType78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DtType"):
                    opp_val = getattr(item, "xhtml_DtType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DtType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DtType"):
                    opp_val = getattr(item, "xhtml_DtType", None)
                    
                    setattr(item, "xhtml_DtType", self)
                    

    @property
    def xhtml_DlType80(self):
        return self.__xhtml_DlType80

    @xhtml_DlType80.setter
    def xhtml_DlType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType80", None)
        self.__xhtml_DlType80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DdType"):
                    opp_val = getattr(item, "xhtml_DdType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DdType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DdType"):
                    opp_val = getattr(item, "xhtml_DdType", None)
                    
                    setattr(item, "xhtml_DdType", self)
                    

    @property
    def xhtml_DlType(self):
        return self.__xhtml_DlType

    @xhtml_DlType.setter
    def xhtml_DlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType", None)
        self.__xhtml_DlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block65"):
                opp_val = getattr(old_value, "xhtml_Block65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block65"):
                opp_val = getattr(value, "xhtml_Block65", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DlType456(self):
        return self.__xhtml_DlType456

    @xhtml_DlType456.setter
    def xhtml_DlType456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType456", None)
        self.__xhtml_DlType456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType455"):
                opp_val = getattr(old_value, "xhtml_MapType455", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType455"):
                opp_val = getattr(value, "xhtml_MapType455", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType455", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DlType265(self):
        return self.__xhtml_DlType265

    @xhtml_DlType265.setter
    def xhtml_DlType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType265", None)
        self.__xhtml_DlType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow264"):
                opp_val = getattr(old_value, "xhtml_Flow264", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow264"):
                opp_val = getattr(value, "xhtml_Flow264", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow264", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DlType138(self):
        return self.__xhtml_DlType138

    @xhtml_DlType138.setter
    def xhtml_DlType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType138", None)
        self.__xhtml_DlType138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot137"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot137"):
                opp_val = getattr(value, "xhtml_DocumentRoot137", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BlockquoteType(Block):

    def __init__(self, style: str, title: str, cite: str, class: str, dir: str, id: str, lang: str, lang1: str, xhtml_BlockquoteType: "xhtml_Block" = None, xhtml_BlockquoteType109: "xhtml_DocumentRoot" = None, xhtml_BlockquoteType274: "xhtml_Flow" = None, xhtml_BlockquoteType465: "xhtml_MapType" = None):
        self.style = style
        self.title = title
        self.cite = cite
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.xhtml_BlockquoteType = xhtml_BlockquoteType
        self.xhtml_BlockquoteType109 = xhtml_BlockquoteType109
        self.xhtml_BlockquoteType274 = xhtml_BlockquoteType274
        self.xhtml_BlockquoteType465 = xhtml_BlockquoteType465
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def cite(self) -> str:
        return self.__cite

    @cite.setter
    def cite(self, cite: str):
        self.__cite = cite

    @property
    def xhtml_BlockquoteType274(self):
        return self.__xhtml_BlockquoteType274

    @xhtml_BlockquoteType274.setter
    def xhtml_BlockquoteType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType274", None)
        self.__xhtml_BlockquoteType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow273"):
                opp_val = getattr(old_value, "xhtml_Flow273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow273"):
                opp_val = getattr(value, "xhtml_Flow273", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType109(self):
        return self.__xhtml_BlockquoteType109

    @xhtml_BlockquoteType109.setter
    def xhtml_BlockquoteType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType109", None)
        self.__xhtml_BlockquoteType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot108"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot108"):
                opp_val = getattr(value, "xhtml_DocumentRoot108", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType465(self):
        return self.__xhtml_BlockquoteType465

    @xhtml_BlockquoteType465.setter
    def xhtml_BlockquoteType465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType465", None)
        self.__xhtml_BlockquoteType465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType464"):
                opp_val = getattr(old_value, "xhtml_MapType464", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType464"):
                opp_val = getattr(value, "xhtml_MapType464", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType464", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType(self):
        return self.__xhtml_BlockquoteType

    @xhtml_BlockquoteType.setter
    def xhtml_BlockquoteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType", None)
        self.__xhtml_BlockquoteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block71"):
                opp_val = getattr(old_value, "xhtml_Block71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block71"):
                opp_val = getattr(value, "xhtml_Block71", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_HrType:

    def __init__(self, dir: str, id: str, lang: str, lang1: str, style: str, title: str, class: str, xhtml_HrType: "xhtml_Block" = None, xhtml_HrType165: "xhtml_DocumentRoot" = None, xhtml_HrType271: "xhtml_Flow" = None, xhtml_HrType462: "xhtml_MapType" = None):
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_HrType = xhtml_HrType
        self.xhtml_HrType165 = xhtml_HrType165
        self.xhtml_HrType271 = xhtml_HrType271
        self.xhtml_HrType462 = xhtml_HrType462
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_HrType(self):
        return self.__xhtml_HrType

    @xhtml_HrType.setter
    def xhtml_HrType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType", None)
        self.__xhtml_HrType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block69"):
                opp_val = getattr(old_value, "xhtml_Block69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block69"):
                opp_val = getattr(value, "xhtml_Block69", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_HrType462(self):
        return self.__xhtml_HrType462

    @xhtml_HrType462.setter
    def xhtml_HrType462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType462", None)
        self.__xhtml_HrType462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType461"):
                opp_val = getattr(old_value, "xhtml_MapType461", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType461"):
                opp_val = getattr(value, "xhtml_MapType461", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType461", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_HrType165(self):
        return self.__xhtml_HrType165

    @xhtml_HrType165.setter
    def xhtml_HrType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType165", None)
        self.__xhtml_HrType165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot164"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot164"):
                opp_val = getattr(value, "xhtml_DocumentRoot164", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_HrType271(self):
        return self.__xhtml_HrType271

    @xhtml_HrType271.setter
    def xhtml_HrType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType271", None)
        self.__xhtml_HrType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow270"):
                opp_val = getattr(old_value, "xhtml_Flow270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow270"):
                opp_val = getattr(value, "xhtml_Flow270", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_OlType:

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_OlType: "xhtml_Block" = None, xhtml_OlType182: "xhtml_DocumentRoot" = None, xhtml_OlType262: "xhtml_Flow" = None, xhtml_OlType453: "xhtml_MapType" = None, xhtml_OlType476: set["xhtml_LiType"] = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_OlType = xhtml_OlType
        self.xhtml_OlType182 = xhtml_OlType182
        self.xhtml_OlType262 = xhtml_OlType262
        self.xhtml_OlType453 = xhtml_OlType453
        self.xhtml_OlType476 = xhtml_OlType476 if xhtml_OlType476 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_OlType(self):
        return self.__xhtml_OlType

    @xhtml_OlType.setter
    def xhtml_OlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType", None)
        self.__xhtml_OlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block63"):
                opp_val = getattr(old_value, "xhtml_Block63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block63"):
                opp_val = getattr(value, "xhtml_Block63", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType262(self):
        return self.__xhtml_OlType262

    @xhtml_OlType262.setter
    def xhtml_OlType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType262", None)
        self.__xhtml_OlType262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow261"):
                opp_val = getattr(old_value, "xhtml_Flow261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow261"):
                opp_val = getattr(value, "xhtml_Flow261", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType453(self):
        return self.__xhtml_OlType453

    @xhtml_OlType453.setter
    def xhtml_OlType453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType453", None)
        self.__xhtml_OlType453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType452"):
                opp_val = getattr(old_value, "xhtml_MapType452", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType452"):
                opp_val = getattr(value, "xhtml_MapType452", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType452", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType476(self):
        return self.__xhtml_OlType476

    @xhtml_OlType476.setter
    def xhtml_OlType476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType476", None)
        self.__xhtml_OlType476 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_LiType477"):
                    opp_val = getattr(item, "xhtml_LiType477", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_LiType477", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_LiType477"):
                    opp_val = getattr(item, "xhtml_LiType477", None)
                    
                    setattr(item, "xhtml_LiType477", self)
                    

    @property
    def xhtml_OlType182(self):
        return self.__xhtml_OlType182

    @xhtml_OlType182.setter
    def xhtml_OlType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType182", None)
        self.__xhtml_OlType182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot181"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot181"):
                opp_val = getattr(value, "xhtml_DocumentRoot181", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_UlType:

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_UlType: "xhtml_Block" = None, xhtml_UlType230: "xhtml_DocumentRoot" = None, xhtml_UlType259: "xhtml_Flow" = None, xhtml_UlType450: "xhtml_MapType" = None, xhtml_UlType583: set["xhtml_LiType"] = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_UlType = xhtml_UlType
        self.xhtml_UlType230 = xhtml_UlType230
        self.xhtml_UlType259 = xhtml_UlType259
        self.xhtml_UlType450 = xhtml_UlType450
        self.xhtml_UlType583 = xhtml_UlType583 if xhtml_UlType583 is not None else set()
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_UlType(self):
        return self.__xhtml_UlType

    @xhtml_UlType.setter
    def xhtml_UlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType", None)
        self.__xhtml_UlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block61"):
                opp_val = getattr(old_value, "xhtml_Block61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block61"):
                opp_val = getattr(value, "xhtml_Block61", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UlType583(self):
        return self.__xhtml_UlType583

    @xhtml_UlType583.setter
    def xhtml_UlType583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType583", None)
        self.__xhtml_UlType583 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_LiType584"):
                    opp_val = getattr(item, "xhtml_LiType584", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_LiType584", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_LiType584"):
                    opp_val = getattr(item, "xhtml_LiType584", None)
                    
                    setattr(item, "xhtml_LiType584", self)
                    

    @property
    def xhtml_UlType259(self):
        return self.__xhtml_UlType259

    @xhtml_UlType259.setter
    def xhtml_UlType259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType259", None)
        self.__xhtml_UlType259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow258"):
                opp_val = getattr(old_value, "xhtml_Flow258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow258"):
                opp_val = getattr(value, "xhtml_Flow258", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UlType450(self):
        return self.__xhtml_UlType450

    @xhtml_UlType450.setter
    def xhtml_UlType450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType450", None)
        self.__xhtml_UlType450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType449"):
                opp_val = getattr(old_value, "xhtml_MapType449", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType449"):
                opp_val = getattr(value, "xhtml_MapType449", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType449", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UlType230(self):
        return self.__xhtml_UlType230

    @xhtml_UlType230.setter
    def xhtml_UlType230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType230", None)
        self.__xhtml_UlType230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot229"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot229", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot229"):
                opp_val = getattr(value, "xhtml_DocumentRoot229", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot229", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DivType(Flow):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_DivType: "xhtml_Block" = None, xhtml_DivType135: "xhtml_DocumentRoot" = None, xhtml_DivType256: "xhtml_Flow" = None, xhtml_DivType447: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_DivType = xhtml_DivType
        self.xhtml_DivType135 = xhtml_DivType135
        self.xhtml_DivType256 = xhtml_DivType256
        self.xhtml_DivType447 = xhtml_DivType447
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_DivType135(self):
        return self.__xhtml_DivType135

    @xhtml_DivType135.setter
    def xhtml_DivType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType135", None)
        self.__xhtml_DivType135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot134"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot134"):
                opp_val = getattr(value, "xhtml_DocumentRoot134", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DivType(self):
        return self.__xhtml_DivType

    @xhtml_DivType.setter
    def xhtml_DivType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType", None)
        self.__xhtml_DivType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block59"):
                opp_val = getattr(old_value, "xhtml_Block59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block59"):
                opp_val = getattr(value, "xhtml_Block59", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DivType447(self):
        return self.__xhtml_DivType447

    @xhtml_DivType447.setter
    def xhtml_DivType447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType447", None)
        self.__xhtml_DivType447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType446"):
                opp_val = getattr(old_value, "xhtml_MapType446", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType446"):
                opp_val = getattr(value, "xhtml_MapType446", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType446", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DivType256(self):
        return self.__xhtml_DivType256

    @xhtml_DivType256.setter
    def xhtml_DivType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType256", None)
        self.__xhtml_DivType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow255"):
                opp_val = getattr(old_value, "xhtml_Flow255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow255"):
                opp_val = getattr(value, "xhtml_Flow255", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Block:

    def __init__(self, block: str, xhtml_Block49: set["xhtml_H2Type"] = None, xhtml_Block51: set["xhtml_H3Type"] = None, xhtml_Block53: set["xhtml_H4Type"] = None, xhtml_Block55: set["xhtml_H5Type"] = None, xhtml_Block: set["xhtml_PType"] = None, xhtml_Block47: set["xhtml_H1Type"] = None, xhtml_Block57: set["xhtml_H6Type"] = None, xhtml_Block59: set["xhtml_DivType"] = None, xhtml_Block61: set["xhtml_UlType"] = None, xhtml_Block63: set["xhtml_OlType"] = None, xhtml_Block69: set["xhtml_HrType"] = None, xhtml_Block71: set["xhtml_BlockquoteType"] = None, xhtml_Block73: set["xhtml_AddressType"] = None, xhtml_Block65: set["xhtml_DlType"] = None, xhtml_Block67: set["xhtml_PreType"] = None, xhtml_Block75: set["xhtml_TableType"] = None):
        self.block = block
        self.xhtml_Block49 = xhtml_Block49 if xhtml_Block49 is not None else set()
        self.xhtml_Block51 = xhtml_Block51 if xhtml_Block51 is not None else set()
        self.xhtml_Block53 = xhtml_Block53 if xhtml_Block53 is not None else set()
        self.xhtml_Block55 = xhtml_Block55 if xhtml_Block55 is not None else set()
        self.xhtml_Block = xhtml_Block if xhtml_Block is not None else set()
        self.xhtml_Block47 = xhtml_Block47 if xhtml_Block47 is not None else set()
        self.xhtml_Block57 = xhtml_Block57 if xhtml_Block57 is not None else set()
        self.xhtml_Block59 = xhtml_Block59 if xhtml_Block59 is not None else set()
        self.xhtml_Block61 = xhtml_Block61 if xhtml_Block61 is not None else set()
        self.xhtml_Block63 = xhtml_Block63 if xhtml_Block63 is not None else set()
        self.xhtml_Block69 = xhtml_Block69 if xhtml_Block69 is not None else set()
        self.xhtml_Block71 = xhtml_Block71 if xhtml_Block71 is not None else set()
        self.xhtml_Block73 = xhtml_Block73 if xhtml_Block73 is not None else set()
        self.xhtml_Block65 = xhtml_Block65 if xhtml_Block65 is not None else set()
        self.xhtml_Block67 = xhtml_Block67 if xhtml_Block67 is not None else set()
        self.xhtml_Block75 = xhtml_Block75 if xhtml_Block75 is not None else set()
        
    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def xhtml_Block53(self):
        return self.__xhtml_Block53

    @xhtml_Block53.setter
    def xhtml_Block53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block53", None)
        self.__xhtml_Block53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type"):
                    opp_val = getattr(item, "xhtml_H4Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type"):
                    opp_val = getattr(item, "xhtml_H4Type", None)
                    
                    setattr(item, "xhtml_H4Type", self)
                    

    @property
    def xhtml_Block63(self):
        return self.__xhtml_Block63

    @xhtml_Block63.setter
    def xhtml_Block63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block63", None)
        self.__xhtml_Block63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType"):
                    opp_val = getattr(item, "xhtml_OlType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType"):
                    opp_val = getattr(item, "xhtml_OlType", None)
                    
                    setattr(item, "xhtml_OlType", self)
                    

    @property
    def xhtml_Block51(self):
        return self.__xhtml_Block51

    @xhtml_Block51.setter
    def xhtml_Block51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block51", None)
        self.__xhtml_Block51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type"):
                    opp_val = getattr(item, "xhtml_H3Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type"):
                    opp_val = getattr(item, "xhtml_H3Type", None)
                    
                    setattr(item, "xhtml_H3Type", self)
                    

    @property
    def xhtml_Block75(self):
        return self.__xhtml_Block75

    @xhtml_Block75.setter
    def xhtml_Block75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block75", None)
        self.__xhtml_Block75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType"):
                    opp_val = getattr(item, "xhtml_TableType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType"):
                    opp_val = getattr(item, "xhtml_TableType", None)
                    
                    setattr(item, "xhtml_TableType", self)
                    

    @property
    def xhtml_Block67(self):
        return self.__xhtml_Block67

    @xhtml_Block67.setter
    def xhtml_Block67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block67", None)
        self.__xhtml_Block67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType"):
                    opp_val = getattr(item, "xhtml_PreType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType"):
                    opp_val = getattr(item, "xhtml_PreType", None)
                    
                    setattr(item, "xhtml_PreType", self)
                    

    @property
    def xhtml_Block61(self):
        return self.__xhtml_Block61

    @xhtml_Block61.setter
    def xhtml_Block61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block61", None)
        self.__xhtml_Block61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType"):
                    opp_val = getattr(item, "xhtml_UlType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType"):
                    opp_val = getattr(item, "xhtml_UlType", None)
                    
                    setattr(item, "xhtml_UlType", self)
                    

    @property
    def xhtml_Block73(self):
        return self.__xhtml_Block73

    @xhtml_Block73.setter
    def xhtml_Block73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block73", None)
        self.__xhtml_Block73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType"):
                    opp_val = getattr(item, "xhtml_AddressType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType"):
                    opp_val = getattr(item, "xhtml_AddressType", None)
                    
                    setattr(item, "xhtml_AddressType", self)
                    

    @property
    def xhtml_Block65(self):
        return self.__xhtml_Block65

    @xhtml_Block65.setter
    def xhtml_Block65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block65", None)
        self.__xhtml_Block65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType"):
                    opp_val = getattr(item, "xhtml_DlType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType"):
                    opp_val = getattr(item, "xhtml_DlType", None)
                    
                    setattr(item, "xhtml_DlType", self)
                    

    @property
    def xhtml_Block55(self):
        return self.__xhtml_Block55

    @xhtml_Block55.setter
    def xhtml_Block55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block55", None)
        self.__xhtml_Block55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type"):
                    opp_val = getattr(item, "xhtml_H5Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type"):
                    opp_val = getattr(item, "xhtml_H5Type", None)
                    
                    setattr(item, "xhtml_H5Type", self)
                    

    @property
    def xhtml_Block69(self):
        return self.__xhtml_Block69

    @xhtml_Block69.setter
    def xhtml_Block69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block69", None)
        self.__xhtml_Block69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType"):
                    opp_val = getattr(item, "xhtml_HrType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType"):
                    opp_val = getattr(item, "xhtml_HrType", None)
                    
                    setattr(item, "xhtml_HrType", self)
                    

    @property
    def xhtml_Block57(self):
        return self.__xhtml_Block57

    @xhtml_Block57.setter
    def xhtml_Block57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block57", None)
        self.__xhtml_Block57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type"):
                    opp_val = getattr(item, "xhtml_H6Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type"):
                    opp_val = getattr(item, "xhtml_H6Type", None)
                    
                    setattr(item, "xhtml_H6Type", self)
                    

    @property
    def xhtml_Block47(self):
        return self.__xhtml_Block47

    @xhtml_Block47.setter
    def xhtml_Block47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block47", None)
        self.__xhtml_Block47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type"):
                    opp_val = getattr(item, "xhtml_H1Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type"):
                    opp_val = getattr(item, "xhtml_H1Type", None)
                    
                    setattr(item, "xhtml_H1Type", self)
                    

    @property
    def xhtml_Block59(self):
        return self.__xhtml_Block59

    @xhtml_Block59.setter
    def xhtml_Block59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block59", None)
        self.__xhtml_Block59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType"):
                    opp_val = getattr(item, "xhtml_DivType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType"):
                    opp_val = getattr(item, "xhtml_DivType", None)
                    
                    setattr(item, "xhtml_DivType", self)
                    

    @property
    def xhtml_Block49(self):
        return self.__xhtml_Block49

    @xhtml_Block49.setter
    def xhtml_Block49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block49", None)
        self.__xhtml_Block49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type"):
                    opp_val = getattr(item, "xhtml_H2Type", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type"):
                    opp_val = getattr(item, "xhtml_H2Type", None)
                    
                    setattr(item, "xhtml_H2Type", self)
                    

    @property
    def xhtml_Block(self):
        return self.__xhtml_Block

    @xhtml_Block.setter
    def xhtml_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block", None)
        self.__xhtml_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType"):
                    opp_val = getattr(item, "xhtml_PType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType"):
                    opp_val = getattr(item, "xhtml_PType", None)
                    
                    setattr(item, "xhtml_PType", self)
                    

    @property
    def xhtml_Block71(self):
        return self.__xhtml_Block71

    @xhtml_Block71.setter
    def xhtml_Block71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block71", None)
        self.__xhtml_Block71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType"):
                    opp_val = getattr(item, "xhtml_BlockquoteType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType"):
                    opp_val = getattr(item, "xhtml_BlockquoteType", None)
                    
                    setattr(item, "xhtml_BlockquoteType", self)
                    

class AContent:

    pass
class xhtml_AType(AContent):

    def __init__(self, coords: str, dir: str, href: str, hreflang: str, id: str, lang: str, lang1: str, name: str, accesskey: str, charset: str, class: str, rel: str, rev: str, shape: str, style: str, tabindex: str, title: str, type: str, xhtml_AType: "xhtml_DocumentRoot" = None, xhtml_AType283: "xhtml_Flow" = None, xhtml_AType354: "xhtml_Inline" = None, xhtml_AType479: "xhtml_PreContent" = None):
        self.coords = coords
        self.dir = dir
        self.href = href
        self.hreflang = hreflang
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.name = name
        self.accesskey = accesskey
        self.charset = charset
        self.class = class
        self.rel = rel
        self.rev = rev
        self.shape = shape
        self.style = style
        self.tabindex = tabindex
        self.title = title
        self.type = type
        self.xhtml_AType = xhtml_AType
        self.xhtml_AType283 = xhtml_AType283
        self.xhtml_AType354 = xhtml_AType354
        self.xhtml_AType479 = xhtml_AType479
        
    @property
    def rel(self) -> str:
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def coords(self) -> str:
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def charset(self) -> str:
        return self.__charset

    @charset.setter
    def charset(self, charset: str):
        self.__charset = charset

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def accesskey(self) -> str:
        return self.__accesskey

    @accesskey.setter
    def accesskey(self, accesskey: str):
        self.__accesskey = accesskey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def rev(self) -> str:
        return self.__rev

    @rev.setter
    def rev(self, rev: str):
        self.__rev = rev

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def hreflang(self) -> str:
        return self.__hreflang

    @hreflang.setter
    def hreflang(self, hreflang: str):
        self.__hreflang = hreflang

    @property
    def tabindex(self) -> str:
        return self.__tabindex

    @tabindex.setter
    def tabindex(self, tabindex: str):
        self.__tabindex = tabindex

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_AType479(self):
        return self.__xhtml_AType479

    @xhtml_AType479.setter
    def xhtml_AType479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType479", None)
        self.__xhtml_AType479 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent"):
                opp_val = getattr(old_value, "xhtml_PreContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent"):
                opp_val = getattr(value, "xhtml_PreContent", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AType283(self):
        return self.__xhtml_AType283

    @xhtml_AType283.setter
    def xhtml_AType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType283", None)
        self.__xhtml_AType283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow282"):
                opp_val = getattr(old_value, "xhtml_Flow282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow282"):
                opp_val = getattr(value, "xhtml_Flow282", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AType354(self):
        return self.__xhtml_AType354

    @xhtml_AType354.setter
    def xhtml_AType354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType354", None)
        self.__xhtml_AType354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline"):
                opp_val = getattr(old_value, "xhtml_Inline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline"):
                opp_val = getattr(value, "xhtml_Inline", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AType(self):
        return self.__xhtml_AType

    @xhtml_AType.setter
    def xhtml_AType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType", None)
        self.__xhtml_AType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot86"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot86"):
                opp_val = getattr(value, "xhtml_DocumentRoot86", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AreaType:

    def __init__(self, alt: str, class: str, coords: str, dir: str, href: str, id: str, lang: str, accesskey: str, lang1: str, nohref: str, shape: str, style: str, tabindex: str, title: str, xhtml_AreaType: "xhtml_DocumentRoot" = None, xhtml_AreaType474: "xhtml_MapType" = None):
        self.alt = alt
        self.class = class
        self.coords = coords
        self.dir = dir
        self.href = href
        self.id = id
        self.lang = lang
        self.accesskey = accesskey
        self.lang1 = lang1
        self.nohref = nohref
        self.shape = shape
        self.style = style
        self.tabindex = tabindex
        self.title = title
        self.xhtml_AreaType = xhtml_AreaType
        self.xhtml_AreaType474 = xhtml_AreaType474
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def coords(self) -> str:
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def accesskey(self) -> str:
        return self.__accesskey

    @accesskey.setter
    def accesskey(self, accesskey: str):
        self.__accesskey = accesskey

    @property
    def tabindex(self) -> str:
        return self.__tabindex

    @tabindex.setter
    def tabindex(self, tabindex: str):
        self.__tabindex = tabindex

    @property
    def nohref(self) -> str:
        return self.__nohref

    @nohref.setter
    def nohref(self, nohref: str):
        self.__nohref = nohref

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_AreaType(self):
        return self.__xhtml_AreaType

    @xhtml_AreaType.setter
    def xhtml_AreaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AreaType__xhtml_AreaType", None)
        self.__xhtml_AreaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot97"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot97"):
                opp_val = getattr(value, "xhtml_DocumentRoot97", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AreaType474(self):
        return self.__xhtml_AreaType474

    @xhtml_AreaType474.setter
    def xhtml_AreaType474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AreaType__xhtml_AreaType474", None)
        self.__xhtml_AreaType474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType473"):
                opp_val = getattr(old_value, "xhtml_MapType473", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType473"):
                opp_val = getattr(value, "xhtml_MapType473", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType473", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ImgType:

    def __init__(self, alt: str, class: str, width: str, dir: str, height: str, id: str, ismap: str, lang: str, lang1: str, longdesc: str, src: str, style: str, title: str, usemap: str, xhtml_ImgType: "xhtml_AContent" = None, xhtml_ImgType171: "xhtml_DocumentRoot" = None, xhtml_ImgType298: "xhtml_Flow" = None, xhtml_ImgType369: "xhtml_Inline" = None):
        self.alt = alt
        self.class = class
        self.width = width
        self.dir = dir
        self.height = height
        self.id = id
        self.ismap = ismap
        self.lang = lang
        self.lang1 = lang1
        self.longdesc = longdesc
        self.src = src
        self.style = style
        self.title = title
        self.usemap = usemap
        self.xhtml_ImgType = xhtml_ImgType
        self.xhtml_ImgType171 = xhtml_ImgType171
        self.xhtml_ImgType298 = xhtml_ImgType298
        self.xhtml_ImgType369 = xhtml_ImgType369
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def longdesc(self) -> str:
        return self.__longdesc

    @longdesc.setter
    def longdesc(self, longdesc: str):
        self.__longdesc = longdesc

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def usemap(self) -> str:
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def ismap(self) -> str:
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap

    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_ImgType171(self):
        return self.__xhtml_ImgType171

    @xhtml_ImgType171.setter
    def xhtml_ImgType171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType171", None)
        self.__xhtml_ImgType171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot170"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot170"):
                opp_val = getattr(value, "xhtml_DocumentRoot170", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ImgType(self):
        return self.__xhtml_ImgType

    @xhtml_ImgType.setter
    def xhtml_ImgType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType", None)
        self.__xhtml_ImgType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent8"):
                opp_val = getattr(old_value, "xhtml_AContent8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent8"):
                opp_val = getattr(value, "xhtml_AContent8", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ImgType298(self):
        return self.__xhtml_ImgType298

    @xhtml_ImgType298.setter
    def xhtml_ImgType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType298", None)
        self.__xhtml_ImgType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow297"):
                opp_val = getattr(old_value, "xhtml_Flow297", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow297"):
                opp_val = getattr(value, "xhtml_Flow297", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow297", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ImgType369(self):
        return self.__xhtml_ImgType369

    @xhtml_ImgType369.setter
    def xhtml_ImgType369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType369", None)
        self.__xhtml_ImgType369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline368"):
                opp_val = getattr(old_value, "xhtml_Inline368", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline368"):
                opp_val = getattr(value, "xhtml_Inline368", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline368", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_MapType:

    def __init__(self, block: str, class: str, dir: str, id: str, lang: str, lang1: str, name: str, style: str, title: str, xhtml_MapType: "xhtml_AContent" = None, xhtml_MapType179: "xhtml_DocumentRoot" = None, xhtml_MapType295: "xhtml_Flow" = None, xhtml_MapType366: "xhtml_Inline" = None, xhtml_MapType425: set["xhtml_PType"] = None, xhtml_MapType428: set["xhtml_H1Type"] = None, xhtml_MapType431: set["xhtml_H2Type"] = None, xhtml_MapType434: set["xhtml_H3Type"] = None, xhtml_MapType437: set["xhtml_H4Type"] = None, xhtml_MapType440: set["xhtml_H5Type"] = None, xhtml_MapType443: set["xhtml_H6Type"] = None, xhtml_MapType446: set["xhtml_DivType"] = None, xhtml_MapType449: set["xhtml_UlType"] = None, xhtml_MapType452: set["xhtml_OlType"] = None, xhtml_MapType455: set["xhtml_DlType"] = None, xhtml_MapType458: set["xhtml_PreType"] = None, xhtml_MapType461: set["xhtml_HrType"] = None, xhtml_MapType464: set["xhtml_BlockquoteType"] = None, xhtml_MapType467: set["xhtml_AddressType"] = None, xhtml_MapType470: set["xhtml_TableType"] = None, xhtml_MapType473: set["xhtml_AreaType"] = None, xhtml_MapType545: "xhtml_PreContent" = None):
        self.block = block
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.name = name
        self.style = style
        self.title = title
        self.xhtml_MapType = xhtml_MapType
        self.xhtml_MapType179 = xhtml_MapType179
        self.xhtml_MapType295 = xhtml_MapType295
        self.xhtml_MapType366 = xhtml_MapType366
        self.xhtml_MapType425 = xhtml_MapType425 if xhtml_MapType425 is not None else set()
        self.xhtml_MapType428 = xhtml_MapType428 if xhtml_MapType428 is not None else set()
        self.xhtml_MapType431 = xhtml_MapType431 if xhtml_MapType431 is not None else set()
        self.xhtml_MapType434 = xhtml_MapType434 if xhtml_MapType434 is not None else set()
        self.xhtml_MapType437 = xhtml_MapType437 if xhtml_MapType437 is not None else set()
        self.xhtml_MapType440 = xhtml_MapType440 if xhtml_MapType440 is not None else set()
        self.xhtml_MapType443 = xhtml_MapType443 if xhtml_MapType443 is not None else set()
        self.xhtml_MapType446 = xhtml_MapType446 if xhtml_MapType446 is not None else set()
        self.xhtml_MapType449 = xhtml_MapType449 if xhtml_MapType449 is not None else set()
        self.xhtml_MapType452 = xhtml_MapType452 if xhtml_MapType452 is not None else set()
        self.xhtml_MapType455 = xhtml_MapType455 if xhtml_MapType455 is not None else set()
        self.xhtml_MapType458 = xhtml_MapType458 if xhtml_MapType458 is not None else set()
        self.xhtml_MapType461 = xhtml_MapType461 if xhtml_MapType461 is not None else set()
        self.xhtml_MapType464 = xhtml_MapType464 if xhtml_MapType464 is not None else set()
        self.xhtml_MapType467 = xhtml_MapType467 if xhtml_MapType467 is not None else set()
        self.xhtml_MapType470 = xhtml_MapType470 if xhtml_MapType470 is not None else set()
        self.xhtml_MapType473 = xhtml_MapType473 if xhtml_MapType473 is not None else set()
        self.xhtml_MapType545 = xhtml_MapType545
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_MapType449(self):
        return self.__xhtml_MapType449

    @xhtml_MapType449.setter
    def xhtml_MapType449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType449", None)
        self.__xhtml_MapType449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType450"):
                    opp_val = getattr(item, "xhtml_UlType450", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType450", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType450"):
                    opp_val = getattr(item, "xhtml_UlType450", None)
                    
                    setattr(item, "xhtml_UlType450", self)
                    

    @property
    def xhtml_MapType452(self):
        return self.__xhtml_MapType452

    @xhtml_MapType452.setter
    def xhtml_MapType452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType452", None)
        self.__xhtml_MapType452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType453"):
                    opp_val = getattr(item, "xhtml_OlType453", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType453"):
                    opp_val = getattr(item, "xhtml_OlType453", None)
                    
                    setattr(item, "xhtml_OlType453", self)
                    

    @property
    def xhtml_MapType179(self):
        return self.__xhtml_MapType179

    @xhtml_MapType179.setter
    def xhtml_MapType179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType179", None)
        self.__xhtml_MapType179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot178"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot178"):
                opp_val = getattr(value, "xhtml_DocumentRoot178", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_MapType443(self):
        return self.__xhtml_MapType443

    @xhtml_MapType443.setter
    def xhtml_MapType443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType443", None)
        self.__xhtml_MapType443 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type444"):
                    opp_val = getattr(item, "xhtml_H6Type444", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type444", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type444"):
                    opp_val = getattr(item, "xhtml_H6Type444", None)
                    
                    setattr(item, "xhtml_H6Type444", self)
                    

    @property
    def xhtml_MapType431(self):
        return self.__xhtml_MapType431

    @xhtml_MapType431.setter
    def xhtml_MapType431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType431", None)
        self.__xhtml_MapType431 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type432"):
                    opp_val = getattr(item, "xhtml_H2Type432", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type432", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type432"):
                    opp_val = getattr(item, "xhtml_H2Type432", None)
                    
                    setattr(item, "xhtml_H2Type432", self)
                    

    @property
    def xhtml_MapType458(self):
        return self.__xhtml_MapType458

    @xhtml_MapType458.setter
    def xhtml_MapType458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType458", None)
        self.__xhtml_MapType458 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType459"):
                    opp_val = getattr(item, "xhtml_PreType459", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType459", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType459"):
                    opp_val = getattr(item, "xhtml_PreType459", None)
                    
                    setattr(item, "xhtml_PreType459", self)
                    

    @property
    def xhtml_MapType434(self):
        return self.__xhtml_MapType434

    @xhtml_MapType434.setter
    def xhtml_MapType434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType434", None)
        self.__xhtml_MapType434 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type435"):
                    opp_val = getattr(item, "xhtml_H3Type435", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type435", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type435"):
                    opp_val = getattr(item, "xhtml_H3Type435", None)
                    
                    setattr(item, "xhtml_H3Type435", self)
                    

    @property
    def xhtml_MapType545(self):
        return self.__xhtml_MapType545

    @xhtml_MapType545.setter
    def xhtml_MapType545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType545", None)
        self.__xhtml_MapType545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent544"):
                opp_val = getattr(old_value, "xhtml_PreContent544", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent544"):
                opp_val = getattr(value, "xhtml_PreContent544", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent544", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_MapType464(self):
        return self.__xhtml_MapType464

    @xhtml_MapType464.setter
    def xhtml_MapType464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType464", None)
        self.__xhtml_MapType464 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType465"):
                    opp_val = getattr(item, "xhtml_BlockquoteType465", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType465", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType465"):
                    opp_val = getattr(item, "xhtml_BlockquoteType465", None)
                    
                    setattr(item, "xhtml_BlockquoteType465", self)
                    

    @property
    def xhtml_MapType455(self):
        return self.__xhtml_MapType455

    @xhtml_MapType455.setter
    def xhtml_MapType455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType455", None)
        self.__xhtml_MapType455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType456"):
                    opp_val = getattr(item, "xhtml_DlType456", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType456", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType456"):
                    opp_val = getattr(item, "xhtml_DlType456", None)
                    
                    setattr(item, "xhtml_DlType456", self)
                    

    @property
    def xhtml_MapType446(self):
        return self.__xhtml_MapType446

    @xhtml_MapType446.setter
    def xhtml_MapType446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType446", None)
        self.__xhtml_MapType446 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType447"):
                    opp_val = getattr(item, "xhtml_DivType447", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType447"):
                    opp_val = getattr(item, "xhtml_DivType447", None)
                    
                    setattr(item, "xhtml_DivType447", self)
                    

    @property
    def xhtml_MapType295(self):
        return self.__xhtml_MapType295

    @xhtml_MapType295.setter
    def xhtml_MapType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType295", None)
        self.__xhtml_MapType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow294"):
                opp_val = getattr(old_value, "xhtml_Flow294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow294"):
                opp_val = getattr(value, "xhtml_Flow294", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_MapType428(self):
        return self.__xhtml_MapType428

    @xhtml_MapType428.setter
    def xhtml_MapType428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType428", None)
        self.__xhtml_MapType428 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type429"):
                    opp_val = getattr(item, "xhtml_H1Type429", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type429", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type429"):
                    opp_val = getattr(item, "xhtml_H1Type429", None)
                    
                    setattr(item, "xhtml_H1Type429", self)
                    

    @property
    def xhtml_MapType(self):
        return self.__xhtml_MapType

    @xhtml_MapType.setter
    def xhtml_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType", None)
        self.__xhtml_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent6"):
                opp_val = getattr(old_value, "xhtml_AContent6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent6"):
                opp_val = getattr(value, "xhtml_AContent6", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_MapType461(self):
        return self.__xhtml_MapType461

    @xhtml_MapType461.setter
    def xhtml_MapType461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType461", None)
        self.__xhtml_MapType461 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType462"):
                    opp_val = getattr(item, "xhtml_HrType462", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType462", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType462"):
                    opp_val = getattr(item, "xhtml_HrType462", None)
                    
                    setattr(item, "xhtml_HrType462", self)
                    

    @property
    def xhtml_MapType467(self):
        return self.__xhtml_MapType467

    @xhtml_MapType467.setter
    def xhtml_MapType467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType467", None)
        self.__xhtml_MapType467 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType468"):
                    opp_val = getattr(item, "xhtml_AddressType468", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType468", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType468"):
                    opp_val = getattr(item, "xhtml_AddressType468", None)
                    
                    setattr(item, "xhtml_AddressType468", self)
                    

    @property
    def xhtml_MapType440(self):
        return self.__xhtml_MapType440

    @xhtml_MapType440.setter
    def xhtml_MapType440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType440", None)
        self.__xhtml_MapType440 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type441"):
                    opp_val = getattr(item, "xhtml_H5Type441", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type441", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type441"):
                    opp_val = getattr(item, "xhtml_H5Type441", None)
                    
                    setattr(item, "xhtml_H5Type441", self)
                    

    @property
    def xhtml_MapType425(self):
        return self.__xhtml_MapType425

    @xhtml_MapType425.setter
    def xhtml_MapType425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType425", None)
        self.__xhtml_MapType425 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType426"):
                    opp_val = getattr(item, "xhtml_PType426", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType426", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType426"):
                    opp_val = getattr(item, "xhtml_PType426", None)
                    
                    setattr(item, "xhtml_PType426", self)
                    

    @property
    def xhtml_MapType473(self):
        return self.__xhtml_MapType473

    @xhtml_MapType473.setter
    def xhtml_MapType473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType473", None)
        self.__xhtml_MapType473 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AreaType474"):
                    opp_val = getattr(item, "xhtml_AreaType474", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AreaType474", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AreaType474"):
                    opp_val = getattr(item, "xhtml_AreaType474", None)
                    
                    setattr(item, "xhtml_AreaType474", self)
                    

    @property
    def xhtml_MapType437(self):
        return self.__xhtml_MapType437

    @xhtml_MapType437.setter
    def xhtml_MapType437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType437", None)
        self.__xhtml_MapType437 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type438"):
                    opp_val = getattr(item, "xhtml_H4Type438", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type438", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type438"):
                    opp_val = getattr(item, "xhtml_H4Type438", None)
                    
                    setattr(item, "xhtml_H4Type438", self)
                    

    @property
    def xhtml_MapType470(self):
        return self.__xhtml_MapType470

    @xhtml_MapType470.setter
    def xhtml_MapType470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType470", None)
        self.__xhtml_MapType470 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType471"):
                    opp_val = getattr(item, "xhtml_TableType471", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType471", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType471"):
                    opp_val = getattr(item, "xhtml_TableType471", None)
                    
                    setattr(item, "xhtml_TableType471", self)
                    

    @property
    def xhtml_MapType366(self):
        return self.__xhtml_MapType366

    @xhtml_MapType366.setter
    def xhtml_MapType366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_MapType__xhtml_MapType366", None)
        self.__xhtml_MapType366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline365"):
                opp_val = getattr(old_value, "xhtml_Inline365", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline365"):
                opp_val = getattr(value, "xhtml_Inline365", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline365", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AContent:

    def __init__(self, group: str, mixed: str, xhtml_AContent: set["xhtml_BrType"] = None, xhtml_AContent2: set["xhtml_SpanType"] = None, xhtml_AContent4: set["xhtml_BdoType"] = None, xhtml_AContent16: set["xhtml_BigType"] = None, xhtml_AContent18: set["xhtml_SmallType"] = None, xhtml_AContent20: set["xhtml_EmType"] = None, xhtml_AContent22: set["xhtml_StrongType"] = None, xhtml_AContent6: set["xhtml_MapType"] = None, xhtml_AContent8: set["xhtml_ImgType"] = None, xhtml_AContent10: set["xhtml_TtType"] = None, xhtml_AContent12: set["xhtml_IType"] = None, xhtml_AContent14: set["xhtml_BType"] = None, xhtml_AContent34: set["xhtml_VarType"] = None, xhtml_AContent36: set["xhtml_CiteType"] = None, xhtml_AContent38: set["xhtml_AbbrType"] = None, xhtml_AContent24: set["xhtml_DfnType"] = None, xhtml_AContent26: set["xhtml_CodeType"] = None, xhtml_AContent28: set["xhtml_QType"] = None, xhtml_AContent30: set["xhtml_SampType"] = None, xhtml_AContent32: set["xhtml_KbdType"] = None, xhtml_AContent40: set["xhtml_AcronymType"] = None, xhtml_AContent42: set["xhtml_SubType"] = None, xhtml_AContent44: set["xhtml_SupType"] = None):
        self.group = group
        self.mixed = mixed
        self.xhtml_AContent = xhtml_AContent if xhtml_AContent is not None else set()
        self.xhtml_AContent2 = xhtml_AContent2 if xhtml_AContent2 is not None else set()
        self.xhtml_AContent4 = xhtml_AContent4 if xhtml_AContent4 is not None else set()
        self.xhtml_AContent16 = xhtml_AContent16 if xhtml_AContent16 is not None else set()
        self.xhtml_AContent18 = xhtml_AContent18 if xhtml_AContent18 is not None else set()
        self.xhtml_AContent20 = xhtml_AContent20 if xhtml_AContent20 is not None else set()
        self.xhtml_AContent22 = xhtml_AContent22 if xhtml_AContent22 is not None else set()
        self.xhtml_AContent6 = xhtml_AContent6 if xhtml_AContent6 is not None else set()
        self.xhtml_AContent8 = xhtml_AContent8 if xhtml_AContent8 is not None else set()
        self.xhtml_AContent10 = xhtml_AContent10 if xhtml_AContent10 is not None else set()
        self.xhtml_AContent12 = xhtml_AContent12 if xhtml_AContent12 is not None else set()
        self.xhtml_AContent14 = xhtml_AContent14 if xhtml_AContent14 is not None else set()
        self.xhtml_AContent34 = xhtml_AContent34 if xhtml_AContent34 is not None else set()
        self.xhtml_AContent36 = xhtml_AContent36 if xhtml_AContent36 is not None else set()
        self.xhtml_AContent38 = xhtml_AContent38 if xhtml_AContent38 is not None else set()
        self.xhtml_AContent24 = xhtml_AContent24 if xhtml_AContent24 is not None else set()
        self.xhtml_AContent26 = xhtml_AContent26 if xhtml_AContent26 is not None else set()
        self.xhtml_AContent28 = xhtml_AContent28 if xhtml_AContent28 is not None else set()
        self.xhtml_AContent30 = xhtml_AContent30 if xhtml_AContent30 is not None else set()
        self.xhtml_AContent32 = xhtml_AContent32 if xhtml_AContent32 is not None else set()
        self.xhtml_AContent40 = xhtml_AContent40 if xhtml_AContent40 is not None else set()
        self.xhtml_AContent42 = xhtml_AContent42 if xhtml_AContent42 is not None else set()
        self.xhtml_AContent44 = xhtml_AContent44 if xhtml_AContent44 is not None else set()
        
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
    def xhtml_AContent14(self):
        return self.__xhtml_AContent14

    @xhtml_AContent14.setter
    def xhtml_AContent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent14", None)
        self.__xhtml_AContent14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType"):
                    opp_val = getattr(item, "xhtml_BType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType"):
                    opp_val = getattr(item, "xhtml_BType", None)
                    
                    setattr(item, "xhtml_BType", self)
                    

    @property
    def xhtml_AContent40(self):
        return self.__xhtml_AContent40

    @xhtml_AContent40.setter
    def xhtml_AContent40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent40", None)
        self.__xhtml_AContent40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType"):
                    opp_val = getattr(item, "xhtml_AcronymType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType"):
                    opp_val = getattr(item, "xhtml_AcronymType", None)
                    
                    setattr(item, "xhtml_AcronymType", self)
                    

    @property
    def xhtml_AContent44(self):
        return self.__xhtml_AContent44

    @xhtml_AContent44.setter
    def xhtml_AContent44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent44", None)
        self.__xhtml_AContent44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType"):
                    opp_val = getattr(item, "xhtml_SupType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType"):
                    opp_val = getattr(item, "xhtml_SupType", None)
                    
                    setattr(item, "xhtml_SupType", self)
                    

    @property
    def xhtml_AContent32(self):
        return self.__xhtml_AContent32

    @xhtml_AContent32.setter
    def xhtml_AContent32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent32", None)
        self.__xhtml_AContent32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType"):
                    opp_val = getattr(item, "xhtml_KbdType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType"):
                    opp_val = getattr(item, "xhtml_KbdType", None)
                    
                    setattr(item, "xhtml_KbdType", self)
                    

    @property
    def xhtml_AContent42(self):
        return self.__xhtml_AContent42

    @xhtml_AContent42.setter
    def xhtml_AContent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent42", None)
        self.__xhtml_AContent42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType"):
                    opp_val = getattr(item, "xhtml_SubType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType"):
                    opp_val = getattr(item, "xhtml_SubType", None)
                    
                    setattr(item, "xhtml_SubType", self)
                    

    @property
    def xhtml_AContent10(self):
        return self.__xhtml_AContent10

    @xhtml_AContent10.setter
    def xhtml_AContent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent10", None)
        self.__xhtml_AContent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType"):
                    opp_val = getattr(item, "xhtml_TtType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType"):
                    opp_val = getattr(item, "xhtml_TtType", None)
                    
                    setattr(item, "xhtml_TtType", self)
                    

    @property
    def xhtml_AContent4(self):
        return self.__xhtml_AContent4

    @xhtml_AContent4.setter
    def xhtml_AContent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent4", None)
        self.__xhtml_AContent4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BdoType"):
                    opp_val = getattr(item, "xhtml_BdoType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BdoType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BdoType"):
                    opp_val = getattr(item, "xhtml_BdoType", None)
                    
                    setattr(item, "xhtml_BdoType", self)
                    

    @property
    def xhtml_AContent28(self):
        return self.__xhtml_AContent28

    @xhtml_AContent28.setter
    def xhtml_AContent28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent28", None)
        self.__xhtml_AContent28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType"):
                    opp_val = getattr(item, "xhtml_QType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType"):
                    opp_val = getattr(item, "xhtml_QType", None)
                    
                    setattr(item, "xhtml_QType", self)
                    

    @property
    def xhtml_AContent(self):
        return self.__xhtml_AContent

    @xhtml_AContent.setter
    def xhtml_AContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent", None)
        self.__xhtml_AContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType"):
                    opp_val = getattr(item, "xhtml_BrType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType"):
                    opp_val = getattr(item, "xhtml_BrType", None)
                    
                    setattr(item, "xhtml_BrType", self)
                    

    @property
    def xhtml_AContent30(self):
        return self.__xhtml_AContent30

    @xhtml_AContent30.setter
    def xhtml_AContent30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent30", None)
        self.__xhtml_AContent30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType"):
                    opp_val = getattr(item, "xhtml_SampType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType"):
                    opp_val = getattr(item, "xhtml_SampType", None)
                    
                    setattr(item, "xhtml_SampType", self)
                    

    @property
    def xhtml_AContent24(self):
        return self.__xhtml_AContent24

    @xhtml_AContent24.setter
    def xhtml_AContent24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent24", None)
        self.__xhtml_AContent24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType"):
                    opp_val = getattr(item, "xhtml_DfnType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType"):
                    opp_val = getattr(item, "xhtml_DfnType", None)
                    
                    setattr(item, "xhtml_DfnType", self)
                    

    @property
    def xhtml_AContent34(self):
        return self.__xhtml_AContent34

    @xhtml_AContent34.setter
    def xhtml_AContent34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent34", None)
        self.__xhtml_AContent34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType"):
                    opp_val = getattr(item, "xhtml_VarType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType"):
                    opp_val = getattr(item, "xhtml_VarType", None)
                    
                    setattr(item, "xhtml_VarType", self)
                    

    @property
    def xhtml_AContent26(self):
        return self.__xhtml_AContent26

    @xhtml_AContent26.setter
    def xhtml_AContent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent26", None)
        self.__xhtml_AContent26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType"):
                    opp_val = getattr(item, "xhtml_CodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType"):
                    opp_val = getattr(item, "xhtml_CodeType", None)
                    
                    setattr(item, "xhtml_CodeType", self)
                    

    @property
    def xhtml_AContent38(self):
        return self.__xhtml_AContent38

    @xhtml_AContent38.setter
    def xhtml_AContent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent38", None)
        self.__xhtml_AContent38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType"):
                    opp_val = getattr(item, "xhtml_AbbrType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType"):
                    opp_val = getattr(item, "xhtml_AbbrType", None)
                    
                    setattr(item, "xhtml_AbbrType", self)
                    

    @property
    def xhtml_AContent2(self):
        return self.__xhtml_AContent2

    @xhtml_AContent2.setter
    def xhtml_AContent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent2", None)
        self.__xhtml_AContent2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType"):
                    opp_val = getattr(item, "xhtml_SpanType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType"):
                    opp_val = getattr(item, "xhtml_SpanType", None)
                    
                    setattr(item, "xhtml_SpanType", self)
                    

    @property
    def xhtml_AContent6(self):
        return self.__xhtml_AContent6

    @xhtml_AContent6.setter
    def xhtml_AContent6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent6", None)
        self.__xhtml_AContent6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_MapType"):
                    opp_val = getattr(item, "xhtml_MapType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_MapType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_MapType"):
                    opp_val = getattr(item, "xhtml_MapType", None)
                    
                    setattr(item, "xhtml_MapType", self)
                    

    @property
    def xhtml_AContent12(self):
        return self.__xhtml_AContent12

    @xhtml_AContent12.setter
    def xhtml_AContent12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent12", None)
        self.__xhtml_AContent12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType"):
                    opp_val = getattr(item, "xhtml_IType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType"):
                    opp_val = getattr(item, "xhtml_IType", None)
                    
                    setattr(item, "xhtml_IType", self)
                    

    @property
    def xhtml_AContent36(self):
        return self.__xhtml_AContent36

    @xhtml_AContent36.setter
    def xhtml_AContent36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent36", None)
        self.__xhtml_AContent36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType"):
                    opp_val = getattr(item, "xhtml_CiteType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType"):
                    opp_val = getattr(item, "xhtml_CiteType", None)
                    
                    setattr(item, "xhtml_CiteType", self)
                    

    @property
    def xhtml_AContent18(self):
        return self.__xhtml_AContent18

    @xhtml_AContent18.setter
    def xhtml_AContent18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent18", None)
        self.__xhtml_AContent18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType"):
                    opp_val = getattr(item, "xhtml_SmallType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType"):
                    opp_val = getattr(item, "xhtml_SmallType", None)
                    
                    setattr(item, "xhtml_SmallType", self)
                    

    @property
    def xhtml_AContent20(self):
        return self.__xhtml_AContent20

    @xhtml_AContent20.setter
    def xhtml_AContent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent20", None)
        self.__xhtml_AContent20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType"):
                    opp_val = getattr(item, "xhtml_EmType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType"):
                    opp_val = getattr(item, "xhtml_EmType", None)
                    
                    setattr(item, "xhtml_EmType", self)
                    

    @property
    def xhtml_AContent8(self):
        return self.__xhtml_AContent8

    @xhtml_AContent8.setter
    def xhtml_AContent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent8", None)
        self.__xhtml_AContent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType"):
                    opp_val = getattr(item, "xhtml_ImgType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType"):
                    opp_val = getattr(item, "xhtml_ImgType", None)
                    
                    setattr(item, "xhtml_ImgType", self)
                    

    @property
    def xhtml_AContent22(self):
        return self.__xhtml_AContent22

    @xhtml_AContent22.setter
    def xhtml_AContent22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent22", None)
        self.__xhtml_AContent22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType"):
                    opp_val = getattr(item, "xhtml_StrongType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType"):
                    opp_val = getattr(item, "xhtml_StrongType", None)
                    
                    setattr(item, "xhtml_StrongType", self)
                    

    @property
    def xhtml_AContent16(self):
        return self.__xhtml_AContent16

    @xhtml_AContent16.setter
    def xhtml_AContent16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent16", None)
        self.__xhtml_AContent16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType"):
                    opp_val = getattr(item, "xhtml_BigType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType"):
                    opp_val = getattr(item, "xhtml_BigType", None)
                    
                    setattr(item, "xhtml_BigType", self)
                    

class Inline:

    pass
class xhtml_KbdType(Inline):

    def __init__(self, class: str, dir: str, lang: str, lang1: str, style: str, title: str, id: str, xhtml_KbdType: "xhtml_AContent" = None, xhtml_KbdType174: "xhtml_DocumentRoot" = None, xhtml_KbdType334: "xhtml_Flow" = None, xhtml_KbdType405: "xhtml_Inline" = None, xhtml_KbdType515: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.id = id
        self.xhtml_KbdType = xhtml_KbdType
        self.xhtml_KbdType174 = xhtml_KbdType174
        self.xhtml_KbdType334 = xhtml_KbdType334
        self.xhtml_KbdType405 = xhtml_KbdType405
        self.xhtml_KbdType515 = xhtml_KbdType515
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_KbdType515(self):
        return self.__xhtml_KbdType515

    @xhtml_KbdType515.setter
    def xhtml_KbdType515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType515", None)
        self.__xhtml_KbdType515 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent514"):
                opp_val = getattr(old_value, "xhtml_PreContent514", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent514"):
                opp_val = getattr(value, "xhtml_PreContent514", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent514", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType405(self):
        return self.__xhtml_KbdType405

    @xhtml_KbdType405.setter
    def xhtml_KbdType405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType405", None)
        self.__xhtml_KbdType405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline404"):
                opp_val = getattr(old_value, "xhtml_Inline404", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline404"):
                opp_val = getattr(value, "xhtml_Inline404", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline404", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType(self):
        return self.__xhtml_KbdType

    @xhtml_KbdType.setter
    def xhtml_KbdType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType", None)
        self.__xhtml_KbdType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent32"):
                opp_val = getattr(old_value, "xhtml_AContent32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent32"):
                opp_val = getattr(value, "xhtml_AContent32", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType174(self):
        return self.__xhtml_KbdType174

    @xhtml_KbdType174.setter
    def xhtml_KbdType174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType174", None)
        self.__xhtml_KbdType174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot173"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot173"):
                opp_val = getattr(value, "xhtml_DocumentRoot173", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType334(self):
        return self.__xhtml_KbdType334

    @xhtml_KbdType334.setter
    def xhtml_KbdType334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType334", None)
        self.__xhtml_KbdType334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow333"):
                opp_val = getattr(old_value, "xhtml_Flow333", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow333"):
                opp_val = getattr(value, "xhtml_Flow333", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow333", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_IType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_IType: "xhtml_AContent" = None, xhtml_IType168: "xhtml_DocumentRoot" = None, xhtml_IType304: "xhtml_Flow" = None, xhtml_IType375: "xhtml_Inline" = None, xhtml_IType485: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_IType = xhtml_IType
        self.xhtml_IType168 = xhtml_IType168
        self.xhtml_IType304 = xhtml_IType304
        self.xhtml_IType375 = xhtml_IType375
        self.xhtml_IType485 = xhtml_IType485
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_IType168(self):
        return self.__xhtml_IType168

    @xhtml_IType168.setter
    def xhtml_IType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType168", None)
        self.__xhtml_IType168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot167"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot167"):
                opp_val = getattr(value, "xhtml_DocumentRoot167", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType485(self):
        return self.__xhtml_IType485

    @xhtml_IType485.setter
    def xhtml_IType485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType485", None)
        self.__xhtml_IType485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent484"):
                opp_val = getattr(old_value, "xhtml_PreContent484", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent484"):
                opp_val = getattr(value, "xhtml_PreContent484", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent484", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType304(self):
        return self.__xhtml_IType304

    @xhtml_IType304.setter
    def xhtml_IType304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType304", None)
        self.__xhtml_IType304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow303"):
                opp_val = getattr(old_value, "xhtml_Flow303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow303"):
                opp_val = getattr(value, "xhtml_Flow303", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType375(self):
        return self.__xhtml_IType375

    @xhtml_IType375.setter
    def xhtml_IType375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType375", None)
        self.__xhtml_IType375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline374"):
                opp_val = getattr(old_value, "xhtml_Inline374", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline374"):
                opp_val = getattr(value, "xhtml_Inline374", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline374", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType(self):
        return self.__xhtml_IType

    @xhtml_IType.setter
    def xhtml_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType", None)
        self.__xhtml_IType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent12"):
                opp_val = getattr(old_value, "xhtml_AContent12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent12"):
                opp_val = getattr(value, "xhtml_AContent12", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_VarType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_VarType: "xhtml_AContent" = None, xhtml_VarType233: "xhtml_DocumentRoot" = None, xhtml_VarType337: "xhtml_Flow" = None, xhtml_VarType408: "xhtml_Inline" = None, xhtml_VarType518: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_VarType = xhtml_VarType
        self.xhtml_VarType233 = xhtml_VarType233
        self.xhtml_VarType337 = xhtml_VarType337
        self.xhtml_VarType408 = xhtml_VarType408
        self.xhtml_VarType518 = xhtml_VarType518
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_VarType518(self):
        return self.__xhtml_VarType518

    @xhtml_VarType518.setter
    def xhtml_VarType518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType518", None)
        self.__xhtml_VarType518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent517"):
                opp_val = getattr(old_value, "xhtml_PreContent517", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent517"):
                opp_val = getattr(value, "xhtml_PreContent517", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent517", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType(self):
        return self.__xhtml_VarType

    @xhtml_VarType.setter
    def xhtml_VarType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType", None)
        self.__xhtml_VarType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent34"):
                opp_val = getattr(old_value, "xhtml_AContent34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent34"):
                opp_val = getattr(value, "xhtml_AContent34", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType233(self):
        return self.__xhtml_VarType233

    @xhtml_VarType233.setter
    def xhtml_VarType233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType233", None)
        self.__xhtml_VarType233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot232"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot232"):
                opp_val = getattr(value, "xhtml_DocumentRoot232", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType337(self):
        return self.__xhtml_VarType337

    @xhtml_VarType337.setter
    def xhtml_VarType337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType337", None)
        self.__xhtml_VarType337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow336"):
                opp_val = getattr(old_value, "xhtml_Flow336", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow336"):
                opp_val = getattr(value, "xhtml_Flow336", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow336", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType408(self):
        return self.__xhtml_VarType408

    @xhtml_VarType408.setter
    def xhtml_VarType408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType408", None)
        self.__xhtml_VarType408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline407"):
                opp_val = getattr(old_value, "xhtml_Inline407", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline407"):
                opp_val = getattr(value, "xhtml_Inline407", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline407", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CodeType(Inline):

    def __init__(self, lang: str, lang1: str, style: str, title: str, class: str, dir: str, id: str, xhtml_CodeType: "xhtml_AContent" = None, xhtml_CodeType120: "xhtml_DocumentRoot" = None, xhtml_CodeType325: "xhtml_Flow" = None, xhtml_CodeType396: "xhtml_Inline" = None, xhtml_CodeType506: "xhtml_PreContent" = None):
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.dir = dir
        self.id = id
        self.xhtml_CodeType = xhtml_CodeType
        self.xhtml_CodeType120 = xhtml_CodeType120
        self.xhtml_CodeType325 = xhtml_CodeType325
        self.xhtml_CodeType396 = xhtml_CodeType396
        self.xhtml_CodeType506 = xhtml_CodeType506
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_CodeType506(self):
        return self.__xhtml_CodeType506

    @xhtml_CodeType506.setter
    def xhtml_CodeType506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType506", None)
        self.__xhtml_CodeType506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent505"):
                opp_val = getattr(old_value, "xhtml_PreContent505", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent505"):
                opp_val = getattr(value, "xhtml_PreContent505", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent505", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType(self):
        return self.__xhtml_CodeType

    @xhtml_CodeType.setter
    def xhtml_CodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType", None)
        self.__xhtml_CodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent26"):
                opp_val = getattr(old_value, "xhtml_AContent26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent26"):
                opp_val = getattr(value, "xhtml_AContent26", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType120(self):
        return self.__xhtml_CodeType120

    @xhtml_CodeType120.setter
    def xhtml_CodeType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType120", None)
        self.__xhtml_CodeType120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot119"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot119"):
                opp_val = getattr(value, "xhtml_DocumentRoot119", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType396(self):
        return self.__xhtml_CodeType396

    @xhtml_CodeType396.setter
    def xhtml_CodeType396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType396", None)
        self.__xhtml_CodeType396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline395"):
                opp_val = getattr(old_value, "xhtml_Inline395", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline395"):
                opp_val = getattr(value, "xhtml_Inline395", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline395", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType325(self):
        return self.__xhtml_CodeType325

    @xhtml_CodeType325.setter
    def xhtml_CodeType325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType325", None)
        self.__xhtml_CodeType325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow324"):
                opp_val = getattr(old_value, "xhtml_Flow324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow324"):
                opp_val = getattr(value, "xhtml_Flow324", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CaptionType(Inline):

    def __init__(self, id: str, lang: str, lang1: str, style: str, title: str, class: str, dir: str, xhtml_CaptionType: "xhtml_DocumentRoot" = None, xhtml_CaptionType548: "xhtml_TableType" = None):
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.dir = dir
        self.xhtml_CaptionType = xhtml_CaptionType
        self.xhtml_CaptionType548 = xhtml_CaptionType548
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_CaptionType548(self):
        return self.__xhtml_CaptionType548

    @xhtml_CaptionType548.setter
    def xhtml_CaptionType548(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CaptionType__xhtml_CaptionType548", None)
        self.__xhtml_CaptionType548 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType547"):
                opp_val = getattr(old_value, "xhtml_TableType547", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType547", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType547"):
                opp_val = getattr(value, "xhtml_TableType547", None)
                setattr(value, "xhtml_TableType547", self)

    @property
    def xhtml_CaptionType(self):
        return self.__xhtml_CaptionType

    @xhtml_CaptionType.setter
    def xhtml_CaptionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CaptionType__xhtml_CaptionType", None)
        self.__xhtml_CaptionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot114"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot114"):
                opp_val = getattr(value, "xhtml_DocumentRoot114", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SupType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_SupType: "xhtml_AContent" = None, xhtml_SupType209: "xhtml_DocumentRoot" = None, xhtml_SupType352: "xhtml_Flow" = None, xhtml_SupType423: "xhtml_Inline" = None, xhtml_SupType533: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_SupType = xhtml_SupType
        self.xhtml_SupType209 = xhtml_SupType209
        self.xhtml_SupType352 = xhtml_SupType352
        self.xhtml_SupType423 = xhtml_SupType423
        self.xhtml_SupType533 = xhtml_SupType533
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_SupType423(self):
        return self.__xhtml_SupType423

    @xhtml_SupType423.setter
    def xhtml_SupType423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType423", None)
        self.__xhtml_SupType423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline422"):
                opp_val = getattr(old_value, "xhtml_Inline422", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline422"):
                opp_val = getattr(value, "xhtml_Inline422", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline422", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType(self):
        return self.__xhtml_SupType

    @xhtml_SupType.setter
    def xhtml_SupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType", None)
        self.__xhtml_SupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent44"):
                opp_val = getattr(old_value, "xhtml_AContent44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent44"):
                opp_val = getattr(value, "xhtml_AContent44", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType533(self):
        return self.__xhtml_SupType533

    @xhtml_SupType533.setter
    def xhtml_SupType533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType533", None)
        self.__xhtml_SupType533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent532"):
                opp_val = getattr(old_value, "xhtml_PreContent532", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent532"):
                opp_val = getattr(value, "xhtml_PreContent532", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent532", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType352(self):
        return self.__xhtml_SupType352

    @xhtml_SupType352.setter
    def xhtml_SupType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType352", None)
        self.__xhtml_SupType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow351"):
                opp_val = getattr(old_value, "xhtml_Flow351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow351"):
                opp_val = getattr(value, "xhtml_Flow351", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType209(self):
        return self.__xhtml_SupType209

    @xhtml_SupType209.setter
    def xhtml_SupType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType209", None)
        self.__xhtml_SupType209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot208"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot208"):
                opp_val = getattr(value, "xhtml_DocumentRoot208", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_EmType(Inline):

    def __init__(self, dir: str, id: str, lang: str, lang1: str, style: str, title: str, class: str, xhtml_EmType: "xhtml_AContent" = None, xhtml_EmType144: "xhtml_DocumentRoot" = None, xhtml_EmType316: "xhtml_Flow" = None, xhtml_EmType387: "xhtml_Inline" = None, xhtml_EmType497: "xhtml_PreContent" = None):
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_EmType = xhtml_EmType
        self.xhtml_EmType144 = xhtml_EmType144
        self.xhtml_EmType316 = xhtml_EmType316
        self.xhtml_EmType387 = xhtml_EmType387
        self.xhtml_EmType497 = xhtml_EmType497
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_EmType144(self):
        return self.__xhtml_EmType144

    @xhtml_EmType144.setter
    def xhtml_EmType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType144", None)
        self.__xhtml_EmType144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot143"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot143"):
                opp_val = getattr(value, "xhtml_DocumentRoot143", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType497(self):
        return self.__xhtml_EmType497

    @xhtml_EmType497.setter
    def xhtml_EmType497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType497", None)
        self.__xhtml_EmType497 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent496"):
                opp_val = getattr(old_value, "xhtml_PreContent496", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent496"):
                opp_val = getattr(value, "xhtml_PreContent496", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent496", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType316(self):
        return self.__xhtml_EmType316

    @xhtml_EmType316.setter
    def xhtml_EmType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType316", None)
        self.__xhtml_EmType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow315"):
                opp_val = getattr(old_value, "xhtml_Flow315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow315"):
                opp_val = getattr(value, "xhtml_Flow315", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType(self):
        return self.__xhtml_EmType

    @xhtml_EmType.setter
    def xhtml_EmType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType", None)
        self.__xhtml_EmType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent20"):
                opp_val = getattr(old_value, "xhtml_AContent20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent20"):
                opp_val = getattr(value, "xhtml_AContent20", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType387(self):
        return self.__xhtml_EmType387

    @xhtml_EmType387.setter
    def xhtml_EmType387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType387", None)
        self.__xhtml_EmType387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline386"):
                opp_val = getattr(old_value, "xhtml_Inline386", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline386"):
                opp_val = getattr(value, "xhtml_Inline386", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline386", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_QType(Inline):

    def __init__(self, cite1: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, class: str, xhtml_QType: "xhtml_AContent" = None, xhtml_QType191: "xhtml_DocumentRoot" = None, xhtml_QType328: "xhtml_Flow" = None, xhtml_QType399: "xhtml_Inline" = None, xhtml_QType509: "xhtml_PreContent" = None):
        self.cite1 = cite1
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_QType = xhtml_QType
        self.xhtml_QType191 = xhtml_QType191
        self.xhtml_QType328 = xhtml_QType328
        self.xhtml_QType399 = xhtml_QType399
        self.xhtml_QType509 = xhtml_QType509
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def cite1(self) -> str:
        return self.__cite1

    @cite1.setter
    def cite1(self, cite1: str):
        self.__cite1 = cite1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_QType399(self):
        return self.__xhtml_QType399

    @xhtml_QType399.setter
    def xhtml_QType399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType399", None)
        self.__xhtml_QType399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline398"):
                opp_val = getattr(old_value, "xhtml_Inline398", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline398"):
                opp_val = getattr(value, "xhtml_Inline398", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline398", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType191(self):
        return self.__xhtml_QType191

    @xhtml_QType191.setter
    def xhtml_QType191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType191", None)
        self.__xhtml_QType191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot190"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot190"):
                opp_val = getattr(value, "xhtml_DocumentRoot190", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType328(self):
        return self.__xhtml_QType328

    @xhtml_QType328.setter
    def xhtml_QType328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType328", None)
        self.__xhtml_QType328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow327"):
                opp_val = getattr(old_value, "xhtml_Flow327", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow327"):
                opp_val = getattr(value, "xhtml_Flow327", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow327", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType509(self):
        return self.__xhtml_QType509

    @xhtml_QType509.setter
    def xhtml_QType509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType509", None)
        self.__xhtml_QType509 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent508"):
                opp_val = getattr(old_value, "xhtml_PreContent508", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent508"):
                opp_val = getattr(value, "xhtml_PreContent508", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent508", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType(self):
        return self.__xhtml_QType

    @xhtml_QType.setter
    def xhtml_QType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType", None)
        self.__xhtml_QType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent28"):
                opp_val = getattr(old_value, "xhtml_AContent28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent28"):
                opp_val = getattr(value, "xhtml_AContent28", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H5Type(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_H5Type: "xhtml_Block" = None, xhtml_H5Type159: "xhtml_DocumentRoot" = None, xhtml_H5Type250: "xhtml_Flow" = None, xhtml_H5Type441: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_H5Type = xhtml_H5Type
        self.xhtml_H5Type159 = xhtml_H5Type159
        self.xhtml_H5Type250 = xhtml_H5Type250
        self.xhtml_H5Type441 = xhtml_H5Type441
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_H5Type441(self):
        return self.__xhtml_H5Type441

    @xhtml_H5Type441.setter
    def xhtml_H5Type441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type441", None)
        self.__xhtml_H5Type441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType440"):
                opp_val = getattr(old_value, "xhtml_MapType440", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType440"):
                opp_val = getattr(value, "xhtml_MapType440", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType440", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H5Type(self):
        return self.__xhtml_H5Type

    @xhtml_H5Type.setter
    def xhtml_H5Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type", None)
        self.__xhtml_H5Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block55"):
                opp_val = getattr(old_value, "xhtml_Block55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block55"):
                opp_val = getattr(value, "xhtml_Block55", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H5Type250(self):
        return self.__xhtml_H5Type250

    @xhtml_H5Type250.setter
    def xhtml_H5Type250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type250", None)
        self.__xhtml_H5Type250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow249"):
                opp_val = getattr(old_value, "xhtml_Flow249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow249"):
                opp_val = getattr(value, "xhtml_Flow249", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H5Type159(self):
        return self.__xhtml_H5Type159

    @xhtml_H5Type159.setter
    def xhtml_H5Type159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type159", None)
        self.__xhtml_H5Type159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot158"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot158"):
                opp_val = getattr(value, "xhtml_DocumentRoot158", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_BType: "xhtml_AContent" = None, xhtml_BType100: "xhtml_DocumentRoot" = None, xhtml_BType307: "xhtml_Flow" = None, xhtml_BType378: "xhtml_Inline" = None, xhtml_BType488: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_BType = xhtml_BType
        self.xhtml_BType100 = xhtml_BType100
        self.xhtml_BType307 = xhtml_BType307
        self.xhtml_BType378 = xhtml_BType378
        self.xhtml_BType488 = xhtml_BType488
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_BType307(self):
        return self.__xhtml_BType307

    @xhtml_BType307.setter
    def xhtml_BType307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType307", None)
        self.__xhtml_BType307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow306"):
                opp_val = getattr(old_value, "xhtml_Flow306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow306"):
                opp_val = getattr(value, "xhtml_Flow306", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType378(self):
        return self.__xhtml_BType378

    @xhtml_BType378.setter
    def xhtml_BType378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType378", None)
        self.__xhtml_BType378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline377"):
                opp_val = getattr(old_value, "xhtml_Inline377", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline377"):
                opp_val = getattr(value, "xhtml_Inline377", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline377", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType488(self):
        return self.__xhtml_BType488

    @xhtml_BType488.setter
    def xhtml_BType488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType488", None)
        self.__xhtml_BType488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent487"):
                opp_val = getattr(old_value, "xhtml_PreContent487", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent487"):
                opp_val = getattr(value, "xhtml_PreContent487", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent487", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType(self):
        return self.__xhtml_BType

    @xhtml_BType.setter
    def xhtml_BType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType", None)
        self.__xhtml_BType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent14"):
                opp_val = getattr(old_value, "xhtml_AContent14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent14"):
                opp_val = getattr(value, "xhtml_AContent14", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType100(self):
        return self.__xhtml_BType100

    @xhtml_BType100.setter
    def xhtml_BType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType100", None)
        self.__xhtml_BType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot99"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot99"):
                opp_val = getattr(value, "xhtml_DocumentRoot99", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_StrongType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_StrongType: "xhtml_AContent" = None, xhtml_StrongType203: "xhtml_DocumentRoot" = None, xhtml_StrongType319: "xhtml_Flow" = None, xhtml_StrongType390: "xhtml_Inline" = None, xhtml_StrongType500: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_StrongType = xhtml_StrongType
        self.xhtml_StrongType203 = xhtml_StrongType203
        self.xhtml_StrongType319 = xhtml_StrongType319
        self.xhtml_StrongType390 = xhtml_StrongType390
        self.xhtml_StrongType500 = xhtml_StrongType500
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_StrongType390(self):
        return self.__xhtml_StrongType390

    @xhtml_StrongType390.setter
    def xhtml_StrongType390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType390", None)
        self.__xhtml_StrongType390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline389"):
                opp_val = getattr(old_value, "xhtml_Inline389", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline389"):
                opp_val = getattr(value, "xhtml_Inline389", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline389", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType500(self):
        return self.__xhtml_StrongType500

    @xhtml_StrongType500.setter
    def xhtml_StrongType500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType500", None)
        self.__xhtml_StrongType500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent499"):
                opp_val = getattr(old_value, "xhtml_PreContent499", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent499"):
                opp_val = getattr(value, "xhtml_PreContent499", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent499", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType319(self):
        return self.__xhtml_StrongType319

    @xhtml_StrongType319.setter
    def xhtml_StrongType319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType319", None)
        self.__xhtml_StrongType319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow318"):
                opp_val = getattr(old_value, "xhtml_Flow318", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow318"):
                opp_val = getattr(value, "xhtml_Flow318", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow318", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType(self):
        return self.__xhtml_StrongType

    @xhtml_StrongType.setter
    def xhtml_StrongType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType", None)
        self.__xhtml_StrongType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent22"):
                opp_val = getattr(old_value, "xhtml_AContent22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent22"):
                opp_val = getattr(value, "xhtml_AContent22", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType203(self):
        return self.__xhtml_StrongType203

    @xhtml_StrongType203.setter
    def xhtml_StrongType203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType203", None)
        self.__xhtml_StrongType203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot202"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot202"):
                opp_val = getattr(value, "xhtml_DocumentRoot202", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H3Type(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_H3Type: "xhtml_Block" = None, xhtml_H3Type153: "xhtml_DocumentRoot" = None, xhtml_H3Type244: "xhtml_Flow" = None, xhtml_H3Type435: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_H3Type = xhtml_H3Type
        self.xhtml_H3Type153 = xhtml_H3Type153
        self.xhtml_H3Type244 = xhtml_H3Type244
        self.xhtml_H3Type435 = xhtml_H3Type435
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_H3Type153(self):
        return self.__xhtml_H3Type153

    @xhtml_H3Type153.setter
    def xhtml_H3Type153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type153", None)
        self.__xhtml_H3Type153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot152"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot152"):
                opp_val = getattr(value, "xhtml_DocumentRoot152", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H3Type244(self):
        return self.__xhtml_H3Type244

    @xhtml_H3Type244.setter
    def xhtml_H3Type244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type244", None)
        self.__xhtml_H3Type244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow243"):
                opp_val = getattr(old_value, "xhtml_Flow243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow243"):
                opp_val = getattr(value, "xhtml_Flow243", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H3Type(self):
        return self.__xhtml_H3Type

    @xhtml_H3Type.setter
    def xhtml_H3Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type", None)
        self.__xhtml_H3Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block51"):
                opp_val = getattr(old_value, "xhtml_Block51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block51"):
                opp_val = getattr(value, "xhtml_Block51", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H3Type435(self):
        return self.__xhtml_H3Type435

    @xhtml_H3Type435.setter
    def xhtml_H3Type435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type435", None)
        self.__xhtml_H3Type435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType434"):
                opp_val = getattr(old_value, "xhtml_MapType434", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType434"):
                opp_val = getattr(value, "xhtml_MapType434", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType434", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AddressType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_AddressType: "xhtml_Block" = None, xhtml_AddressType95: "xhtml_DocumentRoot" = None, xhtml_AddressType277: "xhtml_Flow" = None, xhtml_AddressType468: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_AddressType = xhtml_AddressType
        self.xhtml_AddressType95 = xhtml_AddressType95
        self.xhtml_AddressType277 = xhtml_AddressType277
        self.xhtml_AddressType468 = xhtml_AddressType468
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_AddressType(self):
        return self.__xhtml_AddressType

    @xhtml_AddressType.setter
    def xhtml_AddressType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType", None)
        self.__xhtml_AddressType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block73"):
                opp_val = getattr(old_value, "xhtml_Block73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block73"):
                opp_val = getattr(value, "xhtml_Block73", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType277(self):
        return self.__xhtml_AddressType277

    @xhtml_AddressType277.setter
    def xhtml_AddressType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType277", None)
        self.__xhtml_AddressType277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow276"):
                opp_val = getattr(old_value, "xhtml_Flow276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow276"):
                opp_val = getattr(value, "xhtml_Flow276", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType468(self):
        return self.__xhtml_AddressType468

    @xhtml_AddressType468.setter
    def xhtml_AddressType468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType468", None)
        self.__xhtml_AddressType468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType467"):
                opp_val = getattr(old_value, "xhtml_MapType467", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType467"):
                opp_val = getattr(value, "xhtml_MapType467", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType467", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType95(self):
        return self.__xhtml_AddressType95

    @xhtml_AddressType95.setter
    def xhtml_AddressType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType95", None)
        self.__xhtml_AddressType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot94"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot94"):
                opp_val = getattr(value, "xhtml_DocumentRoot94", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H1Type(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_H1Type: "xhtml_Block" = None, xhtml_H1Type147: "xhtml_DocumentRoot" = None, xhtml_H1Type238: "xhtml_Flow" = None, xhtml_H1Type429: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_H1Type = xhtml_H1Type
        self.xhtml_H1Type147 = xhtml_H1Type147
        self.xhtml_H1Type238 = xhtml_H1Type238
        self.xhtml_H1Type429 = xhtml_H1Type429
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_H1Type(self):
        return self.__xhtml_H1Type

    @xhtml_H1Type.setter
    def xhtml_H1Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type", None)
        self.__xhtml_H1Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block47"):
                opp_val = getattr(old_value, "xhtml_Block47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block47"):
                opp_val = getattr(value, "xhtml_Block47", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H1Type147(self):
        return self.__xhtml_H1Type147

    @xhtml_H1Type147.setter
    def xhtml_H1Type147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type147", None)
        self.__xhtml_H1Type147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot146"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot146"):
                opp_val = getattr(value, "xhtml_DocumentRoot146", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H1Type429(self):
        return self.__xhtml_H1Type429

    @xhtml_H1Type429.setter
    def xhtml_H1Type429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type429", None)
        self.__xhtml_H1Type429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType428"):
                opp_val = getattr(old_value, "xhtml_MapType428", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType428"):
                opp_val = getattr(value, "xhtml_MapType428", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType428", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H1Type238(self):
        return self.__xhtml_H1Type238

    @xhtml_H1Type238.setter
    def xhtml_H1Type238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type238", None)
        self.__xhtml_H1Type238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow237"):
                opp_val = getattr(old_value, "xhtml_Flow237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow237"):
                opp_val = getattr(value, "xhtml_Flow237", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AcronymType(Inline):

    def __init__(self, lang: str, lang1: str, style: str, title: str, class: str, dir: str, id: str, xhtml_AcronymType: "xhtml_AContent" = None, xhtml_AcronymType92: "xhtml_DocumentRoot" = None, xhtml_AcronymType346: "xhtml_Flow" = None, xhtml_AcronymType417: "xhtml_Inline" = None, xhtml_AcronymType527: "xhtml_PreContent" = None):
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.dir = dir
        self.id = id
        self.xhtml_AcronymType = xhtml_AcronymType
        self.xhtml_AcronymType92 = xhtml_AcronymType92
        self.xhtml_AcronymType346 = xhtml_AcronymType346
        self.xhtml_AcronymType417 = xhtml_AcronymType417
        self.xhtml_AcronymType527 = xhtml_AcronymType527
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_AcronymType417(self):
        return self.__xhtml_AcronymType417

    @xhtml_AcronymType417.setter
    def xhtml_AcronymType417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType417", None)
        self.__xhtml_AcronymType417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline416"):
                opp_val = getattr(old_value, "xhtml_Inline416", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline416"):
                opp_val = getattr(value, "xhtml_Inline416", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline416", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType527(self):
        return self.__xhtml_AcronymType527

    @xhtml_AcronymType527.setter
    def xhtml_AcronymType527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType527", None)
        self.__xhtml_AcronymType527 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent526"):
                opp_val = getattr(old_value, "xhtml_PreContent526", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent526"):
                opp_val = getattr(value, "xhtml_PreContent526", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent526", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType92(self):
        return self.__xhtml_AcronymType92

    @xhtml_AcronymType92.setter
    def xhtml_AcronymType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType92", None)
        self.__xhtml_AcronymType92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot91"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot91"):
                opp_val = getattr(value, "xhtml_DocumentRoot91", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType(self):
        return self.__xhtml_AcronymType

    @xhtml_AcronymType.setter
    def xhtml_AcronymType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType", None)
        self.__xhtml_AcronymType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent40"):
                opp_val = getattr(old_value, "xhtml_AContent40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent40"):
                opp_val = getattr(value, "xhtml_AContent40", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType346(self):
        return self.__xhtml_AcronymType346

    @xhtml_AcronymType346.setter
    def xhtml_AcronymType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType346", None)
        self.__xhtml_AcronymType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow345"):
                opp_val = getattr(old_value, "xhtml_Flow345", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow345"):
                opp_val = getattr(value, "xhtml_Flow345", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow345", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H2Type(Inline):

    def __init__(self, lang: str, lang1: str, style: str, title: str, class: str, dir: str, id: str, xhtml_H2Type: "xhtml_Block" = None, xhtml_H2Type150: "xhtml_DocumentRoot" = None, xhtml_H2Type241: "xhtml_Flow" = None, xhtml_H2Type432: "xhtml_MapType" = None):
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.dir = dir
        self.id = id
        self.xhtml_H2Type = xhtml_H2Type
        self.xhtml_H2Type150 = xhtml_H2Type150
        self.xhtml_H2Type241 = xhtml_H2Type241
        self.xhtml_H2Type432 = xhtml_H2Type432
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_H2Type(self):
        return self.__xhtml_H2Type

    @xhtml_H2Type.setter
    def xhtml_H2Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type", None)
        self.__xhtml_H2Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block49"):
                opp_val = getattr(old_value, "xhtml_Block49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block49"):
                opp_val = getattr(value, "xhtml_Block49", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H2Type241(self):
        return self.__xhtml_H2Type241

    @xhtml_H2Type241.setter
    def xhtml_H2Type241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type241", None)
        self.__xhtml_H2Type241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow240"):
                opp_val = getattr(old_value, "xhtml_Flow240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow240"):
                opp_val = getattr(value, "xhtml_Flow240", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H2Type150(self):
        return self.__xhtml_H2Type150

    @xhtml_H2Type150.setter
    def xhtml_H2Type150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type150", None)
        self.__xhtml_H2Type150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot149"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot149"):
                opp_val = getattr(value, "xhtml_DocumentRoot149", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H2Type432(self):
        return self.__xhtml_H2Type432

    @xhtml_H2Type432.setter
    def xhtml_H2Type432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type432", None)
        self.__xhtml_H2Type432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType431"):
                opp_val = getattr(old_value, "xhtml_MapType431", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType431"):
                opp_val = getattr(value, "xhtml_MapType431", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType431", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_PType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_PType: "xhtml_Block" = None, xhtml_PType185: "xhtml_DocumentRoot" = None, xhtml_PType235: "xhtml_Flow" = None, xhtml_PType426: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_PType = xhtml_PType
        self.xhtml_PType185 = xhtml_PType185
        self.xhtml_PType235 = xhtml_PType235
        self.xhtml_PType426 = xhtml_PType426
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_PType426(self):
        return self.__xhtml_PType426

    @xhtml_PType426.setter
    def xhtml_PType426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType426", None)
        self.__xhtml_PType426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType425"):
                opp_val = getattr(old_value, "xhtml_MapType425", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType425"):
                opp_val = getattr(value, "xhtml_MapType425", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType425", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PType235(self):
        return self.__xhtml_PType235

    @xhtml_PType235.setter
    def xhtml_PType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType235", None)
        self.__xhtml_PType235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow"):
                opp_val = getattr(old_value, "xhtml_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow"):
                opp_val = getattr(value, "xhtml_Flow", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PType(self):
        return self.__xhtml_PType

    @xhtml_PType.setter
    def xhtml_PType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType", None)
        self.__xhtml_PType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block"):
                opp_val = getattr(old_value, "xhtml_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block"):
                opp_val = getattr(value, "xhtml_Block", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PType185(self):
        return self.__xhtml_PType185

    @xhtml_PType185.setter
    def xhtml_PType185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType185", None)
        self.__xhtml_PType185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot184"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot184"):
                opp_val = getattr(value, "xhtml_DocumentRoot184", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TtType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_TtType: "xhtml_AContent" = None, xhtml_TtType227: "xhtml_DocumentRoot" = None, xhtml_TtType301: "xhtml_Flow" = None, xhtml_TtType372: "xhtml_Inline" = None, xhtml_TtType482: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_TtType = xhtml_TtType
        self.xhtml_TtType227 = xhtml_TtType227
        self.xhtml_TtType301 = xhtml_TtType301
        self.xhtml_TtType372 = xhtml_TtType372
        self.xhtml_TtType482 = xhtml_TtType482
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_TtType(self):
        return self.__xhtml_TtType

    @xhtml_TtType.setter
    def xhtml_TtType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType", None)
        self.__xhtml_TtType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent10"):
                opp_val = getattr(old_value, "xhtml_AContent10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent10"):
                opp_val = getattr(value, "xhtml_AContent10", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType372(self):
        return self.__xhtml_TtType372

    @xhtml_TtType372.setter
    def xhtml_TtType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType372", None)
        self.__xhtml_TtType372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline371"):
                opp_val = getattr(old_value, "xhtml_Inline371", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline371"):
                opp_val = getattr(value, "xhtml_Inline371", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline371", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType482(self):
        return self.__xhtml_TtType482

    @xhtml_TtType482.setter
    def xhtml_TtType482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType482", None)
        self.__xhtml_TtType482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent481"):
                opp_val = getattr(old_value, "xhtml_PreContent481", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent481"):
                opp_val = getattr(value, "xhtml_PreContent481", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent481", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType227(self):
        return self.__xhtml_TtType227

    @xhtml_TtType227.setter
    def xhtml_TtType227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType227", None)
        self.__xhtml_TtType227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot226"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot226"):
                opp_val = getattr(value, "xhtml_DocumentRoot226", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType301(self):
        return self.__xhtml_TtType301

    @xhtml_TtType301.setter
    def xhtml_TtType301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType301", None)
        self.__xhtml_TtType301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow300"):
                opp_val = getattr(old_value, "xhtml_Flow300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow300"):
                opp_val = getattr(value, "xhtml_Flow300", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H4Type(Inline):

    def __init__(self, title: str, class: str, dir: str, id: str, lang: str, lang1: str, style: str, xhtml_H4Type: "xhtml_Block" = None, xhtml_H4Type156: "xhtml_DocumentRoot" = None, xhtml_H4Type247: "xhtml_Flow" = None, xhtml_H4Type438: "xhtml_MapType" = None):
        self.title = title
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.xhtml_H4Type = xhtml_H4Type
        self.xhtml_H4Type156 = xhtml_H4Type156
        self.xhtml_H4Type247 = xhtml_H4Type247
        self.xhtml_H4Type438 = xhtml_H4Type438
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_H4Type438(self):
        return self.__xhtml_H4Type438

    @xhtml_H4Type438.setter
    def xhtml_H4Type438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type438", None)
        self.__xhtml_H4Type438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType437"):
                opp_val = getattr(old_value, "xhtml_MapType437", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType437"):
                opp_val = getattr(value, "xhtml_MapType437", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType437", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H4Type156(self):
        return self.__xhtml_H4Type156

    @xhtml_H4Type156.setter
    def xhtml_H4Type156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type156", None)
        self.__xhtml_H4Type156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot155"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot155"):
                opp_val = getattr(value, "xhtml_DocumentRoot155", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H4Type247(self):
        return self.__xhtml_H4Type247

    @xhtml_H4Type247.setter
    def xhtml_H4Type247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type247", None)
        self.__xhtml_H4Type247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow246"):
                opp_val = getattr(old_value, "xhtml_Flow246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow246"):
                opp_val = getattr(value, "xhtml_Flow246", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H4Type(self):
        return self.__xhtml_H4Type

    @xhtml_H4Type.setter
    def xhtml_H4Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type", None)
        self.__xhtml_H4Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block53"):
                opp_val = getattr(old_value, "xhtml_Block53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block53"):
                opp_val = getattr(value, "xhtml_Block53", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DfnType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_DfnType: "xhtml_AContent" = None, xhtml_DfnType132: "xhtml_DocumentRoot" = None, xhtml_DfnType322: "xhtml_Flow" = None, xhtml_DfnType393: "xhtml_Inline" = None, xhtml_DfnType503: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_DfnType = xhtml_DfnType
        self.xhtml_DfnType132 = xhtml_DfnType132
        self.xhtml_DfnType322 = xhtml_DfnType322
        self.xhtml_DfnType393 = xhtml_DfnType393
        self.xhtml_DfnType503 = xhtml_DfnType503
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_DfnType503(self):
        return self.__xhtml_DfnType503

    @xhtml_DfnType503.setter
    def xhtml_DfnType503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType503", None)
        self.__xhtml_DfnType503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent502"):
                opp_val = getattr(old_value, "xhtml_PreContent502", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent502"):
                opp_val = getattr(value, "xhtml_PreContent502", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent502", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType393(self):
        return self.__xhtml_DfnType393

    @xhtml_DfnType393.setter
    def xhtml_DfnType393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType393", None)
        self.__xhtml_DfnType393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline392"):
                opp_val = getattr(old_value, "xhtml_Inline392", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline392"):
                opp_val = getattr(value, "xhtml_Inline392", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline392", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType132(self):
        return self.__xhtml_DfnType132

    @xhtml_DfnType132.setter
    def xhtml_DfnType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType132", None)
        self.__xhtml_DfnType132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot131"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot131"):
                opp_val = getattr(value, "xhtml_DocumentRoot131", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType(self):
        return self.__xhtml_DfnType

    @xhtml_DfnType.setter
    def xhtml_DfnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType", None)
        self.__xhtml_DfnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent24"):
                opp_val = getattr(old_value, "xhtml_AContent24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent24"):
                opp_val = getattr(value, "xhtml_AContent24", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType322(self):
        return self.__xhtml_DfnType322

    @xhtml_DfnType322.setter
    def xhtml_DfnType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType322", None)
        self.__xhtml_DfnType322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow321"):
                opp_val = getattr(old_value, "xhtml_Flow321", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow321"):
                opp_val = getattr(value, "xhtml_Flow321", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow321", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SampType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_SampType: "xhtml_AContent" = None, xhtml_SampType194: "xhtml_DocumentRoot" = None, xhtml_SampType331: "xhtml_Flow" = None, xhtml_SampType402: "xhtml_Inline" = None, xhtml_SampType512: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_SampType = xhtml_SampType
        self.xhtml_SampType194 = xhtml_SampType194
        self.xhtml_SampType331 = xhtml_SampType331
        self.xhtml_SampType402 = xhtml_SampType402
        self.xhtml_SampType512 = xhtml_SampType512
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_SampType402(self):
        return self.__xhtml_SampType402

    @xhtml_SampType402.setter
    def xhtml_SampType402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType402", None)
        self.__xhtml_SampType402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline401"):
                opp_val = getattr(old_value, "xhtml_Inline401", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline401"):
                opp_val = getattr(value, "xhtml_Inline401", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline401", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType(self):
        return self.__xhtml_SampType

    @xhtml_SampType.setter
    def xhtml_SampType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType", None)
        self.__xhtml_SampType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent30"):
                opp_val = getattr(old_value, "xhtml_AContent30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent30"):
                opp_val = getattr(value, "xhtml_AContent30", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType194(self):
        return self.__xhtml_SampType194

    @xhtml_SampType194.setter
    def xhtml_SampType194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType194", None)
        self.__xhtml_SampType194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot193"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot193"):
                opp_val = getattr(value, "xhtml_DocumentRoot193", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType331(self):
        return self.__xhtml_SampType331

    @xhtml_SampType331.setter
    def xhtml_SampType331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType331", None)
        self.__xhtml_SampType331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow330"):
                opp_val = getattr(old_value, "xhtml_Flow330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow330"):
                opp_val = getattr(value, "xhtml_Flow330", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType512(self):
        return self.__xhtml_SampType512

    @xhtml_SampType512.setter
    def xhtml_SampType512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType512", None)
        self.__xhtml_SampType512 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent511"):
                opp_val = getattr(old_value, "xhtml_PreContent511", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent511"):
                opp_val = getattr(value, "xhtml_PreContent511", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent511", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BigType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_BigType: "xhtml_AContent" = None, xhtml_BigType106: "xhtml_DocumentRoot" = None, xhtml_BigType310: "xhtml_Flow" = None, xhtml_BigType381: "xhtml_Inline" = None, xhtml_BigType491: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_BigType = xhtml_BigType
        self.xhtml_BigType106 = xhtml_BigType106
        self.xhtml_BigType310 = xhtml_BigType310
        self.xhtml_BigType381 = xhtml_BigType381
        self.xhtml_BigType491 = xhtml_BigType491
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def xhtml_BigType(self):
        return self.__xhtml_BigType

    @xhtml_BigType.setter
    def xhtml_BigType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType", None)
        self.__xhtml_BigType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent16"):
                opp_val = getattr(old_value, "xhtml_AContent16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent16"):
                opp_val = getattr(value, "xhtml_AContent16", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType106(self):
        return self.__xhtml_BigType106

    @xhtml_BigType106.setter
    def xhtml_BigType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType106", None)
        self.__xhtml_BigType106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot105"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot105"):
                opp_val = getattr(value, "xhtml_DocumentRoot105", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType310(self):
        return self.__xhtml_BigType310

    @xhtml_BigType310.setter
    def xhtml_BigType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType310", None)
        self.__xhtml_BigType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow309"):
                opp_val = getattr(old_value, "xhtml_Flow309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow309"):
                opp_val = getattr(value, "xhtml_Flow309", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow309", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType491(self):
        return self.__xhtml_BigType491

    @xhtml_BigType491.setter
    def xhtml_BigType491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType491", None)
        self.__xhtml_BigType491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent490"):
                opp_val = getattr(old_value, "xhtml_PreContent490", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent490"):
                opp_val = getattr(value, "xhtml_PreContent490", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent490", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType381(self):
        return self.__xhtml_BigType381

    @xhtml_BigType381.setter
    def xhtml_BigType381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType381", None)
        self.__xhtml_BigType381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline380"):
                opp_val = getattr(old_value, "xhtml_Inline380", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline380"):
                opp_val = getattr(value, "xhtml_Inline380", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline380", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DtType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_DtType: "xhtml_DlType" = None, xhtml_DtType141: "xhtml_DocumentRoot" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_DtType = xhtml_DtType
        self.xhtml_DtType141 = xhtml_DtType141
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_DtType(self):
        return self.__xhtml_DtType

    @xhtml_DtType.setter
    def xhtml_DtType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DtType__xhtml_DtType", None)
        self.__xhtml_DtType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DlType78"):
                opp_val = getattr(old_value, "xhtml_DlType78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DlType78"):
                opp_val = getattr(value, "xhtml_DlType78", None)
                if opp_val is None:
                    setattr(value, "xhtml_DlType78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DtType141(self):
        return self.__xhtml_DtType141

    @xhtml_DtType141.setter
    def xhtml_DtType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DtType__xhtml_DtType141", None)
        self.__xhtml_DtType141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot140"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot140"):
                opp_val = getattr(value, "xhtml_DocumentRoot140", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SubType(Inline):

    def __init__(self, class: str, dir: str, lang: str, lang1: str, style: str, title: str, id: str, xhtml_SubType: "xhtml_AContent" = None, xhtml_SubType206: "xhtml_DocumentRoot" = None, xhtml_SubType349: "xhtml_Flow" = None, xhtml_SubType420: "xhtml_Inline" = None, xhtml_SubType530: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.id = id
        self.xhtml_SubType = xhtml_SubType
        self.xhtml_SubType206 = xhtml_SubType206
        self.xhtml_SubType349 = xhtml_SubType349
        self.xhtml_SubType420 = xhtml_SubType420
        self.xhtml_SubType530 = xhtml_SubType530
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_SubType420(self):
        return self.__xhtml_SubType420

    @xhtml_SubType420.setter
    def xhtml_SubType420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType420", None)
        self.__xhtml_SubType420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline419"):
                opp_val = getattr(old_value, "xhtml_Inline419", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline419"):
                opp_val = getattr(value, "xhtml_Inline419", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline419", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType349(self):
        return self.__xhtml_SubType349

    @xhtml_SubType349.setter
    def xhtml_SubType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType349", None)
        self.__xhtml_SubType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow348"):
                opp_val = getattr(old_value, "xhtml_Flow348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow348"):
                opp_val = getattr(value, "xhtml_Flow348", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType(self):
        return self.__xhtml_SubType

    @xhtml_SubType.setter
    def xhtml_SubType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType", None)
        self.__xhtml_SubType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent42"):
                opp_val = getattr(old_value, "xhtml_AContent42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent42"):
                opp_val = getattr(value, "xhtml_AContent42", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType530(self):
        return self.__xhtml_SubType530

    @xhtml_SubType530.setter
    def xhtml_SubType530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType530", None)
        self.__xhtml_SubType530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent529"):
                opp_val = getattr(old_value, "xhtml_PreContent529", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent529"):
                opp_val = getattr(value, "xhtml_PreContent529", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent529", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType206(self):
        return self.__xhtml_SubType206

    @xhtml_SubType206.setter
    def xhtml_SubType206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType206", None)
        self.__xhtml_SubType206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot205"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot205"):
                opp_val = getattr(value, "xhtml_DocumentRoot205", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SmallType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_SmallType: "xhtml_AContent" = None, xhtml_SmallType197: "xhtml_DocumentRoot" = None, xhtml_SmallType313: "xhtml_Flow" = None, xhtml_SmallType384: "xhtml_Inline" = None, xhtml_SmallType494: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_SmallType = xhtml_SmallType
        self.xhtml_SmallType197 = xhtml_SmallType197
        self.xhtml_SmallType313 = xhtml_SmallType313
        self.xhtml_SmallType384 = xhtml_SmallType384
        self.xhtml_SmallType494 = xhtml_SmallType494
        
    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_SmallType197(self):
        return self.__xhtml_SmallType197

    @xhtml_SmallType197.setter
    def xhtml_SmallType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType197", None)
        self.__xhtml_SmallType197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot196"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot196"):
                opp_val = getattr(value, "xhtml_DocumentRoot196", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType384(self):
        return self.__xhtml_SmallType384

    @xhtml_SmallType384.setter
    def xhtml_SmallType384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType384", None)
        self.__xhtml_SmallType384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline383"):
                opp_val = getattr(old_value, "xhtml_Inline383", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline383"):
                opp_val = getattr(value, "xhtml_Inline383", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline383", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType494(self):
        return self.__xhtml_SmallType494

    @xhtml_SmallType494.setter
    def xhtml_SmallType494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType494", None)
        self.__xhtml_SmallType494 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent493"):
                opp_val = getattr(old_value, "xhtml_PreContent493", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent493"):
                opp_val = getattr(value, "xhtml_PreContent493", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent493", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType313(self):
        return self.__xhtml_SmallType313

    @xhtml_SmallType313.setter
    def xhtml_SmallType313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType313", None)
        self.__xhtml_SmallType313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow312"):
                opp_val = getattr(old_value, "xhtml_Flow312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow312"):
                opp_val = getattr(value, "xhtml_Flow312", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType(self):
        return self.__xhtml_SmallType

    @xhtml_SmallType.setter
    def xhtml_SmallType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType", None)
        self.__xhtml_SmallType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent18"):
                opp_val = getattr(old_value, "xhtml_AContent18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent18"):
                opp_val = getattr(value, "xhtml_AContent18", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CiteType(Inline):

    def __init__(self, dir: str, id: str, lang: str, lang1: str, class: str, style: str, title: str, xhtml_CiteType: "xhtml_AContent" = None, xhtml_CiteType117: "xhtml_DocumentRoot" = None, xhtml_CiteType340: "xhtml_Flow" = None, xhtml_CiteType411: "xhtml_Inline" = None, xhtml_CiteType521: "xhtml_PreContent" = None):
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.class = class
        self.style = style
        self.title = title
        self.xhtml_CiteType = xhtml_CiteType
        self.xhtml_CiteType117 = xhtml_CiteType117
        self.xhtml_CiteType340 = xhtml_CiteType340
        self.xhtml_CiteType411 = xhtml_CiteType411
        self.xhtml_CiteType521 = xhtml_CiteType521
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def xhtml_CiteType521(self):
        return self.__xhtml_CiteType521

    @xhtml_CiteType521.setter
    def xhtml_CiteType521(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType521", None)
        self.__xhtml_CiteType521 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent520"):
                opp_val = getattr(old_value, "xhtml_PreContent520", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent520"):
                opp_val = getattr(value, "xhtml_PreContent520", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent520", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType(self):
        return self.__xhtml_CiteType

    @xhtml_CiteType.setter
    def xhtml_CiteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType", None)
        self.__xhtml_CiteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent36"):
                opp_val = getattr(old_value, "xhtml_AContent36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent36"):
                opp_val = getattr(value, "xhtml_AContent36", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType117(self):
        return self.__xhtml_CiteType117

    @xhtml_CiteType117.setter
    def xhtml_CiteType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType117", None)
        self.__xhtml_CiteType117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot116"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot116"):
                opp_val = getattr(value, "xhtml_DocumentRoot116", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType411(self):
        return self.__xhtml_CiteType411

    @xhtml_CiteType411.setter
    def xhtml_CiteType411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType411", None)
        self.__xhtml_CiteType411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline410"):
                opp_val = getattr(old_value, "xhtml_Inline410", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline410"):
                opp_val = getattr(value, "xhtml_Inline410", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline410", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType340(self):
        return self.__xhtml_CiteType340

    @xhtml_CiteType340.setter
    def xhtml_CiteType340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType340", None)
        self.__xhtml_CiteType340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow339"):
                opp_val = getattr(old_value, "xhtml_Flow339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow339"):
                opp_val = getattr(value, "xhtml_Flow339", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow339", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H6Type(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_H6Type: "xhtml_Block" = None, xhtml_H6Type162: "xhtml_DocumentRoot" = None, xhtml_H6Type253: "xhtml_Flow" = None, xhtml_H6Type444: "xhtml_MapType" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_H6Type = xhtml_H6Type
        self.xhtml_H6Type162 = xhtml_H6Type162
        self.xhtml_H6Type253 = xhtml_H6Type253
        self.xhtml_H6Type444 = xhtml_H6Type444
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_H6Type162(self):
        return self.__xhtml_H6Type162

    @xhtml_H6Type162.setter
    def xhtml_H6Type162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type162", None)
        self.__xhtml_H6Type162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot161"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot161"):
                opp_val = getattr(value, "xhtml_DocumentRoot161", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H6Type444(self):
        return self.__xhtml_H6Type444

    @xhtml_H6Type444.setter
    def xhtml_H6Type444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type444", None)
        self.__xhtml_H6Type444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_MapType443"):
                opp_val = getattr(old_value, "xhtml_MapType443", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_MapType443"):
                opp_val = getattr(value, "xhtml_MapType443", None)
                if opp_val is None:
                    setattr(value, "xhtml_MapType443", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H6Type(self):
        return self.__xhtml_H6Type

    @xhtml_H6Type.setter
    def xhtml_H6Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type", None)
        self.__xhtml_H6Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block57"):
                opp_val = getattr(old_value, "xhtml_Block57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block57"):
                opp_val = getattr(value, "xhtml_Block57", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H6Type253(self):
        return self.__xhtml_H6Type253

    @xhtml_H6Type253.setter
    def xhtml_H6Type253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type253", None)
        self.__xhtml_H6Type253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow252"):
                opp_val = getattr(old_value, "xhtml_Flow252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow252"):
                opp_val = getattr(value, "xhtml_Flow252", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BdoType(Inline):

    def __init__(self, lang: str, lang1: str, style: str, title: str, class: str, dir: str, id: str, xhtml_BdoType: "xhtml_AContent" = None, xhtml_BdoType103: "xhtml_DocumentRoot" = None, xhtml_BdoType292: "xhtml_Flow" = None, xhtml_BdoType363: "xhtml_Inline" = None, xhtml_BdoType542: "xhtml_PreContent" = None):
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.class = class
        self.dir = dir
        self.id = id
        self.xhtml_BdoType = xhtml_BdoType
        self.xhtml_BdoType103 = xhtml_BdoType103
        self.xhtml_BdoType292 = xhtml_BdoType292
        self.xhtml_BdoType363 = xhtml_BdoType363
        self.xhtml_BdoType542 = xhtml_BdoType542
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_BdoType(self):
        return self.__xhtml_BdoType

    @xhtml_BdoType.setter
    def xhtml_BdoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BdoType__xhtml_BdoType", None)
        self.__xhtml_BdoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent4"):
                opp_val = getattr(old_value, "xhtml_AContent4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent4"):
                opp_val = getattr(value, "xhtml_AContent4", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BdoType363(self):
        return self.__xhtml_BdoType363

    @xhtml_BdoType363.setter
    def xhtml_BdoType363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BdoType__xhtml_BdoType363", None)
        self.__xhtml_BdoType363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline362"):
                opp_val = getattr(old_value, "xhtml_Inline362", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline362"):
                opp_val = getattr(value, "xhtml_Inline362", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline362", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BdoType103(self):
        return self.__xhtml_BdoType103

    @xhtml_BdoType103.setter
    def xhtml_BdoType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BdoType__xhtml_BdoType103", None)
        self.__xhtml_BdoType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot102"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot102"):
                opp_val = getattr(value, "xhtml_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BdoType292(self):
        return self.__xhtml_BdoType292

    @xhtml_BdoType292.setter
    def xhtml_BdoType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BdoType__xhtml_BdoType292", None)
        self.__xhtml_BdoType292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow291"):
                opp_val = getattr(old_value, "xhtml_Flow291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow291"):
                opp_val = getattr(value, "xhtml_Flow291", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BdoType542(self):
        return self.__xhtml_BdoType542

    @xhtml_BdoType542.setter
    def xhtml_BdoType542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BdoType__xhtml_BdoType542", None)
        self.__xhtml_BdoType542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent541"):
                opp_val = getattr(old_value, "xhtml_PreContent541", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent541"):
                opp_val = getattr(value, "xhtml_PreContent541", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent541", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SpanType(Inline):

    def __init__(self, class: str, dir: str, lang: str, lang1: str, style: str, title: str, id: str, xhtml_SpanType: "xhtml_AContent" = None, xhtml_SpanType200: "xhtml_DocumentRoot" = None, xhtml_SpanType289: "xhtml_Flow" = None, xhtml_SpanType360: "xhtml_Inline" = None, xhtml_SpanType539: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.id = id
        self.xhtml_SpanType = xhtml_SpanType
        self.xhtml_SpanType200 = xhtml_SpanType200
        self.xhtml_SpanType289 = xhtml_SpanType289
        self.xhtml_SpanType360 = xhtml_SpanType360
        self.xhtml_SpanType539 = xhtml_SpanType539
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_SpanType289(self):
        return self.__xhtml_SpanType289

    @xhtml_SpanType289.setter
    def xhtml_SpanType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType289", None)
        self.__xhtml_SpanType289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow288"):
                opp_val = getattr(old_value, "xhtml_Flow288", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow288"):
                opp_val = getattr(value, "xhtml_Flow288", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow288", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType(self):
        return self.__xhtml_SpanType

    @xhtml_SpanType.setter
    def xhtml_SpanType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType", None)
        self.__xhtml_SpanType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent2"):
                opp_val = getattr(old_value, "xhtml_AContent2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent2"):
                opp_val = getattr(value, "xhtml_AContent2", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType539(self):
        return self.__xhtml_SpanType539

    @xhtml_SpanType539.setter
    def xhtml_SpanType539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType539", None)
        self.__xhtml_SpanType539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent538"):
                opp_val = getattr(old_value, "xhtml_PreContent538", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent538"):
                opp_val = getattr(value, "xhtml_PreContent538", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent538", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType200(self):
        return self.__xhtml_SpanType200

    @xhtml_SpanType200.setter
    def xhtml_SpanType200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType200", None)
        self.__xhtml_SpanType200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot199"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot199"):
                opp_val = getattr(value, "xhtml_DocumentRoot199", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType360(self):
        return self.__xhtml_SpanType360

    @xhtml_SpanType360.setter
    def xhtml_SpanType360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType360", None)
        self.__xhtml_SpanType360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline359"):
                opp_val = getattr(old_value, "xhtml_Inline359", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline359"):
                opp_val = getattr(value, "xhtml_Inline359", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline359", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BrType:

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_BrType: "xhtml_AContent" = None, xhtml_BrType112: "xhtml_DocumentRoot" = None, xhtml_BrType286: "xhtml_Flow" = None, xhtml_BrType357: "xhtml_Inline" = None, xhtml_BrType536: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BrType = xhtml_BrType
        self.xhtml_BrType112 = xhtml_BrType112
        self.xhtml_BrType286 = xhtml_BrType286
        self.xhtml_BrType357 = xhtml_BrType357
        self.xhtml_BrType536 = xhtml_BrType536
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_BrType536(self):
        return self.__xhtml_BrType536

    @xhtml_BrType536.setter
    def xhtml_BrType536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType536", None)
        self.__xhtml_BrType536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent535"):
                opp_val = getattr(old_value, "xhtml_PreContent535", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent535"):
                opp_val = getattr(value, "xhtml_PreContent535", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent535", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType357(self):
        return self.__xhtml_BrType357

    @xhtml_BrType357.setter
    def xhtml_BrType357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType357", None)
        self.__xhtml_BrType357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline356"):
                opp_val = getattr(old_value, "xhtml_Inline356", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline356"):
                opp_val = getattr(value, "xhtml_Inline356", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline356", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType286(self):
        return self.__xhtml_BrType286

    @xhtml_BrType286.setter
    def xhtml_BrType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType286", None)
        self.__xhtml_BrType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow285"):
                opp_val = getattr(old_value, "xhtml_Flow285", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow285"):
                opp_val = getattr(value, "xhtml_Flow285", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow285", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType112(self):
        return self.__xhtml_BrType112

    @xhtml_BrType112.setter
    def xhtml_BrType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType112", None)
        self.__xhtml_BrType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot111"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot111"):
                opp_val = getattr(value, "xhtml_DocumentRoot111", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType(self):
        return self.__xhtml_BrType

    @xhtml_BrType.setter
    def xhtml_BrType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType", None)
        self.__xhtml_BrType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent"):
                opp_val = getattr(old_value, "xhtml_AContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent"):
                opp_val = getattr(value, "xhtml_AContent", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AbbrType(Inline):

    def __init__(self, class: str, dir: str, id: str, lang: str, lang1: str, style: str, title: str, xhtml_AbbrType: "xhtml_AContent" = None, xhtml_AbbrType89: "xhtml_DocumentRoot" = None, xhtml_AbbrType343: "xhtml_Flow" = None, xhtml_AbbrType414: "xhtml_Inline" = None, xhtml_AbbrType524: "xhtml_PreContent" = None):
        self.class = class
        self.dir = dir
        self.id = id
        self.lang = lang
        self.lang1 = lang1
        self.style = style
        self.title = title
        self.xhtml_AbbrType = xhtml_AbbrType
        self.xhtml_AbbrType89 = xhtml_AbbrType89
        self.xhtml_AbbrType343 = xhtml_AbbrType343
        self.xhtml_AbbrType414 = xhtml_AbbrType414
        self.xhtml_AbbrType524 = xhtml_AbbrType524
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang1(self) -> str:
        return self.__lang1

    @lang1.setter
    def lang1(self, lang1: str):
        self.__lang1 = lang1

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_AbbrType524(self):
        return self.__xhtml_AbbrType524

    @xhtml_AbbrType524.setter
    def xhtml_AbbrType524(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType524", None)
        self.__xhtml_AbbrType524 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent523"):
                opp_val = getattr(old_value, "xhtml_PreContent523", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent523"):
                opp_val = getattr(value, "xhtml_PreContent523", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent523", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType414(self):
        return self.__xhtml_AbbrType414

    @xhtml_AbbrType414.setter
    def xhtml_AbbrType414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType414", None)
        self.__xhtml_AbbrType414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline413"):
                opp_val = getattr(old_value, "xhtml_Inline413", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline413"):
                opp_val = getattr(value, "xhtml_Inline413", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline413", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType343(self):
        return self.__xhtml_AbbrType343

    @xhtml_AbbrType343.setter
    def xhtml_AbbrType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType343", None)
        self.__xhtml_AbbrType343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow342"):
                opp_val = getattr(old_value, "xhtml_Flow342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow342"):
                opp_val = getattr(value, "xhtml_Flow342", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType89(self):
        return self.__xhtml_AbbrType89

    @xhtml_AbbrType89.setter
    def xhtml_AbbrType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType89", None)
        self.__xhtml_AbbrType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot88"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot88"):
                opp_val = getattr(value, "xhtml_DocumentRoot88", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType(self):
        return self.__xhtml_AbbrType

    @xhtml_AbbrType.setter
    def xhtml_AbbrType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType", None)
        self.__xhtml_AbbrType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent38"):
                opp_val = getattr(old_value, "xhtml_AContent38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent38"):
                opp_val = getattr(value, "xhtml_AContent38", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
