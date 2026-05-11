





import java.util.List;
import java.util.ArrayList;

public class xal_PostBoxNumber  {

    private String mixed;
    private String code;
    private String anyAttribute;





    private xal_PostBox xal_postbox;


    public xal_PostBoxNumber(
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

    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }

}