





import java.util.List;
import java.util.ArrayList;

public class trialStatemachine_Action  {

    private String name;





    private trialStatemachine_Statemachine trialstatemachine_statemachine;


    public trialStatemachine_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public trialStatemachine_Statemachine getTrialstatemachine_statemachine() {
        return trialstatemachine_statemachine;
    }

    public void setTrialstatemachine_statemachine(trialStatemachine_Statemachine trialstatemachine_statemachine) {
        this.trialstatemachine_statemachine = trialstatemachine_statemachine;
    }

}