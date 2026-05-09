





import java.util.List;
import java.util.ArrayList;

public class uma_TeamProfile extends BreakdownElement {

    private String subTeam;
    private String role;
    private String superTeam;
    private String group2;



    public uma_TeamProfile(
        String subTeam,        String role,        String superTeam,        String group2    ) {
        super(
        );
        this.subTeam = subTeam;
        this.role = role;
        this.superTeam = superTeam;
        this.group2 = group2;
    }


    public String getSubteam() {
        return subTeam;
    }

    public void setSubteam(String subTeam) {
        this.subTeam = subTeam;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getSuperteam() {
        return superTeam;
    }

    public void setSuperteam(String superTeam) {
        this.superTeam = superTeam;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}