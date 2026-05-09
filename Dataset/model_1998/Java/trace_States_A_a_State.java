





import java.util.List;
import java.util.ArrayList;

public class trace_States_A_a_State  {

    private int a;





    private model2_TracedA model2_traceda;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_A_a_State(
        int a    ) {
        this.a = a;
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_A_a_State(
        int a        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.a = a;
        this.states_trace_globalstates = states_trace_globalstates;
    }

    public int getA() {
        return a;
    }

    public void setA(int a) {
        this.a = a;
    }

    public model2_TracedA getModel2_traceda() {
        return model2_traceda;
    }

    public void setModel2_traceda(model2_TracedA model2_traceda) {
        this.model2_traceda = model2_traceda;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}