####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
CalendarTypeMember2: Enumeration = Enumeration(
    name="CalendarTypeMember2",
    literals={
            EnumerationLiteral(name="gengou")
    }
)

CalendarTypeMember3: Enumeration = Enumeration(
    name="CalendarTypeMember3",
    literals={
            EnumerationLiteral(name="ROC")
    }
)

CalendarTypeMember4: Enumeration = Enumeration(
    name="CalendarTypeMember4",
    literals={
            EnumerationLiteral(name="hanjaYoil")
    }
)

CalendarTypeMember1: Enumeration = Enumeration(
    name="CalendarTypeMember1",
    literals={
            EnumerationLiteral(name="gregorian")
    }
)

CalendarTypeMember6: Enumeration = Enumeration(
    name="CalendarTypeMember6",
    literals={
            EnumerationLiteral(name="hijri")
    }
)

CalendarTypeMember7: Enumeration = Enumeration(
    name="CalendarTypeMember7",
    literals={
            EnumerationLiteral(name="jewish")
    }
)

CalendarTypeMember8: Enumeration = Enumeration(
    name="CalendarTypeMember8",
    literals={
            EnumerationLiteral(name="buddhist")
    }
)

CalendarTypeMember5: Enumeration = Enumeration(
    name="CalendarTypeMember5",
    literals={
            EnumerationLiteral(name="hanja")
    }
)

FormatSourceType: Enumeration = Enumeration(
    name="FormatSourceType",
    literals={
            EnumerationLiteral(name="fixed"),
			EnumerationLiteral(name="language")
    }
)

StyleType: Enumeration = Enumeration(
    name="StyleType",
    literals={
            EnumerationLiteral(name="short"),
			EnumerationLiteral(name="long")
    }
)

TransliterationStyleType: Enumeration = Enumeration(
    name="TransliterationStyleType",
    literals={
            EnumerationLiteral(name="short"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="long")
    }
)

# Classes
datastyle_BooleanStyleType = Class(name="datastyle_BooleanStyleType")
datastyle_StyleTextPropertiesContent = Class(name="datastyle_StyleTextPropertiesContent")
datastyle_BooleanType = Class(name="datastyle_BooleanType")
datastyle_AmPmType = Class(name="datastyle_AmPmType")
datastyle_MapType = Class(name="datastyle_MapType")
datastyle_NumberType = Class(name="datastyle_NumberType")
datastyle_CurrencySymbolType = Class(name="datastyle_CurrencySymbolType")
datastyle_CurrencyStyleType = Class(name="datastyle_CurrencyStyleType")
datastyle_DateStyleType = Class(name="datastyle_DateStyleType")
datastyle_YearType = Class(name="datastyle_YearType")
datastyle_EraType = Class(name="datastyle_EraType")
datastyle_DayType = Class(name="datastyle_DayType")
datastyle_MonthType = Class(name="datastyle_MonthType")
datastyle_WeekOfYearType = Class(name="datastyle_WeekOfYearType")
datastyle_QuarterType = Class(name="datastyle_QuarterType")
datastyle_HoursType = Class(name="datastyle_HoursType")
datastyle_DayOfWeekType = Class(name="datastyle_DayOfWeekType")
datastyle_MinutesType = Class(name="datastyle_MinutesType")
datastyle_SecondsType = Class(name="datastyle_SecondsType")
datastyle_EmbeddedTextType = Class(name="datastyle_EmbeddedTextType")
datastyle_FractionType = Class(name="datastyle_FractionType")
datastyle_NumberStyleType = Class(name="datastyle_NumberStyleType")
datastyle_EObject = Class(name="datastyle_EObject")
datastyle_PercentageStyleType = Class(name="datastyle_PercentageStyleType")
datastyle_ScientificNumberType = Class(name="datastyle_ScientificNumberType")
datastyle_TextContentType = Class(name="datastyle_TextContentType")
datastyle_TextStyleType = Class(name="datastyle_TextStyleType")
datastyle_TimeStyleType = Class(name="datastyle_TimeStyleType")
datastyle_DocumentRoot = Class(name="datastyle_DocumentRoot")
datastyle_EStringToStringMapEntry = Class(name="datastyle_EStringToStringMapEntry")

