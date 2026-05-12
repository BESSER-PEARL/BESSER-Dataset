





import java.util.List;
import java.util.ArrayList;

public class statemachine_AbstractState extends Named {






    private statemachine_Statemachine statemachine_statemachine;




    private statemachine_AbstractTransition statemachine_abstracttransition;




    private List<statemachine_AbstractTransition> statemachine_abstracttransitions;


    public statemachine_AbstractState(
    ) {
        super(
        );
        this.statemachine_abstracttransitions = new ArrayList<>();
    }

    public statemachine_AbstractState(
        ArrayList<statemachine_AbstractTransition> statemachine_abstracttransitions    ) {
        this.statemachine_abstracttransitions = statemachine_abstracttransitions;
    }


    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public statemachine_AbstractTransition getStatemachine_abstracttransition() {
        return statemachine_abstracttransition;
    }

    public void setStatemachine_abstracttransition(statemachine_AbstractTransition statemachine_abstracttransition) {
        this.statemachine_abstracttransition = statemachine_abstracttransition;
    }
    public List<statemachine_AbstractTransition> getStatemachine_abstracttransitions() {
        return statemachine_abstracttransitions;
    }

    public void addStatemachine_abstracttransition(Statemachine_abstracttransition statemachine_abstracttransition) {
        this.statemachine_abstracttransitions.add(statemachine_abstracttransition);
    }

}