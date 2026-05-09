





import java.util.List;
import java.util.ArrayList;

public class uma_RoleSet extends ContentCategory {

    private String group2;
    private String role;



    public uma_RoleSet(
        String group2,        String role    ) {
        super(
        );
        this.group2 = group2;
        this.role = role;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }


}