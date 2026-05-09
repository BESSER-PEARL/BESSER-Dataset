





import java.util.List;
import java.util.ArrayList;

public class trialStatemachine_LabeledTransition  {

    private String id;





    private trialStatemachine_State trialstatemachine_state;




    private trialStatemachine_Action trialstatemachine_action;




    private trialStatemachine_State trialstatemachine_state;


    public trialStatemachine_LabeledTransition(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public trialStatemachine_State getTrialstatemachine_state() {
        return trialstatemachine_state;
    }

    public void setTrialstatemachine_state(trialStatemachine_State trialstatemachine_state) {
        this.trialstatemachine_state = trialstatemachine_state;
    }
    public trialStatemachine_Action getTrialstatemachine_action() {
        return trialstatemachine_action;
    }

    public void setTrialstatemachine_action(trialStatemachine_Action trialstatemachine_action) {
        this.trialstatemachine_action = trialstatemachine_action;
    }
    public trialStatemachine_State getTrialstatemachine_state() {
        return trialstatemachine_state;
    }

    public void setTrialstatemachine_state(trialStatemachine_State trialstatemachine_state) {
        this.trialstatemachine_state = trialstatemachine_state;
    }

}