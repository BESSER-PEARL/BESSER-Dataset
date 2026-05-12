





import java.util.List;
import java.util.ArrayList;

public class AdminController  {

    private String UserName;
    private int UserLevel;
    private int UserID;



    public AdminController(
        String UserName,        int UserLevel,        int UserID    ) {
        this.UserName = UserName;
        this.UserLevel = UserLevel;
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
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }


}