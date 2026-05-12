





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_States_Transition_clock_Value  {

    private int clock;





    private List<State> states;




    private petrinetv3_TracedTransition petrinetv3_tracedtransition;


    public petrinetv3Trace_States_Transition_clock_Value(
        int clock    ) {
        this.clock = clock;
        this.states = new ArrayList<>();
    }

    public petrinetv3Trace_States_Transition_clock_Value(
        int clock        ArrayList<State> states    ) {
        this.clock = clock;
        this.states = states;
    }

    public int getClock() {
        return clock;
    }

    public void setClock(int clock) {
        this.clock = clock;
    }

    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }
    public petrinetv3_TracedTransition getPetrinetv3_tracedtransition() {
        return petrinetv3_tracedtransition;
    }

    public void setPetrinetv3_tracedtransition(petrinetv3_TracedTransition petrinetv3_tracedtransition) {
        this.petrinetv3_tracedtransition = petrinetv3_tracedtransition;
    }

}