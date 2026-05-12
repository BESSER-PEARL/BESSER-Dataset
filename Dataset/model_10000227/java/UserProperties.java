





import java.util.List;
import java.util.ArrayList;

public class UserProperties  {

    private String roles;
    private String Roles;



    public UserProperties(
        String roles,        String Roles    ) {
        this.roles = roles;
        this.Roles = Roles;
    }


    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }
    public String getRoles() {
        return Roles;
    }

    public void setRoles(String Roles) {
        this.Roles = Roles;
    }


}