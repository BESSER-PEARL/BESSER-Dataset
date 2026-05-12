





import java.util.List;
import java.util.ArrayList;

public class datastyle_DocumentRoot  {

    private String position;
    private String country;
    private String transliterationCountry;
    private String text;
    private String minIntegerDigits;
    private String title;
    private String minNumeratorDigits;
    private String transliterationStyle;
    private String textual;
    private String minExponentDigits;
    private String transliterationFormat;
    private String language;
    private String minDenominatorDigits;
    private String automaticOrder;
    private String calendar;
    private String decimalReplacement;
    private String formatSource;
    private String style;
    private String grouping;
    private String displayFactor;
    private String transliterationLanguage;
    private String decimalPlaces;
    private String possessiveForm;
    private String denominatorValue;
    private String truncateOnOverflow;
    private String mixed;





    private List<datastyle_NumberStyleType> datastyle_numberstyletypes;




    private List<datastyle_CurrencyStyleType> datastyle_currencystyletypes;




    private List<datastyle_SecondsType> datastyle_secondstypes;




    private List<datastyle_TimeStyleType> datastyle_timestyletypes;




    private List<datastyle_ScientificNumberType> datastyle_scientificnumbertypes;




    private List<datastyle_DateStyleType> datastyle_datestyletypes;




    private List<datastyle_QuarterType> datastyle_quartertypes;




    private List<datastyle_NumberType> datastyle_numbertypes;




    private List<datastyle_BooleanStyleType> datastyle_booleanstyletypes;




    private List<datastyle_CurrencySymbolType> datastyle_currencysymboltypes;




    private List<datastyle_HoursType> datastyle_hourstypes;




    private List<datastyle_AmPmType> datastyle_ampmtypes;




    private List<datastyle_EraType> datastyle_eratypes;




    private List<datastyle_TextContentType> datastyle_textcontenttypes;




    private List<datastyle_EmbeddedTextType> datastyle_embeddedtexttypes;




    private List<datastyle_PercentageStyleType> datastyle_percentagestyletypes;




    private List<datastyle_DayType> datastyle_daytypes;




    private List<datastyle_MonthType> datastyle_monthtypes;




    private List<datastyle_BooleanType> datastyle_booleantypes;




    private List<datastyle_FractionType> datastyle_fractiontypes;




    private List<datastyle_DayOfWeekType> datastyle_dayofweektypes;




    private List<datastyle_WeekOfYearType> datastyle_weekofyeartypes;




    private List<datastyle_YearType> datastyle_yeartypes;




    private List<datastyle_MinutesType> datastyle_minutestypes;




    private List<datastyle_TextStyleType> datastyle_textstyletypes;


    public datastyle_DocumentRoot(
        String position,        String country,        String transliterationCountry,        String text,        String minIntegerDigits,        String title,        String minNumeratorDigits,        String transliterationStyle,        String textual,        String minExponentDigits,        String transliterationFormat,        String language,        String minDenominatorDigits,        String automaticOrder,        String calendar,        String decimalReplacement,        String formatSource,        String style,        String grouping,        String displayFactor,        String transliterationLanguage,        String decimalPlaces,        String possessiveForm,        String denominatorValue,        String truncateOnOverflow,        String mixed    ) {
        this.position = position;
        this.country = country;
        this.transliterationCountry = transliterationCountry;
        this.text = text;
        this.minIntegerDigits = minIntegerDigits;
        this.title = title;
        this.minNumeratorDigits = minNumeratorDigits;
        this.transliterationStyle = transliterationStyle;
        this.textual = textual;
        this.minExponentDigits = minExponentDigits;
        this.transliterationFormat = transliterationFormat;
        this.language = language;
        this.minDenominatorDigits = minDenominatorDigits;
        this.automaticOrder = automaticOrder;
        this.calendar = calendar;
        this.decimalReplacement = decimalReplacement;
        this.formatSource = formatSource;
        this.style = style;
        this.grouping = grouping;
        this.displayFactor = displayFactor;
        this.transliterationLanguage = transliterationLanguage;
        this.decimalPlaces = decimalPlaces;
        this.possessiveForm = possessiveForm;
        this.denominatorValue = denominatorValue;
        this.truncateOnOverflow = truncateOnOverflow;
        this.mixed = mixed;
        this.datastyle_numberstyletypes = new ArrayList<>();
        this.datastyle_currencystyletypes = new ArrayList<>();
        this.datastyle_secondstypes = new ArrayList<>();
        this.datastyle_timestyletypes = new ArrayList<>();
        this.datastyle_scientificnumbertypes = new ArrayList<>();
        this.datastyle_datestyletypes = new ArrayList<>();
        this.datastyle_quartertypes = new ArrayList<>();
        this.datastyle_numbertypes = new ArrayList<>();
        this.datastyle_booleanstyletypes = new ArrayList<>();
        this.datastyle_currencysymboltypes = new ArrayList<>();
        this.datastyle_hourstypes = new ArrayList<>();
        this.datastyle_ampmtypes = new ArrayList<>();
        this.datastyle_eratypes = new ArrayList<>();
        this.datastyle_textcontenttypes = new ArrayList<>();
        this.datastyle_embeddedtexttypes = new ArrayList<>();
        this.datastyle_percentagestyletypes = new ArrayList<>();
        this.datastyle_daytypes = new ArrayList<>();
        this.datastyle_monthtypes = new ArrayList<>();
        this.datastyle_booleantypes = new ArrayList<>();
        this.datastyle_fractiontypes = new ArrayList<>();
        this.datastyle_dayofweektypes = new ArrayList<>();
        this.datastyle_weekofyeartypes = new ArrayList<>();
        this.datastyle_yeartypes = new ArrayList<>();
        this.datastyle_minutestypes = new ArrayList<>();
        this.datastyle_textstyletypes = new ArrayList<>();
    }

