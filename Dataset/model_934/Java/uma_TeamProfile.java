





import java.util.List;
import java.util.ArrayList;

public class uma_TeamProfile extends BreakdownElement {

    private String role;
    private String subTeam;
    private String superTeam;
    private String group2;



    public uma_TeamProfile(
        String role,        String subTeam,        String superTeam,        String group2    ) {
        super(
        );
        this.role = role;
        this.subTeam = subTeam;
        this.superTeam = superTeam;
        this.group2 = group2;
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