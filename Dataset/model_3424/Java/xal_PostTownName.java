





import java.util.List;
import java.util.ArrayList;

public class xal_PostTownName  {

    private String anyAttribute;
    private String type;
    private String mixed;
    private String code;



    public xal_PostTownName(
        String anyAttribute,        String type,        String mixed,        String code    ) {
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.mixed = mixed;
        this.code = code;
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


}