





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String loggedoutTime;
    private None userID;
    private String loggedinTime;



    public Login(
        String loggedoutTime,        None userID,        String loggedinTime    ) {
        this.loggedoutTime = loggedoutTime;
        this.userID = userID;
        this.loggedinTime = loggedinTime;
    }


    public String getLoggedouttime() {
        return loggedoutTime;
    }

    public void setLoggedouttime(String loggedoutTime) {
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


}