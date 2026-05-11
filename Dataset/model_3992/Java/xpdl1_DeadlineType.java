





import java.util.List;
import java.util.ArrayList;

public class xpdl1_DeadlineType  {

    private String execution;





    private xpdl1_ActivityType xpdl1_activitytype;


    public xpdl1_DeadlineType(
        String execution    ) {
        this.execution = execution;
    }


    public String getExecution() {
        return execution;
    }

    public void setExecution(String execution) {
        this.execution = execution;
    }

    public xpdl1_ActivityType getXpdl1_activitytype() {
        return xpdl1_activitytype;
    }

    public void setXpdl1_activitytype(xpdl1_ActivityType xpdl1_activitytype) {
        this.xpdl1_activitytype = xpdl1_activitytype;
    }

}