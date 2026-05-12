





import java.util.List;
import java.util.ArrayList;

public class FSMModel_StateMachineDefinition extends NamedElement {






    private List<FSMModel_State> fsmmodel_states;




    private List<FSMModel_State> fsmmodel_states;




    private List<FSMModel_State> fsmmodel_states;




    private List<FSMModel_Transition> fsmmodel_transitions;


    public FSMModel_StateMachineDefinition(
    ) {
        super(
        );
        this.fsmmodel_states = new ArrayList<>();
        this.fsmmodel_states = new ArrayList<>();
        this.fsmmodel_states = new ArrayList<>();
        this.fsmmodel_transitions = new ArrayList<>();
    }

    public FSMModel_StateMachineDefinition(
        ArrayList<FSMModel_State> fsmmodel_states,        ArrayList<FSMModel_State> fsmmodel_states,        ArrayList<FSMModel_State> fsmmodel_states,        ArrayList<FSMModel_Transition> fsmmodel_transitions    ) {
        this.fsmmodel_states = fsmmodel_states;
        this.fsmmodel_states = fsmmodel_states;
        this.fsmmodel_states = fsmmodel_states;
        this.fsmmodel_transitions = fsmmodel_transitions;
    }


    public List<FSMModel_State> getFsmmodel_states() {
        return fsmmodel_states;
    }

    public void addFsmmodel_state(Fsmmodel_state fsmmodel_state) {
        this.fsmmodel_states.add(fsmmodel_state);
    }
    public List<FSMModel_State> getFsmmodel_states() {
        return fsmmodel_states;
    }

    public void addFsmmodel_state(Fsmmodel_state fsmmodel_state) {
        this.fsmmodel_states.add(fsmmodel_state);
    }
    public List<FSMModel_State> getFsmmodel_states() {
        return fsmmodel_states;
    }

    public void addFsmmodel_state(Fsmmodel_state fsmmodel_state) {
        this.fsmmodel_states.add(fsmmodel_state);
    }
    public List<FSMModel_Transition> getFsmmodel_transitions() {
        return fsmmodel_transitions;
    }

    public void addFsmmodel_transition(Fsmmodel_transition fsmmodel_transition) {
        this.fsmmodel_transitions.add(fsmmodel_transition);
    }

}