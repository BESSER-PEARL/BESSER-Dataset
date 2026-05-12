





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String email;
    private String AdminName;



    public Admin(
        String email,        String AdminName    ) {
        this.email = email;
        this.AdminName = AdminName;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAdminname() {
        return AdminName;
    }

    public void setAdminname(String AdminName) {
        this.AdminName = AdminName;
    }


}