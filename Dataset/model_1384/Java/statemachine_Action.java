





import java.util.List;
import java.util.ArrayList;

public class statemachine_Action  {

    private String name;





    private statemachine_LabeledTransition statemachine_labeledtransition;




    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_LabeledTransition getStatemachine_labeledtransition() {
        return statemachine_labeledtransition;
    }

    public void setStatemachine_labeledtransition(statemachine_LabeledTransition statemachine_labeledtransition) {
        this.statemachine_labeledtransition = statemachine_labeledtransition;
    }
    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}