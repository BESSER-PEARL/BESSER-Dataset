





import java.util.List;
import java.util.ArrayList;

public class domain_Roles  {

    private String uid;





    private domain_EObject domain_eobject;




    private List<domain_Role> domain_roles;




    private domain_ApplicationRole domain_applicationrole;




    private domain_ApplicationRole domain_applicationrole;


    public domain_Roles(
        String uid    ) {
        this.uid = uid;
        this.domain_roles = new ArrayList<>();
    }

    public domain_Roles(
        String uid        ArrayList<domain_Role> domain_roles    ) {
        this.uid = uid;
        this.domain_roles = domain_roles;
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
    public List<domain_Role> getDomain_roles() {
        return domain_roles;
    }

    public void addDomain_role(Domain_role domain_role) {
        this.domain_roles.add(domain_role);
    }
    public domain_ApplicationRole getDomain_applicationrole() {
        return domain_applicationrole;
    }

    public void setDomain_applicationrole(domain_ApplicationRole domain_applicationrole) {
        this.domain_applicationrole = domain_applicationrole;
    }
    public domain_ApplicationRole getDomain_applicationrole() {
        return domain_applicationrole;
    }

    public void setDomain_applicationrole(domain_ApplicationRole domain_applicationrole) {
        this.domain_applicationrole = domain_applicationrole;
    }

}