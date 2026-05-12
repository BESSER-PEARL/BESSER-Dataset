





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String loggedinTime;
    private None userID;
    private String loggedoutTime;



    public Login(
        String loggedinTime,        None userID,        String loggedoutTime    ) {
        this.loggedinTime = loggedinTime;
        this.userID = userID;
        this.loggedoutTime = loggedoutTime;
    }


    public String getLoggedintime() {
        return loggedinTime;
    }

    public void setLoggedintime(String loggedinTime) {
        this.loggedinTime = loggedinTime;
    }
    public None getUserid() {
        return userID;
    }

    public void setUserid(None userID) {
        this.userID = userID;
    }
    public String getLoggedouttime() {
        return loggedoutTime;
    }

    public void setLoggedouttime(String loggedoutTime) {
        this.loggedoutTime = loggedoutTime;
    }


}