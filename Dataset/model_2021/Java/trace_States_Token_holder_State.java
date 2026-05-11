





import java.util.List;
import java.util.ArrayList;

public class trace_States_Token_holder_State  {






    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode;




    private activitydiagramConfiguration_TracedToken activitydiagramconfiguration_tracedtoken;


    public trace_States_Token_holder_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_Token_holder_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }
    public activitydiagram_TracedActivityNode getActivitydiagram_tracedactivitynode() {
        return activitydiagram_tracedactivitynode;
    }

    public void setActivitydiagram_tracedactivitynode(activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode) {
        this.activitydiagram_tracedactivitynode = activitydiagram_tracedactivitynode;
    }
    public activitydiagramConfiguration_TracedToken getActivitydiagramconfiguration_tracedtoken() {
        return activitydiagramconfiguration_tracedtoken;
    }

    public void setActivitydiagramconfiguration_tracedtoken(activitydiagramConfiguration_TracedToken activitydiagramconfiguration_tracedtoken) {
        this.activitydiagramconfiguration_tracedtoken = activitydiagramconfiguration_tracedtoken;
    }

}