# datastyle_BooleanStyleType class attributes and methods
datastyle_BooleanStyleType_text: Property = Property(name="text", type=StringType)
datastyle_BooleanStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_BooleanStyleType_country: Property = Property(name="country", type=StringType)
datastyle_BooleanStyleType_language: Property = Property(name="language", type=StringType)
datastyle_BooleanStyleType_name: Property = Property(name="name", type=StringType)
datastyle_BooleanStyleType_title: Property = Property(name="title", type=StringType)
datastyle_BooleanStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_BooleanStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_BooleanStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_BooleanStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_BooleanStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_BooleanStyleType.attributes={datastyle_BooleanStyleType_name, datastyle_BooleanStyleType_country, datastyle_BooleanStyleType_text1, datastyle_BooleanStyleType_text, datastyle_BooleanStyleType_transliterationStyle, datastyle_BooleanStyleType_transliterationLanguage, datastyle_BooleanStyleType_title, datastyle_BooleanStyleType_transliterationCountry, datastyle_BooleanStyleType_language, datastyle_BooleanStyleType_transliterationFormat, datastyle_BooleanStyleType_volatile}

# datastyle_StyleTextPropertiesContent class attributes and methods

# datastyle_BooleanType class attributes and methods

# datastyle_AmPmType class attributes and methods

# datastyle_MapType class attributes and methods

# datastyle_NumberType class attributes and methods
datastyle_NumberType_displayFactor: Property = Property(name="displayFactor", type=StringType)
datastyle_NumberType_grouping: Property = Property(name="grouping", type=StringType)
datastyle_NumberType_minIntegerDigits: Property = Property(name="minIntegerDigits", type=StringType)
datastyle_NumberType_decimalPlaces: Property = Property(name="decimalPlaces", type=StringType)
datastyle_NumberType_decimalReplacement: Property = Property(name="decimalReplacement", type=StringType)
datastyle_NumberType.attributes={datastyle_NumberType_decimalPlaces, datastyle_NumberType_minIntegerDigits, datastyle_NumberType_displayFactor, datastyle_NumberType_grouping, datastyle_NumberType_decimalReplacement}

# datastyle_CurrencySymbolType class attributes and methods
datastyle_CurrencySymbolType_mixed: Property = Property(name="mixed", type=StringType)
datastyle_CurrencySymbolType_country: Property = Property(name="country", type=StringType)
datastyle_CurrencySymbolType_language: Property = Property(name="language", type=StringType)
datastyle_CurrencySymbolType.attributes={datastyle_CurrencySymbolType_mixed, datastyle_CurrencySymbolType_language, datastyle_CurrencySymbolType_country}

# datastyle_CurrencyStyleType class attributes and methods
datastyle_CurrencyStyleType_text: Property = Property(name="text", type=StringType)
datastyle_CurrencyStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_CurrencyStyleType_text2: Property = Property(name="text2", type=StringType)
datastyle_CurrencyStyleType_text3: Property = Property(name="text3", type=StringType)
datastyle_CurrencyStyleType_automaticOrder: Property = Property(name="automaticOrder", type=StringType)
datastyle_CurrencyStyleType_country: Property = Property(name="country", type=StringType)
datastyle_CurrencyStyleType_language: Property = Property(name="language", type=StringType)
datastyle_CurrencyStyleType_name: Property = Property(name="name", type=StringType)
datastyle_CurrencyStyleType_text4: Property = Property(name="text4", type=StringType)
datastyle_CurrencyStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_CurrencyStyleType_title: Property = Property(name="title", type=StringType)
datastyle_CurrencyStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_CurrencyStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_CurrencyStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_CurrencyStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_CurrencyStyleType.attributes={datastyle_CurrencyStyleType_title, datastyle_CurrencyStyleType_text3, datastyle_CurrencyStyleType_text, datastyle_CurrencyStyleType_text2, datastyle_CurrencyStyleType_volatile, datastyle_CurrencyStyleType_automaticOrder, datastyle_CurrencyStyleType_language, datastyle_CurrencyStyleType_name, datastyle_CurrencyStyleType_country, datastyle_CurrencyStyleType_transliterationFormat, datastyle_CurrencyStyleType_text1, datastyle_CurrencyStyleType_transliterationLanguage, datastyle_CurrencyStyleType_transliterationStyle, datastyle_CurrencyStyleType_transliterationCountry, datastyle_CurrencyStyleType_text4}

# datastyle_DateStyleType class attributes and methods
datastyle_DateStyleType_text: Property = Property(name="text", type=StringType)
datastyle_DateStyleType_group: Property = Property(name="group", type=StringType)
datastyle_DateStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_DateStyleType_automaticOrder: Property = Property(name="automaticOrder", type=StringType)
datastyle_DateStyleType_country: Property = Property(name="country", type=StringType)
datastyle_DateStyleType_formatSource: Property = Property(name="formatSource", type=StringType)
datastyle_DateStyleType_title: Property = Property(name="title", type=StringType)
datastyle_DateStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_DateStyleType_language: Property = Property(name="language", type=StringType)
datastyle_DateStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_DateStyleType_name: Property = Property(name="name", type=StringType)
datastyle_DateStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_DateStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_DateStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_DateStyleType.attributes={datastyle_DateStyleType_transliterationStyle, datastyle_DateStyleType_name, datastyle_DateStyleType_text, datastyle_DateStyleType_formatSource, datastyle_DateStyleType_language, datastyle_DateStyleType_transliterationCountry, datastyle_DateStyleType_transliterationFormat, datastyle_DateStyleType_country, datastyle_DateStyleType_title, datastyle_DateStyleType_automaticOrder, datastyle_DateStyleType_group, datastyle_DateStyleType_transliterationLanguage, datastyle_DateStyleType_volatile, datastyle_DateStyleType_text1}

