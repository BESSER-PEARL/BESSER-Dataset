





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String username;
    private String lastLoginTime;
    private String password;
    private String userID;
    private String userRole;



    public User(
        String username,        String lastLoginTime,        String password,        String userID,        String userRole    ) {
        this.username = username;
        this.lastLoginTime = lastLoginTime;
        this.password = password;
        this.userID = userID;
        this.userRole = userRole;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
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
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getUserrole() {
        return userRole;
    }

    public void setUserrole(String userRole) {
        this.userRole = userRole;
    }


}