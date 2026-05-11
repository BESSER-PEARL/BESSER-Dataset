





import java.util.List;
import java.util.ArrayList;

public class trace_States_ForkedToken_baseToken_State  {






    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagramConfiguration_TracedForkedToken activitydiagramconfiguration_tracedforkedtoken;




    private activitydiagramConfiguration_TracedToken activitydiagramconfiguration_tracedtoken;


    public trace_States_ForkedToken_baseToken_State(
    ) {
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ForkedToken_baseToken_State(
        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }
    public activitydiagramConfiguration_TracedForkedToken getActivitydiagramconfiguration_tracedforkedtoken() {
        return activitydiagramconfiguration_tracedforkedtoken;
    }

    public void setActivitydiagramconfiguration_tracedforkedtoken(activitydiagramConfiguration_TracedForkedToken activitydiagramconfiguration_tracedforkedtoken) {
        this.activitydiagramconfiguration_tracedforkedtoken = activitydiagramconfiguration_tracedforkedtoken;
    }
    public activitydiagramConfiguration_TracedToken getActivitydiagramconfiguration_tracedtoken() {
        return activitydiagramconfiguration_tracedtoken;
    }

    public void setActivitydiagramconfiguration_tracedtoken(activitydiagramConfiguration_TracedToken activitydiagramconfiguration_tracedtoken) {
        this.activitydiagramconfiguration_tracedtoken = activitydiagramconfiguration_tracedtoken;
    }

}