# datastyle_YearType class attributes and methods
datastyle_YearType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_YearType_style: Property = Property(name="style", type=StringType)
datastyle_YearType.attributes={datastyle_YearType_calendar, datastyle_YearType_style}

# datastyle_EraType class attributes and methods
datastyle_EraType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_EraType_style: Property = Property(name="style", type=StringType)
datastyle_EraType.attributes={datastyle_EraType_style, datastyle_EraType_calendar}

# datastyle_DayType class attributes and methods
datastyle_DayType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_DayType_style: Property = Property(name="style", type=StringType)
datastyle_DayType.attributes={datastyle_DayType_calendar, datastyle_DayType_style}

# datastyle_MonthType class attributes and methods
datastyle_MonthType_possessiveForm: Property = Property(name="possessiveForm", type=StringType)
datastyle_MonthType_style: Property = Property(name="style", type=StringType)
datastyle_MonthType_textual: Property = Property(name="textual", type=StringType)
datastyle_MonthType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_MonthType.attributes={datastyle_MonthType_possessiveForm, datastyle_MonthType_calendar, datastyle_MonthType_textual, datastyle_MonthType_style}

# datastyle_WeekOfYearType class attributes and methods
datastyle_WeekOfYearType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_WeekOfYearType.attributes={datastyle_WeekOfYearType_calendar}

# datastyle_QuarterType class attributes and methods
datastyle_QuarterType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_QuarterType_style: Property = Property(name="style", type=StringType)
datastyle_QuarterType.attributes={datastyle_QuarterType_calendar, datastyle_QuarterType_style}

# datastyle_HoursType class attributes and methods
datastyle_HoursType_style: Property = Property(name="style", type=StringType)
datastyle_HoursType.attributes={datastyle_HoursType_style}

# datastyle_DayOfWeekType class attributes and methods
datastyle_DayOfWeekType_calendar: Property = Property(name="calendar", type=StringType)
datastyle_DayOfWeekType_style: Property = Property(name="style", type=StringType)
datastyle_DayOfWeekType.attributes={datastyle_DayOfWeekType_calendar, datastyle_DayOfWeekType_style}

# datastyle_MinutesType class attributes and methods
datastyle_MinutesType_style: Property = Property(name="style", type=StringType)
datastyle_MinutesType.attributes={datastyle_MinutesType_style}

# datastyle_SecondsType class attributes and methods
datastyle_SecondsType_decimalPlaces: Property = Property(name="decimalPlaces", type=StringType)
datastyle_SecondsType_style: Property = Property(name="style", type=StringType)
datastyle_SecondsType.attributes={datastyle_SecondsType_style, datastyle_SecondsType_decimalPlaces}

# datastyle_EmbeddedTextType class attributes and methods
datastyle_EmbeddedTextType_mixed: Property = Property(name="mixed", type=StringType)
datastyle_EmbeddedTextType_position: Property = Property(name="position", type=StringType)
datastyle_EmbeddedTextType.attributes={datastyle_EmbeddedTextType_mixed, datastyle_EmbeddedTextType_position}

# datastyle_FractionType class attributes and methods
datastyle_FractionType_denominatorValue: Property = Property(name="denominatorValue", type=StringType)
datastyle_FractionType_grouping: Property = Property(name="grouping", type=StringType)
datastyle_FractionType_minDenominatorDigits: Property = Property(name="minDenominatorDigits", type=StringType)
datastyle_FractionType_minIntegerDigits: Property = Property(name="minIntegerDigits", type=StringType)
datastyle_FractionType_minNumeratorDigits: Property = Property(name="minNumeratorDigits", type=StringType)
datastyle_FractionType.attributes={datastyle_FractionType_grouping, datastyle_FractionType_minDenominatorDigits, datastyle_FractionType_denominatorValue, datastyle_FractionType_minIntegerDigits, datastyle_FractionType_minNumeratorDigits}

