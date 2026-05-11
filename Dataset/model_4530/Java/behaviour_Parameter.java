





import java.util.List;
import java.util.ArrayList;

public class behaviour_Parameter  {

    private String value;
    private String key;





    private behaviour_Feedback behaviour_feedback;




    private behaviour_DeviceAction behaviour_deviceaction;


    public behaviour_Parameter(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public behaviour_Feedback getBehaviour_feedback() {
        return behaviour_feedback;
    }

    public void setBehaviour_feedback(behaviour_Feedback behaviour_feedback) {
        this.behaviour_feedback = behaviour_feedback;
    }
    public behaviour_DeviceAction getBehaviour_deviceaction() {
        return behaviour_deviceaction;
    }

    public void setBehaviour_deviceaction(behaviour_DeviceAction behaviour_deviceaction) {
        this.behaviour_deviceaction = behaviour_deviceaction;
    }

}