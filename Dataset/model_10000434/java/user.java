





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String password;
    private String id;



    public User(
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


}