





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private None userID;
    private String loggedinTime;
    private String loggedoutTime;



    public Login(
        None userID,        String loggedinTime,        String loggedoutTime    ) {
        this.userID = userID;
        this.loggedinTime = loggedinTime;
        this.loggedoutTime = loggedoutTime;
    }


    public None getUserid() {
        return userID;
    }

    public void setUserid(None userID) {
        this.userID = userID;
    }
    public String getLoggedintime() {
        return loggedinTime;
    }

    public void setLoggedintime(String loggedinTime) {
        this.loggedinTime = loggedinTime;
    }
    public String getLoggedouttime() {
        return loggedoutTime;
    }

    public void setLoggedouttime(String loggedoutTime) {
        this.loggedoutTime = loggedoutTime;
    }


}