# datastyle_NumberStyleType class attributes and methods
datastyle_NumberStyleType_anyNumberGroup: Property = Property(name="anyNumberGroup", type=StringType)
datastyle_NumberStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_NumberStyleType_text: Property = Property(name="text", type=StringType)
datastyle_NumberStyleType_language: Property = Property(name="language", type=StringType)
datastyle_NumberStyleType_name: Property = Property(name="name", type=StringType)
datastyle_NumberStyleType_title: Property = Property(name="title", type=StringType)
datastyle_NumberStyleType_country: Property = Property(name="country", type=StringType)
datastyle_NumberStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_NumberStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_NumberStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_NumberStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_NumberStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_NumberStyleType.attributes={datastyle_NumberStyleType_transliterationCountry, datastyle_NumberStyleType_language, datastyle_NumberStyleType_transliterationStyle, datastyle_NumberStyleType_anyNumberGroup, datastyle_NumberStyleType_text, datastyle_NumberStyleType_transliterationFormat, datastyle_NumberStyleType_transliterationLanguage, datastyle_NumberStyleType_name, datastyle_NumberStyleType_text1, datastyle_NumberStyleType_title, datastyle_NumberStyleType_country, datastyle_NumberStyleType_volatile}

# datastyle_EObject class attributes and methods

# datastyle_PercentageStyleType class attributes and methods
datastyle_PercentageStyleType_text: Property = Property(name="text", type=StringType)
datastyle_PercentageStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_PercentageStyleType_language: Property = Property(name="language", type=StringType)
datastyle_PercentageStyleType_name: Property = Property(name="name", type=StringType)
datastyle_PercentageStyleType_title: Property = Property(name="title", type=StringType)
datastyle_PercentageStyleType_country: Property = Property(name="country", type=StringType)
datastyle_PercentageStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_PercentageStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_PercentageStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_PercentageStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_PercentageStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_PercentageStyleType.attributes={datastyle_PercentageStyleType_country, datastyle_PercentageStyleType_transliterationFormat, datastyle_PercentageStyleType_title, datastyle_PercentageStyleType_language, datastyle_PercentageStyleType_transliterationLanguage, datastyle_PercentageStyleType_text, datastyle_PercentageStyleType_transliterationCountry, datastyle_PercentageStyleType_volatile, datastyle_PercentageStyleType_transliterationStyle, datastyle_PercentageStyleType_text1, datastyle_PercentageStyleType_name}

# datastyle_ScientificNumberType class attributes and methods
datastyle_ScientificNumberType_grouping: Property = Property(name="grouping", type=StringType)
datastyle_ScientificNumberType_minExponentDigits: Property = Property(name="minExponentDigits", type=StringType)
datastyle_ScientificNumberType_minIntegerDigits: Property = Property(name="minIntegerDigits", type=StringType)
datastyle_ScientificNumberType_decimalPlaces: Property = Property(name="decimalPlaces", type=StringType)
datastyle_ScientificNumberType.attributes={datastyle_ScientificNumberType_grouping, datastyle_ScientificNumberType_minExponentDigits, datastyle_ScientificNumberType_minIntegerDigits, datastyle_ScientificNumberType_decimalPlaces}

# datastyle_TextContentType class attributes and methods

# datastyle_TextStyleType class attributes and methods
datastyle_TextStyleType_group: Property = Property(name="group", type=StringType)
datastyle_TextStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_TextStyleType_text: Property = Property(name="text", type=StringType)
datastyle_TextStyleType_language: Property = Property(name="language", type=StringType)
datastyle_TextStyleType_name: Property = Property(name="name", type=StringType)
datastyle_TextStyleType_title: Property = Property(name="title", type=StringType)
datastyle_TextStyleType_country: Property = Property(name="country", type=StringType)
datastyle_TextStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_TextStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_TextStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_TextStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_TextStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_TextStyleType.attributes={datastyle_TextStyleType_text1, datastyle_TextStyleType_volatile, datastyle_TextStyleType_transliterationCountry, datastyle_TextStyleType_text, datastyle_TextStyleType_transliterationLanguage, datastyle_TextStyleType_country, datastyle_TextStyleType_name, datastyle_TextStyleType_title, datastyle_TextStyleType_language, datastyle_TextStyleType_transliterationStyle, datastyle_TextStyleType_group, datastyle_TextStyleType_transliterationFormat}

