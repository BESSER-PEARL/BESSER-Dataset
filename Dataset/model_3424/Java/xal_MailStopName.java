





import java.util.List;
import java.util.ArrayList;

public class xal_MailStopName  {

    private String mixed;
    private String code;
    private String anyAttribute;
    private String type;





    private xal_MailStop xal_mailstop;


    public xal_MailStopName(
        String mixed,        String code,        String anyAttribute,        String type    ) {
        this.mixed = mixed;
        this.code = code;
        this.anyAttribute = anyAttribute;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_MailStop getXal_mailstop() {
        return xal_mailstop;
    }

    public void setXal_mailstop(xal_MailStop xal_mailstop) {
        this.xal_mailstop = xal_mailstop;
    }

}