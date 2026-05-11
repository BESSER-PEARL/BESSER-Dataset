





import java.util.List;
import java.util.ArrayList;

public class FlowDesigner_Event  {

    private String action;
    private String event;
    private String guard;



    public FlowDesigner_Event(
        String action,        String event,        String guard    ) {
        this.action = action;
        this.event = event;
        this.guard = guard;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }


}