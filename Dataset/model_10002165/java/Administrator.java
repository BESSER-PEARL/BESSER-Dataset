





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String name;
    private String email;
    private int adminID;





    private Administrator administrator;


    public Administrator(
        String name,        String email,        int adminID    ) {
        this.name = name;
        this.email = email;
        this.adminID = adminID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getAdminid() {
        return adminID;
    }

    public void setAdminid(int adminID) {
        this.adminID = adminID;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}