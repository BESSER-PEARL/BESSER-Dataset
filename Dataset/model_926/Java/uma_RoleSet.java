





import java.util.List;
import java.util.ArrayList;

public class uma_RoleSet extends ContentCategory {






    private List<uma_Role> uma_roles;




    private uma_RoleSetGrouping uma_rolesetgrouping;


    public uma_RoleSet(
    ) {
        super(
        );
        this.uma_roles = new ArrayList<>();
    }

    public uma_RoleSet(
        ArrayList<uma_Role> uma_roles    ) {
        this.uma_roles = uma_roles;
    }


    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }
    public uma_RoleSetGrouping getUma_rolesetgrouping() {
        return uma_rolesetgrouping;
    }

    public void setUma_rolesetgrouping(uma_RoleSetGrouping uma_rolesetgrouping) {
        this.uma_rolesetgrouping = uma_rolesetgrouping;
    }

}