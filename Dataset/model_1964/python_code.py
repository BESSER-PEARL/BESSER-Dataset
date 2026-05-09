from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookTypes(Enum):
    Octochechos = "Octochechos"
    Menaion = "Menaion"
    Euchologion = "Euchologion"
    Pentecostarion = "Pentecostarion"
    Triodion = "Triodion"
    Horologion = "Horologion"
    Eothina = "Eothina"
    Heirmologion = "Heirmologion"
    Katavasias = "Katavasias"
    Psalter = "Psalter"
    Lectionary = "Lectionary"
    Other = "Other"
class PeriodType(Enum):
    pascha = "pascha"
    pentecostarion = "pentecostarion"
    triodion = "triodion"
class TemplateStatuses(Enum):
    NA = "NA"
    Draft = "Draft"
    Review = "Review"
    Final = "Final"
class DayOfWeek(Enum):
    Sunday = "Sunday"
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
class BreakType(Enum):
    line = "line"
    page = "page"
class VersionSwitchType(Enum):
    L1 = "L1"
    L2 = "L2"
    Both = "Both"
class MonthName(Enum):
    Jan = "Jan"
    Feb = "Feb"
    Mar = "Mar"
    Apr = "Apr"
    May = "May"
    Jun = "Jun"
    Jul = "Jul"
    Aug = "Aug"
    Sep = "Sep"
    Oct = "Oct"
    Nov = "Nov"
    Dec = "Dec"
class DayOfMonthTypes(Enum):
    D05 = "D05"
    D06 = "D06"
    D07 = "D07"
    D08 = "D08"
    D09 = "D09"
    D10 = "D10"
    D11 = "D11"
    D12 = "D12"
    D13 = "D13"
    D14 = "D14"
    D15 = "D15"
    D16 = "D16"
    D17 = "D17"
    D18 = "D18"
    D19 = "D19"
    D20 = "D20"
    D21 = "D21"
    D22 = "D22"
    D23 = "D23"
    D24 = "D24"
    D25 = "D25"
    D26 = "D26"
    D27 = "D27"
    D28 = "D28"
    D29 = "D29"
    D30 = "D30"
    D31 = "D31"
    D01 = "D01"
    D02 = "D02"
    D03 = "D03"
    D04 = "D04"
class Seasons(Enum):
    Triodion = "Triodion"
    Pentecostarion = "Pentecostarion"
    Nativity_Fast = "Nativity_Fast"
    Apostles_Fast = "Apostles_Fast"
    Dormition_Fast = "Dormition_Fast"
class ModeTypes(Enum):
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"
    M6 = "M6"
    M7 = "M7"
    M8 = "M8"
class DowTypes(Enum):
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    D4 = "D4"
    D5 = "D5"
    D6 = "D6"
    D7 = "D7"
class Language(Enum):
    L1 = "L1"
    L2 = "L2"
class Null(Enum):
    null = "null"


############################################
# Definition of Classes
############################################

class atem_WhenExistsCase:

    pass
class atem_WhenModeOfWeekCase:

    pass
