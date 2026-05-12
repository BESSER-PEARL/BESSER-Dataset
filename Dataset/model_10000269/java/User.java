





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String username;
    private String password;
    private String userID;
    private String lastLoginTime;





    private Profile profile;


    public User(
        String username,        String password,        String userID,        String lastLoginTime    ) {
        this.username = username;
        this.password = password;
        this.userID = userID;
        this.lastLoginTime = lastLoginTime;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
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
    public String getLastlogintime() {
        return lastLoginTime;
    }

    public void setLastlogintime(String lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}