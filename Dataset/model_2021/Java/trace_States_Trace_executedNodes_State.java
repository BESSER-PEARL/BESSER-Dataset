





import java.util.List;
import java.util.ArrayList;

public class trace_States_Trace_executedNodes_State  {






    private List<States_trace_GlobalState> states_trace_globalstates;




    private List<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes;


    public trace_States_Trace_executedNodes_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
        this.activitydiagram_tracedactivitynodes = new ArrayList<>();
    }

    public trace_States_Trace_executedNodes_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates,        ArrayList<activitydiagram_TracedActivityNode> activitydiagram_tracedactivitynodes    ) {
        this.states_trace_globalstates = states_trace_globalstates;
        this.activitydiagram_tracedactivitynodes = activitydiagram_tracedactivitynodes;
    }


    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }
    public List<activitydiagram_TracedActivityNode> getActivitydiagram_tracedactivitynodes() {
        return activitydiagram_tracedactivitynodes;
    }

    public void addActivitydiagram_tracedactivitynode(Activitydiagram_tracedactivitynode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynodes.add(activitydiagram_tracedactivitynode);
    }

}