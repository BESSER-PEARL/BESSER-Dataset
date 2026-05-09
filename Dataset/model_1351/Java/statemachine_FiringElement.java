





import java.util.List;
import java.util.ArrayList;

public class statemachine_FiringElement  {

    private String action;
    private String trigger;



    public statemachine_FiringElement(
        String action,        String trigger    ) {
        this.action = action;
        this.trigger = trigger;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }


}