





import java.util.List;
import java.util.ArrayList;

public class domain_Messages  {

    private String uid;





    private domain_EObject domain_eobject;




    private domain_ApplicationMessages domain_applicationmessages;




    private domain_ApplicationMessages domain_applicationmessages;


    public domain_Messages(
        String uid    ) {
        this.uid = uid;
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
    public domain_ApplicationMessages getDomain_applicationmessages() {
        return domain_applicationmessages;
    }

    public void setDomain_applicationmessages(domain_ApplicationMessages domain_applicationmessages) {
        this.domain_applicationmessages = domain_applicationmessages;
    }
    public domain_ApplicationMessages getDomain_applicationmessages() {
        return domain_applicationmessages;
    }

    public void setDomain_applicationmessages(domain_ApplicationMessages domain_applicationmessages) {
        this.domain_applicationmessages = domain_applicationmessages;
    }

}