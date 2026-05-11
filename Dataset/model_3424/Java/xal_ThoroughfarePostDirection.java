





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfarePostDirection  {

    private String mixed;
    private String anyAttribute;
    private String code;
    private String type;





    private xal_Thoroughfare xal_thoroughfare;


    public xal_ThoroughfarePostDirection(
        String mixed,        String anyAttribute,        String code,        String type    ) {
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
        this.code = code;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }

}