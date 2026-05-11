





import java.util.List;
import java.util.ArrayList;

public class dXP_Enrolment extends Base {

    private String role;
    private String primary;





    private dXP_OneRoster dxp_oneroster;


    public dXP_Enrolment(
        String role,        String primary    ) {
        super(
        );
        this.role = role;
        this.primary = primary;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getPrimary() {
        return primary;
    }

    public void setPrimary(String primary) {
        this.primary = primary;
    }

    public dXP_OneRoster getDxp_oneroster() {
        return dxp_oneroster;
    }

    public void setDxp_oneroster(dXP_OneRoster dxp_oneroster) {
        this.dxp_oneroster = dxp_oneroster;
    }

}