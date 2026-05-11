





import java.util.List;
import java.util.ArrayList;

public class restapp_model_User  {

    private int status;
    private String user;
    private int id;
    private String password;



    public restapp_model_User(
        int status,        String user,        int id,        String password    ) {
        this.status = status;
        this.user = user;
        this.id = id;
        this.password = password;
    }


    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}