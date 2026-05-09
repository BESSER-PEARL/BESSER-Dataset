





import java.util.List;
import java.util.ArrayList;

public class easyflow_GroupingEvent  {

    private String dagOut;
    private String dagIn;



    public easyflow_GroupingEvent(
        String dagOut,        String dagIn    ) {
        this.dagOut = dagOut;
        this.dagIn = dagIn;
    }


    public String getDagout() {
        return dagOut;
    }

    public void setDagout(String dagOut) {
        this.dagOut = dagOut;
    }
    public String getDagin() {
        return dagIn;
    }

    public void setDagin(String dagIn) {
        this.dagIn = dagIn;
    }


}