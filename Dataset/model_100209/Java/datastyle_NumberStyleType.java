





import java.util.List;
import java.util.ArrayList;

public class datastyle_NumberStyleType  {

    private String title;
    private String volatile;
    private String anyNumberGroup;
    private String text;
    private String language;
    private String transliterationFormat;
    private String name;
    private String country;
    private String transliterationLanguage;
    private String transliterationStyle;
    private String transliterationCountry;
    private String text1;





    private List<datastyle_MapType> datastyle_maptypes;




    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;


    public datastyle_NumberStyleType(
        String title,        String volatile,        String anyNumberGroup,        String text,        String language,        String transliterationFormat,        String name,        String country,        String transliterationLanguage,        String transliterationStyle,        String transliterationCountry,        String text1    ) {
        this.title = title;
        this.volatile = volatile;
        this.anyNumberGroup = anyNumberGroup;
        this.text = text;
        this.language = language;
        this.transliterationFormat = transliterationFormat;
        this.name = name;
        this.country = country;
        this.transliterationLanguage = transliterationLanguage;
        this.transliterationStyle = transliterationStyle;
        this.transliterationCountry = transliterationCountry;
        this.text1 = text1;
        this.datastyle_maptypes = new ArrayList<>();
    }

    public datastyle_NumberStyleType(
        String title,        String volatile,        String anyNumberGroup,        String text,        String language,        String transliterationFormat,        String name,        String country,        String transliterationLanguage,        String transliterationStyle,        String transliterationCountry,        String text1        ArrayList<datastyle_MapType> datastyle_maptypes    ) {
        this.title = title;
        this.volatile = volatile;
        this.anyNumberGroup = anyNumberGroup;
        this.text = text;
        this.language = language;
        this.transliterationFormat = transliterationFormat;
        this.name = name;
        this.country = country;
        this.transliterationLanguage = transliterationLanguage;
        this.transliterationStyle = transliterationStyle;
        this.transliterationCountry = transliterationCountry;
        this.text1 = text1;
        this.datastyle_maptypes = datastyle_maptypes;
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
    public String getAnynumbergroup() {
        return anyNumberGroup;
    }

    public void setAnynumbergroup(String anyNumberGroup) {
        this.anyNumberGroup = anyNumberGroup;
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
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }

    public List<datastyle_MapType> getDatastyle_maptypes() {
        return datastyle_maptypes;
    }

    public void addDatastyle_maptype(Datastyle_maptype datastyle_maptype) {
        this.datastyle_maptypes.add(datastyle_maptype);
    }
    public datastyle_StyleTextPropertiesContent getDatastyle_styletextpropertiescontent() {
        return datastyle_styletextpropertiescontent;
    }

    public void setDatastyle_styletextpropertiescontent(datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent) {
        this.datastyle_styletextpropertiescontent = datastyle_styletextpropertiescontent;
    }

}