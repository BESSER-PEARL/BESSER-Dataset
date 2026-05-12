





import java.util.List;
import java.util.ArrayList;

public class stateMachineActions_EventAction  {

    private String eventExtension;
    private String eventName;





    private stateMachineActions_Action statemachineactions_action;


    public stateMachineActions_EventAction(
        String eventExtension,        String eventName    ) {
        this.eventExtension = eventExtension;
        this.eventName = eventName;
    }


    public String getEventextension() {
        return eventExtension;
    }

    public void setEventextension(String eventExtension) {
        this.eventExtension = eventExtension;
    }
    public String getEventname() {
        return eventName;
    }

    public void setEventname(String eventName) {
        this.eventName = eventName;
    }

    public stateMachineActions_Action getStatemachineactions_action() {
        return statemachineactions_action;
    }

    public void setStatemachineactions_action(stateMachineActions_Action statemachineactions_action) {
        this.statemachineactions_action = statemachineactions_action;
    }

}