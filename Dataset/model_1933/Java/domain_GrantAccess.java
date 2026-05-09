





import java.util.List;
import java.util.ArrayList;

public class domain_GrantAccess  {

    private String uid;





    private domain_Secured domain_secured;


    public domain_GrantAccess(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Secured getDomain_secured() {
        return domain_secured;
    }

    public void setDomain_secured(domain_Secured domain_secured) {
        this.domain_secured = domain_secured;
    }

}