





import java.util.List;
import java.util.ArrayList;

public class datastyle_PercentageStyleType  {

    private String transliterationFormat;
    private String transliterationCountry;
    private String name;
    private String transliterationLanguage;
    private String country;
    private String text;
    private String language;
    private String text1;
    private String transliterationStyle;
    private String title;
    private String volatile;





    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;




    private datastyle_NumberType datastyle_numbertype;




    private List<datastyle_MapType> datastyle_maptypes;


    public datastyle_PercentageStyleType(
        String transliterationFormat,        String transliterationCountry,        String name,        String transliterationLanguage,        String country,        String text,        String language,        String text1,        String transliterationStyle,        String title,        String volatile    ) {
        this.transliterationFormat = transliterationFormat;
        this.transliterationCountry = transliterationCountry;
        this.name = name;
        this.transliterationLanguage = transliterationLanguage;
        this.country = country;
        this.text = text;
        this.language = language;
        this.text1 = text1;
        this.transliterationStyle = transliterationStyle;
        this.title = title;
        this.volatile = volatile;
        this.datastyle_maptypes = new ArrayList<>();
    }

    public datastyle_PercentageStyleType(
        String transliterationFormat,        String transliterationCountry,        String name,        String transliterationLanguage,        String country,        String text,        String language,        String text1,        String transliterationStyle,        String title,        String volatile        ArrayList<datastyle_MapType> datastyle_maptypes    ) {
        this.transliterationFormat = transliterationFormat;
        this.transliterationCountry = transliterationCountry;
        this.name = name;
        this.transliterationLanguage = transliterationLanguage;
        this.country = country;
        this.text = text;
        this.language = language;
        this.text1 = text1;
        this.transliterationStyle = transliterationStyle;
        this.title = title;
        this.volatile = volatile;
        this.datastyle_maptypes = datastyle_maptypes;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }

    public datastyle_StyleTextPropertiesContent getDatastyle_styletextpropertiescontent() {
        return datastyle_styletextpropertiescontent;
    }

    public void setDatastyle_styletextpropertiescontent(datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent) {
        this.datastyle_styletextpropertiescontent = datastyle_styletextpropertiescontent;
    }
    public datastyle_NumberType getDatastyle_numbertype() {
        return datastyle_numbertype;
    }

    public void setDatastyle_numbertype(datastyle_NumberType datastyle_numbertype) {
        this.datastyle_numbertype = datastyle_numbertype;
    }
    public List<datastyle_MapType> getDatastyle_maptypes() {
        return datastyle_maptypes;
    }

    public void addDatastyle_maptype(Datastyle_maptype datastyle_maptype) {
        this.datastyle_maptypes.add(datastyle_maptype);
    }

}