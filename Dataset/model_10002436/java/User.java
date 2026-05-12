





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String userId;
    private String password;
    private boolean active;



    public User(
        String userId,        String password,        boolean active    ) {
        this.userId = userId;
        this.password = password;
        this.active = active;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}