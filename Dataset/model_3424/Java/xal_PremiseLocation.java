





import java.util.List;
import java.util.ArrayList;

public class xal_PremiseLocation  {

    private String code;
    private String anyAttribute;
    private String mixed;



    public xal_PremiseLocation(
        String code,        String anyAttribute,        String mixed    ) {
        this.code = code;
        this.anyAttribute = anyAttribute;
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
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}