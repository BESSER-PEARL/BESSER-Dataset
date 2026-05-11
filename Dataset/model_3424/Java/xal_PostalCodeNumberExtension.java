





import java.util.List;
import java.util.ArrayList;

public class xal_PostalCodeNumberExtension  {

    private String mixed;
    private String numberExtensionSeparator;
    private String type;
    private String anyAttribute;
    private String code;





    private xal_PostalCode xal_postalcode;


    public xal_PostalCodeNumberExtension(
        String mixed,        String numberExtensionSeparator,        String type,        String anyAttribute,        String code    ) {
        this.mixed = mixed;
        this.numberExtensionSeparator = numberExtensionSeparator;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.code = code;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getNumberextensionseparator() {
        return numberExtensionSeparator;
    }

    public void setNumberextensionseparator(String numberExtensionSeparator) {
        this.numberExtensionSeparator = numberExtensionSeparator;
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