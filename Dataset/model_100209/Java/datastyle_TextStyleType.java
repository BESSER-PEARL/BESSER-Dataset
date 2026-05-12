





import java.util.List;
import java.util.ArrayList;

public class datastyle_TextStyleType  {

    private String group;
    private String text;
    private String transliterationStyle;
    private String name;
    private String transliterationFormat;
    private String text1;
    private String volatile;
    private String transliterationLanguage;
    private String title;
    private String language;
    private String transliterationCountry;
    private String country;





    private List<datastyle_TextContentType> datastyle_textcontenttypes;




    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;




    private List<datastyle_MapType> datastyle_maptypes;


    public datastyle_TextStyleType(
        String group,        String text,        String transliterationStyle,        String name,        String transliterationFormat,        String text1,        String volatile,        String transliterationLanguage,        String title,        String language,        String transliterationCountry,        String country    ) {
        this.group = group;
        this.text = text;
        this.transliterationStyle = transliterationStyle;
        this.name = name;
        this.transliterationFormat = transliterationFormat;
        this.text1 = text1;
        this.volatile = volatile;
        this.transliterationLanguage = transliterationLanguage;
        this.title = title;
        this.language = language;
        this.transliterationCountry = transliterationCountry;
        this.country = country;
        this.datastyle_textcontenttypes = new ArrayList<>();
        this.datastyle_maptypes = new ArrayList<>();
    }

    public datastyle_TextStyleType(
        String group,        String text,        String transliterationStyle,        String name,        String transliterationFormat,        String text1,        String volatile,        String transliterationLanguage,        String title,        String language,        String transliterationCountry,        String country        ArrayList<datastyle_TextContentType> datastyle_textcontenttypes,        ArrayList<datastyle_MapType> datastyle_maptypes    ) {
        this.group = group;
        this.text = text;
        this.transliterationStyle = transliterationStyle;
        this.name = name;
        this.transliterationFormat = transliterationFormat;
        this.text1 = text1;
        this.volatile = volatile;
        this.transliterationLanguage = transliterationLanguage;
        this.title = title;
        this.language = language;
        this.transliterationCountry = transliterationCountry;
        this.country = country;
        this.datastyle_textcontenttypes = datastyle_textcontenttypes;
        this.datastyle_maptypes = datastyle_maptypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
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

    public List<datastyle_TextContentType> getDatastyle_textcontenttypes() {
        return datastyle_textcontenttypes;
    }

    public void addDatastyle_textcontenttype(Datastyle_textcontenttype datastyle_textcontenttype) {
        this.datastyle_textcontenttypes.add(datastyle_textcontenttype);
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

}