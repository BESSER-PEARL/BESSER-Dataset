





import java.util.List;
import java.util.ArrayList;

public class datastyle_CurrencyStyleType  {

    private String name;
    private String transliterationCountry;
    private String automaticOrder;
    private String volatile;
    private String title;
    private String text;
    private String transliterationFormat;
    private String text4;
    private String transliterationLanguage;
    private String text1;
    private String text2;
    private String transliterationStyle;
    private String country;
    private String text3;
    private String language;





    private datastyle_CurrencySymbolType datastyle_currencysymboltype;




    private List<datastyle_MapType> datastyle_maptypes;




    private datastyle_NumberType datastyle_numbertype;




    private datastyle_NumberType datastyle_numbertype;




    private datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent;




    private datastyle_CurrencySymbolType datastyle_currencysymboltype;


    public datastyle_CurrencyStyleType(
        String name,        String transliterationCountry,        String automaticOrder,        String volatile,        String title,        String text,        String transliterationFormat,        String text4,        String transliterationLanguage,        String text1,        String text2,        String transliterationStyle,        String country,        String text3,        String language    ) {
        this.name = name;
        this.transliterationCountry = transliterationCountry;
        this.automaticOrder = automaticOrder;
        this.volatile = volatile;
        this.title = title;
        this.text = text;
        this.transliterationFormat = transliterationFormat;
        this.text4 = text4;
        this.transliterationLanguage = transliterationLanguage;
        this.text1 = text1;
        this.text2 = text2;
        this.transliterationStyle = transliterationStyle;
        this.country = country;
        this.text3 = text3;
        this.language = language;
        this.datastyle_maptypes = new ArrayList<>();
    }

    public datastyle_CurrencyStyleType(
        String name,        String transliterationCountry,        String automaticOrder,        String volatile,        String title,        String text,        String transliterationFormat,        String text4,        String transliterationLanguage,        String text1,        String text2,        String transliterationStyle,        String country,        String text3,        String language        ArrayList<datastyle_MapType> datastyle_maptypes    ) {
        this.name = name;
        this.transliterationCountry = transliterationCountry;
        this.automaticOrder = automaticOrder;
        this.volatile = volatile;
        this.title = title;
        this.text = text;
        this.transliterationFormat = transliterationFormat;
        this.text4 = text4;
        this.transliterationLanguage = transliterationLanguage;
        this.text1 = text1;
        this.text2 = text2;
        this.transliterationStyle = transliterationStyle;
        this.country = country;
        this.text3 = text3;
        this.language = language;
        this.datastyle_maptypes = datastyle_maptypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTransliterationcountry() {
        return transliterationCountry;
    }

    public void setTransliterationcountry(String transliterationCountry) {
        this.transliterationCountry = transliterationCountry;
    }
    public String getAutomaticorder() {
        return automaticOrder;
    }

    public void setAutomaticorder(String automaticOrder) {
        this.automaticOrder = automaticOrder;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTransliterationformat() {
        return transliterationFormat;
    }

    public void setTransliterationformat(String transliterationFormat) {
        this.transliterationFormat = transliterationFormat;
    }
    public String getText4() {
        return text4;
    }

    public void setText4(String text4) {
        this.text4 = text4;
    }
    public String getTransliterationlanguage() {
        return transliterationLanguage;
    }

    public void setTransliterationlanguage(String transliterationLanguage) {
        this.transliterationLanguage = transliterationLanguage;
    }
    public String getText1() {
        return text1;
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }
    public String getText2() {
        return text2;
    }

    public void setText2(String text2) {
        this.text2 = text2;
    }
    public String getTransliterationstyle() {
        return transliterationStyle;
    }

    public void setTransliterationstyle(String transliterationStyle) {
        this.transliterationStyle = transliterationStyle;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getText3() {
        return text3;
    }

    public void setText3(String text3) {
        this.text3 = text3;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public datastyle_CurrencySymbolType getDatastyle_currencysymboltype() {
        return datastyle_currencysymboltype;
    }

    public void setDatastyle_currencysymboltype(datastyle_CurrencySymbolType datastyle_currencysymboltype) {
        this.datastyle_currencysymboltype = datastyle_currencysymboltype;
    }
    public List<datastyle_MapType> getDatastyle_maptypes() {
        return datastyle_maptypes;
    }

    public void addDatastyle_maptype(Datastyle_maptype datastyle_maptype) {
        this.datastyle_maptypes.add(datastyle_maptype);
    }
    public datastyle_NumberType getDatastyle_numbertype() {
        return datastyle_numbertype;
    }

    public void setDatastyle_numbertype(datastyle_NumberType datastyle_numbertype) {
        this.datastyle_numbertype = datastyle_numbertype;
    }
    public datastyle_NumberType getDatastyle_numbertype() {
        return datastyle_numbertype;
    }

    public void setDatastyle_numbertype(datastyle_NumberType datastyle_numbertype) {
        this.datastyle_numbertype = datastyle_numbertype;
    }
    public datastyle_StyleTextPropertiesContent getDatastyle_styletextpropertiescontent() {
        return datastyle_styletextpropertiescontent;
    }

    public void setDatastyle_styletextpropertiescontent(datastyle_StyleTextPropertiesContent datastyle_styletextpropertiescontent) {
        this.datastyle_styletextpropertiescontent = datastyle_styletextpropertiescontent;
    }
    public datastyle_CurrencySymbolType getDatastyle_currencysymboltype() {
        return datastyle_currencysymboltype;
    }

    public void setDatastyle_currencysymboltype(datastyle_CurrencySymbolType datastyle_currencysymboltype) {
        this.datastyle_currencysymboltype = datastyle_currencysymboltype;
    }

}