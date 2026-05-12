





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private int ID;
    private String AdminInfo;
    private String Password;
    private String UserName;



    public Admin(
        int ID,        String AdminInfo,        String Password,        String UserName    ) {
        this.ID = ID;
        this.AdminInfo = AdminInfo;
        this.Password = Password;
        this.UserName = UserName;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getAdmininfo() {
        return AdminInfo;
    }

    public void setAdmininfo(String AdminInfo) {
        this.AdminInfo = AdminInfo;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}