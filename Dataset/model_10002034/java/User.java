





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String password;
    private int userID;
    private String loginStatus;





    private User user;


    public User(
        String password,        int userID,        String loginStatus    ) {
        this.password = password;
        this.userID = userID;
        this.loginStatus = loginStatus;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }
    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}