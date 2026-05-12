





import java.util.List;
import java.util.ArrayList;

public class Restaurant_owner  {

    private String user_id;
    private String username;
    private String email;



    public Restaurant_owner(
        String user_id,        String username,        String email    ) {
        this.user_id = user_id;
        this.username = username;
        this.email = email;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}