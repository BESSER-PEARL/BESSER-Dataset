





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String email;
    private String adminName;





    private User user;


    public Administrator(
        String email,        String adminName    ) {
        this.email = email;
        this.adminName = adminName;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAdminname() {
        return adminName;
    }

    public void setAdminname(String adminName) {
        this.adminName = adminName;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}