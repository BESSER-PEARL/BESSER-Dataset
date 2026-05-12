





import java.util.List;
import java.util.ArrayList;

public class datastyle_CurrencySymbolType  {

    private String mixed;
    private String country;
    private String language;



    public datastyle_CurrencySymbolType(
        String mixed,        String country,        String language    ) {
        this.mixed = mixed;
        this.country = country;
        this.language = language;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}