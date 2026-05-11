





import java.util.List;
import java.util.ArrayList;

public class xal_MailStopNumber  {

    private String anyAttribute;
    private String nameNumberSeparator;
    private String mixed;
    private String code;





    private xal_MailStop xal_mailstop;


    public xal_MailStopNumber(
        String anyAttribute,        String nameNumberSeparator,        String mixed,        String code    ) {
        this.anyAttribute = anyAttribute;
        this.nameNumberSeparator = nameNumberSeparator;
        this.mixed = mixed;
        this.code = code;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getNamenumberseparator() {
        return nameNumberSeparator;
    }

    public void setNamenumberseparator(String nameNumberSeparator) {
        this.nameNumberSeparator = nameNumberSeparator;
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

    public xal_MailStop getXal_mailstop() {
        return xal_mailstop;
    }

    public void setXal_mailstop(xal_MailStop xal_mailstop) {
        this.xal_mailstop = xal_mailstop;
    }

}