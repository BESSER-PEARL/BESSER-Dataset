





import java.util.List;
import java.util.ArrayList;

public class statemachine103_StateMachineObject  {

    private String label;





    private statemachine103_StateMachine statemachine103_statemachine;


    public statemachine103_StateMachineObject(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public statemachine103_StateMachine getStatemachine103_statemachine() {
        return statemachine103_statemachine;
    }

    public void setStatemachine103_statemachine(statemachine103_StateMachine statemachine103_statemachine) {
        this.statemachine103_statemachine = statemachine103_statemachine;
    }

}