





import java.util.List;
import java.util.ArrayList;

public class xal_CountryName  {

    private String anyAttribute;
    private String type;
    private String mixed;
    private String code;





    private xal_Country xal_country;


    public xal_CountryName(
        String anyAttribute,        String type,        String mixed,        String code    ) {
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.mixed = mixed;
        this.code = code;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public xal_Country getXal_country() {
        return xal_country;
    }

    public void setXal_country(xal_Country xal_country) {
        this.xal_country = xal_country;
    }

}