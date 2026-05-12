





import java.util.List;
import java.util.ArrayList;

public class DBDetails  {

    private boolean isloggedin;
    private boolean iIssessionout;



    public DBDetails(
        boolean isloggedin,        boolean iIssessionout    ) {
        this.isloggedin = isloggedin;
        this.iIssessionout = iIssessionout;
    }


    public boolean getIsloggedin() {
        return isloggedin;
    }

    public void setIsloggedin(boolean isloggedin) {
        this.isloggedin = isloggedin;
    }
    public boolean getIissessionout() {
        return iIssessionout;
    }

    public void setIissessionout(boolean iIssessionout) {
        this.iIssessionout = iIssessionout;
    }


}