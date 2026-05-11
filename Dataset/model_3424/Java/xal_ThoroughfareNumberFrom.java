





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfareNumberFrom  {

    private String mixed;
    private String code;
    private String anyAttribute;





    private xal_ThoroughfareNumberRange xal_thoroughfarenumberrange;


    public xal_ThoroughfareNumberFrom(
        String mixed,        String code,        String anyAttribute    ) {
        this.mixed = mixed;
        this.code = code;
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
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_ThoroughfareNumberRange getXal_thoroughfarenumberrange() {
        return xal_thoroughfarenumberrange;
    }

    public void setXal_thoroughfarenumberrange(xal_ThoroughfareNumberRange xal_thoroughfarenumberrange) {
        this.xal_thoroughfarenumberrange = xal_thoroughfarenumberrange;
    }

}