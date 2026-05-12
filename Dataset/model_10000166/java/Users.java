





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int UserID;
    private String UserName;
    private int UserLevel;



    public Users(
        int UserID,        String UserName,        int UserLevel    ) {
        this.UserID = UserID;
        this.UserName = UserName;
        this.UserLevel = UserLevel;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getUserlevel() {
        return UserLevel;
    }

    public void setUserlevel(int UserLevel) {
        this.UserLevel = UserLevel;
    }


}