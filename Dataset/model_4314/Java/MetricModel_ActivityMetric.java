





import java.util.List;
import java.util.ArrayList;

public class MetricModel_ActivityMetric extends Metric {

    private String activityBegin;
    private String activityEnd;



    public MetricModel_ActivityMetric(
        String activityBegin,        String activityEnd    ) {
        super(
        );
        this.activityBegin = activityBegin;
        this.activityEnd = activityEnd;
    }


    public String getActivitybegin() {
        return activityBegin;
    }

    public void setActivitybegin(String activityBegin) {
        this.activityBegin = activityBegin;
    }
    public String getActivityend() {
        return activityEnd;
    }

    public void setActivityend(String activityEnd) {
        this.activityEnd = activityEnd;
    }


}