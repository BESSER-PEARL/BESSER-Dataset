





import java.util.List;
import java.util.ArrayList;

public class statemachine_Statemachine  {






    private List<statemachine_State> statemachine_states;




    private List<statemachine_Signal> statemachine_signals;


    public statemachine_Statemachine(
    ) {
        this.statemachine_states = new ArrayList<>();
        this.statemachine_signals = new ArrayList<>();
    }

    public statemachine_Statemachine(
        ArrayList<statemachine_State> statemachine_states,        ArrayList<statemachine_Signal> statemachine_signals    ) {
        this.statemachine_states = statemachine_states;
        this.statemachine_signals = statemachine_signals;
    }


    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public List<statemachine_Signal> getStatemachine_signals() {
        return statemachine_signals;
    }

    public void addStatemachine_signal(Statemachine_signal statemachine_signal) {
        this.statemachine_signals.add(statemachine_signal);
    }

}