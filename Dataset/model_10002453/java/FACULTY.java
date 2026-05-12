





import java.util.List;
import java.util.ArrayList;

public class FACULTY  {

    private String password;
    private String id;





    private ADMIN admin;


    public FACULTY(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ADMIN getAdmin() {
        return admin;
    }

    public void setAdmin(ADMIN admin) {
        this.admin = admin;
    }

}