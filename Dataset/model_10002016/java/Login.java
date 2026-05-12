





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String userid;
    private String password;





    private Admin admin;


    public Login(
        String userid,        String password    ) {
        this.userid = userid;
        this.password = password;
    }


    public String getUserid() {
        return userid;
    }

    public void setUserid(String userid) {
        this.userid = userid;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}