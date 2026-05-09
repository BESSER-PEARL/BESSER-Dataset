





import java.util.List;
import java.util.ArrayList;

public class uma_RoleSetGrouping extends ContentCategory {

    private String roleSet;
    private String group2;



    public uma_RoleSetGrouping(
        String roleSet,        String group2    ) {
        super(
        );
        this.roleSet = roleSet;
        this.group2 = group2;
    }


    public String getRoleset() {
        return roleSet;
    }

    public void setRoleset(String roleSet) {
        this.roleSet = roleSet;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}