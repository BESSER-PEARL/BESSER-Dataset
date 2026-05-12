





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String adminname;
    private String type;
    private int mobile;
    private String gender;
    private String password;





    private System system;


    public Admin(
        String adminname,        String type,        int mobile,        String gender,        String password    ) {
        this.adminname = adminname;
        this.type = type;
        this.mobile = mobile;
        this.gender = gender;
        this.password = password;
    }


    public String getAdminname() {
        return adminname;
    }

    public void setAdminname(String adminname) {
        this.adminname = adminname;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getMobile() {
        return mobile;
    }

    public void setMobile(int mobile) {
        this.mobile = mobile;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}