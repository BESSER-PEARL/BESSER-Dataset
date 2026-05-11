





import java.util.List;
import java.util.ArrayList;

public class xal_LargeMailUserIdentifier  {

    private String mixed;
    private String code;
    private String type;
    private String indicator;
    private String anyAttribute;





    private xal_LargeMailUser xal_largemailuser;


    public xal_LargeMailUserIdentifier(
        String mixed,        String code,        String type,        String indicator,        String anyAttribute    ) {
        this.mixed = mixed;
        this.code = code;
        this.type = type;
        this.indicator = indicator;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_LargeMailUser getXal_largemailuser() {
        return xal_largemailuser;
    }

    public void setXal_largemailuser(xal_LargeMailUser xal_largemailuser) {
        this.xal_largemailuser = xal_largemailuser;
    }

}