





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private int password;
    private String adminEmail;



    public Admin(
        int password,        String adminEmail    ) {
        this.password = password;
        this.adminEmail = adminEmail;
    }


    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public String getAdminemail() {
        return adminEmail;
    }

    public void setAdminemail(String adminEmail) {
        this.adminEmail = adminEmail;
    }


}