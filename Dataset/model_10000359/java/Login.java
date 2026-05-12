





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password;
    private String userid;





    private Admin admin;




    private Applicant applicant;


    public Login(
        String password,        String userid    ) {
        this.password = password;
        this.userid = userid;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUserid() {
        return userid;
    }

    public void setUserid(String userid) {
        this.userid = userid;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }

}