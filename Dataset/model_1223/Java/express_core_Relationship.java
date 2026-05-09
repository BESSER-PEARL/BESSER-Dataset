





import java.util.List;
import java.util.ArrayList;

public class express_core_Relationship  {






    private RangeRole rangerole;




    private List<Role> roles;




    private InvertibleAttribute invertibleattribute;




    private DomainRole domainrole;


    public express_core_Relationship(
    ) {
        this.roles = new ArrayList<>();
    }

    public express_core_Relationship(
        ArrayList<Role> roles    ) {
        this.roles = roles;
    }


    public RangeRole getRangerole() {
        return rangerole;
    }

    public void setRangerole(RangeRole rangerole) {
        this.rangerole = rangerole;
    }
    public List<Role> getRoles() {
        return roles;
    }

    public void addRole(Role role) {
        this.roles.add(role);
    }
    public InvertibleAttribute getInvertibleattribute() {
        return invertibleattribute;
    }

    public void setInvertibleattribute(InvertibleAttribute invertibleattribute) {
        this.invertibleattribute = invertibleattribute;
    }
    public DomainRole getDomainrole() {
        return domainrole;
    }

    public void setDomainrole(DomainRole domainrole) {
        this.domainrole = domainrole;
    }

}