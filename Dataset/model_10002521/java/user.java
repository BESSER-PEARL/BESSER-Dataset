





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String userID;
    private String loginStatus;
    private String password;





    private user user;


    public user(
        String userID,        String loginStatus,        String password    ) {
        this.userID = userID;
        this.loginStatus = loginStatus;
        this.password = password;
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
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}