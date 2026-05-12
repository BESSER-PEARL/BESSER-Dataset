





import java.util.List;
import java.util.ArrayList;

public class System_Login  {

    private String loggedinTime;
    private String loggedoutTime;
    private None userID;



    public System_Login(
        String loggedinTime,        String loggedoutTime,        None userID    ) {
        this.loggedinTime = loggedinTime;
        this.loggedoutTime = loggedoutTime;
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
    public None getUserid() {
        return userID;
    }

    public void setUserid(None userID) {
        this.userID = userID;
    }


}