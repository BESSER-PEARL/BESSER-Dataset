





import java.util.List;
import java.util.ArrayList;

public class dXP_User extends Base {

    private String userName;
    private String identifier;
    private String role;
    private String enabledUser;





    private dXP_AcademicSession dxp_academicsession;




    private dXP_Enrolment dxp_enrolment;


    public dXP_User(
        String userName,        String identifier,        String role,        String enabledUser    ) {
        super(
        );
        this.userName = userName;
        this.identifier = identifier;
        this.role = role;
        this.enabledUser = enabledUser;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getEnableduser() {
        return enabledUser;
    }

    public void setEnableduser(String enabledUser) {
        this.enabledUser = enabledUser;
    }

    public dXP_AcademicSession getDxp_academicsession() {
        return dxp_academicsession;
    }

    public void setDxp_academicsession(dXP_AcademicSession dxp_academicsession) {
        this.dxp_academicsession = dxp_academicsession;
    }
    public dXP_Enrolment getDxp_enrolment() {
        return dxp_enrolment;
    }

    public void setDxp_enrolment(dXP_Enrolment dxp_enrolment) {
        this.dxp_enrolment = dxp_enrolment;
    }

}