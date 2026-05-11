





import java.util.List;
import java.util.ArrayList;

public class xal_PostBoxNumberPrefix  {

    private String numberPrefixSeparator;
    private String code;
    private String mixed;
    private String anyAttribute;





    private xal_PostBox xal_postbox;


    public xal_PostBoxNumberPrefix(
        String numberPrefixSeparator,        String code,        String mixed,        String anyAttribute    ) {
        this.numberPrefixSeparator = numberPrefixSeparator;
        this.code = code;
        this.mixed = mixed;
        this.anyAttribute = anyAttribute;
    }


    public String getNumberprefixseparator() {
        return numberPrefixSeparator;
    }

    public void setNumberprefixseparator(String numberPrefixSeparator) {
        this.numberPrefixSeparator = numberPrefixSeparator;
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

    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }

}