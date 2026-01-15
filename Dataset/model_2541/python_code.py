from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fastfst_vOutList:

    def __init__(self, name: str, value: str, fastfst_vOutList: "fastfst_ModelFastfst" = None):
        self.name = name
        self.value = value
        self.fastfst_vOutList = fastfst_vOutList
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_vOutList(self):
        return self.__fastfst_vOutList

    @fastfst_vOutList.setter
    def fastfst_vOutList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_vOutList__fastfst_vOutList", None)
        self.__fastfst_vOutList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst318"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst318", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst318"):
                opp_val = getattr(value, "fastfst_ModelFastfst318", None)
                setattr(value, "fastfst_ModelFastfst318", self)

class fastfst_aBldGagNd:

    def __init__(self, value: str, name: str, fastfst_aBldGagNd: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_aBldGagNd = fastfst_aBldGagNd
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_aBldGagNd(self):
        return self.__fastfst_aBldGagNd

    @fastfst_aBldGagNd.setter
    def fastfst_aBldGagNd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_aBldGagNd__fastfst_aBldGagNd", None)
        self.__fastfst_aBldGagNd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst316"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst316", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst316"):
                opp_val = getattr(value, "fastfst_ModelFastfst316", None)
                setattr(value, "fastfst_ModelFastfst316", self)

class fastfst_iNBlGages:

    def __init__(self, value: int, name: str, fastfst_iNBlGages: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iNBlGages = fastfst_iNBlGages
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iNBlGages(self):
        return self.__fastfst_iNBlGages

    @fastfst_iNBlGages.setter
    def fastfst_iNBlGages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iNBlGages__fastfst_iNBlGages", None)
        self.__fastfst_iNBlGages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst314"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst314", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst314"):
                opp_val = getattr(value, "fastfst_ModelFastfst314", None)
                setattr(value, "fastfst_ModelFastfst314", self)

class fastfst_aTwrGagNd:

    def __init__(self, value: str, name: str, fastfst_aTwrGagNd: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_aTwrGagNd = fastfst_aTwrGagNd
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_aTwrGagNd(self):
        return self.__fastfst_aTwrGagNd

    @fastfst_aTwrGagNd.setter
    def fastfst_aTwrGagNd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_aTwrGagNd__fastfst_aTwrGagNd", None)
        self.__fastfst_aTwrGagNd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst312"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst312", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst312"):
                opp_val = getattr(value, "fastfst_ModelFastfst312", None)
                setattr(value, "fastfst_ModelFastfst312", self)

class fastfst_iNTwGages:

    def __init__(self, value: int, name: str, fastfst_iNTwGages: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iNTwGages = fastfst_iNTwGages
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iNTwGages(self):
        return self.__fastfst_iNTwGages

    @fastfst_iNTwGages.setter
    def fastfst_iNTwGages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iNTwGages__fastfst_iNTwGages", None)
        self.__fastfst_iNTwGages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst310"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst310", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst310"):
                opp_val = getattr(value, "fastfst_ModelFastfst310", None)
                setattr(value, "fastfst_ModelFastfst310", self)

class fastfst_nShftGagL:

    def __init__(self, value: float, name: str, fastfst_nShftGagL: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nShftGagL = fastfst_nShftGagL
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nShftGagL(self):
        return self.__fastfst_nShftGagL

    @fastfst_nShftGagL.setter
    def fastfst_nShftGagL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nShftGagL__fastfst_nShftGagL", None)
        self.__fastfst_nShftGagL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst308"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst308", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst308"):
                opp_val = getattr(value, "fastfst_ModelFastfst308", None)
                setattr(value, "fastfst_ModelFastfst308", self)

class fastfst_nNcIMUzn:

    def __init__(self, value: float, name: str, fastfst_nNcIMUzn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNcIMUzn = fastfst_nNcIMUzn
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNcIMUzn(self):
        return self.__fastfst_nNcIMUzn

    @fastfst_nNcIMUzn.setter
    def fastfst_nNcIMUzn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNcIMUzn__fastfst_nNcIMUzn", None)
        self.__fastfst_nNcIMUzn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst306"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst306", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst306"):
                opp_val = getattr(value, "fastfst_ModelFastfst306", None)
                setattr(value, "fastfst_ModelFastfst306", self)

class fastfst_nNcIMUyn:

    def __init__(self, value: float, name: str, fastfst_nNcIMUyn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNcIMUyn = fastfst_nNcIMUyn
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNcIMUyn(self):
        return self.__fastfst_nNcIMUyn

    @fastfst_nNcIMUyn.setter
    def fastfst_nNcIMUyn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNcIMUyn__fastfst_nNcIMUyn", None)
        self.__fastfst_nNcIMUyn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst304"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst304", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst304"):
                opp_val = getattr(value, "fastfst_ModelFastfst304", None)
                setattr(value, "fastfst_ModelFastfst304", self)

class fastfst_nNcIMUxn:

    def __init__(self, value: float, name: str, fastfst_nNcIMUxn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNcIMUxn = fastfst_nNcIMUxn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nNcIMUxn(self):
        return self.__fastfst_nNcIMUxn

    @fastfst_nNcIMUxn.setter
    def fastfst_nNcIMUxn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNcIMUxn__fastfst_nNcIMUxn", None)
        self.__fastfst_nNcIMUxn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst302"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst302", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst302"):
                opp_val = getattr(value, "fastfst_ModelFastfst302", None)
                setattr(value, "fastfst_ModelFastfst302", self)

class fastfst_nSttsTime:

    def __init__(self, value: float, name: str, fastfst_nSttsTime: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSttsTime = fastfst_nSttsTime
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nSttsTime(self):
        return self.__fastfst_nSttsTime

    @fastfst_nSttsTime.setter
    def fastfst_nSttsTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSttsTime__fastfst_nSttsTime", None)
        self.__fastfst_nSttsTime = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst300"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst300", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst300"):
                opp_val = getattr(value, "fastfst_ModelFastfst300", None)
                setattr(value, "fastfst_ModelFastfst300", self)

class fastfst_iDecFact:

    def __init__(self, value: int, name: str, fastfst_iDecFact: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iDecFact = fastfst_iDecFact
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iDecFact(self):
        return self.__fastfst_iDecFact

    @fastfst_iDecFact.setter
    def fastfst_iDecFact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iDecFact__fastfst_iDecFact", None)
        self.__fastfst_iDecFact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst298"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst298", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst298"):
                opp_val = getattr(value, "fastfst_ModelFastfst298", None)
                setattr(value, "fastfst_ModelFastfst298", self)

class fastfst_nTStart:

    def __init__(self, value: float, name: str, fastfst_nTStart: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTStart = fastfst_nTStart
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTStart(self):
        return self.__fastfst_nTStart

    @fastfst_nTStart.setter
    def fastfst_nTStart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTStart__fastfst_nTStart", None)
        self.__fastfst_nTStart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst296"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst296", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst296"):
                opp_val = getattr(value, "fastfst_ModelFastfst296", None)
                setattr(value, "fastfst_ModelFastfst296", self)

class fastfst_sOutFmt:

    def __init__(self, value: str, name: str, fastfst_sOutFmt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_sOutFmt = fastfst_sOutFmt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_sOutFmt(self):
        return self.__fastfst_sOutFmt

    @fastfst_sOutFmt.setter
    def fastfst_sOutFmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_sOutFmt__fastfst_sOutFmt", None)
        self.__fastfst_sOutFmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst294"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst294", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst294"):
                opp_val = getattr(value, "fastfst_ModelFastfst294", None)
                setattr(value, "fastfst_ModelFastfst294", self)

class fastfst_bTabDelim:

    def __init__(self, value: bool, name: str, fastfst_bTabDelim: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTabDelim = fastfst_bTabDelim
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bTabDelim(self):
        return self.__fastfst_bTabDelim

    @fastfst_bTabDelim.setter
    def fastfst_bTabDelim(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTabDelim__fastfst_bTabDelim", None)
        self.__fastfst_bTabDelim = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst292"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst292", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst292"):
                opp_val = getattr(value, "fastfst_ModelFastfst292", None)
                setattr(value, "fastfst_ModelFastfst292", self)

class fastfst_bOutFileFmt:

    def __init__(self, value: float, name: str, fastfst_bOutFileFmt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bOutFileFmt = fastfst_bOutFileFmt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_bOutFileFmt(self):
        return self.__fastfst_bOutFileFmt

    @fastfst_bOutFileFmt.setter
    def fastfst_bOutFileFmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bOutFileFmt__fastfst_bOutFileFmt", None)
        self.__fastfst_bOutFileFmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst290"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst290", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst290"):
                opp_val = getattr(value, "fastfst_ModelFastfst290", None)
                setattr(value, "fastfst_ModelFastfst290", self)

class fastfst_bSumPrint:

    def __init__(self, value: bool, name: str, fastfst_bSumPrint: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bSumPrint = fastfst_bSumPrint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bSumPrint(self):
        return self.__fastfst_bSumPrint

    @fastfst_bSumPrint.setter
    def fastfst_bSumPrint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bSumPrint__fastfst_bSumPrint", None)
        self.__fastfst_bSumPrint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst288"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst288", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst288"):
                opp_val = getattr(value, "fastfst_ModelFastfst288", None)
                setattr(value, "fastfst_ModelFastfst288", self)

class fastfst_fLinFile:

    def __init__(self, value: str, name: str, fastfst_fLinFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fLinFile = fastfst_fLinFile
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_fLinFile(self):
        return self.__fastfst_fLinFile

    @fastfst_fLinFile.setter
    def fastfst_fLinFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fLinFile__fastfst_fLinFile", None)
        self.__fastfst_fLinFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst286"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst286", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst286"):
                opp_val = getattr(value, "fastfst_ModelFastfst286", None)
                setattr(value, "fastfst_ModelFastfst286", self)

class fastfst_fADAMSFile:

    def __init__(self, value: str, name: str, fastfst_fADAMSFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fADAMSFile = fastfst_fADAMSFile
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_fADAMSFile(self):
        return self.__fastfst_fADAMSFile

    @fastfst_fADAMSFile.setter
    def fastfst_fADAMSFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fADAMSFile__fastfst_fADAMSFile", None)
        self.__fastfst_fADAMSFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst284"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst284", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst284"):
                opp_val = getattr(value, "fastfst_ModelFastfst284", None)
                setattr(value, "fastfst_ModelFastfst284", self)

class fastfst_fNoiseFile:

    def __init__(self, value: str, name: str, fastfst_fNoiseFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fNoiseFile = fastfst_fNoiseFile
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fNoiseFile(self):
        return self.__fastfst_fNoiseFile

    @fastfst_fNoiseFile.setter
    def fastfst_fNoiseFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fNoiseFile__fastfst_fNoiseFile", None)
        self.__fastfst_fNoiseFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst282"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst282", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst282"):
                opp_val = getattr(value, "fastfst_ModelFastfst282", None)
                setattr(value, "fastfst_ModelFastfst282", self)

class fastfst_fADFile:

    def __init__(self, value: str, name: str, fastfst_fADFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fADFile = fastfst_fADFile
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_fADFile(self):
        return self.__fastfst_fADFile

    @fastfst_fADFile.setter
    def fastfst_fADFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fADFile__fastfst_fADFile", None)
        self.__fastfst_fADFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst280"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst280", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst280"):
                opp_val = getattr(value, "fastfst_ModelFastfst280", None)
                setattr(value, "fastfst_ModelFastfst280", self)

class fastfst_fBldFile_3_:

    def __init__(self, value: str, name: str, fastfst_fBldFile_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fBldFile_3_ = fastfst_fBldFile_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fBldFile_3_(self):
        return self.__fastfst_fBldFile_3_

    @fastfst_fBldFile_3_.setter
    def fastfst_fBldFile_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fBldFile_3___fastfst_fBldFile_3_", None)
        self.__fastfst_fBldFile_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst278"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst278", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst278"):
                opp_val = getattr(value, "fastfst_ModelFastfst278", None)
                setattr(value, "fastfst_ModelFastfst278", self)

class fastfst_fBldFile_2_:

    def __init__(self, value: str, name: str, fastfst_fBldFile_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fBldFile_2_ = fastfst_fBldFile_2_
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_fBldFile_2_(self):
        return self.__fastfst_fBldFile_2_

    @fastfst_fBldFile_2_.setter
    def fastfst_fBldFile_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fBldFile_2___fastfst_fBldFile_2_", None)
        self.__fastfst_fBldFile_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst276"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst276", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst276"):
                opp_val = getattr(value, "fastfst_ModelFastfst276", None)
                setattr(value, "fastfst_ModelFastfst276", self)

class fastfst_fBldFile_1_:

    def __init__(self, value: str, name: str, fastfst_fBldFile_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fBldFile_1_ = fastfst_fBldFile_1_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fBldFile_1_(self):
        return self.__fastfst_fBldFile_1_

    @fastfst_fBldFile_1_.setter
    def fastfst_fBldFile_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fBldFile_1___fastfst_fBldFile_1_", None)
        self.__fastfst_fBldFile_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst274"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst274", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst274"):
                opp_val = getattr(value, "fastfst_ModelFastfst274", None)
                setattr(value, "fastfst_ModelFastfst274", self)

class fastfst_nTpBrDT:

    def __init__(self, value: float, name: str, fastfst_nTpBrDT: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTpBrDT = fastfst_nTpBrDT
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTpBrDT(self):
        return self.__fastfst_nTpBrDT

    @fastfst_nTpBrDT.setter
    def fastfst_nTpBrDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTpBrDT__fastfst_nTpBrDT", None)
        self.__fastfst_nTpBrDT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst272"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst272", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst272"):
                opp_val = getattr(value, "fastfst_ModelFastfst272", None)
                setattr(value, "fastfst_ModelFastfst272", self)

class fastfst_nTBDrConD:

    def __init__(self, value: float, name: str, fastfst_nTBDrConD: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTBDrConD = fastfst_nTBDrConD
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTBDrConD(self):
        return self.__fastfst_nTBDrConD

    @fastfst_nTBDrConD.setter
    def fastfst_nTBDrConD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTBDrConD__fastfst_nTBDrConD", None)
        self.__fastfst_nTBDrConD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst270"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst270", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst270"):
                opp_val = getattr(value, "fastfst_ModelFastfst270", None)
                setattr(value, "fastfst_ModelFastfst270", self)

class fastfst_nTBDrConN:

    def __init__(self, value: float, name: str, fastfst_nTBDrConN: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTBDrConN = fastfst_nTBDrConN
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTBDrConN(self):
        return self.__fastfst_nTBDrConN

    @fastfst_nTBDrConN.setter
    def fastfst_nTBDrConN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTBDrConN__fastfst_nTBDrConN", None)
        self.__fastfst_nTBDrConN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst268"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst268", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst268"):
                opp_val = getattr(value, "fastfst_ModelFastfst268", None)
                setattr(value, "fastfst_ModelFastfst268", self)

class fastfst_nTeetHSSp:

    def __init__(self, value: float, name: str, fastfst_nTeetHSSp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetHSSp = fastfst_nTeetHSSp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTeetHSSp(self):
        return self.__fastfst_nTeetHSSp

    @fastfst_nTeetHSSp.setter
    def fastfst_nTeetHSSp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetHSSp__fastfst_nTeetHSSp", None)
        self.__fastfst_nTeetHSSp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst266"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst266", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst266"):
                opp_val = getattr(value, "fastfst_ModelFastfst266", None)
                setattr(value, "fastfst_ModelFastfst266", self)

class fastfst_nTeetSSSp:

    def __init__(self, value: float, name: str, fastfst_nTeetSSSp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetSSSp = fastfst_nTeetSSSp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTeetSSSp(self):
        return self.__fastfst_nTeetSSSp

    @fastfst_nTeetSSSp.setter
    def fastfst_nTeetSSSp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetSSSp__fastfst_nTeetSSSp", None)
        self.__fastfst_nTeetSSSp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst264"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst264", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst264"):
                opp_val = getattr(value, "fastfst_ModelFastfst264", None)
                setattr(value, "fastfst_ModelFastfst264", self)

class fastfst_nTeetHStP:

    def __init__(self, value: float, name: str, fastfst_nTeetHStP: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetHStP = fastfst_nTeetHStP
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTeetHStP(self):
        return self.__fastfst_nTeetHStP

    @fastfst_nTeetHStP.setter
    def fastfst_nTeetHStP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetHStP__fastfst_nTeetHStP", None)
        self.__fastfst_nTeetHStP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst262"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst262", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst262"):
                opp_val = getattr(value, "fastfst_ModelFastfst262", None)
                setattr(value, "fastfst_ModelFastfst262", self)

class fastfst_nTeetSStP:

    def __init__(self, value: float, name: str, fastfst_nTeetSStP: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetSStP = fastfst_nTeetSStP
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTeetSStP(self):
        return self.__fastfst_nTeetSStP

    @fastfst_nTeetSStP.setter
    def fastfst_nTeetSStP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetSStP__fastfst_nTeetSStP", None)
        self.__fastfst_nTeetSStP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst260"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst260", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst260"):
                opp_val = getattr(value, "fastfst_ModelFastfst260", None)
                setattr(value, "fastfst_ModelFastfst260", self)

class fastfst_nTeetCDmp:

    def __init__(self, value: float, name: str, fastfst_nTeetCDmp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetCDmp = fastfst_nTeetCDmp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTeetCDmp(self):
        return self.__fastfst_nTeetCDmp

    @fastfst_nTeetCDmp.setter
    def fastfst_nTeetCDmp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetCDmp__fastfst_nTeetCDmp", None)
        self.__fastfst_nTeetCDmp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst258"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst258", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst258"):
                opp_val = getattr(value, "fastfst_ModelFastfst258", None)
                setattr(value, "fastfst_ModelFastfst258", self)

class fastfst_nTeetDmp:

    def __init__(self, value: float, name: str, fastfst_nTeetDmp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetDmp = fastfst_nTeetDmp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTeetDmp(self):
        return self.__fastfst_nTeetDmp

    @fastfst_nTeetDmp.setter
    def fastfst_nTeetDmp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetDmp__fastfst_nTeetDmp", None)
        self.__fastfst_nTeetDmp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst256"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst256", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst256"):
                opp_val = getattr(value, "fastfst_ModelFastfst256", None)
                setattr(value, "fastfst_ModelFastfst256", self)

class fastfst_nTeetDmpP:

    def __init__(self, value: float, name: str, fastfst_nTeetDmpP: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetDmpP = fastfst_nTeetDmpP
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTeetDmpP(self):
        return self.__fastfst_nTeetDmpP

    @fastfst_nTeetDmpP.setter
    def fastfst_nTeetDmpP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetDmpP__fastfst_nTeetDmpP", None)
        self.__fastfst_nTeetDmpP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst254"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst254", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst254"):
                opp_val = getattr(value, "fastfst_ModelFastfst254", None)
                setattr(value, "fastfst_ModelFastfst254", self)

class fastfst_iTeetMod:

    def __init__(self, value: int, name: str, fastfst_iTeetMod: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iTeetMod = fastfst_iTeetMod
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iTeetMod(self):
        return self.__fastfst_iTeetMod

    @fastfst_iTeetMod.setter
    def fastfst_iTeetMod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iTeetMod__fastfst_iTeetMod", None)
        self.__fastfst_iTeetMod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst252"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst252", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst252"):
                opp_val = getattr(value, "fastfst_ModelFastfst252", None)
                setattr(value, "fastfst_ModelFastfst252", self)

class fastfst_fFurlFile:

    def __init__(self, value: str, name: str, fastfst_fFurlFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fFurlFile = fastfst_fFurlFile
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fFurlFile(self):
        return self.__fastfst_fFurlFile

    @fastfst_fFurlFile.setter
    def fastfst_fFurlFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fFurlFile__fastfst_fFurlFile", None)
        self.__fastfst_fFurlFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst250"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst250", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst250"):
                opp_val = getattr(value, "fastfst_ModelFastfst250", None)
                setattr(value, "fastfst_ModelFastfst250", self)

class fastfst_bFurling:

    def __init__(self, value: bool, name: str, fastfst_bFurling: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bFurling = fastfst_bFurling
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bFurling(self):
        return self.__fastfst_bFurling

    @fastfst_bFurling.setter
    def fastfst_bFurling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bFurling__fastfst_bFurling", None)
        self.__fastfst_bFurling = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst248"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst248", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst248"):
                opp_val = getattr(value, "fastfst_ModelFastfst248", None)
                setattr(value, "fastfst_ModelFastfst248", self)

class fastfst_nYawNeut:

    def __init__(self, value: float, name: str, fastfst_nYawNeut: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nYawNeut = fastfst_nYawNeut
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nYawNeut(self):
        return self.__fastfst_nYawNeut

    @fastfst_nYawNeut.setter
    def fastfst_nYawNeut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nYawNeut__fastfst_nYawNeut", None)
        self.__fastfst_nYawNeut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst246"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst246", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst246"):
                opp_val = getattr(value, "fastfst_ModelFastfst246", None)
                setattr(value, "fastfst_ModelFastfst246", self)

class fastfst_nYawDamp:

    def __init__(self, value: float, name: str, fastfst_nYawDamp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nYawDamp = fastfst_nYawDamp
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nYawDamp(self):
        return self.__fastfst_nYawDamp

    @fastfst_nYawDamp.setter
    def fastfst_nYawDamp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nYawDamp__fastfst_nYawDamp", None)
        self.__fastfst_nYawDamp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst244"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst244", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst244"):
                opp_val = getattr(value, "fastfst_ModelFastfst244", None)
                setattr(value, "fastfst_ModelFastfst244", self)

class fastfst_nYawSpr:

    def __init__(self, value: float, name: str, fastfst_nYawSpr: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nYawSpr = fastfst_nYawSpr
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nYawSpr(self):
        return self.__fastfst_nYawSpr

    @fastfst_nYawSpr.setter
    def fastfst_nYawSpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nYawSpr__fastfst_nYawSpr", None)
        self.__fastfst_nYawSpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst242"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst242", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst242"):
                opp_val = getattr(value, "fastfst_ModelFastfst242", None)
                setattr(value, "fastfst_ModelFastfst242", self)

class fastfst_fTwrFile:

    def __init__(self, value: str, name: str, fastfst_fTwrFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fTwrFile = fastfst_fTwrFile
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fTwrFile(self):
        return self.__fastfst_fTwrFile

    @fastfst_fTwrFile.setter
    def fastfst_fTwrFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fTwrFile__fastfst_fTwrFile", None)
        self.__fastfst_fTwrFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst240"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst240", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst240"):
                opp_val = getattr(value, "fastfst_ModelFastfst240", None)
                setattr(value, "fastfst_ModelFastfst240", self)

class fastfst_iTwrNodes:

    def __init__(self, value: int, name: str, fastfst_iTwrNodes: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iTwrNodes = fastfst_iTwrNodes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iTwrNodes(self):
        return self.__fastfst_iTwrNodes

    @fastfst_iTwrNodes.setter
    def fastfst_iTwrNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iTwrNodes__fastfst_iTwrNodes", None)
        self.__fastfst_iTwrNodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst238"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst238", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst238"):
                opp_val = getattr(value, "fastfst_ModelFastfst238", None)
                setattr(value, "fastfst_ModelFastfst238", self)

class fastfst_iPtfmModel:

    def __init__(self, value: int, name: str, fastfst_iPtfmModel: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iPtfmModel = fastfst_iPtfmModel
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iPtfmModel(self):
        return self.__fastfst_iPtfmModel

    @fastfst_iPtfmModel.setter
    def fastfst_iPtfmModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iPtfmModel__fastfst_iPtfmModel", None)
        self.__fastfst_iPtfmModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst234"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst234", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst234"):
                opp_val = getattr(value, "fastfst_ModelFastfst234", None)
                setattr(value, "fastfst_ModelFastfst234", self)

class fastfst_nTEC_MR:

    def __init__(self, value: float, name: str, fastfst_nTEC_MR: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_MR = fastfst_nTEC_MR
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTEC_MR(self):
        return self.__fastfst_nTEC_MR

    @fastfst_nTEC_MR.setter
    def fastfst_nTEC_MR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_MR__fastfst_nTEC_MR", None)
        self.__fastfst_nTEC_MR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst232"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst232", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst232"):
                opp_val = getattr(value, "fastfst_ModelFastfst232", None)
                setattr(value, "fastfst_ModelFastfst232", self)

class fastfst_nTEC_RLR:

    def __init__(self, value: float, name: str, fastfst_nTEC_RLR: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_RLR = fastfst_nTEC_RLR
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTEC_RLR(self):
        return self.__fastfst_nTEC_RLR

    @fastfst_nTEC_RLR.setter
    def fastfst_nTEC_RLR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_RLR__fastfst_nTEC_RLR", None)
        self.__fastfst_nTEC_RLR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst230"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst230", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst230"):
                opp_val = getattr(value, "fastfst_ModelFastfst230", None)
                setattr(value, "fastfst_ModelFastfst230", self)

class fastfst_nTEC_SLR:

    def __init__(self, value: float, name: str, fastfst_nTEC_SLR: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_SLR = fastfst_nTEC_SLR
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTEC_SLR(self):
        return self.__fastfst_nTEC_SLR

    @fastfst_nTEC_SLR.setter
    def fastfst_nTEC_SLR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_SLR__fastfst_nTEC_SLR", None)
        self.__fastfst_nTEC_SLR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst228"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst228", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst228"):
                opp_val = getattr(value, "fastfst_ModelFastfst228", None)
                setattr(value, "fastfst_ModelFastfst228", self)

class fastfst_nTEC_VLL:

    def __init__(self, value: float, name: str, fastfst_nTEC_VLL: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_VLL = fastfst_nTEC_VLL
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTEC_VLL(self):
        return self.__fastfst_nTEC_VLL

    @fastfst_nTEC_VLL.setter
    def fastfst_nTEC_VLL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_VLL__fastfst_nTEC_VLL", None)
        self.__fastfst_nTEC_VLL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst226"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst226", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst226"):
                opp_val = getattr(value, "fastfst_ModelFastfst226", None)
                setattr(value, "fastfst_ModelFastfst226", self)

class fastfst_nTEC_Rres:

    def __init__(self, value: float, name: str, fastfst_nTEC_Rres: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_Rres = fastfst_nTEC_Rres
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTEC_Rres(self):
        return self.__fastfst_nTEC_Rres

    @fastfst_nTEC_Rres.setter
    def fastfst_nTEC_Rres(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_Rres__fastfst_nTEC_Rres", None)
        self.__fastfst_nTEC_Rres = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst224"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst224", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst224"):
                opp_val = getattr(value, "fastfst_ModelFastfst224", None)
                setattr(value, "fastfst_ModelFastfst224", self)

class fastfst_nTEC_Sres:

    def __init__(self, value: float, name: str, fastfst_nTEC_Sres: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_Sres = fastfst_nTEC_Sres
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTEC_Sres(self):
        return self.__fastfst_nTEC_Sres

    @fastfst_nTEC_Sres.setter
    def fastfst_nTEC_Sres(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_Sres__fastfst_nTEC_Sres", None)
        self.__fastfst_nTEC_Sres = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst222"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst222", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst222"):
                opp_val = getattr(value, "fastfst_ModelFastfst222", None)
                setattr(value, "fastfst_ModelFastfst222", self)

class fastfst_nTEC_Npol:

    def __init__(self, value: float, name: str, fastfst_nTEC_Npol: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_Npol = fastfst_nTEC_Npol
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTEC_Npol(self):
        return self.__fastfst_nTEC_Npol

    @fastfst_nTEC_Npol.setter
    def fastfst_nTEC_Npol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_Npol__fastfst_nTEC_Npol", None)
        self.__fastfst_nTEC_Npol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst220"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst220", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst220"):
                opp_val = getattr(value, "fastfst_ModelFastfst220", None)
                setattr(value, "fastfst_ModelFastfst220", self)

class fastfst_nTEC_Freq:

    def __init__(self, value: float, name: str, fastfst_nTEC_Freq: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTEC_Freq = fastfst_nTEC_Freq
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTEC_Freq(self):
        return self.__fastfst_nTEC_Freq

    @fastfst_nTEC_Freq.setter
    def fastfst_nTEC_Freq(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTEC_Freq__fastfst_nTEC_Freq", None)
        self.__fastfst_nTEC_Freq = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst218"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst218", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst218"):
                opp_val = getattr(value, "fastfst_ModelFastfst218", None)
                setattr(value, "fastfst_ModelFastfst218", self)

class fastfst_fPtfmFile:

    def __init__(self, value: str, name: str, fastfst_fPtfmFile: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fPtfmFile = fastfst_fPtfmFile
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_fPtfmFile(self):
        return self.__fastfst_fPtfmFile

    @fastfst_fPtfmFile.setter
    def fastfst_fPtfmFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fPtfmFile__fastfst_fPtfmFile", None)
        self.__fastfst_fPtfmFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst236"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst236", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst236"):
                opp_val = getattr(value, "fastfst_ModelFastfst236", None)
                setattr(value, "fastfst_ModelFastfst236", self)

class fastfst_nSIG_PORt:

    def __init__(self, value: float, name: str, fastfst_nSIG_PORt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSIG_PORt = fastfst_nSIG_PORt
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nSIG_PORt(self):
        return self.__fastfst_nSIG_PORt

    @fastfst_nSIG_PORt.setter
    def fastfst_nSIG_PORt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSIG_PORt__fastfst_nSIG_PORt", None)
        self.__fastfst_nSIG_PORt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst216"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst216", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst216"):
                opp_val = getattr(value, "fastfst_ModelFastfst216", None)
                setattr(value, "fastfst_ModelFastfst216", self)

class fastfst_nSIG_RtTq:

    def __init__(self, value: float, name: str, fastfst_nSIG_RtTq: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSIG_RtTq = fastfst_nSIG_RtTq
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nSIG_RtTq(self):
        return self.__fastfst_nSIG_RtTq

    @fastfst_nSIG_RtTq.setter
    def fastfst_nSIG_RtTq(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSIG_RtTq__fastfst_nSIG_RtTq", None)
        self.__fastfst_nSIG_RtTq = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst214"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst214", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst214"):
                opp_val = getattr(value, "fastfst_ModelFastfst214", None)
                setattr(value, "fastfst_ModelFastfst214", self)

class fastfst_nSIG_SySp:

    def __init__(self, value: float, name: str, fastfst_nSIG_SySp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSIG_SySp = fastfst_nSIG_SySp
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nSIG_SySp(self):
        return self.__fastfst_nSIG_SySp

    @fastfst_nSIG_SySp.setter
    def fastfst_nSIG_SySp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSIG_SySp__fastfst_nSIG_SySp", None)
        self.__fastfst_nSIG_SySp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst212"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst212", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst212"):
                opp_val = getattr(value, "fastfst_ModelFastfst212", None)
                setattr(value, "fastfst_ModelFastfst212", self)

class fastfst_nSIG_SlPc:

    def __init__(self, value: float, name: str, fastfst_nSIG_SlPc: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSIG_SlPc = fastfst_nSIG_SlPc
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nSIG_SlPc(self):
        return self.__fastfst_nSIG_SlPc

    @fastfst_nSIG_SlPc.setter
    def fastfst_nSIG_SlPc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSIG_SlPc__fastfst_nSIG_SlPc", None)
        self.__fastfst_nSIG_SlPc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst210"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst210", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst210"):
                opp_val = getattr(value, "fastfst_ModelFastfst210", None)
                setattr(value, "fastfst_ModelFastfst210", self)

class fastfst_nDTTorDmp:

    def __init__(self, value: float, name: str, fastfst_nDTTorDmp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nDTTorDmp = fastfst_nDTTorDmp
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nDTTorDmp(self):
        return self.__fastfst_nDTTorDmp

    @fastfst_nDTTorDmp.setter
    def fastfst_nDTTorDmp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nDTTorDmp__fastfst_nDTTorDmp", None)
        self.__fastfst_nDTTorDmp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst208"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst208", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst208"):
                opp_val = getattr(value, "fastfst_ModelFastfst208", None)
                setattr(value, "fastfst_ModelFastfst208", self)

class fastfst_nDTTorSpr:

    def __init__(self, value: float, name: str, fastfst_nDTTorSpr: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nDTTorSpr = fastfst_nDTTorSpr
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nDTTorSpr(self):
        return self.__fastfst_nDTTorSpr

    @fastfst_nDTTorSpr.setter
    def fastfst_nDTTorSpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nDTTorSpr__fastfst_nDTTorSpr", None)
        self.__fastfst_nDTTorSpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst206"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst206", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst206"):
                opp_val = getattr(value, "fastfst_ModelFastfst206", None)
                setattr(value, "fastfst_ModelFastfst206", self)

class fastfst_fDynBrkFi:

    def __init__(self, value: str, name: str, fastfst_fDynBrkFi: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_fDynBrkFi = fastfst_fDynBrkFi
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fastfst_fDynBrkFi(self):
        return self.__fastfst_fDynBrkFi

    @fastfst_fDynBrkFi.setter
    def fastfst_fDynBrkFi(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_fDynBrkFi__fastfst_fDynBrkFi", None)
        self.__fastfst_fDynBrkFi = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst204"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst204", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst204"):
                opp_val = getattr(value, "fastfst_ModelFastfst204", None)
                setattr(value, "fastfst_ModelFastfst204", self)

class fastfst_nHSSBrDT:

    def __init__(self, value: float, name: str, fastfst_nHSSBrDT: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHSSBrDT = fastfst_nHSSBrDT
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nHSSBrDT(self):
        return self.__fastfst_nHSSBrDT

    @fastfst_nHSSBrDT.setter
    def fastfst_nHSSBrDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHSSBrDT__fastfst_nHSSBrDT", None)
        self.__fastfst_nHSSBrDT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst202"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst202", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst202"):
                opp_val = getattr(value, "fastfst_ModelFastfst202", None)
                setattr(value, "fastfst_ModelFastfst202", self)

class fastfst_nHSSBrTqF:

    def __init__(self, value: float, name: str, fastfst_nHSSBrTqF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHSSBrTqF = fastfst_nHSSBrTqF
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nHSSBrTqF(self):
        return self.__fastfst_nHSSBrTqF

    @fastfst_nHSSBrTqF.setter
    def fastfst_nHSSBrTqF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHSSBrTqF__fastfst_nHSSBrTqF", None)
        self.__fastfst_nHSSBrTqF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst200"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst200", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst200"):
                opp_val = getattr(value, "fastfst_ModelFastfst200", None)
                setattr(value, "fastfst_ModelFastfst200", self)

class fastfst_bGBRevers:

    def __init__(self, value: bool, name: str, fastfst_bGBRevers: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bGBRevers = fastfst_bGBRevers
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bGBRevers(self):
        return self.__fastfst_bGBRevers

    @fastfst_bGBRevers.setter
    def fastfst_bGBRevers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bGBRevers__fastfst_bGBRevers", None)
        self.__fastfst_bGBRevers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst198"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst198", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst198"):
                opp_val = getattr(value, "fastfst_ModelFastfst198", None)
                setattr(value, "fastfst_ModelFastfst198", self)

class fastfst_nYawBrMass:

    def __init__(self, value: float, name: str, fastfst_nYawBrMass: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nYawBrMass = fastfst_nYawBrMass
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nYawBrMass(self):
        return self.__fastfst_nYawBrMass

    @fastfst_nYawBrMass.setter
    def fastfst_nYawBrMass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nYawBrMass__fastfst_nYawBrMass", None)
        self.__fastfst_nYawBrMass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst174"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst174", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst174"):
                opp_val = getattr(value, "fastfst_ModelFastfst174", None)
                setattr(value, "fastfst_ModelFastfst174", self)

class fastfst_nGBRatio:

    def __init__(self, value: float, name: str, fastfst_nGBRatio: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nGBRatio = fastfst_nGBRatio
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nGBRatio(self):
        return self.__fastfst_nGBRatio

    @fastfst_nGBRatio.setter
    def fastfst_nGBRatio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nGBRatio__fastfst_nGBRatio", None)
        self.__fastfst_nGBRatio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst196"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst196", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst196"):
                opp_val = getattr(value, "fastfst_ModelFastfst196", None)
                setattr(value, "fastfst_ModelFastfst196", self)

class fastfst_nGenEff:

    def __init__(self, value: float, name: str, fastfst_nGenEff: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nGenEff = fastfst_nGenEff
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nGenEff(self):
        return self.__fastfst_nGenEff

    @fastfst_nGenEff.setter
    def fastfst_nGenEff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nGenEff__fastfst_nGenEff", None)
        self.__fastfst_nGenEff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst194"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst194", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst194"):
                opp_val = getattr(value, "fastfst_ModelFastfst194", None)
                setattr(value, "fastfst_ModelFastfst194", self)

class fastfst_nGBoxEff:

    def __init__(self, value: float, name: str, fastfst_nGBoxEff: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nGBoxEff = fastfst_nGBoxEff
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nGBoxEff(self):
        return self.__fastfst_nGBoxEff

    @fastfst_nGBoxEff.setter
    def fastfst_nGBoxEff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nGBoxEff__fastfst_nGBoxEff", None)
        self.__fastfst_nGBoxEff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst192"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst192", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst192"):
                opp_val = getattr(value, "fastfst_ModelFastfst192", None)
                setattr(value, "fastfst_ModelFastfst192", self)

class fastfst_nHubIner:

    def __init__(self, value: float, name: str, fastfst_nHubIner: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHubIner = fastfst_nHubIner
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nHubIner(self):
        return self.__fastfst_nHubIner

    @fastfst_nHubIner.setter
    def fastfst_nHubIner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHubIner__fastfst_nHubIner", None)
        self.__fastfst_nHubIner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst190"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst190", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst190"):
                opp_val = getattr(value, "fastfst_ModelFastfst190", None)
                setattr(value, "fastfst_ModelFastfst190", self)

class fastfst_nGenIner:

    def __init__(self, value: float, name: str, fastfst_nGenIner: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nGenIner = fastfst_nGenIner
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nGenIner(self):
        return self.__fastfst_nGenIner

    @fastfst_nGenIner.setter
    def fastfst_nGenIner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nGenIner__fastfst_nGenIner", None)
        self.__fastfst_nGenIner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst188"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst188", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst188"):
                opp_val = getattr(value, "fastfst_ModelFastfst188", None)
                setattr(value, "fastfst_ModelFastfst188", self)

class fastfst_nNacYIner:

    def __init__(self, value: float, name: str, fastfst_nNacYIner: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacYIner = fastfst_nNacYIner
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNacYIner(self):
        return self.__fastfst_nNacYIner

    @fastfst_nNacYIner.setter
    def fastfst_nNacYIner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacYIner__fastfst_nNacYIner", None)
        self.__fastfst_nNacYIner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst186"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst186", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst186"):
                opp_val = getattr(value, "fastfst_ModelFastfst186", None)
                setattr(value, "fastfst_ModelFastfst186", self)

class fastfst_nTipMass_3_:

    def __init__(self, value: float, name: str, fastfst_nTipMass_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTipMass_3_ = fastfst_nTipMass_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTipMass_3_(self):
        return self.__fastfst_nTipMass_3_

    @fastfst_nTipMass_3_.setter
    def fastfst_nTipMass_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTipMass_3___fastfst_nTipMass_3_", None)
        self.__fastfst_nTipMass_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst184"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst184", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst184"):
                opp_val = getattr(value, "fastfst_ModelFastfst184", None)
                setattr(value, "fastfst_ModelFastfst184", self)

class fastfst_nTipMass_2_:

    def __init__(self, value: float, name: str, fastfst_nTipMass_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTipMass_2_ = fastfst_nTipMass_2_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTipMass_2_(self):
        return self.__fastfst_nTipMass_2_

    @fastfst_nTipMass_2_.setter
    def fastfst_nTipMass_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTipMass_2___fastfst_nTipMass_2_", None)
        self.__fastfst_nTipMass_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst182"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst182", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst182"):
                opp_val = getattr(value, "fastfst_ModelFastfst182", None)
                setattr(value, "fastfst_ModelFastfst182", self)

class fastfst_nTipMass_1_:

    def __init__(self, value: float, name: str, fastfst_nTipMass_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTipMass_1_ = fastfst_nTipMass_1_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTipMass_1_(self):
        return self.__fastfst_nTipMass_1_

    @fastfst_nTipMass_1_.setter
    def fastfst_nTipMass_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTipMass_1___fastfst_nTipMass_1_", None)
        self.__fastfst_nTipMass_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst180"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst180", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst180"):
                opp_val = getattr(value, "fastfst_ModelFastfst180", None)
                setattr(value, "fastfst_ModelFastfst180", self)

class fastfst_nHubMass:

    def __init__(self, value: float, name: str, fastfst_nHubMass: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHubMass = fastfst_nHubMass
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nHubMass(self):
        return self.__fastfst_nHubMass

    @fastfst_nHubMass.setter
    def fastfst_nHubMass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHubMass__fastfst_nHubMass", None)
        self.__fastfst_nHubMass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst178"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst178", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst178"):
                opp_val = getattr(value, "fastfst_ModelFastfst178", None)
                setattr(value, "fastfst_ModelFastfst178", self)

class fastfst_nNacMass:

    def __init__(self, value: float, name: str, fastfst_nNacMass: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacMass = fastfst_nNacMass
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNacMass(self):
        return self.__fastfst_nNacMass

    @fastfst_nNacMass.setter
    def fastfst_nNacMass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacMass__fastfst_nNacMass", None)
        self.__fastfst_nNacMass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst176"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst176", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst176"):
                opp_val = getattr(value, "fastfst_ModelFastfst176", None)
                setattr(value, "fastfst_ModelFastfst176", self)

class fastfst_nNacCMyn:

    def __init__(self, value: float, name: str, fastfst_nNacCMyn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacCMyn = fastfst_nNacCMyn
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNacCMyn(self):
        return self.__fastfst_nNacCMyn

    @fastfst_nNacCMyn.setter
    def fastfst_nNacCMyn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacCMyn__fastfst_nNacCMyn", None)
        self.__fastfst_nNacCMyn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst152"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst152", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst152"):
                opp_val = getattr(value, "fastfst_ModelFastfst152", None)
                setattr(value, "fastfst_ModelFastfst152", self)

class fastfst_nNacCMxn:

    def __init__(self, value: float, name: str, fastfst_nNacCMxn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacCMxn = fastfst_nNacCMxn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nNacCMxn(self):
        return self.__fastfst_nNacCMxn

    @fastfst_nNacCMxn.setter
    def fastfst_nNacCMxn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacCMxn__fastfst_nNacCMxn", None)
        self.__fastfst_nNacCMxn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst150"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst150", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst150"):
                opp_val = getattr(value, "fastfst_ModelFastfst150", None)
                setattr(value, "fastfst_ModelFastfst150", self)

class fastfst_nAzimB1Up:

    def __init__(self, value: float, name: str, fastfst_nAzimB1Up: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nAzimB1Up = fastfst_nAzimB1Up
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nAzimB1Up(self):
        return self.__fastfst_nAzimB1Up

    @fastfst_nAzimB1Up.setter
    def fastfst_nAzimB1Up(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nAzimB1Up__fastfst_nAzimB1Up", None)
        self.__fastfst_nAzimB1Up = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst172"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst172", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst172"):
                opp_val = getattr(value, "fastfst_ModelFastfst172", None)
                setattr(value, "fastfst_ModelFastfst172", self)

class fastfst_nPreCone_3_:

    def __init__(self, value: float, name: str, fastfst_nPreCone_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nPreCone_3_ = fastfst_nPreCone_3_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nPreCone_3_(self):
        return self.__fastfst_nPreCone_3_

    @fastfst_nPreCone_3_.setter
    def fastfst_nPreCone_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nPreCone_3___fastfst_nPreCone_3_", None)
        self.__fastfst_nPreCone_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst170"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst170", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst170"):
                opp_val = getattr(value, "fastfst_ModelFastfst170", None)
                setattr(value, "fastfst_ModelFastfst170", self)

class fastfst_nPreCone_2_:

    def __init__(self, value: float, name: str, fastfst_nPreCone_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nPreCone_2_ = fastfst_nPreCone_2_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nPreCone_2_(self):
        return self.__fastfst_nPreCone_2_

    @fastfst_nPreCone_2_.setter
    def fastfst_nPreCone_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nPreCone_2___fastfst_nPreCone_2_", None)
        self.__fastfst_nPreCone_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst168"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst168", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst168"):
                opp_val = getattr(value, "fastfst_ModelFastfst168", None)
                setattr(value, "fastfst_ModelFastfst168", self)

class fastfst_nPreCone_1_:

    def __init__(self, value: float, name: str, fastfst_nPreCone_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nPreCone_1_ = fastfst_nPreCone_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nPreCone_1_(self):
        return self.__fastfst_nPreCone_1_

    @fastfst_nPreCone_1_.setter
    def fastfst_nPreCone_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nPreCone_1___fastfst_nPreCone_1_", None)
        self.__fastfst_nPreCone_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst166"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst166", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst166"):
                opp_val = getattr(value, "fastfst_ModelFastfst166", None)
                setattr(value, "fastfst_ModelFastfst166", self)

class fastfst_nDelta3:

    def __init__(self, value: float, name: str, fastfst_nDelta3: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nDelta3 = fastfst_nDelta3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nDelta3(self):
        return self.__fastfst_nDelta3

    @fastfst_nDelta3.setter
    def fastfst_nDelta3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nDelta3__fastfst_nDelta3", None)
        self.__fastfst_nDelta3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst164"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst164", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst164"):
                opp_val = getattr(value, "fastfst_ModelFastfst164", None)
                setattr(value, "fastfst_ModelFastfst164", self)

class fastfst_nShftTilt:

    def __init__(self, value: float, name: str, fastfst_nShftTilt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nShftTilt = fastfst_nShftTilt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nShftTilt(self):
        return self.__fastfst_nShftTilt

    @fastfst_nShftTilt.setter
    def fastfst_nShftTilt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nShftTilt__fastfst_nShftTilt", None)
        self.__fastfst_nShftTilt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst162"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst162", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst162"):
                opp_val = getattr(value, "fastfst_ModelFastfst162", None)
                setattr(value, "fastfst_ModelFastfst162", self)

class fastfst_nTwrRBHt:

    def __init__(self, value: float, name: str, fastfst_nTwrRBHt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTwrRBHt = fastfst_nTwrRBHt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTwrRBHt(self):
        return self.__fastfst_nTwrRBHt

    @fastfst_nTwrRBHt.setter
    def fastfst_nTwrRBHt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTwrRBHt__fastfst_nTwrRBHt", None)
        self.__fastfst_nTwrRBHt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst160"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst160", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst160"):
                opp_val = getattr(value, "fastfst_ModelFastfst160", None)
                setattr(value, "fastfst_ModelFastfst160", self)

class fastfst_nTwr2Shft:

    def __init__(self, value: float, name: str, fastfst_nTwr2Shft: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTwr2Shft = fastfst_nTwr2Shft
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTwr2Shft(self):
        return self.__fastfst_nTwr2Shft

    @fastfst_nTwr2Shft.setter
    def fastfst_nTwr2Shft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTwr2Shft__fastfst_nTwr2Shft", None)
        self.__fastfst_nTwr2Shft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst158"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst158", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst158"):
                opp_val = getattr(value, "fastfst_ModelFastfst158", None)
                setattr(value, "fastfst_ModelFastfst158", self)

class fastfst_nTowerHt:

    def __init__(self, value: float, name: str, fastfst_nTowerHt: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTowerHt = fastfst_nTowerHt
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTowerHt(self):
        return self.__fastfst_nTowerHt

    @fastfst_nTowerHt.setter
    def fastfst_nTowerHt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTowerHt__fastfst_nTowerHt", None)
        self.__fastfst_nTowerHt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst156"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst156", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst156"):
                opp_val = getattr(value, "fastfst_ModelFastfst156", None)
                setattr(value, "fastfst_ModelFastfst156", self)

class fastfst_nOverHang:

    def __init__(self, name: str, value: float, fastfst_nOverHang: "fastfst_ModelFastfst" = None):
        self.name = name
        self.value = value
        self.fastfst_nOverHang = fastfst_nOverHang
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nOverHang(self):
        return self.__fastfst_nOverHang

    @fastfst_nOverHang.setter
    def fastfst_nOverHang(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nOverHang__fastfst_nOverHang", None)
        self.__fastfst_nOverHang = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst148"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst148", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst148"):
                opp_val = getattr(value, "fastfst_ModelFastfst148", None)
                setattr(value, "fastfst_ModelFastfst148", self)

class fastfst_nHubCM:

    def __init__(self, value: float, name: str, fastfst_nHubCM: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHubCM = fastfst_nHubCM
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nHubCM(self):
        return self.__fastfst_nHubCM

    @fastfst_nHubCM.setter
    def fastfst_nHubCM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHubCM__fastfst_nHubCM", None)
        self.__fastfst_nHubCM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst146"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst146", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst146"):
                opp_val = getattr(value, "fastfst_ModelFastfst146", None)
                setattr(value, "fastfst_ModelFastfst146", self)

class fastfst_nNacCMzn:

    def __init__(self, value: float, name: str, fastfst_nNacCMzn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacCMzn = fastfst_nNacCMzn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nNacCMzn(self):
        return self.__fastfst_nNacCMzn

    @fastfst_nNacCMzn.setter
    def fastfst_nNacCMzn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacCMzn__fastfst_nNacCMzn", None)
        self.__fastfst_nNacCMzn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst154"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst154", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst154"):
                opp_val = getattr(value, "fastfst_ModelFastfst154", None)
                setattr(value, "fastfst_ModelFastfst154", self)

class fastfst_nUndSling:

    def __init__(self, value: float, name: str, fastfst_nUndSling: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nUndSling = fastfst_nUndSling
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nUndSling(self):
        return self.__fastfst_nUndSling

    @fastfst_nUndSling.setter
    def fastfst_nUndSling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nUndSling__fastfst_nUndSling", None)
        self.__fastfst_nUndSling = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst144"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst144", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst144"):
                opp_val = getattr(value, "fastfst_ModelFastfst144", None)
                setattr(value, "fastfst_ModelFastfst144", self)

class fastfst_nPSpnElN:

    def __init__(self, value: int, name: str, fastfst_nPSpnElN: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nPSpnElN = fastfst_nPSpnElN
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_nPSpnElN(self):
        return self.__fastfst_nPSpnElN

    @fastfst_nPSpnElN.setter
    def fastfst_nPSpnElN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nPSpnElN__fastfst_nPSpnElN", None)
        self.__fastfst_nPSpnElN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst142"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst142", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst142"):
                opp_val = getattr(value, "fastfst_ModelFastfst142", None)
                setattr(value, "fastfst_ModelFastfst142", self)

class fastfst_nHubRad:

    def __init__(self, value: float, name: str, fastfst_nHubRad: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nHubRad = fastfst_nHubRad
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nHubRad(self):
        return self.__fastfst_nHubRad

    @fastfst_nHubRad.setter
    def fastfst_nHubRad(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nHubRad__fastfst_nHubRad", None)
        self.__fastfst_nHubRad = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst140"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst140", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst140"):
                opp_val = getattr(value, "fastfst_ModelFastfst140", None)
                setattr(value, "fastfst_ModelFastfst140", self)

class fastfst_nTipRad:

    def __init__(self, value: float, name: str, fastfst_nTipRad: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTipRad = fastfst_nTipRad
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTipRad(self):
        return self.__fastfst_nTipRad

    @fastfst_nTipRad.setter
    def fastfst_nTipRad(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTipRad__fastfst_nTipRad", None)
        self.__fastfst_nTipRad = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst138"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst138", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst138"):
                opp_val = getattr(value, "fastfst_ModelFastfst138", None)
                setattr(value, "fastfst_ModelFastfst138", self)

class fastfst_nTTDspSS:

    def __init__(self, value: float, name: str, fastfst_nTTDspSS: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTTDspSS = fastfst_nTTDspSS
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTTDspSS(self):
        return self.__fastfst_nTTDspSS

    @fastfst_nTTDspSS.setter
    def fastfst_nTTDspSS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTTDspSS__fastfst_nTTDspSS", None)
        self.__fastfst_nTTDspSS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst136"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst136", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst136"):
                opp_val = getattr(value, "fastfst_ModelFastfst136", None)
                setattr(value, "fastfst_ModelFastfst136", self)

class fastfst_nTTDspFA:

    def __init__(self, value: float, name: str, fastfst_nTTDspFA: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTTDspFA = fastfst_nTTDspFA
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTTDspFA(self):
        return self.__fastfst_nTTDspFA

    @fastfst_nTTDspFA.setter
    def fastfst_nTTDspFA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTTDspFA__fastfst_nTTDspFA", None)
        self.__fastfst_nTTDspFA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst134"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst134", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst134"):
                opp_val = getattr(value, "fastfst_ModelFastfst134", None)
                setattr(value, "fastfst_ModelFastfst134", self)

class fastfst_nNacYaw:

    def __init__(self, value: float, name: str, fastfst_nNacYaw: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacYaw = fastfst_nNacYaw
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nNacYaw(self):
        return self.__fastfst_nNacYaw

    @fastfst_nNacYaw.setter
    def fastfst_nNacYaw(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacYaw__fastfst_nNacYaw", None)
        self.__fastfst_nNacYaw = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst132"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst132", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst132"):
                opp_val = getattr(value, "fastfst_ModelFastfst132", None)
                setattr(value, "fastfst_ModelFastfst132", self)

class fastfst_nTeetDefl:

    def __init__(self, value: float, name: str, fastfst_nTeetDefl: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTeetDefl = fastfst_nTeetDefl
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTeetDefl(self):
        return self.__fastfst_nTeetDefl

    @fastfst_nTeetDefl.setter
    def fastfst_nTeetDefl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTeetDefl__fastfst_nTeetDefl", None)
        self.__fastfst_nTeetDefl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst126"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst126", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst126"):
                opp_val = getattr(value, "fastfst_ModelFastfst126", None)
                setattr(value, "fastfst_ModelFastfst126", self)

class fastfst_nIPDefl:

    def __init__(self, value: float, name: str, fastfst_nIPDefl: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nIPDefl = fastfst_nIPDefl
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nIPDefl(self):
        return self.__fastfst_nIPDefl

    @fastfst_nIPDefl.setter
    def fastfst_nIPDefl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nIPDefl__fastfst_nIPDefl", None)
        self.__fastfst_nIPDefl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst124"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst124", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst124"):
                opp_val = getattr(value, "fastfst_ModelFastfst124", None)
                setattr(value, "fastfst_ModelFastfst124", self)

class fastfst_nOoPDefl:

    def __init__(self, value: float, name: str, fastfst_nOoPDefl: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nOoPDefl = fastfst_nOoPDefl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nOoPDefl(self):
        return self.__fastfst_nOoPDefl

    @fastfst_nOoPDefl.setter
    def fastfst_nOoPDefl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nOoPDefl__fastfst_nOoPDefl", None)
        self.__fastfst_nOoPDefl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst122"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst122", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst122"):
                opp_val = getattr(value, "fastfst_ModelFastfst122", None)
                setattr(value, "fastfst_ModelFastfst122", self)

class fastfst_bCompNoise:

    def __init__(self, value: bool, name: str, fastfst_bCompNoise: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bCompNoise = fastfst_bCompNoise
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bCompNoise(self):
        return self.__fastfst_bCompNoise

    @fastfst_bCompNoise.setter
    def fastfst_bCompNoise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bCompNoise__fastfst_bCompNoise", None)
        self.__fastfst_bCompNoise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst120"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst120", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst120"):
                opp_val = getattr(value, "fastfst_ModelFastfst120", None)
                setattr(value, "fastfst_ModelFastfst120", self)

class fastfst_bCompAero:

    def __init__(self, value: bool, name: str, fastfst_bCompAero: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bCompAero = fastfst_bCompAero
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bCompAero(self):
        return self.__fastfst_bCompAero

    @fastfst_bCompAero.setter
    def fastfst_bCompAero(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bCompAero__fastfst_bCompAero", None)
        self.__fastfst_bCompAero = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst118"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst118", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst118"):
                opp_val = getattr(value, "fastfst_ModelFastfst118", None)
                setattr(value, "fastfst_ModelFastfst118", self)

class fastfst_bTwSSDOF2:

    def __init__(self, value: bool, name: str, fastfst_bTwSSDOF2: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTwSSDOF2 = fastfst_bTwSSDOF2
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bTwSSDOF2(self):
        return self.__fastfst_bTwSSDOF2

    @fastfst_bTwSSDOF2.setter
    def fastfst_bTwSSDOF2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTwSSDOF2__fastfst_bTwSSDOF2", None)
        self.__fastfst_bTwSSDOF2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst116"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst116", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst116"):
                opp_val = getattr(value, "fastfst_ModelFastfst116", None)
                setattr(value, "fastfst_ModelFastfst116", self)

class fastfst_bTwSSDOF1:

    def __init__(self, value: bool, name: str, fastfst_bTwSSDOF1: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTwSSDOF1 = fastfst_bTwSSDOF1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bTwSSDOF1(self):
        return self.__fastfst_bTwSSDOF1

    @fastfst_bTwSSDOF1.setter
    def fastfst_bTwSSDOF1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTwSSDOF1__fastfst_bTwSSDOF1", None)
        self.__fastfst_bTwSSDOF1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst114"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst114", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst114"):
                opp_val = getattr(value, "fastfst_ModelFastfst114", None)
                setattr(value, "fastfst_ModelFastfst114", self)

class fastfst_nRotSpeed:

    def __init__(self, value: float, name: str, fastfst_nRotSpeed: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nRotSpeed = fastfst_nRotSpeed
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nRotSpeed(self):
        return self.__fastfst_nRotSpeed

    @fastfst_nRotSpeed.setter
    def fastfst_nRotSpeed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nRotSpeed__fastfst_nRotSpeed", None)
        self.__fastfst_nRotSpeed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst130"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst130", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst130"):
                opp_val = getattr(value, "fastfst_ModelFastfst130", None)
                setattr(value, "fastfst_ModelFastfst130", self)

class fastfst_nAzimuth:

    def __init__(self, value: float, name: str, fastfst_nAzimuth: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nAzimuth = fastfst_nAzimuth
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nAzimuth(self):
        return self.__fastfst_nAzimuth

    @fastfst_nAzimuth.setter
    def fastfst_nAzimuth(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nAzimuth__fastfst_nAzimuth", None)
        self.__fastfst_nAzimuth = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst128"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst128", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst128"):
                opp_val = getattr(value, "fastfst_ModelFastfst128", None)
                setattr(value, "fastfst_ModelFastfst128", self)

class fastfst_bTwFADOF1:

    def __init__(self, value: bool, name: str, fastfst_bTwFADOF1: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTwFADOF1 = fastfst_bTwFADOF1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bTwFADOF1(self):
        return self.__fastfst_bTwFADOF1

    @fastfst_bTwFADOF1.setter
    def fastfst_bTwFADOF1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTwFADOF1__fastfst_bTwFADOF1", None)
        self.__fastfst_bTwFADOF1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst110"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst110", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst110"):
                opp_val = getattr(value, "fastfst_ModelFastfst110", None)
                setattr(value, "fastfst_ModelFastfst110", self)

class fastfst_bYawDOF:

    def __init__(self, value: bool, name: str, fastfst_bYawDOF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bYawDOF = fastfst_bYawDOF
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bYawDOF(self):
        return self.__fastfst_bYawDOF

    @fastfst_bYawDOF.setter
    def fastfst_bYawDOF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bYawDOF__fastfst_bYawDOF", None)
        self.__fastfst_bYawDOF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst108"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst108", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst108"):
                opp_val = getattr(value, "fastfst_ModelFastfst108", None)
                setattr(value, "fastfst_ModelFastfst108", self)

class fastfst_bGenDOF:

    def __init__(self, value: bool, name: str, fastfst_bGenDOF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bGenDOF = fastfst_bGenDOF
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bGenDOF(self):
        return self.__fastfst_bGenDOF

    @fastfst_bGenDOF.setter
    def fastfst_bGenDOF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bGenDOF__fastfst_bGenDOF", None)
        self.__fastfst_bGenDOF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst106"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst106", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst106"):
                opp_val = getattr(value, "fastfst_ModelFastfst106", None)
                setattr(value, "fastfst_ModelFastfst106", self)

class fastfst_bDrTrDOF:

    def __init__(self, value: bool, name: str, fastfst_bDrTrDOF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bDrTrDOF = fastfst_bDrTrDOF
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bDrTrDOF(self):
        return self.__fastfst_bDrTrDOF

    @fastfst_bDrTrDOF.setter
    def fastfst_bDrTrDOF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bDrTrDOF__fastfst_bDrTrDOF", None)
        self.__fastfst_bDrTrDOF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst104"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst104", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst104"):
                opp_val = getattr(value, "fastfst_ModelFastfst104", None)
                setattr(value, "fastfst_ModelFastfst104", self)

class fastfst_bTeetDOF:

    def __init__(self, value: bool, name: str, fastfst_bTeetDOF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTeetDOF = fastfst_bTeetDOF
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bTeetDOF(self):
        return self.__fastfst_bTeetDOF

    @fastfst_bTeetDOF.setter
    def fastfst_bTeetDOF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTeetDOF__fastfst_bTeetDOF", None)
        self.__fastfst_bTeetDOF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst102"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst102", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst102"):
                opp_val = getattr(value, "fastfst_ModelFastfst102", None)
                setattr(value, "fastfst_ModelFastfst102", self)

class fastfst_bEdgeDOF:

    def __init__(self, value: bool, name: str, fastfst_bEdgeDOF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bEdgeDOF = fastfst_bEdgeDOF
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bEdgeDOF(self):
        return self.__fastfst_bEdgeDOF

    @fastfst_bEdgeDOF.setter
    def fastfst_bEdgeDOF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bEdgeDOF__fastfst_bEdgeDOF", None)
        self.__fastfst_bEdgeDOF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst100"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst100", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst100"):
                opp_val = getattr(value, "fastfst_ModelFastfst100", None)
                setattr(value, "fastfst_ModelFastfst100", self)

class fastfst_bFlapDOF2:

    def __init__(self, value: bool, name: str, fastfst_bFlapDOF2: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bFlapDOF2 = fastfst_bFlapDOF2
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bFlapDOF2(self):
        return self.__fastfst_bFlapDOF2

    @fastfst_bFlapDOF2.setter
    def fastfst_bFlapDOF2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bFlapDOF2__fastfst_bFlapDOF2", None)
        self.__fastfst_bFlapDOF2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst98"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst98", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst98"):
                opp_val = getattr(value, "fastfst_ModelFastfst98", None)
                setattr(value, "fastfst_ModelFastfst98", self)

class fastfst_bFlapDOF1:

    def __init__(self, value: bool, name: str, fastfst_bFlapDOF1: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bFlapDOF1 = fastfst_bFlapDOF1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bFlapDOF1(self):
        return self.__fastfst_bFlapDOF1

    @fastfst_bFlapDOF1.setter
    def fastfst_bFlapDOF1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bFlapDOF1__fastfst_bFlapDOF1", None)
        self.__fastfst_bFlapDOF1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst96"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst96", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst96"):
                opp_val = getattr(value, "fastfst_ModelFastfst96", None)
                setattr(value, "fastfst_ModelFastfst96", self)

class fastfst_bTwFADOF2:

    def __init__(self, value: bool, name: str, fastfst_bTwFADOF2: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bTwFADOF2 = fastfst_bTwFADOF2
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bTwFADOF2(self):
        return self.__fastfst_bTwFADOF2

    @fastfst_bTwFADOF2.setter
    def fastfst_bTwFADOF2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bTwFADOF2__fastfst_bTwFADOF2", None)
        self.__fastfst_bTwFADOF2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst112"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst112", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst112"):
                opp_val = getattr(value, "fastfst_ModelFastfst112", None)
                setattr(value, "fastfst_ModelFastfst112", self)

class fastfst_nBlPitchF_3_:

    def __init__(self, name: str, value: float, fastfst_nBlPitchF_3_: "fastfst_ModelFastfst" = None):
        self.name = name
        self.value = value
        self.fastfst_nBlPitchF_3_ = fastfst_nBlPitchF_3_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nBlPitchF_3_(self):
        return self.__fastfst_nBlPitchF_3_

    @fastfst_nBlPitchF_3_.setter
    def fastfst_nBlPitchF_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitchF_3___fastfst_nBlPitchF_3_", None)
        self.__fastfst_nBlPitchF_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst92"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst92", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst92"):
                opp_val = getattr(value, "fastfst_ModelFastfst92", None)
                setattr(value, "fastfst_ModelFastfst92", self)

class fastfst_nBlPitchF_2_:

    def __init__(self, value: float, name: str, fastfst_nBlPitchF_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nBlPitchF_2_ = fastfst_nBlPitchF_2_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nBlPitchF_2_(self):
        return self.__fastfst_nBlPitchF_2_

    @fastfst_nBlPitchF_2_.setter
    def fastfst_nBlPitchF_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitchF_2___fastfst_nBlPitchF_2_", None)
        self.__fastfst_nBlPitchF_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst90"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst90", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst90"):
                opp_val = getattr(value, "fastfst_ModelFastfst90", None)
                setattr(value, "fastfst_ModelFastfst90", self)

class fastfst_nBlPitchF_1_:

    def __init__(self, value: float, name: str, fastfst_nBlPitchF_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nBlPitchF_1_ = fastfst_nBlPitchF_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nBlPitchF_1_(self):
        return self.__fastfst_nBlPitchF_1_

    @fastfst_nBlPitchF_1_.setter
    def fastfst_nBlPitchF_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitchF_1___fastfst_nBlPitchF_1_", None)
        self.__fastfst_nBlPitchF_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst88"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst88", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst88"):
                opp_val = getattr(value, "fastfst_ModelFastfst88", None)
                setattr(value, "fastfst_ModelFastfst88", self)

class fastfst_nGravity:

    def __init__(self, value: float, name: str, fastfst_nGravity: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nGravity = fastfst_nGravity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nGravity(self):
        return self.__fastfst_nGravity

    @fastfst_nGravity.setter
    def fastfst_nGravity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nGravity__fastfst_nGravity", None)
        self.__fastfst_nGravity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst94"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst94", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst94"):
                opp_val = getattr(value, "fastfst_ModelFastfst94", None)
                setattr(value, "fastfst_ModelFastfst94", self)

class fastfst_nBlPitch_2_:

    def __init__(self, value: float, name: str, fastfst_nBlPitch_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nBlPitch_2_ = fastfst_nBlPitch_2_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nBlPitch_2_(self):
        return self.__fastfst_nBlPitch_2_

    @fastfst_nBlPitch_2_.setter
    def fastfst_nBlPitch_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitch_2___fastfst_nBlPitch_2_", None)
        self.__fastfst_nBlPitch_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst84"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst84", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst84"):
                opp_val = getattr(value, "fastfst_ModelFastfst84", None)
                setattr(value, "fastfst_ModelFastfst84", self)

class fastfst_nBlPitch_1_:

    def __init__(self, value: float, name: str, fastfst_nBlPitch_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nBlPitch_1_ = fastfst_nBlPitch_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nBlPitch_1_(self):
        return self.__fastfst_nBlPitch_1_

    @fastfst_nBlPitch_1_.setter
    def fastfst_nBlPitch_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitch_1___fastfst_nBlPitch_1_", None)
        self.__fastfst_nBlPitch_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst82"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst82", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst82"):
                opp_val = getattr(value, "fastfst_ModelFastfst82", None)
                setattr(value, "fastfst_ModelFastfst82", self)

class fastfst_nTPitManE_3_:

    def __init__(self, value: float, name: str, fastfst_nTPitManE_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManE_3_ = fastfst_nTPitManE_3_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTPitManE_3_(self):
        return self.__fastfst_nTPitManE_3_

    @fastfst_nTPitManE_3_.setter
    def fastfst_nTPitManE_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManE_3___fastfst_nTPitManE_3_", None)
        self.__fastfst_nTPitManE_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst80"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst80", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst80"):
                opp_val = getattr(value, "fastfst_ModelFastfst80", None)
                setattr(value, "fastfst_ModelFastfst80", self)

class fastfst_nTPitManE_2_:

    def __init__(self, value: float, name: str, fastfst_nTPitManE_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManE_2_ = fastfst_nTPitManE_2_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTPitManE_2_(self):
        return self.__fastfst_nTPitManE_2_

    @fastfst_nTPitManE_2_.setter
    def fastfst_nTPitManE_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManE_2___fastfst_nTPitManE_2_", None)
        self.__fastfst_nTPitManE_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst78"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst78", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst78"):
                opp_val = getattr(value, "fastfst_ModelFastfst78", None)
                setattr(value, "fastfst_ModelFastfst78", self)

class fastfst_nBlPitch_3_:

    def __init__(self, value: float, name: str, fastfst_nBlPitch_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nBlPitch_3_ = fastfst_nBlPitch_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nBlPitch_3_(self):
        return self.__fastfst_nBlPitch_3_

    @fastfst_nBlPitch_3_.setter
    def fastfst_nBlPitch_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nBlPitch_3___fastfst_nBlPitch_3_", None)
        self.__fastfst_nBlPitch_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst86"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst86", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst86"):
                opp_val = getattr(value, "fastfst_ModelFastfst86", None)
                setattr(value, "fastfst_ModelFastfst86", self)

class fastfst_nTPitManE_1_:

    def __init__(self, value: float, name: str, fastfst_nTPitManE_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManE_1_ = fastfst_nTPitManE_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTPitManE_1_(self):
        return self.__fastfst_nTPitManE_1_

    @fastfst_nTPitManE_1_.setter
    def fastfst_nTPitManE_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManE_1___fastfst_nTPitManE_1_", None)
        self.__fastfst_nTPitManE_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst76"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst76", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst76"):
                opp_val = getattr(value, "fastfst_ModelFastfst76", None)
                setattr(value, "fastfst_ModelFastfst76", self)

class fastfst_nTPitManS_3_:

    def __init__(self, value: float, name: str, fastfst_nTPitManS_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManS_3_ = fastfst_nTPitManS_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTPitManS_3_(self):
        return self.__fastfst_nTPitManS_3_

    @fastfst_nTPitManS_3_.setter
    def fastfst_nTPitManS_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManS_3___fastfst_nTPitManS_3_", None)
        self.__fastfst_nTPitManS_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst74"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst74", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst74"):
                opp_val = getattr(value, "fastfst_ModelFastfst74", None)
                setattr(value, "fastfst_ModelFastfst74", self)

class fastfst_nTPitManS_2_:

    def __init__(self, value: float, name: str, fastfst_nTPitManS_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManS_2_ = fastfst_nTPitManS_2_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTPitManS_2_(self):
        return self.__fastfst_nTPitManS_2_

    @fastfst_nTPitManS_2_.setter
    def fastfst_nTPitManS_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManS_2___fastfst_nTPitManS_2_", None)
        self.__fastfst_nTPitManS_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst72"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst72", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst72"):
                opp_val = getattr(value, "fastfst_ModelFastfst72", None)
                setattr(value, "fastfst_ModelFastfst72", self)

class fastfst_nTPitManS_1_:

    def __init__(self, value: float, name: str, fastfst_nTPitManS_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPitManS_1_ = fastfst_nTPitManS_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTPitManS_1_(self):
        return self.__fastfst_nTPitManS_1_

    @fastfst_nTPitManS_1_.setter
    def fastfst_nTPitManS_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPitManS_1___fastfst_nTPitManS_1_", None)
        self.__fastfst_nTPitManS_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst70"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst70", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst70"):
                opp_val = getattr(value, "fastfst_ModelFastfst70", None)
                setattr(value, "fastfst_ModelFastfst70", self)

class fastfst_nTYawManE:

    def __init__(self, value: float, name: str, fastfst_nTYawManE: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTYawManE = fastfst_nTYawManE
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTYawManE(self):
        return self.__fastfst_nTYawManE

    @fastfst_nTYawManE.setter
    def fastfst_nTYawManE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTYawManE__fastfst_nTYawManE", None)
        self.__fastfst_nTYawManE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst66"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst66", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst66"):
                opp_val = getattr(value, "fastfst_ModelFastfst66", None)
                setattr(value, "fastfst_ModelFastfst66", self)

class fastfst_nTYawManS:

    def __init__(self, value: float, name: str, fastfst_nTYawManS: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTYawManS = fastfst_nTYawManS
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTYawManS(self):
        return self.__fastfst_nTYawManS

    @fastfst_nTYawManS.setter
    def fastfst_nTYawManS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTYawManS__fastfst_nTYawManS", None)
        self.__fastfst_nTYawManS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst64"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst64", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst64"):
                opp_val = getattr(value, "fastfst_ModelFastfst64", None)
                setattr(value, "fastfst_ModelFastfst64", self)

class fastfst_nTBDepISp_3_:

    def __init__(self, value: float, name: str, fastfst_nTBDepISp_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTBDepISp_3_ = fastfst_nTBDepISp_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTBDepISp_3_(self):
        return self.__fastfst_nTBDepISp_3_

    @fastfst_nTBDepISp_3_.setter
    def fastfst_nTBDepISp_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTBDepISp_3___fastfst_nTBDepISp_3_", None)
        self.__fastfst_nTBDepISp_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst62"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst62", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst62"):
                opp_val = getattr(value, "fastfst_ModelFastfst62", None)
                setattr(value, "fastfst_ModelFastfst62", self)

class fastfst_nTBDepISp_2_:

    def __init__(self, value: float, name: str, fastfst_nTBDepISp_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTBDepISp_2_ = fastfst_nTBDepISp_2_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTBDepISp_2_(self):
        return self.__fastfst_nTBDepISp_2_

    @fastfst_nTBDepISp_2_.setter
    def fastfst_nTBDepISp_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTBDepISp_2___fastfst_nTBDepISp_2_", None)
        self.__fastfst_nTBDepISp_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst60"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst60", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst60"):
                opp_val = getattr(value, "fastfst_ModelFastfst60", None)
                setattr(value, "fastfst_ModelFastfst60", self)

class fastfst_nNacYawF:

    def __init__(self, value: float, name: str, fastfst_nNacYawF: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nNacYawF = fastfst_nNacYawF
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nNacYawF(self):
        return self.__fastfst_nNacYawF

    @fastfst_nNacYawF.setter
    def fastfst_nNacYawF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nNacYawF__fastfst_nNacYawF", None)
        self.__fastfst_nNacYawF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst68"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst68", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst68"):
                opp_val = getattr(value, "fastfst_ModelFastfst68", None)
                setattr(value, "fastfst_ModelFastfst68", self)

class fastfst_nTTpBrDp_3_:

    def __init__(self, value: float, name: str, fastfst_nTTpBrDp_3_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTTpBrDp_3_ = fastfst_nTTpBrDp_3_
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTTpBrDp_3_(self):
        return self.__fastfst_nTTpBrDp_3_

    @fastfst_nTTpBrDp_3_.setter
    def fastfst_nTTpBrDp_3_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTTpBrDp_3___fastfst_nTTpBrDp_3_", None)
        self.__fastfst_nTTpBrDp_3_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst56"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst56", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst56"):
                opp_val = getattr(value, "fastfst_ModelFastfst56", None)
                setattr(value, "fastfst_ModelFastfst56", self)

class fastfst_nTTpBrDp_2_:

    def __init__(self, value: float, name: str, fastfst_nTTpBrDp_2_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTTpBrDp_2_ = fastfst_nTTpBrDp_2_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTTpBrDp_2_(self):
        return self.__fastfst_nTTpBrDp_2_

    @fastfst_nTTpBrDp_2_.setter
    def fastfst_nTTpBrDp_2_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTTpBrDp_2___fastfst_nTTpBrDp_2_", None)
        self.__fastfst_nTTpBrDp_2_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst54"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst54", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst54"):
                opp_val = getattr(value, "fastfst_ModelFastfst54", None)
                setattr(value, "fastfst_ModelFastfst54", self)

class fastfst_nTTpBrDp_1_:

    def __init__(self, value: float, name: str, fastfst_nTTpBrDp_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTTpBrDp_1_ = fastfst_nTTpBrDp_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTTpBrDp_1_(self):
        return self.__fastfst_nTTpBrDp_1_

    @fastfst_nTTpBrDp_1_.setter
    def fastfst_nTTpBrDp_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTTpBrDp_1___fastfst_nTTpBrDp_1_", None)
        self.__fastfst_nTTpBrDp_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst52"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst52", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst52"):
                opp_val = getattr(value, "fastfst_ModelFastfst52", None)
                setattr(value, "fastfst_ModelFastfst52", self)

class fastfst_nTBDepISp_1_:

    def __init__(self, value: float, name: str, fastfst_nTBDepISp_1_: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTBDepISp_1_ = fastfst_nTBDepISp_1_
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTBDepISp_1_(self):
        return self.__fastfst_nTBDepISp_1_

    @fastfst_nTBDepISp_1_.setter
    def fastfst_nTBDepISp_1_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTBDepISp_1___fastfst_nTBDepISp_1_", None)
        self.__fastfst_nTBDepISp_1_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst58"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst58", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst58"):
                opp_val = getattr(value, "fastfst_ModelFastfst58", None)
                setattr(value, "fastfst_ModelFastfst58", self)

class fastfst_iHSSBrMode:

    def __init__(self, value: int, name: str, fastfst_iHSSBrMode: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iHSSBrMode = fastfst_iHSSBrMode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iHSSBrMode(self):
        return self.__fastfst_iHSSBrMode

    @fastfst_iHSSBrMode.setter
    def fastfst_iHSSBrMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iHSSBrMode__fastfst_iHSSBrMode", None)
        self.__fastfst_iHSSBrMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst46"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst46", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst46"):
                opp_val = getattr(value, "fastfst_ModelFastfst46", None)
                setattr(value, "fastfst_ModelFastfst46", self)

class fastfst_nTimGenOf:

    def __init__(self, value: float, name: str, fastfst_nTimGenOf: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTimGenOf = fastfst_nTimGenOf
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTimGenOf(self):
        return self.__fastfst_nTimGenOf

    @fastfst_nTimGenOf.setter
    def fastfst_nTimGenOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTimGenOf__fastfst_nTimGenOf", None)
        self.__fastfst_nTimGenOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst44"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst44", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst44"):
                opp_val = getattr(value, "fastfst_ModelFastfst44", None)
                setattr(value, "fastfst_ModelFastfst44", self)

class fastfst_nTimGenOn:

    def __init__(self, value: float, name: str, fastfst_nTimGenOn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTimGenOn = fastfst_nTimGenOn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTimGenOn(self):
        return self.__fastfst_nTimGenOn

    @fastfst_nTimGenOn.setter
    def fastfst_nTimGenOn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTimGenOn__fastfst_nTimGenOn", None)
        self.__fastfst_nTimGenOn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst42"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst42", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst42"):
                opp_val = getattr(value, "fastfst_ModelFastfst42", None)
                setattr(value, "fastfst_ModelFastfst42", self)

class fastfst_nSpdGenOn:

    def __init__(self, value: float, name: str, fastfst_nSpdGenOn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nSpdGenOn = fastfst_nSpdGenOn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nSpdGenOn(self):
        return self.__fastfst_nSpdGenOn

    @fastfst_nSpdGenOn.setter
    def fastfst_nSpdGenOn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nSpdGenOn__fastfst_nSpdGenOn", None)
        self.__fastfst_nSpdGenOn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst40"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst40", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst40"):
                opp_val = getattr(value, "fastfst_ModelFastfst40", None)
                setattr(value, "fastfst_ModelFastfst40", self)

class fastfst_bGenTiStp:

    def __init__(self, value: bool, name: str, fastfst_bGenTiStp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bGenTiStp = fastfst_bGenTiStp
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_bGenTiStp(self):
        return self.__fastfst_bGenTiStp

    @fastfst_bGenTiStp.setter
    def fastfst_bGenTiStp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bGenTiStp__fastfst_bGenTiStp", None)
        self.__fastfst_bGenTiStp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst38"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst38", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst38"):
                opp_val = getattr(value, "fastfst_ModelFastfst38", None)
                setattr(value, "fastfst_ModelFastfst38", self)

class fastfst_bGenTiStr:

    def __init__(self, value: bool, name: str, fastfst_bGenTiStr: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bGenTiStr = fastfst_bGenTiStr
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bGenTiStr(self):
        return self.__fastfst_bGenTiStr

    @fastfst_bGenTiStr.setter
    def fastfst_bGenTiStr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bGenTiStr__fastfst_bGenTiStr", None)
        self.__fastfst_bGenTiStr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst36"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst36", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst36"):
                opp_val = getattr(value, "fastfst_ModelFastfst36", None)
                setattr(value, "fastfst_ModelFastfst36", self)

class fastfst_iGenModel:

    def __init__(self, value: int, name: str, fastfst_iGenModel: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iGenModel = fastfst_iGenModel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iGenModel(self):
        return self.__fastfst_iGenModel

    @fastfst_iGenModel.setter
    def fastfst_iGenModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iGenModel__fastfst_iGenModel", None)
        self.__fastfst_iGenModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst34"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst34", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst34"):
                opp_val = getattr(value, "fastfst_ModelFastfst34", None)
                setattr(value, "fastfst_ModelFastfst34", self)

class fastfst_nVS_SlPc:

    def __init__(self, value: float, name: str, fastfst_nVS_SlPc: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nVS_SlPc = fastfst_nVS_SlPc
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nVS_SlPc(self):
        return self.__fastfst_nVS_SlPc

    @fastfst_nVS_SlPc.setter
    def fastfst_nVS_SlPc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nVS_SlPc__fastfst_nVS_SlPc", None)
        self.__fastfst_nVS_SlPc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst32"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst32", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst32"):
                opp_val = getattr(value, "fastfst_ModelFastfst32", None)
                setattr(value, "fastfst_ModelFastfst32", self)

class fastfst_nVS_Rgn2K:

    def __init__(self, value: float, name: str, fastfst_nVS_Rgn2K: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nVS_Rgn2K = fastfst_nVS_Rgn2K
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nVS_Rgn2K(self):
        return self.__fastfst_nVS_Rgn2K

    @fastfst_nVS_Rgn2K.setter
    def fastfst_nVS_Rgn2K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nVS_Rgn2K__fastfst_nVS_Rgn2K", None)
        self.__fastfst_nVS_Rgn2K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst30"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst30", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst30"):
                opp_val = getattr(value, "fastfst_ModelFastfst30", None)
                setattr(value, "fastfst_ModelFastfst30", self)

class fastfst_nVS_RtTq:

    def __init__(self, value: float, name: str, fastfst_nVS_RtTq: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nVS_RtTq = fastfst_nVS_RtTq
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nVS_RtTq(self):
        return self.__fastfst_nVS_RtTq

    @fastfst_nVS_RtTq.setter
    def fastfst_nVS_RtTq(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nVS_RtTq__fastfst_nVS_RtTq", None)
        self.__fastfst_nVS_RtTq = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst28"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst28", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst28"):
                opp_val = getattr(value, "fastfst_ModelFastfst28", None)
                setattr(value, "fastfst_ModelFastfst28", self)

class fastfst_nVS_RtGnSp:

    def __init__(self, value: float, name: str, fastfst_nVS_RtGnSp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nVS_RtGnSp = fastfst_nVS_RtGnSp
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nVS_RtGnSp(self):
        return self.__fastfst_nVS_RtGnSp

    @fastfst_nVS_RtGnSp.setter
    def fastfst_nVS_RtGnSp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nVS_RtGnSp__fastfst_nVS_RtGnSp", None)
        self.__fastfst_nVS_RtGnSp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst26"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst26", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst26"):
                opp_val = getattr(value, "fastfst_ModelFastfst26", None)
                setattr(value, "fastfst_ModelFastfst26", self)

class fastfst_iVSContrl:

    def __init__(self, value: int, name: str, fastfst_iVSContrl: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iVSContrl = fastfst_iVSContrl
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iVSContrl(self):
        return self.__fastfst_iVSContrl

    @fastfst_iVSContrl.setter
    def fastfst_iVSContrl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iVSContrl__fastfst_iVSContrl", None)
        self.__fastfst_iVSContrl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst24"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst24", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst24"):
                opp_val = getattr(value, "fastfst_ModelFastfst24", None)
                setattr(value, "fastfst_ModelFastfst24", self)

class fastfst_nTPCOn:

    def __init__(self, value: float, name: str, fastfst_nTPCOn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTPCOn = fastfst_nTPCOn
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTPCOn(self):
        return self.__fastfst_nTPCOn

    @fastfst_nTPCOn.setter
    def fastfst_nTPCOn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTPCOn__fastfst_nTPCOn", None)
        self.__fastfst_nTPCOn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst22"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst22", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst22"):
                opp_val = getattr(value, "fastfst_ModelFastfst22", None)
                setattr(value, "fastfst_ModelFastfst22", self)

class fastfst_iPCMode:

    def __init__(self, value: int, name: str, fastfst_iPCMode: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iPCMode = fastfst_iPCMode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iPCMode(self):
        return self.__fastfst_iPCMode

    @fastfst_iPCMode.setter
    def fastfst_iPCMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iPCMode__fastfst_iPCMode", None)
        self.__fastfst_iPCMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst20"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst20", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst20"):
                opp_val = getattr(value, "fastfst_ModelFastfst20", None)
                setattr(value, "fastfst_ModelFastfst20", self)

class fastfst_nTYCOn:

    def __init__(self, value: float, name: str, fastfst_nTYCOn: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTYCOn = fastfst_nTYCOn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTYCOn(self):
        return self.__fastfst_nTYCOn

    @fastfst_nTYCOn.setter
    def fastfst_nTYCOn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTYCOn__fastfst_nTYCOn", None)
        self.__fastfst_nTYCOn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst18"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst18", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst18"):
                opp_val = getattr(value, "fastfst_ModelFastfst18", None)
                setattr(value, "fastfst_ModelFastfst18", self)

class fastfst_iYCMode:

    def __init__(self, value: int, name: str, fastfst_iYCMode: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iYCMode = fastfst_iYCMode
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iYCMode(self):
        return self.__fastfst_iYCMode

    @fastfst_iYCMode.setter
    def fastfst_iYCMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iYCMode__fastfst_iYCMode", None)
        self.__fastfst_iYCMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst16"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst16", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst16"):
                opp_val = getattr(value, "fastfst_ModelFastfst16", None)
                setattr(value, "fastfst_ModelFastfst16", self)

class fastfst_nDT:

    def __init__(self, value: float, name: str, fastfst_nDT: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nDT = fastfst_nDT
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nDT(self):
        return self.__fastfst_nDT

    @fastfst_nDT.setter
    def fastfst_nDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nDT__fastfst_nDT", None)
        self.__fastfst_nDT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst14"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst14", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst14"):
                opp_val = getattr(value, "fastfst_ModelFastfst14", None)
                setattr(value, "fastfst_ModelFastfst14", self)

class fastfst_nTMax:

    def __init__(self, value: float, name: str, fastfst_nTMax: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTMax = fastfst_nTMax
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTMax(self):
        return self.__fastfst_nTMax

    @fastfst_nTMax.setter
    def fastfst_nTMax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTMax__fastfst_nTMax", None)
        self.__fastfst_nTMax = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst12"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst12", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst12"):
                opp_val = getattr(value, "fastfst_ModelFastfst12", None)
                setattr(value, "fastfst_ModelFastfst12", self)

class fastfst_nTiDynBrk:

    def __init__(self, value: float, name: str, fastfst_nTiDynBrk: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTiDynBrk = fastfst_nTiDynBrk
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_nTiDynBrk(self):
        return self.__fastfst_nTiDynBrk

    @fastfst_nTiDynBrk.setter
    def fastfst_nTiDynBrk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTiDynBrk__fastfst_nTiDynBrk", None)
        self.__fastfst_nTiDynBrk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst50"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst50", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst50"):
                opp_val = getattr(value, "fastfst_ModelFastfst50", None)
                setattr(value, "fastfst_ModelFastfst50", self)

class fastfst_nTHSSBrDp:

    def __init__(self, value: float, name: str, fastfst_nTHSSBrDp: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_nTHSSBrDp = fastfst_nTHSSBrDp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def fastfst_nTHSSBrDp(self):
        return self.__fastfst_nTHSSBrDp

    @fastfst_nTHSSBrDp.setter
    def fastfst_nTHSSBrDp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_nTHSSBrDp__fastfst_nTHSSBrDp", None)
        self.__fastfst_nTHSSBrDp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst48"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst48", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst48"):
                opp_val = getattr(value, "fastfst_ModelFastfst48", None)
                setattr(value, "fastfst_ModelFastfst48", self)

class fastfst_Header:

    def __init__(self, rows: str, fastfst_Header: "fastfst_ModelFastfst" = None):
        self.rows = rows
        self.fastfst_Header = fastfst_Header
        
    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

    @property
    def fastfst_Header(self):
        return self.__fastfst_Header

    @fastfst_Header.setter
    def fastfst_Header(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_Header__fastfst_Header", None)
        self.__fastfst_Header = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst"):
                opp_val = getattr(value, "fastfst_ModelFastfst", None)
                setattr(value, "fastfst_ModelFastfst", self)

class fastfst_ModelFastfst:

    pass
class fastfst_iNumBl:

    def __init__(self, value: int, name: str, fastfst_iNumBl: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iNumBl = fastfst_iNumBl
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iNumBl(self):
        return self.__fastfst_iNumBl

    @fastfst_iNumBl.setter
    def fastfst_iNumBl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iNumBl__fastfst_iNumBl", None)
        self.__fastfst_iNumBl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst10"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst10", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst10"):
                opp_val = getattr(value, "fastfst_ModelFastfst10", None)
                setattr(value, "fastfst_ModelFastfst10", self)

class fastfst_iAnalMode:

    def __init__(self, value: int, name: str, fastfst_iAnalMode: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iAnalMode = fastfst_iAnalMode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fastfst_iAnalMode(self):
        return self.__fastfst_iAnalMode

    @fastfst_iAnalMode.setter
    def fastfst_iAnalMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iAnalMode__fastfst_iAnalMode", None)
        self.__fastfst_iAnalMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst8"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst8", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst8"):
                opp_val = getattr(value, "fastfst_ModelFastfst8", None)
                setattr(value, "fastfst_ModelFastfst8", self)

class fastfst_iADAMSPrep:

    def __init__(self, value: int, name: str, fastfst_iADAMSPrep: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_iADAMSPrep = fastfst_iADAMSPrep
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_iADAMSPrep(self):
        return self.__fastfst_iADAMSPrep

    @fastfst_iADAMSPrep.setter
    def fastfst_iADAMSPrep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_iADAMSPrep__fastfst_iADAMSPrep", None)
        self.__fastfst_iADAMSPrep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst6"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst6", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst6"):
                opp_val = getattr(value, "fastfst_ModelFastfst6", None)
                setattr(value, "fastfst_ModelFastfst6", self)

class fastfst_bEcho:

    def __init__(self, value: bool, name: str, fastfst_bEcho: "fastfst_ModelFastfst" = None):
        self.value = value
        self.name = name
        self.fastfst_bEcho = fastfst_bEcho
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def fastfst_bEcho(self):
        return self.__fastfst_bEcho

    @fastfst_bEcho.setter
    def fastfst_bEcho(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_bEcho__fastfst_bEcho", None)
        self.__fastfst_bEcho = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst4"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst4", None)
                if opp_val == self:
                    setattr(old_value, "fastfst_ModelFastfst4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst4"):
                opp_val = getattr(value, "fastfst_ModelFastfst4", None)
                setattr(value, "fastfst_ModelFastfst4", self)

class fastfst_Section:

    def __init__(self, name: str, fastfst_Section: "fastfst_ModelFastfst" = None):
        self.name = name
        self.fastfst_Section = fastfst_Section
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fastfst_Section(self):
        return self.__fastfst_Section

    @fastfst_Section.setter
    def fastfst_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fastfst_Section__fastfst_Section", None)
        self.__fastfst_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fastfst_ModelFastfst2"):
                opp_val = getattr(old_value, "fastfst_ModelFastfst2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fastfst_ModelFastfst2"):
                opp_val = getattr(value, "fastfst_ModelFastfst2", None)
                if opp_val is None:
                    setattr(value, "fastfst_ModelFastfst2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
