





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremiseLocation  {

    private String mixed;
    private String code;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremiseLocation(
        String mixed,        String code    ) {
        this.mixed = mixed;
        this.code = code;
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

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}