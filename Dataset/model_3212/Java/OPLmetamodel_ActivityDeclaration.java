





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_ActivityDeclaration extends Declaration {

    private String latestEndTime;
    private String earliestStartTime;



    public OPLmetamodel_ActivityDeclaration(
        String latestEndTime,        String earliestStartTime    ) {
        super(
        );
        this.latestEndTime = latestEndTime;
        this.earliestStartTime = earliestStartTime;
    }


    public String getLatestendtime() {
        return latestEndTime;
    }

    public void setLatestendtime(String latestEndTime) {
        this.latestEndTime = latestEndTime;
    }
    public String getEarlieststarttime() {
        return earliestStartTime;
    }

    public void setEarlieststarttime(String earliestStartTime) {
        this.earliestStartTime = earliestStartTime;
    }


}