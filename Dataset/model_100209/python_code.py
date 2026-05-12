from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CalendarTypeMember8(Enum):
    buddhist = "buddhist"
class FormatSourceType(Enum):
    fixed = "fixed"
    language = "language"
class CalendarTypeMember4(Enum):
    hanjaYoil = "hanjaYoil"
class TransliterationStyleType(Enum):
    short = "short"
    medium = "medium"
    long = "long"
class CalendarTypeMember7(Enum):
    jewish = "jewish"
class CalendarTypeMember2(Enum):
    gengou = "gengou"
class CalendarTypeMember6(Enum):
    hijri = "hijri"
class CalendarTypeMember3(Enum):
    ROC = "ROC"
class CalendarTypeMember1(Enum):
    gregorian = "gregorian"
class StyleType(Enum):
    short = "short"
    long = "long"
class CalendarTypeMember5(Enum):
    hanja = "hanja"


############################################
# Definition of Classes
############################################

class datastyle_EStringToStringMapEntry:

    pass
class datastyle_DocumentRoot:

    def __init__(self, mixed: str, text: str, calendar: str, automaticOrder: str, country: str, decimalPlaces: str, decimalReplacement: str, denominatorValue: str, displayFactor: str, formatSource: str, grouping: str, language: str, minDenominatorDigits: str, minExponentDigits: str, minIntegerDigits: str, minNumeratorDigits: str, transliterationFormat: str, position: str, possessiveForm: str, style: str, textual: str, title: str, transliterationCountry: str, transliterationLanguage: str, transliterationStyle: str, truncateOnOverflow: str, datastyle_DocumentRoot: set["datastyle_EStringToStringMapEntry"] = None, datastyle_DocumentRoot90: set["datastyle_EStringToStringMapEntry"] = None, datastyle_DocumentRoot93: set["datastyle_AmPmType"] = None, datastyle_DocumentRoot96: set["datastyle_BooleanType"] = None, datastyle_DocumentRoot99: set["datastyle_BooleanStyleType"] = None, datastyle_DocumentRoot102: set["datastyle_CurrencyStyleType"] = None, datastyle_DocumentRoot105: set["datastyle_CurrencySymbolType"] = None, datastyle_DocumentRoot108: set["datastyle_DateStyleType"] = None, datastyle_DocumentRoot111: set["datastyle_DayType"] = None, datastyle_DocumentRoot114: set["datastyle_DayOfWeekType"] = None, datastyle_DocumentRoot117: set["datastyle_EmbeddedTextType"] = None, datastyle_DocumentRoot120: set["datastyle_EraType"] = None, datastyle_DocumentRoot123: set["datastyle_FractionType"] = None, datastyle_DocumentRoot125: set["datastyle_HoursType"] = None, datastyle_DocumentRoot128: set["datastyle_MinutesType"] = None, datastyle_DocumentRoot131: set["datastyle_MonthType"] = None, datastyle_DocumentRoot134: set["datastyle_NumberType"] = None, datastyle_DocumentRoot137: set["datastyle_NumberStyleType"] = None, datastyle_DocumentRoot140: set["datastyle_PercentageStyleType"] = None, datastyle_DocumentRoot143: set["datastyle_QuarterType"] = None, datastyle_DocumentRoot146: set["datastyle_ScientificNumberType"] = None, datastyle_DocumentRoot148: set["datastyle_SecondsType"] = None, datastyle_DocumentRoot151: set["datastyle_TextContentType"] = None, datastyle_DocumentRoot154: set["datastyle_TextStyleType"] = None, datastyle_DocumentRoot157: set["datastyle_TimeStyleType"] = None, datastyle_DocumentRoot160: set["datastyle_WeekOfYearType"] = None, datastyle_DocumentRoot163: set["datastyle_YearType"] = None):
        self.mixed = mixed
        self.text = text
        self.calendar = calendar
        self.automaticOrder = automaticOrder
        self.country = country
        self.decimalPlaces = decimalPlaces
        self.decimalReplacement = decimalReplacement
        self.denominatorValue = denominatorValue
        self.displayFactor = displayFactor
        self.formatSource = formatSource
        self.grouping = grouping
        self.language = language
        self.minDenominatorDigits = minDenominatorDigits
        self.minExponentDigits = minExponentDigits
        self.minIntegerDigits = minIntegerDigits
        self.minNumeratorDigits = minNumeratorDigits
        self.transliterationFormat = transliterationFormat
        self.position = position
        self.possessiveForm = possessiveForm
        self.style = style
        self.textual = textual
        self.title = title
        self.transliterationCountry = transliterationCountry
        self.transliterationLanguage = transliterationLanguage
        self.transliterationStyle = transliterationStyle
        self.truncateOnOverflow = truncateOnOverflow
        self.datastyle_DocumentRoot = datastyle_DocumentRoot if datastyle_DocumentRoot is not None else set()
        self.datastyle_DocumentRoot90 = datastyle_DocumentRoot90 if datastyle_DocumentRoot90 is not None else set()
        self.datastyle_DocumentRoot93 = datastyle_DocumentRoot93 if datastyle_DocumentRoot93 is not None else set()
        self.datastyle_DocumentRoot96 = datastyle_DocumentRoot96 if datastyle_DocumentRoot96 is not None else set()
        self.datastyle_DocumentRoot99 = datastyle_DocumentRoot99 if datastyle_DocumentRoot99 is not None else set()
        self.datastyle_DocumentRoot102 = datastyle_DocumentRoot102 if datastyle_DocumentRoot102 is not None else set()
        self.datastyle_DocumentRoot105 = datastyle_DocumentRoot105 if datastyle_DocumentRoot105 is not None else set()
        self.datastyle_DocumentRoot108 = datastyle_DocumentRoot108 if datastyle_DocumentRoot108 is not None else set()
        self.datastyle_DocumentRoot111 = datastyle_DocumentRoot111 if datastyle_DocumentRoot111 is not None else set()
        self.datastyle_DocumentRoot114 = datastyle_DocumentRoot114 if datastyle_DocumentRoot114 is not None else set()
        self.datastyle_DocumentRoot117 = datastyle_DocumentRoot117 if datastyle_DocumentRoot117 is not None else set()
        self.datastyle_DocumentRoot120 = datastyle_DocumentRoot120 if datastyle_DocumentRoot120 is not None else set()
        self.datastyle_DocumentRoot123 = datastyle_DocumentRoot123 if datastyle_DocumentRoot123 is not None else set()
        self.datastyle_DocumentRoot125 = datastyle_DocumentRoot125 if datastyle_DocumentRoot125 is not None else set()
        self.datastyle_DocumentRoot128 = datastyle_DocumentRoot128 if datastyle_DocumentRoot128 is not None else set()
        self.datastyle_DocumentRoot131 = datastyle_DocumentRoot131 if datastyle_DocumentRoot131 is not None else set()
        self.datastyle_DocumentRoot134 = datastyle_DocumentRoot134 if datastyle_DocumentRoot134 is not None else set()
        self.datastyle_DocumentRoot137 = datastyle_DocumentRoot137 if datastyle_DocumentRoot137 is not None else set()
        self.datastyle_DocumentRoot140 = datastyle_DocumentRoot140 if datastyle_DocumentRoot140 is not None else set()
        self.datastyle_DocumentRoot143 = datastyle_DocumentRoot143 if datastyle_DocumentRoot143 is not None else set()
        self.datastyle_DocumentRoot146 = datastyle_DocumentRoot146 if datastyle_DocumentRoot146 is not None else set()
        self.datastyle_DocumentRoot148 = datastyle_DocumentRoot148 if datastyle_DocumentRoot148 is not None else set()
        self.datastyle_DocumentRoot151 = datastyle_DocumentRoot151 if datastyle_DocumentRoot151 is not None else set()
        self.datastyle_DocumentRoot154 = datastyle_DocumentRoot154 if datastyle_DocumentRoot154 is not None else set()
        self.datastyle_DocumentRoot157 = datastyle_DocumentRoot157 if datastyle_DocumentRoot157 is not None else set()
        self.datastyle_DocumentRoot160 = datastyle_DocumentRoot160 if datastyle_DocumentRoot160 is not None else set()
        self.datastyle_DocumentRoot163 = datastyle_DocumentRoot163 if datastyle_DocumentRoot163 is not None else set()
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def minIntegerDigits(self):
        return self.__minIntegerDigits

    @minIntegerDigits.setter
    def minIntegerDigits(self, minIntegerDigits: str):
        self.__minIntegerDigits = minIntegerDigits


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def minNumeratorDigits(self):
        return self.__minNumeratorDigits

    @minNumeratorDigits.setter
    def minNumeratorDigits(self, minNumeratorDigits: str):
        self.__minNumeratorDigits = minNumeratorDigits


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def textual(self):
        return self.__textual

    @textual.setter
    def textual(self, textual: str):
        self.__textual = textual


    @property
    def minExponentDigits(self):
        return self.__minExponentDigits

    @minExponentDigits.setter
    def minExponentDigits(self, minExponentDigits: str):
        self.__minExponentDigits = minExponentDigits


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def minDenominatorDigits(self):
        return self.__minDenominatorDigits

    @minDenominatorDigits.setter
    def minDenominatorDigits(self, minDenominatorDigits: str):
        self.__minDenominatorDigits = minDenominatorDigits


    @property
    def automaticOrder(self):
        return self.__automaticOrder

    @automaticOrder.setter
    def automaticOrder(self, automaticOrder: str):
        self.__automaticOrder = automaticOrder


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def decimalReplacement(self):
        return self.__decimalReplacement

    @decimalReplacement.setter
    def decimalReplacement(self, decimalReplacement: str):
        self.__decimalReplacement = decimalReplacement


    @property
    def formatSource(self):
        return self.__formatSource

    @formatSource.setter
    def formatSource(self, formatSource: str):
        self.__formatSource = formatSource


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def grouping(self):
        return self.__grouping

    @grouping.setter
    def grouping(self, grouping: str):
        self.__grouping = grouping


    @property
    def displayFactor(self):
        return self.__displayFactor

    @displayFactor.setter
    def displayFactor(self, displayFactor: str):
        self.__displayFactor = displayFactor


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def decimalPlaces(self):
        return self.__decimalPlaces

    @decimalPlaces.setter
    def decimalPlaces(self, decimalPlaces: str):
        self.__decimalPlaces = decimalPlaces


    @property
    def possessiveForm(self):
        return self.__possessiveForm

    @possessiveForm.setter
    def possessiveForm(self, possessiveForm: str):
        self.__possessiveForm = possessiveForm


    @property
    def denominatorValue(self):
        return self.__denominatorValue

    @denominatorValue.setter
    def denominatorValue(self, denominatorValue: str):
        self.__denominatorValue = denominatorValue


    @property
    def truncateOnOverflow(self):
        return self.__truncateOnOverflow

    @truncateOnOverflow.setter
    def truncateOnOverflow(self, truncateOnOverflow: str):
        self.__truncateOnOverflow = truncateOnOverflow


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def datastyle_DocumentRoot117(self):
        return self.__datastyle_DocumentRoot117

    @datastyle_DocumentRoot117.setter
    def datastyle_DocumentRoot117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot117", None)
        self.__datastyle_DocumentRoot117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EmbeddedTextType118"):
                    opp_val = getattr(item, "datastyle_EmbeddedTextType118", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EmbeddedTextType118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EmbeddedTextType118"):
                    opp_val = getattr(item, "datastyle_EmbeddedTextType118", None)
                    
                    setattr(item, "datastyle_EmbeddedTextType118", self)
                    

    @property
    def datastyle_DocumentRoot125(self):
        return self.__datastyle_DocumentRoot125

    @datastyle_DocumentRoot125.setter
    def datastyle_DocumentRoot125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot125", None)
        self.__datastyle_DocumentRoot125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_HoursType126"):
                    opp_val = getattr(item, "datastyle_HoursType126", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_HoursType126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_HoursType126"):
                    opp_val = getattr(item, "datastyle_HoursType126", None)
                    
                    setattr(item, "datastyle_HoursType126", self)
                    

    @property
    def datastyle_DocumentRoot143(self):
        return self.__datastyle_DocumentRoot143

    @datastyle_DocumentRoot143.setter
    def datastyle_DocumentRoot143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot143", None)
        self.__datastyle_DocumentRoot143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_QuarterType144"):
                    opp_val = getattr(item, "datastyle_QuarterType144", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_QuarterType144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_QuarterType144"):
                    opp_val = getattr(item, "datastyle_QuarterType144", None)
                    
                    setattr(item, "datastyle_QuarterType144", self)
                    

    @property
    def datastyle_DocumentRoot157(self):
        return self.__datastyle_DocumentRoot157

    @datastyle_DocumentRoot157.setter
    def datastyle_DocumentRoot157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot157", None)
        self.__datastyle_DocumentRoot157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_TimeStyleType158"):
                    opp_val = getattr(item, "datastyle_TimeStyleType158", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_TimeStyleType158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_TimeStyleType158"):
                    opp_val = getattr(item, "datastyle_TimeStyleType158", None)
                    
                    setattr(item, "datastyle_TimeStyleType158", self)
                    

    @property
    def datastyle_DocumentRoot120(self):
        return self.__datastyle_DocumentRoot120

    @datastyle_DocumentRoot120.setter
    def datastyle_DocumentRoot120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot120", None)
        self.__datastyle_DocumentRoot120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EraType121"):
                    opp_val = getattr(item, "datastyle_EraType121", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EraType121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EraType121"):
                    opp_val = getattr(item, "datastyle_EraType121", None)
                    
                    setattr(item, "datastyle_EraType121", self)
                    

    @property
    def datastyle_DocumentRoot137(self):
        return self.__datastyle_DocumentRoot137

    @datastyle_DocumentRoot137.setter
    def datastyle_DocumentRoot137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot137", None)
        self.__datastyle_DocumentRoot137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_NumberStyleType138"):
                    opp_val = getattr(item, "datastyle_NumberStyleType138", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_NumberStyleType138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_NumberStyleType138"):
                    opp_val = getattr(item, "datastyle_NumberStyleType138", None)
                    
                    setattr(item, "datastyle_NumberStyleType138", self)
                    

    @property
    def datastyle_DocumentRoot146(self):
        return self.__datastyle_DocumentRoot146

    @datastyle_DocumentRoot146.setter
    def datastyle_DocumentRoot146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot146", None)
        self.__datastyle_DocumentRoot146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_ScientificNumberType"):
                    opp_val = getattr(item, "datastyle_ScientificNumberType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_ScientificNumberType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_ScientificNumberType"):
                    opp_val = getattr(item, "datastyle_ScientificNumberType", None)
                    
                    setattr(item, "datastyle_ScientificNumberType", self)
                    

    @property
    def datastyle_DocumentRoot108(self):
        return self.__datastyle_DocumentRoot108

    @datastyle_DocumentRoot108.setter
    def datastyle_DocumentRoot108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot108", None)
        self.__datastyle_DocumentRoot108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_DateStyleType109"):
                    opp_val = getattr(item, "datastyle_DateStyleType109", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_DateStyleType109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_DateStyleType109"):
                    opp_val = getattr(item, "datastyle_DateStyleType109", None)
                    
                    setattr(item, "datastyle_DateStyleType109", self)
                    

    @property
    def datastyle_DocumentRoot90(self):
        return self.__datastyle_DocumentRoot90

    @datastyle_DocumentRoot90.setter
    def datastyle_DocumentRoot90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot90", None)
        self.__datastyle_DocumentRoot90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EStringToStringMapEntry91"):
                    opp_val = getattr(item, "datastyle_EStringToStringMapEntry91", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EStringToStringMapEntry91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EStringToStringMapEntry91"):
                    opp_val = getattr(item, "datastyle_EStringToStringMapEntry91", None)
                    
                    setattr(item, "datastyle_EStringToStringMapEntry91", self)
                    

    @property
    def datastyle_DocumentRoot(self):
        return self.__datastyle_DocumentRoot

    @datastyle_DocumentRoot.setter
    def datastyle_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot", None)
        self.__datastyle_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EStringToStringMapEntry"):
                    opp_val = getattr(item, "datastyle_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EStringToStringMapEntry"):
                    opp_val = getattr(item, "datastyle_EStringToStringMapEntry", None)
                    
                    setattr(item, "datastyle_EStringToStringMapEntry", self)
                    

    @property
    def datastyle_DocumentRoot123(self):
        return self.__datastyle_DocumentRoot123

    @datastyle_DocumentRoot123.setter
    def datastyle_DocumentRoot123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot123", None)
        self.__datastyle_DocumentRoot123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_FractionType"):
                    opp_val = getattr(item, "datastyle_FractionType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_FractionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_FractionType"):
                    opp_val = getattr(item, "datastyle_FractionType", None)
                    
                    setattr(item, "datastyle_FractionType", self)
                    

    @property
    def datastyle_DocumentRoot131(self):
        return self.__datastyle_DocumentRoot131

    @datastyle_DocumentRoot131.setter
    def datastyle_DocumentRoot131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot131", None)
        self.__datastyle_DocumentRoot131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MonthType132"):
                    opp_val = getattr(item, "datastyle_MonthType132", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MonthType132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MonthType132"):
                    opp_val = getattr(item, "datastyle_MonthType132", None)
                    
                    setattr(item, "datastyle_MonthType132", self)
                    

    @property
    def datastyle_DocumentRoot160(self):
        return self.__datastyle_DocumentRoot160

    @datastyle_DocumentRoot160.setter
    def datastyle_DocumentRoot160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot160", None)
        self.__datastyle_DocumentRoot160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_WeekOfYearType161"):
                    opp_val = getattr(item, "datastyle_WeekOfYearType161", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_WeekOfYearType161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_WeekOfYearType161"):
                    opp_val = getattr(item, "datastyle_WeekOfYearType161", None)
                    
                    setattr(item, "datastyle_WeekOfYearType161", self)
                    

    @property
    def datastyle_DocumentRoot154(self):
        return self.__datastyle_DocumentRoot154

    @datastyle_DocumentRoot154.setter
    def datastyle_DocumentRoot154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot154", None)
        self.__datastyle_DocumentRoot154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_TextStyleType155"):
                    opp_val = getattr(item, "datastyle_TextStyleType155", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_TextStyleType155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_TextStyleType155"):
                    opp_val = getattr(item, "datastyle_TextStyleType155", None)
                    
                    setattr(item, "datastyle_TextStyleType155", self)
                    

    @property
    def datastyle_DocumentRoot114(self):
        return self.__datastyle_DocumentRoot114

    @datastyle_DocumentRoot114.setter
    def datastyle_DocumentRoot114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot114", None)
        self.__datastyle_DocumentRoot114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_DayOfWeekType115"):
                    opp_val = getattr(item, "datastyle_DayOfWeekType115", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_DayOfWeekType115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_DayOfWeekType115"):
                    opp_val = getattr(item, "datastyle_DayOfWeekType115", None)
                    
                    setattr(item, "datastyle_DayOfWeekType115", self)
                    

    @property
    def datastyle_DocumentRoot134(self):
        return self.__datastyle_DocumentRoot134

    @datastyle_DocumentRoot134.setter
    def datastyle_DocumentRoot134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot134", None)
        self.__datastyle_DocumentRoot134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_NumberType135"):
                    opp_val = getattr(item, "datastyle_NumberType135", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_NumberType135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_NumberType135"):
                    opp_val = getattr(item, "datastyle_NumberType135", None)
                    
                    setattr(item, "datastyle_NumberType135", self)
                    

    @property
    def datastyle_DocumentRoot102(self):
        return self.__datastyle_DocumentRoot102

    @datastyle_DocumentRoot102.setter
    def datastyle_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot102", None)
        self.__datastyle_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_CurrencyStyleType103"):
                    opp_val = getattr(item, "datastyle_CurrencyStyleType103", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_CurrencyStyleType103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_CurrencyStyleType103"):
                    opp_val = getattr(item, "datastyle_CurrencyStyleType103", None)
                    
                    setattr(item, "datastyle_CurrencyStyleType103", self)
                    

    @property
    def datastyle_DocumentRoot140(self):
        return self.__datastyle_DocumentRoot140

    @datastyle_DocumentRoot140.setter
    def datastyle_DocumentRoot140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot140", None)
        self.__datastyle_DocumentRoot140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_PercentageStyleType141"):
                    opp_val = getattr(item, "datastyle_PercentageStyleType141", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_PercentageStyleType141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_PercentageStyleType141"):
                    opp_val = getattr(item, "datastyle_PercentageStyleType141", None)
                    
                    setattr(item, "datastyle_PercentageStyleType141", self)
                    

    @property
    def datastyle_DocumentRoot163(self):
        return self.__datastyle_DocumentRoot163

    @datastyle_DocumentRoot163.setter
    def datastyle_DocumentRoot163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot163", None)
        self.__datastyle_DocumentRoot163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_YearType164"):
                    opp_val = getattr(item, "datastyle_YearType164", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_YearType164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_YearType164"):
                    opp_val = getattr(item, "datastyle_YearType164", None)
                    
                    setattr(item, "datastyle_YearType164", self)
                    

    @property
    def datastyle_DocumentRoot96(self):
        return self.__datastyle_DocumentRoot96

    @datastyle_DocumentRoot96.setter
    def datastyle_DocumentRoot96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot96", None)
        self.__datastyle_DocumentRoot96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_BooleanType97"):
                    opp_val = getattr(item, "datastyle_BooleanType97", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_BooleanType97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_BooleanType97"):
                    opp_val = getattr(item, "datastyle_BooleanType97", None)
                    
                    setattr(item, "datastyle_BooleanType97", self)
                    

    @property
    def datastyle_DocumentRoot128(self):
        return self.__datastyle_DocumentRoot128

    @datastyle_DocumentRoot128.setter
    def datastyle_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot128", None)
        self.__datastyle_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MinutesType129"):
                    opp_val = getattr(item, "datastyle_MinutesType129", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MinutesType129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MinutesType129"):
                    opp_val = getattr(item, "datastyle_MinutesType129", None)
                    
                    setattr(item, "datastyle_MinutesType129", self)
                    

    @property
    def datastyle_DocumentRoot151(self):
        return self.__datastyle_DocumentRoot151

    @datastyle_DocumentRoot151.setter
    def datastyle_DocumentRoot151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot151", None)
        self.__datastyle_DocumentRoot151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_TextContentType152"):
                    opp_val = getattr(item, "datastyle_TextContentType152", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_TextContentType152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_TextContentType152"):
                    opp_val = getattr(item, "datastyle_TextContentType152", None)
                    
                    setattr(item, "datastyle_TextContentType152", self)
                    

    @property
    def datastyle_DocumentRoot93(self):
        return self.__datastyle_DocumentRoot93

    @datastyle_DocumentRoot93.setter
    def datastyle_DocumentRoot93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot93", None)
        self.__datastyle_DocumentRoot93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_AmPmType94"):
                    opp_val = getattr(item, "datastyle_AmPmType94", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_AmPmType94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_AmPmType94"):
                    opp_val = getattr(item, "datastyle_AmPmType94", None)
                    
                    setattr(item, "datastyle_AmPmType94", self)
                    

    @property
    def datastyle_DocumentRoot99(self):
        return self.__datastyle_DocumentRoot99

    @datastyle_DocumentRoot99.setter
    def datastyle_DocumentRoot99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot99", None)
        self.__datastyle_DocumentRoot99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_BooleanStyleType100"):
                    opp_val = getattr(item, "datastyle_BooleanStyleType100", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_BooleanStyleType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_BooleanStyleType100"):
                    opp_val = getattr(item, "datastyle_BooleanStyleType100", None)
                    
                    setattr(item, "datastyle_BooleanStyleType100", self)
                    

    @property
    def datastyle_DocumentRoot105(self):
        return self.__datastyle_DocumentRoot105

    @datastyle_DocumentRoot105.setter
    def datastyle_DocumentRoot105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot105", None)
        self.__datastyle_DocumentRoot105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_CurrencySymbolType106"):
                    opp_val = getattr(item, "datastyle_CurrencySymbolType106", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_CurrencySymbolType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_CurrencySymbolType106"):
                    opp_val = getattr(item, "datastyle_CurrencySymbolType106", None)
                    
                    setattr(item, "datastyle_CurrencySymbolType106", self)
                    

    @property
    def datastyle_DocumentRoot148(self):
        return self.__datastyle_DocumentRoot148

    @datastyle_DocumentRoot148.setter
    def datastyle_DocumentRoot148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot148", None)
        self.__datastyle_DocumentRoot148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_SecondsType149"):
                    opp_val = getattr(item, "datastyle_SecondsType149", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_SecondsType149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_SecondsType149"):
                    opp_val = getattr(item, "datastyle_SecondsType149", None)
                    
                    setattr(item, "datastyle_SecondsType149", self)
                    

    @property
    def datastyle_DocumentRoot111(self):
        return self.__datastyle_DocumentRoot111

    @datastyle_DocumentRoot111.setter
    def datastyle_DocumentRoot111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DocumentRoot__datastyle_DocumentRoot111", None)
        self.__datastyle_DocumentRoot111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_DayType112"):
                    opp_val = getattr(item, "datastyle_DayType112", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_DayType112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_DayType112"):
                    opp_val = getattr(item, "datastyle_DayType112", None)
                    
                    setattr(item, "datastyle_DayType112", self)
                    

class datastyle_TimeStyleType:

    def __init__(self, group: str, text: str, country: str, text1: str, title: str, transliterationCountry: str, formatSource: str, language: str, name: str, transliterationStyle: str, truncateOnOverflow: str, volatile: str, transliterationFormat: str, transliterationLanguage: str, datastyle_TimeStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_TimeStyleType77: set["datastyle_AmPmType"] = None, datastyle_TimeStyleType80: set["datastyle_MinutesType"] = None, datastyle_TimeStyleType74: set["datastyle_HoursType"] = None, datastyle_TimeStyleType86: set["datastyle_MapType"] = None, datastyle_TimeStyleType83: set["datastyle_SecondsType"] = None, datastyle_TimeStyleType158: "datastyle_DocumentRoot" = None):
        self.group = group
        self.text = text
        self.country = country
        self.text1 = text1
        self.title = title
        self.transliterationCountry = transliterationCountry
        self.formatSource = formatSource
        self.language = language
        self.name = name
        self.transliterationStyle = transliterationStyle
        self.truncateOnOverflow = truncateOnOverflow
        self.volatile = volatile
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.datastyle_TimeStyleType = datastyle_TimeStyleType
        self.datastyle_TimeStyleType77 = datastyle_TimeStyleType77 if datastyle_TimeStyleType77 is not None else set()
        self.datastyle_TimeStyleType80 = datastyle_TimeStyleType80 if datastyle_TimeStyleType80 is not None else set()
        self.datastyle_TimeStyleType74 = datastyle_TimeStyleType74 if datastyle_TimeStyleType74 is not None else set()
        self.datastyle_TimeStyleType86 = datastyle_TimeStyleType86 if datastyle_TimeStyleType86 is not None else set()
        self.datastyle_TimeStyleType83 = datastyle_TimeStyleType83 if datastyle_TimeStyleType83 is not None else set()
        self.datastyle_TimeStyleType158 = datastyle_TimeStyleType158
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def formatSource(self):
        return self.__formatSource

    @formatSource.setter
    def formatSource(self, formatSource: str):
        self.__formatSource = formatSource


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def truncateOnOverflow(self):
        return self.__truncateOnOverflow

    @truncateOnOverflow.setter
    def truncateOnOverflow(self, truncateOnOverflow: str):
        self.__truncateOnOverflow = truncateOnOverflow


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def datastyle_TimeStyleType74(self):
        return self.__datastyle_TimeStyleType74

    @datastyle_TimeStyleType74.setter
    def datastyle_TimeStyleType74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType74", None)
        self.__datastyle_TimeStyleType74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_HoursType75"):
                    opp_val = getattr(item, "datastyle_HoursType75", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_HoursType75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_HoursType75"):
                    opp_val = getattr(item, "datastyle_HoursType75", None)
                    
                    setattr(item, "datastyle_HoursType75", self)
                    

    @property
    def datastyle_TimeStyleType83(self):
        return self.__datastyle_TimeStyleType83

    @datastyle_TimeStyleType83.setter
    def datastyle_TimeStyleType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType83", None)
        self.__datastyle_TimeStyleType83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_SecondsType84"):
                    opp_val = getattr(item, "datastyle_SecondsType84", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_SecondsType84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_SecondsType84"):
                    opp_val = getattr(item, "datastyle_SecondsType84", None)
                    
                    setattr(item, "datastyle_SecondsType84", self)
                    

    @property
    def datastyle_TimeStyleType77(self):
        return self.__datastyle_TimeStyleType77

    @datastyle_TimeStyleType77.setter
    def datastyle_TimeStyleType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType77", None)
        self.__datastyle_TimeStyleType77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_AmPmType78"):
                    opp_val = getattr(item, "datastyle_AmPmType78", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_AmPmType78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_AmPmType78"):
                    opp_val = getattr(item, "datastyle_AmPmType78", None)
                    
                    setattr(item, "datastyle_AmPmType78", self)
                    

    @property
    def datastyle_TimeStyleType158(self):
        return self.__datastyle_TimeStyleType158

    @datastyle_TimeStyleType158.setter
    def datastyle_TimeStyleType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType158", None)
        self.__datastyle_TimeStyleType158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot157"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot157"):
                opp_val = getattr(value, "datastyle_DocumentRoot157", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_TimeStyleType80(self):
        return self.__datastyle_TimeStyleType80

    @datastyle_TimeStyleType80.setter
    def datastyle_TimeStyleType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType80", None)
        self.__datastyle_TimeStyleType80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MinutesType81"):
                    opp_val = getattr(item, "datastyle_MinutesType81", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MinutesType81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MinutesType81"):
                    opp_val = getattr(item, "datastyle_MinutesType81", None)
                    
                    setattr(item, "datastyle_MinutesType81", self)
                    

    @property
    def datastyle_TimeStyleType(self):
        return self.__datastyle_TimeStyleType

    @datastyle_TimeStyleType.setter
    def datastyle_TimeStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType", None)
        self.__datastyle_TimeStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent72"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent72", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent72"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent72", None)
                setattr(value, "datastyle_StyleTextPropertiesContent72", self)

    @property
    def datastyle_TimeStyleType86(self):
        return self.__datastyle_TimeStyleType86

    @datastyle_TimeStyleType86.setter
    def datastyle_TimeStyleType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TimeStyleType__datastyle_TimeStyleType86", None)
        self.__datastyle_TimeStyleType86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType87"):
                    opp_val = getattr(item, "datastyle_MapType87", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType87"):
                    opp_val = getattr(item, "datastyle_MapType87", None)
                    
                    setattr(item, "datastyle_MapType87", self)
                    

class datastyle_TextStyleType:

    def __init__(self, group: str, text1: str, text: str, language: str, name: str, title: str, country: str, transliterationStyle: str, volatile: str, transliterationCountry: str, transliterationFormat: str, transliterationLanguage: str, datastyle_TextStyleType67: set["datastyle_TextContentType"] = None, datastyle_TextStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_TextStyleType69: set["datastyle_MapType"] = None, datastyle_TextStyleType155: "datastyle_DocumentRoot" = None):
        self.group = group
        self.text1 = text1
        self.text = text
        self.language = language
        self.name = name
        self.title = title
        self.country = country
        self.transliterationStyle = transliterationStyle
        self.volatile = volatile
        self.transliterationCountry = transliterationCountry
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.datastyle_TextStyleType67 = datastyle_TextStyleType67 if datastyle_TextStyleType67 is not None else set()
        self.datastyle_TextStyleType = datastyle_TextStyleType
        self.datastyle_TextStyleType69 = datastyle_TextStyleType69 if datastyle_TextStyleType69 is not None else set()
        self.datastyle_TextStyleType155 = datastyle_TextStyleType155
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def datastyle_TextStyleType155(self):
        return self.__datastyle_TextStyleType155

    @datastyle_TextStyleType155.setter
    def datastyle_TextStyleType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TextStyleType__datastyle_TextStyleType155", None)
        self.__datastyle_TextStyleType155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot154"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot154"):
                opp_val = getattr(value, "datastyle_DocumentRoot154", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_TextStyleType69(self):
        return self.__datastyle_TextStyleType69

    @datastyle_TextStyleType69.setter
    def datastyle_TextStyleType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TextStyleType__datastyle_TextStyleType69", None)
        self.__datastyle_TextStyleType69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType70"):
                    opp_val = getattr(item, "datastyle_MapType70", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType70"):
                    opp_val = getattr(item, "datastyle_MapType70", None)
                    
                    setattr(item, "datastyle_MapType70", self)
                    

    @property
    def datastyle_TextStyleType67(self):
        return self.__datastyle_TextStyleType67

    @datastyle_TextStyleType67.setter
    def datastyle_TextStyleType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TextStyleType__datastyle_TextStyleType67", None)
        self.__datastyle_TextStyleType67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_TextContentType"):
                    opp_val = getattr(item, "datastyle_TextContentType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_TextContentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_TextContentType"):
                    opp_val = getattr(item, "datastyle_TextContentType", None)
                    
                    setattr(item, "datastyle_TextContentType", self)
                    

    @property
    def datastyle_TextStyleType(self):
        return self.__datastyle_TextStyleType

    @datastyle_TextStyleType.setter
    def datastyle_TextStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_TextStyleType__datastyle_TextStyleType", None)
        self.__datastyle_TextStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent65"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent65", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent65"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent65", None)
                setattr(value, "datastyle_StyleTextPropertiesContent65", self)

class datastyle_TextContentType:

    pass
class datastyle_ScientificNumberType:

    def __init__(self, grouping: str, minExponentDigits: str, minIntegerDigits: str, decimalPlaces: str, datastyle_ScientificNumberType: "datastyle_DocumentRoot" = None):
        self.grouping = grouping
        self.minExponentDigits = minExponentDigits
        self.minIntegerDigits = minIntegerDigits
        self.decimalPlaces = decimalPlaces
        self.datastyle_ScientificNumberType = datastyle_ScientificNumberType
        
        pass
    @property
    def decimalPlaces(self):
        return self.__decimalPlaces

    @decimalPlaces.setter
    def decimalPlaces(self, decimalPlaces: str):
        self.__decimalPlaces = decimalPlaces


    @property
    def grouping(self):
        return self.__grouping

    @grouping.setter
    def grouping(self, grouping: str):
        self.__grouping = grouping


    @property
    def minIntegerDigits(self):
        return self.__minIntegerDigits

    @minIntegerDigits.setter
    def minIntegerDigits(self, minIntegerDigits: str):
        self.__minIntegerDigits = minIntegerDigits


    @property
    def minExponentDigits(self):
        return self.__minExponentDigits

    @minExponentDigits.setter
    def minExponentDigits(self, minExponentDigits: str):
        self.__minExponentDigits = minExponentDigits


    @property
    def datastyle_ScientificNumberType(self):
        return self.__datastyle_ScientificNumberType

    @datastyle_ScientificNumberType.setter
    def datastyle_ScientificNumberType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_ScientificNumberType__datastyle_ScientificNumberType", None)
        self.__datastyle_ScientificNumberType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot146"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot146"):
                opp_val = getattr(value, "datastyle_DocumentRoot146", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_PercentageStyleType:

    def __init__(self, text: str, text1: str, language: str, name: str, title: str, country: str, transliterationStyle: str, volatile: str, transliterationCountry: str, transliterationFormat: str, transliterationLanguage: str, datastyle_PercentageStyleType59: "datastyle_NumberType" = None, datastyle_PercentageStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_PercentageStyleType62: set["datastyle_MapType"] = None, datastyle_PercentageStyleType141: "datastyle_DocumentRoot" = None):
        self.text = text
        self.text1 = text1
        self.language = language
        self.name = name
        self.title = title
        self.country = country
        self.transliterationStyle = transliterationStyle
        self.volatile = volatile
        self.transliterationCountry = transliterationCountry
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.datastyle_PercentageStyleType59 = datastyle_PercentageStyleType59
        self.datastyle_PercentageStyleType = datastyle_PercentageStyleType
        self.datastyle_PercentageStyleType62 = datastyle_PercentageStyleType62 if datastyle_PercentageStyleType62 is not None else set()
        self.datastyle_PercentageStyleType141 = datastyle_PercentageStyleType141
        
        pass
    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def datastyle_PercentageStyleType62(self):
        return self.__datastyle_PercentageStyleType62

    @datastyle_PercentageStyleType62.setter
    def datastyle_PercentageStyleType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_PercentageStyleType__datastyle_PercentageStyleType62", None)
        self.__datastyle_PercentageStyleType62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType63"):
                    opp_val = getattr(item, "datastyle_MapType63", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType63"):
                    opp_val = getattr(item, "datastyle_MapType63", None)
                    
                    setattr(item, "datastyle_MapType63", self)
                    

    @property
    def datastyle_PercentageStyleType59(self):
        return self.__datastyle_PercentageStyleType59

    @datastyle_PercentageStyleType59.setter
    def datastyle_PercentageStyleType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_PercentageStyleType__datastyle_PercentageStyleType59", None)
        self.__datastyle_PercentageStyleType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_NumberType60"):
                opp_val = getattr(old_value, "datastyle_NumberType60", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_NumberType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_NumberType60"):
                opp_val = getattr(value, "datastyle_NumberType60", None)
                setattr(value, "datastyle_NumberType60", self)

    @property
    def datastyle_PercentageStyleType141(self):
        return self.__datastyle_PercentageStyleType141

    @datastyle_PercentageStyleType141.setter
    def datastyle_PercentageStyleType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_PercentageStyleType__datastyle_PercentageStyleType141", None)
        self.__datastyle_PercentageStyleType141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot140"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot140"):
                opp_val = getattr(value, "datastyle_DocumentRoot140", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_PercentageStyleType(self):
        return self.__datastyle_PercentageStyleType

    @datastyle_PercentageStyleType.setter
    def datastyle_PercentageStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_PercentageStyleType__datastyle_PercentageStyleType", None)
        self.__datastyle_PercentageStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent57"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent57", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent57"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent57", None)
                setattr(value, "datastyle_StyleTextPropertiesContent57", self)

class datastyle_EObject:

    pass
class datastyle_NumberStyleType:

    def __init__(self, anyNumberGroup: str, text1: str, text: str, language: str, name: str, title: str, country: str, transliterationStyle: str, volatile: str, transliterationCountry: str, transliterationFormat: str, transliterationLanguage: str, datastyle_NumberStyleType50: "datastyle_EObject" = None, datastyle_NumberStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_NumberStyleType52: set["datastyle_MapType"] = None, datastyle_NumberStyleType138: "datastyle_DocumentRoot" = None):
        self.anyNumberGroup = anyNumberGroup
        self.text1 = text1
        self.text = text
        self.language = language
        self.name = name
        self.title = title
        self.country = country
        self.transliterationStyle = transliterationStyle
        self.volatile = volatile
        self.transliterationCountry = transliterationCountry
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.datastyle_NumberStyleType50 = datastyle_NumberStyleType50
        self.datastyle_NumberStyleType = datastyle_NumberStyleType
        self.datastyle_NumberStyleType52 = datastyle_NumberStyleType52 if datastyle_NumberStyleType52 is not None else set()
        self.datastyle_NumberStyleType138 = datastyle_NumberStyleType138
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def anyNumberGroup(self):
        return self.__anyNumberGroup

    @anyNumberGroup.setter
    def anyNumberGroup(self, anyNumberGroup: str):
        self.__anyNumberGroup = anyNumberGroup


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def datastyle_NumberStyleType52(self):
        return self.__datastyle_NumberStyleType52

    @datastyle_NumberStyleType52.setter
    def datastyle_NumberStyleType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberStyleType__datastyle_NumberStyleType52", None)
        self.__datastyle_NumberStyleType52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType53"):
                    opp_val = getattr(item, "datastyle_MapType53", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType53"):
                    opp_val = getattr(item, "datastyle_MapType53", None)
                    
                    setattr(item, "datastyle_MapType53", self)
                    

    @property
    def datastyle_NumberStyleType50(self):
        return self.__datastyle_NumberStyleType50

    @datastyle_NumberStyleType50.setter
    def datastyle_NumberStyleType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberStyleType__datastyle_NumberStyleType50", None)
        self.__datastyle_NumberStyleType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_EObject"):
                opp_val = getattr(old_value, "datastyle_EObject", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_EObject"):
                opp_val = getattr(value, "datastyle_EObject", None)
                setattr(value, "datastyle_EObject", self)

    @property
    def datastyle_NumberStyleType138(self):
        return self.__datastyle_NumberStyleType138

    @datastyle_NumberStyleType138.setter
    def datastyle_NumberStyleType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberStyleType__datastyle_NumberStyleType138", None)
        self.__datastyle_NumberStyleType138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot137"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot137"):
                opp_val = getattr(value, "datastyle_DocumentRoot137", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_NumberStyleType(self):
        return self.__datastyle_NumberStyleType

    @datastyle_NumberStyleType.setter
    def datastyle_NumberStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberStyleType__datastyle_NumberStyleType", None)
        self.__datastyle_NumberStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent48"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent48", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent48"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent48", None)
                setattr(value, "datastyle_StyleTextPropertiesContent48", self)

class datastyle_FractionType:

    def __init__(self, denominatorValue: str, grouping: str, minDenominatorDigits: str, minIntegerDigits: str, minNumeratorDigits: str, datastyle_FractionType: "datastyle_DocumentRoot" = None):
        self.denominatorValue = denominatorValue
        self.grouping = grouping
        self.minDenominatorDigits = minDenominatorDigits
        self.minIntegerDigits = minIntegerDigits
        self.minNumeratorDigits = minNumeratorDigits
        self.datastyle_FractionType = datastyle_FractionType
        
        pass
    @property
    def denominatorValue(self):
        return self.__denominatorValue

    @denominatorValue.setter
    def denominatorValue(self, denominatorValue: str):
        self.__denominatorValue = denominatorValue


    @property
    def grouping(self):
        return self.__grouping

    @grouping.setter
    def grouping(self, grouping: str):
        self.__grouping = grouping


    @property
    def minDenominatorDigits(self):
        return self.__minDenominatorDigits

    @minDenominatorDigits.setter
    def minDenominatorDigits(self, minDenominatorDigits: str):
        self.__minDenominatorDigits = minDenominatorDigits


    @property
    def minNumeratorDigits(self):
        return self.__minNumeratorDigits

    @minNumeratorDigits.setter
    def minNumeratorDigits(self, minNumeratorDigits: str):
        self.__minNumeratorDigits = minNumeratorDigits


    @property
    def minIntegerDigits(self):
        return self.__minIntegerDigits

    @minIntegerDigits.setter
    def minIntegerDigits(self, minIntegerDigits: str):
        self.__minIntegerDigits = minIntegerDigits


    @property
    def datastyle_FractionType(self):
        return self.__datastyle_FractionType

    @datastyle_FractionType.setter
    def datastyle_FractionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_FractionType__datastyle_FractionType", None)
        self.__datastyle_FractionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot123"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot123"):
                opp_val = getattr(value, "datastyle_DocumentRoot123", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_EmbeddedTextType:

    def __init__(self, mixed: str, position: str, datastyle_EmbeddedTextType118: "datastyle_DocumentRoot" = None, datastyle_EmbeddedTextType: "datastyle_NumberType" = None):
        self.mixed = mixed
        self.position = position
        self.datastyle_EmbeddedTextType118 = datastyle_EmbeddedTextType118
        self.datastyle_EmbeddedTextType = datastyle_EmbeddedTextType
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def datastyle_EmbeddedTextType(self):
        return self.__datastyle_EmbeddedTextType

    @datastyle_EmbeddedTextType.setter
    def datastyle_EmbeddedTextType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_EmbeddedTextType__datastyle_EmbeddedTextType", None)
        self.__datastyle_EmbeddedTextType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_NumberType55"):
                opp_val = getattr(old_value, "datastyle_NumberType55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_NumberType55"):
                opp_val = getattr(value, "datastyle_NumberType55", None)
                if opp_val is None:
                    setattr(value, "datastyle_NumberType55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_EmbeddedTextType118(self):
        return self.__datastyle_EmbeddedTextType118

    @datastyle_EmbeddedTextType118.setter
    def datastyle_EmbeddedTextType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_EmbeddedTextType__datastyle_EmbeddedTextType118", None)
        self.__datastyle_EmbeddedTextType118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot117"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot117"):
                opp_val = getattr(value, "datastyle_DocumentRoot117", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_SecondsType:

    def __init__(self, decimalPlaces: str, style: str, datastyle_SecondsType84: "datastyle_TimeStyleType" = None, datastyle_SecondsType: "datastyle_DateStyleType" = None, datastyle_SecondsType149: "datastyle_DocumentRoot" = None):
        self.decimalPlaces = decimalPlaces
        self.style = style
        self.datastyle_SecondsType84 = datastyle_SecondsType84
        self.datastyle_SecondsType = datastyle_SecondsType
        self.datastyle_SecondsType149 = datastyle_SecondsType149
        
        pass
    @property
    def decimalPlaces(self):
        return self.__decimalPlaces

    @decimalPlaces.setter
    def decimalPlaces(self, decimalPlaces: str):
        self.__decimalPlaces = decimalPlaces


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def datastyle_SecondsType149(self):
        return self.__datastyle_SecondsType149

    @datastyle_SecondsType149.setter
    def datastyle_SecondsType149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_SecondsType__datastyle_SecondsType149", None)
        self.__datastyle_SecondsType149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot148"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot148"):
                opp_val = getattr(value, "datastyle_DocumentRoot148", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_SecondsType(self):
        return self.__datastyle_SecondsType

    @datastyle_SecondsType.setter
    def datastyle_SecondsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_SecondsType__datastyle_SecondsType", None)
        self.__datastyle_SecondsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType43"):
                opp_val = getattr(old_value, "datastyle_DateStyleType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType43"):
                opp_val = getattr(value, "datastyle_DateStyleType43", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_SecondsType84(self):
        return self.__datastyle_SecondsType84

    @datastyle_SecondsType84.setter
    def datastyle_SecondsType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_SecondsType__datastyle_SecondsType84", None)
        self.__datastyle_SecondsType84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_TimeStyleType83"):
                opp_val = getattr(old_value, "datastyle_TimeStyleType83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_TimeStyleType83"):
                opp_val = getattr(value, "datastyle_TimeStyleType83", None)
                if opp_val is None:
                    setattr(value, "datastyle_TimeStyleType83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_MinutesType:

    def __init__(self, style: str, datastyle_MinutesType81: "datastyle_TimeStyleType" = None, datastyle_MinutesType: "datastyle_DateStyleType" = None, datastyle_MinutesType129: "datastyle_DocumentRoot" = None):
        self.style = style
        self.datastyle_MinutesType81 = datastyle_MinutesType81
        self.datastyle_MinutesType = datastyle_MinutesType
        self.datastyle_MinutesType129 = datastyle_MinutesType129
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def datastyle_MinutesType129(self):
        return self.__datastyle_MinutesType129

    @datastyle_MinutesType129.setter
    def datastyle_MinutesType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_MinutesType__datastyle_MinutesType129", None)
        self.__datastyle_MinutesType129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot128"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot128"):
                opp_val = getattr(value, "datastyle_DocumentRoot128", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_MinutesType(self):
        return self.__datastyle_MinutesType

    @datastyle_MinutesType.setter
    def datastyle_MinutesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_MinutesType__datastyle_MinutesType", None)
        self.__datastyle_MinutesType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType41"):
                opp_val = getattr(old_value, "datastyle_DateStyleType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType41"):
                opp_val = getattr(value, "datastyle_DateStyleType41", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_MinutesType81(self):
        return self.__datastyle_MinutesType81

    @datastyle_MinutesType81.setter
    def datastyle_MinutesType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_MinutesType__datastyle_MinutesType81", None)
        self.__datastyle_MinutesType81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_TimeStyleType80"):
                opp_val = getattr(old_value, "datastyle_TimeStyleType80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_TimeStyleType80"):
                opp_val = getattr(value, "datastyle_TimeStyleType80", None)
                if opp_val is None:
                    setattr(value, "datastyle_TimeStyleType80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_DayOfWeekType:

    def __init__(self, calendar: str, style: str, datastyle_DayOfWeekType115: "datastyle_DocumentRoot" = None, datastyle_DayOfWeekType: "datastyle_DateStyleType" = None):
        self.calendar = calendar
        self.style = style
        self.datastyle_DayOfWeekType115 = datastyle_DayOfWeekType115
        self.datastyle_DayOfWeekType = datastyle_DayOfWeekType
        
        pass
    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def datastyle_DayOfWeekType(self):
        return self.__datastyle_DayOfWeekType

    @datastyle_DayOfWeekType.setter
    def datastyle_DayOfWeekType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DayOfWeekType__datastyle_DayOfWeekType", None)
        self.__datastyle_DayOfWeekType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType31"):
                opp_val = getattr(old_value, "datastyle_DateStyleType31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType31"):
                opp_val = getattr(value, "datastyle_DateStyleType31", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_DayOfWeekType115(self):
        return self.__datastyle_DayOfWeekType115

    @datastyle_DayOfWeekType115.setter
    def datastyle_DayOfWeekType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DayOfWeekType__datastyle_DayOfWeekType115", None)
        self.__datastyle_DayOfWeekType115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot114"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot114"):
                opp_val = getattr(value, "datastyle_DocumentRoot114", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_HoursType:

    def __init__(self, style: str, datastyle_HoursType75: "datastyle_TimeStyleType" = None, datastyle_HoursType126: "datastyle_DocumentRoot" = None, datastyle_HoursType: "datastyle_DateStyleType" = None):
        self.style = style
        self.datastyle_HoursType75 = datastyle_HoursType75
        self.datastyle_HoursType126 = datastyle_HoursType126
        self.datastyle_HoursType = datastyle_HoursType
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def datastyle_HoursType126(self):
        return self.__datastyle_HoursType126

    @datastyle_HoursType126.setter
    def datastyle_HoursType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_HoursType__datastyle_HoursType126", None)
        self.__datastyle_HoursType126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot125"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot125"):
                opp_val = getattr(value, "datastyle_DocumentRoot125", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_HoursType(self):
        return self.__datastyle_HoursType

    @datastyle_HoursType.setter
    def datastyle_HoursType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_HoursType__datastyle_HoursType", None)
        self.__datastyle_HoursType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType37"):
                opp_val = getattr(old_value, "datastyle_DateStyleType37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType37"):
                opp_val = getattr(value, "datastyle_DateStyleType37", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_HoursType75(self):
        return self.__datastyle_HoursType75

    @datastyle_HoursType75.setter
    def datastyle_HoursType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_HoursType__datastyle_HoursType75", None)
        self.__datastyle_HoursType75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_TimeStyleType74"):
                opp_val = getattr(old_value, "datastyle_TimeStyleType74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_TimeStyleType74"):
                opp_val = getattr(value, "datastyle_TimeStyleType74", None)
                if opp_val is None:
                    setattr(value, "datastyle_TimeStyleType74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_QuarterType:

    def __init__(self, calendar: str, style: str, datastyle_QuarterType: "datastyle_DateStyleType" = None, datastyle_QuarterType144: "datastyle_DocumentRoot" = None):
        self.calendar = calendar
        self.style = style
        self.datastyle_QuarterType = datastyle_QuarterType
        self.datastyle_QuarterType144 = datastyle_QuarterType144
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def datastyle_QuarterType144(self):
        return self.__datastyle_QuarterType144

    @datastyle_QuarterType144.setter
    def datastyle_QuarterType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_QuarterType__datastyle_QuarterType144", None)
        self.__datastyle_QuarterType144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot143"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot143"):
                opp_val = getattr(value, "datastyle_DocumentRoot143", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_QuarterType(self):
        return self.__datastyle_QuarterType

    @datastyle_QuarterType.setter
    def datastyle_QuarterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_QuarterType__datastyle_QuarterType", None)
        self.__datastyle_QuarterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType35"):
                opp_val = getattr(old_value, "datastyle_DateStyleType35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType35"):
                opp_val = getattr(value, "datastyle_DateStyleType35", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_WeekOfYearType:

    def __init__(self, calendar: str, datastyle_WeekOfYearType: "datastyle_DateStyleType" = None, datastyle_WeekOfYearType161: "datastyle_DocumentRoot" = None):
        self.calendar = calendar
        self.datastyle_WeekOfYearType = datastyle_WeekOfYearType
        self.datastyle_WeekOfYearType161 = datastyle_WeekOfYearType161
        
        pass
    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def datastyle_WeekOfYearType161(self):
        return self.__datastyle_WeekOfYearType161

    @datastyle_WeekOfYearType161.setter
    def datastyle_WeekOfYearType161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_WeekOfYearType__datastyle_WeekOfYearType161", None)
        self.__datastyle_WeekOfYearType161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot160"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot160"):
                opp_val = getattr(value, "datastyle_DocumentRoot160", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_WeekOfYearType(self):
        return self.__datastyle_WeekOfYearType

    @datastyle_WeekOfYearType.setter
    def datastyle_WeekOfYearType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_WeekOfYearType__datastyle_WeekOfYearType", None)
        self.__datastyle_WeekOfYearType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType33"):
                opp_val = getattr(old_value, "datastyle_DateStyleType33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType33"):
                opp_val = getattr(value, "datastyle_DateStyleType33", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_MonthType:

    def __init__(self, possessiveForm: str, style: str, textual: str, calendar: str, datastyle_MonthType: "datastyle_DateStyleType" = None, datastyle_MonthType132: "datastyle_DocumentRoot" = None):
        self.possessiveForm = possessiveForm
        self.style = style
        self.textual = textual
        self.calendar = calendar
        self.datastyle_MonthType = datastyle_MonthType
        self.datastyle_MonthType132 = datastyle_MonthType132
        
        pass
    @property
    def textual(self):
        return self.__textual

    @textual.setter
    def textual(self, textual: str):
        self.__textual = textual


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def possessiveForm(self):
        return self.__possessiveForm

    @possessiveForm.setter
    def possessiveForm(self, possessiveForm: str):
        self.__possessiveForm = possessiveForm


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def datastyle_MonthType(self):
        return self.__datastyle_MonthType

    @datastyle_MonthType.setter
    def datastyle_MonthType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_MonthType__datastyle_MonthType", None)
        self.__datastyle_MonthType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType25"):
                opp_val = getattr(old_value, "datastyle_DateStyleType25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType25"):
                opp_val = getattr(value, "datastyle_DateStyleType25", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_MonthType132(self):
        return self.__datastyle_MonthType132

    @datastyle_MonthType132.setter
    def datastyle_MonthType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_MonthType__datastyle_MonthType132", None)
        self.__datastyle_MonthType132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot131"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot131"):
                opp_val = getattr(value, "datastyle_DocumentRoot131", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_DayType:

    def __init__(self, calendar: str, style: str, datastyle_DayType: "datastyle_DateStyleType" = None, datastyle_DayType112: "datastyle_DocumentRoot" = None):
        self.calendar = calendar
        self.style = style
        self.datastyle_DayType = datastyle_DayType
        self.datastyle_DayType112 = datastyle_DayType112
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def datastyle_DayType(self):
        return self.__datastyle_DayType

    @datastyle_DayType.setter
    def datastyle_DayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DayType__datastyle_DayType", None)
        self.__datastyle_DayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType23"):
                opp_val = getattr(old_value, "datastyle_DateStyleType23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType23"):
                opp_val = getattr(value, "datastyle_DateStyleType23", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_DayType112(self):
        return self.__datastyle_DayType112

    @datastyle_DayType112.setter
    def datastyle_DayType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DayType__datastyle_DayType112", None)
        self.__datastyle_DayType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot111"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot111"):
                opp_val = getattr(value, "datastyle_DocumentRoot111", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_EraType:

    def __init__(self, calendar: str, style: str, datastyle_EraType: "datastyle_DateStyleType" = None, datastyle_EraType121: "datastyle_DocumentRoot" = None):
        self.calendar = calendar
        self.style = style
        self.datastyle_EraType = datastyle_EraType
        self.datastyle_EraType121 = datastyle_EraType121
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def datastyle_EraType(self):
        return self.__datastyle_EraType

    @datastyle_EraType.setter
    def datastyle_EraType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_EraType__datastyle_EraType", None)
        self.__datastyle_EraType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType29"):
                opp_val = getattr(old_value, "datastyle_DateStyleType29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType29"):
                opp_val = getattr(value, "datastyle_DateStyleType29", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_EraType121(self):
        return self.__datastyle_EraType121

    @datastyle_EraType121.setter
    def datastyle_EraType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_EraType__datastyle_EraType121", None)
        self.__datastyle_EraType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot120"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot120"):
                opp_val = getattr(value, "datastyle_DocumentRoot120", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_YearType:

    def __init__(self, calendar: str, style: str, datastyle_YearType: "datastyle_DateStyleType" = None, datastyle_YearType164: "datastyle_DocumentRoot" = None):
        self.calendar = calendar
        self.style = style
        self.datastyle_YearType = datastyle_YearType
        self.datastyle_YearType164 = datastyle_YearType164
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, calendar: str):
        self.__calendar = calendar


    @property
    def datastyle_YearType(self):
        return self.__datastyle_YearType

    @datastyle_YearType.setter
    def datastyle_YearType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_YearType__datastyle_YearType", None)
        self.__datastyle_YearType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DateStyleType27"):
                opp_val = getattr(old_value, "datastyle_DateStyleType27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DateStyleType27"):
                opp_val = getattr(value, "datastyle_DateStyleType27", None)
                if opp_val is None:
                    setattr(value, "datastyle_DateStyleType27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_YearType164(self):
        return self.__datastyle_YearType164

    @datastyle_YearType164.setter
    def datastyle_YearType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_YearType__datastyle_YearType164", None)
        self.__datastyle_YearType164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot163"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot163"):
                opp_val = getattr(value, "datastyle_DocumentRoot163", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datastyle_DateStyleType:

    def __init__(self, text: str, group: str, text1: str, automaticOrder: str, country: str, formatSource: str, title: str, transliterationCountry: str, language: str, transliterationFormat: str, name: str, transliterationLanguage: str, transliterationStyle: str, volatile: str, datastyle_DateStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_DateStyleType27: set["datastyle_YearType"] = None, datastyle_DateStyleType29: set["datastyle_EraType"] = None, datastyle_DateStyleType109: "datastyle_DocumentRoot" = None, datastyle_DateStyleType23: set["datastyle_DayType"] = None, datastyle_DateStyleType25: set["datastyle_MonthType"] = None, datastyle_DateStyleType33: set["datastyle_WeekOfYearType"] = None, datastyle_DateStyleType35: set["datastyle_QuarterType"] = None, datastyle_DateStyleType37: set["datastyle_HoursType"] = None, datastyle_DateStyleType31: set["datastyle_DayOfWeekType"] = None, datastyle_DateStyleType39: set["datastyle_AmPmType"] = None, datastyle_DateStyleType45: set["datastyle_MapType"] = None, datastyle_DateStyleType41: set["datastyle_MinutesType"] = None, datastyle_DateStyleType43: set["datastyle_SecondsType"] = None):
        self.text = text
        self.group = group
        self.text1 = text1
        self.automaticOrder = automaticOrder
        self.country = country
        self.formatSource = formatSource
        self.title = title
        self.transliterationCountry = transliterationCountry
        self.language = language
        self.transliterationFormat = transliterationFormat
        self.name = name
        self.transliterationLanguage = transliterationLanguage
        self.transliterationStyle = transliterationStyle
        self.volatile = volatile
        self.datastyle_DateStyleType = datastyle_DateStyleType
        self.datastyle_DateStyleType27 = datastyle_DateStyleType27 if datastyle_DateStyleType27 is not None else set()
        self.datastyle_DateStyleType29 = datastyle_DateStyleType29 if datastyle_DateStyleType29 is not None else set()
        self.datastyle_DateStyleType109 = datastyle_DateStyleType109
        self.datastyle_DateStyleType23 = datastyle_DateStyleType23 if datastyle_DateStyleType23 is not None else set()
        self.datastyle_DateStyleType25 = datastyle_DateStyleType25 if datastyle_DateStyleType25 is not None else set()
        self.datastyle_DateStyleType33 = datastyle_DateStyleType33 if datastyle_DateStyleType33 is not None else set()
        self.datastyle_DateStyleType35 = datastyle_DateStyleType35 if datastyle_DateStyleType35 is not None else set()
        self.datastyle_DateStyleType37 = datastyle_DateStyleType37 if datastyle_DateStyleType37 is not None else set()
        self.datastyle_DateStyleType31 = datastyle_DateStyleType31 if datastyle_DateStyleType31 is not None else set()
        self.datastyle_DateStyleType39 = datastyle_DateStyleType39 if datastyle_DateStyleType39 is not None else set()
        self.datastyle_DateStyleType45 = datastyle_DateStyleType45 if datastyle_DateStyleType45 is not None else set()
        self.datastyle_DateStyleType41 = datastyle_DateStyleType41 if datastyle_DateStyleType41 is not None else set()
        self.datastyle_DateStyleType43 = datastyle_DateStyleType43 if datastyle_DateStyleType43 is not None else set()
        
        pass
    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def formatSource(self):
        return self.__formatSource

    @formatSource.setter
    def formatSource(self, formatSource: str):
        self.__formatSource = formatSource


    @property
    def automaticOrder(self):
        return self.__automaticOrder

    @automaticOrder.setter
    def automaticOrder(self, automaticOrder: str):
        self.__automaticOrder = automaticOrder


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def datastyle_DateStyleType23(self):
        return self.__datastyle_DateStyleType23

    @datastyle_DateStyleType23.setter
    def datastyle_DateStyleType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType23", None)
        self.__datastyle_DateStyleType23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_DayType"):
                    opp_val = getattr(item, "datastyle_DayType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_DayType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_DayType"):
                    opp_val = getattr(item, "datastyle_DayType", None)
                    
                    setattr(item, "datastyle_DayType", self)
                    

    @property
    def datastyle_DateStyleType43(self):
        return self.__datastyle_DateStyleType43

    @datastyle_DateStyleType43.setter
    def datastyle_DateStyleType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType43", None)
        self.__datastyle_DateStyleType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_SecondsType"):
                    opp_val = getattr(item, "datastyle_SecondsType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_SecondsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_SecondsType"):
                    opp_val = getattr(item, "datastyle_SecondsType", None)
                    
                    setattr(item, "datastyle_SecondsType", self)
                    

    @property
    def datastyle_DateStyleType31(self):
        return self.__datastyle_DateStyleType31

    @datastyle_DateStyleType31.setter
    def datastyle_DateStyleType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType31", None)
        self.__datastyle_DateStyleType31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_DayOfWeekType"):
                    opp_val = getattr(item, "datastyle_DayOfWeekType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_DayOfWeekType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_DayOfWeekType"):
                    opp_val = getattr(item, "datastyle_DayOfWeekType", None)
                    
                    setattr(item, "datastyle_DayOfWeekType", self)
                    

    @property
    def datastyle_DateStyleType45(self):
        return self.__datastyle_DateStyleType45

    @datastyle_DateStyleType45.setter
    def datastyle_DateStyleType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType45", None)
        self.__datastyle_DateStyleType45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType46"):
                    opp_val = getattr(item, "datastyle_MapType46", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType46"):
                    opp_val = getattr(item, "datastyle_MapType46", None)
                    
                    setattr(item, "datastyle_MapType46", self)
                    

    @property
    def datastyle_DateStyleType41(self):
        return self.__datastyle_DateStyleType41

    @datastyle_DateStyleType41.setter
    def datastyle_DateStyleType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType41", None)
        self.__datastyle_DateStyleType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MinutesType"):
                    opp_val = getattr(item, "datastyle_MinutesType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MinutesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MinutesType"):
                    opp_val = getattr(item, "datastyle_MinutesType", None)
                    
                    setattr(item, "datastyle_MinutesType", self)
                    

    @property
    def datastyle_DateStyleType(self):
        return self.__datastyle_DateStyleType

    @datastyle_DateStyleType.setter
    def datastyle_DateStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType", None)
        self.__datastyle_DateStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent21"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent21", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent21"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent21", None)
                setattr(value, "datastyle_StyleTextPropertiesContent21", self)

    @property
    def datastyle_DateStyleType109(self):
        return self.__datastyle_DateStyleType109

    @datastyle_DateStyleType109.setter
    def datastyle_DateStyleType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType109", None)
        self.__datastyle_DateStyleType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot108"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot108"):
                opp_val = getattr(value, "datastyle_DocumentRoot108", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_DateStyleType35(self):
        return self.__datastyle_DateStyleType35

    @datastyle_DateStyleType35.setter
    def datastyle_DateStyleType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType35", None)
        self.__datastyle_DateStyleType35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_QuarterType"):
                    opp_val = getattr(item, "datastyle_QuarterType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_QuarterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_QuarterType"):
                    opp_val = getattr(item, "datastyle_QuarterType", None)
                    
                    setattr(item, "datastyle_QuarterType", self)
                    

    @property
    def datastyle_DateStyleType29(self):
        return self.__datastyle_DateStyleType29

    @datastyle_DateStyleType29.setter
    def datastyle_DateStyleType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType29", None)
        self.__datastyle_DateStyleType29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EraType"):
                    opp_val = getattr(item, "datastyle_EraType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EraType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EraType"):
                    opp_val = getattr(item, "datastyle_EraType", None)
                    
                    setattr(item, "datastyle_EraType", self)
                    

    @property
    def datastyle_DateStyleType25(self):
        return self.__datastyle_DateStyleType25

    @datastyle_DateStyleType25.setter
    def datastyle_DateStyleType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType25", None)
        self.__datastyle_DateStyleType25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MonthType"):
                    opp_val = getattr(item, "datastyle_MonthType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MonthType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MonthType"):
                    opp_val = getattr(item, "datastyle_MonthType", None)
                    
                    setattr(item, "datastyle_MonthType", self)
                    

    @property
    def datastyle_DateStyleType39(self):
        return self.__datastyle_DateStyleType39

    @datastyle_DateStyleType39.setter
    def datastyle_DateStyleType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType39", None)
        self.__datastyle_DateStyleType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_AmPmType"):
                    opp_val = getattr(item, "datastyle_AmPmType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_AmPmType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_AmPmType"):
                    opp_val = getattr(item, "datastyle_AmPmType", None)
                    
                    setattr(item, "datastyle_AmPmType", self)
                    

    @property
    def datastyle_DateStyleType27(self):
        return self.__datastyle_DateStyleType27

    @datastyle_DateStyleType27.setter
    def datastyle_DateStyleType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType27", None)
        self.__datastyle_DateStyleType27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_YearType"):
                    opp_val = getattr(item, "datastyle_YearType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_YearType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_YearType"):
                    opp_val = getattr(item, "datastyle_YearType", None)
                    
                    setattr(item, "datastyle_YearType", self)
                    

    @property
    def datastyle_DateStyleType37(self):
        return self.__datastyle_DateStyleType37

    @datastyle_DateStyleType37.setter
    def datastyle_DateStyleType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType37", None)
        self.__datastyle_DateStyleType37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_HoursType"):
                    opp_val = getattr(item, "datastyle_HoursType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_HoursType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_HoursType"):
                    opp_val = getattr(item, "datastyle_HoursType", None)
                    
                    setattr(item, "datastyle_HoursType", self)
                    

    @property
    def datastyle_DateStyleType33(self):
        return self.__datastyle_DateStyleType33

    @datastyle_DateStyleType33.setter
    def datastyle_DateStyleType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_DateStyleType__datastyle_DateStyleType33", None)
        self.__datastyle_DateStyleType33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_WeekOfYearType"):
                    opp_val = getattr(item, "datastyle_WeekOfYearType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_WeekOfYearType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_WeekOfYearType"):
                    opp_val = getattr(item, "datastyle_WeekOfYearType", None)
                    
                    setattr(item, "datastyle_WeekOfYearType", self)
                    

class datastyle_CurrencyStyleType:

    def __init__(self, text: str, text1: str, text2: str, text3: str, automaticOrder: str, country: str, language: str, name: str, text4: str, volatile: str, title: str, transliterationCountry: str, transliterationFormat: str, transliterationLanguage: str, transliterationStyle: str, datastyle_CurrencyStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_CurrencyStyleType8: "datastyle_NumberType" = None, datastyle_CurrencyStyleType10: "datastyle_CurrencySymbolType" = None, datastyle_CurrencyStyleType12: "datastyle_CurrencySymbolType" = None, datastyle_CurrencyStyleType15: "datastyle_NumberType" = None, datastyle_CurrencyStyleType18: set["datastyle_MapType"] = None, datastyle_CurrencyStyleType103: "datastyle_DocumentRoot" = None):
        self.text = text
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.automaticOrder = automaticOrder
        self.country = country
        self.language = language
        self.name = name
        self.text4 = text4
        self.volatile = volatile
        self.title = title
        self.transliterationCountry = transliterationCountry
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.transliterationStyle = transliterationStyle
        self.datastyle_CurrencyStyleType = datastyle_CurrencyStyleType
        self.datastyle_CurrencyStyleType8 = datastyle_CurrencyStyleType8
        self.datastyle_CurrencyStyleType10 = datastyle_CurrencyStyleType10
        self.datastyle_CurrencyStyleType12 = datastyle_CurrencyStyleType12
        self.datastyle_CurrencyStyleType15 = datastyle_CurrencyStyleType15
        self.datastyle_CurrencyStyleType18 = datastyle_CurrencyStyleType18 if datastyle_CurrencyStyleType18 is not None else set()
        self.datastyle_CurrencyStyleType103 = datastyle_CurrencyStyleType103
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def automaticOrder(self):
        return self.__automaticOrder

    @automaticOrder.setter
    def automaticOrder(self, automaticOrder: str):
        self.__automaticOrder = automaticOrder


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def text4(self):
        return self.__text4

    @text4.setter
    def text4(self, text4: str):
        self.__text4 = text4


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def text2(self):
        return self.__text2

    @text2.setter
    def text2(self, text2: str):
        self.__text2 = text2


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def text3(self):
        return self.__text3

    @text3.setter
    def text3(self, text3: str):
        self.__text3 = text3


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def datastyle_CurrencyStyleType103(self):
        return self.__datastyle_CurrencyStyleType103

    @datastyle_CurrencyStyleType103.setter
    def datastyle_CurrencyStyleType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType103", None)
        self.__datastyle_CurrencyStyleType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot102"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot102"):
                opp_val = getattr(value, "datastyle_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_CurrencyStyleType15(self):
        return self.__datastyle_CurrencyStyleType15

    @datastyle_CurrencyStyleType15.setter
    def datastyle_CurrencyStyleType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType15", None)
        self.__datastyle_CurrencyStyleType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_NumberType16"):
                opp_val = getattr(old_value, "datastyle_NumberType16", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_NumberType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_NumberType16"):
                opp_val = getattr(value, "datastyle_NumberType16", None)
                setattr(value, "datastyle_NumberType16", self)

    @property
    def datastyle_CurrencyStyleType(self):
        return self.__datastyle_CurrencyStyleType

    @datastyle_CurrencyStyleType.setter
    def datastyle_CurrencyStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType", None)
        self.__datastyle_CurrencyStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent6"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent6", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent6"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent6", None)
                setattr(value, "datastyle_StyleTextPropertiesContent6", self)

    @property
    def datastyle_CurrencyStyleType18(self):
        return self.__datastyle_CurrencyStyleType18

    @datastyle_CurrencyStyleType18.setter
    def datastyle_CurrencyStyleType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType18", None)
        self.__datastyle_CurrencyStyleType18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType19"):
                    opp_val = getattr(item, "datastyle_MapType19", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType19"):
                    opp_val = getattr(item, "datastyle_MapType19", None)
                    
                    setattr(item, "datastyle_MapType19", self)
                    

    @property
    def datastyle_CurrencyStyleType10(self):
        return self.__datastyle_CurrencyStyleType10

    @datastyle_CurrencyStyleType10.setter
    def datastyle_CurrencyStyleType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType10", None)
        self.__datastyle_CurrencyStyleType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencySymbolType"):
                opp_val = getattr(old_value, "datastyle_CurrencySymbolType", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencySymbolType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencySymbolType"):
                opp_val = getattr(value, "datastyle_CurrencySymbolType", None)
                setattr(value, "datastyle_CurrencySymbolType", self)

    @property
    def datastyle_CurrencyStyleType12(self):
        return self.__datastyle_CurrencyStyleType12

    @datastyle_CurrencyStyleType12.setter
    def datastyle_CurrencyStyleType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType12", None)
        self.__datastyle_CurrencyStyleType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencySymbolType13"):
                opp_val = getattr(old_value, "datastyle_CurrencySymbolType13", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencySymbolType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencySymbolType13"):
                opp_val = getattr(value, "datastyle_CurrencySymbolType13", None)
                setattr(value, "datastyle_CurrencySymbolType13", self)

    @property
    def datastyle_CurrencyStyleType8(self):
        return self.__datastyle_CurrencyStyleType8

    @datastyle_CurrencyStyleType8.setter
    def datastyle_CurrencyStyleType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencyStyleType__datastyle_CurrencyStyleType8", None)
        self.__datastyle_CurrencyStyleType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_NumberType"):
                opp_val = getattr(old_value, "datastyle_NumberType", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_NumberType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_NumberType"):
                opp_val = getattr(value, "datastyle_NumberType", None)
                setattr(value, "datastyle_NumberType", self)

class datastyle_CurrencySymbolType:

    def __init__(self, language: str, mixed: str, country: str, datastyle_CurrencySymbolType: "datastyle_CurrencyStyleType" = None, datastyle_CurrencySymbolType13: "datastyle_CurrencyStyleType" = None, datastyle_CurrencySymbolType106: "datastyle_DocumentRoot" = None):
        self.language = language
        self.mixed = mixed
        self.country = country
        self.datastyle_CurrencySymbolType = datastyle_CurrencySymbolType
        self.datastyle_CurrencySymbolType13 = datastyle_CurrencySymbolType13
        self.datastyle_CurrencySymbolType106 = datastyle_CurrencySymbolType106
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def datastyle_CurrencySymbolType(self):
        return self.__datastyle_CurrencySymbolType

    @datastyle_CurrencySymbolType.setter
    def datastyle_CurrencySymbolType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencySymbolType__datastyle_CurrencySymbolType", None)
        self.__datastyle_CurrencySymbolType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencyStyleType10"):
                opp_val = getattr(old_value, "datastyle_CurrencyStyleType10", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencyStyleType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencyStyleType10"):
                opp_val = getattr(value, "datastyle_CurrencyStyleType10", None)
                setattr(value, "datastyle_CurrencyStyleType10", self)

    @property
    def datastyle_CurrencySymbolType106(self):
        return self.__datastyle_CurrencySymbolType106

    @datastyle_CurrencySymbolType106.setter
    def datastyle_CurrencySymbolType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencySymbolType__datastyle_CurrencySymbolType106", None)
        self.__datastyle_CurrencySymbolType106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot105"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot105"):
                opp_val = getattr(value, "datastyle_DocumentRoot105", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_CurrencySymbolType13(self):
        return self.__datastyle_CurrencySymbolType13

    @datastyle_CurrencySymbolType13.setter
    def datastyle_CurrencySymbolType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_CurrencySymbolType__datastyle_CurrencySymbolType13", None)
        self.__datastyle_CurrencySymbolType13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencyStyleType12"):
                opp_val = getattr(old_value, "datastyle_CurrencyStyleType12", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencyStyleType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencyStyleType12"):
                opp_val = getattr(value, "datastyle_CurrencyStyleType12", None)
                setattr(value, "datastyle_CurrencyStyleType12", self)

class datastyle_NumberType:

    def __init__(self, displayFactor: str, grouping: str, minIntegerDigits: str, decimalPlaces: str, decimalReplacement: str, datastyle_NumberType: "datastyle_CurrencyStyleType" = None, datastyle_NumberType16: "datastyle_CurrencyStyleType" = None, datastyle_NumberType60: "datastyle_PercentageStyleType" = None, datastyle_NumberType55: set["datastyle_EmbeddedTextType"] = None, datastyle_NumberType135: "datastyle_DocumentRoot" = None):
        self.displayFactor = displayFactor
        self.grouping = grouping
        self.minIntegerDigits = minIntegerDigits
        self.decimalPlaces = decimalPlaces
        self.decimalReplacement = decimalReplacement
        self.datastyle_NumberType = datastyle_NumberType
        self.datastyle_NumberType16 = datastyle_NumberType16
        self.datastyle_NumberType60 = datastyle_NumberType60
        self.datastyle_NumberType55 = datastyle_NumberType55 if datastyle_NumberType55 is not None else set()
        self.datastyle_NumberType135 = datastyle_NumberType135
        
        pass
    @property
    def decimalReplacement(self):
        return self.__decimalReplacement

    @decimalReplacement.setter
    def decimalReplacement(self, decimalReplacement: str):
        self.__decimalReplacement = decimalReplacement


    @property
    def grouping(self):
        return self.__grouping

    @grouping.setter
    def grouping(self, grouping: str):
        self.__grouping = grouping


    @property
    def displayFactor(self):
        return self.__displayFactor

    @displayFactor.setter
    def displayFactor(self, displayFactor: str):
        self.__displayFactor = displayFactor


    @property
    def minIntegerDigits(self):
        return self.__minIntegerDigits

    @minIntegerDigits.setter
    def minIntegerDigits(self, minIntegerDigits: str):
        self.__minIntegerDigits = minIntegerDigits


    @property
    def decimalPlaces(self):
        return self.__decimalPlaces

    @decimalPlaces.setter
    def decimalPlaces(self, decimalPlaces: str):
        self.__decimalPlaces = decimalPlaces


    @property
    def datastyle_NumberType(self):
        return self.__datastyle_NumberType

    @datastyle_NumberType.setter
    def datastyle_NumberType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberType__datastyle_NumberType", None)
        self.__datastyle_NumberType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencyStyleType8"):
                opp_val = getattr(old_value, "datastyle_CurrencyStyleType8", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencyStyleType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencyStyleType8"):
                opp_val = getattr(value, "datastyle_CurrencyStyleType8", None)
                setattr(value, "datastyle_CurrencyStyleType8", self)

    @property
    def datastyle_NumberType55(self):
        return self.__datastyle_NumberType55

    @datastyle_NumberType55.setter
    def datastyle_NumberType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberType__datastyle_NumberType55", None)
        self.__datastyle_NumberType55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_EmbeddedTextType"):
                    opp_val = getattr(item, "datastyle_EmbeddedTextType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_EmbeddedTextType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_EmbeddedTextType"):
                    opp_val = getattr(item, "datastyle_EmbeddedTextType", None)
                    
                    setattr(item, "datastyle_EmbeddedTextType", self)
                    

    @property
    def datastyle_NumberType135(self):
        return self.__datastyle_NumberType135

    @datastyle_NumberType135.setter
    def datastyle_NumberType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberType__datastyle_NumberType135", None)
        self.__datastyle_NumberType135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot134"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot134"):
                opp_val = getattr(value, "datastyle_DocumentRoot134", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_NumberType16(self):
        return self.__datastyle_NumberType16

    @datastyle_NumberType16.setter
    def datastyle_NumberType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberType__datastyle_NumberType16", None)
        self.__datastyle_NumberType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_CurrencyStyleType15"):
                opp_val = getattr(old_value, "datastyle_CurrencyStyleType15", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_CurrencyStyleType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_CurrencyStyleType15"):
                opp_val = getattr(value, "datastyle_CurrencyStyleType15", None)
                setattr(value, "datastyle_CurrencyStyleType15", self)

    @property
    def datastyle_NumberType60(self):
        return self.__datastyle_NumberType60

    @datastyle_NumberType60.setter
    def datastyle_NumberType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_NumberType__datastyle_NumberType60", None)
        self.__datastyle_NumberType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_PercentageStyleType59"):
                opp_val = getattr(old_value, "datastyle_PercentageStyleType59", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_PercentageStyleType59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_PercentageStyleType59"):
                opp_val = getattr(value, "datastyle_PercentageStyleType59", None)
                setattr(value, "datastyle_PercentageStyleType59", self)

class datastyle_MapType:

    pass
class datastyle_AmPmType:

    pass
class datastyle_BooleanType:

    pass
class datastyle_StyleTextPropertiesContent:

    pass
class datastyle_BooleanStyleType:

    def __init__(self, text: str, text1: str, country: str, language: str, name: str, title: str, transliterationCountry: str, transliterationFormat: str, transliterationLanguage: str, transliterationStyle: str, volatile: str, datastyle_BooleanStyleType: "datastyle_StyleTextPropertiesContent" = None, datastyle_BooleanStyleType2: "datastyle_BooleanType" = None, datastyle_BooleanStyleType4: set["datastyle_MapType"] = None, datastyle_BooleanStyleType100: "datastyle_DocumentRoot" = None):
        self.text = text
        self.text1 = text1
        self.country = country
        self.language = language
        self.name = name
        self.title = title
        self.transliterationCountry = transliterationCountry
        self.transliterationFormat = transliterationFormat
        self.transliterationLanguage = transliterationLanguage
        self.transliterationStyle = transliterationStyle
        self.volatile = volatile
        self.datastyle_BooleanStyleType = datastyle_BooleanStyleType
        self.datastyle_BooleanStyleType2 = datastyle_BooleanStyleType2
        self.datastyle_BooleanStyleType4 = datastyle_BooleanStyleType4 if datastyle_BooleanStyleType4 is not None else set()
        self.datastyle_BooleanStyleType100 = datastyle_BooleanStyleType100
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def text1(self):
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1


    @property
    def transliterationCountry(self):
        return self.__transliterationCountry

    @transliterationCountry.setter
    def transliterationCountry(self, transliterationCountry: str):
        self.__transliterationCountry = transliterationCountry


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def transliterationStyle(self):
        return self.__transliterationStyle

    @transliterationStyle.setter
    def transliterationStyle(self, transliterationStyle: str):
        self.__transliterationStyle = transliterationStyle


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def transliterationLanguage(self):
        return self.__transliterationLanguage

    @transliterationLanguage.setter
    def transliterationLanguage(self, transliterationLanguage: str):
        self.__transliterationLanguage = transliterationLanguage


    @property
    def transliterationFormat(self):
        return self.__transliterationFormat

    @transliterationFormat.setter
    def transliterationFormat(self, transliterationFormat: str):
        self.__transliterationFormat = transliterationFormat


    @property
    def datastyle_BooleanStyleType4(self):
        return self.__datastyle_BooleanStyleType4

    @datastyle_BooleanStyleType4.setter
    def datastyle_BooleanStyleType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_BooleanStyleType__datastyle_BooleanStyleType4", None)
        self.__datastyle_BooleanStyleType4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datastyle_MapType"):
                    opp_val = getattr(item, "datastyle_MapType", None)
                    
                    if opp_val == self:
                        setattr(item, "datastyle_MapType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datastyle_MapType"):
                    opp_val = getattr(item, "datastyle_MapType", None)
                    
                    setattr(item, "datastyle_MapType", self)
                    

    @property
    def datastyle_BooleanStyleType100(self):
        return self.__datastyle_BooleanStyleType100

    @datastyle_BooleanStyleType100.setter
    def datastyle_BooleanStyleType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_BooleanStyleType__datastyle_BooleanStyleType100", None)
        self.__datastyle_BooleanStyleType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_DocumentRoot99"):
                opp_val = getattr(old_value, "datastyle_DocumentRoot99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_DocumentRoot99"):
                opp_val = getattr(value, "datastyle_DocumentRoot99", None)
                if opp_val is None:
                    setattr(value, "datastyle_DocumentRoot99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datastyle_BooleanStyleType(self):
        return self.__datastyle_BooleanStyleType

    @datastyle_BooleanStyleType.setter
    def datastyle_BooleanStyleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_BooleanStyleType__datastyle_BooleanStyleType", None)
        self.__datastyle_BooleanStyleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_StyleTextPropertiesContent"):
                opp_val = getattr(old_value, "datastyle_StyleTextPropertiesContent", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_StyleTextPropertiesContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_StyleTextPropertiesContent"):
                opp_val = getattr(value, "datastyle_StyleTextPropertiesContent", None)
                setattr(value, "datastyle_StyleTextPropertiesContent", self)

    @property
    def datastyle_BooleanStyleType2(self):
        return self.__datastyle_BooleanStyleType2

    @datastyle_BooleanStyleType2.setter
    def datastyle_BooleanStyleType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datastyle_BooleanStyleType__datastyle_BooleanStyleType2", None)
        self.__datastyle_BooleanStyleType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datastyle_BooleanType"):
                opp_val = getattr(old_value, "datastyle_BooleanType", None)
                if opp_val == self:
                    setattr(old_value, "datastyle_BooleanType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datastyle_BooleanType"):
                opp_val = getattr(value, "datastyle_BooleanType", None)
                setattr(value, "datastyle_BooleanType", self)
