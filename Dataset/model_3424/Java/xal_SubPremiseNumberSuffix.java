





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremiseNumberSuffix  {

    private String numberSuffixSeparator;
    private String code;
    private String mixed;
    private String anyAttribute;
    private String type;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremiseNumberSuffix(
        String numberSuffixSeparator,        String code,        String mixed,        String anyAttribute,        String type    ) {
        this.numberSuffixSeparator = numberSuffixSeparator;
        this.code = code;
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
        this.type = type;
    }


    public String getNumbersuffixseparator() {
        return numberSuffixSeparator;
    }

    public void setNumbersuffixseparator(String numberSuffixSeparator) {
        this.numberSuffixSeparator = numberSuffixSeparator;
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