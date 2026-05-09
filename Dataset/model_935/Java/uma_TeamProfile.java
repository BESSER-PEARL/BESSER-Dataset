





import java.util.List;
import java.util.ArrayList;

public class uma_TeamProfile extends BreakdownElement {

    private String role;
    private String subTeam;
    private String group2;
    private String superTeam;



    public uma_TeamProfile(
        String role,        String subTeam,        String group2,        String superTeam    ) {
        super(
        );
        this.role = role;
        this.subTeam = subTeam;
        this.group2 = group2;
        this.superTeam = superTeam;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getSubteam() {
        return subTeam;
    }

    public void setSubteam(String subTeam) {
        this.subTeam = subTeam;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getSuperteam() {
        return superTeam;
    }

    public void setSuperteam(String superTeam) {
        this.superTeam = superTeam;
    }


}