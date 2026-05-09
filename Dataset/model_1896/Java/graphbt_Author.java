





import java.util.List;
import java.util.ArrayList;

public class graphbt_Author  {

    private String contact;
    private String role;
    private String name;



    public graphbt_Author(
        String contact,        String role,        String name    ) {
        this.contact = contact;
        this.role = role;
        this.name = name;
    }


    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}