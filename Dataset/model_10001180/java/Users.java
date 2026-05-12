




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int UserLevel;
    private String UserName;
    private LocalDate UserBday;
    private int UserID;



    public Users(
        int UserLevel,        String UserName,        LocalDate UserBday,        int UserID    ) {
        this.UserLevel = UserLevel;
        this.UserName = UserName;
        this.UserBday = UserBday;
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
    public LocalDate getUserbday() {
        return UserBday;
    }

    public void setUserbday(LocalDate UserBday) {
        this.UserBday = UserBday;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }


}