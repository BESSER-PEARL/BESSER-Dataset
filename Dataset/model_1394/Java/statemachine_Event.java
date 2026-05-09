





import java.util.List;
import java.util.ArrayList;

public class statemachine_Event extends DataElement {

    private String trigger;



    public statemachine_Event(
        String trigger    ) {
        super(
        );
        this.trigger = trigger;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }


}