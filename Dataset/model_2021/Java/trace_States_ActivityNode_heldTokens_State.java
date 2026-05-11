





import java.util.List;
import java.util.ArrayList;

public class trace_States_ActivityNode_heldTokens_State  {






    private List<activitydiagramConfiguration_TracedToken> activitydiagramconfiguration_tracedtokens;




    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagram_TracedActivityNode activitydiagram_tracedactivitynode;


    public trace_States_ActivityNode_heldTokens_State(
    ) {
        this.activitydiagramconfiguration_tracedtokens = new ArrayList<>();
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ActivityNode_heldTokens_State(
        ArrayList<activitydiagramConfiguration_TracedToken> activitydiagramconfiguration_tracedtokens,        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.activitydiagramconfiguration_tracedtokens = activitydiagramconfiguration_tracedtokens;
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<activitydiagramConfiguration_TracedToken> getActivitydiagramconfiguration_tracedtokens() {
        return activitydiagramconfiguration_tracedtokens;
    }

    public void addActivitydiagramconfiguration_tracedtoken(Activitydiagramconfiguration_tracedtoken activitydiagramconfiguration_tracedtoken) {
        this.activitydiagramconfiguration_tracedtokens.add(activitydiagramconfiguration_tracedtoken);
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

}