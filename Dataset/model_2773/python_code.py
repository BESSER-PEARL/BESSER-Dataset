from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class xDstmdata_composingtype:

    def __init__(self, tID: str, tString: str, xDstmdata_composingtype: "xDstmdata_tMultitype" = None, xDstmdata_composingtype18: "xDstmdata_channel_specifier" = None):
        self.tID = tID
        self.tString = tString
        self.xDstmdata_composingtype = xDstmdata_composingtype
        self.xDstmdata_composingtype18 = xDstmdata_composingtype18
        
    @property
    def tString(self) -> str:
        return self.__tString

    @tString.setter
    def tString(self, tString: str):
        self.__tString = tString

    @property
    def tID(self) -> str:
        return self.__tID

    @tID.setter
    def tID(self, tID: str):
        self.__tID = tID

    @property
    def xDstmdata_composingtype(self):
        return self.__xDstmdata_composingtype

    @xDstmdata_composingtype.setter
    def xDstmdata_composingtype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_composingtype__xDstmdata_composingtype", None)
        self.__xDstmdata_composingtype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tMultitype16"):
                opp_val = getattr(old_value, "xDstmdata_tMultitype16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tMultitype16"):
                opp_val = getattr(value, "xDstmdata_tMultitype16", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tMultitype16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDstmdata_composingtype18(self):
        return self.__xDstmdata_composingtype18

    @xDstmdata_composingtype18.setter
    def xDstmdata_composingtype18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_composingtype__xDstmdata_composingtype18", None)
        self.__xDstmdata_composingtype18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_channel_specifier19"):
                opp_val = getattr(old_value, "xDstmdata_channel_specifier19", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_channel_specifier19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_channel_specifier19"):
                opp_val = getattr(value, "xDstmdata_channel_specifier19", None)
                setattr(value, "xDstmdata_channel_specifier19", self)

class xDstmdata_channel_specifier:

    def __init__(self, type: str, xDstmdata_channel_specifier22: "xDstmdata_cIntchannel" = None, xDstmdata_channel_specifier: "xDstmdata_subtype" = None, xDstmdata_channel_specifier19: "xDstmdata_composingtype" = None, xDstmdata_channel_specifier25: "xDstmdata_cExtchannel" = None, xDstmdata_channel_specifier28: "xDstmdata_vVariable" = None):
        self.type = type
        self.xDstmdata_channel_specifier22 = xDstmdata_channel_specifier22
        self.xDstmdata_channel_specifier = xDstmdata_channel_specifier
        self.xDstmdata_channel_specifier19 = xDstmdata_channel_specifier19
        self.xDstmdata_channel_specifier25 = xDstmdata_channel_specifier25
        self.xDstmdata_channel_specifier28 = xDstmdata_channel_specifier28
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xDstmdata_channel_specifier28(self):
        return self.__xDstmdata_channel_specifier28

    @xDstmdata_channel_specifier28.setter
    def xDstmdata_channel_specifier28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_channel_specifier__xDstmdata_channel_specifier28", None)
        self.__xDstmdata_channel_specifier28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_vVariable27"):
                opp_val = getattr(old_value, "xDstmdata_vVariable27", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_vVariable27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_vVariable27"):
                opp_val = getattr(value, "xDstmdata_vVariable27", None)
                setattr(value, "xDstmdata_vVariable27", self)

    @property
    def xDstmdata_channel_specifier19(self):
        return self.__xDstmdata_channel_specifier19

    @xDstmdata_channel_specifier19.setter
    def xDstmdata_channel_specifier19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_channel_specifier__xDstmdata_channel_specifier19", None)
        self.__xDstmdata_channel_specifier19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_composingtype18"):
                opp_val = getattr(old_value, "xDstmdata_composingtype18", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_composingtype18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_composingtype18"):
                opp_val = getattr(value, "xDstmdata_composingtype18", None)
                setattr(value, "xDstmdata_composingtype18", self)

    @property
    def xDstmdata_channel_specifier25(self):
        return self.__xDstmdata_channel_specifier25

    @xDstmdata_channel_specifier25.setter
    def xDstmdata_channel_specifier25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_channel_specifier__xDstmdata_channel_specifier25", None)
        self.__xDstmdata_channel_specifier25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_cExtchannel24"):
                opp_val = getattr(old_value, "xDstmdata_cExtchannel24", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_cExtchannel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_cExtchannel24"):
                opp_val = getattr(value, "xDstmdata_cExtchannel24", None)
                setattr(value, "xDstmdata_cExtchannel24", self)

    @property
    def xDstmdata_channel_specifier(self):
        return self.__xDstmdata_channel_specifier

    @xDstmdata_channel_specifier.setter
    def xDstmdata_channel_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_channel_specifier__xDstmdata_channel_specifier", None)
        self.__xDstmdata_channel_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_subtype14"):
                opp_val = getattr(old_value, "xDstmdata_subtype14", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_subtype14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_subtype14"):
                opp_val = getattr(value, "xDstmdata_subtype14", None)
                setattr(value, "xDstmdata_subtype14", self)

    @property
    def xDstmdata_channel_specifier22(self):
        return self.__xDstmdata_channel_specifier22

    @xDstmdata_channel_specifier22.setter
    def xDstmdata_channel_specifier22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_channel_specifier__xDstmdata_channel_specifier22", None)
        self.__xDstmdata_channel_specifier22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_cIntchannel21"):
                opp_val = getattr(old_value, "xDstmdata_cIntchannel21", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_cIntchannel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_cIntchannel21"):
                opp_val = getattr(value, "xDstmdata_cIntchannel21", None)
                setattr(value, "xDstmdata_cIntchannel21", self)

class xDstmdata_subtype:

    def __init__(self, tString: str, tID: str, xDstmdata_subtype: "xDstmdata_tCompound" = None, xDstmdata_subtype14: "xDstmdata_channel_specifier" = None):
        self.tString = tString
        self.tID = tID
        self.xDstmdata_subtype = xDstmdata_subtype
        self.xDstmdata_subtype14 = xDstmdata_subtype14
        
    @property
    def tString(self) -> str:
        return self.__tString

    @tString.setter
    def tString(self, tString: str):
        self.__tString = tString

    @property
    def tID(self) -> str:
        return self.__tID

    @tID.setter
    def tID(self, tID: str):
        self.__tID = tID

    @property
    def xDstmdata_subtype(self):
        return self.__xDstmdata_subtype

    @xDstmdata_subtype.setter
    def xDstmdata_subtype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_subtype__xDstmdata_subtype", None)
        self.__xDstmdata_subtype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tCompound12"):
                opp_val = getattr(old_value, "xDstmdata_tCompound12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tCompound12"):
                opp_val = getattr(value, "xDstmdata_tCompound12", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tCompound12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDstmdata_subtype14(self):
        return self.__xDstmdata_subtype14

    @xDstmdata_subtype14.setter
    def xDstmdata_subtype14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_subtype__xDstmdata_subtype14", None)
        self.__xDstmdata_subtype14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_channel_specifier"):
                opp_val = getattr(old_value, "xDstmdata_channel_specifier", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_channel_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_channel_specifier"):
                opp_val = getattr(value, "xDstmdata_channel_specifier", None)
                setattr(value, "xDstmdata_channel_specifier", self)

class xDstmdata_cExtchannel:

    def __init__(self, name: str, tString: str, tID: str, xDstmdata_cExtchannel: "xDstmdata_tTypes" = None, xDstmdata_cExtchannel24: "xDstmdata_channel_specifier" = None):
        self.name = name
        self.tString = tString
        self.tID = tID
        self.xDstmdata_cExtchannel = xDstmdata_cExtchannel
        self.xDstmdata_cExtchannel24 = xDstmdata_cExtchannel24
        
    @property
    def tString(self) -> str:
        return self.__tString

    @tString.setter
    def tString(self, tString: str):
        self.__tString = tString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tID(self) -> str:
        return self.__tID

    @tID.setter
    def tID(self, tID: str):
        self.__tID = tID

    @property
    def xDstmdata_cExtchannel24(self):
        return self.__xDstmdata_cExtchannel24

    @xDstmdata_cExtchannel24.setter
    def xDstmdata_cExtchannel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_cExtchannel__xDstmdata_cExtchannel24", None)
        self.__xDstmdata_cExtchannel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_channel_specifier25"):
                opp_val = getattr(old_value, "xDstmdata_channel_specifier25", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_channel_specifier25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_channel_specifier25"):
                opp_val = getattr(value, "xDstmdata_channel_specifier25", None)
                setattr(value, "xDstmdata_channel_specifier25", self)

    @property
    def xDstmdata_cExtchannel(self):
        return self.__xDstmdata_cExtchannel

    @xDstmdata_cExtchannel.setter
    def xDstmdata_cExtchannel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_cExtchannel__xDstmdata_cExtchannel", None)
        self.__xDstmdata_cExtchannel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes8"):
                opp_val = getattr(old_value, "xDstmdata_tTypes8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes8"):
                opp_val = getattr(value, "xDstmdata_tTypes8", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xDstmdata_cIntchannel:

    def __init__(self, name: str, bound: int, tString: str, tID: str, xDstmdata_cIntchannel: "xDstmdata_tTypes" = None, xDstmdata_cIntchannel21: "xDstmdata_channel_specifier" = None):
        self.name = name
        self.bound = bound
        self.tString = tString
        self.tID = tID
        self.xDstmdata_cIntchannel = xDstmdata_cIntchannel
        self.xDstmdata_cIntchannel21 = xDstmdata_cIntchannel21
        
    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def tID(self) -> str:
        return self.__tID

    @tID.setter
    def tID(self, tID: str):
        self.__tID = tID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tString(self) -> str:
        return self.__tString

    @tString.setter
    def tString(self, tString: str):
        self.__tString = tString

    @property
    def xDstmdata_cIntchannel(self):
        return self.__xDstmdata_cIntchannel

    @xDstmdata_cIntchannel.setter
    def xDstmdata_cIntchannel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_cIntchannel__xDstmdata_cIntchannel", None)
        self.__xDstmdata_cIntchannel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes6"):
                opp_val = getattr(old_value, "xDstmdata_tTypes6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes6"):
                opp_val = getattr(value, "xDstmdata_tTypes6", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDstmdata_cIntchannel21(self):
        return self.__xDstmdata_cIntchannel21

    @xDstmdata_cIntchannel21.setter
    def xDstmdata_cIntchannel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_cIntchannel__xDstmdata_cIntchannel21", None)
        self.__xDstmdata_cIntchannel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_channel_specifier22"):
                opp_val = getattr(old_value, "xDstmdata_channel_specifier22", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_channel_specifier22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_channel_specifier22"):
                opp_val = getattr(value, "xDstmdata_channel_specifier22", None)
                setattr(value, "xDstmdata_channel_specifier22", self)

class xDstmdata_tMultitype:

    def __init__(self, name: str, xDstmdata_tMultitype: "xDstmdata_tTypes" = None, xDstmdata_tMultitype16: set["xDstmdata_composingtype"] = None):
        self.name = name
        self.xDstmdata_tMultitype = xDstmdata_tMultitype
        self.xDstmdata_tMultitype16 = xDstmdata_tMultitype16 if xDstmdata_tMultitype16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xDstmdata_tMultitype(self):
        return self.__xDstmdata_tMultitype

    @xDstmdata_tMultitype.setter
    def xDstmdata_tMultitype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_tMultitype__xDstmdata_tMultitype", None)
        self.__xDstmdata_tMultitype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes4"):
                opp_val = getattr(old_value, "xDstmdata_tTypes4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes4"):
                opp_val = getattr(value, "xDstmdata_tTypes4", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDstmdata_tMultitype16(self):
        return self.__xDstmdata_tMultitype16

    @xDstmdata_tMultitype16.setter
    def xDstmdata_tMultitype16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_tMultitype__xDstmdata_tMultitype16", None)
        self.__xDstmdata_tMultitype16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xDstmdata_composingtype"):
                    opp_val = getattr(item, "xDstmdata_composingtype", None)
                    
                    if opp_val == self:
                        setattr(item, "xDstmdata_composingtype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xDstmdata_composingtype"):
                    opp_val = getattr(item, "xDstmdata_composingtype", None)
                    
                    setattr(item, "xDstmdata_composingtype", self)
                    

class xDstmdata_tCompound:

    def __init__(self, name: str, xDstmdata_tCompound: "xDstmdata_tTypes" = None, xDstmdata_tCompound12: set["xDstmdata_subtype"] = None):
        self.name = name
        self.xDstmdata_tCompound = xDstmdata_tCompound
        self.xDstmdata_tCompound12 = xDstmdata_tCompound12 if xDstmdata_tCompound12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xDstmdata_tCompound(self):
        return self.__xDstmdata_tCompound

    @xDstmdata_tCompound.setter
    def xDstmdata_tCompound(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_tCompound__xDstmdata_tCompound", None)
        self.__xDstmdata_tCompound = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes2"):
                opp_val = getattr(old_value, "xDstmdata_tTypes2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes2"):
                opp_val = getattr(value, "xDstmdata_tTypes2", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDstmdata_tCompound12(self):
        return self.__xDstmdata_tCompound12

    @xDstmdata_tCompound12.setter
    def xDstmdata_tCompound12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_tCompound__xDstmdata_tCompound12", None)
        self.__xDstmdata_tCompound12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xDstmdata_subtype"):
                    opp_val = getattr(item, "xDstmdata_subtype", None)
                    
                    if opp_val == self:
                        setattr(item, "xDstmdata_subtype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xDstmdata_subtype"):
                    opp_val = getattr(item, "xDstmdata_subtype", None)
                    
                    setattr(item, "xDstmdata_subtype", self)
                    

class xDstmdata_tEnum:

    def __init__(self, name: str, literals: str, xDstmdata_tEnum: "xDstmdata_tTypes" = None):
        self.name = name
        self.literals = literals
        self.xDstmdata_tEnum = xDstmdata_tEnum
        
    @property
    def literals(self) -> str:
        return self.__literals

    @literals.setter
    def literals(self, literals: str):
        self.__literals = literals

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xDstmdata_tEnum(self):
        return self.__xDstmdata_tEnum

    @xDstmdata_tEnum.setter
    def xDstmdata_tEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_tEnum__xDstmdata_tEnum", None)
        self.__xDstmdata_tEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes"):
                opp_val = getattr(old_value, "xDstmdata_tTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes"):
                opp_val = getattr(value, "xDstmdata_tTypes", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xDstmdata_tTypes:

    pass
class xDstmdata_vVariable:

    def __init__(self, tString: str, tID: str, name: str, xDstmdata_vVariable: "xDstmdata_tTypes" = None, xDstmdata_vVariable27: "xDstmdata_channel_specifier" = None):
        self.tString = tString
        self.tID = tID
        self.name = name
        self.xDstmdata_vVariable = xDstmdata_vVariable
        self.xDstmdata_vVariable27 = xDstmdata_vVariable27
        
    @property
    def tID(self) -> str:
        return self.__tID

    @tID.setter
    def tID(self, tID: str):
        self.__tID = tID

    @property
    def tString(self) -> str:
        return self.__tString

    @tString.setter
    def tString(self, tString: str):
        self.__tString = tString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xDstmdata_vVariable27(self):
        return self.__xDstmdata_vVariable27

    @xDstmdata_vVariable27.setter
    def xDstmdata_vVariable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_vVariable__xDstmdata_vVariable27", None)
        self.__xDstmdata_vVariable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_channel_specifier28"):
                opp_val = getattr(old_value, "xDstmdata_channel_specifier28", None)
                if opp_val == self:
                    setattr(old_value, "xDstmdata_channel_specifier28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_channel_specifier28"):
                opp_val = getattr(value, "xDstmdata_channel_specifier28", None)
                setattr(value, "xDstmdata_channel_specifier28", self)

    @property
    def xDstmdata_vVariable(self):
        return self.__xDstmdata_vVariable

    @xDstmdata_vVariable.setter
    def xDstmdata_vVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDstmdata_vVariable__xDstmdata_vVariable", None)
        self.__xDstmdata_vVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDstmdata_tTypes10"):
                opp_val = getattr(old_value, "xDstmdata_tTypes10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDstmdata_tTypes10"):
                opp_val = getattr(value, "xDstmdata_tTypes10", None)
                if opp_val is None:
                    setattr(value, "xDstmdata_tTypes10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
