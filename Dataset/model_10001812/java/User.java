





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String loginStatus;
    private String userId;
    private String password;



    public User(
        String loginStatus,        String userId,        String password    ) {
        this.loginStatus = loginStatus;
        this.userId = userId;
        this.password = password;
    }


    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
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


}