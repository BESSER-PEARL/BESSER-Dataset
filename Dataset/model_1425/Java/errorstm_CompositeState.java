





import java.util.List;
import java.util.ArrayList;

public class errorstm_CompositeState extends AbstractState {






    private List<errorstm_AbstractState> errorstm_abstractstates;




    private List<errorstm_Transition> errorstm_transitions;




    private errorstm_StateMachine errorstm_statemachine;


    public errorstm_CompositeState(
    ) {
        super(
        );
        this.errorstm_abstractstates = new ArrayList<>();
        this.errorstm_transitions = new ArrayList<>();
    }

    public errorstm_CompositeState(
        ArrayList<errorstm_AbstractState> errorstm_abstractstates,        ArrayList<errorstm_Transition> errorstm_transitions    ) {
        this.errorstm_abstractstates = errorstm_abstractstates;
        this.errorstm_transitions = errorstm_transitions;
    }


    public List<errorstm_AbstractState> getErrorstm_abstractstates() {
        return errorstm_abstractstates;
    }

    public void addErrorstm_abstractstate(Errorstm_abstractstate errorstm_abstractstate) {
        this.errorstm_abstractstates.add(errorstm_abstractstate);
    }
    public List<errorstm_Transition> getErrorstm_transitions() {
        return errorstm_transitions;
    }

    public void addErrorstm_transition(Errorstm_transition errorstm_transition) {
        this.errorstm_transitions.add(errorstm_transition);
    }
    public errorstm_StateMachine getErrorstm_statemachine() {
        return errorstm_statemachine;
    }

    public void setErrorstm_statemachine(errorstm_StateMachine errorstm_statemachine) {
        this.errorstm_statemachine = errorstm_statemachine;
    }

}