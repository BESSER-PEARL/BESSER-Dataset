





import java.util.List;
import java.util.ArrayList;

public class rtsc_Realtimestatechart extends NamedElement, Behavior {

    private int rounds;





    private rtsc_Clock rtsc_clock;




    private rtsc_State rtsc_state;




    private rtsc_State rtsc_state;




    private rtsc_State rtsc_state;




    private rtsc_Variable rtsc_variable;




    private rtsc_Transition rtsc_transition;




    private List<rtsc_State> rtsc_states;




    private List<rtsc_Variable> rtsc_variables;




    private List<rtsc_Transition> rtsc_transitions;




    private List<rtsc_Clock> rtsc_clocks;


    public rtsc_Realtimestatechart(
        int rounds    ) {
        super(
        );
        this.rounds = rounds;
        this.rtsc_states = new ArrayList<>();
        this.rtsc_variables = new ArrayList<>();
        this.rtsc_transitions = new ArrayList<>();
        this.rtsc_clocks = new ArrayList<>();
    }

    public rtsc_Realtimestatechart(
        int rounds        ArrayList<rtsc_State> rtsc_states,        ArrayList<rtsc_Variable> rtsc_variables,        ArrayList<rtsc_Transition> rtsc_transitions,        ArrayList<rtsc_Clock> rtsc_clocks    ) {
        this.rounds = rounds;
        this.rtsc_states = rtsc_states;
        this.rtsc_variables = rtsc_variables;
        this.rtsc_transitions = rtsc_transitions;
        this.rtsc_clocks = rtsc_clocks;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public rtsc_Clock getRtsc_clock() {
        return rtsc_clock;
    }

    public void setRtsc_clock(rtsc_Clock rtsc_clock) {
        this.rtsc_clock = rtsc_clock;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public rtsc_Variable getRtsc_variable() {
        return rtsc_variable;
    }

    public void setRtsc_variable(rtsc_Variable rtsc_variable) {
        this.rtsc_variable = rtsc_variable;
    }
    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }
    public List<rtsc_State> getRtsc_states() {
        return rtsc_states;
    }

    public void addRtsc_state(Rtsc_state rtsc_state) {
        this.rtsc_states.add(rtsc_state);
    }
    public List<rtsc_Variable> getRtsc_variables() {
        return rtsc_variables;
    }

    public void addRtsc_variable(Rtsc_variable rtsc_variable) {
        this.rtsc_variables.add(rtsc_variable);
    }
    public List<rtsc_Transition> getRtsc_transitions() {
        return rtsc_transitions;
    }

    public void addRtsc_transition(Rtsc_transition rtsc_transition) {
        this.rtsc_transitions.add(rtsc_transition);
    }
    public List<rtsc_Clock> getRtsc_clocks() {
        return rtsc_clocks;
    }

    public void addRtsc_clock(Rtsc_clock rtsc_clock) {
        this.rtsc_clocks.add(rtsc_clock);
    }

}