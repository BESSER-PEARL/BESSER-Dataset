





import java.util.List;
import java.util.ArrayList;

public class trace_States_Activity_trace_State  {






    private activitydiagram_TracedActivity activitydiagram_tracedactivity;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_Activity_trace_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_Activity_trace_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public activitydiagram_TracedActivity getActivitydiagram_tracedactivity() {
        return activitydiagram_tracedactivity;
    }

    public void setActivitydiagram_tracedactivity(activitydiagram_TracedActivity activitydiagram_tracedactivity) {
        this.activitydiagram_tracedactivity = activitydiagram_tracedactivity;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}