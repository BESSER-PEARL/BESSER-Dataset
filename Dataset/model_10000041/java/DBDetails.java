





import java.util.List;
import java.util.ArrayList;

public class DBDetails  {

    private boolean islogg;
    private boolean iIssessionout;



    public DBDetails(
        boolean islogg,        boolean iIssessionout    ) {
        this.islogg = islogg;
        this.iIssessionout = iIssessionout;
    }


    public boolean getIslogg() {
        return islogg;
    }

    public void setIslogg(boolean islogg) {
        this.islogg = islogg;
    }
    public boolean getIissessionout() {
        return iIssessionout;
    }

    public void setIissessionout(boolean iIssessionout) {
        this.iIssessionout = iIssessionout;
    }


}