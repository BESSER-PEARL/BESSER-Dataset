





import java.util.List;
import java.util.ArrayList;

public class xal_PostalRouteNumber  {

    private String code;
    private String mixed;
    private String anyAttribute;





    private xal_PostalRoute xal_postalroute;


    public xal_PostalRouteNumber(
        String code,        String mixed,        String anyAttribute    ) {
        this.code = code;
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
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

    public xal_PostalRoute getXal_postalroute() {
        return xal_postalroute;
    }

    public void setXal_postalroute(xal_PostalRoute xal_postalroute) {
        this.xal_postalroute = xal_postalroute;
    }

}