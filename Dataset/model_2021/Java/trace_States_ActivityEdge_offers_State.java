





import java.util.List;
import java.util.ArrayList;

public class trace_States_ActivityEdge_offers_State  {






    private List<activitydiagramConfiguration_TracedOffer> activitydiagramconfiguration_tracedoffers;




    private activitydiagram_TracedActivityEdge activitydiagram_tracedactivityedge;




    private List<States_trace_GlobalState> states_trace_globalstates;


    public trace_States_ActivityEdge_offers_State(
    ) {
        this.activitydiagramconfiguration_tracedoffers = new ArrayList<>();
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_ActivityEdge_offers_State(
        ArrayList<activitydiagramConfiguration_TracedOffer> activitydiagramconfiguration_tracedoffers,        ArrayList<States_trace_GlobalState> states_trace_globalstates    ) {
        this.activitydiagramconfiguration_tracedoffers = activitydiagramconfiguration_tracedoffers;
        this.states_trace_globalstates = states_trace_globalstates;
    }


    public List<activitydiagramConfiguration_TracedOffer> getActivitydiagramconfiguration_tracedoffers() {
        return activitydiagramconfiguration_tracedoffers;
    }

    public void addActivitydiagramconfiguration_tracedoffer(Activitydiagramconfiguration_tracedoffer activitydiagramconfiguration_tracedoffer) {
        this.activitydiagramconfiguration_tracedoffers.add(activitydiagramconfiguration_tracedoffer);
    }
    public activitydiagram_TracedActivityEdge getActivitydiagram_tracedactivityedge() {
        return activitydiagram_tracedactivityedge;
    }

    public void setActivitydiagram_tracedactivityedge(activitydiagram_TracedActivityEdge activitydiagram_tracedactivityedge) {
        this.activitydiagram_tracedactivityedge = activitydiagram_tracedactivityedge;
    }
    public List<States_trace_GlobalState> getStates_trace_globalstates() {
        return states_trace_globalstates;
    }

    public void addStates_trace_globalstate(States_trace_globalstate states_trace_globalstate) {
        this.states_trace_globalstates.add(states_trace_globalstate);
    }

}