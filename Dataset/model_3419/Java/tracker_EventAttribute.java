





import java.util.List;
import java.util.ArrayList;

public class tracker_EventAttribute  {

    private String key;
    private String value;





    private tracker_GenericEvent tracker_genericevent;


    public tracker_EventAttribute(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public tracker_GenericEvent getTracker_genericevent() {
        return tracker_genericevent;
    }

    public void setTracker_genericevent(tracker_GenericEvent tracker_genericevent) {
        this.tracker_genericevent = tracker_genericevent;
    }

}