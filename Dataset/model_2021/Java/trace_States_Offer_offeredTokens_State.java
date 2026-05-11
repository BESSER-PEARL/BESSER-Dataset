





import java.util.List;
import java.util.ArrayList;

public class trace_States_Offer_offeredTokens_State  {






    private List<activitydiagramConfiguration_TracedToken> activitydiagramconfiguration_tracedtokens;




    private List<States_trace_GlobalState> states_trace_globalstates;




    private activitydiagramConfiguration_TracedOffer activitydiagramconfiguration_tracedoffer;


    public trace_States_Offer_offeredTokens_State(
    ) {
        this.activitydiagramconfiguration_tracedtokens = new ArrayList<>();
        this.states_trace_globalstates = new ArrayList<>();
    }

    public trace_States_Offer_offeredTokens_State(
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
    public activitydiagramConfiguration_TracedOffer getActivitydiagramconfiguration_tracedoffer() {
        return activitydiagramconfiguration_tracedoffer;
    }

    public void setActivitydiagramconfiguration_tracedoffer(activitydiagramConfiguration_TracedOffer activitydiagramconfiguration_tracedoffer) {
        this.activitydiagramconfiguration_tracedoffer = activitydiagramconfiguration_tracedoffer;
    }

}