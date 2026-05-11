





import java.util.List;
import java.util.ArrayList;

public class trace_States_ForkedToken_baseTokenIsWithdrawn_State  {

    private boolean baseTokenIsWithdrawn;





    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagramConfiguration_TracedForkedToken activitydiagramconfiguration_tracedforkedtoken;


    public trace_States_ForkedToken_baseTokenIsWithdrawn_State(
        boolean baseTokenIsWithdrawn    ) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ForkedToken_baseTokenIsWithdrawn_State(
        boolean baseTokenIsWithdrawn        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
        this.states_trace_globalstates = states_trace_globalstates;
    }

    public boolean getBasetokeniswithdrawn() {
        return baseTokenIsWithdrawn;
    }

    public void setBasetokeniswithdrawn(boolean baseTokenIsWithdrawn) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
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

}