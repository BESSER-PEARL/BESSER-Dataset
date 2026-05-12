





import java.util.List;
import java.util.ArrayList;

public class administrator  {

    private String adminName;
    private String email;



    public administrator(
        String adminName,        String email    ) {
        this.adminName = adminName;
        this.email = email;
    }


    public String getAdminname() {
        return adminName;
    }

    public void setAdminname(String adminName) {
        this.adminName = adminName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}