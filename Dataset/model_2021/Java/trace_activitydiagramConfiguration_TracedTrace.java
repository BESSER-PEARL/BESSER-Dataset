





import java.util.List;
import java.util.ArrayList;

public class trace_activitydiagramConfiguration_TracedTrace  {






    private List<Trace_executedNodes_State> trace_executednodes_states;


    public trace_activitydiagramConfiguration_TracedTrace(
    ) {
        this.trace_executednodes_states = new ArrayList<>();
    }

    public trace_activitydiagramConfiguration_TracedTrace(
        ArrayList<Trace_executedNodes_State> trace_executednodes_states    ) {
        this.trace_executednodes_states = trace_executednodes_states;
    }


    public List<Trace_executedNodes_State> getTrace_executednodes_states() {
        return trace_executednodes_states;
    }

    public void addTrace_executednodes_state(Trace_executednodes_state trace_executednodes_state) {
        this.trace_executednodes_states.add(trace_executednodes_state);
    }

}