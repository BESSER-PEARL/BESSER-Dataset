





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {






    private List<fsm_Transition> fsm_transitions;




    private List<fsm_Variable> fsm_variables;


    public fsm_StateMachine(
    ) {
        super(
        );
        this.fsm_transitions = new ArrayList<>();
        this.fsm_variables = new ArrayList<>();
    }

    public fsm_StateMachine(
        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_Variable> fsm_variables    ) {
        this.fsm_transitions = fsm_transitions;
        this.fsm_variables = fsm_variables;
    }


    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public List<fsm_Variable> getFsm_variables() {
        return fsm_variables;
    }

    public void addFsm_variable(Fsm_variable fsm_variable) {
        this.fsm_variables.add(fsm_variable);
    }

}