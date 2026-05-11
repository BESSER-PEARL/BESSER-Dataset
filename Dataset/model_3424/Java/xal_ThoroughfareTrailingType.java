





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfareTrailingType  {

    private String anyAttribute;
    private String mixed;
    private String type;
    private String code;





    private xal_Thoroughfare xal_thoroughfare;


    public xal_ThoroughfareTrailingType(
        String anyAttribute,        String mixed,        String type,        String code    ) {
        this.anyAttribute = anyAttribute;
        this.mixed = mixed;
        this.type = type;
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

    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }

}