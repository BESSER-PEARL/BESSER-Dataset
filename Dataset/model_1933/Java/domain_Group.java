





import java.util.List;
import java.util.ArrayList;

public class domain_Group  {

    private String uid;
    private String name;





    private List<domain_Role> domain_roles;




    private domain_Roles domain_roles;




    private domain_Group domain_group;


    public domain_Group(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
        this.domain_roles = new ArrayList<>();
    }

    public domain_Group(
        String uid,        String name        ArrayList<domain_Role> domain_roles    ) {
        this.uid = uid;
        this.name = name;
        this.domain_roles = domain_roles;
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

    public List<domain_Role> getDomain_roles() {
        return domain_roles;
    }

    public void addDomain_role(Domain_role domain_role) {
        this.domain_roles.add(domain_role);
    }
    public domain_Roles getDomain_roles() {
        return domain_roles;
    }

    public void setDomain_roles(domain_Roles domain_roles) {
        this.domain_roles = domain_roles;
    }
    public domain_Group getDomain_group() {
        return domain_group;
    }

    public void setDomain_group(domain_Group domain_group) {
        this.domain_group = domain_group;
    }

}