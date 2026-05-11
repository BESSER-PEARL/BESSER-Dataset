





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremise  {

    private String any;
    private String type;
    private String anyAttribute;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremise(
        String any,        String type,        String anyAttribute    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}