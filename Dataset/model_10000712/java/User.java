





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String userID;
    private String username;
    private String lastLoginTime;
    private String password;





    private Profile profile;


    public User(
        String userID,        String username,        String lastLoginTime,        String password    ) {
        this.userID = userID;
        this.username = username;
        this.lastLoginTime = lastLoginTime;
        this.password = password;
    }


    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
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

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}