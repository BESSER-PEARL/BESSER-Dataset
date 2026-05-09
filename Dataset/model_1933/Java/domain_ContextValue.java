





import java.util.List;
import java.util.ArrayList;

public class domain_ContextValue  {

    private String value;
    private String uid;
    private boolean constant;





    private domain_ContextParameter domain_contextparameter;


    public domain_ContextValue(
        String value,        String uid,        boolean constant    ) {
        this.value = value;
        this.uid = uid;
        this.constant = constant;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public domain_ContextParameter getDomain_contextparameter() {
        return domain_contextparameter;
    }

    public void setDomain_contextparameter(domain_ContextParameter domain_contextparameter) {
        this.domain_contextparameter = domain_contextparameter;
    }

}