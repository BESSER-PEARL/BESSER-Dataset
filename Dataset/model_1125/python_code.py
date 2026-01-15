from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FIELD_FORMAT(Enum):
    AU = "AU"
    BMP = "BMP"
    JPEG = "JPEG"
    MJPEG = "MJPEG"
    MPEG1 = "MPEG1"
    MPEG2 = "MPEG2"
    MP2 = "MP2"
    MP3 = "MP3"
    MP4 = "MP4"
    RAW = "RAW"
    WAV = "WAV"
    JAUS_MESSAGE = "JAUS_MESSAGE"
    XML = "XML"
    RNC = "RNC"
    RNG = "RNG"
    XSD = "XSD"
    USER_DEFINED = "USER_DEFINED"
class UNIT(Enum):
    CUBIC_METER = "CUBIC_METER"
    METER_PER_SEC = "METER_PER_SEC"
    METER_PER_SEC_SQR = "METER_PER_SEC_SQR"
    RECIPROCAL_METER = "RECIPROCAL_METER"
    KG_PER_CUBIC_METER = "KG_PER_CUBIC_METER"
    CUBICMETERPERKG = "CUBICMETERPERKG"
    AMPPERSQRMETER = "AMPPERSQRMETER"
    AMP_PER_METER = "AMP_PER_METER"
    MOLE_PER_CUBIC_METER = "MOLE_PER_CUBIC_METER"
    CANDELA_PER_SQUARE_METER = "CANDELA_PER_SQUARE_METER"
    RADIAN = "RADIAN"
    STE_RAD = "STE_RAD"
    HRZ = "HRZ"
    NEWTON = "NEWTON"
    PASCAL = "PASCAL"
    JOULE = "JOULE"
    WATT = "WATT"
    COULOMB = "COULOMB"
    VOLT = "VOLT"
    FARAD = "FARAD"
    OHM = "OHM"
    SIEMENS = "SIEMENS"
    WEBER = "WEBER"
    TESLA = "TESLA"
    HENRY = "HENRY"
    CELSIUS = "CELSIUS"
    LUMEN = "LUMEN"
    LUX = "LUX"
    BECQUEREL = "BECQUEREL"
    SIEVERT = "SIEVERT"
    KATAL = "KATAL"
    PASCAL_SEC = "PASCAL_SEC"
    NEWTON_METER = "NEWTON_METER"
    NEWTON_PER_METER = "NEWTON_PER_METER"
    RAD_PER_SEC = "RAD_PER_SEC"
    RAD_PER_SEC_SQR = "RAD_PER_SEC_SQR"
    WATT_PER_SQR_METER = "WATT_PER_SQR_METER"
    JOULE_PER_KELVIN = "JOULE_PER_KELVIN"
    METER = "METER"
    KG = "KG"
    SEC = "SEC"
    AMP = "AMP"
    KELVIN = "KELVIN"
    MOLE = "MOLE"
    CANDELA = "CANDELA"
    ONE = "ONE"
    SQR_METER = "SQR_METER"
    GRAY_PER_SEC = "GRAY_PER_SEC"
    WATT_PER_SQR_METER_STERAD = "WATT_PER_SQR_METER_STERAD"
    KATAL_PER_CUBIC_METER = "KATAL_PER_CUBIC_METER"
    MIN = "MIN"
    HOUR = "HOUR"
    DAY = "DAY"
    DEGREE = "DEGREE"
    LTR = "LTR"
    MTON = "MTON"
    NEPER = "NEPER"
    BEL = "BEL"
    NMILE = "NMILE"
    KNOT = "KNOT"
    ARE = "ARE"
    HECTARE = "HECTARE"
    BAR = "BAR"
    ANGSROM = "ANGSROM"
    BARN = "BARN"
    CURIE = "CURIE"
    ROENTGEN = "ROENTGEN"
    RAD = "RAD"
    REM = "REM"
    JOULE_PER_KG = "JOULE_PER_KG"
    WATT_PER_METER_KELVIN = "WATT_PER_METER_KELVIN"
    JOULES_PER_CUBIC_METER = "JOULES_PER_CUBIC_METER"
    VOLT_PER_METER = "VOLT_PER_METER"
    COULOMB_PER_CUBIC_METER = "COULOMB_PER_CUBIC_METER"
    COULOMB_PER_SQR_METER = "COULOMB_PER_SQR_METER"
    FARAD_PER_METER = "FARAD_PER_METER"
    HENRY_PER_METER = "HENRY_PER_METER"
    JOULE_PER_MOLE = "JOULE_PER_MOLE"
    JOULE_PER_MOLE_KELVIN = "JOULE_PER_MOLE_KELVIN"
    COULOMB_PER_KG = "COULOMB_PER_KG"


############################################
# Definition of Classes
############################################

class cjsidl_taggedItemDef:

    pass
class containerDef:

    pass
