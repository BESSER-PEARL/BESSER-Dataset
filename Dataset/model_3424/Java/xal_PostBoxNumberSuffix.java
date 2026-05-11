





import java.util.List;
import java.util.ArrayList;

public class xal_PostBoxNumberSuffix  {

    private String anyAttribute;
    private String code;
    private String numberSuffixSeparator;
    private String mixed;





    private xal_PostBox xal_postbox;


    public xal_PostBoxNumberSuffix(
        String anyAttribute,        String code,        String numberSuffixSeparator,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.numberSuffixSeparator = numberSuffixSeparator;
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
    public String getNumbersuffixseparator() {
        return numberSuffixSeparator;
    }

    public void setNumbersuffixseparator(String numberSuffixSeparator) {
        this.numberSuffixSeparator = numberSuffixSeparator;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }

}