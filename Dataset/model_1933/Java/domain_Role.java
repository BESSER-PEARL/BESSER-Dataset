





import java.util.List;
import java.util.ArrayList;

public class domain_Role  {

    private String uid;
    private String name;





    private domain_GrantAccess domain_grantaccess;


    public domain_Role(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_GrantAccess getDomain_grantaccess() {
        return domain_grantaccess;
    }

    public void setDomain_grantaccess(domain_GrantAccess domain_grantaccess) {
        this.domain_grantaccess = domain_grantaccess;
    }

}