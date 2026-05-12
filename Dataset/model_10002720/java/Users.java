





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String role_id;
    private String name;



    public Users(
        String role_id,        String name    ) {
        this.role_id = role_id;
        this.name = name;
    }


    public String getRole_id() {
        return role_id;
    }

    public void setRole_id(String role_id) {
        this.role_id = role_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}