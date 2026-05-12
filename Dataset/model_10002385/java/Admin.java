





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String adminPassword;
    private int adminId;
    private String adminRmail;
    private String adminName;



    public Admin(
        String adminPassword,        int adminId,        String adminRmail,        String adminName    ) {
        this.adminPassword = adminPassword;
        this.adminId = adminId;
        this.adminRmail = adminRmail;
        this.adminName = adminName;
    }


    public String getAdminpassword() {
        return adminPassword;
    }

    public void setAdminpassword(String adminPassword) {
        this.adminPassword = adminPassword;
    }
    public int getAdminid() {
        return adminId;
    }

    public void setAdminid(int adminId) {
        this.adminId = adminId;
    }
    public String getAdminrmail() {
        return adminRmail;
    }

    public void setAdminrmail(String adminRmail) {
        this.adminRmail = adminRmail;
    }
    public String getAdminname() {
        return adminName;
    }

    public void setAdminname(String adminName) {
        this.adminName = adminName;
    }


}