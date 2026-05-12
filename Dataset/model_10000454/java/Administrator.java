





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String AdminName;
    private String Email;



    public Administrator(
        String AdminName,        String Email    ) {
        this.AdminName = AdminName;
        this.Email = Email;
    }


    public String getAdminname() {
        return AdminName;
    }

    public void setAdminname(String AdminName) {
        this.AdminName = AdminName;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}