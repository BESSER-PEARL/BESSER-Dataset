





import java.util.List;
import java.util.ArrayList;

public class trace_GlobalState  {






    private List<EventOccurrence> eventoccurrences;




    private List<C_c_State> c_c_states;




    private trace_Trace trace_trace;




    private List<A_a_State> a_a_states;




    private List<B_b_State> b_b_states;


    public trace_GlobalState(
    ) {
        this.eventoccurrences = new ArrayList<>();
        this.c_c_states = new ArrayList<>();
        this.a_a_states = new ArrayList<>();
        this.b_b_states = new ArrayList<>();
    }

    public trace_GlobalState(
        ArrayList<EventOccurrence> eventoccurrences,        ArrayList<C_c_State> c_c_states,        ArrayList<A_a_State> a_a_states,        ArrayList<B_b_State> b_b_states    ) {
        this.eventoccurrences = eventoccurrences;
        this.c_c_states = c_c_states;
        this.a_a_states = a_a_states;
        this.b_b_states = b_b_states;
    }


    public List<EventOccurrence> getEventoccurrences() {
        return eventoccurrences;
    }

    public void addEventoccurrence(Eventoccurrence eventoccurrence) {
        this.eventoccurrences.add(eventoccurrence);
    }
    public List<C_c_State> getC_c_states() {
        return c_c_states;
    }

    public void addC_c_state(C_c_state c_c_state) {
        this.c_c_states.add(c_c_state);
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public List<A_a_State> getA_a_states() {
        return a_a_states;
    }

    public void addA_a_state(A_a_state a_a_state) {
        this.a_a_states.add(a_a_state);
    }
    public List<B_b_State> getB_b_states() {
        return b_b_states;
    }

    public void addB_b_state(B_b_state b_b_state) {
        this.b_b_states.add(b_b_state);
    }

}