from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dml_TAN:

    def __init__(self, t: str, dml_TAN: "dml_PL" = None, dml_TAN104: "dml_ID" = None):
        self.t = t
        self.dml_TAN = dml_TAN
        self.dml_TAN104 = dml_TAN104
        
    @property
    def t(self) -> str:
        return self.__t

    @t.setter
    def t(self, t: str):
        self.__t = t

    @property
    def dml_TAN104(self):
        return self.__dml_TAN104

    @dml_TAN104.setter
    def dml_TAN104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_TAN__dml_TAN104", None)
        self.__dml_TAN104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_ID105"):
                opp_val = getattr(old_value, "dml_ID105", None)
                if opp_val == self:
                    setattr(old_value, "dml_ID105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_ID105"):
                opp_val = getattr(value, "dml_ID105", None)
                setattr(value, "dml_ID105", self)

    @property
    def dml_TAN(self):
        return self.__dml_TAN

    @dml_TAN.setter
    def dml_TAN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_TAN__dml_TAN", None)
        self.__dml_TAN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_PL80"):
                opp_val = getattr(old_value, "dml_PL80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_PL80"):
                opp_val = getattr(value, "dml_PL80", None)
                if opp_val is None:
                    setattr(value, "dml_PL80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dml_TE:

    def __init__(self, i: int, d: float, s: str, b: str, dml_TE: "dml_E" = None, dml_TE89: "dml_FC" = None, dml_TE92: "dml_DI" = None):
        self.i = i
        self.d = d
        self.s = s
        self.b = b
        self.dml_TE = dml_TE
        self.dml_TE89 = dml_TE89
        self.dml_TE92 = dml_TE92
        
    @property
    def d(self) -> float:
        return self.__d

    @d.setter
    def d(self, d: float):
        self.__d = d

    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def s(self) -> str:
        return self.__s

    @s.setter
    def s(self, s: str):
        self.__s = s

    @property
    def dml_TE92(self):
        return self.__dml_TE92

    @dml_TE92.setter
    def dml_TE92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_TE__dml_TE92", None)
        self.__dml_TE92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_DI93"):
                opp_val = getattr(old_value, "dml_DI93", None)
                if opp_val == self:
                    setattr(old_value, "dml_DI93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_DI93"):
                opp_val = getattr(value, "dml_DI93", None)
                setattr(value, "dml_DI93", self)

    @property
    def dml_TE89(self):
        return self.__dml_TE89

    @dml_TE89.setter
    def dml_TE89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_TE__dml_TE89", None)
        self.__dml_TE89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FC90"):
                opp_val = getattr(old_value, "dml_FC90", None)
                if opp_val == self:
                    setattr(old_value, "dml_FC90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FC90"):
                opp_val = getattr(value, "dml_FC90", None)
                setattr(value, "dml_FC90", self)

    @property
    def dml_TE(self):
        return self.__dml_TE

    @dml_TE.setter
    def dml_TE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_TE__dml_TE", None)
        self.__dml_TE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_E87"):
                opp_val = getattr(old_value, "dml_E87", None)
                if opp_val == self:
                    setattr(old_value, "dml_E87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_E87"):
                opp_val = getattr(value, "dml_E87", None)
                setattr(value, "dml_E87", self)

class dml_EObject:

    pass
class dml_PE:

    pass
class dml_IS:

    pass
class dml_PARFORPARAMS:

    def __init__(self, params: str, dml_PARFORPARAMS: "dml_S" = None):
        self.params = params
        self.dml_PARFORPARAMS = dml_PARFORPARAMS
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def dml_PARFORPARAMS(self):
        return self.__dml_PARFORPARAMS

    @dml_PARFORPARAMS.setter
    def dml_PARFORPARAMS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_PARFORPARAMS__dml_PARFORPARAMS", None)
        self.__dml_PARFORPARAMS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S28"):
                opp_val = getattr(old_value, "dml_S28", None)
                if opp_val == self:
                    setattr(old_value, "dml_S28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S28"):
                opp_val = getattr(value, "dml_S28", None)
                setattr(value, "dml_S28", self)

class dml_FP:

    pass
class dml_BS:

    pass
class dml_FC:

    def __init__(self, bif: str, dml_FC: "dml_S" = None, dml_FC49: "dml_ID" = None, dml_FC52: set["dml_PE"] = None, dml_FC90: "dml_TE" = None):
        self.bif = bif
        self.dml_FC = dml_FC
        self.dml_FC49 = dml_FC49
        self.dml_FC52 = dml_FC52 if dml_FC52 is not None else set()
        self.dml_FC90 = dml_FC90
        
    @property
    def bif(self) -> str:
        return self.__bif

    @bif.setter
    def bif(self, bif: str):
        self.__bif = bif

    @property
    def dml_FC(self):
        return self.__dml_FC

    @dml_FC.setter
    def dml_FC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_FC__dml_FC", None)
        self.__dml_FC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S41"):
                opp_val = getattr(old_value, "dml_S41", None)
                if opp_val == self:
                    setattr(old_value, "dml_S41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S41"):
                opp_val = getattr(value, "dml_S41", None)
                setattr(value, "dml_S41", self)

    @property
    def dml_FC90(self):
        return self.__dml_FC90

    @dml_FC90.setter
    def dml_FC90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_FC__dml_FC90", None)
        self.__dml_FC90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_TE89"):
                opp_val = getattr(old_value, "dml_TE89", None)
                if opp_val == self:
                    setattr(old_value, "dml_TE89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_TE89"):
                opp_val = getattr(value, "dml_TE89", None)
                setattr(value, "dml_TE89", self)

    @property
    def dml_FC52(self):
        return self.__dml_FC52

    @dml_FC52.setter
    def dml_FC52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_FC__dml_FC52", None)
        self.__dml_FC52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dml_PE"):
                    opp_val = getattr(item, "dml_PE", None)
                    
                    if opp_val == self:
                        setattr(item, "dml_PE", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dml_PE"):
                    opp_val = getattr(item, "dml_PE", None)
                    
                    setattr(item, "dml_PE", self)
                    

    @property
    def dml_FC49(self):
        return self.__dml_FC49

    @dml_FC49.setter
    def dml_FC49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_FC__dml_FC49", None)
        self.__dml_FC49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_ID50"):
                opp_val = getattr(old_value, "dml_ID50", None)
                if opp_val == self:
                    setattr(old_value, "dml_ID50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_ID50"):
                opp_val = getattr(value, "dml_ID50", None)
                setattr(value, "dml_ID50", self)

class dml_DI:

    def __init__(self, clid: str, cln: str, dml_DI: "dml_S" = None, dml_DI44: "dml_S" = None, dml_DI65: "dml_ID" = None, dml_DI68: "dml_IS" = None, dml_DI71: "dml_IS" = None, dml_DI93: "dml_TE" = None):
        self.clid = clid
        self.cln = cln
        self.dml_DI = dml_DI
        self.dml_DI44 = dml_DI44
        self.dml_DI65 = dml_DI65
        self.dml_DI68 = dml_DI68
        self.dml_DI71 = dml_DI71
        self.dml_DI93 = dml_DI93
        
    @property
    def cln(self) -> str:
        return self.__cln

    @cln.setter
    def cln(self, cln: str):
        self.__cln = cln

    @property
    def clid(self) -> str:
        return self.__clid

    @clid.setter
    def clid(self, clid: str):
        self.__clid = clid

    @property
    def dml_DI65(self):
        return self.__dml_DI65

    @dml_DI65.setter
    def dml_DI65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI65", None)
        self.__dml_DI65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_ID66"):
                opp_val = getattr(old_value, "dml_ID66", None)
                if opp_val == self:
                    setattr(old_value, "dml_ID66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_ID66"):
                opp_val = getattr(value, "dml_ID66", None)
                setattr(value, "dml_ID66", self)

    @property
    def dml_DI93(self):
        return self.__dml_DI93

    @dml_DI93.setter
    def dml_DI93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI93", None)
        self.__dml_DI93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_TE92"):
                opp_val = getattr(old_value, "dml_TE92", None)
                if opp_val == self:
                    setattr(old_value, "dml_TE92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_TE92"):
                opp_val = getattr(value, "dml_TE92", None)
                setattr(value, "dml_TE92", self)

    @property
    def dml_DI68(self):
        return self.__dml_DI68

    @dml_DI68.setter
    def dml_DI68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI68", None)
        self.__dml_DI68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_IS69"):
                opp_val = getattr(old_value, "dml_IS69", None)
                if opp_val == self:
                    setattr(old_value, "dml_IS69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_IS69"):
                opp_val = getattr(value, "dml_IS69", None)
                setattr(value, "dml_IS69", self)

    @property
    def dml_DI44(self):
        return self.__dml_DI44

    @dml_DI44.setter
    def dml_DI44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI44", None)
        self.__dml_DI44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S43"):
                opp_val = getattr(old_value, "dml_S43", None)
                if opp_val == self:
                    setattr(old_value, "dml_S43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S43"):
                opp_val = getattr(value, "dml_S43", None)
                setattr(value, "dml_S43", self)

    @property
    def dml_DI71(self):
        return self.__dml_DI71

    @dml_DI71.setter
    def dml_DI71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI71", None)
        self.__dml_DI71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_IS72"):
                opp_val = getattr(old_value, "dml_IS72", None)
                if opp_val == self:
                    setattr(old_value, "dml_IS72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_IS72"):
                opp_val = getattr(value, "dml_IS72", None)
                setattr(value, "dml_IS72", self)

    @property
    def dml_DI(self):
        return self.__dml_DI

    @dml_DI.setter
    def dml_DI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_DI__dml_DI", None)
        self.__dml_DI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S39"):
                opp_val = getattr(old_value, "dml_S39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S39"):
                opp_val = getattr(value, "dml_S39", None)
                if opp_val is None:
                    setattr(value, "dml_S39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dml_SPKV:

    def __init__(self, v: str, dml_SPKV: "dml_F" = None, dml_SPKV95: "dml_ID" = None):
        self.v = v
        self.dml_SPKV = dml_SPKV
        self.dml_SPKV95 = dml_SPKV95
        
    @property
    def v(self) -> str:
        return self.__v

    @v.setter
    def v(self, v: str):
        self.__v = v

    @property
    def dml_SPKV(self):
        return self.__dml_SPKV

    @dml_SPKV.setter
    def dml_SPKV(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_SPKV__dml_SPKV", None)
        self.__dml_SPKV = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_F14"):
                opp_val = getattr(old_value, "dml_F14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_F14"):
                opp_val = getattr(value, "dml_F14", None)
                if opp_val is None:
                    setattr(value, "dml_F14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dml_SPKV95(self):
        return self.__dml_SPKV95

    @dml_SPKV95.setter
    def dml_SPKV95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_SPKV__dml_SPKV95", None)
        self.__dml_SPKV95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_ID96"):
                opp_val = getattr(old_value, "dml_ID96", None)
                if opp_val == self:
                    setattr(old_value, "dml_ID96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_ID96"):
                opp_val = getattr(value, "dml_ID96", None)
                setattr(value, "dml_ID96", self)

class dml_PL:

    pass
class dml_ID:

    def __init__(self, name: str, dml_ID17: "dml_S" = None, dml_ID: "dml_F" = None, dml_ID66: "dml_DI" = None, dml_ID50: "dml_FC" = None, dml_ID61: "dml_FP" = None, dml_ID96: "dml_SPKV" = None, dml_ID105: "dml_TAN" = None, dml_ID99: "dml_PE" = None):
        self.name = name
        self.dml_ID17 = dml_ID17
        self.dml_ID = dml_ID
        self.dml_ID66 = dml_ID66
        self.dml_ID50 = dml_ID50
        self.dml_ID61 = dml_ID61
        self.dml_ID96 = dml_ID96
        self.dml_ID105 = dml_ID105
        self.dml_ID99 = dml_ID99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dml_ID96(self):
        return self.__dml_ID96

    @dml_ID96.setter
    def dml_ID96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID96", None)
        self.__dml_ID96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_SPKV95"):
                opp_val = getattr(old_value, "dml_SPKV95", None)
                if opp_val == self:
                    setattr(old_value, "dml_SPKV95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_SPKV95"):
                opp_val = getattr(value, "dml_SPKV95", None)
                setattr(value, "dml_SPKV95", self)

    @property
    def dml_ID(self):
        return self.__dml_ID

    @dml_ID.setter
    def dml_ID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID", None)
        self.__dml_ID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_F4"):
                opp_val = getattr(old_value, "dml_F4", None)
                if opp_val == self:
                    setattr(old_value, "dml_F4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_F4"):
                opp_val = getattr(value, "dml_F4", None)
                setattr(value, "dml_F4", self)

    @property
    def dml_ID99(self):
        return self.__dml_ID99

    @dml_ID99.setter
    def dml_ID99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID99", None)
        self.__dml_ID99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_PE98"):
                opp_val = getattr(old_value, "dml_PE98", None)
                if opp_val == self:
                    setattr(old_value, "dml_PE98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_PE98"):
                opp_val = getattr(value, "dml_PE98", None)
                setattr(value, "dml_PE98", self)

    @property
    def dml_ID50(self):
        return self.__dml_ID50

    @dml_ID50.setter
    def dml_ID50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID50", None)
        self.__dml_ID50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FC49"):
                opp_val = getattr(old_value, "dml_FC49", None)
                if opp_val == self:
                    setattr(old_value, "dml_FC49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FC49"):
                opp_val = getattr(value, "dml_FC49", None)
                setattr(value, "dml_FC49", self)

    @property
    def dml_ID17(self):
        return self.__dml_ID17

    @dml_ID17.setter
    def dml_ID17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID17", None)
        self.__dml_ID17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S16"):
                opp_val = getattr(old_value, "dml_S16", None)
                if opp_val == self:
                    setattr(old_value, "dml_S16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S16"):
                opp_val = getattr(value, "dml_S16", None)
                setattr(value, "dml_S16", self)

    @property
    def dml_ID105(self):
        return self.__dml_ID105

    @dml_ID105.setter
    def dml_ID105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID105", None)
        self.__dml_ID105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_TAN104"):
                opp_val = getattr(old_value, "dml_TAN104", None)
                if opp_val == self:
                    setattr(old_value, "dml_TAN104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_TAN104"):
                opp_val = getattr(value, "dml_TAN104", None)
                setattr(value, "dml_TAN104", self)

    @property
    def dml_ID66(self):
        return self.__dml_ID66

    @dml_ID66.setter
    def dml_ID66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID66", None)
        self.__dml_ID66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_DI65"):
                opp_val = getattr(old_value, "dml_DI65", None)
                if opp_val == self:
                    setattr(old_value, "dml_DI65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_DI65"):
                opp_val = getattr(value, "dml_DI65", None)
                setattr(value, "dml_DI65", self)

    @property
    def dml_ID61(self):
        return self.__dml_ID61

    @dml_ID61.setter
    def dml_ID61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_ID__dml_ID61", None)
        self.__dml_ID61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FP60"):
                opp_val = getattr(old_value, "dml_FP60", None)
                if opp_val == self:
                    setattr(old_value, "dml_FP60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FP60"):
                opp_val = getattr(value, "dml_FP60", None)
                setattr(value, "dml_FP60", self)

class dml_S:

    def __init__(self, src: str, cwd: str, dml_S16: "dml_ID" = None, dml_S19: "dml_E" = None, dml_S: "dml_D" = None, dml_S12: "dml_F" = None, dml_S39: set["dml_DI"] = None, dml_S41: "dml_FC" = None, dml_S43: "dml_DI" = None, dml_S21: "dml_BS" = None, dml_S46: set["dml_E"] = None, dml_S23: "dml_BS" = None, dml_S26: "dml_FP" = None, dml_S28: "dml_PARFORPARAMS" = None, dml_S30: "dml_BS" = None, dml_S33: "dml_FP" = None, dml_S36: "dml_E" = None, dml_S55: "dml_BS" = None, dml_S58: "dml_BS" = None):
        self.src = src
        self.cwd = cwd
        self.dml_S16 = dml_S16
        self.dml_S19 = dml_S19
        self.dml_S = dml_S
        self.dml_S12 = dml_S12
        self.dml_S39 = dml_S39 if dml_S39 is not None else set()
        self.dml_S41 = dml_S41
        self.dml_S43 = dml_S43
        self.dml_S21 = dml_S21
        self.dml_S46 = dml_S46 if dml_S46 is not None else set()
        self.dml_S23 = dml_S23
        self.dml_S26 = dml_S26
        self.dml_S28 = dml_S28
        self.dml_S30 = dml_S30
        self.dml_S33 = dml_S33
        self.dml_S36 = dml_S36
        self.dml_S55 = dml_S55
        self.dml_S58 = dml_S58
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def cwd(self) -> str:
        return self.__cwd

    @cwd.setter
    def cwd(self, cwd: str):
        self.__cwd = cwd

    @property
    def dml_S16(self):
        return self.__dml_S16

    @dml_S16.setter
    def dml_S16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S16", None)
        self.__dml_S16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_ID17"):
                opp_val = getattr(old_value, "dml_ID17", None)
                if opp_val == self:
                    setattr(old_value, "dml_ID17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_ID17"):
                opp_val = getattr(value, "dml_ID17", None)
                setattr(value, "dml_ID17", self)

    @property
    def dml_S58(self):
        return self.__dml_S58

    @dml_S58.setter
    def dml_S58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S58", None)
        self.__dml_S58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_BS57"):
                opp_val = getattr(old_value, "dml_BS57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_BS57"):
                opp_val = getattr(value, "dml_BS57", None)
                if opp_val is None:
                    setattr(value, "dml_BS57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dml_S23(self):
        return self.__dml_S23

    @dml_S23.setter
    def dml_S23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S23", None)
        self.__dml_S23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_BS24"):
                opp_val = getattr(old_value, "dml_BS24", None)
                if opp_val == self:
                    setattr(old_value, "dml_BS24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_BS24"):
                opp_val = getattr(value, "dml_BS24", None)
                setattr(value, "dml_BS24", self)

    @property
    def dml_S55(self):
        return self.__dml_S55

    @dml_S55.setter
    def dml_S55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S55", None)
        self.__dml_S55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_BS54"):
                opp_val = getattr(old_value, "dml_BS54", None)
                if opp_val == self:
                    setattr(old_value, "dml_BS54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_BS54"):
                opp_val = getattr(value, "dml_BS54", None)
                setattr(value, "dml_BS54", self)

    @property
    def dml_S41(self):
        return self.__dml_S41

    @dml_S41.setter
    def dml_S41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S41", None)
        self.__dml_S41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FC"):
                opp_val = getattr(old_value, "dml_FC", None)
                if opp_val == self:
                    setattr(old_value, "dml_FC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FC"):
                opp_val = getattr(value, "dml_FC", None)
                setattr(value, "dml_FC", self)

    @property
    def dml_S(self):
        return self.__dml_S

    @dml_S.setter
    def dml_S(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S", None)
        self.__dml_S = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_D2"):
                opp_val = getattr(old_value, "dml_D2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_D2"):
                opp_val = getattr(value, "dml_D2", None)
                if opp_val is None:
                    setattr(value, "dml_D2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dml_S12(self):
        return self.__dml_S12

    @dml_S12.setter
    def dml_S12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S12", None)
        self.__dml_S12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_F11"):
                opp_val = getattr(old_value, "dml_F11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_F11"):
                opp_val = getattr(value, "dml_F11", None)
                if opp_val is None:
                    setattr(value, "dml_F11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dml_S30(self):
        return self.__dml_S30

    @dml_S30.setter
    def dml_S30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S30", None)
        self.__dml_S30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_BS31"):
                opp_val = getattr(old_value, "dml_BS31", None)
                if opp_val == self:
                    setattr(old_value, "dml_BS31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_BS31"):
                opp_val = getattr(value, "dml_BS31", None)
                setattr(value, "dml_BS31", self)

    @property
    def dml_S28(self):
        return self.__dml_S28

    @dml_S28.setter
    def dml_S28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S28", None)
        self.__dml_S28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_PARFORPARAMS"):
                opp_val = getattr(old_value, "dml_PARFORPARAMS", None)
                if opp_val == self:
                    setattr(old_value, "dml_PARFORPARAMS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_PARFORPARAMS"):
                opp_val = getattr(value, "dml_PARFORPARAMS", None)
                setattr(value, "dml_PARFORPARAMS", self)

    @property
    def dml_S39(self):
        return self.__dml_S39

    @dml_S39.setter
    def dml_S39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S39", None)
        self.__dml_S39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dml_DI"):
                    opp_val = getattr(item, "dml_DI", None)
                    
                    if opp_val == self:
                        setattr(item, "dml_DI", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dml_DI"):
                    opp_val = getattr(item, "dml_DI", None)
                    
                    setattr(item, "dml_DI", self)
                    

    @property
    def dml_S36(self):
        return self.__dml_S36

    @dml_S36.setter
    def dml_S36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S36", None)
        self.__dml_S36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_E37"):
                opp_val = getattr(old_value, "dml_E37", None)
                if opp_val == self:
                    setattr(old_value, "dml_E37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_E37"):
                opp_val = getattr(value, "dml_E37", None)
                setattr(value, "dml_E37", self)

    @property
    def dml_S21(self):
        return self.__dml_S21

    @dml_S21.setter
    def dml_S21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S21", None)
        self.__dml_S21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_BS"):
                opp_val = getattr(old_value, "dml_BS", None)
                if opp_val == self:
                    setattr(old_value, "dml_BS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_BS"):
                opp_val = getattr(value, "dml_BS", None)
                setattr(value, "dml_BS", self)

    @property
    def dml_S43(self):
        return self.__dml_S43

    @dml_S43.setter
    def dml_S43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S43", None)
        self.__dml_S43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_DI44"):
                opp_val = getattr(old_value, "dml_DI44", None)
                if opp_val == self:
                    setattr(old_value, "dml_DI44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_DI44"):
                opp_val = getattr(value, "dml_DI44", None)
                setattr(value, "dml_DI44", self)

    @property
    def dml_S26(self):
        return self.__dml_S26

    @dml_S26.setter
    def dml_S26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S26", None)
        self.__dml_S26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FP"):
                opp_val = getattr(old_value, "dml_FP", None)
                if opp_val == self:
                    setattr(old_value, "dml_FP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FP"):
                opp_val = getattr(value, "dml_FP", None)
                setattr(value, "dml_FP", self)

    @property
    def dml_S33(self):
        return self.__dml_S33

    @dml_S33.setter
    def dml_S33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S33", None)
        self.__dml_S33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_FP34"):
                opp_val = getattr(old_value, "dml_FP34", None)
                if opp_val == self:
                    setattr(old_value, "dml_FP34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_FP34"):
                opp_val = getattr(value, "dml_FP34", None)
                setattr(value, "dml_FP34", self)

    @property
    def dml_S46(self):
        return self.__dml_S46

    @dml_S46.setter
    def dml_S46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S46", None)
        self.__dml_S46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dml_E47"):
                    opp_val = getattr(item, "dml_E47", None)
                    
                    if opp_val == self:
                        setattr(item, "dml_E47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dml_E47"):
                    opp_val = getattr(item, "dml_E47", None)
                    
                    setattr(item, "dml_E47", self)
                    

    @property
    def dml_S19(self):
        return self.__dml_S19

    @dml_S19.setter
    def dml_S19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_S__dml_S19", None)
        self.__dml_S19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_E"):
                opp_val = getattr(old_value, "dml_E", None)
                if opp_val == self:
                    setattr(old_value, "dml_E", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_E"):
                opp_val = getattr(value, "dml_E", None)
                setattr(value, "dml_E", self)

class dml_E:

    def __init__(self, op: str, dml_E: "dml_S" = None, dml_E47: "dml_S" = None, dml_E37: "dml_S" = None, dml_E75: "dml_IS" = None, dml_E78: "dml_IS" = None, dml_E82: "dml_EObject" = None, dml_E85: "dml_E" = None, dml_E83: "dml_E" = None, dml_E87: "dml_TE" = None, dml_E102: "dml_PE" = None):
        self.op = op
        self.dml_E = dml_E
        self.dml_E47 = dml_E47
        self.dml_E37 = dml_E37
        self.dml_E75 = dml_E75
        self.dml_E78 = dml_E78
        self.dml_E82 = dml_E82
        self.dml_E85 = dml_E85
        self.dml_E83 = dml_E83
        self.dml_E87 = dml_E87
        self.dml_E102 = dml_E102
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def dml_E37(self):
        return self.__dml_E37

    @dml_E37.setter
    def dml_E37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E37", None)
        self.__dml_E37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S36"):
                opp_val = getattr(old_value, "dml_S36", None)
                if opp_val == self:
                    setattr(old_value, "dml_S36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S36"):
                opp_val = getattr(value, "dml_S36", None)
                setattr(value, "dml_S36", self)

    @property
    def dml_E47(self):
        return self.__dml_E47

    @dml_E47.setter
    def dml_E47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E47", None)
        self.__dml_E47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S46"):
                opp_val = getattr(old_value, "dml_S46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S46"):
                opp_val = getattr(value, "dml_S46", None)
                if opp_val is None:
                    setattr(value, "dml_S46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dml_E102(self):
        return self.__dml_E102

    @dml_E102.setter
    def dml_E102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E102", None)
        self.__dml_E102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_PE101"):
                opp_val = getattr(old_value, "dml_PE101", None)
                if opp_val == self:
                    setattr(old_value, "dml_PE101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_PE101"):
                opp_val = getattr(value, "dml_PE101", None)
                setattr(value, "dml_PE101", self)

    @property
    def dml_E78(self):
        return self.__dml_E78

    @dml_E78.setter
    def dml_E78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E78", None)
        self.__dml_E78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_IS77"):
                opp_val = getattr(old_value, "dml_IS77", None)
                if opp_val == self:
                    setattr(old_value, "dml_IS77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_IS77"):
                opp_val = getattr(value, "dml_IS77", None)
                setattr(value, "dml_IS77", self)

    @property
    def dml_E83(self):
        return self.__dml_E83

    @dml_E83.setter
    def dml_E83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E83", None)
        self.__dml_E83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_E85"):
                opp_val = getattr(old_value, "dml_E85", None)
                if opp_val == self:
                    setattr(old_value, "dml_E85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_E85"):
                opp_val = getattr(value, "dml_E85", None)
                setattr(value, "dml_E85", self)

    @property
    def dml_E85(self):
        return self.__dml_E85

    @dml_E85.setter
    def dml_E85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E85", None)
        self.__dml_E85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_E83"):
                opp_val = getattr(old_value, "dml_E83", None)
                if opp_val == self:
                    setattr(old_value, "dml_E83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_E83"):
                opp_val = getattr(value, "dml_E83", None)
                setattr(value, "dml_E83", self)

    @property
    def dml_E87(self):
        return self.__dml_E87

    @dml_E87.setter
    def dml_E87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E87", None)
        self.__dml_E87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_TE"):
                opp_val = getattr(old_value, "dml_TE", None)
                if opp_val == self:
                    setattr(old_value, "dml_TE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_TE"):
                opp_val = getattr(value, "dml_TE", None)
                setattr(value, "dml_TE", self)

    @property
    def dml_E82(self):
        return self.__dml_E82

    @dml_E82.setter
    def dml_E82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E82", None)
        self.__dml_E82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_EObject"):
                opp_val = getattr(old_value, "dml_EObject", None)
                if opp_val == self:
                    setattr(old_value, "dml_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_EObject"):
                opp_val = getattr(value, "dml_EObject", None)
                setattr(value, "dml_EObject", self)

    @property
    def dml_E(self):
        return self.__dml_E

    @dml_E.setter
    def dml_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E", None)
        self.__dml_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_S19"):
                opp_val = getattr(old_value, "dml_S19", None)
                if opp_val == self:
                    setattr(old_value, "dml_S19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_S19"):
                opp_val = getattr(value, "dml_S19", None)
                setattr(value, "dml_S19", self)

    @property
    def dml_E75(self):
        return self.__dml_E75

    @dml_E75.setter
    def dml_E75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dml_E__dml_E75", None)
        self.__dml_E75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dml_IS74"):
                opp_val = getattr(old_value, "dml_IS74", None)
                if opp_val == self:
                    setattr(old_value, "dml_IS74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dml_IS74"):
                opp_val = getattr(value, "dml_IS74", None)
                setattr(value, "dml_IS74", self)

class dml_F:

    pass
class dml_D:

    pass