





import java.util.List;
import java.util.ArrayList;

public class sipme_Activity extends EnterpriseProcessor {

    private int ActivityDuration;
    private String endingStatus;



    public sipme_Activity(
        int ActivityDuration,        String endingStatus    ) {
        super(
        );
        this.ActivityDuration = ActivityDuration;
        this.endingStatus = endingStatus;
    }


    public int getActivityduration() {
        return ActivityDuration;
    }

    public void setActivityduration(int ActivityDuration) {
        this.ActivityDuration = ActivityDuration;
    }
    public String getEndingstatus() {
        return endingStatus;
    }

    public void setEndingstatus(String endingStatus) {
        this.endingStatus = endingStatus;
    }


}