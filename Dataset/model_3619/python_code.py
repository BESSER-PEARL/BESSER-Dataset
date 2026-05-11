from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TelecommunicationAddressUse(Enum):
    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    AS = "AS"
    EC = "EC"
    MC = "MC"
    PG = "PG"
class AddressPartType(Enum):
    AL = "AL"
    ADL = "ADL"
    UNID = "UNID"
    UNIT = "UNIT"
    STR = "STR"
    STB = "STB"
    STTYP = "STTYP"
    DIR = "DIR"
    INT = "INT"
    CAR = "CAR"
    CEN = "CEN"
    DAL = "DAL"
    DINST = "DINST"
    DINSTA = "DINSTA"
    DINSTQ = "DINSTQ"
    DMOD = "DMOD"
    DMODID = "DMODID"
    SAL = "SAL"
    BNR = "BNR"
    BNN = "BNN"
    BNS = "BNS"
    STA = "STA"
    ZIP = "ZIP"
    DPID = "DPID"
    CNT = "CNT"
    CPA = "CPA"
    CTY = "CTY"
    DEL = "DEL"
    POB = "POB"
    PRE = "PRE"
class CalendarCycle(Enum):
    WY = "WY"
    DM = "DM"
    CD = "CD"
    DY = "DY"
    DW = "DW"
    HD = "HD"
    CH = "CH"
    NH = "NH"
    CN = "CN"
    SN = "SN"
    CS = "CS"
    CY = "CY"
    MY = "MY"
    CM = "CM"
    CW = "CW"
    WM = "WM"
class EntityNameUse(Enum):
    OR = "OR"
    T = "T"
    I = "I"
    P = "P"
    ANON = "ANON"
    A = "A"
    R = "R"
    OLD = "OLD"
    DN = "DN"
    M = "M"
    PHON = "PHON"
    SRCH = "SRCH"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    C = "C"
class IntegrityCheckAlgorithm(Enum):
    SHA1 = "SHA1"
    SHA256 = "SHA256"
class PostalAddressUse(Enum):
    H = "H"
    HP = "HP"
    SYL = "SYL"
    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    PHYS = "PHYS"
    PST = "PST"
    TMP = "TMP"
    ABC = "ABC"
    IDE = "IDE"
class Compression(Enum):
    DF = "DF"
    GZ = "GZ"
    ZL = "ZL"
    Z = "Z"
    BZ = "BZ"
    Z7 = "Z7"
class TelecommunicationCapability(Enum):
    voice = "voice"
    fax = "fax"
    data = "data"
    tty = "tty"
    sms = "sms"
class EntityNamePartType(Enum):
    FAM = "FAM"
    GIV = "GIV"
    TITLE = "TITLE"
    DEL = "DEL"
class EntityNamePartQualifier(Enum):
    PR = "PR"
    HON = "HON"
    BR = "BR"
    AD = "AD"
    SP = "SP"
    MID = "MID"
    CL = "CL"
    IN = "IN"
    PFX = "PFX"
    SFX = "SFX"
    LS = "LS"
    AC = "AC"
    NB = "NB"


############################################
# Definition of Classes
############################################

class r2_XP:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class QSET:

    pass
class r2_IVL(QSET):

    pass
class IVL:

    pass
