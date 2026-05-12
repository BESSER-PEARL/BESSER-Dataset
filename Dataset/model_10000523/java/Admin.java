





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String type;
    private String adminname;
    private String password;
    private int mobile;
    private String gender;





    private System system;


    public Admin(
        String type,        String adminname,        String password,        int mobile,        String gender    ) {
        this.type = type;
        this.adminname = adminname;
        this.password = password;
        this.mobile = mobile;
        this.gender = gender;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAdminname() {
        return adminname;
    }

    public void setAdminname(String adminname) {
        this.adminname = adminname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}