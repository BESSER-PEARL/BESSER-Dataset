





import java.util.List;
import java.util.ArrayList;

public class trace_States_ForkedToken_remainingOffersCount_State  {

    private int remainingOffersCount;





    private activitydiagramConfiguration_TracedForkedToken activitydiagramconfiguration_tracedforkedtoken;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_ForkedToken_remainingOffersCount_State(
        int remainingOffersCount    ) {
        this.remainingOffersCount = remainingOffersCount;
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ForkedToken_remainingOffersCount_State(
        int remainingOffersCount        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.remainingOffersCount = remainingOffersCount;
        this.states_trace_globalstates = states_trace_globalstates;
    }

    public int getRemainingofferscount() {
        return remainingOffersCount;
    }

    public void setRemainingofferscount(int remainingOffersCount) {
        this.remainingOffersCount = remainingOffersCount;
    }

    public activitydiagramConfiguration_TracedForkedToken getActivitydiagramconfiguration_tracedforkedtoken() {
        return activitydiagramconfiguration_tracedforkedtoken;
    }

    public void setActivitydiagramconfiguration_tracedforkedtoken(activitydiagramConfiguration_TracedForkedToken activitydiagramconfiguration_tracedforkedtoken) {
        this.activitydiagramconfiguration_tracedforkedtoken = activitydiagramconfiguration_tracedforkedtoken;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}