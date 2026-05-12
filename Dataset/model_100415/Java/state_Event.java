





import java.util.List;
import java.util.ArrayList;

public class state_Event  {

    private String body;





    private state_Trigger state_trigger;


    public state_Event(
        String body    ) {
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public state_Trigger getState_trigger() {
        return state_trigger;
    }

    public void setState_trigger(state_Trigger state_trigger) {
        this.state_trigger = state_trigger;
    }

}