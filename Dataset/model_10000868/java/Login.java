





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String loggedoutTime;
    private String loggedinTime;
    private None userID;



    public Login(
        String loggedoutTime,        String loggedinTime,        None userID    ) {
        this.loggedoutTime = loggedoutTime;
        this.loggedinTime = loggedinTime;
        this.userID = userID;
    }


    public String getLoggedouttime() {
        return loggedoutTime;
    }

    public void setLoggedouttime(String loggedoutTime) {
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


}