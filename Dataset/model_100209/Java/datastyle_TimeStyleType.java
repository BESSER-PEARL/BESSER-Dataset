





import java.util.List;
import java.util.ArrayList;

public class datastyle_TimeStyleType  {

    private String text;
    private String title;
    private String language;
    private String text1;
    private String transliterationFormat;
    private String transliterationCountry;
    private String formatSource;
    private String country;
    private String transliterationLanguage;
    private String name;
    private String transliterationStyle;
    private String volatile;
    private String truncateOnOverflow;
    private String group;





    private List<datastyle_AmPmType> datastyle_ampmtypes;




    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;




    private List<datastyle_SecondsType> datastyle_secondstypes;




    private List<datastyle_MinutesType> datastyle_minutestypes;




    private List<datastyle_HoursType> datastyle_hourstypes;




    private List<datastyle_MapType> datastyle_maptypes;


    public datastyle_TimeStyleType(
        String text,        String title,        String language,        String text1,        String transliterationFormat,        String transliterationCountry,        String formatSource,        String country,        String transliterationLanguage,        String name,        String transliterationStyle,        String volatile,        String truncateOnOverflow,        String group    ) {
        this.text = text;
        this.title = title;
        this.language = language;
        this.text1 = text1;
        this.transliterationFormat = transliterationFormat;
        this.transliterationCountry = transliterationCountry;
        this.formatSource = formatSource;
        this.country = country;
        this.transliterationLanguage = transliterationLanguage;
        this.name = name;
        this.transliterationStyle = transliterationStyle;
        this.volatile = volatile;
        this.truncateOnOverflow = truncateOnOverflow;
        this.group = group;
        this.datastyle_ampmtypes = new ArrayList<>();
        this.datastyle_secondstypes = new ArrayList<>();
        this.datastyle_minutestypes = new ArrayList<>();
        this.datastyle_hourstypes = new ArrayList<>();
        this.datastyle_maptypes = new ArrayList<>();
    }

    public datastyle_TimeStyleType(
        String text,        String title,        String language,        String text1,        String transliterationFormat,        String transliterationCountry,        String formatSource,        String country,        String transliterationLanguage,        String name,        String transliterationStyle,        String volatile,        String truncateOnOverflow,        String group        ArrayList<datastyle_AmPmType> datastyle_ampmtypes,        ArrayList<datastyle_SecondsType> datastyle_secondstypes,        ArrayList<datastyle_MinutesType> datastyle_minutestypes,        ArrayList<datastyle_HoursType> datastyle_hourstypes,        ArrayList<datastyle_MapType> datastyle_maptypes    ) {
        this.text = text;
        this.title = title;
        this.language = language;
        this.text1 = text1;
        this.transliterationFormat = transliterationFormat;
        this.transliterationCountry = transliterationCountry;
        this.formatSource = formatSource;
        this.country = country;
        this.transliterationLanguage = transliterationLanguage;
        this.name = name;
        this.transliterationStyle = transliterationStyle;
        this.volatile = volatile;
        this.truncateOnOverflow = truncateOnOverflow;
        this.group = group;
        this.datastyle_ampmtypes = datastyle_ampmtypes;
        this.datastyle_secondstypes = datastyle_secondstypes;
        this.datastyle_minutestypes = datastyle_minutestypes;
        this.datastyle_hourstypes = datastyle_hourstypes;
        this.datastyle_maptypes = datastyle_maptypes;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getFormatsource() {
        return formatSource;
    }

    public void setFormatsource(String formatSource) {
        this.formatSource = formatSource;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getTruncateonoverflow() {
        return truncateOnOverflow;
    }

    public void setTruncateonoverflow(String truncateOnOverflow) {
        this.truncateOnOverflow = truncateOnOverflow;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<datastyle_AmPmType> getDatastyle_ampmtypes() {
        return datastyle_ampmtypes;
    }

    public void addDatastyle_ampmtype(Datastyle_ampmtype datastyle_ampmtype) {
        this.datastyle_ampmtypes.add(datastyle_ampmtype);
    }
    public datastyle_StyleTextPropertiesContent getDatastyle_styletextpropertiescontent() {
        return datastyle_styletextpropertiescontent;
    }

    public void setDatastyle_styletextpropertiescontent(datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent) {
        this.datastyle_styletextpropertiescontent = datastyle_styletextpropertiescontent;
    }
    public List<datastyle_SecondsType> getDatastyle_secondstypes() {
        return datastyle_secondstypes;
    }

    public void addDatastyle_secondstype(Datastyle_secondstype datastyle_secondstype) {
        this.datastyle_secondstypes.add(datastyle_secondstype);
    }
    public List<datastyle_MinutesType> getDatastyle_minutestypes() {
        return datastyle_minutestypes;
    }

    public void addDatastyle_minutestype(Datastyle_minutestype datastyle_minutestype) {
        this.datastyle_minutestypes.add(datastyle_minutestype);
    }
    public List<datastyle_HoursType> getDatastyle_hourstypes() {
        return datastyle_hourstypes;
    }

    public void addDatastyle_hourstype(Datastyle_hourstype datastyle_hourstype) {
        this.datastyle_hourstypes.add(datastyle_hourstype);
    }
    public List<datastyle_MapType> getDatastyle_maptypes() {
        return datastyle_maptypes;
    }

    public void addDatastyle_maptype(Datastyle_maptype datastyle_maptype) {
        this.datastyle_maptypes.add(datastyle_maptype);
    }

}