class atem_SundaysBeforeTriodionCase:

    def __init__(self, dsl_SundaysBeforeTriodionCase_Days: int, atem_SundaysBeforeTriodionCase: "atem_WhenSundaysBeforeTriodion" = None, atem_SundaysBeforeTriodionCase157: set["atem_AbstractComponent"] = None):
        self.dsl_SundaysBeforeTriodionCase_Days = dsl_SundaysBeforeTriodionCase_Days
        self.atem_SundaysBeforeTriodionCase = atem_SundaysBeforeTriodionCase
        self.atem_SundaysBeforeTriodionCase157 = atem_SundaysBeforeTriodionCase157 if atem_SundaysBeforeTriodionCase157 is not None else set()
        
        pass
    @property
    def dsl_SundaysBeforeTriodionCase_Days(self):
        return self.__dsl_SundaysBeforeTriodionCase_Days

    @dsl_SundaysBeforeTriodionCase_Days.setter
    def dsl_SundaysBeforeTriodionCase_Days(self, dsl_SundaysBeforeTriodionCase_Days: int):
        self.__dsl_SundaysBeforeTriodionCase_Days = dsl_SundaysBeforeTriodionCase_Days


    @property
    def atem_SundaysBeforeTriodionCase(self):
        return self.__atem_SundaysBeforeTriodionCase

    @atem_SundaysBeforeTriodionCase.setter
    def atem_SundaysBeforeTriodionCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_SundaysBeforeTriodionCase__atem_SundaysBeforeTriodionCase", None)
        self.__atem_SundaysBeforeTriodionCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_WhenSundaysBeforeTriodion"):
                opp_val = getattr(old_value, "atem_WhenSundaysBeforeTriodion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_WhenSundaysBeforeTriodion"):
                opp_val = getattr(value, "atem_WhenSundaysBeforeTriodion", None)
                if opp_val is None:
                    setattr(value, "atem_WhenSundaysBeforeTriodion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def atem_SundaysBeforeTriodionCase157(self):
        return self.__atem_SundaysBeforeTriodionCase157

    @atem_SundaysBeforeTriodionCase157.setter
    def atem_SundaysBeforeTriodionCase157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_SundaysBeforeTriodionCase__atem_SundaysBeforeTriodionCase157", None)
        self.__atem_SundaysBeforeTriodionCase157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_AbstractComponent158"):
                    opp_val = getattr(item, "atem_AbstractComponent158", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_AbstractComponent158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_AbstractComponent158"):
                    opp_val = getattr(item, "atem_AbstractComponent158", None)
                    
                    setattr(item, "atem_AbstractComponent158", self)
                    

class atem_ModeOfWeekSet:

    def __init__(self, dsl_ModeOfWeekSet_MOWs: str, atem_ModeOfWeekSet: "atem_WhenModeOfWeekCase" = None):
        self.dsl_ModeOfWeekSet_MOWs = dsl_ModeOfWeekSet_MOWs
        self.atem_ModeOfWeekSet = atem_ModeOfWeekSet
        
        pass
    @property
    def dsl_ModeOfWeekSet_MOWs(self):
        return self.__dsl_ModeOfWeekSet_MOWs

    @dsl_ModeOfWeekSet_MOWs.setter
    def dsl_ModeOfWeekSet_MOWs(self, dsl_ModeOfWeekSet_MOWs: str):
        self.__dsl_ModeOfWeekSet_MOWs = dsl_ModeOfWeekSet_MOWs


    @property
    def atem_ModeOfWeekSet(self):
        return self.__atem_ModeOfWeekSet

    @atem_ModeOfWeekSet.setter
    def atem_ModeOfWeekSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_ModeOfWeekSet__atem_ModeOfWeekSet", None)
        self.__atem_ModeOfWeekSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_WhenModeOfWeekCase148"):
                opp_val = getattr(old_value, "atem_WhenModeOfWeekCase148", None)
                if opp_val == self:
                    setattr(old_value, "atem_WhenModeOfWeekCase148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_WhenModeOfWeekCase148"):
                opp_val = getattr(value, "atem_WhenModeOfWeekCase148", None)
                setattr(value, "atem_WhenModeOfWeekCase148", self)

class AbstractDayCase:

    pass
class atem_DaySet(AbstractDayCase):

    def __init__(self, dslSetValue_Days: int):
        self.dslSetValue_Days = dslSetValue_Days
        
        pass
    @property
    def dslSetValue_Days(self):
        return self.__dslSetValue_Days

    @dslSetValue_Days.setter
    def dslSetValue_Days(self, dslSetValue_Days: int):
        self.__dslSetValue_Days = dslSetValue_Days


class atem_DayRange(AbstractDayCase):

    def __init__(self, dsl_DayRange_from: int, dsl_Range_To: int):
        self.dsl_DayRange_from = dsl_DayRange_from
        self.dsl_Range_To = dsl_Range_To
        
        pass
    @property
    def dsl_DayRange_from(self):
        return self.__dsl_DayRange_from

    @dsl_DayRange_from.setter
    def dsl_DayRange_from(self, dsl_DayRange_from: int):
        self.__dsl_DayRange_from = dsl_DayRange_from


    @property
    def dsl_Range_To(self):
        return self.__dsl_Range_To

    @dsl_Range_To.setter
    def dsl_Range_To(self, dsl_Range_To: int):
        self.__dsl_Range_To = dsl_Range_To


class atem_AbstractDayCase:

    pass
class AbstractDateCase:

    pass
class atem_DateSet(AbstractDateCase):

    def __init__(self, dslDateSet_Values: int):
        self.dslDateSet_Values = dslDateSet_Values
        
        pass
    @property
    def dslDateSet_Values(self):
        return self.__dslDateSet_Values

    @dslDateSet_Values.setter
    def dslDateSet_Values(self, dslDateSet_Values: int):
        self.__dslDateSet_Values = dslDateSet_Values


class atem_DateRange(AbstractDateCase):

    def __init__(self, dsl_DateRange_from: int, dsl_DateRange_To: int):
        self.dsl_DateRange_from = dsl_DateRange_from
        self.dsl_DateRange_To = dsl_DateRange_To
        
        pass
    @property
    def dsl_DateRange_To(self):
        return self.__dsl_DateRange_To

    @dsl_DateRange_To.setter
    def dsl_DateRange_To(self, dsl_DateRange_To: int):
        self.__dsl_DateRange_To = dsl_DateRange_To


    @property
    def dsl_DateRange_from(self):
        return self.__dsl_DateRange_from

    @dsl_DateRange_from.setter
    def dsl_DateRange_from(self, dsl_DateRange_from: int):
        self.__dsl_DateRange_from = dsl_DateRange_from


class atem_WhenPeriodCase:

    pass
class AbstractDayNameCase:

    pass
class atem_DayNameSet(AbstractDayNameCase):

    def __init__(self, dslDayNameSet_Values: str):
        self.dslDayNameSet_Values = dslDayNameSet_Values
        
        pass
    @property
    def dslDayNameSet_Values(self):
        return self.__dslDayNameSet_Values

    @dslDayNameSet_Values.setter
    def dslDayNameSet_Values(self, dslDayNameSet_Values: str):
        self.__dslDayNameSet_Values = dslDayNameSet_Values


class atem_DayNameRange(AbstractDayNameCase):

    def __init__(self, dsl_DayNameRange_from: str, dsl_DayNameRange_To: str):
        self.dsl_DayNameRange_from = dsl_DayNameRange_from
        self.dsl_DayNameRange_To = dsl_DayNameRange_To
        
        pass
    @property
    def dsl_DayNameRange_from(self):
        return self.__dsl_DayNameRange_from

    @dsl_DayNameRange_from.setter
    def dsl_DayNameRange_from(self, dsl_DayNameRange_from: str):
        self.__dsl_DayNameRange_from = dsl_DayNameRange_from


    @property
    def dsl_DayNameRange_To(self):
        return self.__dsl_DayNameRange_To

    @dsl_DayNameRange_To.setter
    def dsl_DayNameRange_To(self, dsl_DayNameRange_To: str):
        self.__dsl_DayNameRange_To = dsl_DayNameRange_To


class atem_AbstractDayNameCase:

    pass
class atem_WhenDayNameCase:

    pass
class atem_AbstractDateCase:

    pass
class atem_WhenOther:

    pass
class atem_WhenDateCase:

    def __init__(self, dsl_WhenDate_Case_Month: str, atem_WhenDateCase: "atem_WhenDate" = None, atem_WhenDateCase93: "atem_AbstractDateCase" = None, atem_WhenDateCase95: set["atem_AbstractComponent"] = None, atem_WhenDateCase121: "atem_WhenSundayAfterElevationOfCrossDay" = None):
        self.dsl_WhenDate_Case_Month = dsl_WhenDate_Case_Month
        self.atem_WhenDateCase = atem_WhenDateCase
        self.atem_WhenDateCase93 = atem_WhenDateCase93
        self.atem_WhenDateCase95 = atem_WhenDateCase95 if atem_WhenDateCase95 is not None else set()
        self.atem_WhenDateCase121 = atem_WhenDateCase121
        
        pass
    @property
    def dsl_WhenDate_Case_Month(self):
        return self.__dsl_WhenDate_Case_Month

    @dsl_WhenDate_Case_Month.setter
    def dsl_WhenDate_Case_Month(self, dsl_WhenDate_Case_Month: str):
        self.__dsl_WhenDate_Case_Month = dsl_WhenDate_Case_Month


    @property
    def atem_WhenDateCase95(self):
        return self.__atem_WhenDateCase95

    @atem_WhenDateCase95.setter
    def atem_WhenDateCase95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_WhenDateCase__atem_WhenDateCase95", None)
        self.__atem_WhenDateCase95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_AbstractComponent96"):
                    opp_val = getattr(item, "atem_AbstractComponent96", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_AbstractComponent96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_AbstractComponent96"):
                    opp_val = getattr(item, "atem_AbstractComponent96", None)
                    
                    setattr(item, "atem_AbstractComponent96", self)
                    

    @property
    def atem_WhenDateCase121(self):
        return self.__atem_WhenDateCase121

    @atem_WhenDateCase121.setter
    def atem_WhenDateCase121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_WhenDateCase__atem_WhenDateCase121", None)
        self.__atem_WhenDateCase121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_WhenSundayAfterElevationOfCrossDay"):
                opp_val = getattr(old_value, "atem_WhenSundayAfterElevationOfCrossDay", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_WhenSundayAfterElevationOfCrossDay"):
                opp_val = getattr(value, "atem_WhenSundayAfterElevationOfCrossDay", None)
                if opp_val is None:
                    setattr(value, "atem_WhenSundayAfterElevationOfCrossDay", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def atem_WhenDateCase93(self):
        return self.__atem_WhenDateCase93

    @atem_WhenDateCase93.setter
    def atem_WhenDateCase93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_WhenDateCase__atem_WhenDateCase93", None)
        self.__atem_WhenDateCase93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_AbstractDateCase"):
                opp_val = getattr(old_value, "atem_AbstractDateCase", None)
                if opp_val == self:
                    setattr(old_value, "atem_AbstractDateCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_AbstractDateCase"):
                opp_val = getattr(value, "atem_AbstractDateCase", None)
                setattr(value, "atem_AbstractDateCase", self)

    @property
    def atem_WhenDateCase(self):
        return self.__atem_WhenDateCase

    @atem_WhenDateCase.setter
    def atem_WhenDateCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_WhenDateCase__atem_WhenDateCase", None)
        self.__atem_WhenDateCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_WhenDate"):
                opp_val = getattr(old_value, "atem_WhenDate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_WhenDate"):
                opp_val = getattr(value, "atem_WhenDate", None)
                if opp_val is None:
                    setattr(value, "atem_WhenDate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class atem_PrefaceFragment:

    pass
class LdpType:

    pass
class atem_SBT(LdpType):

    def __init__(self, dsl_Display_SundaysBeforeTriodion: bool):
        self.dsl_Display_SundaysBeforeTriodion = dsl_Display_SundaysBeforeTriodion
        
        pass
    @property
    def dsl_Display_SundaysBeforeTriodion(self):
        return self.__dsl_Display_SundaysBeforeTriodion

    @dsl_Display_SundaysBeforeTriodion.setter
    def dsl_Display_SundaysBeforeTriodion(self, dsl_Display_SundaysBeforeTriodion: bool):
        self.__dsl_Display_SundaysBeforeTriodion = dsl_Display_SundaysBeforeTriodion


class atem_GenDate(LdpType):

    def __init__(self, dsl_Display_Date: bool):
        self.dsl_Display_Date = dsl_Display_Date
        
        pass
    @property
    def dsl_Display_Date(self):
        return self.__dsl_Display_Date

    @dsl_Display_Date.setter
    def dsl_Display_Date(self, dsl_Display_Date: bool):
        self.__dsl_Display_Date = dsl_Display_Date


class atem_DOM(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_MOW(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_MCD(LdpType):

    def __init__(self, dsl_MCD_value: bool):
        self.dsl_MCD_value = dsl_MCD_value
        
        pass
    @property
    def dsl_MCD_value(self):
        return self.__dsl_MCD_value

    @dsl_MCD_value.setter
    def dsl_MCD_value(self, dsl_MCD_value: bool):
        self.__dsl_MCD_value = dsl_MCD_value


class atem_GenYear(LdpType):

    def __init__(self, dsl_Display_Year: bool):
        self.dsl_Display_Year = dsl_Display_Year
        
        pass
    @property
    def dsl_Display_Year(self):
        return self.__dsl_Display_Year

    @dsl_Display_Year.setter
    def dsl_Display_Year(self, dsl_Display_Year: bool):
        self.__dsl_Display_Year = dsl_Display_Year


class atem_NOP(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_DOL(LdpType):

    def __init__(self, dsl_Display_DayLukan: bool):
        self.dsl_Display_DayLukan = dsl_Display_DayLukan
        
        pass
    @property
    def dsl_Display_DayLukan(self):
        return self.__dsl_Display_DayLukan

    @dsl_Display_DayLukan.setter
    def dsl_Display_DayLukan(self, dsl_Display_DayLukan: bool):
        self.__dsl_Display_DayLukan = dsl_Display_DayLukan


class atem_WOLC(LdpType):

    def __init__(self, dsl_Display_DayLukan: bool):
        self.dsl_Display_DayLukan = dsl_Display_DayLukan
        
        pass
    @property
    def dsl_Display_DayLukan(self):
        return self.__dsl_Display_DayLukan

    @dsl_Display_DayLukan.setter
    def dsl_Display_DayLukan(self, dsl_Display_DayLukan: bool):
        self.__dsl_Display_DayLukan = dsl_Display_DayLukan


class atem_WDOLC(LdpType):

    def __init__(self, dsl_Display_DayLukan: bool):
        self.dsl_Display_DayLukan = dsl_Display_DayLukan
        
        pass
    @property
    def dsl_Display_DayLukan(self):
        return self.__dsl_Display_DayLukan

    @dsl_Display_DayLukan.setter
    def dsl_Display_DayLukan(self, dsl_Display_DayLukan: bool):
        self.__dsl_Display_DayLukan = dsl_Display_DayLukan


class atem_All(LdpType):

    def __init__(self, dsl_Display_LiturgicalDayProperties: bool):
        self.dsl_Display_LiturgicalDayProperties = dsl_Display_LiturgicalDayProperties
        
        pass
    @property
    def dsl_Display_LiturgicalDayProperties(self):
        return self.__dsl_Display_LiturgicalDayProperties

    @dsl_Display_LiturgicalDayProperties.setter
    def dsl_Display_LiturgicalDayProperties(self, dsl_Display_LiturgicalDayProperties: bool):
        self.__dsl_Display_LiturgicalDayProperties = dsl_Display_LiturgicalDayProperties


class atem_SectionElementType:

    pass
class atem_PrefaceElementType:

    pass
class atem_SOL(LdpType):

    def __init__(self, dsl_Display_StartLukan: bool):
        self.dsl_Display_StartLukan = dsl_Display_StartLukan
        
        pass
    @property
    def dsl_Display_StartLukan(self):
        return self.__dsl_Display_StartLukan

    @dsl_Display_StartLukan.setter
    def dsl_Display_StartLukan(self, dsl_Display_StartLukan: bool):
        self.__dsl_Display_StartLukan = dsl_Display_StartLukan


class atem_SAEC(LdpType):

    def __init__(self, dsl_Display_SundayAfterElevationCross: bool):
        self.dsl_Display_SundayAfterElevationCross = dsl_Display_SundayAfterElevationCross
        
        pass
    @property
    def dsl_Display_SundayAfterElevationCross(self):
        return self.__dsl_Display_SundayAfterElevationCross

    @dsl_Display_SundayAfterElevationCross.setter
    def dsl_Display_SundayAfterElevationCross(self, dsl_Display_SundayAfterElevationCross: bool):
        self.__dsl_Display_SundayAfterElevationCross = dsl_Display_SundayAfterElevationCross


class atem_EOW(LdpType):

    def __init__(self, dsl_Display_Eothinon: bool):
        self.dsl_Display_Eothinon = dsl_Display_Eothinon
        
        pass
    @property
    def dsl_Display_Eothinon(self):
        return self.__dsl_Display_Eothinon

    @dsl_Display_Eothinon.setter
    def dsl_Display_Eothinon(self, dsl_Display_Eothinon: bool):
        self.__dsl_Display_Eothinon = dsl_Display_Eothinon


class atem_DOWT(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_DOWN(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_DOP(LdpType):

    def __init__(self, dsl_Display_Mode: bool):
        self.dsl_Display_Mode = dsl_Display_Mode
        
        pass
    @property
    def dsl_Display_Mode(self):
        return self.__dsl_Display_Mode

    @dsl_Display_Mode.setter
    def dsl_Display_Mode(self, dsl_Display_Mode: bool):
        self.__dsl_Display_Mode = dsl_Display_Mode


class atem_LdpType:

    pass
class atem_Definition:

    pass
class ElementType:

    pass
class atem_TaggedText(ElementType):

    pass
class atem_Lookup(ElementType):

    def __init__(self, dsl_Lookup_Media_Off: bool, dsl_Lookup_Override_Mode_Set: bool, dsl_Lookup_OverrideMode: str, dsl_Lookup_Override__Day_Set: bool, dsl_Lookup_OverrideDay: str, atem_Lookup: "atem_Definition" = None):
        self.dsl_Lookup_Media_Off = dsl_Lookup_Media_Off
        self.dsl_Lookup_Override_Mode_Set = dsl_Lookup_Override_Mode_Set
        self.dsl_Lookup_OverrideMode = dsl_Lookup_OverrideMode
        self.dsl_Lookup_Override__Day_Set = dsl_Lookup_Override__Day_Set
        self.dsl_Lookup_OverrideDay = dsl_Lookup_OverrideDay
        self.atem_Lookup = atem_Lookup
        
        pass
    @property
    def dsl_Lookup_Media_Off(self):
        return self.__dsl_Lookup_Media_Off

    @dsl_Lookup_Media_Off.setter
    def dsl_Lookup_Media_Off(self, dsl_Lookup_Media_Off: bool):
        self.__dsl_Lookup_Media_Off = dsl_Lookup_Media_Off


    @property
    def dsl_Lookup_OverrideDay(self):
        return self.__dsl_Lookup_OverrideDay

    @dsl_Lookup_OverrideDay.setter
    def dsl_Lookup_OverrideDay(self, dsl_Lookup_OverrideDay: str):
        self.__dsl_Lookup_OverrideDay = dsl_Lookup_OverrideDay


    @property
    def dsl_Lookup_Override_Mode_Set(self):
        return self.__dsl_Lookup_Override_Mode_Set

    @dsl_Lookup_Override_Mode_Set.setter
    def dsl_Lookup_Override_Mode_Set(self, dsl_Lookup_Override_Mode_Set: bool):
        self.__dsl_Lookup_Override_Mode_Set = dsl_Lookup_Override_Mode_Set


    @property
    def dsl_Lookup_Override__Day_Set(self):
        return self.__dsl_Lookup_Override__Day_Set

    @dsl_Lookup_Override__Day_Set.setter
    def dsl_Lookup_Override__Day_Set(self, dsl_Lookup_Override__Day_Set: bool):
        self.__dsl_Lookup_Override__Day_Set = dsl_Lookup_Override__Day_Set


    @property
    def dsl_Lookup_OverrideMode(self):
        return self.__dsl_Lookup_OverrideMode

    @dsl_Lookup_OverrideMode.setter
    def dsl_Lookup_OverrideMode(self, dsl_Lookup_OverrideMode: str):
        self.__dsl_Lookup_OverrideMode = dsl_Lookup_OverrideMode


    @property
    def atem_Lookup(self):
        return self.__atem_Lookup

    @atem_Lookup.setter
    def atem_Lookup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Lookup__atem_Lookup", None)
        self.__atem_Lookup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Definition29"):
                opp_val = getattr(old_value, "atem_Definition29", None)
                if opp_val == self:
                    setattr(old_value, "atem_Definition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Definition29"):
                opp_val = getattr(value, "atem_Definition29", None)
                setattr(value, "atem_Definition29", self)

class atem_LDP(ElementType):

    pass
class atem_ResourceText(ElementType):

    def __init__(self, dsl_ResourceText_Media_Off: bool, atem_ResourceText: "atem_Definition" = None):
        self.dsl_ResourceText_Media_Off = dsl_ResourceText_Media_Off
        self.atem_ResourceText = atem_ResourceText
        
        pass
    @property
    def dsl_ResourceText_Media_Off(self):
        return self.__dsl_ResourceText_Media_Off

    @dsl_ResourceText_Media_Off.setter
    def dsl_ResourceText_Media_Off(self, dsl_ResourceText_Media_Off: bool):
        self.__dsl_ResourceText_Media_Off = dsl_ResourceText_Media_Off


    @property
    def atem_ResourceText(self):
        return self.__atem_ResourceText

    @atem_ResourceText.setter
    def atem_ResourceText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_ResourceText__atem_ResourceText", None)
        self.__atem_ResourceText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Definition"):
                opp_val = getattr(old_value, "atem_Definition", None)
                if opp_val == self:
                    setattr(old_value, "atem_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Definition"):
                opp_val = getattr(value, "atem_Definition", None)
                setattr(value, "atem_Definition", self)

class SectionElementType:

    pass
class atem_InfoElementType:

    pass
class atem_ElementType:

    pass
class HeaderFooterFragment:

    pass
class atem_HeaderFooterPageNumber(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterPageNumber: bool):
        self.dsl_HeaderFooterPageNumber = dsl_HeaderFooterPageNumber
        
        pass
    @property
    def dsl_HeaderFooterPageNumber(self):
        return self.__dsl_HeaderFooterPageNumber

    @dsl_HeaderFooterPageNumber.setter
    def dsl_HeaderFooterPageNumber(self, dsl_HeaderFooterPageNumber: bool):
        self.__dsl_HeaderFooterPageNumber = dsl_HeaderFooterPageNumber


class atem_HeaderFooterTitle(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterTitle: bool):
        self.dsl_HeaderFooterTitle = dsl_HeaderFooterTitle
        
        pass
    @property
    def dsl_HeaderFooterTitle(self):
        return self.__dsl_HeaderFooterTitle

    @dsl_HeaderFooterTitle.setter
    def dsl_HeaderFooterTitle(self, dsl_HeaderFooterTitle: bool):
        self.__dsl_HeaderFooterTitle = dsl_HeaderFooterTitle


class atem_HeaderFooterLookup(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterLookup_Language: str, atem_HeaderFooterLookup: set["atem_ElementType"] = None):
        self.dsl_HeaderFooterLookup_Language = dsl_HeaderFooterLookup_Language
        self.atem_HeaderFooterLookup = atem_HeaderFooterLookup if atem_HeaderFooterLookup is not None else set()
        
        pass
    @property
    def dsl_HeaderFooterLookup_Language(self):
        return self.__dsl_HeaderFooterLookup_Language

    @dsl_HeaderFooterLookup_Language.setter
    def dsl_HeaderFooterLookup_Language(self, dsl_HeaderFooterLookup_Language: str):
        self.__dsl_HeaderFooterLookup_Language = dsl_HeaderFooterLookup_Language


    @property
    def atem_HeaderFooterLookup(self):
        return self.__atem_HeaderFooterLookup

    @atem_HeaderFooterLookup.setter
    def atem_HeaderFooterLookup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_HeaderFooterLookup__atem_HeaderFooterLookup", None)
        self.__atem_HeaderFooterLookup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_ElementType"):
                    opp_val = getattr(item, "atem_ElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_ElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_ElementType"):
                    opp_val = getattr(item, "atem_ElementType", None)
                    
                    setattr(item, "atem_ElementType", self)
                    

class atem_HeaderFooterCommemoration(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterCommemoration: bool):
        self.dsl_HeaderFooterCommemoration = dsl_HeaderFooterCommemoration
        
        pass
    @property
    def dsl_HeaderFooterCommemoration(self):
        return self.__dsl_HeaderFooterCommemoration

    @dsl_HeaderFooterCommemoration.setter
    def dsl_HeaderFooterCommemoration(self, dsl_HeaderFooterCommemoration: bool):
        self.__dsl_HeaderFooterCommemoration = dsl_HeaderFooterCommemoration


class atem_HeaderFooterDate(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterDate: bool, dsl_HeaderFooterDate_Language: str):
        self.dsl_HeaderFooterDate = dsl_HeaderFooterDate
        self.dsl_HeaderFooterDate_Language = dsl_HeaderFooterDate_Language
        
        pass
    @property
    def dsl_HeaderFooterDate_Language(self):
        return self.__dsl_HeaderFooterDate_Language

    @dsl_HeaderFooterDate_Language.setter
    def dsl_HeaderFooterDate_Language(self, dsl_HeaderFooterDate_Language: str):
        self.__dsl_HeaderFooterDate_Language = dsl_HeaderFooterDate_Language


    @property
    def dsl_HeaderFooterDate(self):
        return self.__dsl_HeaderFooterDate

    @dsl_HeaderFooterDate.setter
    def dsl_HeaderFooterDate(self, dsl_HeaderFooterDate: bool):
        self.__dsl_HeaderFooterDate = dsl_HeaderFooterDate


class atem_HeaderFooterText(HeaderFooterFragment):

    def __init__(self, dsl_HeaderFooterText: str):
        self.dsl_HeaderFooterText = dsl_HeaderFooterText
        
        pass
    @property
    def dsl_HeaderFooterText(self):
        return self.__dsl_HeaderFooterText

    @dsl_HeaderFooterText.setter
    def dsl_HeaderFooterText(self, dsl_HeaderFooterText: str):
        self.__dsl_HeaderFooterText = dsl_HeaderFooterText


class HeaderFooterColumn:

    pass
class atem_HeaderFooterColumnCenter(HeaderFooterColumn):

    pass
class atem_HeaderFooterColumnRight(HeaderFooterColumn):

    pass
class atem_HeaderFooterColumnLeft(HeaderFooterColumn):

    pass
class PrefaceElementType:

    pass
class InfoElementType:

    pass
class AbstractComponent:

    pass
class atem_WhenTriodionDay(AbstractComponent, SectionElementType):

    pass
class atem_WhenMovableCycleDay(AbstractComponent, SectionElementType):

    pass
class atem_Section(AbstractComponent, PrefaceElementType, SectionElementType):

    def __init__(self, name: str, atem_Section: "atem_Definition" = None, atem_Section42: set["atem_SectionElementType"] = None, atem_Section48: "atem_SectionFragment" = None):
        self.name = name
        self.atem_Section = atem_Section
        self.atem_Section42 = atem_Section42 if atem_Section42 is not None else set()
        self.atem_Section48 = atem_Section48
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def atem_Section48(self):
        return self.__atem_Section48

    @atem_Section48.setter
    def atem_Section48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Section__atem_Section48", None)
        self.__atem_Section48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_SectionFragment"):
                opp_val = getattr(old_value, "atem_SectionFragment", None)
                if opp_val == self:
                    setattr(old_value, "atem_SectionFragment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_SectionFragment"):
                opp_val = getattr(value, "atem_SectionFragment", None)
                setattr(value, "atem_SectionFragment", self)

    @property
    def atem_Section(self):
        return self.__atem_Section

    @atem_Section.setter
    def atem_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Section__atem_Section", None)
        self.__atem_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Definition40"):
                opp_val = getattr(old_value, "atem_Definition40", None)
                if opp_val == self:
                    setattr(old_value, "atem_Definition40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Definition40"):
                opp_val = getattr(value, "atem_Definition40", None)
                setattr(value, "atem_Definition40", self)

    @property
    def atem_Section42(self):
        return self.__atem_Section42

    @atem_Section42.setter
    def atem_Section42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Section__atem_Section42", None)
        self.__atem_Section42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_SectionElementType"):
                    opp_val = getattr(item, "atem_SectionElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_SectionElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_SectionElementType"):
                    opp_val = getattr(item, "atem_SectionElementType", None)
                    
                    setattr(item, "atem_SectionElementType", self)
                    

class atem_WhenExists(AbstractComponent, SectionElementType):

    pass
class atem_WhenDate(AbstractComponent, SectionElementType):

    pass
class atem_WhenSundaysBeforeTriodion(AbstractComponent, SectionElementType):

    pass
class atem_Verse(AbstractComponent, SectionElementType):

    pass
class atem_WhenPascha(AbstractComponent, SectionElementType):

    pass
class atem_PassThroughPdf(AbstractComponent, SectionElementType):

    def __init__(self, dsl_Passthrough_pdf_text: str):
        self.dsl_Passthrough_pdf_text = dsl_Passthrough_pdf_text
        
        pass
    @property
    def dsl_Passthrough_pdf_text(self):
        return self.__dsl_Passthrough_pdf_text

    @dsl_Passthrough_pdf_text.setter
    def dsl_Passthrough_pdf_text(self, dsl_Passthrough_pdf_text: str):
        self.__dsl_Passthrough_pdf_text = dsl_Passthrough_pdf_text


class atem_Media(AbstractComponent, SectionElementType):

    pass
class atem_WhenPentecostarionDay(AbstractComponent, SectionElementType):

    pass
class atem_Dialog(AbstractComponent, SectionElementType):

    pass
class atem_Break(AbstractComponent, SectionElementType):

    def __init__(self, dsl_break_type: str):
        self.dsl_break_type = dsl_break_type
        
        pass
    @property
    def dsl_break_type(self):
        return self.__dsl_break_type

    @dsl_break_type.setter
    def dsl_break_type(self, dsl_break_type: str):
        self.__dsl_break_type = dsl_break_type


class atem_Block(SectionElementType, AbstractComponent, PrefaceElementType, InfoElementType):

    pass
class atem_PassThroughHtml(AbstractComponent, SectionElementType):

    def __init__(self, dsl_Passthrough_html_text: str):
        self.dsl_Passthrough_html_text = dsl_Passthrough_html_text
        
        pass
    @property
    def dsl_Passthrough_html_text(self):
        return self.__dsl_Passthrough_html_text

    @dsl_Passthrough_html_text.setter
    def dsl_Passthrough_html_text(self, dsl_Passthrough_html_text: str):
        self.__dsl_Passthrough_html_text = dsl_Passthrough_html_text


class atem_WhenDayName(AbstractComponent, SectionElementType):

    pass
class atem_Paragraph(InfoElementType, AbstractComponent, PrefaceElementType, SectionElementType):

    pass
class atem_WhenLukanCycleDay(AbstractComponent, SectionElementType):

    pass
class atem_Aid(AbstractComponent):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atem_RestoreLocale(AbstractComponent, SectionElementType):

    def __init__(self, dsl_RestoreLocale: bool):
        self.dsl_RestoreLocale = dsl_RestoreLocale
        
        pass
    @property
    def dsl_RestoreLocale(self):
        return self.__dsl_RestoreLocale

    @dsl_RestoreLocale.setter
    def dsl_RestoreLocale(self, dsl_RestoreLocale: bool):
        self.__dsl_RestoreLocale = dsl_RestoreLocale


class atem_WhenSundayAfterElevationOfCrossDay(AbstractComponent, SectionElementType):

    pass
class atem_Info(AbstractComponent):

    def __init__(self, name: str, atem_Info: set["atem_InfoElementType"] = None):
        self.name = name
        self.atem_Info = atem_Info if atem_Info is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def atem_Info(self):
        return self.__atem_Info

    @atem_Info.setter
    def atem_Info(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Info__atem_Info", None)
        self.__atem_Info = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_InfoElementType"):
                    opp_val = getattr(item, "atem_InfoElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_InfoElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_InfoElementType"):
                    opp_val = getattr(item, "atem_InfoElementType", None)
                    
                    setattr(item, "atem_InfoElementType", self)
                    

class atem_Hymn(AbstractComponent, SectionElementType):

    pass
class atem_Version(AbstractComponent):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atem_Heading1(AbstractComponent, SectionElementType):

    pass
class atem_SubTitle(SectionElementType, AbstractComponent, PrefaceElementType, InfoElementType):

    pass
class atem_Actor(AbstractComponent, SectionElementType):

    pass
class atem_LitBook(AbstractComponent):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atem_SetLocale(AbstractComponent, SectionElementType):

    def __init__(self, dsl_SetLocale_V1: str, dsl_SetLocale_V2: str):
        self.dsl_SetLocale_V1 = dsl_SetLocale_V1
        self.dsl_SetLocale_V2 = dsl_SetLocale_V2
        
        pass
    @property
    def dsl_SetLocale_V1(self):
        return self.__dsl_SetLocale_V1

    @dsl_SetLocale_V1.setter
    def dsl_SetLocale_V1(self, dsl_SetLocale_V1: str):
        self.__dsl_SetLocale_V1 = dsl_SetLocale_V1


    @property
    def dsl_SetLocale_V2(self):
        return self.__dsl_SetLocale_V2

    @dsl_SetLocale_V2.setter
    def dsl_SetLocale_V2(self, dsl_SetLocale_V2: str):
        self.__dsl_SetLocale_V2 = dsl_SetLocale_V2


class atem_Heading2(AbstractComponent, SectionElementType):

    pass
class atem_Reading(AbstractComponent, SectionElementType):

    pass
class atem_Rubric(AbstractComponent, SectionElementType):

    pass
class atem_Title(AbstractComponent, InfoElementType, PrefaceElementType, SectionElementType):

    pass
class atem_Heading3(AbstractComponent, SectionElementType):

    pass
class atem_SectionFragment(AbstractComponent, PrefaceElementType, SectionElementType):

    pass
class atem_TemplateFragment(AbstractComponent, PrefaceElementType, SectionElementType):

    pass
class atem_WhenModeOfWeek(AbstractComponent, SectionElementType):

    pass
class atem_VersionSwitch(AbstractComponent, InfoElementType, PrefaceElementType):

    def __init__(self, dsl_VersionSwitch_flag: str):
        self.dsl_VersionSwitch_flag = dsl_VersionSwitch_flag
        
        pass
    @property
    def dsl_VersionSwitch_flag(self):
        return self.__dsl_VersionSwitch_flag

    @dsl_VersionSwitch_flag.setter
    def dsl_VersionSwitch_flag(self, dsl_VersionSwitch_flag: str):
        self.__dsl_VersionSwitch_flag = dsl_VersionSwitch_flag


class HeadComponent:

    pass
class atem_PageNumber(HeadComponent):

    def __init__(self, dsl_PageNumber_value: int):
        self.dsl_PageNumber_value = dsl_PageNumber_value
        
        pass
    @property
    def dsl_PageNumber_value(self):
        return self.__dsl_PageNumber_value

    @dsl_PageNumber_value.setter
    def dsl_PageNumber_value(self, dsl_PageNumber_value: int):
        self.__dsl_PageNumber_value = dsl_PageNumber_value


class atem_PageFooterOdd(HeadComponent):

    pass
class atem_Commemoration(HeadComponent):

    pass
class atem_Date(HeadComponent, SectionElementType):

    def __init__(self, dsl_Date_month: int, dsl_Date_day: int, dsl_Date_year: int):
        self.dsl_Date_month = dsl_Date_month
        self.dsl_Date_day = dsl_Date_day
        self.dsl_Date_year = dsl_Date_year
        
        pass
    @property
    def dsl_Date_month(self):
        return self.__dsl_Date_month

    @dsl_Date_month.setter
    def dsl_Date_month(self, dsl_Date_month: int):
        self.__dsl_Date_month = dsl_Date_month


    @property
    def dsl_Date_year(self):
        return self.__dsl_Date_year

    @dsl_Date_year.setter
    def dsl_Date_year(self, dsl_Date_year: int):
        self.__dsl_Date_year = dsl_Date_year


    @property
    def dsl_Date_day(self):
        return self.__dsl_Date_day

    @dsl_Date_day.setter
    def dsl_Date_day(self, dsl_Date_day: int):
        self.__dsl_Date_day = dsl_Date_day


class atem_TemplateTitle(HeadComponent):

    pass
class atem_PageFooterEven(HeadComponent):

    pass
class atem_PageHeaderOdd(HeadComponent):

    pass
class atem_HeaderFooterColumn:

    pass
class atem_PageHeaderEven(HeadComponent):

    pass
class atem_PageKeepWithNext(HeadComponent):

    def __init__(self, dsl_PageKeepWithNext_value: str):
        self.dsl_PageKeepWithNext_value = dsl_PageKeepWithNext_value
        
        pass
    @property
    def dsl_PageKeepWithNext_value(self):
        return self.__dsl_PageKeepWithNext_value

    @dsl_PageKeepWithNext_value.setter
    def dsl_PageKeepWithNext_value(self, dsl_PageKeepWithNext_value: str):
        self.__dsl_PageKeepWithNext_value = dsl_PageKeepWithNext_value


class atem_HeaderFooterFragment:

    pass
class atem_Preface:

    def __init__(self, name: str, atem_Preface: "atem_AtemModel" = None, atem_Preface38: set["atem_PrefaceElementType"] = None, atem_Preface46: "atem_PrefaceFragment" = None):
        self.name = name
        self.atem_Preface = atem_Preface
        self.atem_Preface38 = atem_Preface38 if atem_Preface38 is not None else set()
        self.atem_Preface46 = atem_Preface46
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def atem_Preface(self):
        return self.__atem_Preface

    @atem_Preface.setter
    def atem_Preface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Preface__atem_Preface", None)
        self.__atem_Preface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_AtemModel8"):
                opp_val = getattr(old_value, "atem_AtemModel8", None)
                if opp_val == self:
                    setattr(old_value, "atem_AtemModel8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_AtemModel8"):
                opp_val = getattr(value, "atem_AtemModel8", None)
                setattr(value, "atem_AtemModel8", self)

    @property
    def atem_Preface38(self):
        return self.__atem_Preface38

    @atem_Preface38.setter
    def atem_Preface38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Preface__atem_Preface38", None)
        self.__atem_Preface38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_PrefaceElementType"):
                    opp_val = getattr(item, "atem_PrefaceElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_PrefaceElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_PrefaceElementType"):
                    opp_val = getattr(item, "atem_PrefaceElementType", None)
                    
                    setattr(item, "atem_PrefaceElementType", self)
                    

    @property
    def atem_Preface46(self):
        return self.__atem_Preface46

    @atem_Preface46.setter
    def atem_Preface46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Preface__atem_Preface46", None)
        self.__atem_Preface46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_PrefaceFragment"):
                opp_val = getattr(old_value, "atem_PrefaceFragment", None)
                if opp_val == self:
                    setattr(old_value, "atem_PrefaceFragment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_PrefaceFragment"):
                opp_val = getattr(value, "atem_PrefaceFragment", None)
                setattr(value, "atem_PrefaceFragment", self)

class atem_Head:

    pass
class atem_Driver:

    def __init__(self, dsl_Driver_RegEx: str, dsl_Driver_Status: str, atem_Driver: "atem_AtemModel" = None):
        self.dsl_Driver_RegEx = dsl_Driver_RegEx
        self.dsl_Driver_Status = dsl_Driver_Status
        self.atem_Driver = atem_Driver
        
        pass
    @property
    def dsl_Driver_RegEx(self):
        return self.__dsl_Driver_RegEx

    @dsl_Driver_RegEx.setter
    def dsl_Driver_RegEx(self, dsl_Driver_RegEx: str):
        self.__dsl_Driver_RegEx = dsl_Driver_RegEx


    @property
    def dsl_Driver_Status(self):
        return self.__dsl_Driver_Status

    @dsl_Driver_Status.setter
    def dsl_Driver_Status(self, dsl_Driver_Status: str):
        self.__dsl_Driver_Status = dsl_Driver_Status


    @property
    def atem_Driver(self):
        return self.__atem_Driver

    @atem_Driver.setter
    def atem_Driver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Driver__atem_Driver", None)
        self.__atem_Driver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_AtemModel4"):
                opp_val = getattr(old_value, "atem_AtemModel4", None)
                if opp_val == self:
                    setattr(old_value, "atem_AtemModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_AtemModel4"):
                opp_val = getattr(value, "atem_AtemModel4", None)
                setattr(value, "atem_AtemModel4", self)

class atem_Import:

    def __init__(self, importedNamespace: str, atem_Import: "atem_AtemModel" = None):
        self.importedNamespace = importedNamespace
        self.atem_Import = atem_Import
        
        pass
    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


    @property
    def atem_Import(self):
        return self.__atem_Import

    @atem_Import.setter
    def atem_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_Import__atem_Import", None)
        self.__atem_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_AtemModel2"):
                opp_val = getattr(old_value, "atem_AtemModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_AtemModel2"):
                opp_val = getattr(value, "atem_AtemModel2", None)
                if opp_val is None:
                    setattr(value, "atem_AtemModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class atem_TemplateStatus:

    def __init__(self, dsl_TemplateStatus: str, atem_TemplateStatus: "atem_AtemModel" = None):
        self.dsl_TemplateStatus = dsl_TemplateStatus
        self.atem_TemplateStatus = atem_TemplateStatus
        
        pass
    @property
    def dsl_TemplateStatus(self):
        return self.__dsl_TemplateStatus

    @dsl_TemplateStatus.setter
    def dsl_TemplateStatus(self, dsl_TemplateStatus: str):
        self.__dsl_TemplateStatus = dsl_TemplateStatus


    @property
    def atem_TemplateStatus(self):
        return self.__atem_TemplateStatus

    @atem_TemplateStatus.setter
    def atem_TemplateStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_TemplateStatus__atem_TemplateStatus", None)
        self.__atem_TemplateStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_AtemModel"):
                opp_val = getattr(old_value, "atem_AtemModel", None)
                if opp_val == self:
                    setattr(old_value, "atem_AtemModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_AtemModel"):
                opp_val = getattr(value, "atem_AtemModel", None)
                setattr(value, "atem_AtemModel", self)

class atem_AtemModel:

    def __init__(self, name: str, atem_AtemModel10: set["atem_AbstractComponent"] = None, atem_AtemModel: "atem_TemplateStatus" = None, atem_AtemModel2: set["atem_Import"] = None, atem_AtemModel4: "atem_Driver" = None, atem_AtemModel6: "atem_Head" = None, atem_AtemModel8: "atem_Preface" = None, atem_AtemModel44: "atem_TemplateFragment" = None):
        self.name = name
        self.atem_AtemModel10 = atem_AtemModel10 if atem_AtemModel10 is not None else set()
        self.atem_AtemModel = atem_AtemModel
        self.atem_AtemModel2 = atem_AtemModel2 if atem_AtemModel2 is not None else set()
        self.atem_AtemModel4 = atem_AtemModel4
        self.atem_AtemModel6 = atem_AtemModel6
        self.atem_AtemModel8 = atem_AtemModel8
        self.atem_AtemModel44 = atem_AtemModel44
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def atem_AtemModel44(self):
        return self.__atem_AtemModel44

    @atem_AtemModel44.setter
    def atem_AtemModel44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel44", None)
        self.__atem_AtemModel44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_TemplateFragment"):
                opp_val = getattr(old_value, "atem_TemplateFragment", None)
                if opp_val == self:
                    setattr(old_value, "atem_TemplateFragment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_TemplateFragment"):
                opp_val = getattr(value, "atem_TemplateFragment", None)
                setattr(value, "atem_TemplateFragment", self)

    @property
    def atem_AtemModel10(self):
        return self.__atem_AtemModel10

    @atem_AtemModel10.setter
    def atem_AtemModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel10", None)
        self.__atem_AtemModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_AbstractComponent"):
                    opp_val = getattr(item, "atem_AbstractComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_AbstractComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_AbstractComponent"):
                    opp_val = getattr(item, "atem_AbstractComponent", None)
                    
                    setattr(item, "atem_AbstractComponent", self)
                    

    @property
    def atem_AtemModel2(self):
        return self.__atem_AtemModel2

    @atem_AtemModel2.setter
    def atem_AtemModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel2", None)
        self.__atem_AtemModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "atem_Import"):
                    opp_val = getattr(item, "atem_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "atem_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "atem_Import"):
                    opp_val = getattr(item, "atem_Import", None)
                    
                    setattr(item, "atem_Import", self)
                    

    @property
    def atem_AtemModel8(self):
        return self.__atem_AtemModel8

    @atem_AtemModel8.setter
    def atem_AtemModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel8", None)
        self.__atem_AtemModel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Preface"):
                opp_val = getattr(old_value, "atem_Preface", None)
                if opp_val == self:
                    setattr(old_value, "atem_Preface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Preface"):
                opp_val = getattr(value, "atem_Preface", None)
                setattr(value, "atem_Preface", self)

    @property
    def atem_AtemModel4(self):
        return self.__atem_AtemModel4

    @atem_AtemModel4.setter
    def atem_AtemModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel4", None)
        self.__atem_AtemModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Driver"):
                opp_val = getattr(old_value, "atem_Driver", None)
                if opp_val == self:
                    setattr(old_value, "atem_Driver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Driver"):
                opp_val = getattr(value, "atem_Driver", None)
                setattr(value, "atem_Driver", self)

    @property
    def atem_AtemModel(self):
        return self.__atem_AtemModel

    @atem_AtemModel.setter
    def atem_AtemModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel", None)
        self.__atem_AtemModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_TemplateStatus"):
                opp_val = getattr(old_value, "atem_TemplateStatus", None)
                if opp_val == self:
                    setattr(old_value, "atem_TemplateStatus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_TemplateStatus"):
                opp_val = getattr(value, "atem_TemplateStatus", None)
                setattr(value, "atem_TemplateStatus", self)

    @property
    def atem_AtemModel6(self):
        return self.__atem_AtemModel6

    @atem_AtemModel6.setter
    def atem_AtemModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atem_AtemModel__atem_AtemModel6", None)
        self.__atem_AtemModel6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atem_Head"):
                opp_val = getattr(old_value, "atem_Head", None)
                if opp_val == self:
                    setattr(old_value, "atem_Head", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atem_Head"):
                opp_val = getattr(value, "atem_Head", None)
                setattr(value, "atem_Head", self)

class atem_HeadComponent:

    pass
class atem_AbstractComponent:

    pass