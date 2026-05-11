





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremiseNumberPrefix  {

    private String mixed;
    private String code;
    private String anyAttribute;
    private String numberPrefixSeparator;
    private String type;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremiseNumberPrefix(
        String mixed,        String code,        String anyAttribute,        String numberPrefixSeparator,        String type    ) {
        this.mixed = mixed;
        this.code = code;
        this.anyAttribute = anyAttribute;
        this.numberPrefixSeparator = numberPrefixSeparator;
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
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getNumberprefixseparator() {
        return numberPrefixSeparator;
    }

    public void setNumberprefixseparator(String numberPrefixSeparator) {
        this.numberPrefixSeparator = numberPrefixSeparator;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}