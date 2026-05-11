





import java.util.List;
import java.util.ArrayList;

public class ram_StateMachine  {






    private ram_State ram_state;




    private List<ram_State> ram_states;




    private ram_StateView ram_stateview;




    private List<ram_Transition> ram_transitions;


    public ram_StateMachine(
    ) {
        this.ram_states = new ArrayList<>();
        this.ram_transitions = new ArrayList<>();
    }

    public ram_StateMachine(
        ArrayList<ram_State> ram_states,        ArrayList<ram_Transition> ram_transitions    ) {
        this.ram_states = ram_states;
        this.ram_transitions = ram_transitions;
    }


    public ram_State getRam_state() {
        return ram_state;
    }

    public void setRam_state(ram_State ram_state) {
        this.ram_state = ram_state;
    }
    public List<ram_State> getRam_states() {
        return ram_states;
    }

    public void addRam_state(Ram_state ram_state) {
        this.ram_states.add(ram_state);
    }
    public ram_StateView getRam_stateview() {
        return ram_stateview;
    }

    public void setRam_stateview(ram_StateView ram_stateview) {
        this.ram_stateview = ram_stateview;
    }
    public List<ram_Transition> getRam_transitions() {
        return ram_transitions;
    }

    public void addRam_transition(Ram_transition ram_transition) {
        this.ram_transitions.add(ram_transition);
    }

}