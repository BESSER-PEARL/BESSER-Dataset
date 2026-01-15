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
class DeclareType(Enum):
    declare = "declare"
class Scope(Enum):
    row = "row"
    col = "col"
    rowgroup = "rowgroup"
    colgroup = "colgroup"
class IsmapType(Enum):
    ismap = "ismap"
class ValuetypeType(Enum):
    data = "data"
    ref = "ref"
    object = "object"
class AlignType(Enum):
    left = "left"
    center = "center"
    right = "right"
    justify = "justify"
    char = "char"
class ValignType(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"
    baseline = "baseline"


############################################
# Definition of Classes
############################################

class PreContent:

    pass
class xhtml_PreContent:

    def __init__(self, mixed: str, group: str, xhtml_PreContent: set["xhtml_AType"] = None, xhtml_PreContent661: set["xhtml_TtType"] = None, xhtml_PreContent664: set["xhtml_IType"] = None, xhtml_PreContent667: set["xhtml_BType"] = None, xhtml_PreContent670: set["xhtml_BigType"] = None, xhtml_PreContent676: set["xhtml_UType"] = None, xhtml_PreContent679: set["xhtml_StrikeType"] = None, xhtml_PreContent682: set["xhtml_EmType"] = None, xhtml_PreContent685: set["xhtml_StrongType"] = None, xhtml_PreContent688: set["xhtml_DfnType"] = None, xhtml_PreContent691: set["xhtml_CodeType"] = None, xhtml_PreContent694: set["xhtml_QType"] = None, xhtml_PreContent697: set["xhtml_SampType"] = None, xhtml_PreContent673: set["xhtml_SmallType"] = None, xhtml_PreContent700: set["xhtml_KbdType"] = None, xhtml_PreContent703: set["xhtml_VarType"] = None, xhtml_PreContent706: set["xhtml_CiteType"] = None, xhtml_PreContent709: set["xhtml_AbbrType"] = None, xhtml_PreContent712: set["xhtml_AcronymType"] = None, xhtml_PreContent715: set["xhtml_SubType"] = None, xhtml_PreContent721: set["xhtml_BrType"] = None, xhtml_PreContent724: set["xhtml_SpanType"] = None, xhtml_PreContent727: set["xhtml_InsType"] = None, xhtml_PreContent730: set["xhtml_DelType"] = None, xhtml_PreContent718: set["xhtml_SupType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_PreContent = xhtml_PreContent if xhtml_PreContent is not None else set()
        self.xhtml_PreContent661 = xhtml_PreContent661 if xhtml_PreContent661 is not None else set()
        self.xhtml_PreContent664 = xhtml_PreContent664 if xhtml_PreContent664 is not None else set()
        self.xhtml_PreContent667 = xhtml_PreContent667 if xhtml_PreContent667 is not None else set()
        self.xhtml_PreContent670 = xhtml_PreContent670 if xhtml_PreContent670 is not None else set()
        self.xhtml_PreContent676 = xhtml_PreContent676 if xhtml_PreContent676 is not None else set()
        self.xhtml_PreContent679 = xhtml_PreContent679 if xhtml_PreContent679 is not None else set()
        self.xhtml_PreContent682 = xhtml_PreContent682 if xhtml_PreContent682 is not None else set()
        self.xhtml_PreContent685 = xhtml_PreContent685 if xhtml_PreContent685 is not None else set()
        self.xhtml_PreContent688 = xhtml_PreContent688 if xhtml_PreContent688 is not None else set()
        self.xhtml_PreContent691 = xhtml_PreContent691 if xhtml_PreContent691 is not None else set()
        self.xhtml_PreContent694 = xhtml_PreContent694 if xhtml_PreContent694 is not None else set()
        self.xhtml_PreContent697 = xhtml_PreContent697 if xhtml_PreContent697 is not None else set()
        self.xhtml_PreContent673 = xhtml_PreContent673 if xhtml_PreContent673 is not None else set()
        self.xhtml_PreContent700 = xhtml_PreContent700 if xhtml_PreContent700 is not None else set()
        self.xhtml_PreContent703 = xhtml_PreContent703 if xhtml_PreContent703 is not None else set()
        self.xhtml_PreContent706 = xhtml_PreContent706 if xhtml_PreContent706 is not None else set()
        self.xhtml_PreContent709 = xhtml_PreContent709 if xhtml_PreContent709 is not None else set()
        self.xhtml_PreContent712 = xhtml_PreContent712 if xhtml_PreContent712 is not None else set()
        self.xhtml_PreContent715 = xhtml_PreContent715 if xhtml_PreContent715 is not None else set()
        self.xhtml_PreContent721 = xhtml_PreContent721 if xhtml_PreContent721 is not None else set()
        self.xhtml_PreContent724 = xhtml_PreContent724 if xhtml_PreContent724 is not None else set()
        self.xhtml_PreContent727 = xhtml_PreContent727 if xhtml_PreContent727 is not None else set()
        self.xhtml_PreContent730 = xhtml_PreContent730 if xhtml_PreContent730 is not None else set()
        self.xhtml_PreContent718 = xhtml_PreContent718 if xhtml_PreContent718 is not None else set()
        
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
    def xhtml_PreContent679(self):
        return self.__xhtml_PreContent679

    @xhtml_PreContent679.setter
    def xhtml_PreContent679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent679", None)
        self.__xhtml_PreContent679 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrikeType680"):
                    opp_val = getattr(item, "xhtml_StrikeType680", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType680", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType680"):
                    opp_val = getattr(item, "xhtml_StrikeType680", None)
                    
                    setattr(item, "xhtml_StrikeType680", self)
                    

    @property
    def xhtml_PreContent727(self):
        return self.__xhtml_PreContent727

    @xhtml_PreContent727.setter
    def xhtml_PreContent727(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent727", None)
        self.__xhtml_PreContent727 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType728"):
                    opp_val = getattr(item, "xhtml_InsType728", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType728", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType728"):
                    opp_val = getattr(item, "xhtml_InsType728", None)
                    
                    setattr(item, "xhtml_InsType728", self)
                    

    @property
    def xhtml_PreContent712(self):
        return self.__xhtml_PreContent712

    @xhtml_PreContent712.setter
    def xhtml_PreContent712(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent712", None)
        self.__xhtml_PreContent712 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType713"):
                    opp_val = getattr(item, "xhtml_AcronymType713", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType713", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType713"):
                    opp_val = getattr(item, "xhtml_AcronymType713", None)
                    
                    setattr(item, "xhtml_AcronymType713", self)
                    

    @property
    def xhtml_PreContent673(self):
        return self.__xhtml_PreContent673

    @xhtml_PreContent673.setter
    def xhtml_PreContent673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent673", None)
        self.__xhtml_PreContent673 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType674"):
                    opp_val = getattr(item, "xhtml_SmallType674", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType674", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType674"):
                    opp_val = getattr(item, "xhtml_SmallType674", None)
                    
                    setattr(item, "xhtml_SmallType674", self)
                    

    @property
    def xhtml_PreContent682(self):
        return self.__xhtml_PreContent682

    @xhtml_PreContent682.setter
    def xhtml_PreContent682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent682", None)
        self.__xhtml_PreContent682 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType683"):
                    opp_val = getattr(item, "xhtml_EmType683", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType683"):
                    opp_val = getattr(item, "xhtml_EmType683", None)
                    
                    setattr(item, "xhtml_EmType683", self)
                    

    @property
    def xhtml_PreContent724(self):
        return self.__xhtml_PreContent724

    @xhtml_PreContent724.setter
    def xhtml_PreContent724(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent724", None)
        self.__xhtml_PreContent724 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType725"):
                    opp_val = getattr(item, "xhtml_SpanType725", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType725", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType725"):
                    opp_val = getattr(item, "xhtml_SpanType725", None)
                    
                    setattr(item, "xhtml_SpanType725", self)
                    

    @property
    def xhtml_PreContent700(self):
        return self.__xhtml_PreContent700

    @xhtml_PreContent700.setter
    def xhtml_PreContent700(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent700", None)
        self.__xhtml_PreContent700 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType701"):
                    opp_val = getattr(item, "xhtml_KbdType701", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType701", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType701"):
                    opp_val = getattr(item, "xhtml_KbdType701", None)
                    
                    setattr(item, "xhtml_KbdType701", self)
                    

    @property
    def xhtml_PreContent715(self):
        return self.__xhtml_PreContent715

    @xhtml_PreContent715.setter
    def xhtml_PreContent715(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent715", None)
        self.__xhtml_PreContent715 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType716"):
                    opp_val = getattr(item, "xhtml_SubType716", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType716", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType716"):
                    opp_val = getattr(item, "xhtml_SubType716", None)
                    
                    setattr(item, "xhtml_SubType716", self)
                    

    @property
    def xhtml_PreContent718(self):
        return self.__xhtml_PreContent718

    @xhtml_PreContent718.setter
    def xhtml_PreContent718(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent718", None)
        self.__xhtml_PreContent718 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType719"):
                    opp_val = getattr(item, "xhtml_SupType719", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType719", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType719"):
                    opp_val = getattr(item, "xhtml_SupType719", None)
                    
                    setattr(item, "xhtml_SupType719", self)
                    

    @property
    def xhtml_PreContent706(self):
        return self.__xhtml_PreContent706

    @xhtml_PreContent706.setter
    def xhtml_PreContent706(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent706", None)
        self.__xhtml_PreContent706 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType707"):
                    opp_val = getattr(item, "xhtml_CiteType707", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType707", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType707"):
                    opp_val = getattr(item, "xhtml_CiteType707", None)
                    
                    setattr(item, "xhtml_CiteType707", self)
                    

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
                if hasattr(item, "xhtml_AType659"):
                    opp_val = getattr(item, "xhtml_AType659", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType659", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType659"):
                    opp_val = getattr(item, "xhtml_AType659", None)
                    
                    setattr(item, "xhtml_AType659", self)
                    

    @property
    def xhtml_PreContent721(self):
        return self.__xhtml_PreContent721

    @xhtml_PreContent721.setter
    def xhtml_PreContent721(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent721", None)
        self.__xhtml_PreContent721 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType722"):
                    opp_val = getattr(item, "xhtml_BrType722", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType722", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType722"):
                    opp_val = getattr(item, "xhtml_BrType722", None)
                    
                    setattr(item, "xhtml_BrType722", self)
                    

    @property
    def xhtml_PreContent730(self):
        return self.__xhtml_PreContent730

    @xhtml_PreContent730.setter
    def xhtml_PreContent730(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent730", None)
        self.__xhtml_PreContent730 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType731"):
                    opp_val = getattr(item, "xhtml_DelType731", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType731", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType731"):
                    opp_val = getattr(item, "xhtml_DelType731", None)
                    
                    setattr(item, "xhtml_DelType731", self)
                    

    @property
    def xhtml_PreContent661(self):
        return self.__xhtml_PreContent661

    @xhtml_PreContent661.setter
    def xhtml_PreContent661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent661", None)
        self.__xhtml_PreContent661 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType662"):
                    opp_val = getattr(item, "xhtml_TtType662", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType662", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType662"):
                    opp_val = getattr(item, "xhtml_TtType662", None)
                    
                    setattr(item, "xhtml_TtType662", self)
                    

    @property
    def xhtml_PreContent703(self):
        return self.__xhtml_PreContent703

    @xhtml_PreContent703.setter
    def xhtml_PreContent703(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent703", None)
        self.__xhtml_PreContent703 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType704"):
                    opp_val = getattr(item, "xhtml_VarType704", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType704", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType704"):
                    opp_val = getattr(item, "xhtml_VarType704", None)
                    
                    setattr(item, "xhtml_VarType704", self)
                    

    @property
    def xhtml_PreContent697(self):
        return self.__xhtml_PreContent697

    @xhtml_PreContent697.setter
    def xhtml_PreContent697(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent697", None)
        self.__xhtml_PreContent697 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType698"):
                    opp_val = getattr(item, "xhtml_SampType698", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType698", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType698"):
                    opp_val = getattr(item, "xhtml_SampType698", None)
                    
                    setattr(item, "xhtml_SampType698", self)
                    

    @property
    def xhtml_PreContent691(self):
        return self.__xhtml_PreContent691

    @xhtml_PreContent691.setter
    def xhtml_PreContent691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent691", None)
        self.__xhtml_PreContent691 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType692"):
                    opp_val = getattr(item, "xhtml_CodeType692", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType692", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType692"):
                    opp_val = getattr(item, "xhtml_CodeType692", None)
                    
                    setattr(item, "xhtml_CodeType692", self)
                    

    @property
    def xhtml_PreContent694(self):
        return self.__xhtml_PreContent694

    @xhtml_PreContent694.setter
    def xhtml_PreContent694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent694", None)
        self.__xhtml_PreContent694 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType695"):
                    opp_val = getattr(item, "xhtml_QType695", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType695", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType695"):
                    opp_val = getattr(item, "xhtml_QType695", None)
                    
                    setattr(item, "xhtml_QType695", self)
                    

    @property
    def xhtml_PreContent688(self):
        return self.__xhtml_PreContent688

    @xhtml_PreContent688.setter
    def xhtml_PreContent688(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent688", None)
        self.__xhtml_PreContent688 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType689"):
                    opp_val = getattr(item, "xhtml_DfnType689", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType689", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType689"):
                    opp_val = getattr(item, "xhtml_DfnType689", None)
                    
                    setattr(item, "xhtml_DfnType689", self)
                    

    @property
    def xhtml_PreContent667(self):
        return self.__xhtml_PreContent667

    @xhtml_PreContent667.setter
    def xhtml_PreContent667(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent667", None)
        self.__xhtml_PreContent667 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType668"):
                    opp_val = getattr(item, "xhtml_BType668", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType668", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType668"):
                    opp_val = getattr(item, "xhtml_BType668", None)
                    
                    setattr(item, "xhtml_BType668", self)
                    

    @property
    def xhtml_PreContent670(self):
        return self.__xhtml_PreContent670

    @xhtml_PreContent670.setter
    def xhtml_PreContent670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent670", None)
        self.__xhtml_PreContent670 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType671"):
                    opp_val = getattr(item, "xhtml_BigType671", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType671", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType671"):
                    opp_val = getattr(item, "xhtml_BigType671", None)
                    
                    setattr(item, "xhtml_BigType671", self)
                    

    @property
    def xhtml_PreContent664(self):
        return self.__xhtml_PreContent664

    @xhtml_PreContent664.setter
    def xhtml_PreContent664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent664", None)
        self.__xhtml_PreContent664 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType665"):
                    opp_val = getattr(item, "xhtml_IType665", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType665", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType665"):
                    opp_val = getattr(item, "xhtml_IType665", None)
                    
                    setattr(item, "xhtml_IType665", self)
                    

    @property
    def xhtml_PreContent676(self):
        return self.__xhtml_PreContent676

    @xhtml_PreContent676.setter
    def xhtml_PreContent676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent676", None)
        self.__xhtml_PreContent676 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UType677"):
                    opp_val = getattr(item, "xhtml_UType677", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType677", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType677"):
                    opp_val = getattr(item, "xhtml_UType677", None)
                    
                    setattr(item, "xhtml_UType677", self)
                    

    @property
    def xhtml_PreContent685(self):
        return self.__xhtml_PreContent685

    @xhtml_PreContent685.setter
    def xhtml_PreContent685(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent685", None)
        self.__xhtml_PreContent685 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType686"):
                    opp_val = getattr(item, "xhtml_StrongType686", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType686", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType686"):
                    opp_val = getattr(item, "xhtml_StrongType686", None)
                    
                    setattr(item, "xhtml_StrongType686", self)
                    

    @property
    def xhtml_PreContent709(self):
        return self.__xhtml_PreContent709

    @xhtml_PreContent709.setter
    def xhtml_PreContent709(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent709", None)
        self.__xhtml_PreContent709 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType710"):
                    opp_val = getattr(item, "xhtml_AbbrType710", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType710", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType710"):
                    opp_val = getattr(item, "xhtml_AbbrType710", None)
                    
                    setattr(item, "xhtml_AbbrType710", self)
                    

class xhtml_Inline:

    def __init__(self, mixed: str, group: str, xhtml_Inline: set["xhtml_AType"] = None, xhtml_Inline446: set["xhtml_BrType"] = None, xhtml_Inline473: set["xhtml_UType"] = None, xhtml_Inline449: set["xhtml_SpanType"] = None, xhtml_Inline452: set["xhtml_ObjectType"] = None, xhtml_Inline455: set["xhtml_ImgType"] = None, xhtml_Inline458: set["xhtml_TtType"] = None, xhtml_Inline461: set["xhtml_IType"] = None, xhtml_Inline464: set["xhtml_BType"] = None, xhtml_Inline467: set["xhtml_BigType"] = None, xhtml_Inline470: set["xhtml_SmallType"] = None, xhtml_Inline476: set["xhtml_StrikeType"] = None, xhtml_Inline479: set["xhtml_EmType"] = None, xhtml_Inline482: set["xhtml_StrongType"] = None, xhtml_Inline485: set["xhtml_DfnType"] = None, xhtml_Inline488: set["xhtml_CodeType"] = None, xhtml_Inline491: set["xhtml_QType"] = None, xhtml_Inline494: set["xhtml_SampType"] = None, xhtml_Inline497: set["xhtml_KbdType"] = None, xhtml_Inline500: set["xhtml_VarType"] = None, xhtml_Inline503: set["xhtml_CiteType"] = None, xhtml_Inline506: set["xhtml_AbbrType"] = None, xhtml_Inline509: set["xhtml_AcronymType"] = None, xhtml_Inline512: set["xhtml_SubType"] = None, xhtml_Inline515: set["xhtml_SupType"] = None, xhtml_Inline518: set["xhtml_InsType"] = None, xhtml_Inline521: set["xhtml_DelType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_Inline = xhtml_Inline if xhtml_Inline is not None else set()
        self.xhtml_Inline446 = xhtml_Inline446 if xhtml_Inline446 is not None else set()
        self.xhtml_Inline473 = xhtml_Inline473 if xhtml_Inline473 is not None else set()
        self.xhtml_Inline449 = xhtml_Inline449 if xhtml_Inline449 is not None else set()
        self.xhtml_Inline452 = xhtml_Inline452 if xhtml_Inline452 is not None else set()
        self.xhtml_Inline455 = xhtml_Inline455 if xhtml_Inline455 is not None else set()
        self.xhtml_Inline458 = xhtml_Inline458 if xhtml_Inline458 is not None else set()
        self.xhtml_Inline461 = xhtml_Inline461 if xhtml_Inline461 is not None else set()
        self.xhtml_Inline464 = xhtml_Inline464 if xhtml_Inline464 is not None else set()
        self.xhtml_Inline467 = xhtml_Inline467 if xhtml_Inline467 is not None else set()
        self.xhtml_Inline470 = xhtml_Inline470 if xhtml_Inline470 is not None else set()
        self.xhtml_Inline476 = xhtml_Inline476 if xhtml_Inline476 is not None else set()
        self.xhtml_Inline479 = xhtml_Inline479 if xhtml_Inline479 is not None else set()
        self.xhtml_Inline482 = xhtml_Inline482 if xhtml_Inline482 is not None else set()
        self.xhtml_Inline485 = xhtml_Inline485 if xhtml_Inline485 is not None else set()
        self.xhtml_Inline488 = xhtml_Inline488 if xhtml_Inline488 is not None else set()
        self.xhtml_Inline491 = xhtml_Inline491 if xhtml_Inline491 is not None else set()
        self.xhtml_Inline494 = xhtml_Inline494 if xhtml_Inline494 is not None else set()
        self.xhtml_Inline497 = xhtml_Inline497 if xhtml_Inline497 is not None else set()
        self.xhtml_Inline500 = xhtml_Inline500 if xhtml_Inline500 is not None else set()
        self.xhtml_Inline503 = xhtml_Inline503 if xhtml_Inline503 is not None else set()
        self.xhtml_Inline506 = xhtml_Inline506 if xhtml_Inline506 is not None else set()
        self.xhtml_Inline509 = xhtml_Inline509 if xhtml_Inline509 is not None else set()
        self.xhtml_Inline512 = xhtml_Inline512 if xhtml_Inline512 is not None else set()
        self.xhtml_Inline515 = xhtml_Inline515 if xhtml_Inline515 is not None else set()
        self.xhtml_Inline518 = xhtml_Inline518 if xhtml_Inline518 is not None else set()
        self.xhtml_Inline521 = xhtml_Inline521 if xhtml_Inline521 is not None else set()
        
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
    def xhtml_Inline476(self):
        return self.__xhtml_Inline476

    @xhtml_Inline476.setter
    def xhtml_Inline476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline476", None)
        self.__xhtml_Inline476 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrikeType477"):
                    opp_val = getattr(item, "xhtml_StrikeType477", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType477", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType477"):
                    opp_val = getattr(item, "xhtml_StrikeType477", None)
                    
                    setattr(item, "xhtml_StrikeType477", self)
                    

    @property
    def xhtml_Inline473(self):
        return self.__xhtml_Inline473

    @xhtml_Inline473.setter
    def xhtml_Inline473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline473", None)
        self.__xhtml_Inline473 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UType474"):
                    opp_val = getattr(item, "xhtml_UType474", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType474", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType474"):
                    opp_val = getattr(item, "xhtml_UType474", None)
                    
                    setattr(item, "xhtml_UType474", self)
                    

    @property
    def xhtml_Inline503(self):
        return self.__xhtml_Inline503

    @xhtml_Inline503.setter
    def xhtml_Inline503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline503", None)
        self.__xhtml_Inline503 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType504"):
                    opp_val = getattr(item, "xhtml_CiteType504", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType504", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType504"):
                    opp_val = getattr(item, "xhtml_CiteType504", None)
                    
                    setattr(item, "xhtml_CiteType504", self)
                    

    @property
    def xhtml_Inline458(self):
        return self.__xhtml_Inline458

    @xhtml_Inline458.setter
    def xhtml_Inline458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline458", None)
        self.__xhtml_Inline458 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType459"):
                    opp_val = getattr(item, "xhtml_TtType459", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType459", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType459"):
                    opp_val = getattr(item, "xhtml_TtType459", None)
                    
                    setattr(item, "xhtml_TtType459", self)
                    

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
                if hasattr(item, "xhtml_AType444"):
                    opp_val = getattr(item, "xhtml_AType444", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType444", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType444"):
                    opp_val = getattr(item, "xhtml_AType444", None)
                    
                    setattr(item, "xhtml_AType444", self)
                    

    @property
    def xhtml_Inline500(self):
        return self.__xhtml_Inline500

    @xhtml_Inline500.setter
    def xhtml_Inline500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline500", None)
        self.__xhtml_Inline500 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType501"):
                    opp_val = getattr(item, "xhtml_VarType501", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType501", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType501"):
                    opp_val = getattr(item, "xhtml_VarType501", None)
                    
                    setattr(item, "xhtml_VarType501", self)
                    

    @property
    def xhtml_Inline467(self):
        return self.__xhtml_Inline467

    @xhtml_Inline467.setter
    def xhtml_Inline467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline467", None)
        self.__xhtml_Inline467 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType468"):
                    opp_val = getattr(item, "xhtml_BigType468", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType468", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType468"):
                    opp_val = getattr(item, "xhtml_BigType468", None)
                    
                    setattr(item, "xhtml_BigType468", self)
                    

    @property
    def xhtml_Inline512(self):
        return self.__xhtml_Inline512

    @xhtml_Inline512.setter
    def xhtml_Inline512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline512", None)
        self.__xhtml_Inline512 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType513"):
                    opp_val = getattr(item, "xhtml_SubType513", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType513", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType513"):
                    opp_val = getattr(item, "xhtml_SubType513", None)
                    
                    setattr(item, "xhtml_SubType513", self)
                    

    @property
    def xhtml_Inline515(self):
        return self.__xhtml_Inline515

    @xhtml_Inline515.setter
    def xhtml_Inline515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline515", None)
        self.__xhtml_Inline515 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType516"):
                    opp_val = getattr(item, "xhtml_SupType516", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType516", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType516"):
                    opp_val = getattr(item, "xhtml_SupType516", None)
                    
                    setattr(item, "xhtml_SupType516", self)
                    

    @property
    def xhtml_Inline455(self):
        return self.__xhtml_Inline455

    @xhtml_Inline455.setter
    def xhtml_Inline455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline455", None)
        self.__xhtml_Inline455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType456"):
                    opp_val = getattr(item, "xhtml_ImgType456", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType456", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType456"):
                    opp_val = getattr(item, "xhtml_ImgType456", None)
                    
                    setattr(item, "xhtml_ImgType456", self)
                    

    @property
    def xhtml_Inline482(self):
        return self.__xhtml_Inline482

    @xhtml_Inline482.setter
    def xhtml_Inline482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline482", None)
        self.__xhtml_Inline482 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType483"):
                    opp_val = getattr(item, "xhtml_StrongType483", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType483", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType483"):
                    opp_val = getattr(item, "xhtml_StrongType483", None)
                    
                    setattr(item, "xhtml_StrongType483", self)
                    

    @property
    def xhtml_Inline509(self):
        return self.__xhtml_Inline509

    @xhtml_Inline509.setter
    def xhtml_Inline509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline509", None)
        self.__xhtml_Inline509 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType510"):
                    opp_val = getattr(item, "xhtml_AcronymType510", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType510", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType510"):
                    opp_val = getattr(item, "xhtml_AcronymType510", None)
                    
                    setattr(item, "xhtml_AcronymType510", self)
                    

    @property
    def xhtml_Inline464(self):
        return self.__xhtml_Inline464

    @xhtml_Inline464.setter
    def xhtml_Inline464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline464", None)
        self.__xhtml_Inline464 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType465"):
                    opp_val = getattr(item, "xhtml_BType465", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType465", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType465"):
                    opp_val = getattr(item, "xhtml_BType465", None)
                    
                    setattr(item, "xhtml_BType465", self)
                    

    @property
    def xhtml_Inline452(self):
        return self.__xhtml_Inline452

    @xhtml_Inline452.setter
    def xhtml_Inline452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline452", None)
        self.__xhtml_Inline452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ObjectType453"):
                    opp_val = getattr(item, "xhtml_ObjectType453", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ObjectType453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ObjectType453"):
                    opp_val = getattr(item, "xhtml_ObjectType453", None)
                    
                    setattr(item, "xhtml_ObjectType453", self)
                    

    @property
    def xhtml_Inline494(self):
        return self.__xhtml_Inline494

    @xhtml_Inline494.setter
    def xhtml_Inline494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline494", None)
        self.__xhtml_Inline494 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType495"):
                    opp_val = getattr(item, "xhtml_SampType495", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType495", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType495"):
                    opp_val = getattr(item, "xhtml_SampType495", None)
                    
                    setattr(item, "xhtml_SampType495", self)
                    

    @property
    def xhtml_Inline470(self):
        return self.__xhtml_Inline470

    @xhtml_Inline470.setter
    def xhtml_Inline470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline470", None)
        self.__xhtml_Inline470 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType471"):
                    opp_val = getattr(item, "xhtml_SmallType471", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType471", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType471"):
                    opp_val = getattr(item, "xhtml_SmallType471", None)
                    
                    setattr(item, "xhtml_SmallType471", self)
                    

    @property
    def xhtml_Inline506(self):
        return self.__xhtml_Inline506

    @xhtml_Inline506.setter
    def xhtml_Inline506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline506", None)
        self.__xhtml_Inline506 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType507"):
                    opp_val = getattr(item, "xhtml_AbbrType507", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType507", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType507"):
                    opp_val = getattr(item, "xhtml_AbbrType507", None)
                    
                    setattr(item, "xhtml_AbbrType507", self)
                    

    @property
    def xhtml_Inline446(self):
        return self.__xhtml_Inline446

    @xhtml_Inline446.setter
    def xhtml_Inline446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline446", None)
        self.__xhtml_Inline446 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType447"):
                    opp_val = getattr(item, "xhtml_BrType447", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType447"):
                    opp_val = getattr(item, "xhtml_BrType447", None)
                    
                    setattr(item, "xhtml_BrType447", self)
                    

    @property
    def xhtml_Inline479(self):
        return self.__xhtml_Inline479

    @xhtml_Inline479.setter
    def xhtml_Inline479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline479", None)
        self.__xhtml_Inline479 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType480"):
                    opp_val = getattr(item, "xhtml_EmType480", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType480", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType480"):
                    opp_val = getattr(item, "xhtml_EmType480", None)
                    
                    setattr(item, "xhtml_EmType480", self)
                    

    @property
    def xhtml_Inline461(self):
        return self.__xhtml_Inline461

    @xhtml_Inline461.setter
    def xhtml_Inline461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline461", None)
        self.__xhtml_Inline461 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType462"):
                    opp_val = getattr(item, "xhtml_IType462", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType462", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType462"):
                    opp_val = getattr(item, "xhtml_IType462", None)
                    
                    setattr(item, "xhtml_IType462", self)
                    

    @property
    def xhtml_Inline488(self):
        return self.__xhtml_Inline488

    @xhtml_Inline488.setter
    def xhtml_Inline488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline488", None)
        self.__xhtml_Inline488 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType489"):
                    opp_val = getattr(item, "xhtml_CodeType489", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType489"):
                    opp_val = getattr(item, "xhtml_CodeType489", None)
                    
                    setattr(item, "xhtml_CodeType489", self)
                    

    @property
    def xhtml_Inline491(self):
        return self.__xhtml_Inline491

    @xhtml_Inline491.setter
    def xhtml_Inline491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline491", None)
        self.__xhtml_Inline491 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType492"):
                    opp_val = getattr(item, "xhtml_QType492", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType492", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType492"):
                    opp_val = getattr(item, "xhtml_QType492", None)
                    
                    setattr(item, "xhtml_QType492", self)
                    

    @property
    def xhtml_Inline485(self):
        return self.__xhtml_Inline485

    @xhtml_Inline485.setter
    def xhtml_Inline485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline485", None)
        self.__xhtml_Inline485 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType486"):
                    opp_val = getattr(item, "xhtml_DfnType486", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType486", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType486"):
                    opp_val = getattr(item, "xhtml_DfnType486", None)
                    
                    setattr(item, "xhtml_DfnType486", self)
                    

    @property
    def xhtml_Inline497(self):
        return self.__xhtml_Inline497

    @xhtml_Inline497.setter
    def xhtml_Inline497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline497", None)
        self.__xhtml_Inline497 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType498"):
                    opp_val = getattr(item, "xhtml_KbdType498", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType498", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType498"):
                    opp_val = getattr(item, "xhtml_KbdType498", None)
                    
                    setattr(item, "xhtml_KbdType498", self)
                    

    @property
    def xhtml_Inline521(self):
        return self.__xhtml_Inline521

    @xhtml_Inline521.setter
    def xhtml_Inline521(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline521", None)
        self.__xhtml_Inline521 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType522"):
                    opp_val = getattr(item, "xhtml_DelType522", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType522", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType522"):
                    opp_val = getattr(item, "xhtml_DelType522", None)
                    
                    setattr(item, "xhtml_DelType522", self)
                    

    @property
    def xhtml_Inline449(self):
        return self.__xhtml_Inline449

    @xhtml_Inline449.setter
    def xhtml_Inline449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline449", None)
        self.__xhtml_Inline449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType450"):
                    opp_val = getattr(item, "xhtml_SpanType450", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType450", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType450"):
                    opp_val = getattr(item, "xhtml_SpanType450", None)
                    
                    setattr(item, "xhtml_SpanType450", self)
                    

    @property
    def xhtml_Inline518(self):
        return self.__xhtml_Inline518

    @xhtml_Inline518.setter
    def xhtml_Inline518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline518", None)
        self.__xhtml_Inline518 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType519"):
                    opp_val = getattr(item, "xhtml_InsType519", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType519", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType519"):
                    opp_val = getattr(item, "xhtml_InsType519", None)
                    
                    setattr(item, "xhtml_InsType519", self)
                    

class xhtml_FormContent:

    def __init__(self, group: str, xhtml_FormContent: set["xhtml_PType"] = None, xhtml_FormContent390: set["xhtml_H1Type"] = None, xhtml_FormContent393: set["xhtml_H2Type"] = None, xhtml_FormContent396: set["xhtml_H3Type"] = None, xhtml_FormContent399: set["xhtml_H4Type"] = None, xhtml_FormContent402: set["xhtml_H5Type"] = None, xhtml_FormContent405: set["xhtml_H6Type"] = None, xhtml_FormContent408: set["xhtml_DivType"] = None, xhtml_FormContent411: set["xhtml_UlType"] = None, xhtml_FormContent414: set["xhtml_OlType"] = None, xhtml_FormContent417: set["xhtml_DlType"] = None, xhtml_FormContent420: set["xhtml_PreType"] = None, xhtml_FormContent423: set["xhtml_HrType"] = None, xhtml_FormContent426: set["xhtml_BlockquoteType"] = None, xhtml_FormContent429: set["xhtml_AddressType"] = None, xhtml_FormContent432: set["xhtml_TableType"] = None, xhtml_FormContent435: set["xhtml_InsType"] = None, xhtml_FormContent438: set["xhtml_DelType"] = None):
        self.group = group
        self.xhtml_FormContent = xhtml_FormContent if xhtml_FormContent is not None else set()
        self.xhtml_FormContent390 = xhtml_FormContent390 if xhtml_FormContent390 is not None else set()
        self.xhtml_FormContent393 = xhtml_FormContent393 if xhtml_FormContent393 is not None else set()
        self.xhtml_FormContent396 = xhtml_FormContent396 if xhtml_FormContent396 is not None else set()
        self.xhtml_FormContent399 = xhtml_FormContent399 if xhtml_FormContent399 is not None else set()
        self.xhtml_FormContent402 = xhtml_FormContent402 if xhtml_FormContent402 is not None else set()
        self.xhtml_FormContent405 = xhtml_FormContent405 if xhtml_FormContent405 is not None else set()
        self.xhtml_FormContent408 = xhtml_FormContent408 if xhtml_FormContent408 is not None else set()
        self.xhtml_FormContent411 = xhtml_FormContent411 if xhtml_FormContent411 is not None else set()
        self.xhtml_FormContent414 = xhtml_FormContent414 if xhtml_FormContent414 is not None else set()
        self.xhtml_FormContent417 = xhtml_FormContent417 if xhtml_FormContent417 is not None else set()
        self.xhtml_FormContent420 = xhtml_FormContent420 if xhtml_FormContent420 is not None else set()
        self.xhtml_FormContent423 = xhtml_FormContent423 if xhtml_FormContent423 is not None else set()
        self.xhtml_FormContent426 = xhtml_FormContent426 if xhtml_FormContent426 is not None else set()
        self.xhtml_FormContent429 = xhtml_FormContent429 if xhtml_FormContent429 is not None else set()
        self.xhtml_FormContent432 = xhtml_FormContent432 if xhtml_FormContent432 is not None else set()
        self.xhtml_FormContent435 = xhtml_FormContent435 if xhtml_FormContent435 is not None else set()
        self.xhtml_FormContent438 = xhtml_FormContent438 if xhtml_FormContent438 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_FormContent414(self):
        return self.__xhtml_FormContent414

    @xhtml_FormContent414.setter
    def xhtml_FormContent414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent414", None)
        self.__xhtml_FormContent414 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType415"):
                    opp_val = getattr(item, "xhtml_OlType415", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType415", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType415"):
                    opp_val = getattr(item, "xhtml_OlType415", None)
                    
                    setattr(item, "xhtml_OlType415", self)
                    

    @property
    def xhtml_FormContent438(self):
        return self.__xhtml_FormContent438

    @xhtml_FormContent438.setter
    def xhtml_FormContent438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent438", None)
        self.__xhtml_FormContent438 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType439"):
                    opp_val = getattr(item, "xhtml_DelType439", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType439", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType439"):
                    opp_val = getattr(item, "xhtml_DelType439", None)
                    
                    setattr(item, "xhtml_DelType439", self)
                    

    @property
    def xhtml_FormContent396(self):
        return self.__xhtml_FormContent396

    @xhtml_FormContent396.setter
    def xhtml_FormContent396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent396", None)
        self.__xhtml_FormContent396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type397"):
                    opp_val = getattr(item, "xhtml_H3Type397", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type397", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type397"):
                    opp_val = getattr(item, "xhtml_H3Type397", None)
                    
                    setattr(item, "xhtml_H3Type397", self)
                    

    @property
    def xhtml_FormContent(self):
        return self.__xhtml_FormContent

    @xhtml_FormContent.setter
    def xhtml_FormContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent", None)
        self.__xhtml_FormContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType388"):
                    opp_val = getattr(item, "xhtml_PType388", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType388", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType388"):
                    opp_val = getattr(item, "xhtml_PType388", None)
                    
                    setattr(item, "xhtml_PType388", self)
                    

    @property
    def xhtml_FormContent432(self):
        return self.__xhtml_FormContent432

    @xhtml_FormContent432.setter
    def xhtml_FormContent432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent432", None)
        self.__xhtml_FormContent432 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType433"):
                    opp_val = getattr(item, "xhtml_TableType433", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType433", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType433"):
                    opp_val = getattr(item, "xhtml_TableType433", None)
                    
                    setattr(item, "xhtml_TableType433", self)
                    

    @property
    def xhtml_FormContent417(self):
        return self.__xhtml_FormContent417

    @xhtml_FormContent417.setter
    def xhtml_FormContent417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent417", None)
        self.__xhtml_FormContent417 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType418"):
                    opp_val = getattr(item, "xhtml_DlType418", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType418", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType418"):
                    opp_val = getattr(item, "xhtml_DlType418", None)
                    
                    setattr(item, "xhtml_DlType418", self)
                    

    @property
    def xhtml_FormContent399(self):
        return self.__xhtml_FormContent399

    @xhtml_FormContent399.setter
    def xhtml_FormContent399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent399", None)
        self.__xhtml_FormContent399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type400"):
                    opp_val = getattr(item, "xhtml_H4Type400", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type400"):
                    opp_val = getattr(item, "xhtml_H4Type400", None)
                    
                    setattr(item, "xhtml_H4Type400", self)
                    

    @property
    def xhtml_FormContent420(self):
        return self.__xhtml_FormContent420

    @xhtml_FormContent420.setter
    def xhtml_FormContent420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent420", None)
        self.__xhtml_FormContent420 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType421"):
                    opp_val = getattr(item, "xhtml_PreType421", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType421", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType421"):
                    opp_val = getattr(item, "xhtml_PreType421", None)
                    
                    setattr(item, "xhtml_PreType421", self)
                    

    @property
    def xhtml_FormContent435(self):
        return self.__xhtml_FormContent435

    @xhtml_FormContent435.setter
    def xhtml_FormContent435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent435", None)
        self.__xhtml_FormContent435 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType436"):
                    opp_val = getattr(item, "xhtml_InsType436", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType436", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType436"):
                    opp_val = getattr(item, "xhtml_InsType436", None)
                    
                    setattr(item, "xhtml_InsType436", self)
                    

    @property
    def xhtml_FormContent402(self):
        return self.__xhtml_FormContent402

    @xhtml_FormContent402.setter
    def xhtml_FormContent402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent402", None)
        self.__xhtml_FormContent402 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type403"):
                    opp_val = getattr(item, "xhtml_H5Type403", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type403", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type403"):
                    opp_val = getattr(item, "xhtml_H5Type403", None)
                    
                    setattr(item, "xhtml_H5Type403", self)
                    

    @property
    def xhtml_FormContent411(self):
        return self.__xhtml_FormContent411

    @xhtml_FormContent411.setter
    def xhtml_FormContent411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent411", None)
        self.__xhtml_FormContent411 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType412"):
                    opp_val = getattr(item, "xhtml_UlType412", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType412", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType412"):
                    opp_val = getattr(item, "xhtml_UlType412", None)
                    
                    setattr(item, "xhtml_UlType412", self)
                    

    @property
    def xhtml_FormContent405(self):
        return self.__xhtml_FormContent405

    @xhtml_FormContent405.setter
    def xhtml_FormContent405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent405", None)
        self.__xhtml_FormContent405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type406"):
                    opp_val = getattr(item, "xhtml_H6Type406", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type406"):
                    opp_val = getattr(item, "xhtml_H6Type406", None)
                    
                    setattr(item, "xhtml_H6Type406", self)
                    

    @property
    def xhtml_FormContent393(self):
        return self.__xhtml_FormContent393

    @xhtml_FormContent393.setter
    def xhtml_FormContent393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent393", None)
        self.__xhtml_FormContent393 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type394"):
                    opp_val = getattr(item, "xhtml_H2Type394", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type394", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type394"):
                    opp_val = getattr(item, "xhtml_H2Type394", None)
                    
                    setattr(item, "xhtml_H2Type394", self)
                    

    @property
    def xhtml_FormContent390(self):
        return self.__xhtml_FormContent390

    @xhtml_FormContent390.setter
    def xhtml_FormContent390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent390", None)
        self.__xhtml_FormContent390 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type391"):
                    opp_val = getattr(item, "xhtml_H1Type391", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type391", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type391"):
                    opp_val = getattr(item, "xhtml_H1Type391", None)
                    
                    setattr(item, "xhtml_H1Type391", self)
                    

    @property
    def xhtml_FormContent423(self):
        return self.__xhtml_FormContent423

    @xhtml_FormContent423.setter
    def xhtml_FormContent423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent423", None)
        self.__xhtml_FormContent423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType424"):
                    opp_val = getattr(item, "xhtml_HrType424", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType424"):
                    opp_val = getattr(item, "xhtml_HrType424", None)
                    
                    setattr(item, "xhtml_HrType424", self)
                    

    @property
    def xhtml_FormContent408(self):
        return self.__xhtml_FormContent408

    @xhtml_FormContent408.setter
    def xhtml_FormContent408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent408", None)
        self.__xhtml_FormContent408 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType409"):
                    opp_val = getattr(item, "xhtml_DivType409", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType409", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType409"):
                    opp_val = getattr(item, "xhtml_DivType409", None)
                    
                    setattr(item, "xhtml_DivType409", self)
                    

    @property
    def xhtml_FormContent426(self):
        return self.__xhtml_FormContent426

    @xhtml_FormContent426.setter
    def xhtml_FormContent426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent426", None)
        self.__xhtml_FormContent426 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType427"):
                    opp_val = getattr(item, "xhtml_BlockquoteType427", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType427"):
                    opp_val = getattr(item, "xhtml_BlockquoteType427", None)
                    
                    setattr(item, "xhtml_BlockquoteType427", self)
                    

    @property
    def xhtml_FormContent429(self):
        return self.__xhtml_FormContent429

    @xhtml_FormContent429.setter
    def xhtml_FormContent429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_FormContent__xhtml_FormContent429", None)
        self.__xhtml_FormContent429 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType430"):
                    opp_val = getattr(item, "xhtml_AddressType430", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType430", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType430"):
                    opp_val = getattr(item, "xhtml_AddressType430", None)
                    
                    setattr(item, "xhtml_AddressType430", self)
                    

class xhtml_Flow:

    def __init__(self, mixed: str, group: str, xhtml_Flow: set["xhtml_PType"] = None, xhtml_Flow262: set["xhtml_H1Type"] = None, xhtml_Flow265: set["xhtml_H2Type"] = None, xhtml_Flow268: set["xhtml_H3Type"] = None, xhtml_Flow271: set["xhtml_H4Type"] = None, xhtml_Flow274: set["xhtml_H5Type"] = None, xhtml_Flow277: set["xhtml_H6Type"] = None, xhtml_Flow280: set["xhtml_DivType"] = None, xhtml_Flow283: set["xhtml_UlType"] = None, xhtml_Flow286: set["xhtml_OlType"] = None, xhtml_Flow289: set["xhtml_DlType"] = None, xhtml_Flow292: set["xhtml_PreType"] = None, xhtml_Flow301: set["xhtml_AddressType"] = None, xhtml_Flow304: set["xhtml_TableType"] = None, xhtml_Flow307: set["xhtml_AType"] = None, xhtml_Flow310: set["xhtml_BrType"] = None, xhtml_Flow313: set["xhtml_SpanType"] = None, xhtml_Flow316: set["xhtml_ObjectType"] = None, xhtml_Flow295: set["xhtml_HrType"] = None, xhtml_Flow298: set["xhtml_BlockquoteType"] = None, xhtml_Flow328: set["xhtml_BType"] = None, xhtml_Flow331: set["xhtml_BigType"] = None, xhtml_Flow334: set["xhtml_SmallType"] = None, xhtml_Flow337: set["xhtml_UType"] = None, xhtml_Flow340: set["xhtml_StrikeType"] = None, xhtml_Flow343: set["xhtml_EmType"] = None, xhtml_Flow319: set["xhtml_ImgType"] = None, xhtml_Flow322: set["xhtml_TtType"] = None, xhtml_Flow325: set["xhtml_IType"] = None, xhtml_Flow349: set["xhtml_DfnType"] = None, xhtml_Flow352: set["xhtml_CodeType"] = None, xhtml_Flow355: set["xhtml_QType"] = None, xhtml_Flow358: set["xhtml_SampType"] = None, xhtml_Flow361: set["xhtml_KbdType"] = None, xhtml_Flow364: set["xhtml_VarType"] = None, xhtml_Flow346: set["xhtml_StrongType"] = None, xhtml_Flow370: set["xhtml_AbbrType"] = None, xhtml_Flow373: set["xhtml_AcronymType"] = None, xhtml_Flow376: set["xhtml_SubType"] = None, xhtml_Flow379: set["xhtml_SupType"] = None, xhtml_Flow382: set["xhtml_InsType"] = None, xhtml_Flow385: set["xhtml_DelType"] = None, xhtml_Flow367: set["xhtml_CiteType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_Flow = xhtml_Flow if xhtml_Flow is not None else set()
        self.xhtml_Flow262 = xhtml_Flow262 if xhtml_Flow262 is not None else set()
        self.xhtml_Flow265 = xhtml_Flow265 if xhtml_Flow265 is not None else set()
        self.xhtml_Flow268 = xhtml_Flow268 if xhtml_Flow268 is not None else set()
        self.xhtml_Flow271 = xhtml_Flow271 if xhtml_Flow271 is not None else set()
        self.xhtml_Flow274 = xhtml_Flow274 if xhtml_Flow274 is not None else set()
        self.xhtml_Flow277 = xhtml_Flow277 if xhtml_Flow277 is not None else set()
        self.xhtml_Flow280 = xhtml_Flow280 if xhtml_Flow280 is not None else set()
        self.xhtml_Flow283 = xhtml_Flow283 if xhtml_Flow283 is not None else set()
        self.xhtml_Flow286 = xhtml_Flow286 if xhtml_Flow286 is not None else set()
        self.xhtml_Flow289 = xhtml_Flow289 if xhtml_Flow289 is not None else set()
        self.xhtml_Flow292 = xhtml_Flow292 if xhtml_Flow292 is not None else set()
        self.xhtml_Flow301 = xhtml_Flow301 if xhtml_Flow301 is not None else set()
        self.xhtml_Flow304 = xhtml_Flow304 if xhtml_Flow304 is not None else set()
        self.xhtml_Flow307 = xhtml_Flow307 if xhtml_Flow307 is not None else set()
        self.xhtml_Flow310 = xhtml_Flow310 if xhtml_Flow310 is not None else set()
        self.xhtml_Flow313 = xhtml_Flow313 if xhtml_Flow313 is not None else set()
        self.xhtml_Flow316 = xhtml_Flow316 if xhtml_Flow316 is not None else set()
        self.xhtml_Flow295 = xhtml_Flow295 if xhtml_Flow295 is not None else set()
        self.xhtml_Flow298 = xhtml_Flow298 if xhtml_Flow298 is not None else set()
        self.xhtml_Flow328 = xhtml_Flow328 if xhtml_Flow328 is not None else set()
        self.xhtml_Flow331 = xhtml_Flow331 if xhtml_Flow331 is not None else set()
        self.xhtml_Flow334 = xhtml_Flow334 if xhtml_Flow334 is not None else set()
        self.xhtml_Flow337 = xhtml_Flow337 if xhtml_Flow337 is not None else set()
        self.xhtml_Flow340 = xhtml_Flow340 if xhtml_Flow340 is not None else set()
        self.xhtml_Flow343 = xhtml_Flow343 if xhtml_Flow343 is not None else set()
        self.xhtml_Flow319 = xhtml_Flow319 if xhtml_Flow319 is not None else set()
        self.xhtml_Flow322 = xhtml_Flow322 if xhtml_Flow322 is not None else set()
        self.xhtml_Flow325 = xhtml_Flow325 if xhtml_Flow325 is not None else set()
        self.xhtml_Flow349 = xhtml_Flow349 if xhtml_Flow349 is not None else set()
        self.xhtml_Flow352 = xhtml_Flow352 if xhtml_Flow352 is not None else set()
        self.xhtml_Flow355 = xhtml_Flow355 if xhtml_Flow355 is not None else set()
        self.xhtml_Flow358 = xhtml_Flow358 if xhtml_Flow358 is not None else set()
        self.xhtml_Flow361 = xhtml_Flow361 if xhtml_Flow361 is not None else set()
        self.xhtml_Flow364 = xhtml_Flow364 if xhtml_Flow364 is not None else set()
        self.xhtml_Flow346 = xhtml_Flow346 if xhtml_Flow346 is not None else set()
        self.xhtml_Flow370 = xhtml_Flow370 if xhtml_Flow370 is not None else set()
        self.xhtml_Flow373 = xhtml_Flow373 if xhtml_Flow373 is not None else set()
        self.xhtml_Flow376 = xhtml_Flow376 if xhtml_Flow376 is not None else set()
        self.xhtml_Flow379 = xhtml_Flow379 if xhtml_Flow379 is not None else set()
        self.xhtml_Flow382 = xhtml_Flow382 if xhtml_Flow382 is not None else set()
        self.xhtml_Flow385 = xhtml_Flow385 if xhtml_Flow385 is not None else set()
        self.xhtml_Flow367 = xhtml_Flow367 if xhtml_Flow367 is not None else set()
        
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
    def xhtml_Flow310(self):
        return self.__xhtml_Flow310

    @xhtml_Flow310.setter
    def xhtml_Flow310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow310", None)
        self.__xhtml_Flow310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType311"):
                    opp_val = getattr(item, "xhtml_BrType311", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType311"):
                    opp_val = getattr(item, "xhtml_BrType311", None)
                    
                    setattr(item, "xhtml_BrType311", self)
                    

    @property
    def xhtml_Flow331(self):
        return self.__xhtml_Flow331

    @xhtml_Flow331.setter
    def xhtml_Flow331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow331", None)
        self.__xhtml_Flow331 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType332"):
                    opp_val = getattr(item, "xhtml_BigType332", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType332", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType332"):
                    opp_val = getattr(item, "xhtml_BigType332", None)
                    
                    setattr(item, "xhtml_BigType332", self)
                    

    @property
    def xhtml_Flow334(self):
        return self.__xhtml_Flow334

    @xhtml_Flow334.setter
    def xhtml_Flow334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow334", None)
        self.__xhtml_Flow334 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType335"):
                    opp_val = getattr(item, "xhtml_SmallType335", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType335"):
                    opp_val = getattr(item, "xhtml_SmallType335", None)
                    
                    setattr(item, "xhtml_SmallType335", self)
                    

    @property
    def xhtml_Flow262(self):
        return self.__xhtml_Flow262

    @xhtml_Flow262.setter
    def xhtml_Flow262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow262", None)
        self.__xhtml_Flow262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type263"):
                    opp_val = getattr(item, "xhtml_H1Type263", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type263"):
                    opp_val = getattr(item, "xhtml_H1Type263", None)
                    
                    setattr(item, "xhtml_H1Type263", self)
                    

    @property
    def xhtml_Flow268(self):
        return self.__xhtml_Flow268

    @xhtml_Flow268.setter
    def xhtml_Flow268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow268", None)
        self.__xhtml_Flow268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type269"):
                    opp_val = getattr(item, "xhtml_H3Type269", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type269"):
                    opp_val = getattr(item, "xhtml_H3Type269", None)
                    
                    setattr(item, "xhtml_H3Type269", self)
                    

    @property
    def xhtml_Flow274(self):
        return self.__xhtml_Flow274

    @xhtml_Flow274.setter
    def xhtml_Flow274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow274", None)
        self.__xhtml_Flow274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type275"):
                    opp_val = getattr(item, "xhtml_H5Type275", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type275"):
                    opp_val = getattr(item, "xhtml_H5Type275", None)
                    
                    setattr(item, "xhtml_H5Type275", self)
                    

    @property
    def xhtml_Flow349(self):
        return self.__xhtml_Flow349

    @xhtml_Flow349.setter
    def xhtml_Flow349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow349", None)
        self.__xhtml_Flow349 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType350"):
                    opp_val = getattr(item, "xhtml_DfnType350", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType350", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType350"):
                    opp_val = getattr(item, "xhtml_DfnType350", None)
                    
                    setattr(item, "xhtml_DfnType350", self)
                    

    @property
    def xhtml_Flow343(self):
        return self.__xhtml_Flow343

    @xhtml_Flow343.setter
    def xhtml_Flow343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow343", None)
        self.__xhtml_Flow343 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType344"):
                    opp_val = getattr(item, "xhtml_EmType344", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType344"):
                    opp_val = getattr(item, "xhtml_EmType344", None)
                    
                    setattr(item, "xhtml_EmType344", self)
                    

    @property
    def xhtml_Flow352(self):
        return self.__xhtml_Flow352

    @xhtml_Flow352.setter
    def xhtml_Flow352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow352", None)
        self.__xhtml_Flow352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType353"):
                    opp_val = getattr(item, "xhtml_CodeType353", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType353"):
                    opp_val = getattr(item, "xhtml_CodeType353", None)
                    
                    setattr(item, "xhtml_CodeType353", self)
                    

    @property
    def xhtml_Flow337(self):
        return self.__xhtml_Flow337

    @xhtml_Flow337.setter
    def xhtml_Flow337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow337", None)
        self.__xhtml_Flow337 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UType338"):
                    opp_val = getattr(item, "xhtml_UType338", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType338", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType338"):
                    opp_val = getattr(item, "xhtml_UType338", None)
                    
                    setattr(item, "xhtml_UType338", self)
                    

    @property
    def xhtml_Flow313(self):
        return self.__xhtml_Flow313

    @xhtml_Flow313.setter
    def xhtml_Flow313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow313", None)
        self.__xhtml_Flow313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType314"):
                    opp_val = getattr(item, "xhtml_SpanType314", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType314", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType314"):
                    opp_val = getattr(item, "xhtml_SpanType314", None)
                    
                    setattr(item, "xhtml_SpanType314", self)
                    

    @property
    def xhtml_Flow340(self):
        return self.__xhtml_Flow340

    @xhtml_Flow340.setter
    def xhtml_Flow340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow340", None)
        self.__xhtml_Flow340 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrikeType341"):
                    opp_val = getattr(item, "xhtml_StrikeType341", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType341", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType341"):
                    opp_val = getattr(item, "xhtml_StrikeType341", None)
                    
                    setattr(item, "xhtml_StrikeType341", self)
                    

    @property
    def xhtml_Flow319(self):
        return self.__xhtml_Flow319

    @xhtml_Flow319.setter
    def xhtml_Flow319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow319", None)
        self.__xhtml_Flow319 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType320"):
                    opp_val = getattr(item, "xhtml_ImgType320", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType320"):
                    opp_val = getattr(item, "xhtml_ImgType320", None)
                    
                    setattr(item, "xhtml_ImgType320", self)
                    

    @property
    def xhtml_Flow295(self):
        return self.__xhtml_Flow295

    @xhtml_Flow295.setter
    def xhtml_Flow295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow295", None)
        self.__xhtml_Flow295 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType296"):
                    opp_val = getattr(item, "xhtml_HrType296", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType296"):
                    opp_val = getattr(item, "xhtml_HrType296", None)
                    
                    setattr(item, "xhtml_HrType296", self)
                    

    @property
    def xhtml_Flow373(self):
        return self.__xhtml_Flow373

    @xhtml_Flow373.setter
    def xhtml_Flow373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow373", None)
        self.__xhtml_Flow373 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType374"):
                    opp_val = getattr(item, "xhtml_AcronymType374", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType374", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType374"):
                    opp_val = getattr(item, "xhtml_AcronymType374", None)
                    
                    setattr(item, "xhtml_AcronymType374", self)
                    

    @property
    def xhtml_Flow367(self):
        return self.__xhtml_Flow367

    @xhtml_Flow367.setter
    def xhtml_Flow367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow367", None)
        self.__xhtml_Flow367 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType368"):
                    opp_val = getattr(item, "xhtml_CiteType368", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType368", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType368"):
                    opp_val = getattr(item, "xhtml_CiteType368", None)
                    
                    setattr(item, "xhtml_CiteType368", self)
                    

    @property
    def xhtml_Flow328(self):
        return self.__xhtml_Flow328

    @xhtml_Flow328.setter
    def xhtml_Flow328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow328", None)
        self.__xhtml_Flow328 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType329"):
                    opp_val = getattr(item, "xhtml_BType329", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType329", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType329"):
                    opp_val = getattr(item, "xhtml_BType329", None)
                    
                    setattr(item, "xhtml_BType329", self)
                    

    @property
    def xhtml_Flow379(self):
        return self.__xhtml_Flow379

    @xhtml_Flow379.setter
    def xhtml_Flow379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow379", None)
        self.__xhtml_Flow379 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType380"):
                    opp_val = getattr(item, "xhtml_SupType380", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType380", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType380"):
                    opp_val = getattr(item, "xhtml_SupType380", None)
                    
                    setattr(item, "xhtml_SupType380", self)
                    

    @property
    def xhtml_Flow364(self):
        return self.__xhtml_Flow364

    @xhtml_Flow364.setter
    def xhtml_Flow364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow364", None)
        self.__xhtml_Flow364 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType365"):
                    opp_val = getattr(item, "xhtml_VarType365", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType365", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType365"):
                    opp_val = getattr(item, "xhtml_VarType365", None)
                    
                    setattr(item, "xhtml_VarType365", self)
                    

    @property
    def xhtml_Flow271(self):
        return self.__xhtml_Flow271

    @xhtml_Flow271.setter
    def xhtml_Flow271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow271", None)
        self.__xhtml_Flow271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type272"):
                    opp_val = getattr(item, "xhtml_H4Type272", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type272"):
                    opp_val = getattr(item, "xhtml_H4Type272", None)
                    
                    setattr(item, "xhtml_H4Type272", self)
                    

    @property
    def xhtml_Flow298(self):
        return self.__xhtml_Flow298

    @xhtml_Flow298.setter
    def xhtml_Flow298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow298", None)
        self.__xhtml_Flow298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType299"):
                    opp_val = getattr(item, "xhtml_BlockquoteType299", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType299"):
                    opp_val = getattr(item, "xhtml_BlockquoteType299", None)
                    
                    setattr(item, "xhtml_BlockquoteType299", self)
                    

    @property
    def xhtml_Flow277(self):
        return self.__xhtml_Flow277

    @xhtml_Flow277.setter
    def xhtml_Flow277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow277", None)
        self.__xhtml_Flow277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type278"):
                    opp_val = getattr(item, "xhtml_H6Type278", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type278"):
                    opp_val = getattr(item, "xhtml_H6Type278", None)
                    
                    setattr(item, "xhtml_H6Type278", self)
                    

    @property
    def xhtml_Flow283(self):
        return self.__xhtml_Flow283

    @xhtml_Flow283.setter
    def xhtml_Flow283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow283", None)
        self.__xhtml_Flow283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType284"):
                    opp_val = getattr(item, "xhtml_UlType284", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType284"):
                    opp_val = getattr(item, "xhtml_UlType284", None)
                    
                    setattr(item, "xhtml_UlType284", self)
                    

    @property
    def xhtml_Flow325(self):
        return self.__xhtml_Flow325

    @xhtml_Flow325.setter
    def xhtml_Flow325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow325", None)
        self.__xhtml_Flow325 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType326"):
                    opp_val = getattr(item, "xhtml_IType326", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType326", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType326"):
                    opp_val = getattr(item, "xhtml_IType326", None)
                    
                    setattr(item, "xhtml_IType326", self)
                    

    @property
    def xhtml_Flow361(self):
        return self.__xhtml_Flow361

    @xhtml_Flow361.setter
    def xhtml_Flow361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow361", None)
        self.__xhtml_Flow361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType362"):
                    opp_val = getattr(item, "xhtml_KbdType362", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType362"):
                    opp_val = getattr(item, "xhtml_KbdType362", None)
                    
                    setattr(item, "xhtml_KbdType362", self)
                    

    @property
    def xhtml_Flow307(self):
        return self.__xhtml_Flow307

    @xhtml_Flow307.setter
    def xhtml_Flow307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow307", None)
        self.__xhtml_Flow307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType308"):
                    opp_val = getattr(item, "xhtml_AType308", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType308"):
                    opp_val = getattr(item, "xhtml_AType308", None)
                    
                    setattr(item, "xhtml_AType308", self)
                    

    @property
    def xhtml_Flow322(self):
        return self.__xhtml_Flow322

    @xhtml_Flow322.setter
    def xhtml_Flow322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow322", None)
        self.__xhtml_Flow322 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType323"):
                    opp_val = getattr(item, "xhtml_TtType323", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType323"):
                    opp_val = getattr(item, "xhtml_TtType323", None)
                    
                    setattr(item, "xhtml_TtType323", self)
                    

    @property
    def xhtml_Flow286(self):
        return self.__xhtml_Flow286

    @xhtml_Flow286.setter
    def xhtml_Flow286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow286", None)
        self.__xhtml_Flow286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType287"):
                    opp_val = getattr(item, "xhtml_OlType287", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType287"):
                    opp_val = getattr(item, "xhtml_OlType287", None)
                    
                    setattr(item, "xhtml_OlType287", self)
                    

    @property
    def xhtml_Flow292(self):
        return self.__xhtml_Flow292

    @xhtml_Flow292.setter
    def xhtml_Flow292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow292", None)
        self.__xhtml_Flow292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType293"):
                    opp_val = getattr(item, "xhtml_PreType293", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType293"):
                    opp_val = getattr(item, "xhtml_PreType293", None)
                    
                    setattr(item, "xhtml_PreType293", self)
                    

    @property
    def xhtml_Flow376(self):
        return self.__xhtml_Flow376

    @xhtml_Flow376.setter
    def xhtml_Flow376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow376", None)
        self.__xhtml_Flow376 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType377"):
                    opp_val = getattr(item, "xhtml_SubType377", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType377", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType377"):
                    opp_val = getattr(item, "xhtml_SubType377", None)
                    
                    setattr(item, "xhtml_SubType377", self)
                    

    @property
    def xhtml_Flow280(self):
        return self.__xhtml_Flow280

    @xhtml_Flow280.setter
    def xhtml_Flow280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow280", None)
        self.__xhtml_Flow280 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType281"):
                    opp_val = getattr(item, "xhtml_DivType281", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType281"):
                    opp_val = getattr(item, "xhtml_DivType281", None)
                    
                    setattr(item, "xhtml_DivType281", self)
                    

    @property
    def xhtml_Flow382(self):
        return self.__xhtml_Flow382

    @xhtml_Flow382.setter
    def xhtml_Flow382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow382", None)
        self.__xhtml_Flow382 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType383"):
                    opp_val = getattr(item, "xhtml_InsType383", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType383", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType383"):
                    opp_val = getattr(item, "xhtml_InsType383", None)
                    
                    setattr(item, "xhtml_InsType383", self)
                    

    @property
    def xhtml_Flow358(self):
        return self.__xhtml_Flow358

    @xhtml_Flow358.setter
    def xhtml_Flow358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow358", None)
        self.__xhtml_Flow358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType359"):
                    opp_val = getattr(item, "xhtml_SampType359", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType359", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType359"):
                    opp_val = getattr(item, "xhtml_SampType359", None)
                    
                    setattr(item, "xhtml_SampType359", self)
                    

    @property
    def xhtml_Flow370(self):
        return self.__xhtml_Flow370

    @xhtml_Flow370.setter
    def xhtml_Flow370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow370", None)
        self.__xhtml_Flow370 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType371"):
                    opp_val = getattr(item, "xhtml_AbbrType371", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType371", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType371"):
                    opp_val = getattr(item, "xhtml_AbbrType371", None)
                    
                    setattr(item, "xhtml_AbbrType371", self)
                    

    @property
    def xhtml_Flow289(self):
        return self.__xhtml_Flow289

    @xhtml_Flow289.setter
    def xhtml_Flow289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow289", None)
        self.__xhtml_Flow289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType290"):
                    opp_val = getattr(item, "xhtml_DlType290", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType290"):
                    opp_val = getattr(item, "xhtml_DlType290", None)
                    
                    setattr(item, "xhtml_DlType290", self)
                    

    @property
    def xhtml_Flow346(self):
        return self.__xhtml_Flow346

    @xhtml_Flow346.setter
    def xhtml_Flow346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow346", None)
        self.__xhtml_Flow346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType347"):
                    opp_val = getattr(item, "xhtml_StrongType347", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType347"):
                    opp_val = getattr(item, "xhtml_StrongType347", None)
                    
                    setattr(item, "xhtml_StrongType347", self)
                    

    @property
    def xhtml_Flow316(self):
        return self.__xhtml_Flow316

    @xhtml_Flow316.setter
    def xhtml_Flow316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow316", None)
        self.__xhtml_Flow316 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ObjectType317"):
                    opp_val = getattr(item, "xhtml_ObjectType317", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ObjectType317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ObjectType317"):
                    opp_val = getattr(item, "xhtml_ObjectType317", None)
                    
                    setattr(item, "xhtml_ObjectType317", self)
                    

    @property
    def xhtml_Flow355(self):
        return self.__xhtml_Flow355

    @xhtml_Flow355.setter
    def xhtml_Flow355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow355", None)
        self.__xhtml_Flow355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType356"):
                    opp_val = getattr(item, "xhtml_QType356", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType356"):
                    opp_val = getattr(item, "xhtml_QType356", None)
                    
                    setattr(item, "xhtml_QType356", self)
                    

    @property
    def xhtml_Flow385(self):
        return self.__xhtml_Flow385

    @xhtml_Flow385.setter
    def xhtml_Flow385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow385", None)
        self.__xhtml_Flow385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType386"):
                    opp_val = getattr(item, "xhtml_DelType386", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType386"):
                    opp_val = getattr(item, "xhtml_DelType386", None)
                    
                    setattr(item, "xhtml_DelType386", self)
                    

    @property
    def xhtml_Flow265(self):
        return self.__xhtml_Flow265

    @xhtml_Flow265.setter
    def xhtml_Flow265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow265", None)
        self.__xhtml_Flow265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type266"):
                    opp_val = getattr(item, "xhtml_H2Type266", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type266"):
                    opp_val = getattr(item, "xhtml_H2Type266", None)
                    
                    setattr(item, "xhtml_H2Type266", self)
                    

    @property
    def xhtml_Flow304(self):
        return self.__xhtml_Flow304

    @xhtml_Flow304.setter
    def xhtml_Flow304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow304", None)
        self.__xhtml_Flow304 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType305"):
                    opp_val = getattr(item, "xhtml_TableType305", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType305"):
                    opp_val = getattr(item, "xhtml_TableType305", None)
                    
                    setattr(item, "xhtml_TableType305", self)
                    

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
                if hasattr(item, "xhtml_PType260"):
                    opp_val = getattr(item, "xhtml_PType260", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType260"):
                    opp_val = getattr(item, "xhtml_PType260", None)
                    
                    setattr(item, "xhtml_PType260", self)
                    

    @property
    def xhtml_Flow301(self):
        return self.__xhtml_Flow301

    @xhtml_Flow301.setter
    def xhtml_Flow301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow301", None)
        self.__xhtml_Flow301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType302"):
                    opp_val = getattr(item, "xhtml_AddressType302", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType302"):
                    opp_val = getattr(item, "xhtml_AddressType302", None)
                    
                    setattr(item, "xhtml_AddressType302", self)
                    

class xhtml_TheadType:

    def __init__(self, charoff: str, align: str, char: str, class: str, id: str, style: str, title: str, valign: str, xhtml_TheadType: "xhtml_DocumentRoot" = None, xhtml_TheadType743: "xhtml_TableType" = None, xhtml_TheadType760: set["xhtml_TrType"] = None):
        self.charoff = charoff
        self.align = align
        self.char = char
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TheadType = xhtml_TheadType
        self.xhtml_TheadType743 = xhtml_TheadType743
        self.xhtml_TheadType760 = xhtml_TheadType760 if xhtml_TheadType760 is not None else set()
        
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
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

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
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def xhtml_TheadType760(self):
        return self.__xhtml_TheadType760

    @xhtml_TheadType760.setter
    def xhtml_TheadType760(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TheadType__xhtml_TheadType760", None)
        self.__xhtml_TheadType760 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType761"):
                    opp_val = getattr(item, "xhtml_TrType761", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType761", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType761"):
                    opp_val = getattr(item, "xhtml_TrType761", None)
                    
                    setattr(item, "xhtml_TrType761", self)
                    

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
            if hasattr(old_value, "xhtml_DocumentRoot244"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot244"):
                opp_val = getattr(value, "xhtml_DocumentRoot244", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TheadType743(self):
        return self.__xhtml_TheadType743

    @xhtml_TheadType743.setter
    def xhtml_TheadType743(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TheadType__xhtml_TheadType743", None)
        self.__xhtml_TheadType743 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType742"):
                opp_val = getattr(old_value, "xhtml_TableType742", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType742", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType742"):
                opp_val = getattr(value, "xhtml_TableType742", None)
                setattr(value, "xhtml_TableType742", self)

class xhtml_TrType:

    def __init__(self, group: str, align: str, char: str, charoff: str, class: str, id: str, style: str, title: str, valign: str, xhtml_TrType: "xhtml_DocumentRoot" = None, xhtml_TrType755: "xhtml_TbodyType" = None, xhtml_TrType752: "xhtml_TableType" = None, xhtml_TrType758: "xhtml_TfootType" = None, xhtml_TrType761: "xhtml_TheadType" = None, xhtml_TrType763: set["xhtml_ThType"] = None, xhtml_TrType766: set["xhtml_TdType"] = None):
        self.group = group
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TrType = xhtml_TrType
        self.xhtml_TrType755 = xhtml_TrType755
        self.xhtml_TrType752 = xhtml_TrType752
        self.xhtml_TrType758 = xhtml_TrType758
        self.xhtml_TrType761 = xhtml_TrType761
        self.xhtml_TrType763 = xhtml_TrType763 if xhtml_TrType763 is not None else set()
        self.xhtml_TrType766 = xhtml_TrType766 if xhtml_TrType766 is not None else set()
        
    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

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
    def xhtml_TrType763(self):
        return self.__xhtml_TrType763

    @xhtml_TrType763.setter
    def xhtml_TrType763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType763", None)
        self.__xhtml_TrType763 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ThType764"):
                    opp_val = getattr(item, "xhtml_ThType764", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ThType764", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ThType764"):
                    opp_val = getattr(item, "xhtml_ThType764", None)
                    
                    setattr(item, "xhtml_ThType764", self)
                    

    @property
    def xhtml_TrType758(self):
        return self.__xhtml_TrType758

    @xhtml_TrType758.setter
    def xhtml_TrType758(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType758", None)
        self.__xhtml_TrType758 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TfootType757"):
                opp_val = getattr(old_value, "xhtml_TfootType757", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TfootType757"):
                opp_val = getattr(value, "xhtml_TfootType757", None)
                if opp_val is None:
                    setattr(value, "xhtml_TfootType757", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType755(self):
        return self.__xhtml_TrType755

    @xhtml_TrType755.setter
    def xhtml_TrType755(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType755", None)
        self.__xhtml_TrType755 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TbodyType754"):
                opp_val = getattr(old_value, "xhtml_TbodyType754", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TbodyType754"):
                opp_val = getattr(value, "xhtml_TbodyType754", None)
                if opp_val is None:
                    setattr(value, "xhtml_TbodyType754", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType766(self):
        return self.__xhtml_TrType766

    @xhtml_TrType766.setter
    def xhtml_TrType766(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType766", None)
        self.__xhtml_TrType766 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TdType767"):
                    opp_val = getattr(item, "xhtml_TdType767", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TdType767", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TdType767"):
                    opp_val = getattr(item, "xhtml_TdType767", None)
                    
                    setattr(item, "xhtml_TdType767", self)
                    

    @property
    def xhtml_TrType761(self):
        return self.__xhtml_TrType761

    @xhtml_TrType761.setter
    def xhtml_TrType761(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType761", None)
        self.__xhtml_TrType761 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TheadType760"):
                opp_val = getattr(old_value, "xhtml_TheadType760", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TheadType760"):
                opp_val = getattr(value, "xhtml_TheadType760", None)
                if opp_val is None:
                    setattr(value, "xhtml_TheadType760", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "xhtml_DocumentRoot246"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot246"):
                opp_val = getattr(value, "xhtml_DocumentRoot246", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TrType752(self):
        return self.__xhtml_TrType752

    @xhtml_TrType752.setter
    def xhtml_TrType752(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TrType__xhtml_TrType752", None)
        self.__xhtml_TrType752 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType751"):
                opp_val = getattr(old_value, "xhtml_TableType751", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType751"):
                opp_val = getattr(value, "xhtml_TableType751", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType751", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TfootType:

    def __init__(self, align: str, char: str, charoff: str, class: str, id: str, style: str, title: str, valign: str, xhtml_TfootType: "xhtml_DocumentRoot" = None, xhtml_TfootType746: "xhtml_TableType" = None, xhtml_TfootType757: set["xhtml_TrType"] = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TfootType = xhtml_TfootType
        self.xhtml_TfootType746 = xhtml_TfootType746
        self.xhtml_TfootType757 = xhtml_TfootType757 if xhtml_TfootType757 is not None else set()
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

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
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def xhtml_TfootType757(self):
        return self.__xhtml_TfootType757

    @xhtml_TfootType757.setter
    def xhtml_TfootType757(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TfootType__xhtml_TfootType757", None)
        self.__xhtml_TfootType757 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType758"):
                    opp_val = getattr(item, "xhtml_TrType758", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType758", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType758"):
                    opp_val = getattr(item, "xhtml_TrType758", None)
                    
                    setattr(item, "xhtml_TrType758", self)
                    

    @property
    def xhtml_TfootType746(self):
        return self.__xhtml_TfootType746

    @xhtml_TfootType746.setter
    def xhtml_TfootType746(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TfootType__xhtml_TfootType746", None)
        self.__xhtml_TfootType746 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType745"):
                opp_val = getattr(old_value, "xhtml_TableType745", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType745", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType745"):
                opp_val = getattr(value, "xhtml_TableType745", None)
                setattr(value, "xhtml_TableType745", self)

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
            if hasattr(old_value, "xhtml_DocumentRoot240"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot240"):
                opp_val = getattr(value, "xhtml_DocumentRoot240", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TbodyType:

    def __init__(self, align: str, char: str, charoff: str, class: str, id: str, style: str, title: str, valign: str, xhtml_TbodyType: "xhtml_DocumentRoot" = None, xhtml_TbodyType754: set["xhtml_TrType"] = None, xhtml_TbodyType749: "xhtml_TableType" = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TbodyType = xhtml_TbodyType
        self.xhtml_TbodyType754 = xhtml_TbodyType754 if xhtml_TbodyType754 is not None else set()
        self.xhtml_TbodyType749 = xhtml_TbodyType749
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

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
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

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
            if hasattr(old_value, "xhtml_DocumentRoot236"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot236"):
                opp_val = getattr(value, "xhtml_DocumentRoot236", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TbodyType754(self):
        return self.__xhtml_TbodyType754

    @xhtml_TbodyType754.setter
    def xhtml_TbodyType754(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TbodyType__xhtml_TbodyType754", None)
        self.__xhtml_TbodyType754 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType755"):
                    opp_val = getattr(item, "xhtml_TrType755", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType755", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType755"):
                    opp_val = getattr(item, "xhtml_TrType755", None)
                    
                    setattr(item, "xhtml_TrType755", self)
                    

    @property
    def xhtml_TbodyType749(self):
        return self.__xhtml_TbodyType749

    @xhtml_TbodyType749.setter
    def xhtml_TbodyType749(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TbodyType__xhtml_TbodyType749", None)
        self.__xhtml_TbodyType749 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType748"):
                opp_val = getattr(old_value, "xhtml_TableType748", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType748"):
                opp_val = getattr(value, "xhtml_TableType748", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType748", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ParamType:

    def __init__(self, id: str, name: str, valuetype: str, type: str, value: str, xhtml_ParamType: "xhtml_DocumentRoot" = None, xhtml_ParamType525: "xhtml_ObjectType" = None):
        self.id = id
        self.name = name
        self.valuetype = valuetype
        self.type = type
        self.value = value
        self.xhtml_ParamType = xhtml_ParamType
        self.xhtml_ParamType525 = xhtml_ParamType525
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def valuetype(self) -> str:
        return self.__valuetype

    @valuetype.setter
    def valuetype(self, valuetype: str):
        self.__valuetype = valuetype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xhtml_ParamType(self):
        return self.__xhtml_ParamType

    @xhtml_ParamType.setter
    def xhtml_ParamType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ParamType__xhtml_ParamType", None)
        self.__xhtml_ParamType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot204"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot204"):
                opp_val = getattr(value, "xhtml_DocumentRoot204", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ParamType525(self):
        return self.__xhtml_ParamType525

    @xhtml_ParamType525.setter
    def xhtml_ParamType525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ParamType__xhtml_ParamType525", None)
        self.__xhtml_ParamType525 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType524"):
                opp_val = getattr(old_value, "xhtml_ObjectType524", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType524"):
                opp_val = getattr(value, "xhtml_ObjectType524", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType524", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_HtmlType:

    def __init__(self, id: str, xhtml_HtmlType: "xhtml_DocumentRoot" = None, xhtml_HtmlType441: "xhtml_BodyType" = None):
        self.id = id
        self.xhtml_HtmlType = xhtml_HtmlType
        self.xhtml_HtmlType441 = xhtml_HtmlType441
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_HtmlType441(self):
        return self.__xhtml_HtmlType441

    @xhtml_HtmlType441.setter
    def xhtml_HtmlType441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HtmlType__xhtml_HtmlType441", None)
        self.__xhtml_HtmlType441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_BodyType442"):
                opp_val = getattr(old_value, "xhtml_BodyType442", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_BodyType442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_BodyType442"):
                opp_val = getattr(value, "xhtml_BodyType442", None)
                setattr(value, "xhtml_BodyType442", self)

    @property
    def xhtml_HtmlType(self):
        return self.__xhtml_HtmlType

    @xhtml_HtmlType.setter
    def xhtml_HtmlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HtmlType__xhtml_HtmlType", None)
        self.__xhtml_HtmlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot179"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot179"):
                opp_val = getattr(value, "xhtml_DocumentRoot179", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DocumentRoot:

    def __init__(self, mixed: str, xhtml_DocumentRoot: set["xhtml_EStringToStringMapEntry"] = None, xhtml_DocumentRoot95: set["xhtml_EStringToStringMapEntry"] = None, xhtml_DocumentRoot98: set["xhtml_AType"] = None, xhtml_DocumentRoot100: set["xhtml_AbbrType"] = None, xhtml_DocumentRoot103: set["xhtml_AcronymType"] = None, xhtml_DocumentRoot106: set["xhtml_AddressType"] = None, xhtml_DocumentRoot115: set["xhtml_BlockquoteType"] = None, xhtml_DocumentRoot118: set["xhtml_BodyType"] = None, xhtml_DocumentRoot120: set["xhtml_BrType"] = None, xhtml_DocumentRoot123: set["xhtml_CaptionType"] = None, xhtml_DocumentRoot125: set["xhtml_CiteType"] = None, xhtml_DocumentRoot109: set["xhtml_BType"] = None, xhtml_DocumentRoot112: set["xhtml_BigType"] = None, xhtml_DocumentRoot134: set["xhtml_ColgroupType"] = None, xhtml_DocumentRoot137: set["xhtml_DdType"] = None, xhtml_DocumentRoot140: set["xhtml_DelType"] = None, xhtml_DocumentRoot143: set["xhtml_DfnType"] = None, xhtml_DocumentRoot146: set["xhtml_DivType"] = None, xhtml_DocumentRoot149: set["xhtml_DlType"] = None, xhtml_DocumentRoot128: set["xhtml_CodeType"] = None, xhtml_DocumentRoot131: set["xhtml_ColType"] = None, xhtml_DocumentRoot161: set["xhtml_H2Type"] = None, xhtml_DocumentRoot164: set["xhtml_H3Type"] = None, xhtml_DocumentRoot167: set["xhtml_H4Type"] = None, xhtml_DocumentRoot170: set["xhtml_H5Type"] = None, xhtml_DocumentRoot173: set["xhtml_H6Type"] = None, xhtml_DocumentRoot176: set["xhtml_HrType"] = None, xhtml_DocumentRoot179: set["xhtml_HtmlType"] = None, xhtml_DocumentRoot152: set["xhtml_DtType"] = None, xhtml_DocumentRoot155: set["xhtml_EmType"] = None, xhtml_DocumentRoot158: set["xhtml_H1Type"] = None, xhtml_DocumentRoot190: set["xhtml_KbdType"] = None, xhtml_DocumentRoot193: set["xhtml_LiType"] = None, xhtml_DocumentRoot195: set["xhtml_ObjectType"] = None, xhtml_DocumentRoot198: set["xhtml_OlType"] = None, xhtml_DocumentRoot201: set["xhtml_PType"] = None, xhtml_DocumentRoot204: set["xhtml_ParamType"] = None, xhtml_DocumentRoot181: set["xhtml_IType"] = None, xhtml_DocumentRoot184: set["xhtml_ImgType"] = None, xhtml_DocumentRoot187: set["xhtml_InsType"] = None, xhtml_DocumentRoot212: set["xhtml_SampType"] = None, xhtml_DocumentRoot215: set["xhtml_SmallType"] = None, xhtml_DocumentRoot218: set["xhtml_SpanType"] = None, xhtml_DocumentRoot221: set["xhtml_StrikeType"] = None, xhtml_DocumentRoot224: set["xhtml_StrongType"] = None, xhtml_DocumentRoot227: set["xhtml_SubType"] = None, xhtml_DocumentRoot206: set["xhtml_PreType"] = None, xhtml_DocumentRoot209: set["xhtml_QType"] = None, xhtml_DocumentRoot236: set["xhtml_TbodyType"] = None, xhtml_DocumentRoot238: set["xhtml_TdType"] = None, xhtml_DocumentRoot240: set["xhtml_TfootType"] = None, xhtml_DocumentRoot242: set["xhtml_ThType"] = None, xhtml_DocumentRoot230: set["xhtml_SupType"] = None, xhtml_DocumentRoot233: set["xhtml_TableType"] = None, xhtml_DocumentRoot246: set["xhtml_TrType"] = None, xhtml_DocumentRoot248: set["xhtml_TtType"] = None, xhtml_DocumentRoot251: set["xhtml_UType"] = None, xhtml_DocumentRoot254: set["xhtml_UlType"] = None, xhtml_DocumentRoot257: set["xhtml_VarType"] = None, xhtml_DocumentRoot244: set["xhtml_TheadType"] = None):
        self.mixed = mixed
        self.xhtml_DocumentRoot = xhtml_DocumentRoot if xhtml_DocumentRoot is not None else set()
        self.xhtml_DocumentRoot95 = xhtml_DocumentRoot95 if xhtml_DocumentRoot95 is not None else set()
        self.xhtml_DocumentRoot98 = xhtml_DocumentRoot98 if xhtml_DocumentRoot98 is not None else set()
        self.xhtml_DocumentRoot100 = xhtml_DocumentRoot100 if xhtml_DocumentRoot100 is not None else set()
        self.xhtml_DocumentRoot103 = xhtml_DocumentRoot103 if xhtml_DocumentRoot103 is not None else set()
        self.xhtml_DocumentRoot106 = xhtml_DocumentRoot106 if xhtml_DocumentRoot106 is not None else set()
        self.xhtml_DocumentRoot115 = xhtml_DocumentRoot115 if xhtml_DocumentRoot115 is not None else set()
        self.xhtml_DocumentRoot118 = xhtml_DocumentRoot118 if xhtml_DocumentRoot118 is not None else set()
        self.xhtml_DocumentRoot120 = xhtml_DocumentRoot120 if xhtml_DocumentRoot120 is not None else set()
        self.xhtml_DocumentRoot123 = xhtml_DocumentRoot123 if xhtml_DocumentRoot123 is not None else set()
        self.xhtml_DocumentRoot125 = xhtml_DocumentRoot125 if xhtml_DocumentRoot125 is not None else set()
        self.xhtml_DocumentRoot109 = xhtml_DocumentRoot109 if xhtml_DocumentRoot109 is not None else set()
        self.xhtml_DocumentRoot112 = xhtml_DocumentRoot112 if xhtml_DocumentRoot112 is not None else set()
        self.xhtml_DocumentRoot134 = xhtml_DocumentRoot134 if xhtml_DocumentRoot134 is not None else set()
        self.xhtml_DocumentRoot137 = xhtml_DocumentRoot137 if xhtml_DocumentRoot137 is not None else set()
        self.xhtml_DocumentRoot140 = xhtml_DocumentRoot140 if xhtml_DocumentRoot140 is not None else set()
        self.xhtml_DocumentRoot143 = xhtml_DocumentRoot143 if xhtml_DocumentRoot143 is not None else set()
        self.xhtml_DocumentRoot146 = xhtml_DocumentRoot146 if xhtml_DocumentRoot146 is not None else set()
        self.xhtml_DocumentRoot149 = xhtml_DocumentRoot149 if xhtml_DocumentRoot149 is not None else set()
        self.xhtml_DocumentRoot128 = xhtml_DocumentRoot128 if xhtml_DocumentRoot128 is not None else set()
        self.xhtml_DocumentRoot131 = xhtml_DocumentRoot131 if xhtml_DocumentRoot131 is not None else set()
        self.xhtml_DocumentRoot161 = xhtml_DocumentRoot161 if xhtml_DocumentRoot161 is not None else set()
        self.xhtml_DocumentRoot164 = xhtml_DocumentRoot164 if xhtml_DocumentRoot164 is not None else set()
        self.xhtml_DocumentRoot167 = xhtml_DocumentRoot167 if xhtml_DocumentRoot167 is not None else set()
        self.xhtml_DocumentRoot170 = xhtml_DocumentRoot170 if xhtml_DocumentRoot170 is not None else set()
        self.xhtml_DocumentRoot173 = xhtml_DocumentRoot173 if xhtml_DocumentRoot173 is not None else set()
        self.xhtml_DocumentRoot176 = xhtml_DocumentRoot176 if xhtml_DocumentRoot176 is not None else set()
        self.xhtml_DocumentRoot179 = xhtml_DocumentRoot179 if xhtml_DocumentRoot179 is not None else set()
        self.xhtml_DocumentRoot152 = xhtml_DocumentRoot152 if xhtml_DocumentRoot152 is not None else set()
        self.xhtml_DocumentRoot155 = xhtml_DocumentRoot155 if xhtml_DocumentRoot155 is not None else set()
        self.xhtml_DocumentRoot158 = xhtml_DocumentRoot158 if xhtml_DocumentRoot158 is not None else set()
        self.xhtml_DocumentRoot190 = xhtml_DocumentRoot190 if xhtml_DocumentRoot190 is not None else set()
        self.xhtml_DocumentRoot193 = xhtml_DocumentRoot193 if xhtml_DocumentRoot193 is not None else set()
        self.xhtml_DocumentRoot195 = xhtml_DocumentRoot195 if xhtml_DocumentRoot195 is not None else set()
        self.xhtml_DocumentRoot198 = xhtml_DocumentRoot198 if xhtml_DocumentRoot198 is not None else set()
        self.xhtml_DocumentRoot201 = xhtml_DocumentRoot201 if xhtml_DocumentRoot201 is not None else set()
        self.xhtml_DocumentRoot204 = xhtml_DocumentRoot204 if xhtml_DocumentRoot204 is not None else set()
        self.xhtml_DocumentRoot181 = xhtml_DocumentRoot181 if xhtml_DocumentRoot181 is not None else set()
        self.xhtml_DocumentRoot184 = xhtml_DocumentRoot184 if xhtml_DocumentRoot184 is not None else set()
        self.xhtml_DocumentRoot187 = xhtml_DocumentRoot187 if xhtml_DocumentRoot187 is not None else set()
        self.xhtml_DocumentRoot212 = xhtml_DocumentRoot212 if xhtml_DocumentRoot212 is not None else set()
        self.xhtml_DocumentRoot215 = xhtml_DocumentRoot215 if xhtml_DocumentRoot215 is not None else set()
        self.xhtml_DocumentRoot218 = xhtml_DocumentRoot218 if xhtml_DocumentRoot218 is not None else set()
        self.xhtml_DocumentRoot221 = xhtml_DocumentRoot221 if xhtml_DocumentRoot221 is not None else set()
        self.xhtml_DocumentRoot224 = xhtml_DocumentRoot224 if xhtml_DocumentRoot224 is not None else set()
        self.xhtml_DocumentRoot227 = xhtml_DocumentRoot227 if xhtml_DocumentRoot227 is not None else set()
        self.xhtml_DocumentRoot206 = xhtml_DocumentRoot206 if xhtml_DocumentRoot206 is not None else set()
        self.xhtml_DocumentRoot209 = xhtml_DocumentRoot209 if xhtml_DocumentRoot209 is not None else set()
        self.xhtml_DocumentRoot236 = xhtml_DocumentRoot236 if xhtml_DocumentRoot236 is not None else set()
        self.xhtml_DocumentRoot238 = xhtml_DocumentRoot238 if xhtml_DocumentRoot238 is not None else set()
        self.xhtml_DocumentRoot240 = xhtml_DocumentRoot240 if xhtml_DocumentRoot240 is not None else set()
        self.xhtml_DocumentRoot242 = xhtml_DocumentRoot242 if xhtml_DocumentRoot242 is not None else set()
        self.xhtml_DocumentRoot230 = xhtml_DocumentRoot230 if xhtml_DocumentRoot230 is not None else set()
        self.xhtml_DocumentRoot233 = xhtml_DocumentRoot233 if xhtml_DocumentRoot233 is not None else set()
        self.xhtml_DocumentRoot246 = xhtml_DocumentRoot246 if xhtml_DocumentRoot246 is not None else set()
        self.xhtml_DocumentRoot248 = xhtml_DocumentRoot248 if xhtml_DocumentRoot248 is not None else set()
        self.xhtml_DocumentRoot251 = xhtml_DocumentRoot251 if xhtml_DocumentRoot251 is not None else set()
        self.xhtml_DocumentRoot254 = xhtml_DocumentRoot254 if xhtml_DocumentRoot254 is not None else set()
        self.xhtml_DocumentRoot257 = xhtml_DocumentRoot257 if xhtml_DocumentRoot257 is not None else set()
        self.xhtml_DocumentRoot244 = xhtml_DocumentRoot244 if xhtml_DocumentRoot244 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xhtml_DocumentRoot212(self):
        return self.__xhtml_DocumentRoot212

    @xhtml_DocumentRoot212.setter
    def xhtml_DocumentRoot212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot212", None)
        self.__xhtml_DocumentRoot212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType213"):
                    opp_val = getattr(item, "xhtml_SampType213", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType213"):
                    opp_val = getattr(item, "xhtml_SampType213", None)
                    
                    setattr(item, "xhtml_SampType213", self)
                    

    @property
    def xhtml_DocumentRoot98(self):
        return self.__xhtml_DocumentRoot98

    @xhtml_DocumentRoot98.setter
    def xhtml_DocumentRoot98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot98", None)
        self.__xhtml_DocumentRoot98 = value if value is not None else set()
        
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
                if hasattr(item, "xhtml_SpanType219"):
                    opp_val = getattr(item, "xhtml_SpanType219", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType219"):
                    opp_val = getattr(item, "xhtml_SpanType219", None)
                    
                    setattr(item, "xhtml_SpanType219", self)
                    

    @property
    def xhtml_DocumentRoot95(self):
        return self.__xhtml_DocumentRoot95

    @xhtml_DocumentRoot95.setter
    def xhtml_DocumentRoot95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot95", None)
        self.__xhtml_DocumentRoot95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EStringToStringMapEntry96"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry96", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EStringToStringMapEntry96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EStringToStringMapEntry96"):
                    opp_val = getattr(item, "xhtml_EStringToStringMapEntry96", None)
                    
                    setattr(item, "xhtml_EStringToStringMapEntry96", self)
                    

    @property
    def xhtml_DocumentRoot257(self):
        return self.__xhtml_DocumentRoot257

    @xhtml_DocumentRoot257.setter
    def xhtml_DocumentRoot257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot257", None)
        self.__xhtml_DocumentRoot257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType258"):
                    opp_val = getattr(item, "xhtml_VarType258", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType258"):
                    opp_val = getattr(item, "xhtml_VarType258", None)
                    
                    setattr(item, "xhtml_VarType258", self)
                    

    @property
    def xhtml_DocumentRoot221(self):
        return self.__xhtml_DocumentRoot221

    @xhtml_DocumentRoot221.setter
    def xhtml_DocumentRoot221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot221", None)
        self.__xhtml_DocumentRoot221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrikeType222"):
                    opp_val = getattr(item, "xhtml_StrikeType222", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType222"):
                    opp_val = getattr(item, "xhtml_StrikeType222", None)
                    
                    setattr(item, "xhtml_StrikeType222", self)
                    

    @property
    def xhtml_DocumentRoot106(self):
        return self.__xhtml_DocumentRoot106

    @xhtml_DocumentRoot106.setter
    def xhtml_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot106", None)
        self.__xhtml_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType107"):
                    opp_val = getattr(item, "xhtml_AddressType107", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType107"):
                    opp_val = getattr(item, "xhtml_AddressType107", None)
                    
                    setattr(item, "xhtml_AddressType107", self)
                    

    @property
    def xhtml_DocumentRoot236(self):
        return self.__xhtml_DocumentRoot236

    @xhtml_DocumentRoot236.setter
    def xhtml_DocumentRoot236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot236", None)
        self.__xhtml_DocumentRoot236 = value if value is not None else set()
        
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
                if hasattr(item, "xhtml_DelType141"):
                    opp_val = getattr(item, "xhtml_DelType141", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType141"):
                    opp_val = getattr(item, "xhtml_DelType141", None)
                    
                    setattr(item, "xhtml_DelType141", self)
                    

    @property
    def xhtml_DocumentRoot112(self):
        return self.__xhtml_DocumentRoot112

    @xhtml_DocumentRoot112.setter
    def xhtml_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot112", None)
        self.__xhtml_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType113"):
                    opp_val = getattr(item, "xhtml_BigType113", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType113"):
                    opp_val = getattr(item, "xhtml_BigType113", None)
                    
                    setattr(item, "xhtml_BigType113", self)
                    

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
                if hasattr(item, "xhtml_InsType188"):
                    opp_val = getattr(item, "xhtml_InsType188", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType188"):
                    opp_val = getattr(item, "xhtml_InsType188", None)
                    
                    setattr(item, "xhtml_InsType188", self)
                    

    @property
    def xhtml_DocumentRoot227(self):
        return self.__xhtml_DocumentRoot227

    @xhtml_DocumentRoot227.setter
    def xhtml_DocumentRoot227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot227", None)
        self.__xhtml_DocumentRoot227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType228"):
                    opp_val = getattr(item, "xhtml_SubType228", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType228"):
                    opp_val = getattr(item, "xhtml_SubType228", None)
                    
                    setattr(item, "xhtml_SubType228", self)
                    

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
                if hasattr(item, "xhtml_EmType156"):
                    opp_val = getattr(item, "xhtml_EmType156", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType156"):
                    opp_val = getattr(item, "xhtml_EmType156", None)
                    
                    setattr(item, "xhtml_EmType156", self)
                    

    @property
    def xhtml_DocumentRoot195(self):
        return self.__xhtml_DocumentRoot195

    @xhtml_DocumentRoot195.setter
    def xhtml_DocumentRoot195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot195", None)
        self.__xhtml_DocumentRoot195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ObjectType196"):
                    opp_val = getattr(item, "xhtml_ObjectType196", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ObjectType196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ObjectType196"):
                    opp_val = getattr(item, "xhtml_ObjectType196", None)
                    
                    setattr(item, "xhtml_ObjectType196", self)
                    

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
                if hasattr(item, "xhtml_HrType177"):
                    opp_val = getattr(item, "xhtml_HrType177", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType177"):
                    opp_val = getattr(item, "xhtml_HrType177", None)
                    
                    setattr(item, "xhtml_HrType177", self)
                    

    @property
    def xhtml_DocumentRoot198(self):
        return self.__xhtml_DocumentRoot198

    @xhtml_DocumentRoot198.setter
    def xhtml_DocumentRoot198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot198", None)
        self.__xhtml_DocumentRoot198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType199"):
                    opp_val = getattr(item, "xhtml_OlType199", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType199"):
                    opp_val = getattr(item, "xhtml_OlType199", None)
                    
                    setattr(item, "xhtml_OlType199", self)
                    

    @property
    def xhtml_DocumentRoot109(self):
        return self.__xhtml_DocumentRoot109

    @xhtml_DocumentRoot109.setter
    def xhtml_DocumentRoot109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot109", None)
        self.__xhtml_DocumentRoot109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType110"):
                    opp_val = getattr(item, "xhtml_BType110", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType110"):
                    opp_val = getattr(item, "xhtml_BType110", None)
                    
                    setattr(item, "xhtml_BType110", self)
                    

    @property
    def xhtml_DocumentRoot204(self):
        return self.__xhtml_DocumentRoot204

    @xhtml_DocumentRoot204.setter
    def xhtml_DocumentRoot204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot204", None)
        self.__xhtml_DocumentRoot204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ParamType"):
                    opp_val = getattr(item, "xhtml_ParamType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ParamType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ParamType"):
                    opp_val = getattr(item, "xhtml_ParamType", None)
                    
                    setattr(item, "xhtml_ParamType", self)
                    

    @property
    def xhtml_DocumentRoot120(self):
        return self.__xhtml_DocumentRoot120

    @xhtml_DocumentRoot120.setter
    def xhtml_DocumentRoot120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot120", None)
        self.__xhtml_DocumentRoot120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType121"):
                    opp_val = getattr(item, "xhtml_BrType121", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType121"):
                    opp_val = getattr(item, "xhtml_BrType121", None)
                    
                    setattr(item, "xhtml_BrType121", self)
                    

    @property
    def xhtml_DocumentRoot251(self):
        return self.__xhtml_DocumentRoot251

    @xhtml_DocumentRoot251.setter
    def xhtml_DocumentRoot251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot251", None)
        self.__xhtml_DocumentRoot251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UType252"):
                    opp_val = getattr(item, "xhtml_UType252", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType252"):
                    opp_val = getattr(item, "xhtml_UType252", None)
                    
                    setattr(item, "xhtml_UType252", self)
                    

    @property
    def xhtml_DocumentRoot248(self):
        return self.__xhtml_DocumentRoot248

    @xhtml_DocumentRoot248.setter
    def xhtml_DocumentRoot248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot248", None)
        self.__xhtml_DocumentRoot248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType249"):
                    opp_val = getattr(item, "xhtml_TtType249", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType249"):
                    opp_val = getattr(item, "xhtml_TtType249", None)
                    
                    setattr(item, "xhtml_TtType249", self)
                    

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
                if hasattr(item, "xhtml_StrongType225"):
                    opp_val = getattr(item, "xhtml_StrongType225", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType225"):
                    opp_val = getattr(item, "xhtml_StrongType225", None)
                    
                    setattr(item, "xhtml_StrongType225", self)
                    

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
                if hasattr(item, "xhtml_DlType150"):
                    opp_val = getattr(item, "xhtml_DlType150", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType150"):
                    opp_val = getattr(item, "xhtml_DlType150", None)
                    
                    setattr(item, "xhtml_DlType150", self)
                    

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
                if hasattr(item, "xhtml_H3Type165"):
                    opp_val = getattr(item, "xhtml_H3Type165", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type165"):
                    opp_val = getattr(item, "xhtml_H3Type165", None)
                    
                    setattr(item, "xhtml_H3Type165", self)
                    

    @property
    def xhtml_DocumentRoot206(self):
        return self.__xhtml_DocumentRoot206

    @xhtml_DocumentRoot206.setter
    def xhtml_DocumentRoot206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot206", None)
        self.__xhtml_DocumentRoot206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType207"):
                    opp_val = getattr(item, "xhtml_PreType207", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType207"):
                    opp_val = getattr(item, "xhtml_PreType207", None)
                    
                    setattr(item, "xhtml_PreType207", self)
                    

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
                if hasattr(item, "xhtml_CodeType129"):
                    opp_val = getattr(item, "xhtml_CodeType129", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType129"):
                    opp_val = getattr(item, "xhtml_CodeType129", None)
                    
                    setattr(item, "xhtml_CodeType129", self)
                    

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
                if hasattr(item, "xhtml_H4Type168"):
                    opp_val = getattr(item, "xhtml_H4Type168", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type168"):
                    opp_val = getattr(item, "xhtml_H4Type168", None)
                    
                    setattr(item, "xhtml_H4Type168", self)
                    

    @property
    def xhtml_DocumentRoot100(self):
        return self.__xhtml_DocumentRoot100

    @xhtml_DocumentRoot100.setter
    def xhtml_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot100", None)
        self.__xhtml_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType101"):
                    opp_val = getattr(item, "xhtml_AbbrType101", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType101"):
                    opp_val = getattr(item, "xhtml_AbbrType101", None)
                    
                    setattr(item, "xhtml_AbbrType101", self)
                    

    @property
    def xhtml_DocumentRoot179(self):
        return self.__xhtml_DocumentRoot179

    @xhtml_DocumentRoot179.setter
    def xhtml_DocumentRoot179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot179", None)
        self.__xhtml_DocumentRoot179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HtmlType"):
                    opp_val = getattr(item, "xhtml_HtmlType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HtmlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HtmlType"):
                    opp_val = getattr(item, "xhtml_HtmlType", None)
                    
                    setattr(item, "xhtml_HtmlType", self)
                    

    @property
    def xhtml_DocumentRoot215(self):
        return self.__xhtml_DocumentRoot215

    @xhtml_DocumentRoot215.setter
    def xhtml_DocumentRoot215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot215", None)
        self.__xhtml_DocumentRoot215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType216"):
                    opp_val = getattr(item, "xhtml_SmallType216", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType216"):
                    opp_val = getattr(item, "xhtml_SmallType216", None)
                    
                    setattr(item, "xhtml_SmallType216", self)
                    

    @property
    def xhtml_DocumentRoot118(self):
        return self.__xhtml_DocumentRoot118

    @xhtml_DocumentRoot118.setter
    def xhtml_DocumentRoot118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot118", None)
        self.__xhtml_DocumentRoot118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BodyType"):
                    opp_val = getattr(item, "xhtml_BodyType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BodyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BodyType"):
                    opp_val = getattr(item, "xhtml_BodyType", None)
                    
                    setattr(item, "xhtml_BodyType", self)
                    

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
                if hasattr(item, "xhtml_IType182"):
                    opp_val = getattr(item, "xhtml_IType182", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType182"):
                    opp_val = getattr(item, "xhtml_IType182", None)
                    
                    setattr(item, "xhtml_IType182", self)
                    

    @property
    def xhtml_DocumentRoot123(self):
        return self.__xhtml_DocumentRoot123

    @xhtml_DocumentRoot123.setter
    def xhtml_DocumentRoot123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot123", None)
        self.__xhtml_DocumentRoot123 = value if value is not None else set()
        
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
                if hasattr(item, "xhtml_ColgroupType135"):
                    opp_val = getattr(item, "xhtml_ColgroupType135", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColgroupType135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColgroupType135"):
                    opp_val = getattr(item, "xhtml_ColgroupType135", None)
                    
                    setattr(item, "xhtml_ColgroupType135", self)
                    

    @property
    def xhtml_DocumentRoot233(self):
        return self.__xhtml_DocumentRoot233

    @xhtml_DocumentRoot233.setter
    def xhtml_DocumentRoot233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot233", None)
        self.__xhtml_DocumentRoot233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType234"):
                    opp_val = getattr(item, "xhtml_TableType234", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType234"):
                    opp_val = getattr(item, "xhtml_TableType234", None)
                    
                    setattr(item, "xhtml_TableType234", self)
                    

    @property
    def xhtml_DocumentRoot230(self):
        return self.__xhtml_DocumentRoot230

    @xhtml_DocumentRoot230.setter
    def xhtml_DocumentRoot230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot230", None)
        self.__xhtml_DocumentRoot230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType231"):
                    opp_val = getattr(item, "xhtml_SupType231", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType231"):
                    opp_val = getattr(item, "xhtml_SupType231", None)
                    
                    setattr(item, "xhtml_SupType231", self)
                    

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
                if hasattr(item, "xhtml_H6Type174"):
                    opp_val = getattr(item, "xhtml_H6Type174", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type174"):
                    opp_val = getattr(item, "xhtml_H6Type174", None)
                    
                    setattr(item, "xhtml_H6Type174", self)
                    

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
                if hasattr(item, "xhtml_KbdType191"):
                    opp_val = getattr(item, "xhtml_KbdType191", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType191"):
                    opp_val = getattr(item, "xhtml_KbdType191", None)
                    
                    setattr(item, "xhtml_KbdType191", self)
                    

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
                if hasattr(item, "xhtml_H2Type162"):
                    opp_val = getattr(item, "xhtml_H2Type162", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type162"):
                    opp_val = getattr(item, "xhtml_H2Type162", None)
                    
                    setattr(item, "xhtml_H2Type162", self)
                    

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
                if hasattr(item, "xhtml_H1Type159"):
                    opp_val = getattr(item, "xhtml_H1Type159", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type159"):
                    opp_val = getattr(item, "xhtml_H1Type159", None)
                    
                    setattr(item, "xhtml_H1Type159", self)
                    

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
                if hasattr(item, "xhtml_DfnType144"):
                    opp_val = getattr(item, "xhtml_DfnType144", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType144"):
                    opp_val = getattr(item, "xhtml_DfnType144", None)
                    
                    setattr(item, "xhtml_DfnType144", self)
                    

    @property
    def xhtml_DocumentRoot240(self):
        return self.__xhtml_DocumentRoot240

    @xhtml_DocumentRoot240.setter
    def xhtml_DocumentRoot240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot240", None)
        self.__xhtml_DocumentRoot240 = value if value is not None else set()
        
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
    def xhtml_DocumentRoot254(self):
        return self.__xhtml_DocumentRoot254

    @xhtml_DocumentRoot254.setter
    def xhtml_DocumentRoot254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot254", None)
        self.__xhtml_DocumentRoot254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType255"):
                    opp_val = getattr(item, "xhtml_UlType255", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType255"):
                    opp_val = getattr(item, "xhtml_UlType255", None)
                    
                    setattr(item, "xhtml_UlType255", self)
                    

    @property
    def xhtml_DocumentRoot246(self):
        return self.__xhtml_DocumentRoot246

    @xhtml_DocumentRoot246.setter
    def xhtml_DocumentRoot246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot246", None)
        self.__xhtml_DocumentRoot246 = value if value is not None else set()
        
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
                if hasattr(item, "xhtml_DtType153"):
                    opp_val = getattr(item, "xhtml_DtType153", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DtType153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DtType153"):
                    opp_val = getattr(item, "xhtml_DtType153", None)
                    
                    setattr(item, "xhtml_DtType153", self)
                    

    @property
    def xhtml_DocumentRoot209(self):
        return self.__xhtml_DocumentRoot209

    @xhtml_DocumentRoot209.setter
    def xhtml_DocumentRoot209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot209", None)
        self.__xhtml_DocumentRoot209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType210"):
                    opp_val = getattr(item, "xhtml_QType210", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType210"):
                    opp_val = getattr(item, "xhtml_QType210", None)
                    
                    setattr(item, "xhtml_QType210", self)
                    

    @property
    def xhtml_DocumentRoot244(self):
        return self.__xhtml_DocumentRoot244

    @xhtml_DocumentRoot244.setter
    def xhtml_DocumentRoot244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot244", None)
        self.__xhtml_DocumentRoot244 = value if value is not None else set()
        
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
    def xhtml_DocumentRoot201(self):
        return self.__xhtml_DocumentRoot201

    @xhtml_DocumentRoot201.setter
    def xhtml_DocumentRoot201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot201", None)
        self.__xhtml_DocumentRoot201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType202"):
                    opp_val = getattr(item, "xhtml_PType202", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType202"):
                    opp_val = getattr(item, "xhtml_PType202", None)
                    
                    setattr(item, "xhtml_PType202", self)
                    

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
                if hasattr(item, "xhtml_DdType138"):
                    opp_val = getattr(item, "xhtml_DdType138", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DdType138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DdType138"):
                    opp_val = getattr(item, "xhtml_DdType138", None)
                    
                    setattr(item, "xhtml_DdType138", self)
                    

    @property
    def xhtml_DocumentRoot242(self):
        return self.__xhtml_DocumentRoot242

    @xhtml_DocumentRoot242.setter
    def xhtml_DocumentRoot242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot242", None)
        self.__xhtml_DocumentRoot242 = value if value is not None else set()
        
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
    def xhtml_DocumentRoot115(self):
        return self.__xhtml_DocumentRoot115

    @xhtml_DocumentRoot115.setter
    def xhtml_DocumentRoot115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot115", None)
        self.__xhtml_DocumentRoot115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType116"):
                    opp_val = getattr(item, "xhtml_BlockquoteType116", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType116"):
                    opp_val = getattr(item, "xhtml_BlockquoteType116", None)
                    
                    setattr(item, "xhtml_BlockquoteType116", self)
                    

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
                if hasattr(item, "xhtml_H5Type171"):
                    opp_val = getattr(item, "xhtml_H5Type171", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type171"):
                    opp_val = getattr(item, "xhtml_H5Type171", None)
                    
                    setattr(item, "xhtml_H5Type171", self)
                    

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
                if hasattr(item, "xhtml_DivType147"):
                    opp_val = getattr(item, "xhtml_DivType147", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType147"):
                    opp_val = getattr(item, "xhtml_DivType147", None)
                    
                    setattr(item, "xhtml_DivType147", self)
                    

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
                if hasattr(item, "xhtml_CiteType126"):
                    opp_val = getattr(item, "xhtml_CiteType126", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType126"):
                    opp_val = getattr(item, "xhtml_CiteType126", None)
                    
                    setattr(item, "xhtml_CiteType126", self)
                    

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
                if hasattr(item, "xhtml_ColType132"):
                    opp_val = getattr(item, "xhtml_ColType132", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColType132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColType132"):
                    opp_val = getattr(item, "xhtml_ColType132", None)
                    
                    setattr(item, "xhtml_ColType132", self)
                    

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
                if hasattr(item, "xhtml_ImgType185"):
                    opp_val = getattr(item, "xhtml_ImgType185", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType185"):
                    opp_val = getattr(item, "xhtml_ImgType185", None)
                    
                    setattr(item, "xhtml_ImgType185", self)
                    

    @property
    def xhtml_DocumentRoot238(self):
        return self.__xhtml_DocumentRoot238

    @xhtml_DocumentRoot238.setter
    def xhtml_DocumentRoot238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot238", None)
        self.__xhtml_DocumentRoot238 = value if value is not None else set()
        
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
    def xhtml_DocumentRoot103(self):
        return self.__xhtml_DocumentRoot103

    @xhtml_DocumentRoot103.setter
    def xhtml_DocumentRoot103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DocumentRoot__xhtml_DocumentRoot103", None)
        self.__xhtml_DocumentRoot103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType104"):
                    opp_val = getattr(item, "xhtml_AcronymType104", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType104"):
                    opp_val = getattr(item, "xhtml_AcronymType104", None)
                    
                    setattr(item, "xhtml_AcronymType104", self)
                    

class xhtml_EStringToStringMapEntry:

    pass
class Flow:

    pass
class xhtml_LiType(Flow):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_LiType: "xhtml_DocumentRoot" = None, xhtml_LiType657: "xhtml_OlType" = None, xhtml_LiType770: "xhtml_UlType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_LiType = xhtml_LiType
        self.xhtml_LiType657 = xhtml_LiType657
        self.xhtml_LiType770 = xhtml_LiType770
        
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
    def xhtml_LiType770(self):
        return self.__xhtml_LiType770

    @xhtml_LiType770.setter
    def xhtml_LiType770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_LiType__xhtml_LiType770", None)
        self.__xhtml_LiType770 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_UlType769"):
                opp_val = getattr(old_value, "xhtml_UlType769", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_UlType769"):
                opp_val = getattr(value, "xhtml_UlType769", None)
                if opp_val is None:
                    setattr(value, "xhtml_UlType769", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_LiType657(self):
        return self.__xhtml_LiType657

    @xhtml_LiType657.setter
    def xhtml_LiType657(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_LiType__xhtml_LiType657", None)
        self.__xhtml_LiType657 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_OlType656"):
                opp_val = getattr(old_value, "xhtml_OlType656", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_OlType656"):
                opp_val = getattr(value, "xhtml_OlType656", None)
                if opp_val is None:
                    setattr(value, "xhtml_OlType656", set([self]))
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

class xhtml_TdType(Flow):

    def __init__(self, scope: str, abbr1: str, align: str, axis: str, char: str, charoff: str, class: str, colspan: str, headers: str, id: str, rowspan: str, style: str, title: str, valign: str, xhtml_TdType: "xhtml_DocumentRoot" = None, xhtml_TdType767: "xhtml_TrType" = None):
        self.scope = scope
        self.abbr1 = abbr1
        self.align = align
        self.axis = axis
        self.char = char
        self.charoff = charoff
        self.class = class
        self.colspan = colspan
        self.headers = headers
        self.id = id
        self.rowspan = rowspan
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_TdType = xhtml_TdType
        self.xhtml_TdType767 = xhtml_TdType767
        
    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

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
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def abbr1(self) -> str:
        return self.__abbr1

    @abbr1.setter
    def abbr1(self, abbr1: str):
        self.__abbr1 = abbr1

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
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

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
    def xhtml_TdType767(self):
        return self.__xhtml_TdType767

    @xhtml_TdType767.setter
    def xhtml_TdType767(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TdType__xhtml_TdType767", None)
        self.__xhtml_TdType767 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TrType766"):
                opp_val = getattr(old_value, "xhtml_TrType766", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TrType766"):
                opp_val = getattr(value, "xhtml_TrType766", None)
                if opp_val is None:
                    setattr(value, "xhtml_TrType766", set([self]))
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
            if hasattr(old_value, "xhtml_DocumentRoot238"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot238"):
                opp_val = getattr(value, "xhtml_DocumentRoot238", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ThType(Flow):

    def __init__(self, abbr1: str, align: str, axis: str, char: str, charoff: str, class: str, colspan: str, headers: str, id: str, rowspan: str, scope: str, style: str, title: str, valign: str, xhtml_ThType: "xhtml_DocumentRoot" = None, xhtml_ThType764: "xhtml_TrType" = None):
        self.abbr1 = abbr1
        self.align = align
        self.axis = axis
        self.char = char
        self.charoff = charoff
        self.class = class
        self.colspan = colspan
        self.headers = headers
        self.id = id
        self.rowspan = rowspan
        self.scope = scope
        self.style = style
        self.title = title
        self.valign = valign
        self.xhtml_ThType = xhtml_ThType
        self.xhtml_ThType764 = xhtml_ThType764
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

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
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

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
    def headers(self) -> str:
        return self.__headers

    @headers.setter
    def headers(self, headers: str):
        self.__headers = headers

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

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
    def axis(self) -> str:
        return self.__axis

    @axis.setter
    def axis(self, axis: str):
        self.__axis = axis

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def abbr1(self) -> str:
        return self.__abbr1

    @abbr1.setter
    def abbr1(self, abbr1: str):
        self.__abbr1 = abbr1

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
            if hasattr(old_value, "xhtml_DocumentRoot242"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot242"):
                opp_val = getattr(value, "xhtml_DocumentRoot242", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ThType764(self):
        return self.__xhtml_ThType764

    @xhtml_ThType764.setter
    def xhtml_ThType764(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ThType__xhtml_ThType764", None)
        self.__xhtml_ThType764 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TrType763"):
                opp_val = getattr(old_value, "xhtml_TrType763", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TrType763"):
                opp_val = getattr(value, "xhtml_TrType763", None)
                if opp_val is None:
                    setattr(value, "xhtml_TrType763", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DdType(Flow):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_DdType: "xhtml_DlType" = None, xhtml_DdType138: "xhtml_DocumentRoot" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_DdType = xhtml_DdType
        self.xhtml_DdType138 = xhtml_DdType138
        
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
    def xhtml_DdType(self):
        return self.__xhtml_DdType

    @xhtml_DdType.setter
    def xhtml_DdType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DdType__xhtml_DdType", None)
        self.__xhtml_DdType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DlType92"):
                opp_val = getattr(old_value, "xhtml_DlType92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DlType92"):
                opp_val = getattr(value, "xhtml_DlType92", None)
                if opp_val is None:
                    setattr(value, "xhtml_DlType92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DdType138(self):
        return self.__xhtml_DdType138

    @xhtml_DdType138.setter
    def xhtml_DdType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DdType__xhtml_DdType138", None)
        self.__xhtml_DdType138 = value
        
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

class xhtml_ColType:

    def __init__(self, align: str, char: str, charoff: str, class: str, id: str, span: str, style: str, title: str, valign: str, width: str, xhtml_ColType: "xhtml_ColgroupType" = None, xhtml_ColType132: "xhtml_DocumentRoot" = None, xhtml_ColType737: "xhtml_TableType" = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.span = span
        self.style = style
        self.title = title
        self.valign = valign
        self.width = width
        self.xhtml_ColType = xhtml_ColType
        self.xhtml_ColType132 = xhtml_ColType132
        self.xhtml_ColType737 = xhtml_ColType737
        
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
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

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
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def xhtml_ColType737(self):
        return self.__xhtml_ColType737

    @xhtml_ColType737.setter
    def xhtml_ColType737(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColType__xhtml_ColType737", None)
        self.__xhtml_ColType737 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType736"):
                opp_val = getattr(old_value, "xhtml_TableType736", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType736"):
                opp_val = getattr(value, "xhtml_TableType736", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType736", set([self]))
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
    def xhtml_ColType132(self):
        return self.__xhtml_ColType132

    @xhtml_ColType132.setter
    def xhtml_ColType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColType__xhtml_ColType132", None)
        self.__xhtml_ColType132 = value
        
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

class xhtml_ColgroupType:

    def __init__(self, char: str, charoff: str, class: str, id: str, span: str, style: str, title: str, valign: str, width: str, align: str, xhtml_ColgroupType: set["xhtml_ColType"] = None, xhtml_ColgroupType135: "xhtml_DocumentRoot" = None, xhtml_ColgroupType740: "xhtml_TableType" = None):
        self.char = char
        self.charoff = charoff
        self.class = class
        self.id = id
        self.span = span
        self.style = style
        self.title = title
        self.valign = valign
        self.width = width
        self.align = align
        self.xhtml_ColgroupType = xhtml_ColgroupType if xhtml_ColgroupType is not None else set()
        self.xhtml_ColgroupType135 = xhtml_ColgroupType135
        self.xhtml_ColgroupType740 = xhtml_ColgroupType740
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

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
    def xhtml_ColgroupType740(self):
        return self.__xhtml_ColgroupType740

    @xhtml_ColgroupType740.setter
    def xhtml_ColgroupType740(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColgroupType__xhtml_ColgroupType740", None)
        self.__xhtml_ColgroupType740 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType739"):
                opp_val = getattr(old_value, "xhtml_TableType739", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType739"):
                opp_val = getattr(value, "xhtml_TableType739", None)
                if opp_val is None:
                    setattr(value, "xhtml_TableType739", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def xhtml_ColgroupType135(self):
        return self.__xhtml_ColgroupType135

    @xhtml_ColgroupType135.setter
    def xhtml_ColgroupType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ColgroupType__xhtml_ColgroupType135", None)
        self.__xhtml_ColgroupType135 = value
        
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

class Block:

    pass
class xhtml_BodyType(Block):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_BodyType: "xhtml_DocumentRoot" = None, xhtml_BodyType442: "xhtml_HtmlType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BodyType = xhtml_BodyType
        self.xhtml_BodyType442 = xhtml_BodyType442
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_BodyType442(self):
        return self.__xhtml_BodyType442

    @xhtml_BodyType442.setter
    def xhtml_BodyType442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BodyType__xhtml_BodyType442", None)
        self.__xhtml_BodyType442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_HtmlType441"):
                opp_val = getattr(old_value, "xhtml_HtmlType441", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_HtmlType441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_HtmlType441"):
                opp_val = getattr(value, "xhtml_HtmlType441", None)
                setattr(value, "xhtml_HtmlType441", self)

    @property
    def xhtml_BodyType(self):
        return self.__xhtml_BodyType

    @xhtml_BodyType.setter
    def xhtml_BodyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BodyType__xhtml_BodyType", None)
        self.__xhtml_BodyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot118"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot118"):
                opp_val = getattr(value, "xhtml_DocumentRoot118", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_PreType(PreContent):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_PreType: "xhtml_Block" = None, xhtml_PreType207: "xhtml_DocumentRoot" = None, xhtml_PreType293: "xhtml_Flow" = None, xhtml_PreType421: "xhtml_FormContent" = None, xhtml_PreType561: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_PreType = xhtml_PreType
        self.xhtml_PreType207 = xhtml_PreType207
        self.xhtml_PreType293 = xhtml_PreType293
        self.xhtml_PreType421 = xhtml_PreType421
        self.xhtml_PreType561 = xhtml_PreType561
        
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
    def xhtml_PreType207(self):
        return self.__xhtml_PreType207

    @xhtml_PreType207.setter
    def xhtml_PreType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType207", None)
        self.__xhtml_PreType207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot206"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot206"):
                opp_val = getattr(value, "xhtml_DocumentRoot206", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType561(self):
        return self.__xhtml_PreType561

    @xhtml_PreType561.setter
    def xhtml_PreType561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType561", None)
        self.__xhtml_PreType561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType560"):
                opp_val = getattr(old_value, "xhtml_ObjectType560", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType560"):
                opp_val = getattr(value, "xhtml_ObjectType560", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType560", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType293(self):
        return self.__xhtml_PreType293

    @xhtml_PreType293.setter
    def xhtml_PreType293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType293", None)
        self.__xhtml_PreType293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow292"):
                opp_val = getattr(old_value, "xhtml_Flow292", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow292"):
                opp_val = getattr(value, "xhtml_Flow292", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow292", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PreType421(self):
        return self.__xhtml_PreType421

    @xhtml_PreType421.setter
    def xhtml_PreType421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreType__xhtml_PreType421", None)
        self.__xhtml_PreType421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent420"):
                opp_val = getattr(old_value, "xhtml_FormContent420", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent420"):
                opp_val = getattr(value, "xhtml_FormContent420", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent420", set([self]))
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

class xhtml_DlType:

    def __init__(self, group: str, class: str, id: str, style: str, title: str, xhtml_DlType: "xhtml_Block" = None, xhtml_DlType90: set["xhtml_DtType"] = None, xhtml_DlType92: set["xhtml_DdType"] = None, xhtml_DlType150: "xhtml_DocumentRoot" = None, xhtml_DlType290: "xhtml_Flow" = None, xhtml_DlType418: "xhtml_FormContent" = None, xhtml_DlType558: "xhtml_ObjectType" = None):
        self.group = group
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_DlType = xhtml_DlType
        self.xhtml_DlType90 = xhtml_DlType90 if xhtml_DlType90 is not None else set()
        self.xhtml_DlType92 = xhtml_DlType92 if xhtml_DlType92 is not None else set()
        self.xhtml_DlType150 = xhtml_DlType150
        self.xhtml_DlType290 = xhtml_DlType290
        self.xhtml_DlType418 = xhtml_DlType418
        self.xhtml_DlType558 = xhtml_DlType558
        
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
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_DlType418(self):
        return self.__xhtml_DlType418

    @xhtml_DlType418.setter
    def xhtml_DlType418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType418", None)
        self.__xhtml_DlType418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent417"):
                opp_val = getattr(old_value, "xhtml_FormContent417", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent417"):
                opp_val = getattr(value, "xhtml_FormContent417", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent417", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DlType90(self):
        return self.__xhtml_DlType90

    @xhtml_DlType90.setter
    def xhtml_DlType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType90", None)
        self.__xhtml_DlType90 = value if value is not None else set()
        
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
    def xhtml_DlType290(self):
        return self.__xhtml_DlType290

    @xhtml_DlType290.setter
    def xhtml_DlType290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType290", None)
        self.__xhtml_DlType290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow289"):
                opp_val = getattr(old_value, "xhtml_Flow289", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow289"):
                opp_val = getattr(value, "xhtml_Flow289", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow289", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DlType150(self):
        return self.__xhtml_DlType150

    @xhtml_DlType150.setter
    def xhtml_DlType150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType150", None)
        self.__xhtml_DlType150 = value
        
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
    def xhtml_DlType92(self):
        return self.__xhtml_DlType92

    @xhtml_DlType92.setter
    def xhtml_DlType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType92", None)
        self.__xhtml_DlType92 = value if value is not None else set()
        
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
    def xhtml_DlType558(self):
        return self.__xhtml_DlType558

    @xhtml_DlType558.setter
    def xhtml_DlType558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DlType__xhtml_DlType558", None)
        self.__xhtml_DlType558 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType557"):
                opp_val = getattr(old_value, "xhtml_ObjectType557", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType557"):
                opp_val = getattr(value, "xhtml_ObjectType557", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType557", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class xhtml_OlType:

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_OlType: "xhtml_Block" = None, xhtml_OlType199: "xhtml_DocumentRoot" = None, xhtml_OlType287: "xhtml_Flow" = None, xhtml_OlType415: "xhtml_FormContent" = None, xhtml_OlType555: "xhtml_ObjectType" = None, xhtml_OlType656: set["xhtml_LiType"] = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_OlType = xhtml_OlType
        self.xhtml_OlType199 = xhtml_OlType199
        self.xhtml_OlType287 = xhtml_OlType287
        self.xhtml_OlType415 = xhtml_OlType415
        self.xhtml_OlType555 = xhtml_OlType555
        self.xhtml_OlType656 = xhtml_OlType656 if xhtml_OlType656 is not None else set()
        
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
    def xhtml_OlType287(self):
        return self.__xhtml_OlType287

    @xhtml_OlType287.setter
    def xhtml_OlType287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType287", None)
        self.__xhtml_OlType287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow286"):
                opp_val = getattr(old_value, "xhtml_Flow286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow286"):
                opp_val = getattr(value, "xhtml_Flow286", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType199(self):
        return self.__xhtml_OlType199

    @xhtml_OlType199.setter
    def xhtml_OlType199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType199", None)
        self.__xhtml_OlType199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot198"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot198"):
                opp_val = getattr(value, "xhtml_DocumentRoot198", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType656(self):
        return self.__xhtml_OlType656

    @xhtml_OlType656.setter
    def xhtml_OlType656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType656", None)
        self.__xhtml_OlType656 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_LiType657"):
                    opp_val = getattr(item, "xhtml_LiType657", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_LiType657", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_LiType657"):
                    opp_val = getattr(item, "xhtml_LiType657", None)
                    
                    setattr(item, "xhtml_LiType657", self)
                    

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
    def xhtml_OlType555(self):
        return self.__xhtml_OlType555

    @xhtml_OlType555.setter
    def xhtml_OlType555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType555", None)
        self.__xhtml_OlType555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType554"):
                opp_val = getattr(old_value, "xhtml_ObjectType554", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType554"):
                opp_val = getattr(value, "xhtml_ObjectType554", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType554", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_OlType415(self):
        return self.__xhtml_OlType415

    @xhtml_OlType415.setter
    def xhtml_OlType415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_OlType__xhtml_OlType415", None)
        self.__xhtml_OlType415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent414"):
                opp_val = getattr(old_value, "xhtml_FormContent414", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent414"):
                opp_val = getattr(value, "xhtml_FormContent414", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent414", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TableType:

    def __init__(self, border: str, cellpadding: str, cellspacing: str, class: str, id: str, style: str, summary: str, title: str, width: str, xhtml_TableType: "xhtml_Block" = None, xhtml_TableType234: "xhtml_DocumentRoot" = None, xhtml_TableType305: "xhtml_Flow" = None, xhtml_TableType433: "xhtml_FormContent" = None, xhtml_TableType573: "xhtml_ObjectType" = None, xhtml_TableType733: "xhtml_CaptionType" = None, xhtml_TableType736: set["xhtml_ColType"] = None, xhtml_TableType739: set["xhtml_ColgroupType"] = None, xhtml_TableType742: "xhtml_TheadType" = None, xhtml_TableType745: "xhtml_TfootType" = None, xhtml_TableType748: set["xhtml_TbodyType"] = None, xhtml_TableType751: set["xhtml_TrType"] = None):
        self.border = border
        self.cellpadding = cellpadding
        self.cellspacing = cellspacing
        self.class = class
        self.id = id
        self.style = style
        self.summary = summary
        self.title = title
        self.width = width
        self.xhtml_TableType = xhtml_TableType
        self.xhtml_TableType234 = xhtml_TableType234
        self.xhtml_TableType305 = xhtml_TableType305
        self.xhtml_TableType433 = xhtml_TableType433
        self.xhtml_TableType573 = xhtml_TableType573
        self.xhtml_TableType733 = xhtml_TableType733
        self.xhtml_TableType736 = xhtml_TableType736 if xhtml_TableType736 is not None else set()
        self.xhtml_TableType739 = xhtml_TableType739 if xhtml_TableType739 is not None else set()
        self.xhtml_TableType742 = xhtml_TableType742
        self.xhtml_TableType745 = xhtml_TableType745
        self.xhtml_TableType748 = xhtml_TableType748 if xhtml_TableType748 is not None else set()
        self.xhtml_TableType751 = xhtml_TableType751 if xhtml_TableType751 is not None else set()
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

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
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

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
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

    @property
    def cellpadding(self) -> str:
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding

    @property
    def xhtml_TableType748(self):
        return self.__xhtml_TableType748

    @xhtml_TableType748.setter
    def xhtml_TableType748(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType748", None)
        self.__xhtml_TableType748 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TbodyType749"):
                    opp_val = getattr(item, "xhtml_TbodyType749", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TbodyType749", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TbodyType749"):
                    opp_val = getattr(item, "xhtml_TbodyType749", None)
                    
                    setattr(item, "xhtml_TbodyType749", self)
                    

    @property
    def xhtml_TableType733(self):
        return self.__xhtml_TableType733

    @xhtml_TableType733.setter
    def xhtml_TableType733(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType733", None)
        self.__xhtml_TableType733 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_CaptionType734"):
                opp_val = getattr(old_value, "xhtml_CaptionType734", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_CaptionType734", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_CaptionType734"):
                opp_val = getattr(value, "xhtml_CaptionType734", None)
                setattr(value, "xhtml_CaptionType734", self)

    @property
    def xhtml_TableType433(self):
        return self.__xhtml_TableType433

    @xhtml_TableType433.setter
    def xhtml_TableType433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType433", None)
        self.__xhtml_TableType433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent432"):
                opp_val = getattr(old_value, "xhtml_FormContent432", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent432"):
                opp_val = getattr(value, "xhtml_FormContent432", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent432", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "xhtml_Block81"):
                opp_val = getattr(old_value, "xhtml_Block81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block81"):
                opp_val = getattr(value, "xhtml_Block81", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType742(self):
        return self.__xhtml_TableType742

    @xhtml_TableType742.setter
    def xhtml_TableType742(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType742", None)
        self.__xhtml_TableType742 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TheadType743"):
                opp_val = getattr(old_value, "xhtml_TheadType743", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TheadType743", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TheadType743"):
                opp_val = getattr(value, "xhtml_TheadType743", None)
                setattr(value, "xhtml_TheadType743", self)

    @property
    def xhtml_TableType234(self):
        return self.__xhtml_TableType234

    @xhtml_TableType234.setter
    def xhtml_TableType234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType234", None)
        self.__xhtml_TableType234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot233"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot233"):
                opp_val = getattr(value, "xhtml_DocumentRoot233", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType736(self):
        return self.__xhtml_TableType736

    @xhtml_TableType736.setter
    def xhtml_TableType736(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType736", None)
        self.__xhtml_TableType736 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColType737"):
                    opp_val = getattr(item, "xhtml_ColType737", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColType737", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColType737"):
                    opp_val = getattr(item, "xhtml_ColType737", None)
                    
                    setattr(item, "xhtml_ColType737", self)
                    

    @property
    def xhtml_TableType573(self):
        return self.__xhtml_TableType573

    @xhtml_TableType573.setter
    def xhtml_TableType573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType573", None)
        self.__xhtml_TableType573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType572"):
                opp_val = getattr(old_value, "xhtml_ObjectType572", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType572"):
                opp_val = getattr(value, "xhtml_ObjectType572", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType572", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType305(self):
        return self.__xhtml_TableType305

    @xhtml_TableType305.setter
    def xhtml_TableType305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType305", None)
        self.__xhtml_TableType305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow304"):
                opp_val = getattr(old_value, "xhtml_Flow304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow304"):
                opp_val = getattr(value, "xhtml_Flow304", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow304", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TableType739(self):
        return self.__xhtml_TableType739

    @xhtml_TableType739.setter
    def xhtml_TableType739(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType739", None)
        self.__xhtml_TableType739 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ColgroupType740"):
                    opp_val = getattr(item, "xhtml_ColgroupType740", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ColgroupType740", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ColgroupType740"):
                    opp_val = getattr(item, "xhtml_ColgroupType740", None)
                    
                    setattr(item, "xhtml_ColgroupType740", self)
                    

    @property
    def xhtml_TableType745(self):
        return self.__xhtml_TableType745

    @xhtml_TableType745.setter
    def xhtml_TableType745(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType745", None)
        self.__xhtml_TableType745 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TfootType746"):
                opp_val = getattr(old_value, "xhtml_TfootType746", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TfootType746", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TfootType746"):
                opp_val = getattr(value, "xhtml_TfootType746", None)
                setattr(value, "xhtml_TfootType746", self)

    @property
    def xhtml_TableType751(self):
        return self.__xhtml_TableType751

    @xhtml_TableType751.setter
    def xhtml_TableType751(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TableType__xhtml_TableType751", None)
        self.__xhtml_TableType751 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TrType752"):
                    opp_val = getattr(item, "xhtml_TrType752", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TrType752", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TrType752"):
                    opp_val = getattr(item, "xhtml_TrType752", None)
                    
                    setattr(item, "xhtml_TrType752", self)
                    

class xhtml_BlockquoteType(Block):

    def __init__(self, cite: str, class: str, id: str, style: str, title: str, xhtml_BlockquoteType: "xhtml_Block" = None, xhtml_BlockquoteType116: "xhtml_DocumentRoot" = None, xhtml_BlockquoteType299: "xhtml_Flow" = None, xhtml_BlockquoteType427: "xhtml_FormContent" = None, xhtml_BlockquoteType567: "xhtml_ObjectType" = None):
        self.cite = cite
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BlockquoteType = xhtml_BlockquoteType
        self.xhtml_BlockquoteType116 = xhtml_BlockquoteType116
        self.xhtml_BlockquoteType299 = xhtml_BlockquoteType299
        self.xhtml_BlockquoteType427 = xhtml_BlockquoteType427
        self.xhtml_BlockquoteType567 = xhtml_BlockquoteType567
        
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
    def cite(self) -> str:
        return self.__cite

    @cite.setter
    def cite(self, cite: str):
        self.__cite = cite

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
    def xhtml_BlockquoteType(self):
        return self.__xhtml_BlockquoteType

    @xhtml_BlockquoteType.setter
    def xhtml_BlockquoteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType", None)
        self.__xhtml_BlockquoteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block77"):
                opp_val = getattr(old_value, "xhtml_Block77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block77"):
                opp_val = getattr(value, "xhtml_Block77", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType427(self):
        return self.__xhtml_BlockquoteType427

    @xhtml_BlockquoteType427.setter
    def xhtml_BlockquoteType427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType427", None)
        self.__xhtml_BlockquoteType427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent426"):
                opp_val = getattr(old_value, "xhtml_FormContent426", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent426"):
                opp_val = getattr(value, "xhtml_FormContent426", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent426", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType116(self):
        return self.__xhtml_BlockquoteType116

    @xhtml_BlockquoteType116.setter
    def xhtml_BlockquoteType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType116", None)
        self.__xhtml_BlockquoteType116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot115"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot115"):
                opp_val = getattr(value, "xhtml_DocumentRoot115", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType567(self):
        return self.__xhtml_BlockquoteType567

    @xhtml_BlockquoteType567.setter
    def xhtml_BlockquoteType567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType567", None)
        self.__xhtml_BlockquoteType567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType566"):
                opp_val = getattr(old_value, "xhtml_ObjectType566", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType566"):
                opp_val = getattr(value, "xhtml_ObjectType566", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType566", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BlockquoteType299(self):
        return self.__xhtml_BlockquoteType299

    @xhtml_BlockquoteType299.setter
    def xhtml_BlockquoteType299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BlockquoteType__xhtml_BlockquoteType299", None)
        self.__xhtml_BlockquoteType299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow298"):
                opp_val = getattr(old_value, "xhtml_Flow298", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow298"):
                opp_val = getattr(value, "xhtml_Flow298", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow298", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_HrType:

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_HrType: "xhtml_Block" = None, xhtml_HrType177: "xhtml_DocumentRoot" = None, xhtml_HrType296: "xhtml_Flow" = None, xhtml_HrType424: "xhtml_FormContent" = None, xhtml_HrType564: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_HrType = xhtml_HrType
        self.xhtml_HrType177 = xhtml_HrType177
        self.xhtml_HrType296 = xhtml_HrType296
        self.xhtml_HrType424 = xhtml_HrType424
        self.xhtml_HrType564 = xhtml_HrType564
        
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
    def xhtml_HrType177(self):
        return self.__xhtml_HrType177

    @xhtml_HrType177.setter
    def xhtml_HrType177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType177", None)
        self.__xhtml_HrType177 = value
        
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

    @property
    def xhtml_HrType564(self):
        return self.__xhtml_HrType564

    @xhtml_HrType564.setter
    def xhtml_HrType564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType564", None)
        self.__xhtml_HrType564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType563"):
                opp_val = getattr(old_value, "xhtml_ObjectType563", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType563"):
                opp_val = getattr(value, "xhtml_ObjectType563", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType563", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def xhtml_HrType424(self):
        return self.__xhtml_HrType424

    @xhtml_HrType424.setter
    def xhtml_HrType424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType424", None)
        self.__xhtml_HrType424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent423"):
                opp_val = getattr(old_value, "xhtml_FormContent423", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent423"):
                opp_val = getattr(value, "xhtml_FormContent423", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent423", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_HrType296(self):
        return self.__xhtml_HrType296

    @xhtml_HrType296.setter
    def xhtml_HrType296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_HrType__xhtml_HrType296", None)
        self.__xhtml_HrType296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow295"):
                opp_val = getattr(old_value, "xhtml_Flow295", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow295"):
                opp_val = getattr(value, "xhtml_Flow295", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow295", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_UlType:

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_UlType: "xhtml_Block" = None, xhtml_UlType255: "xhtml_DocumentRoot" = None, xhtml_UlType284: "xhtml_Flow" = None, xhtml_UlType412: "xhtml_FormContent" = None, xhtml_UlType552: "xhtml_ObjectType" = None, xhtml_UlType769: set["xhtml_LiType"] = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_UlType = xhtml_UlType
        self.xhtml_UlType255 = xhtml_UlType255
        self.xhtml_UlType284 = xhtml_UlType284
        self.xhtml_UlType412 = xhtml_UlType412
        self.xhtml_UlType552 = xhtml_UlType552
        self.xhtml_UlType769 = xhtml_UlType769 if xhtml_UlType769 is not None else set()
        
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
    def xhtml_UlType552(self):
        return self.__xhtml_UlType552

    @xhtml_UlType552.setter
    def xhtml_UlType552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType552", None)
        self.__xhtml_UlType552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType551"):
                opp_val = getattr(old_value, "xhtml_ObjectType551", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType551"):
                opp_val = getattr(value, "xhtml_ObjectType551", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType551", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UlType284(self):
        return self.__xhtml_UlType284

    @xhtml_UlType284.setter
    def xhtml_UlType284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType284", None)
        self.__xhtml_UlType284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow283"):
                opp_val = getattr(old_value, "xhtml_Flow283", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow283"):
                opp_val = getattr(value, "xhtml_Flow283", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow283", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def xhtml_UlType255(self):
        return self.__xhtml_UlType255

    @xhtml_UlType255.setter
    def xhtml_UlType255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType255", None)
        self.__xhtml_UlType255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot254"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot254"):
                opp_val = getattr(value, "xhtml_DocumentRoot254", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UlType769(self):
        return self.__xhtml_UlType769

    @xhtml_UlType769.setter
    def xhtml_UlType769(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType769", None)
        self.__xhtml_UlType769 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_LiType770"):
                    opp_val = getattr(item, "xhtml_LiType770", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_LiType770", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_LiType770"):
                    opp_val = getattr(item, "xhtml_LiType770", None)
                    
                    setattr(item, "xhtml_LiType770", self)
                    

    @property
    def xhtml_UlType412(self):
        return self.__xhtml_UlType412

    @xhtml_UlType412.setter
    def xhtml_UlType412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UlType__xhtml_UlType412", None)
        self.__xhtml_UlType412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent411"):
                opp_val = getattr(old_value, "xhtml_FormContent411", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent411"):
                opp_val = getattr(value, "xhtml_FormContent411", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent411", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DivType(Flow):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_DivType: "xhtml_Block" = None, xhtml_DivType147: "xhtml_DocumentRoot" = None, xhtml_DivType281: "xhtml_Flow" = None, xhtml_DivType409: "xhtml_FormContent" = None, xhtml_DivType549: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_DivType = xhtml_DivType
        self.xhtml_DivType147 = xhtml_DivType147
        self.xhtml_DivType281 = xhtml_DivType281
        self.xhtml_DivType409 = xhtml_DivType409
        self.xhtml_DivType549 = xhtml_DivType549
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xhtml_DivType281(self):
        return self.__xhtml_DivType281

    @xhtml_DivType281.setter
    def xhtml_DivType281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType281", None)
        self.__xhtml_DivType281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow280"):
                opp_val = getattr(old_value, "xhtml_Flow280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow280"):
                opp_val = getattr(value, "xhtml_Flow280", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DivType147(self):
        return self.__xhtml_DivType147

    @xhtml_DivType147.setter
    def xhtml_DivType147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType147", None)
        self.__xhtml_DivType147 = value
        
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
    def xhtml_DivType409(self):
        return self.__xhtml_DivType409

    @xhtml_DivType409.setter
    def xhtml_DivType409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType409", None)
        self.__xhtml_DivType409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent408"):
                opp_val = getattr(old_value, "xhtml_FormContent408", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent408"):
                opp_val = getattr(value, "xhtml_FormContent408", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent408", set([self]))
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
    def xhtml_DivType549(self):
        return self.__xhtml_DivType549

    @xhtml_DivType549.setter
    def xhtml_DivType549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DivType__xhtml_DivType549", None)
        self.__xhtml_DivType549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType548"):
                opp_val = getattr(old_value, "xhtml_ObjectType548", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType548"):
                opp_val = getattr(value, "xhtml_ObjectType548", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType548", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Block:

    def __init__(self, group: str, xhtml_Block: set["xhtml_PType"] = None, xhtml_Block57: set["xhtml_H3Type"] = None, xhtml_Block59: set["xhtml_H4Type"] = None, xhtml_Block61: set["xhtml_H5Type"] = None, xhtml_Block63: set["xhtml_H6Type"] = None, xhtml_Block65: set["xhtml_DivType"] = None, xhtml_Block67: set["xhtml_UlType"] = None, xhtml_Block53: set["xhtml_H1Type"] = None, xhtml_Block75: set["xhtml_HrType"] = None, xhtml_Block55: set["xhtml_H2Type"] = None, xhtml_Block77: set["xhtml_BlockquoteType"] = None, xhtml_Block79: set["xhtml_AddressType"] = None, xhtml_Block81: set["xhtml_TableType"] = None, xhtml_Block83: set["xhtml_InsType"] = None, xhtml_Block86: set["xhtml_DelType"] = None, xhtml_Block69: set["xhtml_OlType"] = None, xhtml_Block71: set["xhtml_DlType"] = None, xhtml_Block73: set["xhtml_PreType"] = None):
        self.group = group
        self.xhtml_Block = xhtml_Block if xhtml_Block is not None else set()
        self.xhtml_Block57 = xhtml_Block57 if xhtml_Block57 is not None else set()
        self.xhtml_Block59 = xhtml_Block59 if xhtml_Block59 is not None else set()
        self.xhtml_Block61 = xhtml_Block61 if xhtml_Block61 is not None else set()
        self.xhtml_Block63 = xhtml_Block63 if xhtml_Block63 is not None else set()
        self.xhtml_Block65 = xhtml_Block65 if xhtml_Block65 is not None else set()
        self.xhtml_Block67 = xhtml_Block67 if xhtml_Block67 is not None else set()
        self.xhtml_Block53 = xhtml_Block53 if xhtml_Block53 is not None else set()
        self.xhtml_Block75 = xhtml_Block75 if xhtml_Block75 is not None else set()
        self.xhtml_Block55 = xhtml_Block55 if xhtml_Block55 is not None else set()
        self.xhtml_Block77 = xhtml_Block77 if xhtml_Block77 is not None else set()
        self.xhtml_Block79 = xhtml_Block79 if xhtml_Block79 is not None else set()
        self.xhtml_Block81 = xhtml_Block81 if xhtml_Block81 is not None else set()
        self.xhtml_Block83 = xhtml_Block83 if xhtml_Block83 is not None else set()
        self.xhtml_Block86 = xhtml_Block86 if xhtml_Block86 is not None else set()
        self.xhtml_Block69 = xhtml_Block69 if xhtml_Block69 is not None else set()
        self.xhtml_Block71 = xhtml_Block71 if xhtml_Block71 is not None else set()
        self.xhtml_Block73 = xhtml_Block73 if xhtml_Block73 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_Block83(self):
        return self.__xhtml_Block83

    @xhtml_Block83.setter
    def xhtml_Block83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block83", None)
        self.__xhtml_Block83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType84"):
                    opp_val = getattr(item, "xhtml_InsType84", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType84"):
                    opp_val = getattr(item, "xhtml_InsType84", None)
                    
                    setattr(item, "xhtml_InsType84", self)
                    

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
    def xhtml_Block77(self):
        return self.__xhtml_Block77

    @xhtml_Block77.setter
    def xhtml_Block77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block77", None)
        self.__xhtml_Block77 = value if value is not None else set()
        
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
    def xhtml_Block79(self):
        return self.__xhtml_Block79

    @xhtml_Block79.setter
    def xhtml_Block79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block79", None)
        self.__xhtml_Block79 = value if value is not None else set()
        
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
    def xhtml_Block86(self):
        return self.__xhtml_Block86

    @xhtml_Block86.setter
    def xhtml_Block86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block86", None)
        self.__xhtml_Block86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType87"):
                    opp_val = getattr(item, "xhtml_DelType87", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType87"):
                    opp_val = getattr(item, "xhtml_DelType87", None)
                    
                    setattr(item, "xhtml_DelType87", self)
                    

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
    def xhtml_Block81(self):
        return self.__xhtml_Block81

    @xhtml_Block81.setter
    def xhtml_Block81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block81", None)
        self.__xhtml_Block81 = value if value is not None else set()
        
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
                    

class xhtml_DelType(Flow):

    def __init__(self, cite1: str, class: str, datetime: str, id: str, style: str, title: str, xhtml_DelType: "xhtml_AContent" = None, xhtml_DelType87: "xhtml_Block" = None, xhtml_DelType141: "xhtml_DocumentRoot" = None, xhtml_DelType386: "xhtml_Flow" = None, xhtml_DelType439: "xhtml_FormContent" = None, xhtml_DelType522: "xhtml_Inline" = None, xhtml_DelType654: "xhtml_ObjectType" = None, xhtml_DelType731: "xhtml_PreContent" = None):
        self.cite1 = cite1
        self.class = class
        self.datetime = datetime
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_DelType = xhtml_DelType
        self.xhtml_DelType87 = xhtml_DelType87
        self.xhtml_DelType141 = xhtml_DelType141
        self.xhtml_DelType386 = xhtml_DelType386
        self.xhtml_DelType439 = xhtml_DelType439
        self.xhtml_DelType522 = xhtml_DelType522
        self.xhtml_DelType654 = xhtml_DelType654
        self.xhtml_DelType731 = xhtml_DelType731
        
    @property
    def datetime(self) -> str:
        return self.__datetime

    @datetime.setter
    def datetime(self, datetime: str):
        self.__datetime = datetime

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def cite1(self) -> str:
        return self.__cite1

    @cite1.setter
    def cite1(self, cite1: str):
        self.__cite1 = cite1

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
    def xhtml_DelType87(self):
        return self.__xhtml_DelType87

    @xhtml_DelType87.setter
    def xhtml_DelType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType87", None)
        self.__xhtml_DelType87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block86"):
                opp_val = getattr(old_value, "xhtml_Block86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block86"):
                opp_val = getattr(value, "xhtml_Block86", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType522(self):
        return self.__xhtml_DelType522

    @xhtml_DelType522.setter
    def xhtml_DelType522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType522", None)
        self.__xhtml_DelType522 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline521"):
                opp_val = getattr(old_value, "xhtml_Inline521", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline521"):
                opp_val = getattr(value, "xhtml_Inline521", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline521", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType731(self):
        return self.__xhtml_DelType731

    @xhtml_DelType731.setter
    def xhtml_DelType731(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType731", None)
        self.__xhtml_DelType731 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent730"):
                opp_val = getattr(old_value, "xhtml_PreContent730", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent730"):
                opp_val = getattr(value, "xhtml_PreContent730", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent730", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType439(self):
        return self.__xhtml_DelType439

    @xhtml_DelType439.setter
    def xhtml_DelType439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType439", None)
        self.__xhtml_DelType439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent438"):
                opp_val = getattr(old_value, "xhtml_FormContent438", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent438"):
                opp_val = getattr(value, "xhtml_FormContent438", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent438", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType386(self):
        return self.__xhtml_DelType386

    @xhtml_DelType386.setter
    def xhtml_DelType386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType386", None)
        self.__xhtml_DelType386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow385"):
                opp_val = getattr(old_value, "xhtml_Flow385", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow385"):
                opp_val = getattr(value, "xhtml_Flow385", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow385", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType141(self):
        return self.__xhtml_DelType141

    @xhtml_DelType141.setter
    def xhtml_DelType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType141", None)
        self.__xhtml_DelType141 = value
        
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

    @property
    def xhtml_DelType654(self):
        return self.__xhtml_DelType654

    @xhtml_DelType654.setter
    def xhtml_DelType654(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType654", None)
        self.__xhtml_DelType654 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType653"):
                opp_val = getattr(old_value, "xhtml_ObjectType653", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType653"):
                opp_val = getattr(value, "xhtml_ObjectType653", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType653", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DelType(self):
        return self.__xhtml_DelType

    @xhtml_DelType.setter
    def xhtml_DelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DelType__xhtml_DelType", None)
        self.__xhtml_DelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent50"):
                opp_val = getattr(old_value, "xhtml_AContent50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent50"):
                opp_val = getattr(value, "xhtml_AContent50", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AContent:

    pass
class xhtml_AType(AContent):

    def __init__(self, charset: str, class: str, rev: str, shape: str, style: str, title: str, type: str, coords: str, href: str, hreflang: str, id: str, name: str, rel: str, xhtml_AType: "xhtml_DocumentRoot" = None, xhtml_AType308: "xhtml_Flow" = None, xhtml_AType444: "xhtml_Inline" = None, xhtml_AType576: "xhtml_ObjectType" = None, xhtml_AType659: "xhtml_PreContent" = None):
        self.charset = charset
        self.class = class
        self.rev = rev
        self.shape = shape
        self.style = style
        self.title = title
        self.type = type
        self.coords = coords
        self.href = href
        self.hreflang = hreflang
        self.id = id
        self.name = name
        self.rel = rel
        self.xhtml_AType = xhtml_AType
        self.xhtml_AType308 = xhtml_AType308
        self.xhtml_AType444 = xhtml_AType444
        self.xhtml_AType576 = xhtml_AType576
        self.xhtml_AType659 = xhtml_AType659
        
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
    def coords(self) -> str:
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords

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
    def charset(self) -> str:
        return self.__charset

    @charset.setter
    def charset(self, charset: str):
        self.__charset = charset

    @property
    def hreflang(self) -> str:
        return self.__hreflang

    @hreflang.setter
    def hreflang(self, hreflang: str):
        self.__hreflang = hreflang

    @property
    def rel(self) -> str:
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def xhtml_AType444(self):
        return self.__xhtml_AType444

    @xhtml_AType444.setter
    def xhtml_AType444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType444", None)
        self.__xhtml_AType444 = value
        
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
    def xhtml_AType576(self):
        return self.__xhtml_AType576

    @xhtml_AType576.setter
    def xhtml_AType576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType576", None)
        self.__xhtml_AType576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType575"):
                opp_val = getattr(old_value, "xhtml_ObjectType575", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType575"):
                opp_val = getattr(value, "xhtml_ObjectType575", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType575", set([self]))
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
            if hasattr(old_value, "xhtml_DocumentRoot98"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot98"):
                opp_val = getattr(value, "xhtml_DocumentRoot98", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AType308(self):
        return self.__xhtml_AType308

    @xhtml_AType308.setter
    def xhtml_AType308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType308", None)
        self.__xhtml_AType308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow307"):
                opp_val = getattr(old_value, "xhtml_Flow307", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow307"):
                opp_val = getattr(value, "xhtml_Flow307", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow307", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AType659(self):
        return self.__xhtml_AType659

    @xhtml_AType659.setter
    def xhtml_AType659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AType__xhtml_AType659", None)
        self.__xhtml_AType659 = value
        
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

class xhtml_InsType(Flow):

    def __init__(self, cite1: str, class: str, datetime: str, id: str, style: str, title: str, xhtml_InsType: "xhtml_AContent" = None, xhtml_InsType84: "xhtml_Block" = None, xhtml_InsType188: "xhtml_DocumentRoot" = None, xhtml_InsType383: "xhtml_Flow" = None, xhtml_InsType436: "xhtml_FormContent" = None, xhtml_InsType519: "xhtml_Inline" = None, xhtml_InsType651: "xhtml_ObjectType" = None, xhtml_InsType728: "xhtml_PreContent" = None):
        self.cite1 = cite1
        self.class = class
        self.datetime = datetime
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_InsType = xhtml_InsType
        self.xhtml_InsType84 = xhtml_InsType84
        self.xhtml_InsType188 = xhtml_InsType188
        self.xhtml_InsType383 = xhtml_InsType383
        self.xhtml_InsType436 = xhtml_InsType436
        self.xhtml_InsType519 = xhtml_InsType519
        self.xhtml_InsType651 = xhtml_InsType651
        self.xhtml_InsType728 = xhtml_InsType728
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def datetime(self) -> str:
        return self.__datetime

    @datetime.setter
    def datetime(self, datetime: str):
        self.__datetime = datetime

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
    def xhtml_InsType436(self):
        return self.__xhtml_InsType436

    @xhtml_InsType436.setter
    def xhtml_InsType436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType436", None)
        self.__xhtml_InsType436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent435"):
                opp_val = getattr(old_value, "xhtml_FormContent435", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent435"):
                opp_val = getattr(value, "xhtml_FormContent435", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent435", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType651(self):
        return self.__xhtml_InsType651

    @xhtml_InsType651.setter
    def xhtml_InsType651(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType651", None)
        self.__xhtml_InsType651 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType650"):
                opp_val = getattr(old_value, "xhtml_ObjectType650", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType650"):
                opp_val = getattr(value, "xhtml_ObjectType650", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType650", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType519(self):
        return self.__xhtml_InsType519

    @xhtml_InsType519.setter
    def xhtml_InsType519(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType519", None)
        self.__xhtml_InsType519 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline518"):
                opp_val = getattr(old_value, "xhtml_Inline518", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline518"):
                opp_val = getattr(value, "xhtml_Inline518", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline518", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType(self):
        return self.__xhtml_InsType

    @xhtml_InsType.setter
    def xhtml_InsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType", None)
        self.__xhtml_InsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent48"):
                opp_val = getattr(old_value, "xhtml_AContent48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent48"):
                opp_val = getattr(value, "xhtml_AContent48", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType728(self):
        return self.__xhtml_InsType728

    @xhtml_InsType728.setter
    def xhtml_InsType728(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType728", None)
        self.__xhtml_InsType728 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent727"):
                opp_val = getattr(old_value, "xhtml_PreContent727", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent727"):
                opp_val = getattr(value, "xhtml_PreContent727", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent727", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType383(self):
        return self.__xhtml_InsType383

    @xhtml_InsType383.setter
    def xhtml_InsType383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType383", None)
        self.__xhtml_InsType383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow382"):
                opp_val = getattr(old_value, "xhtml_Flow382", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow382"):
                opp_val = getattr(value, "xhtml_Flow382", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow382", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType84(self):
        return self.__xhtml_InsType84

    @xhtml_InsType84.setter
    def xhtml_InsType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType84", None)
        self.__xhtml_InsType84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block83"):
                opp_val = getattr(old_value, "xhtml_Block83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block83"):
                opp_val = getattr(value, "xhtml_Block83", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_InsType188(self):
        return self.__xhtml_InsType188

    @xhtml_InsType188.setter
    def xhtml_InsType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_InsType__xhtml_InsType188", None)
        self.__xhtml_InsType188 = value
        
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

class xhtml_BrType:

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_BrType: "xhtml_AContent" = None, xhtml_BrType121: "xhtml_DocumentRoot" = None, xhtml_BrType311: "xhtml_Flow" = None, xhtml_BrType447: "xhtml_Inline" = None, xhtml_BrType579: "xhtml_ObjectType" = None, xhtml_BrType722: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BrType = xhtml_BrType
        self.xhtml_BrType121 = xhtml_BrType121
        self.xhtml_BrType311 = xhtml_BrType311
        self.xhtml_BrType447 = xhtml_BrType447
        self.xhtml_BrType579 = xhtml_BrType579
        self.xhtml_BrType722 = xhtml_BrType722
        
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
    def xhtml_BrType579(self):
        return self.__xhtml_BrType579

    @xhtml_BrType579.setter
    def xhtml_BrType579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType579", None)
        self.__xhtml_BrType579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType578"):
                opp_val = getattr(old_value, "xhtml_ObjectType578", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType578"):
                opp_val = getattr(value, "xhtml_ObjectType578", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType578", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType311(self):
        return self.__xhtml_BrType311

    @xhtml_BrType311.setter
    def xhtml_BrType311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType311", None)
        self.__xhtml_BrType311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow310"):
                opp_val = getattr(old_value, "xhtml_Flow310", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow310"):
                opp_val = getattr(value, "xhtml_Flow310", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow310", set([self]))
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

    @property
    def xhtml_BrType722(self):
        return self.__xhtml_BrType722

    @xhtml_BrType722.setter
    def xhtml_BrType722(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType722", None)
        self.__xhtml_BrType722 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent721"):
                opp_val = getattr(old_value, "xhtml_PreContent721", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent721"):
                opp_val = getattr(value, "xhtml_PreContent721", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent721", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType447(self):
        return self.__xhtml_BrType447

    @xhtml_BrType447.setter
    def xhtml_BrType447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType447", None)
        self.__xhtml_BrType447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline446"):
                opp_val = getattr(old_value, "xhtml_Inline446", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline446"):
                opp_val = getattr(value, "xhtml_Inline446", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline446", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BrType121(self):
        return self.__xhtml_BrType121

    @xhtml_BrType121.setter
    def xhtml_BrType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BrType__xhtml_BrType121", None)
        self.__xhtml_BrType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot120"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot120"):
                opp_val = getattr(value, "xhtml_DocumentRoot120", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ImgType:

    def __init__(self, alt: str, class: str, height: str, id: str, ismap: str, longdesc: str, src: str, style: str, title: str, usemap: str, width: str, xhtml_ImgType: "xhtml_AContent" = None, xhtml_ImgType185: "xhtml_DocumentRoot" = None, xhtml_ImgType320: "xhtml_Flow" = None, xhtml_ImgType456: "xhtml_Inline" = None, xhtml_ImgType588: "xhtml_ObjectType" = None):
        self.alt = alt
        self.class = class
        self.height = height
        self.id = id
        self.ismap = ismap
        self.longdesc = longdesc
        self.src = src
        self.style = style
        self.title = title
        self.usemap = usemap
        self.width = width
        self.xhtml_ImgType = xhtml_ImgType
        self.xhtml_ImgType185 = xhtml_ImgType185
        self.xhtml_ImgType320 = xhtml_ImgType320
        self.xhtml_ImgType456 = xhtml_ImgType456
        self.xhtml_ImgType588 = xhtml_ImgType588
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def usemap(self) -> str:
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap

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
    def longdesc(self) -> str:
        return self.__longdesc

    @longdesc.setter
    def longdesc(self, longdesc: str):
        self.__longdesc = longdesc

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
    def xhtml_ImgType456(self):
        return self.__xhtml_ImgType456

    @xhtml_ImgType456.setter
    def xhtml_ImgType456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType456", None)
        self.__xhtml_ImgType456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline455"):
                opp_val = getattr(old_value, "xhtml_Inline455", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline455"):
                opp_val = getattr(value, "xhtml_Inline455", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline455", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ImgType320(self):
        return self.__xhtml_ImgType320

    @xhtml_ImgType320.setter
    def xhtml_ImgType320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType320", None)
        self.__xhtml_ImgType320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow319"):
                opp_val = getattr(old_value, "xhtml_Flow319", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow319"):
                opp_val = getattr(value, "xhtml_Flow319", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow319", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ImgType185(self):
        return self.__xhtml_ImgType185

    @xhtml_ImgType185.setter
    def xhtml_ImgType185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType185", None)
        self.__xhtml_ImgType185 = value
        
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
    def xhtml_ImgType588(self):
        return self.__xhtml_ImgType588

    @xhtml_ImgType588.setter
    def xhtml_ImgType588(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ImgType__xhtml_ImgType588", None)
        self.__xhtml_ImgType588 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType587"):
                opp_val = getattr(old_value, "xhtml_ObjectType587", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType587"):
                opp_val = getattr(value, "xhtml_ObjectType587", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType587", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_ObjectType:

    def __init__(self, mixed: str, group: str, archive: str, class: str, classid: str, codebase: str, codetype: str, data: str, id: str, name: str, standby: str, style: str, tabindex: str, title: str, type: str, usemap: str, width: str, declare: str, height: str, xhtml_ObjectType: "xhtml_AContent" = None, xhtml_ObjectType196: "xhtml_DocumentRoot" = None, xhtml_ObjectType317: "xhtml_Flow" = None, xhtml_ObjectType453: "xhtml_Inline" = None, xhtml_ObjectType524: set["xhtml_ParamType"] = None, xhtml_ObjectType527: set["xhtml_PType"] = None, xhtml_ObjectType530: set["xhtml_H1Type"] = None, xhtml_ObjectType533: set["xhtml_H2Type"] = None, xhtml_ObjectType536: set["xhtml_H3Type"] = None, xhtml_ObjectType539: set["xhtml_H4Type"] = None, xhtml_ObjectType542: set["xhtml_H5Type"] = None, xhtml_ObjectType545: set["xhtml_H6Type"] = None, xhtml_ObjectType548: set["xhtml_DivType"] = None, xhtml_ObjectType551: set["xhtml_UlType"] = None, xhtml_ObjectType554: set["xhtml_OlType"] = None, xhtml_ObjectType557: set["xhtml_DlType"] = None, xhtml_ObjectType560: set["xhtml_PreType"] = None, xhtml_ObjectType563: set["xhtml_HrType"] = None, xhtml_ObjectType566: set["xhtml_BlockquoteType"] = None, xhtml_ObjectType569: set["xhtml_AddressType"] = None, xhtml_ObjectType572: set["xhtml_TableType"] = None, xhtml_ObjectType575: set["xhtml_AType"] = None, xhtml_ObjectType578: set["xhtml_BrType"] = None, xhtml_ObjectType581: set["xhtml_SpanType"] = None, xhtml_ObjectType585: "xhtml_ObjectType" = None, xhtml_ObjectType583: set["xhtml_ObjectType"] = None, xhtml_ObjectType587: set["xhtml_ImgType"] = None, xhtml_ObjectType590: set["xhtml_TtType"] = None, xhtml_ObjectType593: set["xhtml_IType"] = None, xhtml_ObjectType596: set["xhtml_BType"] = None, xhtml_ObjectType599: set["xhtml_BigType"] = None, xhtml_ObjectType602: set["xhtml_SmallType"] = None, xhtml_ObjectType605: set["xhtml_UType"] = None, xhtml_ObjectType608: set["xhtml_StrikeType"] = None, xhtml_ObjectType611: set["xhtml_EmType"] = None, xhtml_ObjectType614: set["xhtml_StrongType"] = None, xhtml_ObjectType617: set["xhtml_DfnType"] = None, xhtml_ObjectType620: set["xhtml_CodeType"] = None, xhtml_ObjectType623: set["xhtml_QType"] = None, xhtml_ObjectType626: set["xhtml_SampType"] = None, xhtml_ObjectType629: set["xhtml_KbdType"] = None, xhtml_ObjectType632: set["xhtml_VarType"] = None, xhtml_ObjectType635: set["xhtml_CiteType"] = None, xhtml_ObjectType638: set["xhtml_AbbrType"] = None, xhtml_ObjectType641: set["xhtml_AcronymType"] = None, xhtml_ObjectType644: set["xhtml_SubType"] = None, xhtml_ObjectType647: set["xhtml_SupType"] = None, xhtml_ObjectType650: set["xhtml_InsType"] = None, xhtml_ObjectType653: set["xhtml_DelType"] = None):
        self.mixed = mixed
        self.group = group
        self.archive = archive
        self.class = class
        self.classid = classid
        self.codebase = codebase
        self.codetype = codetype
        self.data = data
        self.id = id
        self.name = name
        self.standby = standby
        self.style = style
        self.tabindex = tabindex
        self.title = title
        self.type = type
        self.usemap = usemap
        self.width = width
        self.declare = declare
        self.height = height
        self.xhtml_ObjectType = xhtml_ObjectType
        self.xhtml_ObjectType196 = xhtml_ObjectType196
        self.xhtml_ObjectType317 = xhtml_ObjectType317
        self.xhtml_ObjectType453 = xhtml_ObjectType453
        self.xhtml_ObjectType524 = xhtml_ObjectType524 if xhtml_ObjectType524 is not None else set()
        self.xhtml_ObjectType527 = xhtml_ObjectType527 if xhtml_ObjectType527 is not None else set()
        self.xhtml_ObjectType530 = xhtml_ObjectType530 if xhtml_ObjectType530 is not None else set()
        self.xhtml_ObjectType533 = xhtml_ObjectType533 if xhtml_ObjectType533 is not None else set()
        self.xhtml_ObjectType536 = xhtml_ObjectType536 if xhtml_ObjectType536 is not None else set()
        self.xhtml_ObjectType539 = xhtml_ObjectType539 if xhtml_ObjectType539 is not None else set()
        self.xhtml_ObjectType542 = xhtml_ObjectType542 if xhtml_ObjectType542 is not None else set()
        self.xhtml_ObjectType545 = xhtml_ObjectType545 if xhtml_ObjectType545 is not None else set()
        self.xhtml_ObjectType548 = xhtml_ObjectType548 if xhtml_ObjectType548 is not None else set()
        self.xhtml_ObjectType551 = xhtml_ObjectType551 if xhtml_ObjectType551 is not None else set()
        self.xhtml_ObjectType554 = xhtml_ObjectType554 if xhtml_ObjectType554 is not None else set()
        self.xhtml_ObjectType557 = xhtml_ObjectType557 if xhtml_ObjectType557 is not None else set()
        self.xhtml_ObjectType560 = xhtml_ObjectType560 if xhtml_ObjectType560 is not None else set()
        self.xhtml_ObjectType563 = xhtml_ObjectType563 if xhtml_ObjectType563 is not None else set()
        self.xhtml_ObjectType566 = xhtml_ObjectType566 if xhtml_ObjectType566 is not None else set()
        self.xhtml_ObjectType569 = xhtml_ObjectType569 if xhtml_ObjectType569 is not None else set()
        self.xhtml_ObjectType572 = xhtml_ObjectType572 if xhtml_ObjectType572 is not None else set()
        self.xhtml_ObjectType575 = xhtml_ObjectType575 if xhtml_ObjectType575 is not None else set()
        self.xhtml_ObjectType578 = xhtml_ObjectType578 if xhtml_ObjectType578 is not None else set()
        self.xhtml_ObjectType581 = xhtml_ObjectType581 if xhtml_ObjectType581 is not None else set()
        self.xhtml_ObjectType585 = xhtml_ObjectType585
        self.xhtml_ObjectType583 = xhtml_ObjectType583 if xhtml_ObjectType583 is not None else set()
        self.xhtml_ObjectType587 = xhtml_ObjectType587 if xhtml_ObjectType587 is not None else set()
        self.xhtml_ObjectType590 = xhtml_ObjectType590 if xhtml_ObjectType590 is not None else set()
        self.xhtml_ObjectType593 = xhtml_ObjectType593 if xhtml_ObjectType593 is not None else set()
        self.xhtml_ObjectType596 = xhtml_ObjectType596 if xhtml_ObjectType596 is not None else set()
        self.xhtml_ObjectType599 = xhtml_ObjectType599 if xhtml_ObjectType599 is not None else set()
        self.xhtml_ObjectType602 = xhtml_ObjectType602 if xhtml_ObjectType602 is not None else set()
        self.xhtml_ObjectType605 = xhtml_ObjectType605 if xhtml_ObjectType605 is not None else set()
        self.xhtml_ObjectType608 = xhtml_ObjectType608 if xhtml_ObjectType608 is not None else set()
        self.xhtml_ObjectType611 = xhtml_ObjectType611 if xhtml_ObjectType611 is not None else set()
        self.xhtml_ObjectType614 = xhtml_ObjectType614 if xhtml_ObjectType614 is not None else set()
        self.xhtml_ObjectType617 = xhtml_ObjectType617 if xhtml_ObjectType617 is not None else set()
        self.xhtml_ObjectType620 = xhtml_ObjectType620 if xhtml_ObjectType620 is not None else set()
        self.xhtml_ObjectType623 = xhtml_ObjectType623 if xhtml_ObjectType623 is not None else set()
        self.xhtml_ObjectType626 = xhtml_ObjectType626 if xhtml_ObjectType626 is not None else set()
        self.xhtml_ObjectType629 = xhtml_ObjectType629 if xhtml_ObjectType629 is not None else set()
        self.xhtml_ObjectType632 = xhtml_ObjectType632 if xhtml_ObjectType632 is not None else set()
        self.xhtml_ObjectType635 = xhtml_ObjectType635 if xhtml_ObjectType635 is not None else set()
        self.xhtml_ObjectType638 = xhtml_ObjectType638 if xhtml_ObjectType638 is not None else set()
        self.xhtml_ObjectType641 = xhtml_ObjectType641 if xhtml_ObjectType641 is not None else set()
        self.xhtml_ObjectType644 = xhtml_ObjectType644 if xhtml_ObjectType644 is not None else set()
        self.xhtml_ObjectType647 = xhtml_ObjectType647 if xhtml_ObjectType647 is not None else set()
        self.xhtml_ObjectType650 = xhtml_ObjectType650 if xhtml_ObjectType650 is not None else set()
        self.xhtml_ObjectType653 = xhtml_ObjectType653 if xhtml_ObjectType653 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def usemap(self) -> str:
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

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
    def declare(self) -> str:
        return self.__declare

    @declare.setter
    def declare(self, declare: str):
        self.__declare = declare

    @property
    def archive(self) -> str:
        return self.__archive

    @archive.setter
    def archive(self, archive: str):
        self.__archive = archive

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def classid(self) -> str:
        return self.__classid

    @classid.setter
    def classid(self, classid: str):
        self.__classid = classid

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
    def tabindex(self) -> str:
        return self.__tabindex

    @tabindex.setter
    def tabindex(self, tabindex: str):
        self.__tabindex = tabindex

    @property
    def codetype(self) -> str:
        return self.__codetype

    @codetype.setter
    def codetype(self, codetype: str):
        self.__codetype = codetype

    @property
    def codebase(self) -> str:
        return self.__codebase

    @codebase.setter
    def codebase(self, codebase: str):
        self.__codebase = codebase

    @property
    def standby(self) -> str:
        return self.__standby

    @standby.setter
    def standby(self, standby: str):
        self.__standby = standby

    @property
    def xhtml_ObjectType453(self):
        return self.__xhtml_ObjectType453

    @xhtml_ObjectType453.setter
    def xhtml_ObjectType453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType453", None)
        self.__xhtml_ObjectType453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline452"):
                opp_val = getattr(old_value, "xhtml_Inline452", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline452"):
                opp_val = getattr(value, "xhtml_Inline452", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline452", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ObjectType575(self):
        return self.__xhtml_ObjectType575

    @xhtml_ObjectType575.setter
    def xhtml_ObjectType575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType575", None)
        self.__xhtml_ObjectType575 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AType576"):
                    opp_val = getattr(item, "xhtml_AType576", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AType576", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AType576"):
                    opp_val = getattr(item, "xhtml_AType576", None)
                    
                    setattr(item, "xhtml_AType576", self)
                    

    @property
    def xhtml_ObjectType585(self):
        return self.__xhtml_ObjectType585

    @xhtml_ObjectType585.setter
    def xhtml_ObjectType585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType585", None)
        self.__xhtml_ObjectType585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType583"):
                opp_val = getattr(old_value, "xhtml_ObjectType583", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType583"):
                opp_val = getattr(value, "xhtml_ObjectType583", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType583", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ObjectType569(self):
        return self.__xhtml_ObjectType569

    @xhtml_ObjectType569.setter
    def xhtml_ObjectType569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType569", None)
        self.__xhtml_ObjectType569 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AddressType570"):
                    opp_val = getattr(item, "xhtml_AddressType570", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AddressType570", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AddressType570"):
                    opp_val = getattr(item, "xhtml_AddressType570", None)
                    
                    setattr(item, "xhtml_AddressType570", self)
                    

    @property
    def xhtml_ObjectType563(self):
        return self.__xhtml_ObjectType563

    @xhtml_ObjectType563.setter
    def xhtml_ObjectType563(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType563", None)
        self.__xhtml_ObjectType563 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_HrType564"):
                    opp_val = getattr(item, "xhtml_HrType564", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_HrType564", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_HrType564"):
                    opp_val = getattr(item, "xhtml_HrType564", None)
                    
                    setattr(item, "xhtml_HrType564", self)
                    

    @property
    def xhtml_ObjectType605(self):
        return self.__xhtml_ObjectType605

    @xhtml_ObjectType605.setter
    def xhtml_ObjectType605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType605", None)
        self.__xhtml_ObjectType605 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UType606"):
                    opp_val = getattr(item, "xhtml_UType606", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType606", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType606"):
                    opp_val = getattr(item, "xhtml_UType606", None)
                    
                    setattr(item, "xhtml_UType606", self)
                    

    @property
    def xhtml_ObjectType635(self):
        return self.__xhtml_ObjectType635

    @xhtml_ObjectType635.setter
    def xhtml_ObjectType635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType635", None)
        self.__xhtml_ObjectType635 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CiteType636"):
                    opp_val = getattr(item, "xhtml_CiteType636", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CiteType636", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CiteType636"):
                    opp_val = getattr(item, "xhtml_CiteType636", None)
                    
                    setattr(item, "xhtml_CiteType636", self)
                    

    @property
    def xhtml_ObjectType647(self):
        return self.__xhtml_ObjectType647

    @xhtml_ObjectType647.setter
    def xhtml_ObjectType647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType647", None)
        self.__xhtml_ObjectType647 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SupType648"):
                    opp_val = getattr(item, "xhtml_SupType648", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SupType648", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SupType648"):
                    opp_val = getattr(item, "xhtml_SupType648", None)
                    
                    setattr(item, "xhtml_SupType648", self)
                    

    @property
    def xhtml_ObjectType614(self):
        return self.__xhtml_ObjectType614

    @xhtml_ObjectType614.setter
    def xhtml_ObjectType614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType614", None)
        self.__xhtml_ObjectType614 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrongType615"):
                    opp_val = getattr(item, "xhtml_StrongType615", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrongType615", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrongType615"):
                    opp_val = getattr(item, "xhtml_StrongType615", None)
                    
                    setattr(item, "xhtml_StrongType615", self)
                    

    @property
    def xhtml_ObjectType554(self):
        return self.__xhtml_ObjectType554

    @xhtml_ObjectType554.setter
    def xhtml_ObjectType554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType554", None)
        self.__xhtml_ObjectType554 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_OlType555"):
                    opp_val = getattr(item, "xhtml_OlType555", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_OlType555", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_OlType555"):
                    opp_val = getattr(item, "xhtml_OlType555", None)
                    
                    setattr(item, "xhtml_OlType555", self)
                    

    @property
    def xhtml_ObjectType593(self):
        return self.__xhtml_ObjectType593

    @xhtml_ObjectType593.setter
    def xhtml_ObjectType593(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType593", None)
        self.__xhtml_ObjectType593 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_IType594"):
                    opp_val = getattr(item, "xhtml_IType594", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_IType594", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_IType594"):
                    opp_val = getattr(item, "xhtml_IType594", None)
                    
                    setattr(item, "xhtml_IType594", self)
                    

    @property
    def xhtml_ObjectType653(self):
        return self.__xhtml_ObjectType653

    @xhtml_ObjectType653.setter
    def xhtml_ObjectType653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType653", None)
        self.__xhtml_ObjectType653 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType654"):
                    opp_val = getattr(item, "xhtml_DelType654", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType654", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType654"):
                    opp_val = getattr(item, "xhtml_DelType654", None)
                    
                    setattr(item, "xhtml_DelType654", self)
                    

    @property
    def xhtml_ObjectType545(self):
        return self.__xhtml_ObjectType545

    @xhtml_ObjectType545.setter
    def xhtml_ObjectType545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType545", None)
        self.__xhtml_ObjectType545 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H6Type546"):
                    opp_val = getattr(item, "xhtml_H6Type546", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H6Type546", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H6Type546"):
                    opp_val = getattr(item, "xhtml_H6Type546", None)
                    
                    setattr(item, "xhtml_H6Type546", self)
                    

    @property
    def xhtml_ObjectType632(self):
        return self.__xhtml_ObjectType632

    @xhtml_ObjectType632.setter
    def xhtml_ObjectType632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType632", None)
        self.__xhtml_ObjectType632 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_VarType633"):
                    opp_val = getattr(item, "xhtml_VarType633", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_VarType633", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_VarType633"):
                    opp_val = getattr(item, "xhtml_VarType633", None)
                    
                    setattr(item, "xhtml_VarType633", self)
                    

    @property
    def xhtml_ObjectType599(self):
        return self.__xhtml_ObjectType599

    @xhtml_ObjectType599.setter
    def xhtml_ObjectType599(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType599", None)
        self.__xhtml_ObjectType599 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BigType600"):
                    opp_val = getattr(item, "xhtml_BigType600", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BigType600", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BigType600"):
                    opp_val = getattr(item, "xhtml_BigType600", None)
                    
                    setattr(item, "xhtml_BigType600", self)
                    

    @property
    def xhtml_ObjectType638(self):
        return self.__xhtml_ObjectType638

    @xhtml_ObjectType638.setter
    def xhtml_ObjectType638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType638", None)
        self.__xhtml_ObjectType638 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AbbrType639"):
                    opp_val = getattr(item, "xhtml_AbbrType639", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AbbrType639", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AbbrType639"):
                    opp_val = getattr(item, "xhtml_AbbrType639", None)
                    
                    setattr(item, "xhtml_AbbrType639", self)
                    

    @property
    def xhtml_ObjectType524(self):
        return self.__xhtml_ObjectType524

    @xhtml_ObjectType524.setter
    def xhtml_ObjectType524(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType524", None)
        self.__xhtml_ObjectType524 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ParamType525"):
                    opp_val = getattr(item, "xhtml_ParamType525", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ParamType525", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ParamType525"):
                    opp_val = getattr(item, "xhtml_ParamType525", None)
                    
                    setattr(item, "xhtml_ParamType525", self)
                    

    @property
    def xhtml_ObjectType608(self):
        return self.__xhtml_ObjectType608

    @xhtml_ObjectType608.setter
    def xhtml_ObjectType608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType608", None)
        self.__xhtml_ObjectType608 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_StrikeType609"):
                    opp_val = getattr(item, "xhtml_StrikeType609", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType609", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType609"):
                    opp_val = getattr(item, "xhtml_StrikeType609", None)
                    
                    setattr(item, "xhtml_StrikeType609", self)
                    

    @property
    def xhtml_ObjectType539(self):
        return self.__xhtml_ObjectType539

    @xhtml_ObjectType539.setter
    def xhtml_ObjectType539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType539", None)
        self.__xhtml_ObjectType539 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H4Type540"):
                    opp_val = getattr(item, "xhtml_H4Type540", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H4Type540", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H4Type540"):
                    opp_val = getattr(item, "xhtml_H4Type540", None)
                    
                    setattr(item, "xhtml_H4Type540", self)
                    

    @property
    def xhtml_ObjectType590(self):
        return self.__xhtml_ObjectType590

    @xhtml_ObjectType590.setter
    def xhtml_ObjectType590(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType590", None)
        self.__xhtml_ObjectType590 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TtType591"):
                    opp_val = getattr(item, "xhtml_TtType591", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TtType591", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TtType591"):
                    opp_val = getattr(item, "xhtml_TtType591", None)
                    
                    setattr(item, "xhtml_TtType591", self)
                    

    @property
    def xhtml_ObjectType317(self):
        return self.__xhtml_ObjectType317

    @xhtml_ObjectType317.setter
    def xhtml_ObjectType317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType317", None)
        self.__xhtml_ObjectType317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow316"):
                opp_val = getattr(old_value, "xhtml_Flow316", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow316"):
                opp_val = getattr(value, "xhtml_Flow316", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow316", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ObjectType560(self):
        return self.__xhtml_ObjectType560

    @xhtml_ObjectType560.setter
    def xhtml_ObjectType560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType560", None)
        self.__xhtml_ObjectType560 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PreType561"):
                    opp_val = getattr(item, "xhtml_PreType561", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PreType561", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PreType561"):
                    opp_val = getattr(item, "xhtml_PreType561", None)
                    
                    setattr(item, "xhtml_PreType561", self)
                    

    @property
    def xhtml_ObjectType527(self):
        return self.__xhtml_ObjectType527

    @xhtml_ObjectType527.setter
    def xhtml_ObjectType527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType527", None)
        self.__xhtml_ObjectType527 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_PType528"):
                    opp_val = getattr(item, "xhtml_PType528", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_PType528", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_PType528"):
                    opp_val = getattr(item, "xhtml_PType528", None)
                    
                    setattr(item, "xhtml_PType528", self)
                    

    @property
    def xhtml_ObjectType644(self):
        return self.__xhtml_ObjectType644

    @xhtml_ObjectType644.setter
    def xhtml_ObjectType644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType644", None)
        self.__xhtml_ObjectType644 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SubType645"):
                    opp_val = getattr(item, "xhtml_SubType645", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SubType645", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SubType645"):
                    opp_val = getattr(item, "xhtml_SubType645", None)
                    
                    setattr(item, "xhtml_SubType645", self)
                    

    @property
    def xhtml_ObjectType551(self):
        return self.__xhtml_ObjectType551

    @xhtml_ObjectType551.setter
    def xhtml_ObjectType551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType551", None)
        self.__xhtml_ObjectType551 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_UlType552"):
                    opp_val = getattr(item, "xhtml_UlType552", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UlType552", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UlType552"):
                    opp_val = getattr(item, "xhtml_UlType552", None)
                    
                    setattr(item, "xhtml_UlType552", self)
                    

    @property
    def xhtml_ObjectType530(self):
        return self.__xhtml_ObjectType530

    @xhtml_ObjectType530.setter
    def xhtml_ObjectType530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType530", None)
        self.__xhtml_ObjectType530 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H1Type531"):
                    opp_val = getattr(item, "xhtml_H1Type531", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H1Type531", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H1Type531"):
                    opp_val = getattr(item, "xhtml_H1Type531", None)
                    
                    setattr(item, "xhtml_H1Type531", self)
                    

    @property
    def xhtml_ObjectType557(self):
        return self.__xhtml_ObjectType557

    @xhtml_ObjectType557.setter
    def xhtml_ObjectType557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType557", None)
        self.__xhtml_ObjectType557 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DlType558"):
                    opp_val = getattr(item, "xhtml_DlType558", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DlType558", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DlType558"):
                    opp_val = getattr(item, "xhtml_DlType558", None)
                    
                    setattr(item, "xhtml_DlType558", self)
                    

    @property
    def xhtml_ObjectType620(self):
        return self.__xhtml_ObjectType620

    @xhtml_ObjectType620.setter
    def xhtml_ObjectType620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType620", None)
        self.__xhtml_ObjectType620 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_CodeType621"):
                    opp_val = getattr(item, "xhtml_CodeType621", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_CodeType621", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_CodeType621"):
                    opp_val = getattr(item, "xhtml_CodeType621", None)
                    
                    setattr(item, "xhtml_CodeType621", self)
                    

    @property
    def xhtml_ObjectType596(self):
        return self.__xhtml_ObjectType596

    @xhtml_ObjectType596.setter
    def xhtml_ObjectType596(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType596", None)
        self.__xhtml_ObjectType596 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BType597"):
                    opp_val = getattr(item, "xhtml_BType597", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BType597", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BType597"):
                    opp_val = getattr(item, "xhtml_BType597", None)
                    
                    setattr(item, "xhtml_BType597", self)
                    

    @property
    def xhtml_ObjectType623(self):
        return self.__xhtml_ObjectType623

    @xhtml_ObjectType623.setter
    def xhtml_ObjectType623(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType623", None)
        self.__xhtml_ObjectType623 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_QType624"):
                    opp_val = getattr(item, "xhtml_QType624", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_QType624", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_QType624"):
                    opp_val = getattr(item, "xhtml_QType624", None)
                    
                    setattr(item, "xhtml_QType624", self)
                    

    @property
    def xhtml_ObjectType536(self):
        return self.__xhtml_ObjectType536

    @xhtml_ObjectType536.setter
    def xhtml_ObjectType536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType536", None)
        self.__xhtml_ObjectType536 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H3Type537"):
                    opp_val = getattr(item, "xhtml_H3Type537", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H3Type537", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H3Type537"):
                    opp_val = getattr(item, "xhtml_H3Type537", None)
                    
                    setattr(item, "xhtml_H3Type537", self)
                    

    @property
    def xhtml_ObjectType566(self):
        return self.__xhtml_ObjectType566

    @xhtml_ObjectType566.setter
    def xhtml_ObjectType566(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType566", None)
        self.__xhtml_ObjectType566 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BlockquoteType567"):
                    opp_val = getattr(item, "xhtml_BlockquoteType567", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BlockquoteType567", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BlockquoteType567"):
                    opp_val = getattr(item, "xhtml_BlockquoteType567", None)
                    
                    setattr(item, "xhtml_BlockquoteType567", self)
                    

    @property
    def xhtml_ObjectType617(self):
        return self.__xhtml_ObjectType617

    @xhtml_ObjectType617.setter
    def xhtml_ObjectType617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType617", None)
        self.__xhtml_ObjectType617 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DfnType618"):
                    opp_val = getattr(item, "xhtml_DfnType618", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DfnType618", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DfnType618"):
                    opp_val = getattr(item, "xhtml_DfnType618", None)
                    
                    setattr(item, "xhtml_DfnType618", self)
                    

    @property
    def xhtml_ObjectType(self):
        return self.__xhtml_ObjectType

    @xhtml_ObjectType.setter
    def xhtml_ObjectType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType", None)
        self.__xhtml_ObjectType = value
        
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
    def xhtml_ObjectType583(self):
        return self.__xhtml_ObjectType583

    @xhtml_ObjectType583.setter
    def xhtml_ObjectType583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType583", None)
        self.__xhtml_ObjectType583 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ObjectType585"):
                    opp_val = getattr(item, "xhtml_ObjectType585", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ObjectType585", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ObjectType585"):
                    opp_val = getattr(item, "xhtml_ObjectType585", None)
                    
                    setattr(item, "xhtml_ObjectType585", self)
                    

    @property
    def xhtml_ObjectType611(self):
        return self.__xhtml_ObjectType611

    @xhtml_ObjectType611.setter
    def xhtml_ObjectType611(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType611", None)
        self.__xhtml_ObjectType611 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_EmType612"):
                    opp_val = getattr(item, "xhtml_EmType612", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_EmType612", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_EmType612"):
                    opp_val = getattr(item, "xhtml_EmType612", None)
                    
                    setattr(item, "xhtml_EmType612", self)
                    

    @property
    def xhtml_ObjectType542(self):
        return self.__xhtml_ObjectType542

    @xhtml_ObjectType542.setter
    def xhtml_ObjectType542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType542", None)
        self.__xhtml_ObjectType542 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H5Type543"):
                    opp_val = getattr(item, "xhtml_H5Type543", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H5Type543", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H5Type543"):
                    opp_val = getattr(item, "xhtml_H5Type543", None)
                    
                    setattr(item, "xhtml_H5Type543", self)
                    

    @property
    def xhtml_ObjectType533(self):
        return self.__xhtml_ObjectType533

    @xhtml_ObjectType533.setter
    def xhtml_ObjectType533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType533", None)
        self.__xhtml_ObjectType533 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_H2Type534"):
                    opp_val = getattr(item, "xhtml_H2Type534", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_H2Type534", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_H2Type534"):
                    opp_val = getattr(item, "xhtml_H2Type534", None)
                    
                    setattr(item, "xhtml_H2Type534", self)
                    

    @property
    def xhtml_ObjectType629(self):
        return self.__xhtml_ObjectType629

    @xhtml_ObjectType629.setter
    def xhtml_ObjectType629(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType629", None)
        self.__xhtml_ObjectType629 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_KbdType630"):
                    opp_val = getattr(item, "xhtml_KbdType630", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_KbdType630", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_KbdType630"):
                    opp_val = getattr(item, "xhtml_KbdType630", None)
                    
                    setattr(item, "xhtml_KbdType630", self)
                    

    @property
    def xhtml_ObjectType650(self):
        return self.__xhtml_ObjectType650

    @xhtml_ObjectType650.setter
    def xhtml_ObjectType650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType650", None)
        self.__xhtml_ObjectType650 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType651"):
                    opp_val = getattr(item, "xhtml_InsType651", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType651", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType651"):
                    opp_val = getattr(item, "xhtml_InsType651", None)
                    
                    setattr(item, "xhtml_InsType651", self)
                    

    @property
    def xhtml_ObjectType587(self):
        return self.__xhtml_ObjectType587

    @xhtml_ObjectType587.setter
    def xhtml_ObjectType587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType587", None)
        self.__xhtml_ObjectType587 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_ImgType588"):
                    opp_val = getattr(item, "xhtml_ImgType588", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ImgType588", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ImgType588"):
                    opp_val = getattr(item, "xhtml_ImgType588", None)
                    
                    setattr(item, "xhtml_ImgType588", self)
                    

    @property
    def xhtml_ObjectType641(self):
        return self.__xhtml_ObjectType641

    @xhtml_ObjectType641.setter
    def xhtml_ObjectType641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType641", None)
        self.__xhtml_ObjectType641 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_AcronymType642"):
                    opp_val = getattr(item, "xhtml_AcronymType642", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_AcronymType642", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_AcronymType642"):
                    opp_val = getattr(item, "xhtml_AcronymType642", None)
                    
                    setattr(item, "xhtml_AcronymType642", self)
                    

    @property
    def xhtml_ObjectType602(self):
        return self.__xhtml_ObjectType602

    @xhtml_ObjectType602.setter
    def xhtml_ObjectType602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType602", None)
        self.__xhtml_ObjectType602 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SmallType603"):
                    opp_val = getattr(item, "xhtml_SmallType603", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SmallType603", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SmallType603"):
                    opp_val = getattr(item, "xhtml_SmallType603", None)
                    
                    setattr(item, "xhtml_SmallType603", self)
                    

    @property
    def xhtml_ObjectType196(self):
        return self.__xhtml_ObjectType196

    @xhtml_ObjectType196.setter
    def xhtml_ObjectType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType196", None)
        self.__xhtml_ObjectType196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot195"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot195"):
                opp_val = getattr(value, "xhtml_DocumentRoot195", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_ObjectType548(self):
        return self.__xhtml_ObjectType548

    @xhtml_ObjectType548.setter
    def xhtml_ObjectType548(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType548", None)
        self.__xhtml_ObjectType548 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DivType549"):
                    opp_val = getattr(item, "xhtml_DivType549", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DivType549", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DivType549"):
                    opp_val = getattr(item, "xhtml_DivType549", None)
                    
                    setattr(item, "xhtml_DivType549", self)
                    

    @property
    def xhtml_ObjectType581(self):
        return self.__xhtml_ObjectType581

    @xhtml_ObjectType581.setter
    def xhtml_ObjectType581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType581", None)
        self.__xhtml_ObjectType581 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SpanType582"):
                    opp_val = getattr(item, "xhtml_SpanType582", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SpanType582", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SpanType582"):
                    opp_val = getattr(item, "xhtml_SpanType582", None)
                    
                    setattr(item, "xhtml_SpanType582", self)
                    

    @property
    def xhtml_ObjectType578(self):
        return self.__xhtml_ObjectType578

    @xhtml_ObjectType578.setter
    def xhtml_ObjectType578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType578", None)
        self.__xhtml_ObjectType578 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_BrType579"):
                    opp_val = getattr(item, "xhtml_BrType579", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_BrType579", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_BrType579"):
                    opp_val = getattr(item, "xhtml_BrType579", None)
                    
                    setattr(item, "xhtml_BrType579", self)
                    

    @property
    def xhtml_ObjectType572(self):
        return self.__xhtml_ObjectType572

    @xhtml_ObjectType572.setter
    def xhtml_ObjectType572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType572", None)
        self.__xhtml_ObjectType572 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_TableType573"):
                    opp_val = getattr(item, "xhtml_TableType573", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_TableType573", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_TableType573"):
                    opp_val = getattr(item, "xhtml_TableType573", None)
                    
                    setattr(item, "xhtml_TableType573", self)
                    

    @property
    def xhtml_ObjectType626(self):
        return self.__xhtml_ObjectType626

    @xhtml_ObjectType626.setter
    def xhtml_ObjectType626(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_ObjectType__xhtml_ObjectType626", None)
        self.__xhtml_ObjectType626 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_SampType627"):
                    opp_val = getattr(item, "xhtml_SampType627", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_SampType627", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_SampType627"):
                    opp_val = getattr(item, "xhtml_SampType627", None)
                    
                    setattr(item, "xhtml_SampType627", self)
                    

class xhtml_AContent:

    def __init__(self, mixed: str, group: str, xhtml_AContent4: set["xhtml_ObjectType"] = None, xhtml_AContent6: set["xhtml_ImgType"] = None, xhtml_AContent8: set["xhtml_TtType"] = None, xhtml_AContent10: set["xhtml_IType"] = None, xhtml_AContent12: set["xhtml_BType"] = None, xhtml_AContent14: set["xhtml_BigType"] = None, xhtml_AContent: set["xhtml_BrType"] = None, xhtml_AContent2: set["xhtml_SpanType"] = None, xhtml_AContent22: set["xhtml_EmType"] = None, xhtml_AContent24: set["xhtml_StrongType"] = None, xhtml_AContent26: set["xhtml_DfnType"] = None, xhtml_AContent28: set["xhtml_CodeType"] = None, xhtml_AContent30: set["xhtml_QType"] = None, xhtml_AContent16: set["xhtml_SmallType"] = None, xhtml_AContent18: set["xhtml_UType"] = None, xhtml_AContent20: set["xhtml_StrikeType"] = None, xhtml_AContent38: set["xhtml_CiteType"] = None, xhtml_AContent40: set["xhtml_AbbrType"] = None, xhtml_AContent42: set["xhtml_AcronymType"] = None, xhtml_AContent44: set["xhtml_SubType"] = None, xhtml_AContent46: set["xhtml_SupType"] = None, xhtml_AContent48: set["xhtml_InsType"] = None, xhtml_AContent32: set["xhtml_SampType"] = None, xhtml_AContent34: set["xhtml_KbdType"] = None, xhtml_AContent36: set["xhtml_VarType"] = None, xhtml_AContent50: set["xhtml_DelType"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_AContent4 = xhtml_AContent4 if xhtml_AContent4 is not None else set()
        self.xhtml_AContent6 = xhtml_AContent6 if xhtml_AContent6 is not None else set()
        self.xhtml_AContent8 = xhtml_AContent8 if xhtml_AContent8 is not None else set()
        self.xhtml_AContent10 = xhtml_AContent10 if xhtml_AContent10 is not None else set()
        self.xhtml_AContent12 = xhtml_AContent12 if xhtml_AContent12 is not None else set()
        self.xhtml_AContent14 = xhtml_AContent14 if xhtml_AContent14 is not None else set()
        self.xhtml_AContent = xhtml_AContent if xhtml_AContent is not None else set()
        self.xhtml_AContent2 = xhtml_AContent2 if xhtml_AContent2 is not None else set()
        self.xhtml_AContent22 = xhtml_AContent22 if xhtml_AContent22 is not None else set()
        self.xhtml_AContent24 = xhtml_AContent24 if xhtml_AContent24 is not None else set()
        self.xhtml_AContent26 = xhtml_AContent26 if xhtml_AContent26 is not None else set()
        self.xhtml_AContent28 = xhtml_AContent28 if xhtml_AContent28 is not None else set()
        self.xhtml_AContent30 = xhtml_AContent30 if xhtml_AContent30 is not None else set()
        self.xhtml_AContent16 = xhtml_AContent16 if xhtml_AContent16 is not None else set()
        self.xhtml_AContent18 = xhtml_AContent18 if xhtml_AContent18 is not None else set()
        self.xhtml_AContent20 = xhtml_AContent20 if xhtml_AContent20 is not None else set()
        self.xhtml_AContent38 = xhtml_AContent38 if xhtml_AContent38 is not None else set()
        self.xhtml_AContent40 = xhtml_AContent40 if xhtml_AContent40 is not None else set()
        self.xhtml_AContent42 = xhtml_AContent42 if xhtml_AContent42 is not None else set()
        self.xhtml_AContent44 = xhtml_AContent44 if xhtml_AContent44 is not None else set()
        self.xhtml_AContent46 = xhtml_AContent46 if xhtml_AContent46 is not None else set()
        self.xhtml_AContent48 = xhtml_AContent48 if xhtml_AContent48 is not None else set()
        self.xhtml_AContent32 = xhtml_AContent32 if xhtml_AContent32 is not None else set()
        self.xhtml_AContent34 = xhtml_AContent34 if xhtml_AContent34 is not None else set()
        self.xhtml_AContent36 = xhtml_AContent36 if xhtml_AContent36 is not None else set()
        self.xhtml_AContent50 = xhtml_AContent50 if xhtml_AContent50 is not None else set()
        
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
    def xhtml_AContent48(self):
        return self.__xhtml_AContent48

    @xhtml_AContent48.setter
    def xhtml_AContent48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent48", None)
        self.__xhtml_AContent48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_InsType"):
                    opp_val = getattr(item, "xhtml_InsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_InsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_InsType"):
                    opp_val = getattr(item, "xhtml_InsType", None)
                    
                    setattr(item, "xhtml_InsType", self)
                    

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
                if hasattr(item, "xhtml_StrikeType"):
                    opp_val = getattr(item, "xhtml_StrikeType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_StrikeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_StrikeType"):
                    opp_val = getattr(item, "xhtml_StrikeType", None)
                    
                    setattr(item, "xhtml_StrikeType", self)
                    

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
    def xhtml_AContent50(self):
        return self.__xhtml_AContent50

    @xhtml_AContent50.setter
    def xhtml_AContent50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent50", None)
        self.__xhtml_AContent50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_DelType"):
                    opp_val = getattr(item, "xhtml_DelType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_DelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_DelType"):
                    opp_val = getattr(item, "xhtml_DelType", None)
                    
                    setattr(item, "xhtml_DelType", self)
                    

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
    def xhtml_AContent46(self):
        return self.__xhtml_AContent46

    @xhtml_AContent46.setter
    def xhtml_AContent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent46", None)
        self.__xhtml_AContent46 = value if value is not None else set()
        
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
                if hasattr(item, "xhtml_UType"):
                    opp_val = getattr(item, "xhtml_UType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_UType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_UType"):
                    opp_val = getattr(item, "xhtml_UType", None)
                    
                    setattr(item, "xhtml_UType", self)
                    

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
                if hasattr(item, "xhtml_ObjectType"):
                    opp_val = getattr(item, "xhtml_ObjectType", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_ObjectType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_ObjectType"):
                    opp_val = getattr(item, "xhtml_ObjectType", None)
                    
                    setattr(item, "xhtml_ObjectType", self)
                    

class Inline:

    pass
class xhtml_BigType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_BigType: "xhtml_AContent" = None, xhtml_BigType113: "xhtml_DocumentRoot" = None, xhtml_BigType332: "xhtml_Flow" = None, xhtml_BigType468: "xhtml_Inline" = None, xhtml_BigType600: "xhtml_ObjectType" = None, xhtml_BigType671: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BigType = xhtml_BigType
        self.xhtml_BigType113 = xhtml_BigType113
        self.xhtml_BigType332 = xhtml_BigType332
        self.xhtml_BigType468 = xhtml_BigType468
        self.xhtml_BigType600 = xhtml_BigType600
        self.xhtml_BigType671 = xhtml_BigType671
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_BigType600(self):
        return self.__xhtml_BigType600

    @xhtml_BigType600.setter
    def xhtml_BigType600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType600", None)
        self.__xhtml_BigType600 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType599"):
                opp_val = getattr(old_value, "xhtml_ObjectType599", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType599"):
                opp_val = getattr(value, "xhtml_ObjectType599", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType599", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def xhtml_BigType332(self):
        return self.__xhtml_BigType332

    @xhtml_BigType332.setter
    def xhtml_BigType332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType332", None)
        self.__xhtml_BigType332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow331"):
                opp_val = getattr(old_value, "xhtml_Flow331", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow331"):
                opp_val = getattr(value, "xhtml_Flow331", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow331", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType468(self):
        return self.__xhtml_BigType468

    @xhtml_BigType468.setter
    def xhtml_BigType468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType468", None)
        self.__xhtml_BigType468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline467"):
                opp_val = getattr(old_value, "xhtml_Inline467", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline467"):
                opp_val = getattr(value, "xhtml_Inline467", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline467", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType671(self):
        return self.__xhtml_BigType671

    @xhtml_BigType671.setter
    def xhtml_BigType671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType671", None)
        self.__xhtml_BigType671 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent670"):
                opp_val = getattr(old_value, "xhtml_PreContent670", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent670"):
                opp_val = getattr(value, "xhtml_PreContent670", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent670", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BigType113(self):
        return self.__xhtml_BigType113

    @xhtml_BigType113.setter
    def xhtml_BigType113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BigType__xhtml_BigType113", None)
        self.__xhtml_BigType113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot112"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot112"):
                opp_val = getattr(value, "xhtml_DocumentRoot112", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_BType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_BType: "xhtml_AContent" = None, xhtml_BType110: "xhtml_DocumentRoot" = None, xhtml_BType329: "xhtml_Flow" = None, xhtml_BType465: "xhtml_Inline" = None, xhtml_BType597: "xhtml_ObjectType" = None, xhtml_BType668: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_BType = xhtml_BType
        self.xhtml_BType110 = xhtml_BType110
        self.xhtml_BType329 = xhtml_BType329
        self.xhtml_BType465 = xhtml_BType465
        self.xhtml_BType597 = xhtml_BType597
        self.xhtml_BType668 = xhtml_BType668
        
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
    def xhtml_BType465(self):
        return self.__xhtml_BType465

    @xhtml_BType465.setter
    def xhtml_BType465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType465", None)
        self.__xhtml_BType465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline464"):
                opp_val = getattr(old_value, "xhtml_Inline464", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline464"):
                opp_val = getattr(value, "xhtml_Inline464", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline464", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType110(self):
        return self.__xhtml_BType110

    @xhtml_BType110.setter
    def xhtml_BType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType110", None)
        self.__xhtml_BType110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot109"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot109"):
                opp_val = getattr(value, "xhtml_DocumentRoot109", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType668(self):
        return self.__xhtml_BType668

    @xhtml_BType668.setter
    def xhtml_BType668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType668", None)
        self.__xhtml_BType668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent667"):
                opp_val = getattr(old_value, "xhtml_PreContent667", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent667"):
                opp_val = getattr(value, "xhtml_PreContent667", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent667", set([self]))
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

    @property
    def xhtml_BType329(self):
        return self.__xhtml_BType329

    @xhtml_BType329.setter
    def xhtml_BType329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType329", None)
        self.__xhtml_BType329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow328"):
                opp_val = getattr(old_value, "xhtml_Flow328", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow328"):
                opp_val = getattr(value, "xhtml_Flow328", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow328", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_BType597(self):
        return self.__xhtml_BType597

    @xhtml_BType597.setter
    def xhtml_BType597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_BType__xhtml_BType597", None)
        self.__xhtml_BType597 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType596"):
                opp_val = getattr(old_value, "xhtml_ObjectType596", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType596"):
                opp_val = getattr(value, "xhtml_ObjectType596", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType596", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AcronymType(Inline):

    def __init__(self, id: str, style: str, title: str, class: str, xhtml_AcronymType: "xhtml_AContent" = None, xhtml_AcronymType104: "xhtml_DocumentRoot" = None, xhtml_AcronymType374: "xhtml_Flow" = None, xhtml_AcronymType510: "xhtml_Inline" = None, xhtml_AcronymType642: "xhtml_ObjectType" = None, xhtml_AcronymType713: "xhtml_PreContent" = None):
        self.id = id
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_AcronymType = xhtml_AcronymType
        self.xhtml_AcronymType104 = xhtml_AcronymType104
        self.xhtml_AcronymType374 = xhtml_AcronymType374
        self.xhtml_AcronymType510 = xhtml_AcronymType510
        self.xhtml_AcronymType642 = xhtml_AcronymType642
        self.xhtml_AcronymType713 = xhtml_AcronymType713
        
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
    def xhtml_AcronymType374(self):
        return self.__xhtml_AcronymType374

    @xhtml_AcronymType374.setter
    def xhtml_AcronymType374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType374", None)
        self.__xhtml_AcronymType374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow373"):
                opp_val = getattr(old_value, "xhtml_Flow373", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow373"):
                opp_val = getattr(value, "xhtml_Flow373", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow373", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType642(self):
        return self.__xhtml_AcronymType642

    @xhtml_AcronymType642.setter
    def xhtml_AcronymType642(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType642", None)
        self.__xhtml_AcronymType642 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType641"):
                opp_val = getattr(old_value, "xhtml_ObjectType641", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType641"):
                opp_val = getattr(value, "xhtml_ObjectType641", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType641", set([self]))
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
    def xhtml_AcronymType510(self):
        return self.__xhtml_AcronymType510

    @xhtml_AcronymType510.setter
    def xhtml_AcronymType510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType510", None)
        self.__xhtml_AcronymType510 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline509"):
                opp_val = getattr(old_value, "xhtml_Inline509", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline509"):
                opp_val = getattr(value, "xhtml_Inline509", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline509", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType104(self):
        return self.__xhtml_AcronymType104

    @xhtml_AcronymType104.setter
    def xhtml_AcronymType104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType104", None)
        self.__xhtml_AcronymType104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot103"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot103"):
                opp_val = getattr(value, "xhtml_DocumentRoot103", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AcronymType713(self):
        return self.__xhtml_AcronymType713

    @xhtml_AcronymType713.setter
    def xhtml_AcronymType713(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AcronymType__xhtml_AcronymType713", None)
        self.__xhtml_AcronymType713 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent712"):
                opp_val = getattr(old_value, "xhtml_PreContent712", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent712"):
                opp_val = getattr(value, "xhtml_PreContent712", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent712", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H1Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H1Type: "xhtml_Block" = None, xhtml_H1Type159: "xhtml_DocumentRoot" = None, xhtml_H1Type263: "xhtml_Flow" = None, xhtml_H1Type391: "xhtml_FormContent" = None, xhtml_H1Type531: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H1Type = xhtml_H1Type
        self.xhtml_H1Type159 = xhtml_H1Type159
        self.xhtml_H1Type263 = xhtml_H1Type263
        self.xhtml_H1Type391 = xhtml_H1Type391
        self.xhtml_H1Type531 = xhtml_H1Type531
        
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
    def xhtml_H1Type159(self):
        return self.__xhtml_H1Type159

    @xhtml_H1Type159.setter
    def xhtml_H1Type159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type159", None)
        self.__xhtml_H1Type159 = value
        
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

    @property
    def xhtml_H1Type391(self):
        return self.__xhtml_H1Type391

    @xhtml_H1Type391.setter
    def xhtml_H1Type391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type391", None)
        self.__xhtml_H1Type391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent390"):
                opp_val = getattr(old_value, "xhtml_FormContent390", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent390"):
                opp_val = getattr(value, "xhtml_FormContent390", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent390", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def xhtml_H1Type531(self):
        return self.__xhtml_H1Type531

    @xhtml_H1Type531.setter
    def xhtml_H1Type531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type531", None)
        self.__xhtml_H1Type531 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType530"):
                opp_val = getattr(old_value, "xhtml_ObjectType530", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType530"):
                opp_val = getattr(value, "xhtml_ObjectType530", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType530", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H1Type263(self):
        return self.__xhtml_H1Type263

    @xhtml_H1Type263.setter
    def xhtml_H1Type263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H1Type__xhtml_H1Type263", None)
        self.__xhtml_H1Type263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow262"):
                opp_val = getattr(old_value, "xhtml_Flow262", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow262"):
                opp_val = getattr(value, "xhtml_Flow262", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow262", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_TtType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_TtType: "xhtml_AContent" = None, xhtml_TtType249: "xhtml_DocumentRoot" = None, xhtml_TtType323: "xhtml_Flow" = None, xhtml_TtType459: "xhtml_Inline" = None, xhtml_TtType591: "xhtml_ObjectType" = None, xhtml_TtType662: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_TtType = xhtml_TtType
        self.xhtml_TtType249 = xhtml_TtType249
        self.xhtml_TtType323 = xhtml_TtType323
        self.xhtml_TtType459 = xhtml_TtType459
        self.xhtml_TtType591 = xhtml_TtType591
        self.xhtml_TtType662 = xhtml_TtType662
        
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
    def xhtml_TtType459(self):
        return self.__xhtml_TtType459

    @xhtml_TtType459.setter
    def xhtml_TtType459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType459", None)
        self.__xhtml_TtType459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline458"):
                opp_val = getattr(old_value, "xhtml_Inline458", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline458"):
                opp_val = getattr(value, "xhtml_Inline458", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline458", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType323(self):
        return self.__xhtml_TtType323

    @xhtml_TtType323.setter
    def xhtml_TtType323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType323", None)
        self.__xhtml_TtType323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow322"):
                opp_val = getattr(old_value, "xhtml_Flow322", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow322"):
                opp_val = getattr(value, "xhtml_Flow322", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow322", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType249(self):
        return self.__xhtml_TtType249

    @xhtml_TtType249.setter
    def xhtml_TtType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType249", None)
        self.__xhtml_TtType249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot248"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot248"):
                opp_val = getattr(value, "xhtml_DocumentRoot248", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_TtType662(self):
        return self.__xhtml_TtType662

    @xhtml_TtType662.setter
    def xhtml_TtType662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType662", None)
        self.__xhtml_TtType662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent661"):
                opp_val = getattr(old_value, "xhtml_PreContent661", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent661"):
                opp_val = getattr(value, "xhtml_PreContent661", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent661", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def xhtml_TtType591(self):
        return self.__xhtml_TtType591

    @xhtml_TtType591.setter
    def xhtml_TtType591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_TtType__xhtml_TtType591", None)
        self.__xhtml_TtType591 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType590"):
                opp_val = getattr(old_value, "xhtml_ObjectType590", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType590"):
                opp_val = getattr(value, "xhtml_ObjectType590", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType590", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_EmType(Inline):

    def __init__(self, id: str, style: str, title: str, class: str, xhtml_EmType: "xhtml_AContent" = None, xhtml_EmType156: "xhtml_DocumentRoot" = None, xhtml_EmType344: "xhtml_Flow" = None, xhtml_EmType480: "xhtml_Inline" = None, xhtml_EmType612: "xhtml_ObjectType" = None, xhtml_EmType683: "xhtml_PreContent" = None):
        self.id = id
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_EmType = xhtml_EmType
        self.xhtml_EmType156 = xhtml_EmType156
        self.xhtml_EmType344 = xhtml_EmType344
        self.xhtml_EmType480 = xhtml_EmType480
        self.xhtml_EmType612 = xhtml_EmType612
        self.xhtml_EmType683 = xhtml_EmType683
        
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
    def xhtml_EmType683(self):
        return self.__xhtml_EmType683

    @xhtml_EmType683.setter
    def xhtml_EmType683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType683", None)
        self.__xhtml_EmType683 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent682"):
                opp_val = getattr(old_value, "xhtml_PreContent682", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent682"):
                opp_val = getattr(value, "xhtml_PreContent682", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent682", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType344(self):
        return self.__xhtml_EmType344

    @xhtml_EmType344.setter
    def xhtml_EmType344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType344", None)
        self.__xhtml_EmType344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow343"):
                opp_val = getattr(old_value, "xhtml_Flow343", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow343"):
                opp_val = getattr(value, "xhtml_Flow343", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow343", set([self]))
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
    def xhtml_EmType612(self):
        return self.__xhtml_EmType612

    @xhtml_EmType612.setter
    def xhtml_EmType612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType612", None)
        self.__xhtml_EmType612 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType611"):
                opp_val = getattr(old_value, "xhtml_ObjectType611", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType611"):
                opp_val = getattr(value, "xhtml_ObjectType611", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType611", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_EmType156(self):
        return self.__xhtml_EmType156

    @xhtml_EmType156.setter
    def xhtml_EmType156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType156", None)
        self.__xhtml_EmType156 = value
        
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
    def xhtml_EmType480(self):
        return self.__xhtml_EmType480

    @xhtml_EmType480.setter
    def xhtml_EmType480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_EmType__xhtml_EmType480", None)
        self.__xhtml_EmType480 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline479"):
                opp_val = getattr(old_value, "xhtml_Inline479", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline479"):
                opp_val = getattr(value, "xhtml_Inline479", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline479", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DtType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_DtType: "xhtml_DlType" = None, xhtml_DtType153: "xhtml_DocumentRoot" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_DtType = xhtml_DtType
        self.xhtml_DtType153 = xhtml_DtType153
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_DtType153(self):
        return self.__xhtml_DtType153

    @xhtml_DtType153.setter
    def xhtml_DtType153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DtType__xhtml_DtType153", None)
        self.__xhtml_DtType153 = value
        
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
    def xhtml_DtType(self):
        return self.__xhtml_DtType

    @xhtml_DtType.setter
    def xhtml_DtType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DtType__xhtml_DtType", None)
        self.__xhtml_DtType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DlType90"):
                opp_val = getattr(old_value, "xhtml_DlType90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DlType90"):
                opp_val = getattr(value, "xhtml_DlType90", None)
                if opp_val is None:
                    setattr(value, "xhtml_DlType90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_QType(Inline):

    def __init__(self, cite1: str, class: str, id: str, style: str, title: str, xhtml_QType: "xhtml_AContent" = None, xhtml_QType210: "xhtml_DocumentRoot" = None, xhtml_QType356: "xhtml_Flow" = None, xhtml_QType492: "xhtml_Inline" = None, xhtml_QType624: "xhtml_ObjectType" = None, xhtml_QType695: "xhtml_PreContent" = None):
        self.cite1 = cite1
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_QType = xhtml_QType
        self.xhtml_QType210 = xhtml_QType210
        self.xhtml_QType356 = xhtml_QType356
        self.xhtml_QType492 = xhtml_QType492
        self.xhtml_QType624 = xhtml_QType624
        self.xhtml_QType695 = xhtml_QType695
        
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
    def xhtml_QType695(self):
        return self.__xhtml_QType695

    @xhtml_QType695.setter
    def xhtml_QType695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType695", None)
        self.__xhtml_QType695 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent694"):
                opp_val = getattr(old_value, "xhtml_PreContent694", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent694"):
                opp_val = getattr(value, "xhtml_PreContent694", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent694", set([self]))
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
    def xhtml_QType210(self):
        return self.__xhtml_QType210

    @xhtml_QType210.setter
    def xhtml_QType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType210", None)
        self.__xhtml_QType210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot209"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot209"):
                opp_val = getattr(value, "xhtml_DocumentRoot209", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType624(self):
        return self.__xhtml_QType624

    @xhtml_QType624.setter
    def xhtml_QType624(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType624", None)
        self.__xhtml_QType624 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType623"):
                opp_val = getattr(old_value, "xhtml_ObjectType623", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType623"):
                opp_val = getattr(value, "xhtml_ObjectType623", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType623", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType492(self):
        return self.__xhtml_QType492

    @xhtml_QType492.setter
    def xhtml_QType492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType492", None)
        self.__xhtml_QType492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline491"):
                opp_val = getattr(old_value, "xhtml_Inline491", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline491"):
                opp_val = getattr(value, "xhtml_Inline491", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline491", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_QType356(self):
        return self.__xhtml_QType356

    @xhtml_QType356.setter
    def xhtml_QType356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_QType__xhtml_QType356", None)
        self.__xhtml_QType356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow355"):
                opp_val = getattr(old_value, "xhtml_Flow355", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow355"):
                opp_val = getattr(value, "xhtml_Flow355", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow355", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_KbdType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_KbdType: "xhtml_AContent" = None, xhtml_KbdType191: "xhtml_DocumentRoot" = None, xhtml_KbdType362: "xhtml_Flow" = None, xhtml_KbdType498: "xhtml_Inline" = None, xhtml_KbdType630: "xhtml_ObjectType" = None, xhtml_KbdType701: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_KbdType = xhtml_KbdType
        self.xhtml_KbdType191 = xhtml_KbdType191
        self.xhtml_KbdType362 = xhtml_KbdType362
        self.xhtml_KbdType498 = xhtml_KbdType498
        self.xhtml_KbdType630 = xhtml_KbdType630
        self.xhtml_KbdType701 = xhtml_KbdType701
        
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
    def xhtml_KbdType362(self):
        return self.__xhtml_KbdType362

    @xhtml_KbdType362.setter
    def xhtml_KbdType362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType362", None)
        self.__xhtml_KbdType362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow361"):
                opp_val = getattr(old_value, "xhtml_Flow361", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow361"):
                opp_val = getattr(value, "xhtml_Flow361", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow361", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType191(self):
        return self.__xhtml_KbdType191

    @xhtml_KbdType191.setter
    def xhtml_KbdType191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType191", None)
        self.__xhtml_KbdType191 = value
        
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
    def xhtml_KbdType498(self):
        return self.__xhtml_KbdType498

    @xhtml_KbdType498.setter
    def xhtml_KbdType498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType498", None)
        self.__xhtml_KbdType498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline497"):
                opp_val = getattr(old_value, "xhtml_Inline497", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline497"):
                opp_val = getattr(value, "xhtml_Inline497", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline497", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_KbdType630(self):
        return self.__xhtml_KbdType630

    @xhtml_KbdType630.setter
    def xhtml_KbdType630(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType630", None)
        self.__xhtml_KbdType630 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType629"):
                opp_val = getattr(old_value, "xhtml_ObjectType629", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType629"):
                opp_val = getattr(value, "xhtml_ObjectType629", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType629", set([self]))
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
    def xhtml_KbdType701(self):
        return self.__xhtml_KbdType701

    @xhtml_KbdType701.setter
    def xhtml_KbdType701(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_KbdType__xhtml_KbdType701", None)
        self.__xhtml_KbdType701 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent700"):
                opp_val = getattr(old_value, "xhtml_PreContent700", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent700"):
                opp_val = getattr(value, "xhtml_PreContent700", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent700", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CaptionType(Inline):

    def __init__(self, title: str, class: str, id: str, style: str, xhtml_CaptionType: "xhtml_DocumentRoot" = None, xhtml_CaptionType734: "xhtml_TableType" = None):
        self.title = title
        self.class = class
        self.id = id
        self.style = style
        self.xhtml_CaptionType = xhtml_CaptionType
        self.xhtml_CaptionType734 = xhtml_CaptionType734
        
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
    def xhtml_CaptionType734(self):
        return self.__xhtml_CaptionType734

    @xhtml_CaptionType734.setter
    def xhtml_CaptionType734(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CaptionType__xhtml_CaptionType734", None)
        self.__xhtml_CaptionType734 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_TableType733"):
                opp_val = getattr(old_value, "xhtml_TableType733", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_TableType733", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_TableType733"):
                opp_val = getattr(value, "xhtml_TableType733", None)
                setattr(value, "xhtml_TableType733", self)

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
            if hasattr(old_value, "xhtml_DocumentRoot123"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot123"):
                opp_val = getattr(value, "xhtml_DocumentRoot123", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H5Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H5Type: "xhtml_Block" = None, xhtml_H5Type171: "xhtml_DocumentRoot" = None, xhtml_H5Type275: "xhtml_Flow" = None, xhtml_H5Type403: "xhtml_FormContent" = None, xhtml_H5Type543: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H5Type = xhtml_H5Type
        self.xhtml_H5Type171 = xhtml_H5Type171
        self.xhtml_H5Type275 = xhtml_H5Type275
        self.xhtml_H5Type403 = xhtml_H5Type403
        self.xhtml_H5Type543 = xhtml_H5Type543
        
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
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_H5Type543(self):
        return self.__xhtml_H5Type543

    @xhtml_H5Type543.setter
    def xhtml_H5Type543(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type543", None)
        self.__xhtml_H5Type543 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType542"):
                opp_val = getattr(old_value, "xhtml_ObjectType542", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType542"):
                opp_val = getattr(value, "xhtml_ObjectType542", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType542", set([self]))
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
    def xhtml_H5Type403(self):
        return self.__xhtml_H5Type403

    @xhtml_H5Type403.setter
    def xhtml_H5Type403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type403", None)
        self.__xhtml_H5Type403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent402"):
                opp_val = getattr(old_value, "xhtml_FormContent402", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent402"):
                opp_val = getattr(value, "xhtml_FormContent402", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent402", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H5Type171(self):
        return self.__xhtml_H5Type171

    @xhtml_H5Type171.setter
    def xhtml_H5Type171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type171", None)
        self.__xhtml_H5Type171 = value
        
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
    def xhtml_H5Type275(self):
        return self.__xhtml_H5Type275

    @xhtml_H5Type275.setter
    def xhtml_H5Type275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H5Type__xhtml_H5Type275", None)
        self.__xhtml_H5Type275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow274"):
                opp_val = getattr(old_value, "xhtml_Flow274", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow274"):
                opp_val = getattr(value, "xhtml_Flow274", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow274", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SupType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_SupType: "xhtml_AContent" = None, xhtml_SupType231: "xhtml_DocumentRoot" = None, xhtml_SupType380: "xhtml_Flow" = None, xhtml_SupType516: "xhtml_Inline" = None, xhtml_SupType648: "xhtml_ObjectType" = None, xhtml_SupType719: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_SupType = xhtml_SupType
        self.xhtml_SupType231 = xhtml_SupType231
        self.xhtml_SupType380 = xhtml_SupType380
        self.xhtml_SupType516 = xhtml_SupType516
        self.xhtml_SupType648 = xhtml_SupType648
        self.xhtml_SupType719 = xhtml_SupType719
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_SupType231(self):
        return self.__xhtml_SupType231

    @xhtml_SupType231.setter
    def xhtml_SupType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType231", None)
        self.__xhtml_SupType231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot230"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot230"):
                opp_val = getattr(value, "xhtml_DocumentRoot230", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType719(self):
        return self.__xhtml_SupType719

    @xhtml_SupType719.setter
    def xhtml_SupType719(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType719", None)
        self.__xhtml_SupType719 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent718"):
                opp_val = getattr(old_value, "xhtml_PreContent718", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent718"):
                opp_val = getattr(value, "xhtml_PreContent718", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent718", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType516(self):
        return self.__xhtml_SupType516

    @xhtml_SupType516.setter
    def xhtml_SupType516(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType516", None)
        self.__xhtml_SupType516 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline515"):
                opp_val = getattr(old_value, "xhtml_Inline515", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline515"):
                opp_val = getattr(value, "xhtml_Inline515", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline515", set([self]))
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
            if hasattr(old_value, "xhtml_AContent46"):
                opp_val = getattr(old_value, "xhtml_AContent46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent46"):
                opp_val = getattr(value, "xhtml_AContent46", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType380(self):
        return self.__xhtml_SupType380

    @xhtml_SupType380.setter
    def xhtml_SupType380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType380", None)
        self.__xhtml_SupType380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow379"):
                opp_val = getattr(old_value, "xhtml_Flow379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow379"):
                opp_val = getattr(value, "xhtml_Flow379", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SupType648(self):
        return self.__xhtml_SupType648

    @xhtml_SupType648.setter
    def xhtml_SupType648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SupType__xhtml_SupType648", None)
        self.__xhtml_SupType648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType647"):
                opp_val = getattr(old_value, "xhtml_ObjectType647", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType647"):
                opp_val = getattr(value, "xhtml_ObjectType647", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType647", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_DfnType(Inline):

    def __init__(self, style: str, title: str, class: str, id: str, xhtml_DfnType: "xhtml_AContent" = None, xhtml_DfnType144: "xhtml_DocumentRoot" = None, xhtml_DfnType350: "xhtml_Flow" = None, xhtml_DfnType486: "xhtml_Inline" = None, xhtml_DfnType618: "xhtml_ObjectType" = None, xhtml_DfnType689: "xhtml_PreContent" = None):
        self.style = style
        self.title = title
        self.class = class
        self.id = id
        self.xhtml_DfnType = xhtml_DfnType
        self.xhtml_DfnType144 = xhtml_DfnType144
        self.xhtml_DfnType350 = xhtml_DfnType350
        self.xhtml_DfnType486 = xhtml_DfnType486
        self.xhtml_DfnType618 = xhtml_DfnType618
        self.xhtml_DfnType689 = xhtml_DfnType689
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_DfnType144(self):
        return self.__xhtml_DfnType144

    @xhtml_DfnType144.setter
    def xhtml_DfnType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType144", None)
        self.__xhtml_DfnType144 = value
        
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
    def xhtml_DfnType486(self):
        return self.__xhtml_DfnType486

    @xhtml_DfnType486.setter
    def xhtml_DfnType486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType486", None)
        self.__xhtml_DfnType486 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline485"):
                opp_val = getattr(old_value, "xhtml_Inline485", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline485"):
                opp_val = getattr(value, "xhtml_Inline485", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline485", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType618(self):
        return self.__xhtml_DfnType618

    @xhtml_DfnType618.setter
    def xhtml_DfnType618(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType618", None)
        self.__xhtml_DfnType618 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType617"):
                opp_val = getattr(old_value, "xhtml_ObjectType617", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType617"):
                opp_val = getattr(value, "xhtml_ObjectType617", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType617", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType689(self):
        return self.__xhtml_DfnType689

    @xhtml_DfnType689.setter
    def xhtml_DfnType689(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType689", None)
        self.__xhtml_DfnType689 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent688"):
                opp_val = getattr(old_value, "xhtml_PreContent688", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent688"):
                opp_val = getattr(value, "xhtml_PreContent688", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent688", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_DfnType350(self):
        return self.__xhtml_DfnType350

    @xhtml_DfnType350.setter
    def xhtml_DfnType350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_DfnType__xhtml_DfnType350", None)
        self.__xhtml_DfnType350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow349"):
                opp_val = getattr(old_value, "xhtml_Flow349", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow349"):
                opp_val = getattr(value, "xhtml_Flow349", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow349", set([self]))
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

class xhtml_H4Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H4Type: "xhtml_Block" = None, xhtml_H4Type168: "xhtml_DocumentRoot" = None, xhtml_H4Type272: "xhtml_Flow" = None, xhtml_H4Type400: "xhtml_FormContent" = None, xhtml_H4Type540: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H4Type = xhtml_H4Type
        self.xhtml_H4Type168 = xhtml_H4Type168
        self.xhtml_H4Type272 = xhtml_H4Type272
        self.xhtml_H4Type400 = xhtml_H4Type400
        self.xhtml_H4Type540 = xhtml_H4Type540
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_H4Type540(self):
        return self.__xhtml_H4Type540

    @xhtml_H4Type540.setter
    def xhtml_H4Type540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type540", None)
        self.__xhtml_H4Type540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType539"):
                opp_val = getattr(old_value, "xhtml_ObjectType539", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType539"):
                opp_val = getattr(value, "xhtml_ObjectType539", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType539", set([self]))
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
    def xhtml_H4Type400(self):
        return self.__xhtml_H4Type400

    @xhtml_H4Type400.setter
    def xhtml_H4Type400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type400", None)
        self.__xhtml_H4Type400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent399"):
                opp_val = getattr(old_value, "xhtml_FormContent399", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent399"):
                opp_val = getattr(value, "xhtml_FormContent399", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent399", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H4Type272(self):
        return self.__xhtml_H4Type272

    @xhtml_H4Type272.setter
    def xhtml_H4Type272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type272", None)
        self.__xhtml_H4Type272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow271"):
                opp_val = getattr(old_value, "xhtml_Flow271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow271"):
                opp_val = getattr(value, "xhtml_Flow271", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H4Type168(self):
        return self.__xhtml_H4Type168

    @xhtml_H4Type168.setter
    def xhtml_H4Type168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H4Type__xhtml_H4Type168", None)
        self.__xhtml_H4Type168 = value
        
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

class xhtml_PType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_PType: "xhtml_Block" = None, xhtml_PType202: "xhtml_DocumentRoot" = None, xhtml_PType260: "xhtml_Flow" = None, xhtml_PType388: "xhtml_FormContent" = None, xhtml_PType528: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_PType = xhtml_PType
        self.xhtml_PType202 = xhtml_PType202
        self.xhtml_PType260 = xhtml_PType260
        self.xhtml_PType388 = xhtml_PType388
        self.xhtml_PType528 = xhtml_PType528
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def xhtml_PType388(self):
        return self.__xhtml_PType388

    @xhtml_PType388.setter
    def xhtml_PType388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType388", None)
        self.__xhtml_PType388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent"):
                opp_val = getattr(old_value, "xhtml_FormContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent"):
                opp_val = getattr(value, "xhtml_FormContent", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PType528(self):
        return self.__xhtml_PType528

    @xhtml_PType528.setter
    def xhtml_PType528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType528", None)
        self.__xhtml_PType528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType527"):
                opp_val = getattr(old_value, "xhtml_ObjectType527", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType527"):
                opp_val = getattr(value, "xhtml_ObjectType527", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType527", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_PType260(self):
        return self.__xhtml_PType260

    @xhtml_PType260.setter
    def xhtml_PType260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType260", None)
        self.__xhtml_PType260 = value
        
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
    def xhtml_PType202(self):
        return self.__xhtml_PType202

    @xhtml_PType202.setter
    def xhtml_PType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PType__xhtml_PType202", None)
        self.__xhtml_PType202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot201"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot201"):
                opp_val = getattr(value, "xhtml_DocumentRoot201", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SubType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_SubType: "xhtml_AContent" = None, xhtml_SubType228: "xhtml_DocumentRoot" = None, xhtml_SubType377: "xhtml_Flow" = None, xhtml_SubType513: "xhtml_Inline" = None, xhtml_SubType645: "xhtml_ObjectType" = None, xhtml_SubType716: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_SubType = xhtml_SubType
        self.xhtml_SubType228 = xhtml_SubType228
        self.xhtml_SubType377 = xhtml_SubType377
        self.xhtml_SubType513 = xhtml_SubType513
        self.xhtml_SubType645 = xhtml_SubType645
        self.xhtml_SubType716 = xhtml_SubType716
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_SubType716(self):
        return self.__xhtml_SubType716

    @xhtml_SubType716.setter
    def xhtml_SubType716(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType716", None)
        self.__xhtml_SubType716 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent715"):
                opp_val = getattr(old_value, "xhtml_PreContent715", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent715"):
                opp_val = getattr(value, "xhtml_PreContent715", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent715", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType645(self):
        return self.__xhtml_SubType645

    @xhtml_SubType645.setter
    def xhtml_SubType645(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType645", None)
        self.__xhtml_SubType645 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType644"):
                opp_val = getattr(old_value, "xhtml_ObjectType644", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType644"):
                opp_val = getattr(value, "xhtml_ObjectType644", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType644", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType513(self):
        return self.__xhtml_SubType513

    @xhtml_SubType513.setter
    def xhtml_SubType513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType513", None)
        self.__xhtml_SubType513 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline512"):
                opp_val = getattr(old_value, "xhtml_Inline512", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline512"):
                opp_val = getattr(value, "xhtml_Inline512", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline512", set([self]))
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
    def xhtml_SubType377(self):
        return self.__xhtml_SubType377

    @xhtml_SubType377.setter
    def xhtml_SubType377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType377", None)
        self.__xhtml_SubType377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow376"):
                opp_val = getattr(old_value, "xhtml_Flow376", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow376"):
                opp_val = getattr(value, "xhtml_Flow376", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow376", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SubType228(self):
        return self.__xhtml_SubType228

    @xhtml_SubType228.setter
    def xhtml_SubType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SubType__xhtml_SubType228", None)
        self.__xhtml_SubType228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot227"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot227"):
                opp_val = getattr(value, "xhtml_DocumentRoot227", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CiteType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_CiteType: "xhtml_AContent" = None, xhtml_CiteType126: "xhtml_DocumentRoot" = None, xhtml_CiteType368: "xhtml_Flow" = None, xhtml_CiteType504: "xhtml_Inline" = None, xhtml_CiteType636: "xhtml_ObjectType" = None, xhtml_CiteType707: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_CiteType = xhtml_CiteType
        self.xhtml_CiteType126 = xhtml_CiteType126
        self.xhtml_CiteType368 = xhtml_CiteType368
        self.xhtml_CiteType504 = xhtml_CiteType504
        self.xhtml_CiteType636 = xhtml_CiteType636
        self.xhtml_CiteType707 = xhtml_CiteType707
        
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
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

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

    @property
    def xhtml_CiteType126(self):
        return self.__xhtml_CiteType126

    @xhtml_CiteType126.setter
    def xhtml_CiteType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType126", None)
        self.__xhtml_CiteType126 = value
        
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
    def xhtml_CiteType707(self):
        return self.__xhtml_CiteType707

    @xhtml_CiteType707.setter
    def xhtml_CiteType707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType707", None)
        self.__xhtml_CiteType707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent706"):
                opp_val = getattr(old_value, "xhtml_PreContent706", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent706"):
                opp_val = getattr(value, "xhtml_PreContent706", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent706", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType636(self):
        return self.__xhtml_CiteType636

    @xhtml_CiteType636.setter
    def xhtml_CiteType636(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType636", None)
        self.__xhtml_CiteType636 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType635"):
                opp_val = getattr(old_value, "xhtml_ObjectType635", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType635"):
                opp_val = getattr(value, "xhtml_ObjectType635", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType635", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType368(self):
        return self.__xhtml_CiteType368

    @xhtml_CiteType368.setter
    def xhtml_CiteType368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType368", None)
        self.__xhtml_CiteType368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow367"):
                opp_val = getattr(old_value, "xhtml_Flow367", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow367"):
                opp_val = getattr(value, "xhtml_Flow367", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow367", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CiteType504(self):
        return self.__xhtml_CiteType504

    @xhtml_CiteType504.setter
    def xhtml_CiteType504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CiteType__xhtml_CiteType504", None)
        self.__xhtml_CiteType504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline503"):
                opp_val = getattr(old_value, "xhtml_Inline503", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline503"):
                opp_val = getattr(value, "xhtml_Inline503", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline503", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_StrikeType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_StrikeType: "xhtml_AContent" = None, xhtml_StrikeType222: "xhtml_DocumentRoot" = None, xhtml_StrikeType341: "xhtml_Flow" = None, xhtml_StrikeType477: "xhtml_Inline" = None, xhtml_StrikeType609: "xhtml_ObjectType" = None, xhtml_StrikeType680: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_StrikeType = xhtml_StrikeType
        self.xhtml_StrikeType222 = xhtml_StrikeType222
        self.xhtml_StrikeType341 = xhtml_StrikeType341
        self.xhtml_StrikeType477 = xhtml_StrikeType477
        self.xhtml_StrikeType609 = xhtml_StrikeType609
        self.xhtml_StrikeType680 = xhtml_StrikeType680
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_StrikeType(self):
        return self.__xhtml_StrikeType

    @xhtml_StrikeType.setter
    def xhtml_StrikeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType", None)
        self.__xhtml_StrikeType = value
        
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
    def xhtml_StrikeType609(self):
        return self.__xhtml_StrikeType609

    @xhtml_StrikeType609.setter
    def xhtml_StrikeType609(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType609", None)
        self.__xhtml_StrikeType609 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType608"):
                opp_val = getattr(old_value, "xhtml_ObjectType608", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType608"):
                opp_val = getattr(value, "xhtml_ObjectType608", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType608", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrikeType477(self):
        return self.__xhtml_StrikeType477

    @xhtml_StrikeType477.setter
    def xhtml_StrikeType477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType477", None)
        self.__xhtml_StrikeType477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline476"):
                opp_val = getattr(old_value, "xhtml_Inline476", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline476"):
                opp_val = getattr(value, "xhtml_Inline476", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline476", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrikeType341(self):
        return self.__xhtml_StrikeType341

    @xhtml_StrikeType341.setter
    def xhtml_StrikeType341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType341", None)
        self.__xhtml_StrikeType341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow340"):
                opp_val = getattr(old_value, "xhtml_Flow340", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow340"):
                opp_val = getattr(value, "xhtml_Flow340", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow340", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrikeType680(self):
        return self.__xhtml_StrikeType680

    @xhtml_StrikeType680.setter
    def xhtml_StrikeType680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType680", None)
        self.__xhtml_StrikeType680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent679"):
                opp_val = getattr(old_value, "xhtml_PreContent679", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent679"):
                opp_val = getattr(value, "xhtml_PreContent679", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent679", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrikeType222(self):
        return self.__xhtml_StrikeType222

    @xhtml_StrikeType222.setter
    def xhtml_StrikeType222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrikeType__xhtml_StrikeType222", None)
        self.__xhtml_StrikeType222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot221"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot221"):
                opp_val = getattr(value, "xhtml_DocumentRoot221", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_VarType(Inline):

    def __init__(self, id: str, style: str, title: str, class: str, xhtml_VarType: "xhtml_AContent" = None, xhtml_VarType258: "xhtml_DocumentRoot" = None, xhtml_VarType365: "xhtml_Flow" = None, xhtml_VarType501: "xhtml_Inline" = None, xhtml_VarType633: "xhtml_ObjectType" = None, xhtml_VarType704: "xhtml_PreContent" = None):
        self.id = id
        self.style = style
        self.title = title
        self.class = class
        self.xhtml_VarType = xhtml_VarType
        self.xhtml_VarType258 = xhtml_VarType258
        self.xhtml_VarType365 = xhtml_VarType365
        self.xhtml_VarType501 = xhtml_VarType501
        self.xhtml_VarType633 = xhtml_VarType633
        self.xhtml_VarType704 = xhtml_VarType704
        
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
    def xhtml_VarType258(self):
        return self.__xhtml_VarType258

    @xhtml_VarType258.setter
    def xhtml_VarType258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType258", None)
        self.__xhtml_VarType258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot257"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot257", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot257"):
                opp_val = getattr(value, "xhtml_DocumentRoot257", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot257", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType501(self):
        return self.__xhtml_VarType501

    @xhtml_VarType501.setter
    def xhtml_VarType501(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType501", None)
        self.__xhtml_VarType501 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline500"):
                opp_val = getattr(old_value, "xhtml_Inline500", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline500"):
                opp_val = getattr(value, "xhtml_Inline500", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline500", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType704(self):
        return self.__xhtml_VarType704

    @xhtml_VarType704.setter
    def xhtml_VarType704(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType704", None)
        self.__xhtml_VarType704 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent703"):
                opp_val = getattr(old_value, "xhtml_PreContent703", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent703"):
                opp_val = getattr(value, "xhtml_PreContent703", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent703", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_VarType633(self):
        return self.__xhtml_VarType633

    @xhtml_VarType633.setter
    def xhtml_VarType633(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType633", None)
        self.__xhtml_VarType633 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType632"):
                opp_val = getattr(old_value, "xhtml_ObjectType632", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType632"):
                opp_val = getattr(value, "xhtml_ObjectType632", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType632", set([self]))
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
    def xhtml_VarType365(self):
        return self.__xhtml_VarType365

    @xhtml_VarType365.setter
    def xhtml_VarType365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_VarType__xhtml_VarType365", None)
        self.__xhtml_VarType365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow364"):
                opp_val = getattr(old_value, "xhtml_Flow364", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow364"):
                opp_val = getattr(value, "xhtml_Flow364", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow364", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SampType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_SampType: "xhtml_AContent" = None, xhtml_SampType213: "xhtml_DocumentRoot" = None, xhtml_SampType359: "xhtml_Flow" = None, xhtml_SampType495: "xhtml_Inline" = None, xhtml_SampType627: "xhtml_ObjectType" = None, xhtml_SampType698: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_SampType = xhtml_SampType
        self.xhtml_SampType213 = xhtml_SampType213
        self.xhtml_SampType359 = xhtml_SampType359
        self.xhtml_SampType495 = xhtml_SampType495
        self.xhtml_SampType627 = xhtml_SampType627
        self.xhtml_SampType698 = xhtml_SampType698
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def xhtml_SampType359(self):
        return self.__xhtml_SampType359

    @xhtml_SampType359.setter
    def xhtml_SampType359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType359", None)
        self.__xhtml_SampType359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow358"):
                opp_val = getattr(old_value, "xhtml_Flow358", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow358"):
                opp_val = getattr(value, "xhtml_Flow358", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow358", set([self]))
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
    def xhtml_SampType495(self):
        return self.__xhtml_SampType495

    @xhtml_SampType495.setter
    def xhtml_SampType495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType495", None)
        self.__xhtml_SampType495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline494"):
                opp_val = getattr(old_value, "xhtml_Inline494", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline494"):
                opp_val = getattr(value, "xhtml_Inline494", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline494", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType698(self):
        return self.__xhtml_SampType698

    @xhtml_SampType698.setter
    def xhtml_SampType698(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType698", None)
        self.__xhtml_SampType698 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent697"):
                opp_val = getattr(old_value, "xhtml_PreContent697", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent697"):
                opp_val = getattr(value, "xhtml_PreContent697", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent697", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType213(self):
        return self.__xhtml_SampType213

    @xhtml_SampType213.setter
    def xhtml_SampType213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType213", None)
        self.__xhtml_SampType213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot212"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot212"):
                opp_val = getattr(value, "xhtml_DocumentRoot212", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SampType627(self):
        return self.__xhtml_SampType627

    @xhtml_SampType627.setter
    def xhtml_SampType627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SampType__xhtml_SampType627", None)
        self.__xhtml_SampType627 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType626"):
                opp_val = getattr(old_value, "xhtml_ObjectType626", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType626"):
                opp_val = getattr(value, "xhtml_ObjectType626", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType626", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SmallType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_SmallType: "xhtml_AContent" = None, xhtml_SmallType216: "xhtml_DocumentRoot" = None, xhtml_SmallType335: "xhtml_Flow" = None, xhtml_SmallType471: "xhtml_Inline" = None, xhtml_SmallType603: "xhtml_ObjectType" = None, xhtml_SmallType674: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_SmallType = xhtml_SmallType
        self.xhtml_SmallType216 = xhtml_SmallType216
        self.xhtml_SmallType335 = xhtml_SmallType335
        self.xhtml_SmallType471 = xhtml_SmallType471
        self.xhtml_SmallType603 = xhtml_SmallType603
        self.xhtml_SmallType674 = xhtml_SmallType674
        
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
    def xhtml_SmallType335(self):
        return self.__xhtml_SmallType335

    @xhtml_SmallType335.setter
    def xhtml_SmallType335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType335", None)
        self.__xhtml_SmallType335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow334"):
                opp_val = getattr(old_value, "xhtml_Flow334", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow334"):
                opp_val = getattr(value, "xhtml_Flow334", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow334", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType216(self):
        return self.__xhtml_SmallType216

    @xhtml_SmallType216.setter
    def xhtml_SmallType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType216", None)
        self.__xhtml_SmallType216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot215"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot215"):
                opp_val = getattr(value, "xhtml_DocumentRoot215", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot215", set([self]))
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
    def xhtml_SmallType674(self):
        return self.__xhtml_SmallType674

    @xhtml_SmallType674.setter
    def xhtml_SmallType674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType674", None)
        self.__xhtml_SmallType674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent673"):
                opp_val = getattr(old_value, "xhtml_PreContent673", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent673"):
                opp_val = getattr(value, "xhtml_PreContent673", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent673", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType603(self):
        return self.__xhtml_SmallType603

    @xhtml_SmallType603.setter
    def xhtml_SmallType603(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType603", None)
        self.__xhtml_SmallType603 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType602"):
                opp_val = getattr(old_value, "xhtml_ObjectType602", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType602"):
                opp_val = getattr(value, "xhtml_ObjectType602", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType602", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SmallType471(self):
        return self.__xhtml_SmallType471

    @xhtml_SmallType471.setter
    def xhtml_SmallType471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SmallType__xhtml_SmallType471", None)
        self.__xhtml_SmallType471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline470"):
                opp_val = getattr(old_value, "xhtml_Inline470", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline470"):
                opp_val = getattr(value, "xhtml_Inline470", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline470", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_IType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_IType: "xhtml_AContent" = None, xhtml_IType182: "xhtml_DocumentRoot" = None, xhtml_IType326: "xhtml_Flow" = None, xhtml_IType462: "xhtml_Inline" = None, xhtml_IType594: "xhtml_ObjectType" = None, xhtml_IType665: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_IType = xhtml_IType
        self.xhtml_IType182 = xhtml_IType182
        self.xhtml_IType326 = xhtml_IType326
        self.xhtml_IType462 = xhtml_IType462
        self.xhtml_IType594 = xhtml_IType594
        self.xhtml_IType665 = xhtml_IType665
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_IType182(self):
        return self.__xhtml_IType182

    @xhtml_IType182.setter
    def xhtml_IType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType182", None)
        self.__xhtml_IType182 = value
        
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

    @property
    def xhtml_IType665(self):
        return self.__xhtml_IType665

    @xhtml_IType665.setter
    def xhtml_IType665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType665", None)
        self.__xhtml_IType665 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent664"):
                opp_val = getattr(old_value, "xhtml_PreContent664", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent664"):
                opp_val = getattr(value, "xhtml_PreContent664", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent664", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType462(self):
        return self.__xhtml_IType462

    @xhtml_IType462.setter
    def xhtml_IType462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType462", None)
        self.__xhtml_IType462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline461"):
                opp_val = getattr(old_value, "xhtml_Inline461", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline461"):
                opp_val = getattr(value, "xhtml_Inline461", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline461", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_IType326(self):
        return self.__xhtml_IType326

    @xhtml_IType326.setter
    def xhtml_IType326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType326", None)
        self.__xhtml_IType326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow325"):
                opp_val = getattr(old_value, "xhtml_Flow325", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow325"):
                opp_val = getattr(value, "xhtml_Flow325", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow325", set([self]))
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
    def xhtml_IType594(self):
        return self.__xhtml_IType594

    @xhtml_IType594.setter
    def xhtml_IType594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_IType__xhtml_IType594", None)
        self.__xhtml_IType594 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType593"):
                opp_val = getattr(old_value, "xhtml_ObjectType593", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType593"):
                opp_val = getattr(value, "xhtml_ObjectType593", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType593", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_CodeType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_CodeType: "xhtml_AContent" = None, xhtml_CodeType129: "xhtml_DocumentRoot" = None, xhtml_CodeType353: "xhtml_Flow" = None, xhtml_CodeType489: "xhtml_Inline" = None, xhtml_CodeType621: "xhtml_ObjectType" = None, xhtml_CodeType692: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_CodeType = xhtml_CodeType
        self.xhtml_CodeType129 = xhtml_CodeType129
        self.xhtml_CodeType353 = xhtml_CodeType353
        self.xhtml_CodeType489 = xhtml_CodeType489
        self.xhtml_CodeType621 = xhtml_CodeType621
        self.xhtml_CodeType692 = xhtml_CodeType692
        
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
    def xhtml_CodeType129(self):
        return self.__xhtml_CodeType129

    @xhtml_CodeType129.setter
    def xhtml_CodeType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType129", None)
        self.__xhtml_CodeType129 = value
        
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

    @property
    def xhtml_CodeType353(self):
        return self.__xhtml_CodeType353

    @xhtml_CodeType353.setter
    def xhtml_CodeType353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType353", None)
        self.__xhtml_CodeType353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow352"):
                opp_val = getattr(old_value, "xhtml_Flow352", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow352"):
                opp_val = getattr(value, "xhtml_Flow352", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow352", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType621(self):
        return self.__xhtml_CodeType621

    @xhtml_CodeType621.setter
    def xhtml_CodeType621(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType621", None)
        self.__xhtml_CodeType621 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType620"):
                opp_val = getattr(old_value, "xhtml_ObjectType620", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType620"):
                opp_val = getattr(value, "xhtml_ObjectType620", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType620", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType692(self):
        return self.__xhtml_CodeType692

    @xhtml_CodeType692.setter
    def xhtml_CodeType692(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType692", None)
        self.__xhtml_CodeType692 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent691"):
                opp_val = getattr(old_value, "xhtml_PreContent691", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent691"):
                opp_val = getattr(value, "xhtml_PreContent691", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent691", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_CodeType489(self):
        return self.__xhtml_CodeType489

    @xhtml_CodeType489.setter
    def xhtml_CodeType489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_CodeType__xhtml_CodeType489", None)
        self.__xhtml_CodeType489 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline488"):
                opp_val = getattr(old_value, "xhtml_Inline488", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline488"):
                opp_val = getattr(value, "xhtml_Inline488", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline488", set([self]))
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

class xhtml_UType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_UType: "xhtml_AContent" = None, xhtml_UType252: "xhtml_DocumentRoot" = None, xhtml_UType338: "xhtml_Flow" = None, xhtml_UType474: "xhtml_Inline" = None, xhtml_UType606: "xhtml_ObjectType" = None, xhtml_UType677: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_UType = xhtml_UType
        self.xhtml_UType252 = xhtml_UType252
        self.xhtml_UType338 = xhtml_UType338
        self.xhtml_UType474 = xhtml_UType474
        self.xhtml_UType606 = xhtml_UType606
        self.xhtml_UType677 = xhtml_UType677
        
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
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_UType338(self):
        return self.__xhtml_UType338

    @xhtml_UType338.setter
    def xhtml_UType338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType338", None)
        self.__xhtml_UType338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow337"):
                opp_val = getattr(old_value, "xhtml_Flow337", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow337"):
                opp_val = getattr(value, "xhtml_Flow337", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow337", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UType677(self):
        return self.__xhtml_UType677

    @xhtml_UType677.setter
    def xhtml_UType677(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType677", None)
        self.__xhtml_UType677 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent676"):
                opp_val = getattr(old_value, "xhtml_PreContent676", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent676"):
                opp_val = getattr(value, "xhtml_PreContent676", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent676", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UType252(self):
        return self.__xhtml_UType252

    @xhtml_UType252.setter
    def xhtml_UType252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType252", None)
        self.__xhtml_UType252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot251"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot251"):
                opp_val = getattr(value, "xhtml_DocumentRoot251", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UType606(self):
        return self.__xhtml_UType606

    @xhtml_UType606.setter
    def xhtml_UType606(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType606", None)
        self.__xhtml_UType606 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType605"):
                opp_val = getattr(old_value, "xhtml_ObjectType605", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType605"):
                opp_val = getattr(value, "xhtml_ObjectType605", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType605", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UType474(self):
        return self.__xhtml_UType474

    @xhtml_UType474.setter
    def xhtml_UType474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType474", None)
        self.__xhtml_UType474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline473"):
                opp_val = getattr(old_value, "xhtml_Inline473", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline473"):
                opp_val = getattr(value, "xhtml_Inline473", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline473", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_UType(self):
        return self.__xhtml_UType

    @xhtml_UType.setter
    def xhtml_UType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_UType__xhtml_UType", None)
        self.__xhtml_UType = value
        
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

class xhtml_H2Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H2Type: "xhtml_Block" = None, xhtml_H2Type162: "xhtml_DocumentRoot" = None, xhtml_H2Type266: "xhtml_Flow" = None, xhtml_H2Type394: "xhtml_FormContent" = None, xhtml_H2Type534: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H2Type = xhtml_H2Type
        self.xhtml_H2Type162 = xhtml_H2Type162
        self.xhtml_H2Type266 = xhtml_H2Type266
        self.xhtml_H2Type394 = xhtml_H2Type394
        self.xhtml_H2Type534 = xhtml_H2Type534
        
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
    def xhtml_H2Type162(self):
        return self.__xhtml_H2Type162

    @xhtml_H2Type162.setter
    def xhtml_H2Type162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type162", None)
        self.__xhtml_H2Type162 = value
        
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
    def xhtml_H2Type534(self):
        return self.__xhtml_H2Type534

    @xhtml_H2Type534.setter
    def xhtml_H2Type534(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type534", None)
        self.__xhtml_H2Type534 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType533"):
                opp_val = getattr(old_value, "xhtml_ObjectType533", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType533"):
                opp_val = getattr(value, "xhtml_ObjectType533", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType533", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H2Type394(self):
        return self.__xhtml_H2Type394

    @xhtml_H2Type394.setter
    def xhtml_H2Type394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type394", None)
        self.__xhtml_H2Type394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent393"):
                opp_val = getattr(old_value, "xhtml_FormContent393", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent393"):
                opp_val = getattr(value, "xhtml_FormContent393", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent393", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H2Type266(self):
        return self.__xhtml_H2Type266

    @xhtml_H2Type266.setter
    def xhtml_H2Type266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H2Type__xhtml_H2Type266", None)
        self.__xhtml_H2Type266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow265"):
                opp_val = getattr(old_value, "xhtml_Flow265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow265"):
                opp_val = getattr(value, "xhtml_Flow265", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class xhtml_AddressType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_AddressType: "xhtml_Block" = None, xhtml_AddressType107: "xhtml_DocumentRoot" = None, xhtml_AddressType302: "xhtml_Flow" = None, xhtml_AddressType430: "xhtml_FormContent" = None, xhtml_AddressType570: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_AddressType = xhtml_AddressType
        self.xhtml_AddressType107 = xhtml_AddressType107
        self.xhtml_AddressType302 = xhtml_AddressType302
        self.xhtml_AddressType430 = xhtml_AddressType430
        self.xhtml_AddressType570 = xhtml_AddressType570
        
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
    def xhtml_AddressType302(self):
        return self.__xhtml_AddressType302

    @xhtml_AddressType302.setter
    def xhtml_AddressType302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType302", None)
        self.__xhtml_AddressType302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow301"):
                opp_val = getattr(old_value, "xhtml_Flow301", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow301"):
                opp_val = getattr(value, "xhtml_Flow301", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow301", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType107(self):
        return self.__xhtml_AddressType107

    @xhtml_AddressType107.setter
    def xhtml_AddressType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType107", None)
        self.__xhtml_AddressType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot106"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot106"):
                opp_val = getattr(value, "xhtml_DocumentRoot106", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType570(self):
        return self.__xhtml_AddressType570

    @xhtml_AddressType570.setter
    def xhtml_AddressType570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType570", None)
        self.__xhtml_AddressType570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType569"):
                opp_val = getattr(old_value, "xhtml_ObjectType569", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType569"):
                opp_val = getattr(value, "xhtml_ObjectType569", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType569", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "xhtml_Block79"):
                opp_val = getattr(old_value, "xhtml_Block79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block79"):
                opp_val = getattr(value, "xhtml_Block79", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AddressType430(self):
        return self.__xhtml_AddressType430

    @xhtml_AddressType430.setter
    def xhtml_AddressType430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AddressType__xhtml_AddressType430", None)
        self.__xhtml_AddressType430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent429"):
                opp_val = getattr(old_value, "xhtml_FormContent429", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent429"):
                opp_val = getattr(value, "xhtml_FormContent429", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent429", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_StrongType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_StrongType: "xhtml_AContent" = None, xhtml_StrongType225: "xhtml_DocumentRoot" = None, xhtml_StrongType347: "xhtml_Flow" = None, xhtml_StrongType483: "xhtml_Inline" = None, xhtml_StrongType615: "xhtml_ObjectType" = None, xhtml_StrongType686: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_StrongType = xhtml_StrongType
        self.xhtml_StrongType225 = xhtml_StrongType225
        self.xhtml_StrongType347 = xhtml_StrongType347
        self.xhtml_StrongType483 = xhtml_StrongType483
        self.xhtml_StrongType615 = xhtml_StrongType615
        self.xhtml_StrongType686 = xhtml_StrongType686
        
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
    def xhtml_StrongType(self):
        return self.__xhtml_StrongType

    @xhtml_StrongType.setter
    def xhtml_StrongType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType", None)
        self.__xhtml_StrongType = value
        
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
    def xhtml_StrongType686(self):
        return self.__xhtml_StrongType686

    @xhtml_StrongType686.setter
    def xhtml_StrongType686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType686", None)
        self.__xhtml_StrongType686 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent685"):
                opp_val = getattr(old_value, "xhtml_PreContent685", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent685"):
                opp_val = getattr(value, "xhtml_PreContent685", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent685", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType225(self):
        return self.__xhtml_StrongType225

    @xhtml_StrongType225.setter
    def xhtml_StrongType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType225", None)
        self.__xhtml_StrongType225 = value
        
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
    def xhtml_StrongType347(self):
        return self.__xhtml_StrongType347

    @xhtml_StrongType347.setter
    def xhtml_StrongType347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType347", None)
        self.__xhtml_StrongType347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow346"):
                opp_val = getattr(old_value, "xhtml_Flow346", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow346"):
                opp_val = getattr(value, "xhtml_Flow346", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow346", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType615(self):
        return self.__xhtml_StrongType615

    @xhtml_StrongType615.setter
    def xhtml_StrongType615(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType615", None)
        self.__xhtml_StrongType615 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType614"):
                opp_val = getattr(old_value, "xhtml_ObjectType614", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType614"):
                opp_val = getattr(value, "xhtml_ObjectType614", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType614", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_StrongType483(self):
        return self.__xhtml_StrongType483

    @xhtml_StrongType483.setter
    def xhtml_StrongType483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_StrongType__xhtml_StrongType483", None)
        self.__xhtml_StrongType483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline482"):
                opp_val = getattr(old_value, "xhtml_Inline482", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline482"):
                opp_val = getattr(value, "xhtml_Inline482", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline482", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H6Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H6Type: "xhtml_Block" = None, xhtml_H6Type174: "xhtml_DocumentRoot" = None, xhtml_H6Type278: "xhtml_Flow" = None, xhtml_H6Type406: "xhtml_FormContent" = None, xhtml_H6Type546: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H6Type = xhtml_H6Type
        self.xhtml_H6Type174 = xhtml_H6Type174
        self.xhtml_H6Type278 = xhtml_H6Type278
        self.xhtml_H6Type406 = xhtml_H6Type406
        self.xhtml_H6Type546 = xhtml_H6Type546
        
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
    def xhtml_H6Type(self):
        return self.__xhtml_H6Type

    @xhtml_H6Type.setter
    def xhtml_H6Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type", None)
        self.__xhtml_H6Type = value
        
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
    def xhtml_H6Type546(self):
        return self.__xhtml_H6Type546

    @xhtml_H6Type546.setter
    def xhtml_H6Type546(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type546", None)
        self.__xhtml_H6Type546 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType545"):
                opp_val = getattr(old_value, "xhtml_ObjectType545", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType545"):
                opp_val = getattr(value, "xhtml_ObjectType545", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType545", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H6Type406(self):
        return self.__xhtml_H6Type406

    @xhtml_H6Type406.setter
    def xhtml_H6Type406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type406", None)
        self.__xhtml_H6Type406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent405"):
                opp_val = getattr(old_value, "xhtml_FormContent405", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent405"):
                opp_val = getattr(value, "xhtml_FormContent405", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent405", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H6Type174(self):
        return self.__xhtml_H6Type174

    @xhtml_H6Type174.setter
    def xhtml_H6Type174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type174", None)
        self.__xhtml_H6Type174 = value
        
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
    def xhtml_H6Type278(self):
        return self.__xhtml_H6Type278

    @xhtml_H6Type278.setter
    def xhtml_H6Type278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H6Type__xhtml_H6Type278", None)
        self.__xhtml_H6Type278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow277"):
                opp_val = getattr(old_value, "xhtml_Flow277", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow277"):
                opp_val = getattr(value, "xhtml_Flow277", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow277", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_SpanType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_SpanType: "xhtml_AContent" = None, xhtml_SpanType219: "xhtml_DocumentRoot" = None, xhtml_SpanType314: "xhtml_Flow" = None, xhtml_SpanType450: "xhtml_Inline" = None, xhtml_SpanType582: "xhtml_ObjectType" = None, xhtml_SpanType725: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_SpanType = xhtml_SpanType
        self.xhtml_SpanType219 = xhtml_SpanType219
        self.xhtml_SpanType314 = xhtml_SpanType314
        self.xhtml_SpanType450 = xhtml_SpanType450
        self.xhtml_SpanType582 = xhtml_SpanType582
        self.xhtml_SpanType725 = xhtml_SpanType725
        
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
    def xhtml_SpanType219(self):
        return self.__xhtml_SpanType219

    @xhtml_SpanType219.setter
    def xhtml_SpanType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType219", None)
        self.__xhtml_SpanType219 = value
        
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
    def xhtml_SpanType582(self):
        return self.__xhtml_SpanType582

    @xhtml_SpanType582.setter
    def xhtml_SpanType582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType582", None)
        self.__xhtml_SpanType582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType581"):
                opp_val = getattr(old_value, "xhtml_ObjectType581", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType581"):
                opp_val = getattr(value, "xhtml_ObjectType581", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType581", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType450(self):
        return self.__xhtml_SpanType450

    @xhtml_SpanType450.setter
    def xhtml_SpanType450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType450", None)
        self.__xhtml_SpanType450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline449"):
                opp_val = getattr(old_value, "xhtml_Inline449", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline449"):
                opp_val = getattr(value, "xhtml_Inline449", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline449", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType314(self):
        return self.__xhtml_SpanType314

    @xhtml_SpanType314.setter
    def xhtml_SpanType314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType314", None)
        self.__xhtml_SpanType314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow313"):
                opp_val = getattr(old_value, "xhtml_Flow313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow313"):
                opp_val = getattr(value, "xhtml_Flow313", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_SpanType725(self):
        return self.__xhtml_SpanType725

    @xhtml_SpanType725.setter
    def xhtml_SpanType725(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_SpanType__xhtml_SpanType725", None)
        self.__xhtml_SpanType725 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent724"):
                opp_val = getattr(old_value, "xhtml_PreContent724", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent724"):
                opp_val = getattr(value, "xhtml_PreContent724", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent724", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_H3Type(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_H3Type: "xhtml_Block" = None, xhtml_H3Type165: "xhtml_DocumentRoot" = None, xhtml_H3Type269: "xhtml_Flow" = None, xhtml_H3Type397: "xhtml_FormContent" = None, xhtml_H3Type537: "xhtml_ObjectType" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_H3Type = xhtml_H3Type
        self.xhtml_H3Type165 = xhtml_H3Type165
        self.xhtml_H3Type269 = xhtml_H3Type269
        self.xhtml_H3Type397 = xhtml_H3Type397
        self.xhtml_H3Type537 = xhtml_H3Type537
        
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
    def xhtml_H3Type397(self):
        return self.__xhtml_H3Type397

    @xhtml_H3Type397.setter
    def xhtml_H3Type397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type397", None)
        self.__xhtml_H3Type397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_FormContent396"):
                opp_val = getattr(old_value, "xhtml_FormContent396", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_FormContent396"):
                opp_val = getattr(value, "xhtml_FormContent396", None)
                if opp_val is None:
                    setattr(value, "xhtml_FormContent396", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H3Type269(self):
        return self.__xhtml_H3Type269

    @xhtml_H3Type269.setter
    def xhtml_H3Type269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type269", None)
        self.__xhtml_H3Type269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow268"):
                opp_val = getattr(old_value, "xhtml_Flow268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow268"):
                opp_val = getattr(value, "xhtml_Flow268", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow268", set([self]))
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
    def xhtml_H3Type537(self):
        return self.__xhtml_H3Type537

    @xhtml_H3Type537.setter
    def xhtml_H3Type537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type537", None)
        self.__xhtml_H3Type537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType536"):
                opp_val = getattr(old_value, "xhtml_ObjectType536", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType536"):
                opp_val = getattr(value, "xhtml_ObjectType536", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType536", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_H3Type165(self):
        return self.__xhtml_H3Type165

    @xhtml_H3Type165.setter
    def xhtml_H3Type165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_H3Type__xhtml_H3Type165", None)
        self.__xhtml_H3Type165 = value
        
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

class xhtml_AbbrType(Inline):

    def __init__(self, class: str, id: str, style: str, title: str, xhtml_AbbrType: "xhtml_AContent" = None, xhtml_AbbrType101: "xhtml_DocumentRoot" = None, xhtml_AbbrType371: "xhtml_Flow" = None, xhtml_AbbrType507: "xhtml_Inline" = None, xhtml_AbbrType639: "xhtml_ObjectType" = None, xhtml_AbbrType710: "xhtml_PreContent" = None):
        self.class = class
        self.id = id
        self.style = style
        self.title = title
        self.xhtml_AbbrType = xhtml_AbbrType
        self.xhtml_AbbrType101 = xhtml_AbbrType101
        self.xhtml_AbbrType371 = xhtml_AbbrType371
        self.xhtml_AbbrType507 = xhtml_AbbrType507
        self.xhtml_AbbrType639 = xhtml_AbbrType639
        self.xhtml_AbbrType710 = xhtml_AbbrType710
        
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
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

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
    def xhtml_AbbrType639(self):
        return self.__xhtml_AbbrType639

    @xhtml_AbbrType639.setter
    def xhtml_AbbrType639(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType639", None)
        self.__xhtml_AbbrType639 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_ObjectType638"):
                opp_val = getattr(old_value, "xhtml_ObjectType638", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_ObjectType638"):
                opp_val = getattr(value, "xhtml_ObjectType638", None)
                if opp_val is None:
                    setattr(value, "xhtml_ObjectType638", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType710(self):
        return self.__xhtml_AbbrType710

    @xhtml_AbbrType710.setter
    def xhtml_AbbrType710(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType710", None)
        self.__xhtml_AbbrType710 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent709"):
                opp_val = getattr(old_value, "xhtml_PreContent709", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent709"):
                opp_val = getattr(value, "xhtml_PreContent709", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent709", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType371(self):
        return self.__xhtml_AbbrType371

    @xhtml_AbbrType371.setter
    def xhtml_AbbrType371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType371", None)
        self.__xhtml_AbbrType371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow370"):
                opp_val = getattr(old_value, "xhtml_Flow370", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow370"):
                opp_val = getattr(value, "xhtml_Flow370", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow370", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType507(self):
        return self.__xhtml_AbbrType507

    @xhtml_AbbrType507.setter
    def xhtml_AbbrType507(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType507", None)
        self.__xhtml_AbbrType507 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline506"):
                opp_val = getattr(old_value, "xhtml_Inline506", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline506"):
                opp_val = getattr(value, "xhtml_Inline506", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline506", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_AbbrType101(self):
        return self.__xhtml_AbbrType101

    @xhtml_AbbrType101.setter
    def xhtml_AbbrType101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AbbrType__xhtml_AbbrType101", None)
        self.__xhtml_AbbrType101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_DocumentRoot100"):
                opp_val = getattr(old_value, "xhtml_DocumentRoot100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_DocumentRoot100"):
                opp_val = getattr(value, "xhtml_DocumentRoot100", None)
                if opp_val is None:
                    setattr(value, "xhtml_DocumentRoot100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
