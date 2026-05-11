





import java.util.List;
import java.util.ArrayList;

public class xal_CountryNameCode  {

    private String scheme;
    private String mixed;
    private String code;
    private String anyAttribute;





    private xal_Country xal_country;


    public xal_CountryNameCode(
        String scheme,        String mixed,        String code,        String anyAttribute    ) {
        this.scheme = scheme;
        this.mixed = mixed;
        this.code = code;
        this.anyAttribute = anyAttribute;
    }


    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_Country getXal_country() {
        return xal_country;
    }

    public void setXal_country(xal_Country xal_country) {
        this.xal_country = xal_country;
    }

}