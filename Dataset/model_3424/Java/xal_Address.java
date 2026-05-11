





import java.util.List;
import java.util.ArrayList;

public class xal_Address  {

    private String type;
    private String code;
    private String mixed;
    private String anyAttribute;



    public xal_Address(
        String type,        String code,        String mixed,        String anyAttribute    ) {
        this.type = type;
        this.code = code;
        this.mixed = mixed;
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


}