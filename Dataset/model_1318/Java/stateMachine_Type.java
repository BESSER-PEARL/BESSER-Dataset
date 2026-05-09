





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Type  {

    private String type;





    private stateMachine_Event statemachine_event;


    public stateMachine_Type(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public stateMachine_Event getStatemachine_event() {
        return statemachine_event;
    }

    public void setStatemachine_event(stateMachine_Event statemachine_event) {
        this.statemachine_event = statemachine_event;
    }

}