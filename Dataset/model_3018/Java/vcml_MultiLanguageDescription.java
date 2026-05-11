





import java.util.List;
import java.util.ArrayList;

public class vcml_MultiLanguageDescription  {

    private String language;
    private String value;





    private vcml_MultiLanguageDescriptions vcml_multilanguagedescriptions;


    public vcml_MultiLanguageDescription(
        String language,        String value    ) {
        this.language = language;
        this.value = value;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vcml_MultiLanguageDescriptions getVcml_multilanguagedescriptions() {
        return vcml_multilanguagedescriptions;
    }

    public void setVcml_multilanguagedescriptions(vcml_MultiLanguageDescriptions vcml_multilanguagedescriptions) {
        this.vcml_multilanguagedescriptions = vcml_multilanguagedescriptions;
    }

}