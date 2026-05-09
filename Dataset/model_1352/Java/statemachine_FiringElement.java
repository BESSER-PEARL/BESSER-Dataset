





import java.util.List;
import java.util.ArrayList;

public class statemachine_FiringElement  {

    private String trigger;
    private String action;



    public statemachine_FiringElement(
        String trigger,        String action    ) {
        this.trigger = trigger;
        this.action = action;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}