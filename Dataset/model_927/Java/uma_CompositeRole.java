





import java.util.List;
import java.util.ArrayList;

public class uma_CompositeRole extends RoleDescriptor {






    private List<uma_Role> uma_roles;


    public uma_CompositeRole(
    ) {
        super(
        );
        this.uma_roles = new ArrayList<>();
    }

    public uma_CompositeRole(
        ArrayList<uma_Role> uma_roles    ) {
        this.uma_roles = uma_roles;
    }


    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }

}