# datastyle_TimeStyleType class attributes and methods
datastyle_TimeStyleType_group: Property = Property(name="group", type=StringType)
datastyle_TimeStyleType_text: Property = Property(name="text", type=StringType)
datastyle_TimeStyleType_country: Property = Property(name="country", type=StringType)
datastyle_TimeStyleType_text1: Property = Property(name="text1", type=StringType)
datastyle_TimeStyleType_title: Property = Property(name="title", type=StringType)
datastyle_TimeStyleType_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_TimeStyleType_formatSource: Property = Property(name="formatSource", type=StringType)
datastyle_TimeStyleType_language: Property = Property(name="language", type=StringType)
datastyle_TimeStyleType_name: Property = Property(name="name", type=StringType)
datastyle_TimeStyleType_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_TimeStyleType_truncateOnOverflow: Property = Property(name="truncateOnOverflow", type=StringType)
datastyle_TimeStyleType_volatile: Property = Property(name="volatile", type=StringType)
datastyle_TimeStyleType_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_TimeStyleType_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_TimeStyleType.attributes={datastyle_TimeStyleType_transliterationCountry, datastyle_TimeStyleType_transliterationLanguage, datastyle_TimeStyleType_text, datastyle_TimeStyleType_country, datastyle_TimeStyleType_transliterationStyle, datastyle_TimeStyleType_transliterationFormat, datastyle_TimeStyleType_formatSource, datastyle_TimeStyleType_language, datastyle_TimeStyleType_name, datastyle_TimeStyleType_truncateOnOverflow, datastyle_TimeStyleType_title, datastyle_TimeStyleType_volatile, datastyle_TimeStyleType_group, datastyle_TimeStyleType_text1}

# datastyle_DocumentRoot class attributes and methods
datastyle_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
datastyle_DocumentRoot_text: Property = Property(name="text", type=StringType)
datastyle_DocumentRoot_calendar: Property = Property(name="calendar", type=StringType)
datastyle_DocumentRoot_automaticOrder: Property = Property(name="automaticOrder", type=StringType)
datastyle_DocumentRoot_country: Property = Property(name="country", type=StringType)
datastyle_DocumentRoot_decimalPlaces: Property = Property(name="decimalPlaces", type=StringType)
datastyle_DocumentRoot_decimalReplacement: Property = Property(name="decimalReplacement", type=StringType)
datastyle_DocumentRoot_denominatorValue: Property = Property(name="denominatorValue", type=StringType)
datastyle_DocumentRoot_displayFactor: Property = Property(name="displayFactor", type=StringType)
datastyle_DocumentRoot_formatSource: Property = Property(name="formatSource", type=StringType)
datastyle_DocumentRoot_grouping: Property = Property(name="grouping", type=StringType)
datastyle_DocumentRoot_language: Property = Property(name="language", type=StringType)
datastyle_DocumentRoot_minDenominatorDigits: Property = Property(name="minDenominatorDigits", type=StringType)
datastyle_DocumentRoot_minExponentDigits: Property = Property(name="minExponentDigits", type=StringType)
datastyle_DocumentRoot_minIntegerDigits: Property = Property(name="minIntegerDigits", type=StringType)
datastyle_DocumentRoot_minNumeratorDigits: Property = Property(name="minNumeratorDigits", type=StringType)
datastyle_DocumentRoot_transliterationFormat: Property = Property(name="transliterationFormat", type=StringType)
datastyle_DocumentRoot_position: Property = Property(name="position", type=StringType)
datastyle_DocumentRoot_possessiveForm: Property = Property(name="possessiveForm", type=StringType)
datastyle_DocumentRoot_style: Property = Property(name="style", type=StringType)
datastyle_DocumentRoot_textual: Property = Property(name="textual", type=StringType)
datastyle_DocumentRoot_title: Property = Property(name="title", type=StringType)
datastyle_DocumentRoot_transliterationCountry: Property = Property(name="transliterationCountry", type=StringType)
datastyle_DocumentRoot_transliterationLanguage: Property = Property(name="transliterationLanguage", type=StringType)
datastyle_DocumentRoot_transliterationStyle: Property = Property(name="transliterationStyle", type=StringType)
datastyle_DocumentRoot_truncateOnOverflow: Property = Property(name="truncateOnOverflow", type=StringType)
datastyle_DocumentRoot.attributes={datastyle_DocumentRoot_calendar, datastyle_DocumentRoot_minIntegerDigits, datastyle_DocumentRoot_possessiveForm, datastyle_DocumentRoot_minExponentDigits, datastyle_DocumentRoot_mixed, datastyle_DocumentRoot_transliterationCountry, datastyle_DocumentRoot_style, datastyle_DocumentRoot_truncateOnOverflow, datastyle_DocumentRoot_denominatorValue, datastyle_DocumentRoot_decimalReplacement, datastyle_DocumentRoot_minNumeratorDigits, datastyle_DocumentRoot_title, datastyle_DocumentRoot_transliterationStyle, datastyle_DocumentRoot_textual, datastyle_DocumentRoot_position, datastyle_DocumentRoot_automaticOrder, datastyle_DocumentRoot_country, datastyle_DocumentRoot_text, datastyle_DocumentRoot_decimalPlaces, datastyle_DocumentRoot_formatSource, datastyle_DocumentRoot_transliterationFormat, datastyle_DocumentRoot_language, datastyle_DocumentRoot_displayFactor, datastyle_DocumentRoot_transliterationLanguage, datastyle_DocumentRoot_minDenominatorDigits, datastyle_DocumentRoot_grouping}

