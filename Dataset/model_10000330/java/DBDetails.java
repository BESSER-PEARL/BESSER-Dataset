





import java.util.List;
import java.util.ArrayList;

public class DBDetails  {

    private boolean iIssessionout;
    private boolean isloggedin;



    public DBDetails(
        boolean iIssessionout,        boolean isloggedin    ) {
        this.iIssessionout = iIssessionout;
        this.isloggedin = isloggedin;
    }


    public boolean getIissessionout() {
        return iIssessionout;
    }

    public void setIissessionout(boolean iIssessionout) {
        this.iIssessionout = iIssessionout;
    }
    public boolean getIsloggedin() {
        return isloggedin;
    }

    public void setIsloggedin(boolean isloggedin) {
        this.isloggedin = isloggedin;
    }


}