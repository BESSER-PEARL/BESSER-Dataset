





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String userID;
    private String loginStatus;
    private String Password;



    public User(
        String userID,        String loginStatus,        String Password    ) {
        this.userID = userID;
        this.loginStatus = loginStatus;
        this.Password = Password;
    }


    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}