# datastyle_EStringToStringMapEntry class attributes and methods

# Relationships
textProperties0: BinaryAssociation = BinaryAssociation(
    name="textProperties0",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent", type=datastyle_BooleanStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_BooleanStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolean1: BinaryAssociation = BinaryAssociation(
    name="boolean1",
    ends={
        Property(name="datastyle_BooleanType", type=datastyle_BooleanStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_BooleanStyleType2", type=datastyle_BooleanType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map3: BinaryAssociation = BinaryAssociation(
    name="map3",
    ends={
        Property(name="datastyle_MapType", type=datastyle_BooleanStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_BooleanStyleType4", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textProperties5: BinaryAssociation = BinaryAssociation(
    name="textProperties5",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent6", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number7: BinaryAssociation = BinaryAssociation(
    name="number7",
    ends={
        Property(name="datastyle_NumberType", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType8", type=datastyle_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currencySymbol9: BinaryAssociation = BinaryAssociation(
    name="currencySymbol9",
    ends={
        Property(name="datastyle_CurrencySymbolType", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType10", type=datastyle_CurrencySymbolType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currencySymbol111: BinaryAssociation = BinaryAssociation(
    name="currencySymbol111",
    ends={
        Property(name="datastyle_CurrencySymbolType13", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType12", type=datastyle_CurrencySymbolType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number114: BinaryAssociation = BinaryAssociation(
    name="number114",
    ends={
        Property(name="datastyle_NumberType16", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType15", type=datastyle_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map17: BinaryAssociation = BinaryAssociation(
    name="map17",
    ends={
        Property(name="datastyle_MapType19", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_CurrencyStyleType18", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textProperties20: BinaryAssociation = BinaryAssociation(
    name="textProperties20",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent21", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
year26: BinaryAssociation = BinaryAssociation(
    name="year26",
    ends={
        Property(name="datastyle_YearType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType27", type=datastyle_YearType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
era28: BinaryAssociation = BinaryAssociation(
    name="era28",
    ends={
        Property(name="datastyle_EraType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType29", type=datastyle_EraType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
day22: BinaryAssociation = BinaryAssociation(
    name="day22",
    ends={
        Property(name="datastyle_DayType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType23", type=datastyle_DayType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
month24: BinaryAssociation = BinaryAssociation(
    name="month24",
    ends={
        Property(name="datastyle_MonthType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType25", type=datastyle_MonthType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
weekOfYear32: BinaryAssociation = BinaryAssociation(
    name="weekOfYear32",
    ends={
        Property(name="datastyle_WeekOfYearType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType33", type=datastyle_WeekOfYearType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quarter34: BinaryAssociation = BinaryAssociation(
    name="quarter34",
    ends={
        Property(name="datastyle_QuarterType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType35", type=datastyle_QuarterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hours36: BinaryAssociation = BinaryAssociation(
    name="hours36",
    ends={
        Property(name="datastyle_HoursType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType37", type=datastyle_HoursType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dayOfWeek30: BinaryAssociation = BinaryAssociation(
    name="dayOfWeek30",
    ends={
        Property(name="datastyle_DayOfWeekType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType31", type=datastyle_DayOfWeekType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
amPm38: BinaryAssociation = BinaryAssociation(
    name="amPm38",
    ends={
        Property(name="datastyle_AmPmType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType39", type=datastyle_AmPmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map44: BinaryAssociation = BinaryAssociation(
    name="map44",
    ends={
        Property(name="datastyle_MapType46", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType45", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minutes40: BinaryAssociation = BinaryAssociation(
    name="minutes40",
    ends={
        Property(name="datastyle_MinutesType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType41", type=datastyle_MinutesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seconds42: BinaryAssociation = BinaryAssociation(
    name="seconds42",
    ends={
        Property(name="datastyle_SecondsType", type=datastyle_DateStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DateStyleType43", type=datastyle_SecondsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anyNumber49: BinaryAssociation = BinaryAssociation(
    name="anyNumber49",
    ends={
        Property(name="datastyle_EObject", type=datastyle_NumberStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_NumberStyleType50", type=datastyle_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textProperties47: BinaryAssociation = BinaryAssociation(
    name="textProperties47",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent48", type=datastyle_NumberStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_NumberStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map51: BinaryAssociation = BinaryAssociation(
    name="map51",
    ends={
        Property(name="datastyle_MapType53", type=datastyle_NumberStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_NumberStyleType52", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embeddedText54: BinaryAssociation = BinaryAssociation(
    name="embeddedText54",
    ends={
        Property(name="datastyle_EmbeddedTextType", type=datastyle_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_NumberType55", type=datastyle_EmbeddedTextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number58: BinaryAssociation = BinaryAssociation(
    name="number58",
    ends={
        Property(name="datastyle_NumberType60", type=datastyle_PercentageStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_PercentageStyleType59", type=datastyle_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textProperties56: BinaryAssociation = BinaryAssociation(
    name="textProperties56",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent57", type=datastyle_PercentageStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_PercentageStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map61: BinaryAssociation = BinaryAssociation(
    name="map61",
    ends={
        Property(name="datastyle_MapType63", type=datastyle_PercentageStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_PercentageStyleType62", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textContent66: BinaryAssociation = BinaryAssociation(
    name="textContent66",
    ends={
        Property(name="datastyle_TextContentType", type=datastyle_TextStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TextStyleType67", type=datastyle_TextContentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textProperties64: BinaryAssociation = BinaryAssociation(
    name="textProperties64",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent65", type=datastyle_TextStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TextStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map68: BinaryAssociation = BinaryAssociation(
    name="map68",
    ends={
        Property(name="datastyle_MapType70", type=datastyle_TextStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TextStyleType69", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textProperties71: BinaryAssociation = BinaryAssociation(
    name="textProperties71",
    ends={
        Property(name="datastyle_StyleTextPropertiesContent72", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType", type=datastyle_StyleTextPropertiesContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
amPm76: BinaryAssociation = BinaryAssociation(
    name="amPm76",
    ends={
        Property(name="datastyle_AmPmType78", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType77", type=datastyle_AmPmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minutes79: BinaryAssociation = BinaryAssociation(
    name="minutes79",
    ends={
        Property(name="datastyle_MinutesType81", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType80", type=datastyle_MinutesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hours73: BinaryAssociation = BinaryAssociation(
    name="hours73",
    ends={
        Property(name="datastyle_HoursType75", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType74", type=datastyle_HoursType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map85: BinaryAssociation = BinaryAssociation(
    name="map85",
    ends={
        Property(name="datastyle_MapType87", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType86", type=datastyle_MapType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seconds82: BinaryAssociation = BinaryAssociation(
    name="seconds82",
    ends={
        Property(name="datastyle_SecondsType84", type=datastyle_TimeStyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_TimeStyleType83", type=datastyle_SecondsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap88: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap88",
    ends={
        Property(name="datastyle_EStringToStringMapEntry", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot", type=datastyle_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation89: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation89",
    ends={
        Property(name="datastyle_EStringToStringMapEntry91", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot90", type=datastyle_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
amPm92: BinaryAssociation = BinaryAssociation(
    name="amPm92",
    ends={
        Property(name="datastyle_AmPmType94", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot93", type=datastyle_AmPmType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boolean95: BinaryAssociation = BinaryAssociation(
    name="boolean95",
    ends={
        Property(name="datastyle_BooleanType97", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot96", type=datastyle_BooleanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanStyle98: BinaryAssociation = BinaryAssociation(
    name="booleanStyle98",
    ends={
        Property(name="datastyle_BooleanStyleType100", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot99", type=datastyle_BooleanStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currencyStyle101: BinaryAssociation = BinaryAssociation(
    name="currencyStyle101",
    ends={
        Property(name="datastyle_CurrencyStyleType103", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot102", type=datastyle_CurrencyStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currencySymbol104: BinaryAssociation = BinaryAssociation(
    name="currencySymbol104",
    ends={
        Property(name="datastyle_CurrencySymbolType106", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot105", type=datastyle_CurrencySymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dateStyle107: BinaryAssociation = BinaryAssociation(
    name="dateStyle107",
    ends={
        Property(name="datastyle_DateStyleType109", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot108", type=datastyle_DateStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
day110: BinaryAssociation = BinaryAssociation(
    name="day110",
    ends={
        Property(name="datastyle_DayType112", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot111", type=datastyle_DayType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dayOfWeek113: BinaryAssociation = BinaryAssociation(
    name="dayOfWeek113",
    ends={
        Property(name="datastyle_DayOfWeekType115", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot114", type=datastyle_DayOfWeekType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embeddedText116: BinaryAssociation = BinaryAssociation(
    name="embeddedText116",
    ends={
        Property(name="datastyle_EmbeddedTextType118", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot117", type=datastyle_EmbeddedTextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
era119: BinaryAssociation = BinaryAssociation(
    name="era119",
    ends={
        Property(name="datastyle_EraType121", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot120", type=datastyle_EraType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fraction122: BinaryAssociation = BinaryAssociation(
    name="fraction122",
    ends={
        Property(name="datastyle_FractionType", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot123", type=datastyle_FractionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hours124: BinaryAssociation = BinaryAssociation(
    name="hours124",
    ends={
        Property(name="datastyle_HoursType126", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot125", type=datastyle_HoursType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minutes127: BinaryAssociation = BinaryAssociation(
    name="minutes127",
    ends={
        Property(name="datastyle_MinutesType129", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot128", type=datastyle_MinutesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
month130: BinaryAssociation = BinaryAssociation(
    name="month130",
    ends={
        Property(name="datastyle_MonthType132", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot131", type=datastyle_MonthType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number133: BinaryAssociation = BinaryAssociation(
    name="number133",
    ends={
        Property(name="datastyle_NumberType135", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot134", type=datastyle_NumberType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
numberStyle136: BinaryAssociation = BinaryAssociation(
    name="numberStyle136",
    ends={
        Property(name="datastyle_NumberStyleType138", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot137", type=datastyle_NumberStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
percentageStyle139: BinaryAssociation = BinaryAssociation(
    name="percentageStyle139",
    ends={
        Property(name="datastyle_PercentageStyleType141", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot140", type=datastyle_PercentageStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quarter142: BinaryAssociation = BinaryAssociation(
    name="quarter142",
    ends={
        Property(name="datastyle_QuarterType144", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot143", type=datastyle_QuarterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scientificNumber145: BinaryAssociation = BinaryAssociation(
    name="scientificNumber145",
    ends={
        Property(name="datastyle_ScientificNumberType", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot146", type=datastyle_ScientificNumberType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seconds147: BinaryAssociation = BinaryAssociation(
    name="seconds147",
    ends={
        Property(name="datastyle_SecondsType149", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot148", type=datastyle_SecondsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textContent150: BinaryAssociation = BinaryAssociation(
    name="textContent150",
    ends={
        Property(name="datastyle_TextContentType152", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot151", type=datastyle_TextContentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textStyle153: BinaryAssociation = BinaryAssociation(
    name="textStyle153",
    ends={
        Property(name="datastyle_TextStyleType155", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot154", type=datastyle_TextStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeStyle156: BinaryAssociation = BinaryAssociation(
    name="timeStyle156",
    ends={
        Property(name="datastyle_TimeStyleType158", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot157", type=datastyle_TimeStyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
weekOfYear159: BinaryAssociation = BinaryAssociation(
    name="weekOfYear159",
    ends={
        Property(name="datastyle_WeekOfYearType161", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot160", type=datastyle_WeekOfYearType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
year162: BinaryAssociation = BinaryAssociation(
    name="year162",
    ends={
        Property(name="datastyle_YearType164", type=datastyle_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="datastyle_DocumentRoot163", type=datastyle_YearType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="datastyle",
    types={datastyle_BooleanStyleType, datastyle_StyleTextPropertiesContent, datastyle_BooleanType, datastyle_AmPmType, datastyle_MapType, datastyle_NumberType, datastyle_CurrencySymbolType, datastyle_CurrencyStyleType, datastyle_DateStyleType, datastyle_YearType, datastyle_EraType, datastyle_DayType, datastyle_MonthType, datastyle_WeekOfYearType, datastyle_QuarterType, datastyle_HoursType, datastyle_DayOfWeekType, datastyle_MinutesType, datastyle_SecondsType, datastyle_EmbeddedTextType, datastyle_FractionType, datastyle_NumberStyleType, datastyle_EObject, datastyle_PercentageStyleType, datastyle_ScientificNumberType, datastyle_TextContentType, datastyle_TextStyleType, datastyle_TimeStyleType, datastyle_DocumentRoot, datastyle_EStringToStringMapEntry, CalendarTypeMember2, CalendarTypeMember3, CalendarTypeMember4, CalendarTypeMember1, CalendarTypeMember6, CalendarTypeMember7, CalendarTypeMember8, CalendarTypeMember5, FormatSourceType, StyleType, TransliterationStyleType},
    associations={textProperties0, boolean1, map3, textProperties5, number7, currencySymbol9, currencySymbol111, number114, map17, textProperties20, year26, era28, day22, month24, weekOfYear32, quarter34, hours36, dayOfWeek30, amPm38, map44, minutes40, seconds42, anyNumber49, textProperties47, map51, embeddedText54, number58, textProperties56, map61, textContent66, textProperties64, map68, textProperties71, amPm76, minutes79, hours73, map85, seconds82, xMLNSPrefixMap88, xSISchemaLocation89, amPm92, boolean95, booleanStyle98, currencyStyle101, currencySymbol104, dateStyle107, day110, dayOfWeek113, embeddedText116, era119, fraction122, hours124, minutes127, month130, number133, numberStyle136, percentageStyle139, quarter142, scientificNumber145, seconds147, textContent150, textStyle153, timeStyle156, weekOfYear159, year162},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)