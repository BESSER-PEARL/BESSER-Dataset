





import java.util.List;
import java.util.ArrayList;

public class typedef_TypeLanguageBinding  {

    private String lang;
    private String langSpecificType;
    private String defaultInitValue;
    private String nullValueLiteral;
    private String langSpecificNS;





    private typedef_PrimitiveType typedef_primitivetype;


    public typedef_TypeLanguageBinding(
        String lang,        String langSpecificType,        String defaultInitValue,        String nullValueLiteral,        String langSpecificNS    ) {
        this.lang = lang;
        this.langSpecificType = langSpecificType;
        this.defaultInitValue = defaultInitValue;
        this.nullValueLiteral = nullValueLiteral;
        this.langSpecificNS = langSpecificNS;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getLangspecifictype() {
        return langSpecificType;
    }

    public void setLangspecifictype(String langSpecificType) {
        this.langSpecificType = langSpecificType;
    }
    public String getDefaultinitvalue() {
        return defaultInitValue;
    }

    public void setDefaultinitvalue(String defaultInitValue) {
        this.defaultInitValue = defaultInitValue;
    }
    public String getNullvalueliteral() {
        return nullValueLiteral;
    }

    public void setNullvalueliteral(String nullValueLiteral) {
        this.nullValueLiteral = nullValueLiteral;
    }
    public String getLangspecificns() {
        return langSpecificNS;
    }

    public void setLangspecificns(String langSpecificNS) {
        this.langSpecificNS = langSpecificNS;
    }

    public typedef_PrimitiveType getTypedef_primitivetype() {
        return typedef_primitivetype;
    }

    public void setTypedef_primitivetype(typedef_PrimitiveType typedef_primitivetype) {
        this.typedef_primitivetype = typedef_primitivetype;
    }

}