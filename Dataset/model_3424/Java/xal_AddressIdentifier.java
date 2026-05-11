





import java.util.List;
import java.util.ArrayList;

public class xal_AddressIdentifier  {

    private String anyAttribute;
    private String code;
    private String type;
    private String identifierType;
    private String mixed;





    private xal_PostalServiceElements xal_postalserviceelements;


    public xal_AddressIdentifier(
        String anyAttribute,        String code,        String type,        String identifierType,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.type = type;
        this.identifierType = identifierType;
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
    public String getIdentifiertype() {
        return identifierType;
    }

    public void setIdentifiertype(String identifierType) {
        this.identifierType = identifierType;
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