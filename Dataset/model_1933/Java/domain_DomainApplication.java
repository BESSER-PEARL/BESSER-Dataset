





import java.util.List;
import java.util.ArrayList;

public class domain_DomainApplication  {

    private String name;
    private String uid;





    private domain_GrantAccess domain_grantaccess;




    private domain_DomainApplications domain_domainapplications;




    private domain_DomainApplications domain_domainapplications;


    public domain_DomainApplication(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_GrantAccess getDomain_grantaccess() {
        return domain_grantaccess;
    }

    public void setDomain_grantaccess(domain_GrantAccess domain_grantaccess) {
        this.domain_grantaccess = domain_grantaccess;
    }
    public domain_DomainApplications getDomain_domainapplications() {
        return domain_domainapplications;
    }

    public void setDomain_domainapplications(domain_DomainApplications domain_domainapplications) {
        this.domain_domainapplications = domain_domainapplications;
    }
    public domain_DomainApplications getDomain_domainapplications() {
        return domain_domainapplications;
    }

    public void setDomain_domainapplications(domain_DomainApplications domain_domainapplications) {
        this.domain_domainapplications = domain_domainapplications;
    }

}