class cjsidl_subField:

    def __init__(self, comment: str, name: str, fromIndex: str, toIndex: str, cjsidl_subField: "cjsidl_bitfieldDef" = None, cjsidl_subField380: "cjsidl_valueSetDef" = None):
        self.comment = comment
        self.name = name
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.cjsidl_subField = cjsidl_subField
        self.cjsidl_subField380 = cjsidl_subField380
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def fromIndex(self) -> str:
        return self.__fromIndex

    @fromIndex.setter
    def fromIndex(self, fromIndex: str):
        self.__fromIndex = fromIndex

    @property
    def toIndex(self) -> str:
        return self.__toIndex

    @toIndex.setter
    def toIndex(self, toIndex: str):
        self.__toIndex = toIndex

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_subField(self):
        return self.__cjsidl_subField

    @cjsidl_subField.setter
    def cjsidl_subField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_subField__cjsidl_subField", None)
        self.__cjsidl_subField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_bitfieldDef354"):
                opp_val = getattr(old_value, "cjsidl_bitfieldDef354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_bitfieldDef354"):
                opp_val = getattr(value, "cjsidl_bitfieldDef354", None)
                if opp_val is None:
                    setattr(value, "cjsidl_bitfieldDef354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_subField380(self):
        return self.__cjsidl_subField380

    @cjsidl_subField380.setter
    def cjsidl_subField380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_subField__cjsidl_subField380", None)
        self.__cjsidl_subField380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_valueSetDef381"):
                opp_val = getattr(old_value, "cjsidl_valueSetDef381", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_valueSetDef381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_valueSetDef381"):
                opp_val = getattr(value, "cjsidl_valueSetDef381", None)
                setattr(value, "cjsidl_valueSetDef381", self)

class cjsidl_formatEnumDef:

    def __init__(self, index: str, fieldFormat: str, fieldFormatStr: str, cjsidl_formatEnumDef: "cjsidl_varFormatField" = None, cjsidl_formatEnumDef345: "cjsidl_constReference" = None, cjsidl_formatEnumDef348: "cjsidl_scopedConstId" = None):
        self.index = index
        self.fieldFormat = fieldFormat
        self.fieldFormatStr = fieldFormatStr
        self.cjsidl_formatEnumDef = cjsidl_formatEnumDef
        self.cjsidl_formatEnumDef345 = cjsidl_formatEnumDef345
        self.cjsidl_formatEnumDef348 = cjsidl_formatEnumDef348
        
    @property
    def fieldFormatStr(self) -> str:
        return self.__fieldFormatStr

    @fieldFormatStr.setter
    def fieldFormatStr(self, fieldFormatStr: str):
        self.__fieldFormatStr = fieldFormatStr

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def fieldFormat(self) -> str:
        return self.__fieldFormat

    @fieldFormat.setter
    def fieldFormat(self, fieldFormat: str):
        self.__fieldFormat = fieldFormat

    @property
    def cjsidl_formatEnumDef345(self):
        return self.__cjsidl_formatEnumDef345

    @cjsidl_formatEnumDef345.setter
    def cjsidl_formatEnumDef345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_formatEnumDef__cjsidl_formatEnumDef345", None)
        self.__cjsidl_formatEnumDef345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference346"):
                opp_val = getattr(old_value, "cjsidl_constReference346", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference346"):
                opp_val = getattr(value, "cjsidl_constReference346", None)
                setattr(value, "cjsidl_constReference346", self)

    @property
    def cjsidl_formatEnumDef348(self):
        return self.__cjsidl_formatEnumDef348

    @cjsidl_formatEnumDef348.setter
    def cjsidl_formatEnumDef348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_formatEnumDef__cjsidl_formatEnumDef348", None)
        self.__cjsidl_formatEnumDef348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId349"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId349", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId349"):
                opp_val = getattr(value, "cjsidl_scopedConstId349", None)
                setattr(value, "cjsidl_scopedConstId349", self)

    @property
    def cjsidl_formatEnumDef(self):
        return self.__cjsidl_formatEnumDef

    @cjsidl_formatEnumDef.setter
    def cjsidl_formatEnumDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_formatEnumDef__cjsidl_formatEnumDef", None)
        self.__cjsidl_formatEnumDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varFormatField343"):
                opp_val = getattr(old_value, "cjsidl_varFormatField343", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varFormatField343"):
                opp_val = getattr(value, "cjsidl_varFormatField343", None)
                if opp_val is None:
                    setattr(value, "cjsidl_varFormatField343", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_valueRange:

    def __init__(self, upperLim: str, upperLimit_type: str, comment: str, lowerLimit_type: str, lowerLim: str, cjsidl_valueRange359: "cjsidl_scopedConstId" = None, cjsidl_valueRange362: "cjsidl_constReference" = None, cjsidl_valueRange365: "cjsidl_scopedConstId" = None, cjsidl_valueRange: "cjsidl_varFormatField" = None, cjsidl_valueRange356: "cjsidl_constReference" = None):
        self.upperLim = upperLim
        self.upperLimit_type = upperLimit_type
        self.comment = comment
        self.lowerLimit_type = lowerLimit_type
        self.lowerLim = lowerLim
        self.cjsidl_valueRange359 = cjsidl_valueRange359
        self.cjsidl_valueRange362 = cjsidl_valueRange362
        self.cjsidl_valueRange365 = cjsidl_valueRange365
        self.cjsidl_valueRange = cjsidl_valueRange
        self.cjsidl_valueRange356 = cjsidl_valueRange356
        
    @property
    def lowerLimit_type(self) -> str:
        return self.__lowerLimit_type

    @lowerLimit_type.setter
    def lowerLimit_type(self, lowerLimit_type: str):
        self.__lowerLimit_type = lowerLimit_type

    @property
    def upperLimit_type(self) -> str:
        return self.__upperLimit_type

    @upperLimit_type.setter
    def upperLimit_type(self, upperLimit_type: str):
        self.__upperLimit_type = upperLimit_type

    @property
    def upperLim(self) -> str:
        return self.__upperLim

    @upperLim.setter
    def upperLim(self, upperLim: str):
        self.__upperLim = upperLim

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def lowerLim(self) -> str:
        return self.__lowerLim

    @lowerLim.setter
    def lowerLim(self, lowerLim: str):
        self.__lowerLim = lowerLim

    @property
    def cjsidl_valueRange362(self):
        return self.__cjsidl_valueRange362

    @cjsidl_valueRange362.setter
    def cjsidl_valueRange362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueRange__cjsidl_valueRange362", None)
        self.__cjsidl_valueRange362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference363"):
                opp_val = getattr(old_value, "cjsidl_constReference363", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference363"):
                opp_val = getattr(value, "cjsidl_constReference363", None)
                setattr(value, "cjsidl_constReference363", self)

    @property
    def cjsidl_valueRange359(self):
        return self.__cjsidl_valueRange359

    @cjsidl_valueRange359.setter
    def cjsidl_valueRange359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueRange__cjsidl_valueRange359", None)
        self.__cjsidl_valueRange359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId360"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId360", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId360"):
                opp_val = getattr(value, "cjsidl_scopedConstId360", None)
                setattr(value, "cjsidl_scopedConstId360", self)

    @property
    def cjsidl_valueRange356(self):
        return self.__cjsidl_valueRange356

    @cjsidl_valueRange356.setter
    def cjsidl_valueRange356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueRange__cjsidl_valueRange356", None)
        self.__cjsidl_valueRange356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference357"):
                opp_val = getattr(old_value, "cjsidl_constReference357", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference357"):
                opp_val = getattr(value, "cjsidl_constReference357", None)
                setattr(value, "cjsidl_constReference357", self)

    @property
    def cjsidl_valueRange(self):
        return self.__cjsidl_valueRange

    @cjsidl_valueRange.setter
    def cjsidl_valueRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueRange__cjsidl_valueRange", None)
        self.__cjsidl_valueRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varFormatField341"):
                opp_val = getattr(old_value, "cjsidl_varFormatField341", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_varFormatField341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varFormatField341"):
                opp_val = getattr(value, "cjsidl_varFormatField341", None)
                setattr(value, "cjsidl_varFormatField341", self)

    @property
    def cjsidl_valueRange365(self):
        return self.__cjsidl_valueRange365

    @cjsidl_valueRange365.setter
    def cjsidl_valueRange365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueRange__cjsidl_valueRange365", None)
        self.__cjsidl_valueRange365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId366"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId366", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId366"):
                opp_val = getattr(value, "cjsidl_scopedConstId366", None)
                setattr(value, "cjsidl_scopedConstId366", self)

class cjsidl_valueSpec:

    def __init__(self, comment: str, name: str, value: str):
        self.comment = comment
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cjsidl_taggedUnitsEnum:

    def __init__(self, fieldUnit: str, const_tag: str, name: str, cjsidl_taggedUnitsEnum337: "cjsidl_valueSetDef" = None, cjsidl_taggedUnitsEnum339: "cjsidl_scaledRangeDef" = None, cjsidl_taggedUnitsEnum: "cjsidl_varField" = None, cjsidl_taggedUnitsEnum328: "cjsidl_constReference" = None, cjsidl_taggedUnitsEnum331: "cjsidl_scopedConstId" = None, cjsidl_taggedUnitsEnum334: "cjsidl_simpleNumericType" = None):
        self.fieldUnit = fieldUnit
        self.const_tag = const_tag
        self.name = name
        self.cjsidl_taggedUnitsEnum337 = cjsidl_taggedUnitsEnum337
        self.cjsidl_taggedUnitsEnum339 = cjsidl_taggedUnitsEnum339
        self.cjsidl_taggedUnitsEnum = cjsidl_taggedUnitsEnum
        self.cjsidl_taggedUnitsEnum328 = cjsidl_taggedUnitsEnum328
        self.cjsidl_taggedUnitsEnum331 = cjsidl_taggedUnitsEnum331
        self.cjsidl_taggedUnitsEnum334 = cjsidl_taggedUnitsEnum334
        
    @property
    def const_tag(self) -> str:
        return self.__const_tag

    @const_tag.setter
    def const_tag(self, const_tag: str):
        self.__const_tag = const_tag

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fieldUnit(self) -> str:
        return self.__fieldUnit

    @fieldUnit.setter
    def fieldUnit(self, fieldUnit: str):
        self.__fieldUnit = fieldUnit

    @property
    def cjsidl_taggedUnitsEnum(self):
        return self.__cjsidl_taggedUnitsEnum

    @cjsidl_taggedUnitsEnum.setter
    def cjsidl_taggedUnitsEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum", None)
        self.__cjsidl_taggedUnitsEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varField314"):
                opp_val = getattr(old_value, "cjsidl_varField314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varField314"):
                opp_val = getattr(value, "cjsidl_varField314", None)
                if opp_val is None:
                    setattr(value, "cjsidl_varField314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_taggedUnitsEnum337(self):
        return self.__cjsidl_taggedUnitsEnum337

    @cjsidl_taggedUnitsEnum337.setter
    def cjsidl_taggedUnitsEnum337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum337", None)
        self.__cjsidl_taggedUnitsEnum337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_valueSetDef"):
                opp_val = getattr(old_value, "cjsidl_valueSetDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_valueSetDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_valueSetDef"):
                opp_val = getattr(value, "cjsidl_valueSetDef", None)
                setattr(value, "cjsidl_valueSetDef", self)

    @property
    def cjsidl_taggedUnitsEnum334(self):
        return self.__cjsidl_taggedUnitsEnum334

    @cjsidl_taggedUnitsEnum334.setter
    def cjsidl_taggedUnitsEnum334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum334", None)
        self.__cjsidl_taggedUnitsEnum334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_simpleNumericType335"):
                opp_val = getattr(old_value, "cjsidl_simpleNumericType335", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_simpleNumericType335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_simpleNumericType335"):
                opp_val = getattr(value, "cjsidl_simpleNumericType335", None)
                setattr(value, "cjsidl_simpleNumericType335", self)

    @property
    def cjsidl_taggedUnitsEnum339(self):
        return self.__cjsidl_taggedUnitsEnum339

    @cjsidl_taggedUnitsEnum339.setter
    def cjsidl_taggedUnitsEnum339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum339", None)
        self.__cjsidl_taggedUnitsEnum339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scaledRangeDef"):
                opp_val = getattr(old_value, "cjsidl_scaledRangeDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scaledRangeDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scaledRangeDef"):
                opp_val = getattr(value, "cjsidl_scaledRangeDef", None)
                setattr(value, "cjsidl_scaledRangeDef", self)

    @property
    def cjsidl_taggedUnitsEnum331(self):
        return self.__cjsidl_taggedUnitsEnum331

    @cjsidl_taggedUnitsEnum331.setter
    def cjsidl_taggedUnitsEnum331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum331", None)
        self.__cjsidl_taggedUnitsEnum331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId332"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId332", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId332"):
                opp_val = getattr(value, "cjsidl_scopedConstId332", None)
                setattr(value, "cjsidl_scopedConstId332", self)

    @property
    def cjsidl_taggedUnitsEnum328(self):
        return self.__cjsidl_taggedUnitsEnum328

    @cjsidl_taggedUnitsEnum328.setter
    def cjsidl_taggedUnitsEnum328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum328", None)
        self.__cjsidl_taggedUnitsEnum328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference329"):
                opp_val = getattr(old_value, "cjsidl_constReference329", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference329"):
                opp_val = getattr(value, "cjsidl_constReference329", None)
                setattr(value, "cjsidl_constReference329", self)

class cjsidl_scaledRangeDef:

    def __init__(self, interp: str, lowerLim: str, upperLim: str, function: str, cjsidl_scaledRangeDef: "cjsidl_taggedUnitsEnum" = None, cjsidl_scaledRangeDef368: "cjsidl_constReference" = None, cjsidl_scaledRangeDef371: "cjsidl_scopedConstId" = None, cjsidl_scaledRangeDef374: "cjsidl_constReference" = None, cjsidl_scaledRangeDef377: "cjsidl_scopedConstId" = None):
        self.interp = interp
        self.lowerLim = lowerLim
        self.upperLim = upperLim
        self.function = function
        self.cjsidl_scaledRangeDef = cjsidl_scaledRangeDef
        self.cjsidl_scaledRangeDef368 = cjsidl_scaledRangeDef368
        self.cjsidl_scaledRangeDef371 = cjsidl_scaledRangeDef371
        self.cjsidl_scaledRangeDef374 = cjsidl_scaledRangeDef374
        self.cjsidl_scaledRangeDef377 = cjsidl_scaledRangeDef377
        
    @property
    def upperLim(self) -> str:
        return self.__upperLim

    @upperLim.setter
    def upperLim(self, upperLim: str):
        self.__upperLim = upperLim

    @property
    def interp(self) -> str:
        return self.__interp

    @interp.setter
    def interp(self, interp: str):
        self.__interp = interp

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def lowerLim(self) -> str:
        return self.__lowerLim

    @lowerLim.setter
    def lowerLim(self, lowerLim: str):
        self.__lowerLim = lowerLim

    @property
    def cjsidl_scaledRangeDef(self):
        return self.__cjsidl_scaledRangeDef

    @cjsidl_scaledRangeDef.setter
    def cjsidl_scaledRangeDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scaledRangeDef__cjsidl_scaledRangeDef", None)
        self.__cjsidl_scaledRangeDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedUnitsEnum339"):
                opp_val = getattr(old_value, "cjsidl_taggedUnitsEnum339", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedUnitsEnum339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedUnitsEnum339"):
                opp_val = getattr(value, "cjsidl_taggedUnitsEnum339", None)
                setattr(value, "cjsidl_taggedUnitsEnum339", self)

    @property
    def cjsidl_scaledRangeDef377(self):
        return self.__cjsidl_scaledRangeDef377

    @cjsidl_scaledRangeDef377.setter
    def cjsidl_scaledRangeDef377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scaledRangeDef__cjsidl_scaledRangeDef377", None)
        self.__cjsidl_scaledRangeDef377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId378"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId378", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId378"):
                opp_val = getattr(value, "cjsidl_scopedConstId378", None)
                setattr(value, "cjsidl_scopedConstId378", self)

    @property
    def cjsidl_scaledRangeDef368(self):
        return self.__cjsidl_scaledRangeDef368

    @cjsidl_scaledRangeDef368.setter
    def cjsidl_scaledRangeDef368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scaledRangeDef__cjsidl_scaledRangeDef368", None)
        self.__cjsidl_scaledRangeDef368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference369"):
                opp_val = getattr(old_value, "cjsidl_constReference369", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference369", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference369"):
                opp_val = getattr(value, "cjsidl_constReference369", None)
                setattr(value, "cjsidl_constReference369", self)

    @property
    def cjsidl_scaledRangeDef374(self):
        return self.__cjsidl_scaledRangeDef374

    @cjsidl_scaledRangeDef374.setter
    def cjsidl_scaledRangeDef374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scaledRangeDef__cjsidl_scaledRangeDef374", None)
        self.__cjsidl_scaledRangeDef374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference375"):
                opp_val = getattr(old_value, "cjsidl_constReference375", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference375"):
                opp_val = getattr(value, "cjsidl_constReference375", None)
                setattr(value, "cjsidl_constReference375", self)

    @property
    def cjsidl_scaledRangeDef371(self):
        return self.__cjsidl_scaledRangeDef371

    @cjsidl_scaledRangeDef371.setter
    def cjsidl_scaledRangeDef371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scaledRangeDef__cjsidl_scaledRangeDef371", None)
        self.__cjsidl_scaledRangeDef371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId372"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId372", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId372"):
                opp_val = getattr(value, "cjsidl_scopedConstId372", None)
                setattr(value, "cjsidl_scopedConstId372", self)

class cjsidl_valueSetDef:

    def __init__(self, offset: str, cjsidl_valueSetDef: "cjsidl_taggedUnitsEnum" = None, cjsidl_valueSetDef351: set["cjsidl_EObject"] = None, cjsidl_valueSetDef381: "cjsidl_subField" = None):
        self.offset = offset
        self.cjsidl_valueSetDef = cjsidl_valueSetDef
        self.cjsidl_valueSetDef351 = cjsidl_valueSetDef351 if cjsidl_valueSetDef351 is not None else set()
        self.cjsidl_valueSetDef381 = cjsidl_valueSetDef381
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def cjsidl_valueSetDef381(self):
        return self.__cjsidl_valueSetDef381

    @cjsidl_valueSetDef381.setter
    def cjsidl_valueSetDef381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueSetDef__cjsidl_valueSetDef381", None)
        self.__cjsidl_valueSetDef381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_subField380"):
                opp_val = getattr(old_value, "cjsidl_subField380", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_subField380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_subField380"):
                opp_val = getattr(value, "cjsidl_subField380", None)
                setattr(value, "cjsidl_subField380", self)

    @property
    def cjsidl_valueSetDef(self):
        return self.__cjsidl_valueSetDef

    @cjsidl_valueSetDef.setter
    def cjsidl_valueSetDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueSetDef__cjsidl_valueSetDef", None)
        self.__cjsidl_valueSetDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedUnitsEnum337"):
                opp_val = getattr(old_value, "cjsidl_taggedUnitsEnum337", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedUnitsEnum337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedUnitsEnum337"):
                opp_val = getattr(value, "cjsidl_taggedUnitsEnum337", None)
                setattr(value, "cjsidl_taggedUnitsEnum337", self)

    @property
    def cjsidl_valueSetDef351(self):
        return self.__cjsidl_valueSetDef351

    @cjsidl_valueSetDef351.setter
    def cjsidl_valueSetDef351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_valueSetDef__cjsidl_valueSetDef351", None)
        self.__cjsidl_valueSetDef351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_EObject352"):
                    opp_val = getattr(item, "cjsidl_EObject352", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_EObject352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_EObject352"):
                    opp_val = getattr(item, "cjsidl_EObject352", None)
                    
                    setattr(item, "cjsidl_EObject352", self)
                    

class cjsidl_scopedConstId:

    pass
class cjsidl_constReference:

    def __init__(self, comment: str, cjsidl_constReference303: "cjsidl_varLenString" = None, cjsidl_constReference: "cjsidl_fixedLenString" = None, cjsidl_constReference297: "cjsidl_varLenString" = None, cjsidl_constReference317: "cjsidl_varLenField" = None, cjsidl_constReference323: "cjsidl_varLenField" = None, cjsidl_constReference329: "cjsidl_taggedUnitsEnum" = None, cjsidl_constReference363: "cjsidl_valueRange" = None, cjsidl_constReference346: "cjsidl_formatEnumDef" = None, cjsidl_constReference357: "cjsidl_valueRange" = None, cjsidl_constReference384: "cjsidl_listDef" = None, cjsidl_constReference369: "cjsidl_scaledRangeDef" = None, cjsidl_constReference375: "cjsidl_scaledRangeDef" = None, cjsidl_constReference390: "cjsidl_listDef" = None, cjsidl_constReference402: "cjsidl_variantDef" = None, cjsidl_constReference408: "cjsidl_variantDef" = None, cjsidl_constReference454: "cjsidl_constDef" = None):
        self.comment = comment
        self.cjsidl_constReference303 = cjsidl_constReference303
        self.cjsidl_constReference = cjsidl_constReference
        self.cjsidl_constReference297 = cjsidl_constReference297
        self.cjsidl_constReference317 = cjsidl_constReference317
        self.cjsidl_constReference323 = cjsidl_constReference323
        self.cjsidl_constReference329 = cjsidl_constReference329
        self.cjsidl_constReference363 = cjsidl_constReference363
        self.cjsidl_constReference346 = cjsidl_constReference346
        self.cjsidl_constReference357 = cjsidl_constReference357
        self.cjsidl_constReference384 = cjsidl_constReference384
        self.cjsidl_constReference369 = cjsidl_constReference369
        self.cjsidl_constReference375 = cjsidl_constReference375
        self.cjsidl_constReference390 = cjsidl_constReference390
        self.cjsidl_constReference402 = cjsidl_constReference402
        self.cjsidl_constReference408 = cjsidl_constReference408
        self.cjsidl_constReference454 = cjsidl_constReference454
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_constReference408(self):
        return self.__cjsidl_constReference408

    @cjsidl_constReference408.setter
    def cjsidl_constReference408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference408", None)
        self.__cjsidl_constReference408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_variantDef407"):
                opp_val = getattr(old_value, "cjsidl_variantDef407", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_variantDef407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_variantDef407"):
                opp_val = getattr(value, "cjsidl_variantDef407", None)
                setattr(value, "cjsidl_variantDef407", self)

    @property
    def cjsidl_constReference346(self):
        return self.__cjsidl_constReference346

    @cjsidl_constReference346.setter
    def cjsidl_constReference346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference346", None)
        self.__cjsidl_constReference346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_formatEnumDef345"):
                opp_val = getattr(old_value, "cjsidl_formatEnumDef345", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_formatEnumDef345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_formatEnumDef345"):
                opp_val = getattr(value, "cjsidl_formatEnumDef345", None)
                setattr(value, "cjsidl_formatEnumDef345", self)

    @property
    def cjsidl_constReference402(self):
        return self.__cjsidl_constReference402

    @cjsidl_constReference402.setter
    def cjsidl_constReference402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference402", None)
        self.__cjsidl_constReference402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_variantDef401"):
                opp_val = getattr(old_value, "cjsidl_variantDef401", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_variantDef401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_variantDef401"):
                opp_val = getattr(value, "cjsidl_variantDef401", None)
                setattr(value, "cjsidl_variantDef401", self)

    @property
    def cjsidl_constReference390(self):
        return self.__cjsidl_constReference390

    @cjsidl_constReference390.setter
    def cjsidl_constReference390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference390", None)
        self.__cjsidl_constReference390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_listDef389"):
                opp_val = getattr(old_value, "cjsidl_listDef389", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_listDef389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_listDef389"):
                opp_val = getattr(value, "cjsidl_listDef389", None)
                setattr(value, "cjsidl_listDef389", self)

    @property
    def cjsidl_constReference357(self):
        return self.__cjsidl_constReference357

    @cjsidl_constReference357.setter
    def cjsidl_constReference357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference357", None)
        self.__cjsidl_constReference357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_valueRange356"):
                opp_val = getattr(old_value, "cjsidl_valueRange356", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_valueRange356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_valueRange356"):
                opp_val = getattr(value, "cjsidl_valueRange356", None)
                setattr(value, "cjsidl_valueRange356", self)

    @property
    def cjsidl_constReference384(self):
        return self.__cjsidl_constReference384

    @cjsidl_constReference384.setter
    def cjsidl_constReference384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference384", None)
        self.__cjsidl_constReference384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_listDef383"):
                opp_val = getattr(old_value, "cjsidl_listDef383", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_listDef383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_listDef383"):
                opp_val = getattr(value, "cjsidl_listDef383", None)
                setattr(value, "cjsidl_listDef383", self)

    @property
    def cjsidl_constReference454(self):
        return self.__cjsidl_constReference454

    @cjsidl_constReference454.setter
    def cjsidl_constReference454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference454", None)
        self.__cjsidl_constReference454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constDef455"):
                opp_val = getattr(old_value, "cjsidl_constDef455", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constDef455", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constDef455"):
                opp_val = getattr(value, "cjsidl_constDef455", None)
                setattr(value, "cjsidl_constDef455", self)

    @property
    def cjsidl_constReference(self):
        return self.__cjsidl_constReference

    @cjsidl_constReference.setter
    def cjsidl_constReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference", None)
        self.__cjsidl_constReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_fixedLenString292"):
                opp_val = getattr(old_value, "cjsidl_fixedLenString292", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_fixedLenString292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_fixedLenString292"):
                opp_val = getattr(value, "cjsidl_fixedLenString292", None)
                setattr(value, "cjsidl_fixedLenString292", self)

    @property
    def cjsidl_constReference297(self):
        return self.__cjsidl_constReference297

    @cjsidl_constReference297.setter
    def cjsidl_constReference297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference297", None)
        self.__cjsidl_constReference297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varLenString296"):
                opp_val = getattr(old_value, "cjsidl_varLenString296", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_varLenString296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varLenString296"):
                opp_val = getattr(value, "cjsidl_varLenString296", None)
                setattr(value, "cjsidl_varLenString296", self)

    @property
    def cjsidl_constReference363(self):
        return self.__cjsidl_constReference363

    @cjsidl_constReference363.setter
    def cjsidl_constReference363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference363", None)
        self.__cjsidl_constReference363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_valueRange362"):
                opp_val = getattr(old_value, "cjsidl_valueRange362", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_valueRange362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_valueRange362"):
                opp_val = getattr(value, "cjsidl_valueRange362", None)
                setattr(value, "cjsidl_valueRange362", self)

    @property
    def cjsidl_constReference323(self):
        return self.__cjsidl_constReference323

    @cjsidl_constReference323.setter
    def cjsidl_constReference323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference323", None)
        self.__cjsidl_constReference323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varLenField322"):
                opp_val = getattr(old_value, "cjsidl_varLenField322", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_varLenField322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varLenField322"):
                opp_val = getattr(value, "cjsidl_varLenField322", None)
                setattr(value, "cjsidl_varLenField322", self)

    @property
    def cjsidl_constReference329(self):
        return self.__cjsidl_constReference329

    @cjsidl_constReference329.setter
    def cjsidl_constReference329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference329", None)
        self.__cjsidl_constReference329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedUnitsEnum328"):
                opp_val = getattr(old_value, "cjsidl_taggedUnitsEnum328", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedUnitsEnum328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedUnitsEnum328"):
                opp_val = getattr(value, "cjsidl_taggedUnitsEnum328", None)
                setattr(value, "cjsidl_taggedUnitsEnum328", self)

    @property
    def cjsidl_constReference317(self):
        return self.__cjsidl_constReference317

    @cjsidl_constReference317.setter
    def cjsidl_constReference317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference317", None)
        self.__cjsidl_constReference317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varLenField316"):
                opp_val = getattr(old_value, "cjsidl_varLenField316", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_varLenField316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varLenField316"):
                opp_val = getattr(value, "cjsidl_varLenField316", None)
                setattr(value, "cjsidl_varLenField316", self)

    @property
    def cjsidl_constReference303(self):
        return self.__cjsidl_constReference303

    @cjsidl_constReference303.setter
    def cjsidl_constReference303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference303", None)
        self.__cjsidl_constReference303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_varLenString302"):
                opp_val = getattr(old_value, "cjsidl_varLenString302", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_varLenString302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_varLenString302"):
                opp_val = getattr(value, "cjsidl_varLenString302", None)
                setattr(value, "cjsidl_varLenString302", self)

    @property
    def cjsidl_constReference369(self):
        return self.__cjsidl_constReference369

    @cjsidl_constReference369.setter
    def cjsidl_constReference369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference369", None)
        self.__cjsidl_constReference369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scaledRangeDef368"):
                opp_val = getattr(old_value, "cjsidl_scaledRangeDef368", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scaledRangeDef368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scaledRangeDef368"):
                opp_val = getattr(value, "cjsidl_scaledRangeDef368", None)
                setattr(value, "cjsidl_scaledRangeDef368", self)

    @property
    def cjsidl_constReference375(self):
        return self.__cjsidl_constReference375

    @cjsidl_constReference375.setter
    def cjsidl_constReference375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constReference__cjsidl_constReference375", None)
        self.__cjsidl_constReference375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scaledRangeDef374"):
                opp_val = getattr(old_value, "cjsidl_scaledRangeDef374", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scaledRangeDef374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scaledRangeDef374"):
                opp_val = getattr(value, "cjsidl_scaledRangeDef374", None)
                setattr(value, "cjsidl_scaledRangeDef374", self)

class cjsidl_containerDef:

    def __init__(self, comment: str, optional: str, name: str, cjsidl_containerDef: "cjsidl_containerRef" = None, cjsidl_containerDef416: "cjsidl_taggedItemDef" = None, cjsidl_containerDef399: "cjsidl_listDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.cjsidl_containerDef = cjsidl_containerDef
        self.cjsidl_containerDef416 = cjsidl_containerDef416
        self.cjsidl_containerDef399 = cjsidl_containerDef399
        
    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_containerDef416(self):
        return self.__cjsidl_containerDef416

    @cjsidl_containerDef416.setter
    def cjsidl_containerDef416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerDef__cjsidl_containerDef416", None)
        self.__cjsidl_containerDef416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedItemDef415"):
                opp_val = getattr(old_value, "cjsidl_taggedItemDef415", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedItemDef415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedItemDef415"):
                opp_val = getattr(value, "cjsidl_taggedItemDef415", None)
                setattr(value, "cjsidl_taggedItemDef415", self)

    @property
    def cjsidl_containerDef399(self):
        return self.__cjsidl_containerDef399

    @cjsidl_containerDef399.setter
    def cjsidl_containerDef399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerDef__cjsidl_containerDef399", None)
        self.__cjsidl_containerDef399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_listDef398"):
                opp_val = getattr(old_value, "cjsidl_listDef398", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_listDef398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_listDef398"):
                opp_val = getattr(value, "cjsidl_listDef398", None)
                setattr(value, "cjsidl_listDef398", self)

    @property
    def cjsidl_containerDef(self):
        return self.__cjsidl_containerDef

    @cjsidl_containerDef.setter
    def cjsidl_containerDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerDef__cjsidl_containerDef", None)
        self.__cjsidl_containerDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_containerRef"):
                opp_val = getattr(old_value, "cjsidl_containerRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_containerRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_containerRef"):
                opp_val = getattr(value, "cjsidl_containerRef", None)
                setattr(value, "cjsidl_containerRef", self)

class cjsidl_footerScopedRef:

    pass
class cjsidl_footerRef:

    def __init__(self, comment: str, name: str, cjsidl_footerRef: "cjsidl_footerDef" = None, cjsidl_footerRef255: "cjsidl_footerScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_footerRef = cjsidl_footerRef
        self.cjsidl_footerRef255 = cjsidl_footerRef255
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_footerRef255(self):
        return self.__cjsidl_footerRef255

    @cjsidl_footerRef255.setter
    def cjsidl_footerRef255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerRef__cjsidl_footerRef255", None)
        self.__cjsidl_footerRef255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_footerScopedRef"):
                opp_val = getattr(old_value, "cjsidl_footerScopedRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_footerScopedRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_footerScopedRef"):
                opp_val = getattr(value, "cjsidl_footerScopedRef", None)
                setattr(value, "cjsidl_footerScopedRef", self)

    @property
    def cjsidl_footerRef(self):
        return self.__cjsidl_footerRef

    @cjsidl_footerRef.setter
    def cjsidl_footerRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerRef__cjsidl_footerRef", None)
        self.__cjsidl_footerRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_footerDef253"):
                opp_val = getattr(old_value, "cjsidl_footerDef253", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_footerDef253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_footerDef253"):
                opp_val = getattr(value, "cjsidl_footerDef253", None)
                setattr(value, "cjsidl_footerDef253", self)

class cjsidl_declaredEventDef:

    def __init__(self, comment: str, name: str, cjsidl_declaredEventDef: "cjsidl_eventDef" = None, cjsidl_declaredEventDef289: "cjsidl_scopedEventType" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_declaredEventDef = cjsidl_declaredEventDef
        self.cjsidl_declaredEventDef289 = cjsidl_declaredEventDef289
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_declaredEventDef289(self):
        return self.__cjsidl_declaredEventDef289

    @cjsidl_declaredEventDef289.setter
    def cjsidl_declaredEventDef289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredEventDef__cjsidl_declaredEventDef289", None)
        self.__cjsidl_declaredEventDef289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedEventType290"):
                opp_val = getattr(old_value, "cjsidl_scopedEventType290", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedEventType290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedEventType290"):
                opp_val = getattr(value, "cjsidl_scopedEventType290", None)
                setattr(value, "cjsidl_scopedEventType290", self)

    @property
    def cjsidl_declaredEventDef(self):
        return self.__cjsidl_declaredEventDef

    @cjsidl_declaredEventDef.setter
    def cjsidl_declaredEventDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredEventDef__cjsidl_declaredEventDef", None)
        self.__cjsidl_declaredEventDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_eventDef287"):
                opp_val = getattr(old_value, "cjsidl_eventDef287", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_eventDef287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_eventDef287"):
                opp_val = getattr(value, "cjsidl_eventDef287", None)
                setattr(value, "cjsidl_eventDef287", self)

class cjsidl_scopedType:

    pass
class cjsidl_containerRef:

    def __init__(self, comment: str, optional: str, name: str, cjsidl_containerRef: "cjsidl_containerDef" = None, cjsidl_containerRef285: "cjsidl_scopedType" = None, cjsidl_containerRef419: "cjsidl_taggedItemDef" = None, cjsidl_containerRef396: "cjsidl_listDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.cjsidl_containerRef = cjsidl_containerRef
        self.cjsidl_containerRef285 = cjsidl_containerRef285
        self.cjsidl_containerRef419 = cjsidl_containerRef419
        self.cjsidl_containerRef396 = cjsidl_containerRef396
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def cjsidl_containerRef285(self):
        return self.__cjsidl_containerRef285

    @cjsidl_containerRef285.setter
    def cjsidl_containerRef285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerRef__cjsidl_containerRef285", None)
        self.__cjsidl_containerRef285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedType"):
                opp_val = getattr(old_value, "cjsidl_scopedType", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedType"):
                opp_val = getattr(value, "cjsidl_scopedType", None)
                setattr(value, "cjsidl_scopedType", self)

    @property
    def cjsidl_containerRef419(self):
        return self.__cjsidl_containerRef419

    @cjsidl_containerRef419.setter
    def cjsidl_containerRef419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerRef__cjsidl_containerRef419", None)
        self.__cjsidl_containerRef419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedItemDef418"):
                opp_val = getattr(old_value, "cjsidl_taggedItemDef418", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedItemDef418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedItemDef418"):
                opp_val = getattr(value, "cjsidl_taggedItemDef418", None)
                setattr(value, "cjsidl_taggedItemDef418", self)

    @property
    def cjsidl_containerRef(self):
        return self.__cjsidl_containerRef

    @cjsidl_containerRef.setter
    def cjsidl_containerRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerRef__cjsidl_containerRef", None)
        self.__cjsidl_containerRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_containerDef"):
                opp_val = getattr(old_value, "cjsidl_containerDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_containerDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_containerDef"):
                opp_val = getattr(value, "cjsidl_containerDef", None)
                setattr(value, "cjsidl_containerDef", self)

    @property
    def cjsidl_containerRef396(self):
        return self.__cjsidl_containerRef396

    @cjsidl_containerRef396.setter
    def cjsidl_containerRef396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_containerRef__cjsidl_containerRef396", None)
        self.__cjsidl_containerRef396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_listDef395"):
                opp_val = getattr(old_value, "cjsidl_listDef395", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_listDef395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_listDef395"):
                opp_val = getattr(value, "cjsidl_listDef395", None)
                setattr(value, "cjsidl_listDef395", self)

class cjsidl_footerDef:

    def __init__(self, comment: str, name: str, cjsidl_footerDef: "cjsidl_typeDef" = None, cjsidl_footerDef242: "cjsidl_EObject" = None, cjsidl_footerDef253: "cjsidl_footerRef" = None, cjsidl_footerDef282: "cjsidl_footerScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_footerDef = cjsidl_footerDef
        self.cjsidl_footerDef242 = cjsidl_footerDef242
        self.cjsidl_footerDef253 = cjsidl_footerDef253
        self.cjsidl_footerDef282 = cjsidl_footerDef282
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_footerDef282(self):
        return self.__cjsidl_footerDef282

    @cjsidl_footerDef282.setter
    def cjsidl_footerDef282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerDef__cjsidl_footerDef282", None)
        self.__cjsidl_footerDef282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_footerScopedRef281"):
                opp_val = getattr(old_value, "cjsidl_footerScopedRef281", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_footerScopedRef281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_footerScopedRef281"):
                opp_val = getattr(value, "cjsidl_footerScopedRef281", None)
                setattr(value, "cjsidl_footerScopedRef281", self)

    @property
    def cjsidl_footerDef253(self):
        return self.__cjsidl_footerDef253

    @cjsidl_footerDef253.setter
    def cjsidl_footerDef253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerDef__cjsidl_footerDef253", None)
        self.__cjsidl_footerDef253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_footerRef"):
                opp_val = getattr(old_value, "cjsidl_footerRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_footerRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_footerRef"):
                opp_val = getattr(value, "cjsidl_footerRef", None)
                setattr(value, "cjsidl_footerRef", self)

    @property
    def cjsidl_footerDef(self):
        return self.__cjsidl_footerDef

    @cjsidl_footerDef.setter
    def cjsidl_footerDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerDef__cjsidl_footerDef", None)
        self.__cjsidl_footerDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef222"):
                opp_val = getattr(old_value, "cjsidl_typeDef222", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef222"):
                opp_val = getattr(value, "cjsidl_typeDef222", None)
                setattr(value, "cjsidl_typeDef222", self)

    @property
    def cjsidl_footerDef242(self):
        return self.__cjsidl_footerDef242

    @cjsidl_footerDef242.setter
    def cjsidl_footerDef242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_footerDef__cjsidl_footerDef242", None)
        self.__cjsidl_footerDef242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject243"):
                opp_val = getattr(old_value, "cjsidl_EObject243", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject243"):
                opp_val = getattr(value, "cjsidl_EObject243", None)
                setattr(value, "cjsidl_EObject243", self)

class cjsidl_bodyDef:

    def __init__(self, comment: str, name: str, cjsidl_bodyDef249: "cjsidl_bodyRef" = None, cjsidl_bodyDef: "cjsidl_typeDef" = None, cjsidl_bodyDef239: "cjsidl_EObject" = None, cjsidl_bodyDef273: "cjsidl_bodyScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_bodyDef249 = cjsidl_bodyDef249
        self.cjsidl_bodyDef = cjsidl_bodyDef
        self.cjsidl_bodyDef239 = cjsidl_bodyDef239
        self.cjsidl_bodyDef273 = cjsidl_bodyDef273
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_bodyDef(self):
        return self.__cjsidl_bodyDef

    @cjsidl_bodyDef.setter
    def cjsidl_bodyDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyDef__cjsidl_bodyDef", None)
        self.__cjsidl_bodyDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef220"):
                opp_val = getattr(old_value, "cjsidl_typeDef220", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef220"):
                opp_val = getattr(value, "cjsidl_typeDef220", None)
                setattr(value, "cjsidl_typeDef220", self)

    @property
    def cjsidl_bodyDef273(self):
        return self.__cjsidl_bodyDef273

    @cjsidl_bodyDef273.setter
    def cjsidl_bodyDef273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyDef__cjsidl_bodyDef273", None)
        self.__cjsidl_bodyDef273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_bodyScopedRef272"):
                opp_val = getattr(old_value, "cjsidl_bodyScopedRef272", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_bodyScopedRef272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_bodyScopedRef272"):
                opp_val = getattr(value, "cjsidl_bodyScopedRef272", None)
                setattr(value, "cjsidl_bodyScopedRef272", self)

    @property
    def cjsidl_bodyDef249(self):
        return self.__cjsidl_bodyDef249

    @cjsidl_bodyDef249.setter
    def cjsidl_bodyDef249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyDef__cjsidl_bodyDef249", None)
        self.__cjsidl_bodyDef249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_bodyRef"):
                opp_val = getattr(old_value, "cjsidl_bodyRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_bodyRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_bodyRef"):
                opp_val = getattr(value, "cjsidl_bodyRef", None)
                setattr(value, "cjsidl_bodyRef", self)

    @property
    def cjsidl_bodyDef239(self):
        return self.__cjsidl_bodyDef239

    @cjsidl_bodyDef239.setter
    def cjsidl_bodyDef239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyDef__cjsidl_bodyDef239", None)
        self.__cjsidl_bodyDef239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject240"):
                opp_val = getattr(old_value, "cjsidl_EObject240", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject240"):
                opp_val = getattr(value, "cjsidl_EObject240", None)
                setattr(value, "cjsidl_EObject240", self)

class cjsidl_bodyScopedRef:

    pass
class cjsidl_bodyRef:

    def __init__(self, comment: str, name: str, cjsidl_bodyRef: "cjsidl_bodyDef" = None, cjsidl_bodyRef251: "cjsidl_bodyScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_bodyRef = cjsidl_bodyRef
        self.cjsidl_bodyRef251 = cjsidl_bodyRef251
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_bodyRef251(self):
        return self.__cjsidl_bodyRef251

    @cjsidl_bodyRef251.setter
    def cjsidl_bodyRef251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyRef__cjsidl_bodyRef251", None)
        self.__cjsidl_bodyRef251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_bodyScopedRef"):
                opp_val = getattr(old_value, "cjsidl_bodyScopedRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_bodyScopedRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_bodyScopedRef"):
                opp_val = getattr(value, "cjsidl_bodyScopedRef", None)
                setattr(value, "cjsidl_bodyScopedRef", self)

    @property
    def cjsidl_bodyRef(self):
        return self.__cjsidl_bodyRef

    @cjsidl_bodyRef.setter
    def cjsidl_bodyRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bodyRef__cjsidl_bodyRef", None)
        self.__cjsidl_bodyRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_bodyDef249"):
                opp_val = getattr(old_value, "cjsidl_bodyDef249", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_bodyDef249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_bodyDef249"):
                opp_val = getattr(value, "cjsidl_bodyDef249", None)
                setattr(value, "cjsidl_bodyDef249", self)

class cjsidl_headerScopedRef:

    pass
class cjsidl_headerRef:

    def __init__(self, comment: str, name: str, cjsidl_headerRef: "cjsidl_headerDef" = None, cjsidl_headerRef247: "cjsidl_headerScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_headerRef = cjsidl_headerRef
        self.cjsidl_headerRef247 = cjsidl_headerRef247
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_headerRef(self):
        return self.__cjsidl_headerRef

    @cjsidl_headerRef.setter
    def cjsidl_headerRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerRef__cjsidl_headerRef", None)
        self.__cjsidl_headerRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_headerDef245"):
                opp_val = getattr(old_value, "cjsidl_headerDef245", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_headerDef245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_headerDef245"):
                opp_val = getattr(value, "cjsidl_headerDef245", None)
                setattr(value, "cjsidl_headerDef245", self)

    @property
    def cjsidl_headerRef247(self):
        return self.__cjsidl_headerRef247

    @cjsidl_headerRef247.setter
    def cjsidl_headerRef247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerRef__cjsidl_headerRef247", None)
        self.__cjsidl_headerRef247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_headerScopedRef"):
                opp_val = getattr(old_value, "cjsidl_headerScopedRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_headerScopedRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_headerScopedRef"):
                opp_val = getattr(value, "cjsidl_headerScopedRef", None)
                setattr(value, "cjsidl_headerScopedRef", self)

class cjsidl_bitfieldDef:

    def __init__(self, comment: str, optional: str, type: str, name: str, cjsidl_bitfieldDef: "cjsidl_typeDef" = None, cjsidl_bitfieldDef354: set["cjsidl_subField"] = None, cjsidl_bitfieldDef434: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.type = type
        self.name = name
        self.cjsidl_bitfieldDef = cjsidl_bitfieldDef
        self.cjsidl_bitfieldDef354 = cjsidl_bitfieldDef354 if cjsidl_bitfieldDef354 is not None else set()
        self.cjsidl_bitfieldDef434 = cjsidl_bitfieldDef434
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def cjsidl_bitfieldDef354(self):
        return self.__cjsidl_bitfieldDef354

    @cjsidl_bitfieldDef354.setter
    def cjsidl_bitfieldDef354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bitfieldDef__cjsidl_bitfieldDef354", None)
        self.__cjsidl_bitfieldDef354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_subField"):
                    opp_val = getattr(item, "cjsidl_subField", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_subField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_subField"):
                    opp_val = getattr(item, "cjsidl_subField", None)
                    
                    setattr(item, "cjsidl_subField", self)
                    

    @property
    def cjsidl_bitfieldDef(self):
        return self.__cjsidl_bitfieldDef

    @cjsidl_bitfieldDef.setter
    def cjsidl_bitfieldDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bitfieldDef__cjsidl_bitfieldDef", None)
        self.__cjsidl_bitfieldDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef208"):
                opp_val = getattr(old_value, "cjsidl_typeDef208", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef208"):
                opp_val = getattr(value, "cjsidl_typeDef208", None)
                setattr(value, "cjsidl_typeDef208", self)

    @property
    def cjsidl_bitfieldDef434(self):
        return self.__cjsidl_bitfieldDef434

    @cjsidl_bitfieldDef434.setter
    def cjsidl_bitfieldDef434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_bitfieldDef__cjsidl_bitfieldDef434", None)
        self.__cjsidl_bitfieldDef434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef433"):
                opp_val = getattr(old_value, "cjsidl_recordDef433", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef433"):
                opp_val = getattr(value, "cjsidl_recordDef433", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef433", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_varField:

    def __init__(self, comment: str, optional: str, name: str, cjsidl_varField: "cjsidl_typeDef" = None, cjsidl_varField314: set["cjsidl_taggedUnitsEnum"] = None, cjsidl_varField431: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.cjsidl_varField = cjsidl_varField
        self.cjsidl_varField314 = cjsidl_varField314 if cjsidl_varField314 is not None else set()
        self.cjsidl_varField431 = cjsidl_varField431
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_varField314(self):
        return self.__cjsidl_varField314

    @cjsidl_varField314.setter
    def cjsidl_varField314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varField__cjsidl_varField314", None)
        self.__cjsidl_varField314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_taggedUnitsEnum"):
                    opp_val = getattr(item, "cjsidl_taggedUnitsEnum", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_taggedUnitsEnum", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_taggedUnitsEnum"):
                    opp_val = getattr(item, "cjsidl_taggedUnitsEnum", None)
                    
                    setattr(item, "cjsidl_taggedUnitsEnum", self)
                    

    @property
    def cjsidl_varField431(self):
        return self.__cjsidl_varField431

    @cjsidl_varField431.setter
    def cjsidl_varField431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varField__cjsidl_varField431", None)
        self.__cjsidl_varField431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef430"):
                opp_val = getattr(old_value, "cjsidl_recordDef430", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef430"):
                opp_val = getattr(value, "cjsidl_recordDef430", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef430", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_varField(self):
        return self.__cjsidl_varField

    @cjsidl_varField.setter
    def cjsidl_varField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varField__cjsidl_varField", None)
        self.__cjsidl_varField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef206"):
                opp_val = getattr(old_value, "cjsidl_typeDef206", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef206"):
                opp_val = getattr(value, "cjsidl_typeDef206", None)
                setattr(value, "cjsidl_typeDef206", self)

class cjsidl_fixedFieldDef:

    def __init__(self, comment: str, optional: str, name: str, fieldUnit: str, cjsidl_fixedFieldDef: "cjsidl_typeDef" = None, cjsidl_fixedFieldDef308: "cjsidl_simpleNumericType" = None, cjsidl_fixedFieldDef311: "cjsidl_EObject" = None, cjsidl_fixedFieldDef428: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.fieldUnit = fieldUnit
        self.cjsidl_fixedFieldDef = cjsidl_fixedFieldDef
        self.cjsidl_fixedFieldDef308 = cjsidl_fixedFieldDef308
        self.cjsidl_fixedFieldDef311 = cjsidl_fixedFieldDef311
        self.cjsidl_fixedFieldDef428 = cjsidl_fixedFieldDef428
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def fieldUnit(self) -> str:
        return self.__fieldUnit

    @fieldUnit.setter
    def fieldUnit(self, fieldUnit: str):
        self.__fieldUnit = fieldUnit

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def cjsidl_fixedFieldDef311(self):
        return self.__cjsidl_fixedFieldDef311

    @cjsidl_fixedFieldDef311.setter
    def cjsidl_fixedFieldDef311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedFieldDef__cjsidl_fixedFieldDef311", None)
        self.__cjsidl_fixedFieldDef311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject312"):
                opp_val = getattr(old_value, "cjsidl_EObject312", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject312"):
                opp_val = getattr(value, "cjsidl_EObject312", None)
                setattr(value, "cjsidl_EObject312", self)

    @property
    def cjsidl_fixedFieldDef308(self):
        return self.__cjsidl_fixedFieldDef308

    @cjsidl_fixedFieldDef308.setter
    def cjsidl_fixedFieldDef308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedFieldDef__cjsidl_fixedFieldDef308", None)
        self.__cjsidl_fixedFieldDef308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_simpleNumericType309"):
                opp_val = getattr(old_value, "cjsidl_simpleNumericType309", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_simpleNumericType309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_simpleNumericType309"):
                opp_val = getattr(value, "cjsidl_simpleNumericType309", None)
                setattr(value, "cjsidl_simpleNumericType309", self)

    @property
    def cjsidl_fixedFieldDef(self):
        return self.__cjsidl_fixedFieldDef

    @cjsidl_fixedFieldDef.setter
    def cjsidl_fixedFieldDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedFieldDef__cjsidl_fixedFieldDef", None)
        self.__cjsidl_fixedFieldDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef204"):
                opp_val = getattr(old_value, "cjsidl_typeDef204", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef204"):
                opp_val = getattr(value, "cjsidl_typeDef204", None)
                setattr(value, "cjsidl_typeDef204", self)

    @property
    def cjsidl_fixedFieldDef428(self):
        return self.__cjsidl_fixedFieldDef428

    @cjsidl_fixedFieldDef428.setter
    def cjsidl_fixedFieldDef428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedFieldDef__cjsidl_fixedFieldDef428", None)
        self.__cjsidl_fixedFieldDef428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef427"):
                opp_val = getattr(old_value, "cjsidl_recordDef427", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef427"):
                opp_val = getattr(value, "cjsidl_recordDef427", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef427", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_sequenceDef(containerDef):

    pass
class cjsidl_variantDef(containerDef):

    def __init__(self, vtagComment: str, minCount: str, maxCount: str, cjsidl_variantDef: "cjsidl_typeDef" = None, cjsidl_variantDef401: "cjsidl_constReference" = None, cjsidl_variantDef404: "cjsidl_scopedConstId" = None, cjsidl_variantDef407: "cjsidl_constReference" = None, cjsidl_variantDef410: "cjsidl_scopedConstId" = None, cjsidl_variantDef413: set["cjsidl_taggedItemDef"] = None):
        self.vtagComment = vtagComment
        self.minCount = minCount
        self.maxCount = maxCount
        self.cjsidl_variantDef = cjsidl_variantDef
        self.cjsidl_variantDef401 = cjsidl_variantDef401
        self.cjsidl_variantDef404 = cjsidl_variantDef404
        self.cjsidl_variantDef407 = cjsidl_variantDef407
        self.cjsidl_variantDef410 = cjsidl_variantDef410
        self.cjsidl_variantDef413 = cjsidl_variantDef413 if cjsidl_variantDef413 is not None else set()
        
    @property
    def vtagComment(self) -> str:
        return self.__vtagComment

    @vtagComment.setter
    def vtagComment(self, vtagComment: str):
        self.__vtagComment = vtagComment

    @property
    def maxCount(self) -> str:
        return self.__maxCount

    @maxCount.setter
    def maxCount(self, maxCount: str):
        self.__maxCount = maxCount

    @property
    def minCount(self) -> str:
        return self.__minCount

    @minCount.setter
    def minCount(self, minCount: str):
        self.__minCount = minCount

    @property
    def cjsidl_variantDef401(self):
        return self.__cjsidl_variantDef401

    @cjsidl_variantDef401.setter
    def cjsidl_variantDef401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef401", None)
        self.__cjsidl_variantDef401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference402"):
                opp_val = getattr(old_value, "cjsidl_constReference402", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference402"):
                opp_val = getattr(value, "cjsidl_constReference402", None)
                setattr(value, "cjsidl_constReference402", self)

    @property
    def cjsidl_variantDef404(self):
        return self.__cjsidl_variantDef404

    @cjsidl_variantDef404.setter
    def cjsidl_variantDef404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef404", None)
        self.__cjsidl_variantDef404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId405"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId405", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId405"):
                opp_val = getattr(value, "cjsidl_scopedConstId405", None)
                setattr(value, "cjsidl_scopedConstId405", self)

    @property
    def cjsidl_variantDef407(self):
        return self.__cjsidl_variantDef407

    @cjsidl_variantDef407.setter
    def cjsidl_variantDef407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef407", None)
        self.__cjsidl_variantDef407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference408"):
                opp_val = getattr(old_value, "cjsidl_constReference408", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference408"):
                opp_val = getattr(value, "cjsidl_constReference408", None)
                setattr(value, "cjsidl_constReference408", self)

    @property
    def cjsidl_variantDef413(self):
        return self.__cjsidl_variantDef413

    @cjsidl_variantDef413.setter
    def cjsidl_variantDef413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef413", None)
        self.__cjsidl_variantDef413 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_taggedItemDef"):
                    opp_val = getattr(item, "cjsidl_taggedItemDef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_taggedItemDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_taggedItemDef"):
                    opp_val = getattr(item, "cjsidl_taggedItemDef", None)
                    
                    setattr(item, "cjsidl_taggedItemDef", self)
                    

    @property
    def cjsidl_variantDef(self):
        return self.__cjsidl_variantDef

    @cjsidl_variantDef.setter
    def cjsidl_variantDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef", None)
        self.__cjsidl_variantDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef200"):
                opp_val = getattr(old_value, "cjsidl_typeDef200", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef200"):
                opp_val = getattr(value, "cjsidl_typeDef200", None)
                setattr(value, "cjsidl_typeDef200", self)

    @property
    def cjsidl_variantDef410(self):
        return self.__cjsidl_variantDef410

    @cjsidl_variantDef410.setter
    def cjsidl_variantDef410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_variantDef__cjsidl_variantDef410", None)
        self.__cjsidl_variantDef410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId411"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId411", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId411"):
                opp_val = getattr(value, "cjsidl_scopedConstId411", None)
                setattr(value, "cjsidl_scopedConstId411", self)

class cjsidl_listDef(containerDef):

    def __init__(self, countComment: str, minCount: str, maxCount: str, cjsidl_listDef: "cjsidl_typeDef" = None, cjsidl_listDef383: "cjsidl_constReference" = None, cjsidl_listDef386: "cjsidl_scopedConstId" = None, cjsidl_listDef389: "cjsidl_constReference" = None, cjsidl_listDef392: "cjsidl_scopedConstId" = None, cjsidl_listDef395: "cjsidl_containerRef" = None, cjsidl_listDef398: "cjsidl_containerDef" = None):
        self.countComment = countComment
        self.minCount = minCount
        self.maxCount = maxCount
        self.cjsidl_listDef = cjsidl_listDef
        self.cjsidl_listDef383 = cjsidl_listDef383
        self.cjsidl_listDef386 = cjsidl_listDef386
        self.cjsidl_listDef389 = cjsidl_listDef389
        self.cjsidl_listDef392 = cjsidl_listDef392
        self.cjsidl_listDef395 = cjsidl_listDef395
        self.cjsidl_listDef398 = cjsidl_listDef398
        
    @property
    def minCount(self) -> str:
        return self.__minCount

    @minCount.setter
    def minCount(self, minCount: str):
        self.__minCount = minCount

    @property
    def maxCount(self) -> str:
        return self.__maxCount

    @maxCount.setter
    def maxCount(self, maxCount: str):
        self.__maxCount = maxCount

    @property
    def countComment(self) -> str:
        return self.__countComment

    @countComment.setter
    def countComment(self, countComment: str):
        self.__countComment = countComment

    @property
    def cjsidl_listDef(self):
        return self.__cjsidl_listDef

    @cjsidl_listDef.setter
    def cjsidl_listDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef", None)
        self.__cjsidl_listDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef198"):
                opp_val = getattr(old_value, "cjsidl_typeDef198", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef198"):
                opp_val = getattr(value, "cjsidl_typeDef198", None)
                setattr(value, "cjsidl_typeDef198", self)

    @property
    def cjsidl_listDef395(self):
        return self.__cjsidl_listDef395

    @cjsidl_listDef395.setter
    def cjsidl_listDef395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef395", None)
        self.__cjsidl_listDef395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_containerRef396"):
                opp_val = getattr(old_value, "cjsidl_containerRef396", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_containerRef396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_containerRef396"):
                opp_val = getattr(value, "cjsidl_containerRef396", None)
                setattr(value, "cjsidl_containerRef396", self)

    @property
    def cjsidl_listDef383(self):
        return self.__cjsidl_listDef383

    @cjsidl_listDef383.setter
    def cjsidl_listDef383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef383", None)
        self.__cjsidl_listDef383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference384"):
                opp_val = getattr(old_value, "cjsidl_constReference384", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference384"):
                opp_val = getattr(value, "cjsidl_constReference384", None)
                setattr(value, "cjsidl_constReference384", self)

    @property
    def cjsidl_listDef398(self):
        return self.__cjsidl_listDef398

    @cjsidl_listDef398.setter
    def cjsidl_listDef398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef398", None)
        self.__cjsidl_listDef398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_containerDef399"):
                opp_val = getattr(old_value, "cjsidl_containerDef399", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_containerDef399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_containerDef399"):
                opp_val = getattr(value, "cjsidl_containerDef399", None)
                setattr(value, "cjsidl_containerDef399", self)

    @property
    def cjsidl_listDef386(self):
        return self.__cjsidl_listDef386

    @cjsidl_listDef386.setter
    def cjsidl_listDef386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef386", None)
        self.__cjsidl_listDef386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId387"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId387", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId387"):
                opp_val = getattr(value, "cjsidl_scopedConstId387", None)
                setattr(value, "cjsidl_scopedConstId387", self)

    @property
    def cjsidl_listDef389(self):
        return self.__cjsidl_listDef389

    @cjsidl_listDef389.setter
    def cjsidl_listDef389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef389", None)
        self.__cjsidl_listDef389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference390"):
                opp_val = getattr(old_value, "cjsidl_constReference390", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference390", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference390"):
                opp_val = getattr(value, "cjsidl_constReference390", None)
                setattr(value, "cjsidl_constReference390", self)

    @property
    def cjsidl_listDef392(self):
        return self.__cjsidl_listDef392

    @cjsidl_listDef392.setter
    def cjsidl_listDef392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_listDef__cjsidl_listDef392", None)
        self.__cjsidl_listDef392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId393"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId393", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId393"):
                opp_val = getattr(value, "cjsidl_scopedConstId393", None)
                setattr(value, "cjsidl_scopedConstId393", self)

class cjsidl_recordDef(containerDef):

    pass
class cjsidl_arrayDef:

    def __init__(self, comment: str, optional: str, name: str, arraySize: str, cjsidl_arrayDef: "cjsidl_typeDef" = None, cjsidl_arrayDef425: "cjsidl_recordDef" = None, cjsidl_arrayDef460: "cjsidl_EObject" = None, cjsidl_arrayDef463: "cjsidl_scopedType" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.arraySize = arraySize
        self.cjsidl_arrayDef = cjsidl_arrayDef
        self.cjsidl_arrayDef425 = cjsidl_arrayDef425
        self.cjsidl_arrayDef460 = cjsidl_arrayDef460
        self.cjsidl_arrayDef463 = cjsidl_arrayDef463
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def arraySize(self) -> str:
        return self.__arraySize

    @arraySize.setter
    def arraySize(self, arraySize: str):
        self.__arraySize = arraySize

    @property
    def cjsidl_arrayDef460(self):
        return self.__cjsidl_arrayDef460

    @cjsidl_arrayDef460.setter
    def cjsidl_arrayDef460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_arrayDef__cjsidl_arrayDef460", None)
        self.__cjsidl_arrayDef460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject461"):
                opp_val = getattr(old_value, "cjsidl_EObject461", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject461"):
                opp_val = getattr(value, "cjsidl_EObject461", None)
                setattr(value, "cjsidl_EObject461", self)

    @property
    def cjsidl_arrayDef463(self):
        return self.__cjsidl_arrayDef463

    @cjsidl_arrayDef463.setter
    def cjsidl_arrayDef463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_arrayDef__cjsidl_arrayDef463", None)
        self.__cjsidl_arrayDef463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedType464"):
                opp_val = getattr(old_value, "cjsidl_scopedType464", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedType464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedType464"):
                opp_val = getattr(value, "cjsidl_scopedType464", None)
                setattr(value, "cjsidl_scopedType464", self)

    @property
    def cjsidl_arrayDef(self):
        return self.__cjsidl_arrayDef

    @cjsidl_arrayDef.setter
    def cjsidl_arrayDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_arrayDef__cjsidl_arrayDef", None)
        self.__cjsidl_arrayDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef194"):
                opp_val = getattr(old_value, "cjsidl_typeDef194", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef194"):
                opp_val = getattr(value, "cjsidl_typeDef194", None)
                setattr(value, "cjsidl_typeDef194", self)

    @property
    def cjsidl_arrayDef425(self):
        return self.__cjsidl_arrayDef425

    @cjsidl_arrayDef425.setter
    def cjsidl_arrayDef425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_arrayDef__cjsidl_arrayDef425", None)
        self.__cjsidl_arrayDef425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef424"):
                opp_val = getattr(old_value, "cjsidl_recordDef424", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef424"):
                opp_val = getattr(value, "cjsidl_recordDef424", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef424", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_simpleNumericType:

    def __init__(self, type: str, cjsidl_simpleNumericType: "cjsidl_constDef" = None, cjsidl_simpleNumericType309: "cjsidl_fixedFieldDef" = None, cjsidl_simpleNumericType335: "cjsidl_taggedUnitsEnum" = None):
        self.type = type
        self.cjsidl_simpleNumericType = cjsidl_simpleNumericType
        self.cjsidl_simpleNumericType309 = cjsidl_simpleNumericType309
        self.cjsidl_simpleNumericType335 = cjsidl_simpleNumericType335
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cjsidl_simpleNumericType(self):
        return self.__cjsidl_simpleNumericType

    @cjsidl_simpleNumericType.setter
    def cjsidl_simpleNumericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_simpleNumericType__cjsidl_simpleNumericType", None)
        self.__cjsidl_simpleNumericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constDef186"):
                opp_val = getattr(old_value, "cjsidl_constDef186", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constDef186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constDef186"):
                opp_val = getattr(value, "cjsidl_constDef186", None)
                setattr(value, "cjsidl_constDef186", self)

    @property
    def cjsidl_simpleNumericType335(self):
        return self.__cjsidl_simpleNumericType335

    @cjsidl_simpleNumericType335.setter
    def cjsidl_simpleNumericType335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_simpleNumericType__cjsidl_simpleNumericType335", None)
        self.__cjsidl_simpleNumericType335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_taggedUnitsEnum334"):
                opp_val = getattr(old_value, "cjsidl_taggedUnitsEnum334", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_taggedUnitsEnum334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_taggedUnitsEnum334"):
                opp_val = getattr(value, "cjsidl_taggedUnitsEnum334", None)
                setattr(value, "cjsidl_taggedUnitsEnum334", self)

    @property
    def cjsidl_simpleNumericType309(self):
        return self.__cjsidl_simpleNumericType309

    @cjsidl_simpleNumericType309.setter
    def cjsidl_simpleNumericType309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_simpleNumericType__cjsidl_simpleNumericType309", None)
        self.__cjsidl_simpleNumericType309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_fixedFieldDef308"):
                opp_val = getattr(old_value, "cjsidl_fixedFieldDef308", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_fixedFieldDef308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_fixedFieldDef308"):
                opp_val = getattr(value, "cjsidl_fixedFieldDef308", None)
                setattr(value, "cjsidl_fixedFieldDef308", self)

class cjsidl_headerDef:

    def __init__(self, comment: str, name: str, cjsidl_headerDef: "cjsidl_typeDef" = None, cjsidl_headerDef245: "cjsidl_headerRef" = None, cjsidl_headerDef236: "cjsidl_EObject" = None, cjsidl_headerDef264: "cjsidl_headerScopedRef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_headerDef = cjsidl_headerDef
        self.cjsidl_headerDef245 = cjsidl_headerDef245
        self.cjsidl_headerDef236 = cjsidl_headerDef236
        self.cjsidl_headerDef264 = cjsidl_headerDef264
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_headerDef245(self):
        return self.__cjsidl_headerDef245

    @cjsidl_headerDef245.setter
    def cjsidl_headerDef245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerDef__cjsidl_headerDef245", None)
        self.__cjsidl_headerDef245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_headerRef"):
                opp_val = getattr(old_value, "cjsidl_headerRef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_headerRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_headerRef"):
                opp_val = getattr(value, "cjsidl_headerRef", None)
                setattr(value, "cjsidl_headerRef", self)

    @property
    def cjsidl_headerDef(self):
        return self.__cjsidl_headerDef

    @cjsidl_headerDef.setter
    def cjsidl_headerDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerDef__cjsidl_headerDef", None)
        self.__cjsidl_headerDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef218"):
                opp_val = getattr(old_value, "cjsidl_typeDef218", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef218"):
                opp_val = getattr(value, "cjsidl_typeDef218", None)
                setattr(value, "cjsidl_typeDef218", self)

    @property
    def cjsidl_headerDef264(self):
        return self.__cjsidl_headerDef264

    @cjsidl_headerDef264.setter
    def cjsidl_headerDef264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerDef__cjsidl_headerDef264", None)
        self.__cjsidl_headerDef264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_headerScopedRef263"):
                opp_val = getattr(old_value, "cjsidl_headerScopedRef263", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_headerScopedRef263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_headerScopedRef263"):
                opp_val = getattr(value, "cjsidl_headerScopedRef263", None)
                setattr(value, "cjsidl_headerScopedRef263", self)

    @property
    def cjsidl_headerDef236(self):
        return self.__cjsidl_headerDef236

    @cjsidl_headerDef236.setter
    def cjsidl_headerDef236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_headerDef__cjsidl_headerDef236", None)
        self.__cjsidl_headerDef236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject237"):
                opp_val = getattr(old_value, "cjsidl_EObject237", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject237"):
                opp_val = getattr(value, "cjsidl_EObject237", None)
                setattr(value, "cjsidl_EObject237", self)

class cjsidl_varFormatField:

    def __init__(self, comment: str, optional: str, name: str, countComment: str, units: str, cjsidl_varFormatField: "cjsidl_typeDef" = None, cjsidl_varFormatField341: "cjsidl_valueRange" = None, cjsidl_varFormatField343: set["cjsidl_formatEnumDef"] = None, cjsidl_varFormatField446: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.countComment = countComment
        self.units = units
        self.cjsidl_varFormatField = cjsidl_varFormatField
        self.cjsidl_varFormatField341 = cjsidl_varFormatField341
        self.cjsidl_varFormatField343 = cjsidl_varFormatField343 if cjsidl_varFormatField343 is not None else set()
        self.cjsidl_varFormatField446 = cjsidl_varFormatField446
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def countComment(self) -> str:
        return self.__countComment

    @countComment.setter
    def countComment(self, countComment: str):
        self.__countComment = countComment

    @property
    def cjsidl_varFormatField446(self):
        return self.__cjsidl_varFormatField446

    @cjsidl_varFormatField446.setter
    def cjsidl_varFormatField446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varFormatField__cjsidl_varFormatField446", None)
        self.__cjsidl_varFormatField446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef445"):
                opp_val = getattr(old_value, "cjsidl_recordDef445", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef445"):
                opp_val = getattr(value, "cjsidl_recordDef445", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef445", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_varFormatField(self):
        return self.__cjsidl_varFormatField

    @cjsidl_varFormatField.setter
    def cjsidl_varFormatField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varFormatField__cjsidl_varFormatField", None)
        self.__cjsidl_varFormatField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef216"):
                opp_val = getattr(old_value, "cjsidl_typeDef216", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef216"):
                opp_val = getattr(value, "cjsidl_typeDef216", None)
                setattr(value, "cjsidl_typeDef216", self)

    @property
    def cjsidl_varFormatField341(self):
        return self.__cjsidl_varFormatField341

    @cjsidl_varFormatField341.setter
    def cjsidl_varFormatField341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varFormatField__cjsidl_varFormatField341", None)
        self.__cjsidl_varFormatField341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_valueRange"):
                opp_val = getattr(old_value, "cjsidl_valueRange", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_valueRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_valueRange"):
                opp_val = getattr(value, "cjsidl_valueRange", None)
                setattr(value, "cjsidl_valueRange", self)

    @property
    def cjsidl_varFormatField343(self):
        return self.__cjsidl_varFormatField343

    @cjsidl_varFormatField343.setter
    def cjsidl_varFormatField343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varFormatField__cjsidl_varFormatField343", None)
        self.__cjsidl_varFormatField343 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_formatEnumDef"):
                    opp_val = getattr(item, "cjsidl_formatEnumDef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_formatEnumDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_formatEnumDef"):
                    opp_val = getattr(item, "cjsidl_formatEnumDef", None)
                    
                    setattr(item, "cjsidl_formatEnumDef", self)
                    

class cjsidl_varLenField:

    def __init__(self, comment: str, optional: str, fieldFormat: str, name: str, countComment: str, lowerLim: str, upperLim: str, cjsidl_varLenField: "cjsidl_typeDef" = None, cjsidl_varLenField316: "cjsidl_constReference" = None, cjsidl_varLenField319: "cjsidl_scopedConstId" = None, cjsidl_varLenField322: "cjsidl_constReference" = None, cjsidl_varLenField325: "cjsidl_scopedConstId" = None, cjsidl_varLenField443: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.fieldFormat = fieldFormat
        self.name = name
        self.countComment = countComment
        self.lowerLim = lowerLim
        self.upperLim = upperLim
        self.cjsidl_varLenField = cjsidl_varLenField
        self.cjsidl_varLenField316 = cjsidl_varLenField316
        self.cjsidl_varLenField319 = cjsidl_varLenField319
        self.cjsidl_varLenField322 = cjsidl_varLenField322
        self.cjsidl_varLenField325 = cjsidl_varLenField325
        self.cjsidl_varLenField443 = cjsidl_varLenField443
        
    @property
    def upperLim(self) -> str:
        return self.__upperLim

    @upperLim.setter
    def upperLim(self, upperLim: str):
        self.__upperLim = upperLim

    @property
    def lowerLim(self) -> str:
        return self.__lowerLim

    @lowerLim.setter
    def lowerLim(self, lowerLim: str):
        self.__lowerLim = lowerLim

    @property
    def countComment(self) -> str:
        return self.__countComment

    @countComment.setter
    def countComment(self, countComment: str):
        self.__countComment = countComment

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def fieldFormat(self) -> str:
        return self.__fieldFormat

    @fieldFormat.setter
    def fieldFormat(self, fieldFormat: str):
        self.__fieldFormat = fieldFormat

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_varLenField325(self):
        return self.__cjsidl_varLenField325

    @cjsidl_varLenField325.setter
    def cjsidl_varLenField325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField325", None)
        self.__cjsidl_varLenField325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId326"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId326", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId326"):
                opp_val = getattr(value, "cjsidl_scopedConstId326", None)
                setattr(value, "cjsidl_scopedConstId326", self)

    @property
    def cjsidl_varLenField(self):
        return self.__cjsidl_varLenField

    @cjsidl_varLenField.setter
    def cjsidl_varLenField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField", None)
        self.__cjsidl_varLenField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef214"):
                opp_val = getattr(old_value, "cjsidl_typeDef214", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef214"):
                opp_val = getattr(value, "cjsidl_typeDef214", None)
                setattr(value, "cjsidl_typeDef214", self)

    @property
    def cjsidl_varLenField319(self):
        return self.__cjsidl_varLenField319

    @cjsidl_varLenField319.setter
    def cjsidl_varLenField319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField319", None)
        self.__cjsidl_varLenField319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId320"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId320", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId320"):
                opp_val = getattr(value, "cjsidl_scopedConstId320", None)
                setattr(value, "cjsidl_scopedConstId320", self)

    @property
    def cjsidl_varLenField322(self):
        return self.__cjsidl_varLenField322

    @cjsidl_varLenField322.setter
    def cjsidl_varLenField322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField322", None)
        self.__cjsidl_varLenField322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference323"):
                opp_val = getattr(old_value, "cjsidl_constReference323", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference323"):
                opp_val = getattr(value, "cjsidl_constReference323", None)
                setattr(value, "cjsidl_constReference323", self)

    @property
    def cjsidl_varLenField316(self):
        return self.__cjsidl_varLenField316

    @cjsidl_varLenField316.setter
    def cjsidl_varLenField316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField316", None)
        self.__cjsidl_varLenField316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference317"):
                opp_val = getattr(old_value, "cjsidl_constReference317", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference317"):
                opp_val = getattr(value, "cjsidl_constReference317", None)
                setattr(value, "cjsidl_constReference317", self)

    @property
    def cjsidl_varLenField443(self):
        return self.__cjsidl_varLenField443

    @cjsidl_varLenField443.setter
    def cjsidl_varLenField443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenField__cjsidl_varLenField443", None)
        self.__cjsidl_varLenField443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef442"):
                opp_val = getattr(old_value, "cjsidl_recordDef442", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef442"):
                opp_val = getattr(value, "cjsidl_recordDef442", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef442", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_varLenString:

    def __init__(self, comment: str, optional: str, name: str, lowerLim: str, upperLim: str, cjsidl_varLenString: "cjsidl_typeDef" = None, cjsidl_varLenString302: "cjsidl_constReference" = None, cjsidl_varLenString305: "cjsidl_scopedConstId" = None, cjsidl_varLenString296: "cjsidl_constReference" = None, cjsidl_varLenString299: "cjsidl_scopedConstId" = None, cjsidl_varLenString440: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.lowerLim = lowerLim
        self.upperLim = upperLim
        self.cjsidl_varLenString = cjsidl_varLenString
        self.cjsidl_varLenString302 = cjsidl_varLenString302
        self.cjsidl_varLenString305 = cjsidl_varLenString305
        self.cjsidl_varLenString296 = cjsidl_varLenString296
        self.cjsidl_varLenString299 = cjsidl_varLenString299
        self.cjsidl_varLenString440 = cjsidl_varLenString440
        
    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def upperLim(self) -> str:
        return self.__upperLim

    @upperLim.setter
    def upperLim(self, upperLim: str):
        self.__upperLim = upperLim

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lowerLim(self) -> str:
        return self.__lowerLim

    @lowerLim.setter
    def lowerLim(self, lowerLim: str):
        self.__lowerLim = lowerLim

    @property
    def cjsidl_varLenString296(self):
        return self.__cjsidl_varLenString296

    @cjsidl_varLenString296.setter
    def cjsidl_varLenString296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString296", None)
        self.__cjsidl_varLenString296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference297"):
                opp_val = getattr(old_value, "cjsidl_constReference297", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference297"):
                opp_val = getattr(value, "cjsidl_constReference297", None)
                setattr(value, "cjsidl_constReference297", self)

    @property
    def cjsidl_varLenString299(self):
        return self.__cjsidl_varLenString299

    @cjsidl_varLenString299.setter
    def cjsidl_varLenString299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString299", None)
        self.__cjsidl_varLenString299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId300"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId300", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId300"):
                opp_val = getattr(value, "cjsidl_scopedConstId300", None)
                setattr(value, "cjsidl_scopedConstId300", self)

    @property
    def cjsidl_varLenString302(self):
        return self.__cjsidl_varLenString302

    @cjsidl_varLenString302.setter
    def cjsidl_varLenString302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString302", None)
        self.__cjsidl_varLenString302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference303"):
                opp_val = getattr(old_value, "cjsidl_constReference303", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference303"):
                opp_val = getattr(value, "cjsidl_constReference303", None)
                setattr(value, "cjsidl_constReference303", self)

    @property
    def cjsidl_varLenString305(self):
        return self.__cjsidl_varLenString305

    @cjsidl_varLenString305.setter
    def cjsidl_varLenString305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString305", None)
        self.__cjsidl_varLenString305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId306"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId306", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId306"):
                opp_val = getattr(value, "cjsidl_scopedConstId306", None)
                setattr(value, "cjsidl_scopedConstId306", self)

    @property
    def cjsidl_varLenString440(self):
        return self.__cjsidl_varLenString440

    @cjsidl_varLenString440.setter
    def cjsidl_varLenString440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString440", None)
        self.__cjsidl_varLenString440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef439"):
                opp_val = getattr(old_value, "cjsidl_recordDef439", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef439"):
                opp_val = getattr(value, "cjsidl_recordDef439", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef439", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_varLenString(self):
        return self.__cjsidl_varLenString

    @cjsidl_varLenString.setter
    def cjsidl_varLenString(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_varLenString__cjsidl_varLenString", None)
        self.__cjsidl_varLenString = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef212"):
                opp_val = getattr(old_value, "cjsidl_typeDef212", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef212"):
                opp_val = getattr(value, "cjsidl_typeDef212", None)
                setattr(value, "cjsidl_typeDef212", self)

class cjsidl_fixedLenString:

    def __init__(self, comment: str, optional: str, name: str, upperLim: str, cjsidl_fixedLenString: "cjsidl_typeDef" = None, cjsidl_fixedLenString292: "cjsidl_constReference" = None, cjsidl_fixedLenString294: "cjsidl_scopedConstId" = None, cjsidl_fixedLenString437: "cjsidl_recordDef" = None):
        self.comment = comment
        self.optional = optional
        self.name = name
        self.upperLim = upperLim
        self.cjsidl_fixedLenString = cjsidl_fixedLenString
        self.cjsidl_fixedLenString292 = cjsidl_fixedLenString292
        self.cjsidl_fixedLenString294 = cjsidl_fixedLenString294
        self.cjsidl_fixedLenString437 = cjsidl_fixedLenString437
        
    @property
    def upperLim(self) -> str:
        return self.__upperLim

    @upperLim.setter
    def upperLim(self, upperLim: str):
        self.__upperLim = upperLim

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_fixedLenString437(self):
        return self.__cjsidl_fixedLenString437

    @cjsidl_fixedLenString437.setter
    def cjsidl_fixedLenString437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedLenString__cjsidl_fixedLenString437", None)
        self.__cjsidl_fixedLenString437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef436"):
                opp_val = getattr(old_value, "cjsidl_recordDef436", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef436"):
                opp_val = getattr(value, "cjsidl_recordDef436", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef436", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_fixedLenString294(self):
        return self.__cjsidl_fixedLenString294

    @cjsidl_fixedLenString294.setter
    def cjsidl_fixedLenString294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedLenString__cjsidl_fixedLenString294", None)
        self.__cjsidl_fixedLenString294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId"):
                opp_val = getattr(value, "cjsidl_scopedConstId", None)
                setattr(value, "cjsidl_scopedConstId", self)

    @property
    def cjsidl_fixedLenString292(self):
        return self.__cjsidl_fixedLenString292

    @cjsidl_fixedLenString292.setter
    def cjsidl_fixedLenString292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedLenString__cjsidl_fixedLenString292", None)
        self.__cjsidl_fixedLenString292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference"):
                opp_val = getattr(old_value, "cjsidl_constReference", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference"):
                opp_val = getattr(value, "cjsidl_constReference", None)
                setattr(value, "cjsidl_constReference", self)

    @property
    def cjsidl_fixedLenString(self):
        return self.__cjsidl_fixedLenString

    @cjsidl_fixedLenString.setter
    def cjsidl_fixedLenString(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_fixedLenString__cjsidl_fixedLenString", None)
        self.__cjsidl_fixedLenString = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef210"):
                opp_val = getattr(old_value, "cjsidl_typeDef210", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef210"):
                opp_val = getattr(value, "cjsidl_typeDef210", None)
                setattr(value, "cjsidl_typeDef210", self)

class cjsidl_action:

    def __init__(self, comment: str, name: str, cjsidl_action181: "cjsidl_sendActionList" = None, cjsidl_action183: set["cjsidl_guardParam"] = None, cjsidl_action: "cjsidl_actionList" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_action181 = cjsidl_action181
        self.cjsidl_action183 = cjsidl_action183 if cjsidl_action183 is not None else set()
        self.cjsidl_action = cjsidl_action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_action183(self):
        return self.__cjsidl_action183

    @cjsidl_action183.setter
    def cjsidl_action183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_action__cjsidl_action183", None)
        self.__cjsidl_action183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_guardParam184"):
                    opp_val = getattr(item, "cjsidl_guardParam184", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_guardParam184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_guardParam184"):
                    opp_val = getattr(item, "cjsidl_guardParam184", None)
                    
                    setattr(item, "cjsidl_guardParam184", self)
                    

    @property
    def cjsidl_action(self):
        return self.__cjsidl_action

    @cjsidl_action.setter
    def cjsidl_action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_action__cjsidl_action", None)
        self.__cjsidl_action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_actionList178"):
                opp_val = getattr(old_value, "cjsidl_actionList178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_actionList178"):
                opp_val = getattr(value, "cjsidl_actionList178", None)
                if opp_val is None:
                    setattr(value, "cjsidl_actionList178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_action181(self):
        return self.__cjsidl_action181

    @cjsidl_action181.setter
    def cjsidl_action181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_action__cjsidl_action181", None)
        self.__cjsidl_action181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_sendActionList180"):
                opp_val = getattr(old_value, "cjsidl_sendActionList180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_sendActionList180"):
                opp_val = getattr(value, "cjsidl_sendActionList180", None)
                if opp_val is None:
                    setattr(value, "cjsidl_sendActionList180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_guardAction:

    def __init__(self, not: str, name: str, cjsidl_guardAction: "cjsidl_guard" = None, cjsidl_guardAction172: set["cjsidl_guardParam"] = None):
        self.not = not
        self.name = name
        self.cjsidl_guardAction = cjsidl_guardAction
        self.cjsidl_guardAction172 = cjsidl_guardAction172 if cjsidl_guardAction172 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

    @property
    def cjsidl_guardAction172(self):
        return self.__cjsidl_guardAction172

    @cjsidl_guardAction172.setter
    def cjsidl_guardAction172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardAction__cjsidl_guardAction172", None)
        self.__cjsidl_guardAction172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_guardParam173"):
                    opp_val = getattr(item, "cjsidl_guardParam173", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_guardParam173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_guardParam173"):
                    opp_val = getattr(item, "cjsidl_guardParam173", None)
                    
                    setattr(item, "cjsidl_guardParam173", self)
                    

    @property
    def cjsidl_guardAction(self):
        return self.__cjsidl_guardAction

    @cjsidl_guardAction.setter
    def cjsidl_guardAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardAction__cjsidl_guardAction", None)
        self.__cjsidl_guardAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_guard170"):
                opp_val = getattr(old_value, "cjsidl_guard170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_guard170"):
                opp_val = getattr(value, "cjsidl_guard170", None)
                if opp_val is None:
                    setattr(value, "cjsidl_guard170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_guardParam:

    def __init__(self, guardConst: str, cjsidl_guardParam184: "cjsidl_action" = None, cjsidl_guardParam: "cjsidl_popTransition" = None, cjsidl_guardParam173: "cjsidl_guardAction" = None, cjsidl_guardParam175: "cjsidl_transParam" = None):
        self.guardConst = guardConst
        self.cjsidl_guardParam184 = cjsidl_guardParam184
        self.cjsidl_guardParam = cjsidl_guardParam
        self.cjsidl_guardParam173 = cjsidl_guardParam173
        self.cjsidl_guardParam175 = cjsidl_guardParam175
        
    @property
    def guardConst(self) -> str:
        return self.__guardConst

    @guardConst.setter
    def guardConst(self, guardConst: str):
        self.__guardConst = guardConst

    @property
    def cjsidl_guardParam184(self):
        return self.__cjsidl_guardParam184

    @cjsidl_guardParam184.setter
    def cjsidl_guardParam184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardParam__cjsidl_guardParam184", None)
        self.__cjsidl_guardParam184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_action183"):
                opp_val = getattr(old_value, "cjsidl_action183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_action183"):
                opp_val = getattr(value, "cjsidl_action183", None)
                if opp_val is None:
                    setattr(value, "cjsidl_action183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_guardParam173(self):
        return self.__cjsidl_guardParam173

    @cjsidl_guardParam173.setter
    def cjsidl_guardParam173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardParam__cjsidl_guardParam173", None)
        self.__cjsidl_guardParam173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_guardAction172"):
                opp_val = getattr(old_value, "cjsidl_guardAction172", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_guardAction172"):
                opp_val = getattr(value, "cjsidl_guardAction172", None)
                if opp_val is None:
                    setattr(value, "cjsidl_guardAction172", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_guardParam(self):
        return self.__cjsidl_guardParam

    @cjsidl_guardParam.setter
    def cjsidl_guardParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardParam__cjsidl_guardParam", None)
        self.__cjsidl_guardParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_popTransition159"):
                opp_val = getattr(old_value, "cjsidl_popTransition159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_popTransition159"):
                opp_val = getattr(value, "cjsidl_popTransition159", None)
                if opp_val is None:
                    setattr(value, "cjsidl_popTransition159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_guardParam175(self):
        return self.__cjsidl_guardParam175

    @cjsidl_guardParam175.setter
    def cjsidl_guardParam175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guardParam__cjsidl_guardParam175", None)
        self.__cjsidl_guardParam175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transParam176"):
                opp_val = getattr(old_value, "cjsidl_transParam176", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_transParam176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transParam176"):
                opp_val = getattr(value, "cjsidl_transParam176", None)
                setattr(value, "cjsidl_transParam176", self)

class cjsidl_popTransition:

    def __init__(self, comment: str, cjsidl_popTransition: "cjsidl_transition" = None, cjsidl_popTransition159: set["cjsidl_guardParam"] = None):
        self.comment = comment
        self.cjsidl_popTransition = cjsidl_popTransition
        self.cjsidl_popTransition159 = cjsidl_popTransition159 if cjsidl_popTransition159 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_popTransition159(self):
        return self.__cjsidl_popTransition159

    @cjsidl_popTransition159.setter
    def cjsidl_popTransition159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_popTransition__cjsidl_popTransition159", None)
        self.__cjsidl_popTransition159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_guardParam"):
                    opp_val = getattr(item, "cjsidl_guardParam", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_guardParam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_guardParam"):
                    opp_val = getattr(item, "cjsidl_guardParam", None)
                    
                    setattr(item, "cjsidl_guardParam", self)
                    

    @property
    def cjsidl_popTransition(self):
        return self.__cjsidl_popTransition

    @cjsidl_popTransition.setter
    def cjsidl_popTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_popTransition__cjsidl_popTransition", None)
        self.__cjsidl_popTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transition157"):
                opp_val = getattr(old_value, "cjsidl_transition157", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_transition157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transition157"):
                opp_val = getattr(value, "cjsidl_transition157", None)
                setattr(value, "cjsidl_transition157", self)

class cjsidl_guard:

    def __init__(self, comment: str, equiv: str, logicalOperator: str, cjsidl_guard: "cjsidl_transition" = None, cjsidl_guard140: "cjsidl_defaultTransition" = None, cjsidl_guard170: set["cjsidl_guardAction"] = None):
        self.comment = comment
        self.equiv = equiv
        self.logicalOperator = logicalOperator
        self.cjsidl_guard = cjsidl_guard
        self.cjsidl_guard140 = cjsidl_guard140
        self.cjsidl_guard170 = cjsidl_guard170 if cjsidl_guard170 is not None else set()
        
    @property
    def equiv(self) -> str:
        return self.__equiv

    @equiv.setter
    def equiv(self, equiv: str):
        self.__equiv = equiv

    @property
    def logicalOperator(self) -> str:
        return self.__logicalOperator

    @logicalOperator.setter
    def logicalOperator(self, logicalOperator: str):
        self.__logicalOperator = logicalOperator

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_guard170(self):
        return self.__cjsidl_guard170

    @cjsidl_guard170.setter
    def cjsidl_guard170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guard__cjsidl_guard170", None)
        self.__cjsidl_guard170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_guardAction"):
                    opp_val = getattr(item, "cjsidl_guardAction", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_guardAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_guardAction"):
                    opp_val = getattr(item, "cjsidl_guardAction", None)
                    
                    setattr(item, "cjsidl_guardAction", self)
                    

    @property
    def cjsidl_guard140(self):
        return self.__cjsidl_guard140

    @cjsidl_guard140.setter
    def cjsidl_guard140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guard__cjsidl_guard140", None)
        self.__cjsidl_guard140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_defaultTransition139"):
                opp_val = getattr(old_value, "cjsidl_defaultTransition139", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_defaultTransition139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_defaultTransition139"):
                opp_val = getattr(value, "cjsidl_defaultTransition139", None)
                setattr(value, "cjsidl_defaultTransition139", self)

    @property
    def cjsidl_guard(self):
        return self.__cjsidl_guard

    @cjsidl_guard.setter
    def cjsidl_guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_guard__cjsidl_guard", None)
        self.__cjsidl_guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transition128"):
                opp_val = getattr(old_value, "cjsidl_transition128", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_transition128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transition128"):
                opp_val = getattr(value, "cjsidl_transition128", None)
                setattr(value, "cjsidl_transition128", self)

class cjsidl_scopedEventType:

    pass
class cjsidl_pushTransition:

    def __init__(self, comment: str, cjsidl_pushTransition: "cjsidl_nextState" = None, cjsidl_pushTransition154: "cjsidl_simpleTransition" = None):
        self.comment = comment
        self.cjsidl_pushTransition = cjsidl_pushTransition
        self.cjsidl_pushTransition154 = cjsidl_pushTransition154
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_pushTransition154(self):
        return self.__cjsidl_pushTransition154

    @cjsidl_pushTransition154.setter
    def cjsidl_pushTransition154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_pushTransition__cjsidl_pushTransition154", None)
        self.__cjsidl_pushTransition154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_simpleTransition155"):
                opp_val = getattr(old_value, "cjsidl_simpleTransition155", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_simpleTransition155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_simpleTransition155"):
                opp_val = getattr(value, "cjsidl_simpleTransition155", None)
                setattr(value, "cjsidl_simpleTransition155", self)

    @property
    def cjsidl_pushTransition(self):
        return self.__cjsidl_pushTransition

    @cjsidl_pushTransition.setter
    def cjsidl_pushTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_pushTransition__cjsidl_pushTransition", None)
        self.__cjsidl_pushTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_nextState152"):
                opp_val = getattr(old_value, "cjsidl_nextState152", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_nextState152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_nextState152"):
                opp_val = getattr(value, "cjsidl_nextState152", None)
                setattr(value, "cjsidl_nextState152", self)

class cjsidl_nextState:

    def __init__(self, comment: str, cjsidl_nextState: "cjsidl_simpleTransition" = None, cjsidl_nextState152: "cjsidl_pushTransition" = None, cjsidl_nextState161: "cjsidl_state" = None, cjsidl_nextState164: set["cjsidl_state"] = None, cjsidl_nextState167: "cjsidl_state" = None):
        self.comment = comment
        self.cjsidl_nextState = cjsidl_nextState
        self.cjsidl_nextState152 = cjsidl_nextState152
        self.cjsidl_nextState161 = cjsidl_nextState161
        self.cjsidl_nextState164 = cjsidl_nextState164 if cjsidl_nextState164 is not None else set()
        self.cjsidl_nextState167 = cjsidl_nextState167
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_nextState164(self):
        return self.__cjsidl_nextState164

    @cjsidl_nextState164.setter
    def cjsidl_nextState164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_nextState__cjsidl_nextState164", None)
        self.__cjsidl_nextState164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_state165"):
                    opp_val = getattr(item, "cjsidl_state165", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_state165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_state165"):
                    opp_val = getattr(item, "cjsidl_state165", None)
                    
                    setattr(item, "cjsidl_state165", self)
                    

    @property
    def cjsidl_nextState152(self):
        return self.__cjsidl_nextState152

    @cjsidl_nextState152.setter
    def cjsidl_nextState152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_nextState__cjsidl_nextState152", None)
        self.__cjsidl_nextState152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_pushTransition"):
                opp_val = getattr(old_value, "cjsidl_pushTransition", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_pushTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_pushTransition"):
                opp_val = getattr(value, "cjsidl_pushTransition", None)
                setattr(value, "cjsidl_pushTransition", self)

    @property
    def cjsidl_nextState167(self):
        return self.__cjsidl_nextState167

    @cjsidl_nextState167.setter
    def cjsidl_nextState167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_nextState__cjsidl_nextState167", None)
        self.__cjsidl_nextState167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state168"):
                opp_val = getattr(old_value, "cjsidl_state168", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state168"):
                opp_val = getattr(value, "cjsidl_state168", None)
                setattr(value, "cjsidl_state168", self)

    @property
    def cjsidl_nextState(self):
        return self.__cjsidl_nextState

    @cjsidl_nextState.setter
    def cjsidl_nextState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_nextState__cjsidl_nextState", None)
        self.__cjsidl_nextState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_simpleTransition"):
                opp_val = getattr(old_value, "cjsidl_simpleTransition", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_simpleTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_simpleTransition"):
                opp_val = getattr(value, "cjsidl_simpleTransition", None)
                setattr(value, "cjsidl_simpleTransition", self)

    @property
    def cjsidl_nextState161(self):
        return self.__cjsidl_nextState161

    @cjsidl_nextState161.setter
    def cjsidl_nextState161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_nextState__cjsidl_nextState161", None)
        self.__cjsidl_nextState161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state162"):
                opp_val = getattr(old_value, "cjsidl_state162", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state162"):
                opp_val = getattr(value, "cjsidl_state162", None)
                setattr(value, "cjsidl_state162", self)

class cjsidl_simpleTransition:

    def __init__(self, comment: str, cjsidl_simpleTransition: "cjsidl_nextState" = None, cjsidl_simpleTransition155: "cjsidl_pushTransition" = None):
        self.comment = comment
        self.cjsidl_simpleTransition = cjsidl_simpleTransition
        self.cjsidl_simpleTransition155 = cjsidl_simpleTransition155
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_simpleTransition155(self):
        return self.__cjsidl_simpleTransition155

    @cjsidl_simpleTransition155.setter
    def cjsidl_simpleTransition155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_simpleTransition__cjsidl_simpleTransition155", None)
        self.__cjsidl_simpleTransition155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_pushTransition154"):
                opp_val = getattr(old_value, "cjsidl_pushTransition154", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_pushTransition154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_pushTransition154"):
                opp_val = getattr(value, "cjsidl_pushTransition154", None)
                setattr(value, "cjsidl_pushTransition154", self)

    @property
    def cjsidl_simpleTransition(self):
        return self.__cjsidl_simpleTransition

    @cjsidl_simpleTransition.setter
    def cjsidl_simpleTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_simpleTransition__cjsidl_simpleTransition", None)
        self.__cjsidl_simpleTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_nextState"):
                opp_val = getattr(old_value, "cjsidl_nextState", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_nextState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_nextState"):
                opp_val = getattr(value, "cjsidl_nextState", None)
                setattr(value, "cjsidl_nextState", self)

class cjsidl_internalTransition:

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class cjsidl_sendActionList:

    pass
class cjsidl_actionList:

    pass
class cjsidl_defaultTransition:

    def __init__(self, comment: str, type: str, cjsidl_defaultTransition: "cjsidl_state" = None, cjsidl_defaultTransition104: "cjsidl_defaultState" = None, cjsidl_defaultTransition148: "cjsidl_EObject" = None, cjsidl_defaultTransition139: "cjsidl_guard" = None, cjsidl_defaultTransition142: "cjsidl_actionList" = None, cjsidl_defaultTransition145: "cjsidl_sendActionList" = None):
        self.comment = comment
        self.type = type
        self.cjsidl_defaultTransition = cjsidl_defaultTransition
        self.cjsidl_defaultTransition104 = cjsidl_defaultTransition104
        self.cjsidl_defaultTransition148 = cjsidl_defaultTransition148
        self.cjsidl_defaultTransition139 = cjsidl_defaultTransition139
        self.cjsidl_defaultTransition142 = cjsidl_defaultTransition142
        self.cjsidl_defaultTransition145 = cjsidl_defaultTransition145
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_defaultTransition(self):
        return self.__cjsidl_defaultTransition

    @cjsidl_defaultTransition.setter
    def cjsidl_defaultTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition", None)
        self.__cjsidl_defaultTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state92"):
                opp_val = getattr(old_value, "cjsidl_state92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state92"):
                opp_val = getattr(value, "cjsidl_state92", None)
                if opp_val is None:
                    setattr(value, "cjsidl_state92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_defaultTransition145(self):
        return self.__cjsidl_defaultTransition145

    @cjsidl_defaultTransition145.setter
    def cjsidl_defaultTransition145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition145", None)
        self.__cjsidl_defaultTransition145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_sendActionList146"):
                opp_val = getattr(old_value, "cjsidl_sendActionList146", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_sendActionList146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_sendActionList146"):
                opp_val = getattr(value, "cjsidl_sendActionList146", None)
                setattr(value, "cjsidl_sendActionList146", self)

    @property
    def cjsidl_defaultTransition139(self):
        return self.__cjsidl_defaultTransition139

    @cjsidl_defaultTransition139.setter
    def cjsidl_defaultTransition139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition139", None)
        self.__cjsidl_defaultTransition139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_guard140"):
                opp_val = getattr(old_value, "cjsidl_guard140", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_guard140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_guard140"):
                opp_val = getattr(value, "cjsidl_guard140", None)
                setattr(value, "cjsidl_guard140", self)

    @property
    def cjsidl_defaultTransition104(self):
        return self.__cjsidl_defaultTransition104

    @cjsidl_defaultTransition104.setter
    def cjsidl_defaultTransition104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition104", None)
        self.__cjsidl_defaultTransition104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_defaultState103"):
                opp_val = getattr(old_value, "cjsidl_defaultState103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_defaultState103"):
                opp_val = getattr(value, "cjsidl_defaultState103", None)
                if opp_val is None:
                    setattr(value, "cjsidl_defaultState103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_defaultTransition142(self):
        return self.__cjsidl_defaultTransition142

    @cjsidl_defaultTransition142.setter
    def cjsidl_defaultTransition142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition142", None)
        self.__cjsidl_defaultTransition142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_actionList143"):
                opp_val = getattr(old_value, "cjsidl_actionList143", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_actionList143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_actionList143"):
                opp_val = getattr(value, "cjsidl_actionList143", None)
                setattr(value, "cjsidl_actionList143", self)

    @property
    def cjsidl_defaultTransition148(self):
        return self.__cjsidl_defaultTransition148

    @cjsidl_defaultTransition148.setter
    def cjsidl_defaultTransition148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultTransition__cjsidl_defaultTransition148", None)
        self.__cjsidl_defaultTransition148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject149"):
                opp_val = getattr(old_value, "cjsidl_EObject149", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject149"):
                opp_val = getattr(value, "cjsidl_EObject149", None)
                setattr(value, "cjsidl_EObject149", self)

class cjsidl_transition:

    def __init__(self, comment: str, type: str, name: str, cjsidl_transition: "cjsidl_state" = None, cjsidl_transition101: "cjsidl_defaultState" = None, cjsidl_transition122: set["cjsidl_refAttr"] = None, cjsidl_transition125: "cjsidl_transParams" = None, cjsidl_transition128: "cjsidl_guard" = None, cjsidl_transition130: "cjsidl_actionList" = None, cjsidl_transition133: "cjsidl_sendActionList" = None, cjsidl_transition136: "cjsidl_EObject" = None, cjsidl_transition157: "cjsidl_popTransition" = None):
        self.comment = comment
        self.type = type
        self.name = name
        self.cjsidl_transition = cjsidl_transition
        self.cjsidl_transition101 = cjsidl_transition101
        self.cjsidl_transition122 = cjsidl_transition122 if cjsidl_transition122 is not None else set()
        self.cjsidl_transition125 = cjsidl_transition125
        self.cjsidl_transition128 = cjsidl_transition128
        self.cjsidl_transition130 = cjsidl_transition130
        self.cjsidl_transition133 = cjsidl_transition133
        self.cjsidl_transition136 = cjsidl_transition136
        self.cjsidl_transition157 = cjsidl_transition157
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

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
    def cjsidl_transition101(self):
        return self.__cjsidl_transition101

    @cjsidl_transition101.setter
    def cjsidl_transition101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition101", None)
        self.__cjsidl_transition101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_defaultState100"):
                opp_val = getattr(old_value, "cjsidl_defaultState100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_defaultState100"):
                opp_val = getattr(value, "cjsidl_defaultState100", None)
                if opp_val is None:
                    setattr(value, "cjsidl_defaultState100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_transition125(self):
        return self.__cjsidl_transition125

    @cjsidl_transition125.setter
    def cjsidl_transition125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition125", None)
        self.__cjsidl_transition125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transParams126"):
                opp_val = getattr(old_value, "cjsidl_transParams126", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_transParams126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transParams126"):
                opp_val = getattr(value, "cjsidl_transParams126", None)
                setattr(value, "cjsidl_transParams126", self)

    @property
    def cjsidl_transition133(self):
        return self.__cjsidl_transition133

    @cjsidl_transition133.setter
    def cjsidl_transition133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition133", None)
        self.__cjsidl_transition133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_sendActionList134"):
                opp_val = getattr(old_value, "cjsidl_sendActionList134", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_sendActionList134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_sendActionList134"):
                opp_val = getattr(value, "cjsidl_sendActionList134", None)
                setattr(value, "cjsidl_sendActionList134", self)

    @property
    def cjsidl_transition136(self):
        return self.__cjsidl_transition136

    @cjsidl_transition136.setter
    def cjsidl_transition136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition136", None)
        self.__cjsidl_transition136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject137"):
                opp_val = getattr(old_value, "cjsidl_EObject137", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject137"):
                opp_val = getattr(value, "cjsidl_EObject137", None)
                setattr(value, "cjsidl_EObject137", self)

    @property
    def cjsidl_transition130(self):
        return self.__cjsidl_transition130

    @cjsidl_transition130.setter
    def cjsidl_transition130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition130", None)
        self.__cjsidl_transition130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_actionList131"):
                opp_val = getattr(old_value, "cjsidl_actionList131", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_actionList131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_actionList131"):
                opp_val = getattr(value, "cjsidl_actionList131", None)
                setattr(value, "cjsidl_actionList131", self)

    @property
    def cjsidl_transition128(self):
        return self.__cjsidl_transition128

    @cjsidl_transition128.setter
    def cjsidl_transition128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition128", None)
        self.__cjsidl_transition128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_guard"):
                opp_val = getattr(old_value, "cjsidl_guard", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_guard"):
                opp_val = getattr(value, "cjsidl_guard", None)
                setattr(value, "cjsidl_guard", self)

    @property
    def cjsidl_transition157(self):
        return self.__cjsidl_transition157

    @cjsidl_transition157.setter
    def cjsidl_transition157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition157", None)
        self.__cjsidl_transition157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_popTransition"):
                opp_val = getattr(old_value, "cjsidl_popTransition", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_popTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_popTransition"):
                opp_val = getattr(value, "cjsidl_popTransition", None)
                setattr(value, "cjsidl_popTransition", self)

    @property
    def cjsidl_transition122(self):
        return self.__cjsidl_transition122

    @cjsidl_transition122.setter
    def cjsidl_transition122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition122", None)
        self.__cjsidl_transition122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_refAttr123"):
                    opp_val = getattr(item, "cjsidl_refAttr123", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_refAttr123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_refAttr123"):
                    opp_val = getattr(item, "cjsidl_refAttr123", None)
                    
                    setattr(item, "cjsidl_refAttr123", self)
                    

    @property
    def cjsidl_transition(self):
        return self.__cjsidl_transition

    @cjsidl_transition.setter
    def cjsidl_transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transition__cjsidl_transition", None)
        self.__cjsidl_transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state90"):
                opp_val = getattr(old_value, "cjsidl_state90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state90"):
                opp_val = getattr(value, "cjsidl_state90", None)
                if opp_val is None:
                    setattr(value, "cjsidl_state90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_exit:

    def __init__(self, comment: str, cjsidl_exit110: "cjsidl_actionList" = None, cjsidl_exit113: "cjsidl_sendActionList" = None, cjsidl_exit: "cjsidl_state" = None):
        self.comment = comment
        self.cjsidl_exit110 = cjsidl_exit110
        self.cjsidl_exit113 = cjsidl_exit113
        self.cjsidl_exit = cjsidl_exit
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_exit110(self):
        return self.__cjsidl_exit110

    @cjsidl_exit110.setter
    def cjsidl_exit110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_exit__cjsidl_exit110", None)
        self.__cjsidl_exit110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_actionList111"):
                opp_val = getattr(old_value, "cjsidl_actionList111", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_actionList111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_actionList111"):
                opp_val = getattr(value, "cjsidl_actionList111", None)
                setattr(value, "cjsidl_actionList111", self)

    @property
    def cjsidl_exit(self):
        return self.__cjsidl_exit

    @cjsidl_exit.setter
    def cjsidl_exit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_exit__cjsidl_exit", None)
        self.__cjsidl_exit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state88"):
                opp_val = getattr(old_value, "cjsidl_state88", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state88"):
                opp_val = getattr(value, "cjsidl_state88", None)
                setattr(value, "cjsidl_state88", self)

    @property
    def cjsidl_exit113(self):
        return self.__cjsidl_exit113

    @cjsidl_exit113.setter
    def cjsidl_exit113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_exit__cjsidl_exit113", None)
        self.__cjsidl_exit113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_sendActionList114"):
                opp_val = getattr(old_value, "cjsidl_sendActionList114", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_sendActionList114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_sendActionList114"):
                opp_val = getattr(value, "cjsidl_sendActionList114", None)
                setattr(value, "cjsidl_sendActionList114", self)

class cjsidl_entry:

    def __init__(self, comment: str, cjsidl_entry108: "cjsidl_sendActionList" = None, cjsidl_entry: "cjsidl_state" = None, cjsidl_entry106: "cjsidl_actionList" = None):
        self.comment = comment
        self.cjsidl_entry108 = cjsidl_entry108
        self.cjsidl_entry = cjsidl_entry
        self.cjsidl_entry106 = cjsidl_entry106
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_entry106(self):
        return self.__cjsidl_entry106

    @cjsidl_entry106.setter
    def cjsidl_entry106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_entry__cjsidl_entry106", None)
        self.__cjsidl_entry106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_actionList"):
                opp_val = getattr(old_value, "cjsidl_actionList", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_actionList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_actionList"):
                opp_val = getattr(value, "cjsidl_actionList", None)
                setattr(value, "cjsidl_actionList", self)

    @property
    def cjsidl_entry(self):
        return self.__cjsidl_entry

    @cjsidl_entry.setter
    def cjsidl_entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_entry__cjsidl_entry", None)
        self.__cjsidl_entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state86"):
                opp_val = getattr(old_value, "cjsidl_state86", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state86"):
                opp_val = getattr(value, "cjsidl_state86", None)
                setattr(value, "cjsidl_state86", self)

    @property
    def cjsidl_entry108(self):
        return self.__cjsidl_entry108

    @cjsidl_entry108.setter
    def cjsidl_entry108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_entry__cjsidl_entry108", None)
        self.__cjsidl_entry108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_sendActionList"):
                opp_val = getattr(old_value, "cjsidl_sendActionList", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_sendActionList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_sendActionList"):
                opp_val = getattr(value, "cjsidl_sendActionList", None)
                setattr(value, "cjsidl_sendActionList", self)

class cjsidl_defaultState:

    def __init__(self, comment: str, cjsidl_defaultState: "cjsidl_stateMachine" = None, cjsidl_defaultState95: "cjsidl_state" = None, cjsidl_defaultState100: set["cjsidl_transition"] = None, cjsidl_defaultState103: set["cjsidl_defaultTransition"] = None):
        self.comment = comment
        self.cjsidl_defaultState = cjsidl_defaultState
        self.cjsidl_defaultState95 = cjsidl_defaultState95
        self.cjsidl_defaultState100 = cjsidl_defaultState100 if cjsidl_defaultState100 is not None else set()
        self.cjsidl_defaultState103 = cjsidl_defaultState103 if cjsidl_defaultState103 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_defaultState100(self):
        return self.__cjsidl_defaultState100

    @cjsidl_defaultState100.setter
    def cjsidl_defaultState100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultState__cjsidl_defaultState100", None)
        self.__cjsidl_defaultState100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_transition101"):
                    opp_val = getattr(item, "cjsidl_transition101", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_transition101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_transition101"):
                    opp_val = getattr(item, "cjsidl_transition101", None)
                    
                    setattr(item, "cjsidl_transition101", self)
                    

    @property
    def cjsidl_defaultState103(self):
        return self.__cjsidl_defaultState103

    @cjsidl_defaultState103.setter
    def cjsidl_defaultState103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultState__cjsidl_defaultState103", None)
        self.__cjsidl_defaultState103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_defaultTransition104"):
                    opp_val = getattr(item, "cjsidl_defaultTransition104", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_defaultTransition104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_defaultTransition104"):
                    opp_val = getattr(item, "cjsidl_defaultTransition104", None)
                    
                    setattr(item, "cjsidl_defaultTransition104", self)
                    

    @property
    def cjsidl_defaultState95(self):
        return self.__cjsidl_defaultState95

    @cjsidl_defaultState95.setter
    def cjsidl_defaultState95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultState__cjsidl_defaultState95", None)
        self.__cjsidl_defaultState95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state94"):
                opp_val = getattr(old_value, "cjsidl_state94", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state94"):
                opp_val = getattr(value, "cjsidl_state94", None)
                setattr(value, "cjsidl_state94", self)

    @property
    def cjsidl_defaultState(self):
        return self.__cjsidl_defaultState

    @cjsidl_defaultState.setter
    def cjsidl_defaultState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_defaultState__cjsidl_defaultState", None)
        self.__cjsidl_defaultState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_stateMachine81"):
                opp_val = getattr(old_value, "cjsidl_stateMachine81", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_stateMachine81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_stateMachine81"):
                opp_val = getattr(value, "cjsidl_stateMachine81", None)
                setattr(value, "cjsidl_stateMachine81", self)

class cjsidl_transParam:

    def __init__(self, comment: str, unsignedType: str, name: str, cjsidl_transParam: "cjsidl_transParams" = None, cjsidl_transParam117: "cjsidl_EObject" = None, cjsidl_transParam120: "cjsidl_scopedEventType" = None, cjsidl_transParam176: "cjsidl_guardParam" = None):
        self.comment = comment
        self.unsignedType = unsignedType
        self.name = name
        self.cjsidl_transParam = cjsidl_transParam
        self.cjsidl_transParam117 = cjsidl_transParam117
        self.cjsidl_transParam120 = cjsidl_transParam120
        self.cjsidl_transParam176 = cjsidl_transParam176
        
    @property
    def unsignedType(self) -> str:
        return self.__unsignedType

    @unsignedType.setter
    def unsignedType(self, unsignedType: str):
        self.__unsignedType = unsignedType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_transParam120(self):
        return self.__cjsidl_transParam120

    @cjsidl_transParam120.setter
    def cjsidl_transParam120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transParam__cjsidl_transParam120", None)
        self.__cjsidl_transParam120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedEventType"):
                opp_val = getattr(old_value, "cjsidl_scopedEventType", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedEventType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedEventType"):
                opp_val = getattr(value, "cjsidl_scopedEventType", None)
                setattr(value, "cjsidl_scopedEventType", self)

    @property
    def cjsidl_transParam(self):
        return self.__cjsidl_transParam

    @cjsidl_transParam.setter
    def cjsidl_transParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transParam__cjsidl_transParam", None)
        self.__cjsidl_transParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transParams"):
                opp_val = getattr(old_value, "cjsidl_transParams", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transParams"):
                opp_val = getattr(value, "cjsidl_transParams", None)
                if opp_val is None:
                    setattr(value, "cjsidl_transParams", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_transParam176(self):
        return self.__cjsidl_transParam176

    @cjsidl_transParam176.setter
    def cjsidl_transParam176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transParam__cjsidl_transParam176", None)
        self.__cjsidl_transParam176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_guardParam175"):
                opp_val = getattr(old_value, "cjsidl_guardParam175", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_guardParam175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_guardParam175"):
                opp_val = getattr(value, "cjsidl_guardParam175", None)
                setattr(value, "cjsidl_guardParam175", self)

    @property
    def cjsidl_transParam117(self):
        return self.__cjsidl_transParam117

    @cjsidl_transParam117.setter
    def cjsidl_transParam117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_transParam__cjsidl_transParam117", None)
        self.__cjsidl_transParam117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject118"):
                opp_val = getattr(old_value, "cjsidl_EObject118", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject118"):
                opp_val = getattr(value, "cjsidl_EObject118", None)
                setattr(value, "cjsidl_EObject118", self)

class cjsidl_transParams:

    pass
class cjsidl_startState:

    def __init__(self, comment: str, cjsidl_startState: set["cjsidl_state"] = None, cjsidl_startState72: "cjsidl_state" = None, cjsidl_startState79: "cjsidl_stateMachine" = None):
        self.comment = comment
        self.cjsidl_startState = cjsidl_startState if cjsidl_startState is not None else set()
        self.cjsidl_startState72 = cjsidl_startState72
        self.cjsidl_startState79 = cjsidl_startState79
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_startState72(self):
        return self.__cjsidl_startState72

    @cjsidl_startState72.setter
    def cjsidl_startState72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_startState__cjsidl_startState72", None)
        self.__cjsidl_startState72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state73"):
                opp_val = getattr(old_value, "cjsidl_state73", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_state73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state73"):
                opp_val = getattr(value, "cjsidl_state73", None)
                setattr(value, "cjsidl_state73", self)

    @property
    def cjsidl_startState(self):
        return self.__cjsidl_startState

    @cjsidl_startState.setter
    def cjsidl_startState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_startState__cjsidl_startState", None)
        self.__cjsidl_startState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_state"):
                    opp_val = getattr(item, "cjsidl_state", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_state", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_state"):
                    opp_val = getattr(item, "cjsidl_state", None)
                    
                    setattr(item, "cjsidl_state", self)
                    

    @property
    def cjsidl_startState79(self):
        return self.__cjsidl_startState79

    @cjsidl_startState79.setter
    def cjsidl_startState79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_startState__cjsidl_startState79", None)
        self.__cjsidl_startState79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_stateMachine78"):
                opp_val = getattr(old_value, "cjsidl_stateMachine78", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_stateMachine78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_stateMachine78"):
                opp_val = getattr(value, "cjsidl_stateMachine78", None)
                setattr(value, "cjsidl_stateMachine78", self)

class cjsidl_stateMachine:

    def __init__(self, comment: str, name: str, cjsidl_stateMachine75: set["cjsidl_refAttr"] = None, cjsidl_stateMachine78: "cjsidl_startState" = None, cjsidl_stateMachine: "cjsidl_protocolBehavior" = None, cjsidl_stateMachine81: "cjsidl_defaultState" = None, cjsidl_stateMachine83: set["cjsidl_state"] = None):
        self.comment = comment
        self.name = name
        self.cjsidl_stateMachine75 = cjsidl_stateMachine75 if cjsidl_stateMachine75 is not None else set()
        self.cjsidl_stateMachine78 = cjsidl_stateMachine78
        self.cjsidl_stateMachine = cjsidl_stateMachine
        self.cjsidl_stateMachine81 = cjsidl_stateMachine81
        self.cjsidl_stateMachine83 = cjsidl_stateMachine83 if cjsidl_stateMachine83 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_stateMachine81(self):
        return self.__cjsidl_stateMachine81

    @cjsidl_stateMachine81.setter
    def cjsidl_stateMachine81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_stateMachine__cjsidl_stateMachine81", None)
        self.__cjsidl_stateMachine81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_defaultState"):
                opp_val = getattr(old_value, "cjsidl_defaultState", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_defaultState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_defaultState"):
                opp_val = getattr(value, "cjsidl_defaultState", None)
                setattr(value, "cjsidl_defaultState", self)

    @property
    def cjsidl_stateMachine(self):
        return self.__cjsidl_stateMachine

    @cjsidl_stateMachine.setter
    def cjsidl_stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_stateMachine__cjsidl_stateMachine", None)
        self.__cjsidl_stateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_protocolBehavior69"):
                opp_val = getattr(old_value, "cjsidl_protocolBehavior69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_protocolBehavior69"):
                opp_val = getattr(value, "cjsidl_protocolBehavior69", None)
                if opp_val is None:
                    setattr(value, "cjsidl_protocolBehavior69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_stateMachine83(self):
        return self.__cjsidl_stateMachine83

    @cjsidl_stateMachine83.setter
    def cjsidl_stateMachine83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_stateMachine__cjsidl_stateMachine83", None)
        self.__cjsidl_stateMachine83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_state84"):
                    opp_val = getattr(item, "cjsidl_state84", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_state84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_state84"):
                    opp_val = getattr(item, "cjsidl_state84", None)
                    
                    setattr(item, "cjsidl_state84", self)
                    

    @property
    def cjsidl_stateMachine78(self):
        return self.__cjsidl_stateMachine78

    @cjsidl_stateMachine78.setter
    def cjsidl_stateMachine78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_stateMachine__cjsidl_stateMachine78", None)
        self.__cjsidl_stateMachine78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_startState79"):
                opp_val = getattr(old_value, "cjsidl_startState79", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_startState79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_startState79"):
                opp_val = getattr(value, "cjsidl_startState79", None)
                setattr(value, "cjsidl_startState79", self)

    @property
    def cjsidl_stateMachine75(self):
        return self.__cjsidl_stateMachine75

    @cjsidl_stateMachine75.setter
    def cjsidl_stateMachine75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_stateMachine__cjsidl_stateMachine75", None)
        self.__cjsidl_stateMachine75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_refAttr76"):
                    opp_val = getattr(item, "cjsidl_refAttr76", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_refAttr76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_refAttr76"):
                    opp_val = getattr(item, "cjsidl_refAttr76", None)
                    
                    setattr(item, "cjsidl_refAttr76", self)
                    

class cjsidl_eventDef:

    def __init__(self, name: str, cjsidl_eventDef: "cjsidl_description" = None, cjsidl_eventDef57: "cjsidl_EObject" = None, cjsidl_eventDef60: "cjsidl_EObject" = None, cjsidl_eventDef63: "cjsidl_EObject" = None, cjsidl_eventDef287: "cjsidl_declaredEventDef" = None):
        self.name = name
        self.cjsidl_eventDef = cjsidl_eventDef
        self.cjsidl_eventDef57 = cjsidl_eventDef57
        self.cjsidl_eventDef60 = cjsidl_eventDef60
        self.cjsidl_eventDef63 = cjsidl_eventDef63
        self.cjsidl_eventDef287 = cjsidl_eventDef287
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_eventDef(self):
        return self.__cjsidl_eventDef

    @cjsidl_eventDef.setter
    def cjsidl_eventDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_eventDef__cjsidl_eventDef", None)
        self.__cjsidl_eventDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_description55"):
                opp_val = getattr(old_value, "cjsidl_description55", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_description55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_description55"):
                opp_val = getattr(value, "cjsidl_description55", None)
                setattr(value, "cjsidl_description55", self)

    @property
    def cjsidl_eventDef57(self):
        return self.__cjsidl_eventDef57

    @cjsidl_eventDef57.setter
    def cjsidl_eventDef57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_eventDef__cjsidl_eventDef57", None)
        self.__cjsidl_eventDef57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject58"):
                opp_val = getattr(old_value, "cjsidl_EObject58", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject58"):
                opp_val = getattr(value, "cjsidl_EObject58", None)
                setattr(value, "cjsidl_EObject58", self)

    @property
    def cjsidl_eventDef63(self):
        return self.__cjsidl_eventDef63

    @cjsidl_eventDef63.setter
    def cjsidl_eventDef63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_eventDef__cjsidl_eventDef63", None)
        self.__cjsidl_eventDef63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject64"):
                opp_val = getattr(old_value, "cjsidl_EObject64", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject64"):
                opp_val = getattr(value, "cjsidl_EObject64", None)
                setattr(value, "cjsidl_EObject64", self)

    @property
    def cjsidl_eventDef287(self):
        return self.__cjsidl_eventDef287

    @cjsidl_eventDef287.setter
    def cjsidl_eventDef287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_eventDef__cjsidl_eventDef287", None)
        self.__cjsidl_eventDef287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredEventDef"):
                opp_val = getattr(old_value, "cjsidl_declaredEventDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredEventDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredEventDef"):
                opp_val = getattr(value, "cjsidl_declaredEventDef", None)
                setattr(value, "cjsidl_declaredEventDef", self)

    @property
    def cjsidl_eventDef60(self):
        return self.__cjsidl_eventDef60

    @cjsidl_eventDef60.setter
    def cjsidl_eventDef60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_eventDef__cjsidl_eventDef60", None)
        self.__cjsidl_eventDef60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject61"):
                opp_val = getattr(old_value, "cjsidl_EObject61", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject61"):
                opp_val = getattr(value, "cjsidl_EObject61", None)
                setattr(value, "cjsidl_EObject61", self)

class cjsidl_messageScopedRef:

    def __init__(self, comment: str, name: str, cjsidl_messageScopedRef: "cjsidl_messages" = None, cjsidl_messageScopedRef466: "cjsidl_EObject" = None, cjsidl_messageScopedRef469: set["cjsidl_EObject"] = None, cjsidl_messageScopedRef472: "cjsidl_messageDef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_messageScopedRef = cjsidl_messageScopedRef
        self.cjsidl_messageScopedRef466 = cjsidl_messageScopedRef466
        self.cjsidl_messageScopedRef469 = cjsidl_messageScopedRef469 if cjsidl_messageScopedRef469 is not None else set()
        self.cjsidl_messageScopedRef472 = cjsidl_messageScopedRef472
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_messageScopedRef469(self):
        return self.__cjsidl_messageScopedRef469

    @cjsidl_messageScopedRef469.setter
    def cjsidl_messageScopedRef469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageScopedRef__cjsidl_messageScopedRef469", None)
        self.__cjsidl_messageScopedRef469 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_EObject470"):
                    opp_val = getattr(item, "cjsidl_EObject470", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_EObject470", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_EObject470"):
                    opp_val = getattr(item, "cjsidl_EObject470", None)
                    
                    setattr(item, "cjsidl_EObject470", self)
                    

    @property
    def cjsidl_messageScopedRef(self):
        return self.__cjsidl_messageScopedRef

    @cjsidl_messageScopedRef.setter
    def cjsidl_messageScopedRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageScopedRef__cjsidl_messageScopedRef", None)
        self.__cjsidl_messageScopedRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messages50"):
                opp_val = getattr(old_value, "cjsidl_messages50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messages50"):
                opp_val = getattr(value, "cjsidl_messages50", None)
                if opp_val is None:
                    setattr(value, "cjsidl_messages50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_messageScopedRef472(self):
        return self.__cjsidl_messageScopedRef472

    @cjsidl_messageScopedRef472.setter
    def cjsidl_messageScopedRef472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageScopedRef__cjsidl_messageScopedRef472", None)
        self.__cjsidl_messageScopedRef472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageDef473"):
                opp_val = getattr(old_value, "cjsidl_messageDef473", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageDef473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageDef473"):
                opp_val = getattr(value, "cjsidl_messageDef473", None)
                setattr(value, "cjsidl_messageDef473", self)

    @property
    def cjsidl_messageScopedRef466(self):
        return self.__cjsidl_messageScopedRef466

    @cjsidl_messageScopedRef466.setter
    def cjsidl_messageScopedRef466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageScopedRef__cjsidl_messageScopedRef466", None)
        self.__cjsidl_messageScopedRef466 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject467"):
                opp_val = getattr(old_value, "cjsidl_EObject467", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject467"):
                opp_val = getattr(value, "cjsidl_EObject467", None)
                setattr(value, "cjsidl_EObject467", self)

class cjsidl_messageRef:

    def __init__(self, comment: str, name: str, cjsidl_messageRef: "cjsidl_messages" = None, cjsidl_messageRef66: "cjsidl_messageDef" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_messageRef = cjsidl_messageRef
        self.cjsidl_messageRef66 = cjsidl_messageRef66
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_messageRef(self):
        return self.__cjsidl_messageRef

    @cjsidl_messageRef.setter
    def cjsidl_messageRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageRef__cjsidl_messageRef", None)
        self.__cjsidl_messageRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messages48"):
                opp_val = getattr(old_value, "cjsidl_messages48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messages48"):
                opp_val = getattr(value, "cjsidl_messages48", None)
                if opp_val is None:
                    setattr(value, "cjsidl_messages48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_messageRef66(self):
        return self.__cjsidl_messageRef66

    @cjsidl_messageRef66.setter
    def cjsidl_messageRef66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageRef__cjsidl_messageRef66", None)
        self.__cjsidl_messageRef66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageDef67"):
                opp_val = getattr(old_value, "cjsidl_messageDef67", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageDef67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageDef67"):
                opp_val = getattr(value, "cjsidl_messageDef67", None)
                setattr(value, "cjsidl_messageDef67", self)

class cjsidl_messageDef:

    def __init__(self, command: str, messageID: str, name: str, cjsidl_messageDef: "cjsidl_messages" = None, cjsidl_messageDef67: "cjsidl_messageRef" = None, cjsidl_messageDef192: "cjsidl_typeDef" = None, cjsidl_messageDef224: "cjsidl_description" = None, cjsidl_messageDef227: "cjsidl_EObject" = None, cjsidl_messageDef230: "cjsidl_EObject" = None, cjsidl_messageDef233: "cjsidl_EObject" = None, cjsidl_messageDef473: "cjsidl_messageScopedRef" = None):
        self.command = command
        self.messageID = messageID
        self.name = name
        self.cjsidl_messageDef = cjsidl_messageDef
        self.cjsidl_messageDef67 = cjsidl_messageDef67
        self.cjsidl_messageDef192 = cjsidl_messageDef192
        self.cjsidl_messageDef224 = cjsidl_messageDef224
        self.cjsidl_messageDef227 = cjsidl_messageDef227
        self.cjsidl_messageDef230 = cjsidl_messageDef230
        self.cjsidl_messageDef233 = cjsidl_messageDef233
        self.cjsidl_messageDef473 = cjsidl_messageDef473
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def command(self) -> str:
        return self.__command

    @command.setter
    def command(self, command: str):
        self.__command = command

    @property
    def messageID(self) -> str:
        return self.__messageID

    @messageID.setter
    def messageID(self, messageID: str):
        self.__messageID = messageID

    @property
    def cjsidl_messageDef230(self):
        return self.__cjsidl_messageDef230

    @cjsidl_messageDef230.setter
    def cjsidl_messageDef230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef230", None)
        self.__cjsidl_messageDef230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject231"):
                opp_val = getattr(old_value, "cjsidl_EObject231", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject231"):
                opp_val = getattr(value, "cjsidl_EObject231", None)
                setattr(value, "cjsidl_EObject231", self)

    @property
    def cjsidl_messageDef192(self):
        return self.__cjsidl_messageDef192

    @cjsidl_messageDef192.setter
    def cjsidl_messageDef192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef192", None)
        self.__cjsidl_messageDef192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_typeDef191"):
                opp_val = getattr(old_value, "cjsidl_typeDef191", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_typeDef191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_typeDef191"):
                opp_val = getattr(value, "cjsidl_typeDef191", None)
                setattr(value, "cjsidl_typeDef191", self)

    @property
    def cjsidl_messageDef473(self):
        return self.__cjsidl_messageDef473

    @cjsidl_messageDef473.setter
    def cjsidl_messageDef473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef473", None)
        self.__cjsidl_messageDef473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageScopedRef472"):
                opp_val = getattr(old_value, "cjsidl_messageScopedRef472", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageScopedRef472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageScopedRef472"):
                opp_val = getattr(value, "cjsidl_messageScopedRef472", None)
                setattr(value, "cjsidl_messageScopedRef472", self)

    @property
    def cjsidl_messageDef233(self):
        return self.__cjsidl_messageDef233

    @cjsidl_messageDef233.setter
    def cjsidl_messageDef233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef233", None)
        self.__cjsidl_messageDef233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject234"):
                opp_val = getattr(old_value, "cjsidl_EObject234", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject234"):
                opp_val = getattr(value, "cjsidl_EObject234", None)
                setattr(value, "cjsidl_EObject234", self)

    @property
    def cjsidl_messageDef67(self):
        return self.__cjsidl_messageDef67

    @cjsidl_messageDef67.setter
    def cjsidl_messageDef67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef67", None)
        self.__cjsidl_messageDef67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageRef66"):
                opp_val = getattr(old_value, "cjsidl_messageRef66", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageRef66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageRef66"):
                opp_val = getattr(value, "cjsidl_messageRef66", None)
                setattr(value, "cjsidl_messageRef66", self)

    @property
    def cjsidl_messageDef(self):
        return self.__cjsidl_messageDef

    @cjsidl_messageDef.setter
    def cjsidl_messageDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef", None)
        self.__cjsidl_messageDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messages46"):
                opp_val = getattr(old_value, "cjsidl_messages46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messages46"):
                opp_val = getattr(value, "cjsidl_messages46", None)
                if opp_val is None:
                    setattr(value, "cjsidl_messages46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_messageDef227(self):
        return self.__cjsidl_messageDef227

    @cjsidl_messageDef227.setter
    def cjsidl_messageDef227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef227", None)
        self.__cjsidl_messageDef227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject228"):
                opp_val = getattr(old_value, "cjsidl_EObject228", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject228"):
                opp_val = getattr(value, "cjsidl_EObject228", None)
                setattr(value, "cjsidl_EObject228", self)

    @property
    def cjsidl_messageDef224(self):
        return self.__cjsidl_messageDef224

    @cjsidl_messageDef224.setter
    def cjsidl_messageDef224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageDef__cjsidl_messageDef224", None)
        self.__cjsidl_messageDef224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_description225"):
                opp_val = getattr(old_value, "cjsidl_description225", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_description225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_description225"):
                opp_val = getattr(value, "cjsidl_description225", None)
                setattr(value, "cjsidl_description225", self)

class cjsidl_state:

    def __init__(self, comment: str, initial: str, name: str, cjsidl_state: "cjsidl_startState" = None, cjsidl_state73: "cjsidl_startState" = None, cjsidl_state84: "cjsidl_stateMachine" = None, cjsidl_state86: "cjsidl_entry" = None, cjsidl_state88: "cjsidl_exit" = None, cjsidl_state90: set["cjsidl_transition"] = None, cjsidl_state92: set["cjsidl_defaultTransition"] = None, cjsidl_state94: "cjsidl_defaultState" = None, cjsidl_state98: "cjsidl_state" = None, cjsidl_state96: set["cjsidl_state"] = None, cjsidl_state162: "cjsidl_nextState" = None, cjsidl_state165: "cjsidl_nextState" = None, cjsidl_state168: "cjsidl_nextState" = None):
        self.comment = comment
        self.initial = initial
        self.name = name
        self.cjsidl_state = cjsidl_state
        self.cjsidl_state73 = cjsidl_state73
        self.cjsidl_state84 = cjsidl_state84
        self.cjsidl_state86 = cjsidl_state86
        self.cjsidl_state88 = cjsidl_state88
        self.cjsidl_state90 = cjsidl_state90 if cjsidl_state90 is not None else set()
        self.cjsidl_state92 = cjsidl_state92 if cjsidl_state92 is not None else set()
        self.cjsidl_state94 = cjsidl_state94
        self.cjsidl_state98 = cjsidl_state98
        self.cjsidl_state96 = cjsidl_state96 if cjsidl_state96 is not None else set()
        self.cjsidl_state162 = cjsidl_state162
        self.cjsidl_state165 = cjsidl_state165
        self.cjsidl_state168 = cjsidl_state168
        
    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_state92(self):
        return self.__cjsidl_state92

    @cjsidl_state92.setter
    def cjsidl_state92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state92", None)
        self.__cjsidl_state92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_defaultTransition"):
                    opp_val = getattr(item, "cjsidl_defaultTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_defaultTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_defaultTransition"):
                    opp_val = getattr(item, "cjsidl_defaultTransition", None)
                    
                    setattr(item, "cjsidl_defaultTransition", self)
                    

    @property
    def cjsidl_state88(self):
        return self.__cjsidl_state88

    @cjsidl_state88.setter
    def cjsidl_state88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state88", None)
        self.__cjsidl_state88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_exit"):
                opp_val = getattr(old_value, "cjsidl_exit", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_exit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_exit"):
                opp_val = getattr(value, "cjsidl_exit", None)
                setattr(value, "cjsidl_exit", self)

    @property
    def cjsidl_state98(self):
        return self.__cjsidl_state98

    @cjsidl_state98.setter
    def cjsidl_state98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state98", None)
        self.__cjsidl_state98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_state96"):
                opp_val = getattr(old_value, "cjsidl_state96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_state96"):
                opp_val = getattr(value, "cjsidl_state96", None)
                if opp_val is None:
                    setattr(value, "cjsidl_state96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_state165(self):
        return self.__cjsidl_state165

    @cjsidl_state165.setter
    def cjsidl_state165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state165", None)
        self.__cjsidl_state165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_nextState164"):
                opp_val = getattr(old_value, "cjsidl_nextState164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_nextState164"):
                opp_val = getattr(value, "cjsidl_nextState164", None)
                if opp_val is None:
                    setattr(value, "cjsidl_nextState164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_state86(self):
        return self.__cjsidl_state86

    @cjsidl_state86.setter
    def cjsidl_state86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state86", None)
        self.__cjsidl_state86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_entry"):
                opp_val = getattr(old_value, "cjsidl_entry", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_entry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_entry"):
                opp_val = getattr(value, "cjsidl_entry", None)
                setattr(value, "cjsidl_entry", self)

    @property
    def cjsidl_state73(self):
        return self.__cjsidl_state73

    @cjsidl_state73.setter
    def cjsidl_state73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state73", None)
        self.__cjsidl_state73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_startState72"):
                opp_val = getattr(old_value, "cjsidl_startState72", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_startState72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_startState72"):
                opp_val = getattr(value, "cjsidl_startState72", None)
                setattr(value, "cjsidl_startState72", self)

    @property
    def cjsidl_state96(self):
        return self.__cjsidl_state96

    @cjsidl_state96.setter
    def cjsidl_state96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state96", None)
        self.__cjsidl_state96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_state98"):
                    opp_val = getattr(item, "cjsidl_state98", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_state98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_state98"):
                    opp_val = getattr(item, "cjsidl_state98", None)
                    
                    setattr(item, "cjsidl_state98", self)
                    

    @property
    def cjsidl_state94(self):
        return self.__cjsidl_state94

    @cjsidl_state94.setter
    def cjsidl_state94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state94", None)
        self.__cjsidl_state94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_defaultState95"):
                opp_val = getattr(old_value, "cjsidl_defaultState95", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_defaultState95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_defaultState95"):
                opp_val = getattr(value, "cjsidl_defaultState95", None)
                setattr(value, "cjsidl_defaultState95", self)

    @property
    def cjsidl_state(self):
        return self.__cjsidl_state

    @cjsidl_state.setter
    def cjsidl_state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state", None)
        self.__cjsidl_state = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_startState"):
                opp_val = getattr(old_value, "cjsidl_startState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_startState"):
                opp_val = getattr(value, "cjsidl_startState", None)
                if opp_val is None:
                    setattr(value, "cjsidl_startState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_state84(self):
        return self.__cjsidl_state84

    @cjsidl_state84.setter
    def cjsidl_state84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state84", None)
        self.__cjsidl_state84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_stateMachine83"):
                opp_val = getattr(old_value, "cjsidl_stateMachine83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_stateMachine83"):
                opp_val = getattr(value, "cjsidl_stateMachine83", None)
                if opp_val is None:
                    setattr(value, "cjsidl_stateMachine83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_state168(self):
        return self.__cjsidl_state168

    @cjsidl_state168.setter
    def cjsidl_state168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state168", None)
        self.__cjsidl_state168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_nextState167"):
                opp_val = getattr(old_value, "cjsidl_nextState167", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_nextState167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_nextState167"):
                opp_val = getattr(value, "cjsidl_nextState167", None)
                setattr(value, "cjsidl_nextState167", self)

    @property
    def cjsidl_state90(self):
        return self.__cjsidl_state90

    @cjsidl_state90.setter
    def cjsidl_state90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state90", None)
        self.__cjsidl_state90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_transition"):
                    opp_val = getattr(item, "cjsidl_transition", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_transition"):
                    opp_val = getattr(item, "cjsidl_transition", None)
                    
                    setattr(item, "cjsidl_transition", self)
                    

    @property
    def cjsidl_state162(self):
        return self.__cjsidl_state162

    @cjsidl_state162.setter
    def cjsidl_state162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_state__cjsidl_state162", None)
        self.__cjsidl_state162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_nextState161"):
                opp_val = getattr(old_value, "cjsidl_nextState161", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_nextState161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_nextState161"):
                opp_val = getattr(value, "cjsidl_nextState161", None)
                setattr(value, "cjsidl_nextState161", self)

class cjsidl_typeReference:

    def __init__(self, optional: str, name: str, comment: str, cjsidl_typeReference: "cjsidl_declaredTypeSet" = None, cjsidl_typeReference457: "cjsidl_EObject" = None, cjsidl_typeReference449: "cjsidl_recordDef" = None):
        self.optional = optional
        self.name = name
        self.comment = comment
        self.cjsidl_typeReference = cjsidl_typeReference
        self.cjsidl_typeReference457 = cjsidl_typeReference457
        self.cjsidl_typeReference449 = cjsidl_typeReference449
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_typeReference449(self):
        return self.__cjsidl_typeReference449

    @cjsidl_typeReference449.setter
    def cjsidl_typeReference449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_typeReference__cjsidl_typeReference449", None)
        self.__cjsidl_typeReference449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef448"):
                opp_val = getattr(old_value, "cjsidl_recordDef448", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef448"):
                opp_val = getattr(value, "cjsidl_recordDef448", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef448", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_typeReference(self):
        return self.__cjsidl_typeReference

    @cjsidl_typeReference.setter
    def cjsidl_typeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_typeReference__cjsidl_typeReference", None)
        self.__cjsidl_typeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet37"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet37"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet37", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredTypeSet37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_typeReference457(self):
        return self.__cjsidl_typeReference457

    @cjsidl_typeReference457.setter
    def cjsidl_typeReference457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_typeReference__cjsidl_typeReference457", None)
        self.__cjsidl_typeReference457 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_EObject458"):
                opp_val = getattr(old_value, "cjsidl_EObject458", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_EObject458", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_EObject458"):
                opp_val = getattr(value, "cjsidl_EObject458", None)
                setattr(value, "cjsidl_EObject458", self)

class cjsidl_typeDef:

    pass
class cjsidl_declaredTypeSetRef:

    def __init__(self, comment: str, name: str, cjsidl_declaredTypeSetRef: "cjsidl_declaredTypeSet" = None, cjsidl_declaredTypeSetRef188: "cjsidl_declaredTypeSet" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_declaredTypeSetRef = cjsidl_declaredTypeSetRef
        self.cjsidl_declaredTypeSetRef188 = cjsidl_declaredTypeSetRef188
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_declaredTypeSetRef188(self):
        return self.__cjsidl_declaredTypeSetRef188

    @cjsidl_declaredTypeSetRef188.setter
    def cjsidl_declaredTypeSetRef188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSetRef__cjsidl_declaredTypeSetRef188", None)
        self.__cjsidl_declaredTypeSetRef188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet189"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet189", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredTypeSet189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet189"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet189", None)
                setattr(value, "cjsidl_declaredTypeSet189", self)

    @property
    def cjsidl_declaredTypeSetRef(self):
        return self.__cjsidl_declaredTypeSetRef

    @cjsidl_declaredTypeSetRef.setter
    def cjsidl_declaredTypeSetRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSetRef__cjsidl_declaredTypeSetRef", None)
        self.__cjsidl_declaredTypeSetRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet33"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet33"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet33", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredTypeSet33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_constDef:

    def __init__(self, comment: str, name: str, constValue: str, fieldUnits: str, cjsidl_constDef: "cjsidl_declaredConstSet" = None, cjsidl_constDef186: "cjsidl_simpleNumericType" = None, cjsidl_constDef455: "cjsidl_constReference" = None, cjsidl_constDef503: "cjsidl_scopedConstId" = None):
        self.comment = comment
        self.name = name
        self.constValue = constValue
        self.fieldUnits = fieldUnits
        self.cjsidl_constDef = cjsidl_constDef
        self.cjsidl_constDef186 = cjsidl_constDef186
        self.cjsidl_constDef455 = cjsidl_constDef455
        self.cjsidl_constDef503 = cjsidl_constDef503
        
    @property
    def constValue(self) -> str:
        return self.__constValue

    @constValue.setter
    def constValue(self, constValue: str):
        self.__constValue = constValue

    @property
    def fieldUnits(self) -> str:
        return self.__fieldUnits

    @fieldUnits.setter
    def fieldUnits(self, fieldUnits: str):
        self.__fieldUnits = fieldUnits

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_constDef(self):
        return self.__cjsidl_constDef

    @cjsidl_constDef.setter
    def cjsidl_constDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constDef__cjsidl_constDef", None)
        self.__cjsidl_constDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredConstSet25"):
                opp_val = getattr(old_value, "cjsidl_declaredConstSet25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredConstSet25"):
                opp_val = getattr(value, "cjsidl_declaredConstSet25", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredConstSet25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_constDef186(self):
        return self.__cjsidl_constDef186

    @cjsidl_constDef186.setter
    def cjsidl_constDef186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constDef__cjsidl_constDef186", None)
        self.__cjsidl_constDef186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_simpleNumericType"):
                opp_val = getattr(old_value, "cjsidl_simpleNumericType", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_simpleNumericType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_simpleNumericType"):
                opp_val = getattr(value, "cjsidl_simpleNumericType", None)
                setattr(value, "cjsidl_simpleNumericType", self)

    @property
    def cjsidl_constDef503(self):
        return self.__cjsidl_constDef503

    @cjsidl_constDef503.setter
    def cjsidl_constDef503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constDef__cjsidl_constDef503", None)
        self.__cjsidl_constDef503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedConstId502"):
                opp_val = getattr(old_value, "cjsidl_scopedConstId502", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedConstId502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedConstId502"):
                opp_val = getattr(value, "cjsidl_scopedConstId502", None)
                setattr(value, "cjsidl_scopedConstId502", self)

    @property
    def cjsidl_constDef455(self):
        return self.__cjsidl_constDef455

    @cjsidl_constDef455.setter
    def cjsidl_constDef455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_constDef__cjsidl_constDef455", None)
        self.__cjsidl_constDef455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_constReference454"):
                opp_val = getattr(old_value, "cjsidl_constReference454", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_constReference454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_constReference454"):
                opp_val = getattr(value, "cjsidl_constReference454", None)
                setattr(value, "cjsidl_constReference454", self)

class cjsidl_declaredConstSetRef:

    def __init__(self, comment: str, name: str, cjsidl_declaredConstSetRef: "cjsidl_declaredConstSet" = None, cjsidl_declaredConstSetRef27: "cjsidl_declaredConstSet" = None, cjsidl_declaredConstSetRef31: "cjsidl_declaredTypeSet" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_declaredConstSetRef = cjsidl_declaredConstSetRef
        self.cjsidl_declaredConstSetRef27 = cjsidl_declaredConstSetRef27
        self.cjsidl_declaredConstSetRef31 = cjsidl_declaredConstSetRef31
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_declaredConstSetRef31(self):
        return self.__cjsidl_declaredConstSetRef31

    @cjsidl_declaredConstSetRef31.setter
    def cjsidl_declaredConstSetRef31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSetRef__cjsidl_declaredConstSetRef31", None)
        self.__cjsidl_declaredConstSetRef31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet30"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet30"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet30", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredTypeSet30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_declaredConstSetRef27(self):
        return self.__cjsidl_declaredConstSetRef27

    @cjsidl_declaredConstSetRef27.setter
    def cjsidl_declaredConstSetRef27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSetRef__cjsidl_declaredConstSetRef27", None)
        self.__cjsidl_declaredConstSetRef27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredConstSet28"):
                opp_val = getattr(old_value, "cjsidl_declaredConstSet28", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredConstSet28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredConstSet28"):
                opp_val = getattr(value, "cjsidl_declaredConstSet28", None)
                setattr(value, "cjsidl_declaredConstSet28", self)

    @property
    def cjsidl_declaredConstSetRef(self):
        return self.__cjsidl_declaredConstSetRef

    @cjsidl_declaredConstSetRef.setter
    def cjsidl_declaredConstSetRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSetRef__cjsidl_declaredConstSetRef", None)
        self.__cjsidl_declaredConstSetRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredConstSet23"):
                opp_val = getattr(old_value, "cjsidl_declaredConstSet23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredConstSet23"):
                opp_val = getattr(value, "cjsidl_declaredConstSet23", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredConstSet23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_refAttr:

    def __init__(self, comment: str, name: str, cjsidl_refAttr: "cjsidl_references" = None, cjsidl_refAttr18: "cjsidl_references" = None, cjsidl_refAttr20: "cjsidl_serviceDef" = None, cjsidl_refAttr76: "cjsidl_stateMachine" = None, cjsidl_refAttr123: "cjsidl_transition" = None):
        self.comment = comment
        self.name = name
        self.cjsidl_refAttr = cjsidl_refAttr
        self.cjsidl_refAttr18 = cjsidl_refAttr18
        self.cjsidl_refAttr20 = cjsidl_refAttr20
        self.cjsidl_refAttr76 = cjsidl_refAttr76
        self.cjsidl_refAttr123 = cjsidl_refAttr123
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_refAttr76(self):
        return self.__cjsidl_refAttr76

    @cjsidl_refAttr76.setter
    def cjsidl_refAttr76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_refAttr__cjsidl_refAttr76", None)
        self.__cjsidl_refAttr76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_stateMachine75"):
                opp_val = getattr(old_value, "cjsidl_stateMachine75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_stateMachine75"):
                opp_val = getattr(value, "cjsidl_stateMachine75", None)
                if opp_val is None:
                    setattr(value, "cjsidl_stateMachine75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_refAttr(self):
        return self.__cjsidl_refAttr

    @cjsidl_refAttr.setter
    def cjsidl_refAttr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_refAttr__cjsidl_refAttr", None)
        self.__cjsidl_refAttr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_references15"):
                opp_val = getattr(old_value, "cjsidl_references15", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_references15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_references15"):
                opp_val = getattr(value, "cjsidl_references15", None)
                setattr(value, "cjsidl_references15", self)

    @property
    def cjsidl_refAttr123(self):
        return self.__cjsidl_refAttr123

    @cjsidl_refAttr123.setter
    def cjsidl_refAttr123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_refAttr__cjsidl_refAttr123", None)
        self.__cjsidl_refAttr123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_transition122"):
                opp_val = getattr(old_value, "cjsidl_transition122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_transition122"):
                opp_val = getattr(value, "cjsidl_transition122", None)
                if opp_val is None:
                    setattr(value, "cjsidl_transition122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_refAttr20(self):
        return self.__cjsidl_refAttr20

    @cjsidl_refAttr20.setter
    def cjsidl_refAttr20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_refAttr__cjsidl_refAttr20", None)
        self.__cjsidl_refAttr20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef21"):
                opp_val = getattr(old_value, "cjsidl_serviceDef21", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef21"):
                opp_val = getattr(value, "cjsidl_serviceDef21", None)
                setattr(value, "cjsidl_serviceDef21", self)

    @property
    def cjsidl_refAttr18(self):
        return self.__cjsidl_refAttr18

    @cjsidl_refAttr18.setter
    def cjsidl_refAttr18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_refAttr__cjsidl_refAttr18", None)
        self.__cjsidl_refAttr18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_references17"):
                opp_val = getattr(old_value, "cjsidl_references17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_references17"):
                opp_val = getattr(value, "cjsidl_references17", None)
                if opp_val is None:
                    setattr(value, "cjsidl_references17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_messages:

    pass
class cjsidl_scopedTypeId:

    def __init__(self, comment: str, optional: str, scopedName: str, cjsidl_scopedTypeId: "cjsidl_declaredTypeSet" = None, cjsidl_scopedTypeId452: "cjsidl_recordDef" = None, cjsidl_scopedTypeId493: "cjsidl_scopedType" = None):
        self.comment = comment
        self.optional = optional
        self.scopedName = scopedName
        self.cjsidl_scopedTypeId = cjsidl_scopedTypeId
        self.cjsidl_scopedTypeId452 = cjsidl_scopedTypeId452
        self.cjsidl_scopedTypeId493 = cjsidl_scopedTypeId493
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def scopedName(self) -> str:
        return self.__scopedName

    @scopedName.setter
    def scopedName(self, scopedName: str):
        self.__scopedName = scopedName

    @property
    def optional(self) -> str:
        return self.__optional

    @optional.setter
    def optional(self, optional: str):
        self.__optional = optional

    @property
    def cjsidl_scopedTypeId452(self):
        return self.__cjsidl_scopedTypeId452

    @cjsidl_scopedTypeId452.setter
    def cjsidl_scopedTypeId452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scopedTypeId__cjsidl_scopedTypeId452", None)
        self.__cjsidl_scopedTypeId452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_recordDef451"):
                opp_val = getattr(old_value, "cjsidl_recordDef451", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_recordDef451"):
                opp_val = getattr(value, "cjsidl_recordDef451", None)
                if opp_val is None:
                    setattr(value, "cjsidl_recordDef451", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cjsidl_scopedTypeId493(self):
        return self.__cjsidl_scopedTypeId493

    @cjsidl_scopedTypeId493.setter
    def cjsidl_scopedTypeId493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scopedTypeId__cjsidl_scopedTypeId493", None)
        self.__cjsidl_scopedTypeId493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_scopedType494"):
                opp_val = getattr(old_value, "cjsidl_scopedType494", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_scopedType494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_scopedType494"):
                opp_val = getattr(value, "cjsidl_scopedType494", None)
                setattr(value, "cjsidl_scopedType494", self)

    @property
    def cjsidl_scopedTypeId(self):
        return self.__cjsidl_scopedTypeId

    @cjsidl_scopedTypeId.setter
    def cjsidl_scopedTypeId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_scopedTypeId__cjsidl_scopedTypeId", None)
        self.__cjsidl_scopedTypeId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet39"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet39"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet39", None)
                if opp_val is None:
                    setattr(value, "cjsidl_declaredTypeSet39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cjsidl_declaredConstSet:

    def __init__(self, constName: str, name: str, constSetVersion: str, cjsidl_declaredConstSet: "cjsidl_serviceDef" = None, cjsidl_declaredConstSet23: set["cjsidl_declaredConstSetRef"] = None, cjsidl_declaredConstSet25: set["cjsidl_constDef"] = None, cjsidl_declaredConstSet28: "cjsidl_declaredConstSetRef" = None):
        self.constName = constName
        self.name = name
        self.constSetVersion = constSetVersion
        self.cjsidl_declaredConstSet = cjsidl_declaredConstSet
        self.cjsidl_declaredConstSet23 = cjsidl_declaredConstSet23 if cjsidl_declaredConstSet23 is not None else set()
        self.cjsidl_declaredConstSet25 = cjsidl_declaredConstSet25 if cjsidl_declaredConstSet25 is not None else set()
        self.cjsidl_declaredConstSet28 = cjsidl_declaredConstSet28
        
    @property
    def constSetVersion(self) -> str:
        return self.__constSetVersion

    @constSetVersion.setter
    def constSetVersion(self, constSetVersion: str):
        self.__constSetVersion = constSetVersion

    @property
    def constName(self) -> str:
        return self.__constName

    @constName.setter
    def constName(self, constName: str):
        self.__constName = constName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cjsidl_declaredConstSet25(self):
        return self.__cjsidl_declaredConstSet25

    @cjsidl_declaredConstSet25.setter
    def cjsidl_declaredConstSet25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSet__cjsidl_declaredConstSet25", None)
        self.__cjsidl_declaredConstSet25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_constDef"):
                    opp_val = getattr(item, "cjsidl_constDef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_constDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_constDef"):
                    opp_val = getattr(item, "cjsidl_constDef", None)
                    
                    setattr(item, "cjsidl_constDef", self)
                    

    @property
    def cjsidl_declaredConstSet28(self):
        return self.__cjsidl_declaredConstSet28

    @cjsidl_declaredConstSet28.setter
    def cjsidl_declaredConstSet28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSet__cjsidl_declaredConstSet28", None)
        self.__cjsidl_declaredConstSet28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredConstSetRef27"):
                opp_val = getattr(old_value, "cjsidl_declaredConstSetRef27", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredConstSetRef27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredConstSetRef27"):
                opp_val = getattr(value, "cjsidl_declaredConstSetRef27", None)
                setattr(value, "cjsidl_declaredConstSetRef27", self)

    @property
    def cjsidl_declaredConstSet23(self):
        return self.__cjsidl_declaredConstSet23

    @cjsidl_declaredConstSet23.setter
    def cjsidl_declaredConstSet23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSet__cjsidl_declaredConstSet23", None)
        self.__cjsidl_declaredConstSet23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_declaredConstSetRef"):
                    opp_val = getattr(item, "cjsidl_declaredConstSetRef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_declaredConstSetRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_declaredConstSetRef"):
                    opp_val = getattr(item, "cjsidl_declaredConstSetRef", None)
                    
                    setattr(item, "cjsidl_declaredConstSetRef", self)
                    

    @property
    def cjsidl_declaredConstSet(self):
        return self.__cjsidl_declaredConstSet

    @cjsidl_declaredConstSet.setter
    def cjsidl_declaredConstSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredConstSet__cjsidl_declaredConstSet", None)
        self.__cjsidl_declaredConstSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef5"):
                opp_val = getattr(old_value, "cjsidl_serviceDef5", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef5"):
                opp_val = getattr(value, "cjsidl_serviceDef5", None)
                setattr(value, "cjsidl_serviceDef5", self)

class cjsidl_references:

    pass
class cjsidl_description:

    def __init__(self, content: str, cjsidl_description: "cjsidl_serviceDef" = None, cjsidl_description55: "cjsidl_eventDef" = None, cjsidl_description225: "cjsidl_messageDef" = None):
        self.content = content
        self.cjsidl_description = cjsidl_description
        self.cjsidl_description55 = cjsidl_description55
        self.cjsidl_description225 = cjsidl_description225
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def cjsidl_description225(self):
        return self.__cjsidl_description225

    @cjsidl_description225.setter
    def cjsidl_description225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_description__cjsidl_description225", None)
        self.__cjsidl_description225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageDef224"):
                opp_val = getattr(old_value, "cjsidl_messageDef224", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageDef224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageDef224"):
                opp_val = getattr(value, "cjsidl_messageDef224", None)
                setattr(value, "cjsidl_messageDef224", self)

    @property
    def cjsidl_description55(self):
        return self.__cjsidl_description55

    @cjsidl_description55.setter
    def cjsidl_description55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_description__cjsidl_description55", None)
        self.__cjsidl_description55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_eventDef"):
                opp_val = getattr(old_value, "cjsidl_eventDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_eventDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_eventDef"):
                opp_val = getattr(value, "cjsidl_eventDef", None)
                setattr(value, "cjsidl_eventDef", self)

    @property
    def cjsidl_description(self):
        return self.__cjsidl_description

    @cjsidl_description.setter
    def cjsidl_description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_description__cjsidl_description", None)
        self.__cjsidl_description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef"):
                opp_val = getattr(old_value, "cjsidl_serviceDef", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef"):
                opp_val = getattr(value, "cjsidl_serviceDef", None)
                setattr(value, "cjsidl_serviceDef", self)

class cjsidl_serviceDef:

    def __init__(self, serviceName: str, name: str, serviceVersion: str, assumpt: str, cjsidl_serviceDef7: "cjsidl_declaredTypeSet" = None, cjsidl_serviceDef9: "cjsidl_messageSet" = None, cjsidl_serviceDef11: "cjsidl_internalEventSet" = None, cjsidl_serviceDef13: "cjsidl_protocolBehavior" = None, cjsidl_serviceDef: "cjsidl_description" = None, cjsidl_serviceDef3: "cjsidl_references" = None, cjsidl_serviceDef5: "cjsidl_declaredConstSet" = None, cjsidl_serviceDef21: "cjsidl_refAttr" = None):
        self.serviceName = serviceName
        self.name = name
        self.serviceVersion = serviceVersion
        self.assumpt = assumpt
        self.cjsidl_serviceDef7 = cjsidl_serviceDef7
        self.cjsidl_serviceDef9 = cjsidl_serviceDef9
        self.cjsidl_serviceDef11 = cjsidl_serviceDef11
        self.cjsidl_serviceDef13 = cjsidl_serviceDef13
        self.cjsidl_serviceDef = cjsidl_serviceDef
        self.cjsidl_serviceDef3 = cjsidl_serviceDef3
        self.cjsidl_serviceDef5 = cjsidl_serviceDef5
        self.cjsidl_serviceDef21 = cjsidl_serviceDef21
        
    @property
    def assumpt(self) -> str:
        return self.__assumpt

    @assumpt.setter
    def assumpt(self, assumpt: str):
        self.__assumpt = assumpt

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def serviceName(self) -> str:
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

    @property
    def serviceVersion(self) -> str:
        return self.__serviceVersion

    @serviceVersion.setter
    def serviceVersion(self, serviceVersion: str):
        self.__serviceVersion = serviceVersion

    @property
    def cjsidl_serviceDef13(self):
        return self.__cjsidl_serviceDef13

    @cjsidl_serviceDef13.setter
    def cjsidl_serviceDef13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef13", None)
        self.__cjsidl_serviceDef13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_protocolBehavior"):
                opp_val = getattr(old_value, "cjsidl_protocolBehavior", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_protocolBehavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_protocolBehavior"):
                opp_val = getattr(value, "cjsidl_protocolBehavior", None)
                setattr(value, "cjsidl_protocolBehavior", self)

    @property
    def cjsidl_serviceDef21(self):
        return self.__cjsidl_serviceDef21

    @cjsidl_serviceDef21.setter
    def cjsidl_serviceDef21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef21", None)
        self.__cjsidl_serviceDef21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_refAttr20"):
                opp_val = getattr(old_value, "cjsidl_refAttr20", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_refAttr20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_refAttr20"):
                opp_val = getattr(value, "cjsidl_refAttr20", None)
                setattr(value, "cjsidl_refAttr20", self)

    @property
    def cjsidl_serviceDef(self):
        return self.__cjsidl_serviceDef

    @cjsidl_serviceDef.setter
    def cjsidl_serviceDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef", None)
        self.__cjsidl_serviceDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_description"):
                opp_val = getattr(old_value, "cjsidl_description", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_description"):
                opp_val = getattr(value, "cjsidl_description", None)
                setattr(value, "cjsidl_description", self)

    @property
    def cjsidl_serviceDef7(self):
        return self.__cjsidl_serviceDef7

    @cjsidl_serviceDef7.setter
    def cjsidl_serviceDef7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef7", None)
        self.__cjsidl_serviceDef7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSet"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSet", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredTypeSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSet"):
                opp_val = getattr(value, "cjsidl_declaredTypeSet", None)
                setattr(value, "cjsidl_declaredTypeSet", self)

    @property
    def cjsidl_serviceDef5(self):
        return self.__cjsidl_serviceDef5

    @cjsidl_serviceDef5.setter
    def cjsidl_serviceDef5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef5", None)
        self.__cjsidl_serviceDef5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredConstSet"):
                opp_val = getattr(old_value, "cjsidl_declaredConstSet", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredConstSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredConstSet"):
                opp_val = getattr(value, "cjsidl_declaredConstSet", None)
                setattr(value, "cjsidl_declaredConstSet", self)

    @property
    def cjsidl_serviceDef3(self):
        return self.__cjsidl_serviceDef3

    @cjsidl_serviceDef3.setter
    def cjsidl_serviceDef3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef3", None)
        self.__cjsidl_serviceDef3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_references"):
                opp_val = getattr(old_value, "cjsidl_references", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_references", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_references"):
                opp_val = getattr(value, "cjsidl_references", None)
                setattr(value, "cjsidl_references", self)

    @property
    def cjsidl_serviceDef9(self):
        return self.__cjsidl_serviceDef9

    @cjsidl_serviceDef9.setter
    def cjsidl_serviceDef9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef9", None)
        self.__cjsidl_serviceDef9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messageSet"):
                opp_val = getattr(old_value, "cjsidl_messageSet", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messageSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messageSet"):
                opp_val = getattr(value, "cjsidl_messageSet", None)
                setattr(value, "cjsidl_messageSet", self)

    @property
    def cjsidl_serviceDef11(self):
        return self.__cjsidl_serviceDef11

    @cjsidl_serviceDef11.setter
    def cjsidl_serviceDef11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_serviceDef__cjsidl_serviceDef11", None)
        self.__cjsidl_serviceDef11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_internalEventSet"):
                opp_val = getattr(old_value, "cjsidl_internalEventSet", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_internalEventSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_internalEventSet"):
                opp_val = getattr(value, "cjsidl_internalEventSet", None)
                setattr(value, "cjsidl_internalEventSet", self)

class cjsidl_EObject:

    pass
class cjsidl_jaus:

    pass
class cjsidl_protocolBehavior:

    def __init__(self, comment: str, stateless: str, cjsidl_protocolBehavior: "cjsidl_serviceDef" = None, cjsidl_protocolBehavior69: set["cjsidl_stateMachine"] = None):
        self.comment = comment
        self.stateless = stateless
        self.cjsidl_protocolBehavior = cjsidl_protocolBehavior
        self.cjsidl_protocolBehavior69 = cjsidl_protocolBehavior69 if cjsidl_protocolBehavior69 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def stateless(self) -> str:
        return self.__stateless

    @stateless.setter
    def stateless(self, stateless: str):
        self.__stateless = stateless

    @property
    def cjsidl_protocolBehavior(self):
        return self.__cjsidl_protocolBehavior

    @cjsidl_protocolBehavior.setter
    def cjsidl_protocolBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_protocolBehavior__cjsidl_protocolBehavior", None)
        self.__cjsidl_protocolBehavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef13"):
                opp_val = getattr(old_value, "cjsidl_serviceDef13", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef13"):
                opp_val = getattr(value, "cjsidl_serviceDef13", None)
                setattr(value, "cjsidl_serviceDef13", self)

    @property
    def cjsidl_protocolBehavior69(self):
        return self.__cjsidl_protocolBehavior69

    @cjsidl_protocolBehavior69.setter
    def cjsidl_protocolBehavior69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_protocolBehavior__cjsidl_protocolBehavior69", None)
        self.__cjsidl_protocolBehavior69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_stateMachine"):
                    opp_val = getattr(item, "cjsidl_stateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_stateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_stateMachine"):
                    opp_val = getattr(item, "cjsidl_stateMachine", None)
                    
                    setattr(item, "cjsidl_stateMachine", self)
                    

class cjsidl_internalEventSet:

    def __init__(self, comment: str, cjsidl_internalEventSet: "cjsidl_serviceDef" = None, cjsidl_internalEventSet52: set["cjsidl_EObject"] = None):
        self.comment = comment
        self.cjsidl_internalEventSet = cjsidl_internalEventSet
        self.cjsidl_internalEventSet52 = cjsidl_internalEventSet52 if cjsidl_internalEventSet52 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cjsidl_internalEventSet(self):
        return self.__cjsidl_internalEventSet

    @cjsidl_internalEventSet.setter
    def cjsidl_internalEventSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_internalEventSet__cjsidl_internalEventSet", None)
        self.__cjsidl_internalEventSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef11"):
                opp_val = getattr(old_value, "cjsidl_serviceDef11", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef11"):
                opp_val = getattr(value, "cjsidl_serviceDef11", None)
                setattr(value, "cjsidl_serviceDef11", self)

    @property
    def cjsidl_internalEventSet52(self):
        return self.__cjsidl_internalEventSet52

    @cjsidl_internalEventSet52.setter
    def cjsidl_internalEventSet52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_internalEventSet__cjsidl_internalEventSet52", None)
        self.__cjsidl_internalEventSet52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_EObject53"):
                    opp_val = getattr(item, "cjsidl_EObject53", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_EObject53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_EObject53"):
                    opp_val = getattr(item, "cjsidl_EObject53", None)
                    
                    setattr(item, "cjsidl_EObject53", self)
                    

class cjsidl_messageSet:

    def __init__(self, comment: str, inputComment: str, outputComment: str, cjsidl_messageSet: "cjsidl_serviceDef" = None, cjsidl_messageSet41: "cjsidl_messages" = None, cjsidl_messageSet43: "cjsidl_messages" = None):
        self.comment = comment
        self.inputComment = inputComment
        self.outputComment = outputComment
        self.cjsidl_messageSet = cjsidl_messageSet
        self.cjsidl_messageSet41 = cjsidl_messageSet41
        self.cjsidl_messageSet43 = cjsidl_messageSet43
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def outputComment(self) -> str:
        return self.__outputComment

    @outputComment.setter
    def outputComment(self, outputComment: str):
        self.__outputComment = outputComment

    @property
    def inputComment(self) -> str:
        return self.__inputComment

    @inputComment.setter
    def inputComment(self, inputComment: str):
        self.__inputComment = inputComment

    @property
    def cjsidl_messageSet41(self):
        return self.__cjsidl_messageSet41

    @cjsidl_messageSet41.setter
    def cjsidl_messageSet41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageSet__cjsidl_messageSet41", None)
        self.__cjsidl_messageSet41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messages"):
                opp_val = getattr(old_value, "cjsidl_messages", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messages"):
                opp_val = getattr(value, "cjsidl_messages", None)
                setattr(value, "cjsidl_messages", self)

    @property
    def cjsidl_messageSet43(self):
        return self.__cjsidl_messageSet43

    @cjsidl_messageSet43.setter
    def cjsidl_messageSet43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageSet__cjsidl_messageSet43", None)
        self.__cjsidl_messageSet43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_messages44"):
                opp_val = getattr(old_value, "cjsidl_messages44", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_messages44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_messages44"):
                opp_val = getattr(value, "cjsidl_messages44", None)
                setattr(value, "cjsidl_messages44", self)

    @property
    def cjsidl_messageSet(self):
        return self.__cjsidl_messageSet

    @cjsidl_messageSet.setter
    def cjsidl_messageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_messageSet__cjsidl_messageSet", None)
        self.__cjsidl_messageSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef9"):
                opp_val = getattr(old_value, "cjsidl_serviceDef9", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef9"):
                opp_val = getattr(value, "cjsidl_serviceDef9", None)
                setattr(value, "cjsidl_serviceDef9", self)

class cjsidl_declaredTypeSet:

    def __init__(self, typeName: str, name: str, version: str, cjsidl_declaredTypeSet: "cjsidl_serviceDef" = None, cjsidl_declaredTypeSet37: set["cjsidl_typeReference"] = None, cjsidl_declaredTypeSet39: set["cjsidl_scopedTypeId"] = None, cjsidl_declaredTypeSet30: set["cjsidl_declaredConstSetRef"] = None, cjsidl_declaredTypeSet33: set["cjsidl_declaredTypeSetRef"] = None, cjsidl_declaredTypeSet35: set["cjsidl_typeDef"] = None, cjsidl_declaredTypeSet189: "cjsidl_declaredTypeSetRef" = None):
        self.typeName = typeName
        self.name = name
        self.version = version
        self.cjsidl_declaredTypeSet = cjsidl_declaredTypeSet
        self.cjsidl_declaredTypeSet37 = cjsidl_declaredTypeSet37 if cjsidl_declaredTypeSet37 is not None else set()
        self.cjsidl_declaredTypeSet39 = cjsidl_declaredTypeSet39 if cjsidl_declaredTypeSet39 is not None else set()
        self.cjsidl_declaredTypeSet30 = cjsidl_declaredTypeSet30 if cjsidl_declaredTypeSet30 is not None else set()
        self.cjsidl_declaredTypeSet33 = cjsidl_declaredTypeSet33 if cjsidl_declaredTypeSet33 is not None else set()
        self.cjsidl_declaredTypeSet35 = cjsidl_declaredTypeSet35 if cjsidl_declaredTypeSet35 is not None else set()
        self.cjsidl_declaredTypeSet189 = cjsidl_declaredTypeSet189
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def cjsidl_declaredTypeSet39(self):
        return self.__cjsidl_declaredTypeSet39

    @cjsidl_declaredTypeSet39.setter
    def cjsidl_declaredTypeSet39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet39", None)
        self.__cjsidl_declaredTypeSet39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_scopedTypeId"):
                    opp_val = getattr(item, "cjsidl_scopedTypeId", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_scopedTypeId", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_scopedTypeId"):
                    opp_val = getattr(item, "cjsidl_scopedTypeId", None)
                    
                    setattr(item, "cjsidl_scopedTypeId", self)
                    

    @property
    def cjsidl_declaredTypeSet37(self):
        return self.__cjsidl_declaredTypeSet37

    @cjsidl_declaredTypeSet37.setter
    def cjsidl_declaredTypeSet37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet37", None)
        self.__cjsidl_declaredTypeSet37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_typeReference"):
                    opp_val = getattr(item, "cjsidl_typeReference", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_typeReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_typeReference"):
                    opp_val = getattr(item, "cjsidl_typeReference", None)
                    
                    setattr(item, "cjsidl_typeReference", self)
                    

    @property
    def cjsidl_declaredTypeSet33(self):
        return self.__cjsidl_declaredTypeSet33

    @cjsidl_declaredTypeSet33.setter
    def cjsidl_declaredTypeSet33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet33", None)
        self.__cjsidl_declaredTypeSet33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_declaredTypeSetRef"):
                    opp_val = getattr(item, "cjsidl_declaredTypeSetRef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_declaredTypeSetRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_declaredTypeSetRef"):
                    opp_val = getattr(item, "cjsidl_declaredTypeSetRef", None)
                    
                    setattr(item, "cjsidl_declaredTypeSetRef", self)
                    

    @property
    def cjsidl_declaredTypeSet189(self):
        return self.__cjsidl_declaredTypeSet189

    @cjsidl_declaredTypeSet189.setter
    def cjsidl_declaredTypeSet189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet189", None)
        self.__cjsidl_declaredTypeSet189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_declaredTypeSetRef188"):
                opp_val = getattr(old_value, "cjsidl_declaredTypeSetRef188", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_declaredTypeSetRef188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_declaredTypeSetRef188"):
                opp_val = getattr(value, "cjsidl_declaredTypeSetRef188", None)
                setattr(value, "cjsidl_declaredTypeSetRef188", self)

    @property
    def cjsidl_declaredTypeSet30(self):
        return self.__cjsidl_declaredTypeSet30

    @cjsidl_declaredTypeSet30.setter
    def cjsidl_declaredTypeSet30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet30", None)
        self.__cjsidl_declaredTypeSet30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_declaredConstSetRef31"):
                    opp_val = getattr(item, "cjsidl_declaredConstSetRef31", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_declaredConstSetRef31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_declaredConstSetRef31"):
                    opp_val = getattr(item, "cjsidl_declaredConstSetRef31", None)
                    
                    setattr(item, "cjsidl_declaredConstSetRef31", self)
                    

    @property
    def cjsidl_declaredTypeSet35(self):
        return self.__cjsidl_declaredTypeSet35

    @cjsidl_declaredTypeSet35.setter
    def cjsidl_declaredTypeSet35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet35", None)
        self.__cjsidl_declaredTypeSet35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cjsidl_typeDef"):
                    opp_val = getattr(item, "cjsidl_typeDef", None)
                    
                    if opp_val == self:
                        setattr(item, "cjsidl_typeDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cjsidl_typeDef"):
                    opp_val = getattr(item, "cjsidl_typeDef", None)
                    
                    setattr(item, "cjsidl_typeDef", self)
                    

    @property
    def cjsidl_declaredTypeSet(self):
        return self.__cjsidl_declaredTypeSet

    @cjsidl_declaredTypeSet.setter
    def cjsidl_declaredTypeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cjsidl_declaredTypeSet__cjsidl_declaredTypeSet", None)
        self.__cjsidl_declaredTypeSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cjsidl_serviceDef7"):
                opp_val = getattr(old_value, "cjsidl_serviceDef7", None)
                if opp_val == self:
                    setattr(old_value, "cjsidl_serviceDef7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cjsidl_serviceDef7"):
                opp_val = getattr(value, "cjsidl_serviceDef7", None)
                setattr(value, "cjsidl_serviceDef7", self)
