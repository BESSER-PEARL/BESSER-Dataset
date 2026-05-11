





import java.util.List;
import java.util.ArrayList;

public class bpmn_Activity extends Vertex, MessageVertex {

    private String looping;
    private String activityType;



    public bpmn_Activity(
        String looping,        String activityType    ) {
        super(
        );
        this.looping = looping;
        this.activityType = activityType;
    }


    public String getLooping() {
        return looping;
    }

    public void setLooping(String looping) {
        this.looping = looping;
    }
    public String getActivitytype() {
        return activityType;
    }

    public void setActivitytype(String activityType) {
        this.activityType = activityType;
    }


}