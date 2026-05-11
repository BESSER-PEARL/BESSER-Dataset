





import java.util.List;
import java.util.ArrayList;

public class PiServiceComposition_Rule  {

    private String event;
    private String condition;
    private String name;
    private String action;



    public PiServiceComposition_Rule(
        String event,        String condition,        String name,        String action    ) {
        this.event = event;
        this.condition = condition;
        this.name = name;
        this.action = action;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}