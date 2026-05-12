





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int UserLevel;
    private String UserName;
    private int UserID;



    public Users(
        int UserLevel,        String UserName,        int UserID    ) {
        this.UserLevel = UserLevel;
        this.UserName = UserName;
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
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }


}