





import java.util.List;
import java.util.ArrayList;

public class statemachine_Event  {

    private String id;





    private statemachine_Transition statemachine_transition;




    private statemachine_SM statemachine_sm;


    public statemachine_Event(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_SM getStatemachine_sm() {
        return statemachine_sm;
    }

    public void setStatemachine_sm(statemachine_SM statemachine_sm) {
        this.statemachine_sm = statemachine_sm;
    }

}