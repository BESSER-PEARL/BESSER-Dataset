





import java.util.List;
import java.util.ArrayList;

public class xal_Barcode  {

    private String anyAttribute;
    private String code;
    private String type;
    private String mixed;





    private xal_PostalServiceElements xal_postalserviceelements;


    public xal_Barcode(
        String anyAttribute,        String code,        String type,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.type = type;
        this.mixed = mixed;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
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

    public xal_PostalServiceElements getXal_postalserviceelements() {
        return xal_postalserviceelements;
    }

    public void setXal_postalserviceelements(xal_PostalServiceElements xal_postalserviceelements) {
        this.xal_postalserviceelements = xal_postalserviceelements;
    }

}