





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int UserID;
    private int UserLevel;
    private String UserName;



    public Users(
        int UserID,        int UserLevel,        String UserName    ) {
        this.UserID = UserID;
        this.UserLevel = UserLevel;
        this.UserName = UserName;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getUserlevel() {
        return UserLevel;
    }

    public void setUserlevel(int UserLevel) {
        this.UserLevel = UserLevel;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}