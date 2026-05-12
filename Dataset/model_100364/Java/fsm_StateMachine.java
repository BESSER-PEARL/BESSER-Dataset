





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {






    private List<fsm_Variable> fsm_variables;




    private fsm_Transition fsm_transition;




    private List<fsm_Transition> fsm_transitions;


    public fsm_StateMachine(
    ) {
        super(
        );
        this.fsm_variables = new ArrayList<>();
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_StateMachine(
        ArrayList<fsm_Variable> fsm_variables,        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.fsm_variables = fsm_variables;
        this.fsm_transitions = fsm_transitions;
    }


    public List<fsm_Variable> getFsm_variables() {
        return fsm_variables;
    }

    public void addFsm_variable(Fsm_variable fsm_variable) {
        this.fsm_variables.add(fsm_variable);
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}