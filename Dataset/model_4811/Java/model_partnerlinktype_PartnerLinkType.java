





import java.util.List;
import java.util.ArrayList;

public class model_partnerlinktype_PartnerLinkType extends ExtensibilityElement {

    private String name;
    private String ID;





    private List<Role> roles;


    public model_partnerlinktype_PartnerLinkType(
        String name,        String ID    ) {
        super(
        );
        this.name = name;
        this.ID = ID;
        this.roles = new ArrayList<>();
    }

    public model_partnerlinktype_PartnerLinkType(
        String name,        String ID        ArrayList<Role> roles    ) {
        this.name = name;
        this.ID = ID;
        this.roles = roles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<Role> getRoles() {
        return roles;
    }

    public void addRole(Role role) {
        this.roles.add(role);
    }

}