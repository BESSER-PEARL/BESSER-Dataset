





import java.util.List;
import java.util.ArrayList;

public class uma_CompositeRole extends RoleDescriptor {

    private String group2;





    private List<uma_Role> uma_roles;


    public uma_CompositeRole(
        String group2    ) {
        super(
        );
        this.group2 = group2;
        this.uma_roles = new ArrayList<>();
    }

    public uma_CompositeRole(
        String group2        ArrayList<uma_Role> uma_roles    ) {
        this.group2 = group2;
        this.uma_roles = uma_roles;
    }

    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }

}