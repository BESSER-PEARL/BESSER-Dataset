





import java.util.List;
import java.util.ArrayList;

public class trace_States_C_c_State  {






    private model2Configuration_TracedC model2configuration_tracedc;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_C_c_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_C_c_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public model2Configuration_TracedC getModel2configuration_tracedc() {
        return model2configuration_tracedc;
    }

    public void setModel2configuration_tracedc(model2Configuration_TracedC model2configuration_tracedc) {
        this.model2configuration_tracedc = model2configuration_tracedc;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}