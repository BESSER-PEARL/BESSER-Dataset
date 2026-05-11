





import java.util.List;
import java.util.ArrayList;

public class xal_PostalCodeNumber  {

    private String type;
    private String anyAttribute;
    private String mixed;
    private String code;





    private xal_PostalCode xal_postalcode;


    public xal_PostalCodeNumber(
        String type,        String anyAttribute,        String mixed,        String code    ) {
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.mixed = mixed;
        this.code = code;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
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

    public xal_PostalCode getXal_postalcode() {
        return xal_postalcode;
    }

    public void setXal_postalcode(xal_PostalCode xal_postalcode) {
        this.xal_postalcode = xal_postalcode;
    }

}