class r2_IVLQTY(IVL):

    def __init__(self, highClosed: str, lowClosed: str, r2_IVLQTY: "r2_QTY" = None, r2_IVLQTY32: "r2_QTY" = None):
        self.highClosed = highClosed
        self.lowClosed = lowClosed
        self.r2_IVLQTY = r2_IVLQTY
        self.r2_IVLQTY32 = r2_IVLQTY32
        
        pass
    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def r2_IVLQTY32(self):
        return self.__r2_IVLQTY32

    @r2_IVLQTY32.setter
    def r2_IVLQTY32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLQTY__r2_IVLQTY32", None)
        self.__r2_IVLQTY32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_QTY33"):
                opp_val = getattr(old_value, "r2_QTY33", None)
                if opp_val == self:
                    setattr(old_value, "r2_QTY33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_QTY33"):
                opp_val = getattr(value, "r2_QTY33", None)
                setattr(value, "r2_QTY33", self)

    @property
    def r2_IVLQTY(self):
        return self.__r2_IVLQTY

    @r2_IVLQTY.setter
    def r2_IVLQTY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLQTY__r2_IVLQTY", None)
        self.__r2_IVLQTY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_QTY"):
                opp_val = getattr(old_value, "r2_QTY", None)
                if opp_val == self:
                    setattr(old_value, "r2_QTY", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_QTY"):
                opp_val = getattr(value, "r2_QTY", None)
                setattr(value, "r2_QTY", self)

class r2_IVLREAL(IVL):

    def __init__(self, highClosed: str, lowClosed: str, r2_IVLREAL: "r2_REAL" = None, r2_IVLREAL36: "r2_REAL" = None):
        self.highClosed = highClosed
        self.lowClosed = lowClosed
        self.r2_IVLREAL = r2_IVLREAL
        self.r2_IVLREAL36 = r2_IVLREAL36
        
        pass
    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def r2_IVLREAL36(self):
        return self.__r2_IVLREAL36

    @r2_IVLREAL36.setter
    def r2_IVLREAL36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLREAL__r2_IVLREAL36", None)
        self.__r2_IVLREAL36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_REAL37"):
                opp_val = getattr(old_value, "r2_REAL37", None)
                if opp_val == self:
                    setattr(old_value, "r2_REAL37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_REAL37"):
                opp_val = getattr(value, "r2_REAL37", None)
                setattr(value, "r2_REAL37", self)

    @property
    def r2_IVLREAL(self):
        return self.__r2_IVLREAL

    @r2_IVLREAL.setter
    def r2_IVLREAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLREAL__r2_IVLREAL", None)
        self.__r2_IVLREAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_REAL"):
                opp_val = getattr(old_value, "r2_REAL", None)
                if opp_val == self:
                    setattr(old_value, "r2_REAL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_REAL"):
                opp_val = getattr(value, "r2_REAL", None)
                setattr(value, "r2_REAL", self)

class r2_IVLTS(IVL):

    def __init__(self, highClosed: str, lowClosed: str, r2_IVLTS: "r2_TS" = None, r2_IVLTS40: "r2_TS" = None, r2_IVLTS43: "r2_PIVLTS" = None):
        self.highClosed = highClosed
        self.lowClosed = lowClosed
        self.r2_IVLTS = r2_IVLTS
        self.r2_IVLTS40 = r2_IVLTS40
        self.r2_IVLTS43 = r2_IVLTS43
        
        pass
    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def r2_IVLTS40(self):
        return self.__r2_IVLTS40

    @r2_IVLTS40.setter
    def r2_IVLTS40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLTS__r2_IVLTS40", None)
        self.__r2_IVLTS40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_TS41"):
                opp_val = getattr(old_value, "r2_TS41", None)
                if opp_val == self:
                    setattr(old_value, "r2_TS41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_TS41"):
                opp_val = getattr(value, "r2_TS41", None)
                setattr(value, "r2_TS41", self)

    @property
    def r2_IVLTS43(self):
        return self.__r2_IVLTS43

    @r2_IVLTS43.setter
    def r2_IVLTS43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLTS__r2_IVLTS43", None)
        self.__r2_IVLTS43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PIVLTS"):
                opp_val = getattr(old_value, "r2_PIVLTS", None)
                if opp_val == self:
                    setattr(old_value, "r2_PIVLTS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PIVLTS"):
                opp_val = getattr(value, "r2_PIVLTS", None)
                setattr(value, "r2_PIVLTS", self)

    @property
    def r2_IVLTS(self):
        return self.__r2_IVLTS

    @r2_IVLTS.setter
    def r2_IVLTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLTS__r2_IVLTS", None)
        self.__r2_IVLTS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_TS"):
                opp_val = getattr(old_value, "r2_TS", None)
                if opp_val == self:
                    setattr(old_value, "r2_TS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_TS"):
                opp_val = getattr(value, "r2_TS", None)
                setattr(value, "r2_TS", self)

class r2_IVLPQ(IVL):

    def __init__(self, highClosed: str, lowClosed: str, r2_IVLPQ: "r2_PQ" = None, r2_IVLPQ28: "r2_PQ" = None):
        self.highClosed = highClosed
        self.lowClosed = lowClosed
        self.r2_IVLPQ = r2_IVLPQ
        self.r2_IVLPQ28 = r2_IVLPQ28
        
        pass
    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def r2_IVLPQ(self):
        return self.__r2_IVLPQ

    @r2_IVLPQ.setter
    def r2_IVLPQ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLPQ__r2_IVLPQ", None)
        self.__r2_IVLPQ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PQ"):
                opp_val = getattr(old_value, "r2_PQ", None)
                if opp_val == self:
                    setattr(old_value, "r2_PQ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PQ"):
                opp_val = getattr(value, "r2_PQ", None)
                setattr(value, "r2_PQ", self)

    @property
    def r2_IVLPQ28(self):
        return self.__r2_IVLPQ28

    @r2_IVLPQ28.setter
    def r2_IVLPQ28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLPQ__r2_IVLPQ28", None)
        self.__r2_IVLPQ28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PQ29"):
                opp_val = getattr(old_value, "r2_PQ29", None)
                if opp_val == self:
                    setattr(old_value, "r2_PQ29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PQ29"):
                opp_val = getattr(value, "r2_PQ29", None)
                setattr(value, "r2_PQ29", self)

class r2_IVLCO(IVL):

    def __init__(self, highClosed: str, lowClosed: str, r2_IVLCO: "r2_CO" = None, r2_IVLCO20: "r2_CO" = None):
        self.highClosed = highClosed
        self.lowClosed = lowClosed
        self.r2_IVLCO = r2_IVLCO
        self.r2_IVLCO20 = r2_IVLCO20
        
        pass
    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def r2_IVLCO(self):
        return self.__r2_IVLCO

    @r2_IVLCO.setter
    def r2_IVLCO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLCO__r2_IVLCO", None)
        self.__r2_IVLCO = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CO18"):
                opp_val = getattr(old_value, "r2_CO18", None)
                if opp_val == self:
                    setattr(old_value, "r2_CO18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CO18"):
                opp_val = getattr(value, "r2_CO18", None)
                setattr(value, "r2_CO18", self)

    @property
    def r2_IVLCO20(self):
        return self.__r2_IVLCO20

    @r2_IVLCO20.setter
    def r2_IVLCO20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLCO__r2_IVLCO20", None)
        self.__r2_IVLCO20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CO21"):
                opp_val = getattr(old_value, "r2_CO21", None)
                if opp_val == self:
                    setattr(old_value, "r2_CO21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CO21"):
                opp_val = getattr(value, "r2_CO21", None)
                setattr(value, "r2_CO21", self)

class r2_IVLINT(IVL):

    def __init__(self, lowClosed: str, highClosed: str, r2_IVLINT: "r2_INT" = None, r2_IVLINT24: "r2_INT" = None):
        self.lowClosed = lowClosed
        self.highClosed = highClosed
        self.r2_IVLINT = r2_IVLINT
        self.r2_IVLINT24 = r2_IVLINT24
        
        pass
    @property
    def lowClosed(self):
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed


    @property
    def highClosed(self):
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed


    @property
    def r2_IVLINT(self):
        return self.__r2_IVLINT

    @r2_IVLINT.setter
    def r2_IVLINT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLINT__r2_IVLINT", None)
        self.__r2_IVLINT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_INT"):
                opp_val = getattr(old_value, "r2_INT", None)
                if opp_val == self:
                    setattr(old_value, "r2_INT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_INT"):
                opp_val = getattr(value, "r2_INT", None)
                setattr(value, "r2_INT", self)

    @property
    def r2_IVLINT24(self):
        return self.__r2_IVLINT24

    @r2_IVLINT24.setter
    def r2_IVLINT24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_IVLINT__r2_IVLINT24", None)
        self.__r2_IVLINT24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_INT25"):
                opp_val = getattr(old_value, "r2_INT25", None)
                if opp_val == self:
                    setattr(old_value, "r2_INT25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_INT25"):
                opp_val = getattr(value, "r2_INT25", None)
                setattr(value, "r2_INT25", self)

class r2_HXIT(ABC):

    pass
class r2_EObject:

    pass
class QTY:

    pass
class r2_TS(QTY):

    def __init__(self, value: str, r2_TS: "r2_IVLTS" = None, r2_TS41: "r2_IVLTS" = None):
        self.value = value
        self.r2_TS = r2_TS
        self.r2_TS41 = r2_TS41
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_TS(self):
        return self.__r2_TS

    @r2_TS.setter
    def r2_TS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_TS__r2_TS", None)
        self.__r2_TS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLTS"):
                opp_val = getattr(old_value, "r2_IVLTS", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLTS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLTS"):
                opp_val = getattr(value, "r2_IVLTS", None)
                setattr(value, "r2_IVLTS", self)

    @property
    def r2_TS41(self):
        return self.__r2_TS41

    @r2_TS41.setter
    def r2_TS41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_TS__r2_TS41", None)
        self.__r2_TS41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLTS40"):
                opp_val = getattr(old_value, "r2_IVLTS40", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLTS40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLTS40"):
                opp_val = getattr(value, "r2_IVLTS40", None)
                setattr(value, "r2_IVLTS40", self)

class r2_PIVLTS(QTY):

    def __init__(self, alignment: str, isFlexible: str, r2_PIVLTS48: "r2_RTO" = None, r2_PIVLTS50: "r2_INT" = None, r2_PIVLTS: "r2_IVLTS" = None, r2_PIVLTS45: "r2_PQ" = None):
        self.alignment = alignment
        self.isFlexible = isFlexible
        self.r2_PIVLTS48 = r2_PIVLTS48
        self.r2_PIVLTS50 = r2_PIVLTS50
        self.r2_PIVLTS = r2_PIVLTS
        self.r2_PIVLTS45 = r2_PIVLTS45
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


    @property
    def isFlexible(self):
        return self.__isFlexible

    @isFlexible.setter
    def isFlexible(self, isFlexible: str):
        self.__isFlexible = isFlexible


    @property
    def r2_PIVLTS48(self):
        return self.__r2_PIVLTS48

    @r2_PIVLTS48.setter
    def r2_PIVLTS48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PIVLTS__r2_PIVLTS48", None)
        self.__r2_PIVLTS48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_RTO"):
                opp_val = getattr(old_value, "r2_RTO", None)
                if opp_val == self:
                    setattr(old_value, "r2_RTO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_RTO"):
                opp_val = getattr(value, "r2_RTO", None)
                setattr(value, "r2_RTO", self)

    @property
    def r2_PIVLTS(self):
        return self.__r2_PIVLTS

    @r2_PIVLTS.setter
    def r2_PIVLTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PIVLTS__r2_PIVLTS", None)
        self.__r2_PIVLTS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLTS43"):
                opp_val = getattr(old_value, "r2_IVLTS43", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLTS43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLTS43"):
                opp_val = getattr(value, "r2_IVLTS43", None)
                setattr(value, "r2_IVLTS43", self)

    @property
    def r2_PIVLTS50(self):
        return self.__r2_PIVLTS50

    @r2_PIVLTS50.setter
    def r2_PIVLTS50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PIVLTS__r2_PIVLTS50", None)
        self.__r2_PIVLTS50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_INT51"):
                opp_val = getattr(old_value, "r2_INT51", None)
                if opp_val == self:
                    setattr(old_value, "r2_INT51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_INT51"):
                opp_val = getattr(value, "r2_INT51", None)
                setattr(value, "r2_INT51", self)

    @property
    def r2_PIVLTS45(self):
        return self.__r2_PIVLTS45

    @r2_PIVLTS45.setter
    def r2_PIVLTS45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PIVLTS__r2_PIVLTS45", None)
        self.__r2_PIVLTS45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PQ46"):
                opp_val = getattr(old_value, "r2_PQ46", None)
                if opp_val == self:
                    setattr(old_value, "r2_PQ46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PQ46"):
                opp_val = getattr(value, "r2_PQ46", None)
                setattr(value, "r2_PQ46", self)

class r2_RTO(QTY):

    pass
class r2_INT(QTY):

    def __init__(self, value: str, r2_INT: "r2_IVLINT" = None, r2_INT25: "r2_IVLINT" = None, r2_INT51: "r2_PIVLTS" = None):
        self.value = value
        self.r2_INT = r2_INT
        self.r2_INT25 = r2_INT25
        self.r2_INT51 = r2_INT51
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_INT51(self):
        return self.__r2_INT51

    @r2_INT51.setter
    def r2_INT51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_INT__r2_INT51", None)
        self.__r2_INT51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PIVLTS50"):
                opp_val = getattr(old_value, "r2_PIVLTS50", None)
                if opp_val == self:
                    setattr(old_value, "r2_PIVLTS50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PIVLTS50"):
                opp_val = getattr(value, "r2_PIVLTS50", None)
                setattr(value, "r2_PIVLTS50", self)

    @property
    def r2_INT25(self):
        return self.__r2_INT25

    @r2_INT25.setter
    def r2_INT25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_INT__r2_INT25", None)
        self.__r2_INT25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLINT24"):
                opp_val = getattr(old_value, "r2_IVLINT24", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLINT24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLINT24"):
                opp_val = getattr(value, "r2_IVLINT24", None)
                setattr(value, "r2_IVLINT24", self)

    @property
    def r2_INT(self):
        return self.__r2_INT

    @r2_INT.setter
    def r2_INT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_INT__r2_INT", None)
        self.__r2_INT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLINT"):
                opp_val = getattr(old_value, "r2_IVLINT", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLINT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLINT"):
                opp_val = getattr(value, "r2_IVLINT", None)
                setattr(value, "r2_IVLINT", self)

class r2_PQ(QTY):

    def __init__(self, unit: str, value: str, r2_PQ: "r2_IVLPQ" = None, r2_PQ29: "r2_IVLPQ" = None, r2_PQ46: "r2_PIVLTS" = None):
        self.unit = unit
        self.value = value
        self.r2_PQ = r2_PQ
        self.r2_PQ29 = r2_PQ29
        self.r2_PQ46 = r2_PQ46
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def r2_PQ29(self):
        return self.__r2_PQ29

    @r2_PQ29.setter
    def r2_PQ29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PQ__r2_PQ29", None)
        self.__r2_PQ29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLPQ28"):
                opp_val = getattr(old_value, "r2_IVLPQ28", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLPQ28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLPQ28"):
                opp_val = getattr(value, "r2_IVLPQ28", None)
                setattr(value, "r2_IVLPQ28", self)

    @property
    def r2_PQ(self):
        return self.__r2_PQ

    @r2_PQ.setter
    def r2_PQ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PQ__r2_PQ", None)
        self.__r2_PQ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLPQ"):
                opp_val = getattr(old_value, "r2_IVLPQ", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLPQ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLPQ"):
                opp_val = getattr(value, "r2_IVLPQ", None)
                setattr(value, "r2_IVLPQ", self)

    @property
    def r2_PQ46(self):
        return self.__r2_PQ46

    @r2_PQ46.setter
    def r2_PQ46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_PQ__r2_PQ46", None)
        self.__r2_PQ46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_PIVLTS45"):
                opp_val = getattr(old_value, "r2_PIVLTS45", None)
                if opp_val == self:
                    setattr(old_value, "r2_PIVLTS45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_PIVLTS45"):
                opp_val = getattr(value, "r2_PIVLTS45", None)
                setattr(value, "r2_PIVLTS45", self)

class r2_REAL(QTY):

    def __init__(self, value: str, r2_REAL: "r2_IVLREAL" = None, r2_REAL37: "r2_IVLREAL" = None):
        self.value = value
        self.r2_REAL = r2_REAL
        self.r2_REAL37 = r2_REAL37
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_REAL37(self):
        return self.__r2_REAL37

    @r2_REAL37.setter
    def r2_REAL37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_REAL__r2_REAL37", None)
        self.__r2_REAL37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLREAL36"):
                opp_val = getattr(old_value, "r2_IVLREAL36", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLREAL36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLREAL36"):
                opp_val = getattr(value, "r2_IVLREAL36", None)
                setattr(value, "r2_IVLREAL36", self)

    @property
    def r2_REAL(self):
        return self.__r2_REAL

    @r2_REAL.setter
    def r2_REAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_REAL__r2_REAL", None)
        self.__r2_REAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLREAL"):
                opp_val = getattr(old_value, "r2_IVLREAL", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLREAL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLREAL"):
                opp_val = getattr(value, "r2_IVLREAL", None)
                setattr(value, "r2_IVLREAL", self)

class r2_CO(QTY):

    def __init__(self, value: str, r2_CO: "r2_CD" = None, r2_CO18: "r2_IVLCO" = None, r2_CO21: "r2_IVLCO" = None):
        self.value = value
        self.r2_CO = r2_CO
        self.r2_CO18 = r2_CO18
        self.r2_CO21 = r2_CO21
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_CO21(self):
        return self.__r2_CO21

    @r2_CO21.setter
    def r2_CO21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CO__r2_CO21", None)
        self.__r2_CO21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLCO20"):
                opp_val = getattr(old_value, "r2_IVLCO20", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLCO20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLCO20"):
                opp_val = getattr(value, "r2_IVLCO20", None)
                setattr(value, "r2_IVLCO20", self)

    @property
    def r2_CO18(self):
        return self.__r2_CO18

    @r2_CO18.setter
    def r2_CO18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CO__r2_CO18", None)
        self.__r2_CO18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_IVLCO"):
                opp_val = getattr(old_value, "r2_IVLCO", None)
                if opp_val == self:
                    setattr(old_value, "r2_IVLCO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_IVLCO"):
                opp_val = getattr(value, "r2_IVLCO", None)
                setattr(value, "r2_IVLCO", self)

    @property
    def r2_CO(self):
        return self.__r2_CO

    @r2_CO.setter
    def r2_CO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CO__r2_CO", None)
        self.__r2_CO = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CD9"):
                opp_val = getattr(old_value, "r2_CD9", None)
                if opp_val == self:
                    setattr(old_value, "r2_CD9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CD9"):
                opp_val = getattr(value, "r2_CD9", None)
                setattr(value, "r2_CD9", self)

class HXIT:

    pass
class r2_ANY(HXIT):

    pass
class XP:

    pass
class r2_ENXP(XP):

    def __init__(self, qualifier: str, type: str, r2_ENXP: "r2_EN" = None):
        self.qualifier = qualifier
        self.type = type
        self.r2_ENXP = r2_ENXP
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier


    @property
    def r2_ENXP(self):
        return self.__r2_ENXP

    @r2_ENXP.setter
    def r2_ENXP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ENXP__r2_ENXP", None)
        self.__r2_ENXP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_EN"):
                opp_val = getattr(old_value, "r2_EN", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_EN"):
                opp_val = getattr(value, "r2_EN", None)
                if opp_val is None:
                    setattr(value, "r2_EN", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ANY:

    pass
class r2_QTY(ANY):

    pass
class r2_ST(ANY):

    def __init__(self, value: str, r2_ST15: "r2_ED" = None, r2_ST: "r2_CD" = None, r2_ST4: "r2_CD" = None):
        self.value = value
        self.r2_ST15 = r2_ST15
        self.r2_ST = r2_ST
        self.r2_ST4 = r2_ST4
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_ST15(self):
        return self.__r2_ST15

    @r2_ST15.setter
    def r2_ST15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ST__r2_ST15", None)
        self.__r2_ST15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_ED14"):
                opp_val = getattr(old_value, "r2_ED14", None)
                if opp_val == self:
                    setattr(old_value, "r2_ED14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_ED14"):
                opp_val = getattr(value, "r2_ED14", None)
                setattr(value, "r2_ED14", self)

    @property
    def r2_ST(self):
        return self.__r2_ST

    @r2_ST.setter
    def r2_ST(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ST__r2_ST", None)
        self.__r2_ST = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CD"):
                opp_val = getattr(old_value, "r2_CD", None)
                if opp_val == self:
                    setattr(old_value, "r2_CD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CD"):
                opp_val = getattr(value, "r2_CD", None)
                setattr(value, "r2_CD", self)

    @property
    def r2_ST4(self):
        return self.__r2_ST4

    @r2_ST4.setter
    def r2_ST4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ST__r2_ST4", None)
        self.__r2_ST4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CD3"):
                opp_val = getattr(old_value, "r2_CD3", None)
                if opp_val == self:
                    setattr(old_value, "r2_CD3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CD3"):
                opp_val = getattr(value, "r2_CD3", None)
                setattr(value, "r2_CD3", self)

class r2_BL(ANY):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class r2_ED(ANY):

    def __init__(self, data: str, integrityCheckAlgorithm: str, language: str, mediaType: str, value: str, integrityCheck: str, charset: str, compression: str, r2_ED: "r2_EObject" = None, r2_ED12: "r2_TEL" = None, r2_ED14: "r2_ST" = None):
        self.data = data
        self.integrityCheckAlgorithm = integrityCheckAlgorithm
        self.language = language
        self.mediaType = mediaType
        self.value = value
        self.integrityCheck = integrityCheck
        self.charset = charset
        self.compression = compression
        self.r2_ED = r2_ED
        self.r2_ED12 = r2_ED12
        self.r2_ED14 = r2_ED14
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def mediaType(self):
        return self.__mediaType

    @mediaType.setter
    def mediaType(self, mediaType: str):
        self.__mediaType = mediaType


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def charset(self):
        return self.__charset

    @charset.setter
    def charset(self, charset: str):
        self.__charset = charset


    @property
    def compression(self):
        return self.__compression

    @compression.setter
    def compression(self, compression: str):
        self.__compression = compression


    @property
    def integrityCheckAlgorithm(self):
        return self.__integrityCheckAlgorithm

    @integrityCheckAlgorithm.setter
    def integrityCheckAlgorithm(self, integrityCheckAlgorithm: str):
        self.__integrityCheckAlgorithm = integrityCheckAlgorithm


    @property
    def integrityCheck(self):
        return self.__integrityCheck

    @integrityCheck.setter
    def integrityCheck(self, integrityCheck: str):
        self.__integrityCheck = integrityCheck


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def r2_ED(self):
        return self.__r2_ED

    @r2_ED.setter
    def r2_ED(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ED__r2_ED", None)
        self.__r2_ED = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_EObject"):
                opp_val = getattr(old_value, "r2_EObject", None)
                if opp_val == self:
                    setattr(old_value, "r2_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_EObject"):
                opp_val = getattr(value, "r2_EObject", None)
                setattr(value, "r2_EObject", self)

    @property
    def r2_ED14(self):
        return self.__r2_ED14

    @r2_ED14.setter
    def r2_ED14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ED__r2_ED14", None)
        self.__r2_ED14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_ST15"):
                opp_val = getattr(old_value, "r2_ST15", None)
                if opp_val == self:
                    setattr(old_value, "r2_ST15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_ST15"):
                opp_val = getattr(value, "r2_ST15", None)
                setattr(value, "r2_ST15", self)

    @property
    def r2_ED12(self):
        return self.__r2_ED12

    @r2_ED12.setter
    def r2_ED12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ED__r2_ED12", None)
        self.__r2_ED12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_TEL"):
                opp_val = getattr(old_value, "r2_TEL", None)
                if opp_val == self:
                    setattr(old_value, "r2_TEL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_TEL"):
                opp_val = getattr(value, "r2_TEL", None)
                setattr(value, "r2_TEL", self)

class r2_II(ANY):

    def __init__(self, extension: str, identifierName: str, root: str):
        self.extension = extension
        self.identifierName = identifierName
        self.root = root
        
        pass
    @property
    def identifierName(self):
        return self.__identifierName

    @identifierName.setter
    def identifierName(self, identifierName: str):
        self.__identifierName = identifierName


    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension


    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root: str):
        self.__root = root


class r2_CS(ANY):

    def __init__(self, code: str):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class r2_QSET(ANY):

    pass
class r2_TEL(ANY):

    def __init__(self, capabilities: str, use: str, value: str, r2_TEL: "r2_ED" = None):
        self.capabilities = capabilities
        self.use = use
        self.value = value
        self.r2_TEL = r2_TEL
        
        pass
    @property
    def capabilities(self):
        return self.__capabilities

    @capabilities.setter
    def capabilities(self, capabilities: str):
        self.__capabilities = capabilities


    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def r2_TEL(self):
        return self.__r2_TEL

    @r2_TEL.setter
    def r2_TEL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_TEL__r2_TEL", None)
        self.__r2_TEL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_ED12"):
                opp_val = getattr(old_value, "r2_ED12", None)
                if opp_val == self:
                    setattr(old_value, "r2_ED12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_ED12"):
                opp_val = getattr(value, "r2_ED12", None)
                setattr(value, "r2_ED12", self)

class r2_CD(ANY):

    def __init__(self, code: str, codeSystem: str, codeSystemName: str, codeSystemVersion: str, valueSet: str, valueSetVersion: str, r2_CD9: "r2_CO" = None, r2_CD7: "r2_CD" = None, r2_CD5: set["r2_CD"] = None, r2_CD: "r2_ST" = None, r2_CD3: "r2_ST" = None):
        self.code = code
        self.codeSystem = codeSystem
        self.codeSystemName = codeSystemName
        self.codeSystemVersion = codeSystemVersion
        self.valueSet = valueSet
        self.valueSetVersion = valueSetVersion
        self.r2_CD9 = r2_CD9
        self.r2_CD7 = r2_CD7
        self.r2_CD5 = r2_CD5 if r2_CD5 is not None else set()
        self.r2_CD = r2_CD
        self.r2_CD3 = r2_CD3
        
        pass
    @property
    def codeSystemName(self):
        return self.__codeSystemName

    @codeSystemName.setter
    def codeSystemName(self, codeSystemName: str):
        self.__codeSystemName = codeSystemName


    @property
    def valueSet(self):
        return self.__valueSet

    @valueSet.setter
    def valueSet(self, valueSet: str):
        self.__valueSet = valueSet


    @property
    def codeSystemVersion(self):
        return self.__codeSystemVersion

    @codeSystemVersion.setter
    def codeSystemVersion(self, codeSystemVersion: str):
        self.__codeSystemVersion = codeSystemVersion


    @property
    def valueSetVersion(self):
        return self.__valueSetVersion

    @valueSetVersion.setter
    def valueSetVersion(self, valueSetVersion: str):
        self.__valueSetVersion = valueSetVersion


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def codeSystem(self):
        return self.__codeSystem

    @codeSystem.setter
    def codeSystem(self, codeSystem: str):
        self.__codeSystem = codeSystem


    @property
    def r2_CD3(self):
        return self.__r2_CD3

    @r2_CD3.setter
    def r2_CD3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CD__r2_CD3", None)
        self.__r2_CD3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_ST4"):
                opp_val = getattr(old_value, "r2_ST4", None)
                if opp_val == self:
                    setattr(old_value, "r2_ST4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_ST4"):
                opp_val = getattr(value, "r2_ST4", None)
                setattr(value, "r2_ST4", self)

    @property
    def r2_CD5(self):
        return self.__r2_CD5

    @r2_CD5.setter
    def r2_CD5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CD__r2_CD5", None)
        self.__r2_CD5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r2_CD7"):
                    opp_val = getattr(item, "r2_CD7", None)
                    
                    if opp_val == self:
                        setattr(item, "r2_CD7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r2_CD7"):
                    opp_val = getattr(item, "r2_CD7", None)
                    
                    setattr(item, "r2_CD7", self)
                    

    @property
    def r2_CD7(self):
        return self.__r2_CD7

    @r2_CD7.setter
    def r2_CD7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CD__r2_CD7", None)
        self.__r2_CD7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CD5"):
                opp_val = getattr(old_value, "r2_CD5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CD5"):
                opp_val = getattr(value, "r2_CD5", None)
                if opp_val is None:
                    setattr(value, "r2_CD5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r2_CD(self):
        return self.__r2_CD

    @r2_CD.setter
    def r2_CD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CD__r2_CD", None)
        self.__r2_CD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_ST"):
                opp_val = getattr(old_value, "r2_ST", None)
                if opp_val == self:
                    setattr(old_value, "r2_ST", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_ST"):
                opp_val = getattr(value, "r2_ST", None)
                setattr(value, "r2_ST", self)

    @property
    def r2_CD9(self):
        return self.__r2_CD9

    @r2_CD9.setter
    def r2_CD9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_CD__r2_CD9", None)
        self.__r2_CD9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_CO"):
                opp_val = getattr(old_value, "r2_CO", None)
                if opp_val == self:
                    setattr(old_value, "r2_CO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_CO"):
                opp_val = getattr(value, "r2_CO", None)
                setattr(value, "r2_CO", self)

class r2_EN(ANY):

    def __init__(self, use: str, r2_EN: set["r2_ENXP"] = None):
        self.use = use
        self.r2_EN = r2_EN if r2_EN is not None else set()
        
        pass
    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


    @property
    def r2_EN(self):
        return self.__r2_EN

    @r2_EN.setter
    def r2_EN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_EN__r2_EN", None)
        self.__r2_EN = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r2_ENXP"):
                    opp_val = getattr(item, "r2_ENXP", None)
                    
                    if opp_val == self:
                        setattr(item, "r2_ENXP", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r2_ENXP"):
                    opp_val = getattr(item, "r2_ENXP", None)
                    
                    setattr(item, "r2_ENXP", self)
                    

class r2_AD(ANY):

    def __init__(self, use: str, r2_AD: set["r2_ADXP"] = None):
        self.use = use
        self.r2_AD = r2_AD if r2_AD is not None else set()
        
        pass
    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


    @property
    def r2_AD(self):
        return self.__r2_AD

    @r2_AD.setter
    def r2_AD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_AD__r2_AD", None)
        self.__r2_AD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r2_ADXP"):
                    opp_val = getattr(item, "r2_ADXP", None)
                    
                    if opp_val == self:
                        setattr(item, "r2_ADXP", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r2_ADXP"):
                    opp_val = getattr(item, "r2_ADXP", None)
                    
                    setattr(item, "r2_ADXP", self)
                    

class r2_ADXP(XP):

    def __init__(self, type: str, r2_ADXP: "r2_AD" = None):
        self.type = type
        self.r2_ADXP = r2_ADXP
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def r2_ADXP(self):
        return self.__r2_ADXP

    @r2_ADXP.setter
    def r2_ADXP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r2_ADXP__r2_ADXP", None)
        self.__r2_ADXP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r2_AD"):
                opp_val = getattr(old_value, "r2_AD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r2_AD"):
                opp_val = getattr(value, "r2_AD", None)
                if opp_val is None:
                    setattr(value, "r2_AD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
