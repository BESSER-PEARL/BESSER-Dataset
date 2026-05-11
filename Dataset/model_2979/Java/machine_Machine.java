





import java.util.List;
import java.util.ArrayList;

public class machine_Machine  {






    private List<machine_State> machine_states;




    private List<machine_Transition> machine_transitions;


    public machine_Machine(
    ) {
        this.machine_states = new ArrayList<>();
        this.machine_transitions = new ArrayList<>();
    }

    public machine_Machine(
        ArrayList<machine_State> machine_states,        ArrayList<machine_Transition> machine_transitions    ) {
        this.machine_states = machine_states;
        this.machine_transitions = machine_transitions;
    }


    public List<machine_State> getMachine_states() {
        return machine_states;
    }

    public void addMachine_state(Machine_state machine_state) {
        this.machine_states.add(machine_state);
    }
    public List<machine_Transition> getMachine_transitions() {
        return machine_transitions;
    }

    public void addMachine_transition(Machine_transition machine_transition) {
        this.machine_transitions.add(machine_transition);
    }

}