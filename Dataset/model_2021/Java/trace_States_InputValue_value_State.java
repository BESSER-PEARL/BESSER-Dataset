





import java.util.List;
import java.util.ArrayList;

public class trace_States_InputValue_value_State  {






    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_InputValue_value_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_InputValue_value_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}