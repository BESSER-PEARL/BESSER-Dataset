





import java.util.List;
import java.util.ArrayList;

public class xal_FirmName  {

    private String mixed;
    private String type;
    private String anyAttribute;
    private String code;





    private xal_Firm xal_firm;


    public xal_FirmName(
        String mixed,        String type,        String anyAttribute,        String code    ) {
        this.mixed = mixed;
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

    public xal_Firm getXal_firm() {
        return xal_firm;
    }

    public void setXal_firm(xal_Firm xal_firm) {
        this.xal_firm = xal_firm;
    }

}