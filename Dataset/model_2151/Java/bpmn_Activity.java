





import java.util.List;
import java.util.ArrayList;

public class bpmn_Activity extends Vertex, NamedBpmnObject {

    private String orderedMessages;
    private String looping;
    private String activityType;



    public bpmn_Activity(
        String orderedMessages,        String looping,        String activityType    ) {
        super(
        );
        this.orderedMessages = orderedMessages;
        this.looping = looping;
        this.activityType = activityType;
    }


    public String getOrderedmessages() {
        return orderedMessages;
    }

    public void setOrderedmessages(String orderedMessages) {
        this.orderedMessages = orderedMessages;
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