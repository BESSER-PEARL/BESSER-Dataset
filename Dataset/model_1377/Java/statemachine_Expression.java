





import java.util.List;
import java.util.ArrayList;

public class statemachine_Expression  {






    private statemachine_Transition statemachine_transition;




    private statemachine_PrintCommand statemachine_printcommand;


    public statemachine_Expression(
    ) {
    }



    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_PrintCommand getStatemachine_printcommand() {
        return statemachine_printcommand;
    }

    public void setStatemachine_printcommand(statemachine_PrintCommand statemachine_printcommand) {
        this.statemachine_printcommand = statemachine_printcommand;
    }

}