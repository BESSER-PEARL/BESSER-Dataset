





import java.util.List;
import java.util.ArrayList;

public class smalluml_Association extends NamedElement {






    private List<smalluml_Role> smalluml_roles;


    public smalluml_Association(
    ) {
        super(
        );
        this.smalluml_roles = new ArrayList<>();
    }

    public smalluml_Association(
        ArrayList<smalluml_Role> smalluml_roles    ) {
        this.smalluml_roles = smalluml_roles;
    }


    public List<smalluml_Role> getSmalluml_roles() {
        return smalluml_roles;
    }

    public void addSmalluml_role(Smalluml_role smalluml_role) {
        this.smalluml_roles.add(smalluml_role);
    }

}