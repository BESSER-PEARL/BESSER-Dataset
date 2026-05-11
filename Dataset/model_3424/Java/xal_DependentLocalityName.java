





import java.util.List;
import java.util.ArrayList;

public class xal_DependentLocalityName  {

    private String mixed;
    private String anyAttribute;
    private String type;
    private String code;





    private xal_DependentLocality xal_dependentlocality;


    public xal_DependentLocalityName(
        String mixed,        String anyAttribute,        String type,        String code    ) {
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.code = code;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
    }

}