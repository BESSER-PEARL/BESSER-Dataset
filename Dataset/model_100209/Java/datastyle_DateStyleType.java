





import java.util.List;
import java.util.ArrayList;

public class datastyle_DateStyleType  {

    private String transliterationLanguage;
    private String formatSource;
    private String automaticOrder;
    private String title;
    private String group;
    private String transliterationCountry;
    private String country;
    private String text1;
    private String name;
    private String volatile;
    private String language;
    private String text;
    private String transliterationStyle;
    private String transliterationFormat;





    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;




    private List<datastyle_MapType> datastyle_maptypes;




    private List<datastyle_AmPmType> datastyle_ampmtypes;


    public datastyle_DateStyleType(
        String transliterationLanguage,        String formatSource,        String automaticOrder,        String title,        String group,        String transliterationCountry,        String country,        String text1,        String name,        String volatile,        String language,        String text,        String transliterationStyle,        String transliterationFormat    ) {
        this.transliterationLanguage = transliterationLanguage;
        this.formatSource = formatSource;
        this.automaticOrder = automaticOrder;
        this.title = title;
        this.group = group;
        this.transliterationCountry = transliterationCountry;
        this.country = country;
        this.text1 = text1;
        this.name = name;
        this.volatile = volatile;
        this.language = language;
        this.text = text;
        this.transliterationStyle = transliterationStyle;
        this.transliterationFormat = transliterationFormat;
        this.datastyle_maptypes = new ArrayList<>();
        this.datastyle_ampmtypes = new ArrayList<>();
    }

    public datastyle_DateStyleType(
        String transliterationLanguage,        String formatSource,        String automaticOrder,        String title,        String group,        String transliterationCountry,        String country,        String text1,        String name,        String volatile,        String language,        String text,        String transliterationStyle,        String transliterationFormat        ArrayList<datastyle_MapType> datastyle_maptypes,        ArrayList<datastyle_AmPmType> datastyle_ampmtypes    ) {
        this.transliterationLanguage = transliterationLanguage;
        this.formatSource = formatSource;
        this.automaticOrder = automaticOrder;
        this.title = title;
        this.group = group;
        this.transliterationCountry = transliterationCountry;
        this.country = country;
        this.text1 = text1;
        this.name = name;
        this.volatile = volatile;
        this.language = language;
        this.text = text;
        this.transliterationStyle = transliterationStyle;
        this.transliterationFormat = transliterationFormat;
        this.datastyle_maptypes = datastyle_maptypes;
        this.datastyle_ampmtypes = datastyle_ampmtypes;
    }

    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
    }
    public String getFormatsource() {
        return formatSource;
    }

    public void setFormatsource(String formatSource) {
        this.formatSource = formatSource;
    }
    public String getAutomaticorder() {
        return automaticOrder;
    }

    public void setAutomaticorder(String automaticOrder) {
        this.automaticOrder = automaticOrder;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }

    public datastyle_StyleTextPropertiesContent getDatastyle_styletextpropertiescontent() {
        return datastyle_styletextpropertiescontent;
    }

    public void setDatastyle_styletextpropertiescontent(datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent) {
        this.datastyle_styletextpropertiescontent = datastyle_styletextpropertiescontent;
    }
    public List<datastyle_MapType> getDatastyle_maptypes() {
        return datastyle_maptypes;
    }

    public void addDatastyle_maptype(Datastyle_maptype datastyle_maptype) {
        this.datastyle_maptypes.add(datastyle_maptype);
    }
    public List<datastyle_AmPmType> getDatastyle_ampmtypes() {
        return datastyle_ampmtypes;
    }

    public void addDatastyle_ampmtype(Datastyle_ampmtype datastyle_ampmtype) {
        this.datastyle_ampmtypes.add(datastyle_ampmtype);
    }

}