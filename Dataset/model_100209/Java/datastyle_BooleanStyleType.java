





import java.util.List;
import java.util.ArrayList;

public class datastyle_BooleanStyleType  {

    private String name;
    private String title;
    private String text1;
    private String transliterationCountry;
    private String language;
    private String volatile;
    private String transliterationStyle;
    private String text;
    private String country;
    private String transliterationLanguage;
    private String transliterationFormat;



    public datastyle_BooleanStyleType(
        String name,        String title,        String text1,        String transliterationCountry,        String language,        String volatile,        String transliterationStyle,        String text,        String country,        String transliterationLanguage,        String transliterationFormat    ) {
        this.name = name;
        this.title = title;
        this.text1 = text1;
        this.transliterationCountry = transliterationCountry;
        this.language = language;
        this.volatile = volatile;
        this.transliterationStyle = transliterationStyle;
        this.text = text;
        this.country = country;
        this.transliterationLanguage = transliterationLanguage;
        this.transliterationFormat = transliterationFormat;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }


}