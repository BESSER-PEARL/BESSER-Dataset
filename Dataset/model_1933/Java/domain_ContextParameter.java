





import java.util.List;
import java.util.ArrayList;

public class domain_ContextParameter  {

    private String operation;
    private String uid;





    private domain_EObject domain_eobject;


    public domain_ContextParameter(
        String operation,        String uid    ) {
        this.operation = operation;
        this.uid = uid;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }

}