





import java.util.List;
import java.util.ArrayList;

public class xal_SubAdministrativeAreaName  {

    private String type;
    private String mixed;
    private String anyAttribute;
    private String code;



    public xal_SubAdministrativeAreaName(
        String type,        String mixed,        String anyAttribute,        String code    ) {
        this.type = type;
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
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


}