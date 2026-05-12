





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String userRole;
    private String username;
    private String userID;
    private String lastLoginTime;
    private String password;



    public User(
        String userRole,        String username,        String userID,        String lastLoginTime,        String password    ) {
        this.userRole = userRole;
        this.username = username;
        this.userID = userID;
        this.lastLoginTime = lastLoginTime;
        this.password = password;
    }


    public String getUserrole() {
        return userRole;
    }

    public void setUserrole(String userRole) {
        this.userRole = userRole;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(String lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}