    public datastyle_DocumentRoot(
        String position,        String country,        String transliterationCountry,        String text,        String minIntegerDigits,        String title,        String minNumeratorDigits,        String transliterationStyle,        String textual,        String minExponentDigits,        String transliterationFormat,        String language,        String minDenominatorDigits,        String automaticOrder,        String calendar,        String decimalReplacement,        String formatSource,        String style,        String grouping,        String displayFactor,        String transliterationLanguage,        String decimalPlaces,        String possessiveForm,        String denominatorValue,        String truncateOnOverflow,        String mixed        ArrayList<datastyle_NumberStyleType> datastyle_numberstyletypes,        ArrayList<datastyle_CurrencyStyleType> datastyle_currencystyletypes,        ArrayList<datastyle_SecondsType> datastyle_secondstypes,        ArrayList<datastyle_TimeStyleType> datastyle_timestyletypes,        ArrayList<datastyle_ScientificNumberType> datastyle_scientificnumbertypes,        ArrayList<datastyle_DateStyleType> datastyle_datestyletypes,        ArrayList<datastyle_QuarterType> datastyle_quartertypes,        ArrayList<datastyle_NumberType> datastyle_numbertypes,        ArrayList<datastyle_BooleanStyleType> datastyle_booleanstyletypes,        ArrayList<datastyle_CurrencySymbolType> datastyle_currencysymboltypes,        ArrayList<datastyle_HoursType> datastyle_hourstypes,        ArrayList<datastyle_AmPmType> datastyle_ampmtypes,        ArrayList<datastyle_EraType> datastyle_eratypes,        ArrayList<datastyle_TextContentType> datastyle_textcontenttypes,        ArrayList<datastyle_EmbeddedTextType> datastyle_embeddedtexttypes,        ArrayList<datastyle_PercentageStyleType> datastyle_percentagestyletypes,        ArrayList<datastyle_DayType> datastyle_daytypes,        ArrayList<datastyle_MonthType> datastyle_monthtypes,        ArrayList<datastyle_BooleanType> datastyle_booleantypes,        ArrayList<datastyle_FractionType> datastyle_fractiontypes,        ArrayList<datastyle_DayOfWeekType> datastyle_dayofweektypes,        ArrayList<datastyle_WeekOfYearType> datastyle_weekofyeartypes,        ArrayList<datastyle_YearType> datastyle_yeartypes,        ArrayList<datastyle_MinutesType> datastyle_minutestypes,        ArrayList<datastyle_TextStyleType> datastyle_textstyletypes    ) {
        this.position = position;
        this.country = country;
        this.transliterationCountry = transliterationCountry;
        this.text = text;
        this.minIntegerDigits = minIntegerDigits;
        this.title = title;
        this.minNumeratorDigits = minNumeratorDigits;
        this.transliterationStyle = transliterationStyle;
        this.textual = textual;
        this.minExponentDigits = minExponentDigits;
        this.transliterationFormat = transliterationFormat;
        this.language = language;
        this.minDenominatorDigits = minDenominatorDigits;
        this.automaticOrder = automaticOrder;
        this.calendar = calendar;
        this.decimalReplacement = decimalReplacement;
        this.formatSource = formatSource;
        this.style = style;
        this.grouping = grouping;
        this.displayFactor = displayFactor;
        this.transliterationLanguage = transliterationLanguage;
        this.decimalPlaces = decimalPlaces;
        this.possessiveForm = possessiveForm;
        this.denominatorValue = denominatorValue;
        this.truncateOnOverflow = truncateOnOverflow;
        this.mixed = mixed;
        this.datastyle_numberstyletypes = datastyle_numberstyletypes;
        this.datastyle_currencystyletypes = datastyle_currencystyletypes;
        this.datastyle_secondstypes = datastyle_secondstypes;
        this.datastyle_timestyletypes = datastyle_timestyletypes;
        this.datastyle_scientificnumbertypes = datastyle_scientificnumbertypes;
        this.datastyle_datestyletypes = datastyle_datestyletypes;
        this.datastyle_quartertypes = datastyle_quartertypes;
        this.datastyle_numbertypes = datastyle_numbertypes;
        this.datastyle_booleanstyletypes = datastyle_booleanstyletypes;
        this.datastyle_currencysymboltypes = datastyle_currencysymboltypes;
        this.datastyle_hourstypes = datastyle_hourstypes;
        this.datastyle_ampmtypes = datastyle_ampmtypes;
        this.datastyle_eratypes = datastyle_eratypes;
        this.datastyle_textcontenttypes = datastyle_textcontenttypes;
        this.datastyle_embeddedtexttypes = datastyle_embeddedtexttypes;
        this.datastyle_percentagestyletypes = datastyle_percentagestyletypes;
        this.datastyle_daytypes = datastyle_daytypes;
        this.datastyle_monthtypes = datastyle_monthtypes;
        this.datastyle_booleantypes = datastyle_booleantypes;
        this.datastyle_fractiontypes = datastyle_fractiontypes;
        this.datastyle_dayofweektypes = datastyle_dayofweektypes;
        this.datastyle_weekofyeartypes = datastyle_weekofyeartypes;
        this.datastyle_yeartypes = datastyle_yeartypes;
        this.datastyle_minutestypes = datastyle_minutestypes;
        this.datastyle_textstyletypes = datastyle_textstyletypes;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getMinintegerdigits() {
        return minIntegerDigits;
    }

    public void setMinintegerdigits(String minIntegerDigits) {
        this.minIntegerDigits = minIntegerDigits;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getMinnumeratordigits() {
        return minNumeratorDigits;
    }

    public void setMinnumeratordigits(String minNumeratorDigits) {
        this.minNumeratorDigits = minNumeratorDigits;
    }
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getTextual() {
        return textual;
    }

    public void setTextual(String textual) {
        this.textual = textual;
    }
    public String getMinexponentdigits() {
        return minExponentDigits;
    }

    public void setMinexponentdigits(String minExponentDigits) {
        this.minExponentDigits = minExponentDigits;
    }
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getMindenominatordigits() {
        return minDenominatorDigits;
    }

    public void setMindenominatordigits(String minDenominatorDigits) {
        this.minDenominatorDigits = minDenominatorDigits;
    }
    public String getAutomaticorder() {
        return automaticOrder;
    }

    public void setAutomaticorder(String automaticOrder) {
        this.automaticOrder = automaticOrder;
    }
    public String getCalendar() {
        return calendar;
    }

    public void setCalendar(String calendar) {
        this.calendar = calendar;
    }
    public String getDecimalreplacement() {
        return decimalReplacement;
    }

    public void setDecimalreplacement(String decimalReplacement) {
        this.decimalReplacement = decimalReplacement;
    }
    public String getFormatsource() {
        return formatSource;
    }

    public void setFormatsource(String formatSource) {
        this.formatSource = formatSource;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getGrouping() {
        return grouping;
    }

    public void setGrouping(String grouping) {
        this.grouping = grouping;
    }
    public String getDisplayfactor() {
        return displayFactor;
    }

    public void setDisplayfactor(String displayFactor) {
        this.displayFactor = displayFactor;
    }
    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
    }
    public String getDecimalplaces() {
        return decimalPlaces;
    }

    public void setDecimalplaces(String decimalPlaces) {
        this.decimalPlaces = decimalPlaces;
    }
    public String getPossessiveform() {
        return possessiveForm;
    }

    public void setPossessiveform(String possessiveForm) {
        this.possessiveForm = possessiveForm;
    }
    public String getDenominatorvalue() {
        return denominatorValue;
    }

    public void setDenominatorvalue(String denominatorValue) {
        this.denominatorValue = denominatorValue;
    }
    public String getTruncateonoverflow() {
        return truncateOnOverflow;
    }

    public void setTruncateonoverflow(String truncateOnOverflow) {
        this.truncateOnOverflow = truncateOnOverflow;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<datastyle_NumberStyleType> getDatastyle_numberstyletypes() {
        return datastyle_numberstyletypes;
    }

    public void addDatastyle_numberstyletype(Datastyle_numberstyletype datastyle_numberstyletype) {
        this.datastyle_numberstyletypes.add(datastyle_numberstyletype);
    }
    public List<datastyle_CurrencyStyleType> getDatastyle_currencystyletypes() {
        return datastyle_currencystyletypes;
    }

    public void addDatastyle_currencystyletype(Datastyle_currencystyletype datastyle_currencystyletype) {
        this.datastyle_currencystyletypes.add(datastyle_currencystyletype);
    }
    public List<datastyle_SecondsType> getDatastyle_secondstypes() {
        return datastyle_secondstypes;
    }

    public void addDatastyle_secondstype(Datastyle_secondstype datastyle_secondstype) {
        this.datastyle_secondstypes.add(datastyle_secondstype);
    }
    public List<datastyle_TimeStyleType> getDatastyle_timestyletypes() {
        return datastyle_timestyletypes;
    }

    public void addDatastyle_timestyletype(Datastyle_timestyletype datastyle_timestyletype) {
        this.datastyle_timestyletypes.add(datastyle_timestyletype);
    }
    public List<datastyle_ScientificNumberType> getDatastyle_scientificnumbertypes() {
        return datastyle_scientificnumbertypes;
    }

    public void addDatastyle_scientificnumbertype(Datastyle_scientificnumbertype datastyle_scientificnumbertype) {
        this.datastyle_scientificnumbertypes.add(datastyle_scientificnumbertype);
    }
    public List<datastyle_DateStyleType> getDatastyle_datestyletypes() {
        return datastyle_datestyletypes;
    }

    public void addDatastyle_datestyletype(Datastyle_datestyletype datastyle_datestyletype) {
        this.datastyle_datestyletypes.add(datastyle_datestyletype);
    }
    public List<datastyle_QuarterType> getDatastyle_quartertypes() {
        return datastyle_quartertypes;
    }

    public void addDatastyle_quartertype(Datastyle_quartertype datastyle_quartertype) {
        this.datastyle_quartertypes.add(datastyle_quartertype);
    }
    public List<datastyle_NumberType> getDatastyle_numbertypes() {
        return datastyle_numbertypes;
    }

    public void addDatastyle_numbertype(Datastyle_numbertype datastyle_numbertype) {
        this.datastyle_numbertypes.add(datastyle_numbertype);
    }
    public List<datastyle_BooleanStyleType> getDatastyle_booleanstyletypes() {
        return datastyle_booleanstyletypes;
    }

    public void addDatastyle_booleanstyletype(Datastyle_booleanstyletype datastyle_booleanstyletype) {
        this.datastyle_booleanstyletypes.add(datastyle_booleanstyletype);
    }
    public List<datastyle_CurrencySymbolType> getDatastyle_currencysymboltypes() {
        return datastyle_currencysymboltypes;
    }

    public void addDatastyle_currencysymboltype(Datastyle_currencysymboltype datastyle_currencysymboltype) {
        this.datastyle_currencysymboltypes.add(datastyle_currencysymboltype);
    }
    public List<datastyle_HoursType> getDatastyle_hourstypes() {
        return datastyle_hourstypes;
    }

    public void addDatastyle_hourstype(Datastyle_hourstype datastyle_hourstype) {
        this.datastyle_hourstypes.add(datastyle_hourstype);
    }
    public List<datastyle_AmPmType> getDatastyle_ampmtypes() {
        return datastyle_ampmtypes;
    }

    public void addDatastyle_ampmtype(Datastyle_ampmtype datastyle_ampmtype) {
        this.datastyle_ampmtypes.add(datastyle_ampmtype);
    }
    public List<datastyle_EraType> getDatastyle_eratypes() {
        return datastyle_eratypes;
    }

    public void addDatastyle_eratype(Datastyle_eratype datastyle_eratype) {
        this.datastyle_eratypes.add(datastyle_eratype);
    }
    public List<datastyle_TextContentType> getDatastyle_textcontenttypes() {
        return datastyle_textcontenttypes;
    }

    public void addDatastyle_textcontenttype(Datastyle_textcontenttype datastyle_textcontenttype) {
        this.datastyle_textcontenttypes.add(datastyle_textcontenttype);
    }
    public List<datastyle_EmbeddedTextType> getDatastyle_embeddedtexttypes() {
        return datastyle_embeddedtexttypes;
    }

    public void addDatastyle_embeddedtexttype(Datastyle_embeddedtexttype datastyle_embeddedtexttype) {
        this.datastyle_embeddedtexttypes.add(datastyle_embeddedtexttype);
    }
    public List<datastyle_PercentageStyleType> getDatastyle_percentagestyletypes() {
        return datastyle_percentagestyletypes;
    }

    public void addDatastyle_percentagestyletype(Datastyle_percentagestyletype datastyle_percentagestyletype) {
        this.datastyle_percentagestyletypes.add(datastyle_percentagestyletype);
    }
    public List<datastyle_DayType> getDatastyle_daytypes() {
        return datastyle_daytypes;
    }

    public void addDatastyle_daytype(Datastyle_daytype datastyle_daytype) {
        this.datastyle_daytypes.add(datastyle_daytype);
    }
    public List<datastyle_MonthType> getDatastyle_monthtypes() {
        return datastyle_monthtypes;
    }

    public void addDatastyle_monthtype(Datastyle_monthtype datastyle_monthtype) {
        this.datastyle_monthtypes.add(datastyle_monthtype);
    }
    public List<datastyle_BooleanType> getDatastyle_booleantypes() {
        return datastyle_booleantypes;
    }

    public void addDatastyle_booleantype(Datastyle_booleantype datastyle_booleantype) {
        this.datastyle_booleantypes.add(datastyle_booleantype);
    }
    public List<datastyle_FractionType> getDatastyle_fractiontypes() {
        return datastyle_fractiontypes;
    }

    public void addDatastyle_fractiontype(Datastyle_fractiontype datastyle_fractiontype) {
        this.datastyle_fractiontypes.add(datastyle_fractiontype);
    }
    public List<datastyle_DayOfWeekType> getDatastyle_dayofweektypes() {
        return datastyle_dayofweektypes;
    }

    public void addDatastyle_dayofweektype(Datastyle_dayofweektype datastyle_dayofweektype) {
        this.datastyle_dayofweektypes.add(datastyle_dayofweektype);
    }
    public List<datastyle_WeekOfYearType> getDatastyle_weekofyeartypes() {
        return datastyle_weekofyeartypes;
    }

    public void addDatastyle_weekofyeartype(Datastyle_weekofyeartype datastyle_weekofyeartype) {
        this.datastyle_weekofyeartypes.add(datastyle_weekofyeartype);
    }
    public List<datastyle_YearType> getDatastyle_yeartypes() {
        return datastyle_yeartypes;
    }

    public void addDatastyle_yeartype(Datastyle_yeartype datastyle_yeartype) {
        this.datastyle_yeartypes.add(datastyle_yeartype);
    }
    public List<datastyle_MinutesType> getDatastyle_minutestypes() {
        return datastyle_minutestypes;
    }

    public void addDatastyle_minutestype(Datastyle_minutestype datastyle_minutestype) {
        this.datastyle_minutestypes.add(datastyle_minutestype);
    }
    public List<datastyle_TextStyleType> getDatastyle_textstyletypes() {
        return datastyle_textstyletypes;
    }

    public void addDatastyle_textstyletype(Datastyle_textstyletype datastyle_textstyletype) {
        this.datastyle_textstyletypes.add(datastyle_textstyletype);
    }

}