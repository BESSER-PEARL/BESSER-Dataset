





import java.util.List;
import java.util.ArrayList;

public class trace_States_Variable_currentValue_State  {






    private activitydiagram_TracedVariable activitydiagram_tracedvariable;




    private States_trace_Value states_trace_value;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_Variable_currentValue_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_Variable_currentValue_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public activitydiagram_TracedVariable getActivitydiagram_tracedvariable() {
        return activitydiagram_tracedvariable;
    }

    public void setActivitydiagram_tracedvariable(activitydiagram_TracedVariable activitydiagram_tracedvariable) {
        this.activitydiagram_tracedvariable = activitydiagram_tracedvariable;
    }
    public States_trace_Value getStates_trace_value() {
        return states_trace_value;
    }

    public void setStates_trace_value(States_trace_Value states_trace_value) {
        this.states_trace_value = states_trace_value;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}