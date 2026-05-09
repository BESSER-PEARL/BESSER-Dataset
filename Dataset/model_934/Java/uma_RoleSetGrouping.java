





import java.util.List;
import java.util.ArrayList;

public class uma_RoleSetGrouping extends ContentCategory {

    private String group2;
    private String roleSet;



    public uma_RoleSetGrouping(
        String group2,        String roleSet    ) {
        super(
        );
        this.group2 = group2;
        this.roleSet = roleSet;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getRoleset() {
        return roleSet;
    }

    public void setRoleset(String roleSet) {
        this.roleSet = roleSet;
    }


}