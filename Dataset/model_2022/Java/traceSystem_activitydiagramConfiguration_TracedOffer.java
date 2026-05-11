





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagramConfiguration_TracedOffer  {






    private List<Offer_offeredTokens_State> offer_offeredtokens_states;


    public traceSystem_activitydiagramConfiguration_TracedOffer(
    ) {
        this.offer_offeredtokens_states = new ArrayList<>();
    }

    public traceSystem_activitydiagramConfiguration_TracedOffer(
        ArrayList<Offer_offeredTokens_State> offer_offeredtokens_states    ) {
        this.offer_offeredtokens_states = offer_offeredtokens_states;
    }


    public List<Offer_offeredTokens_State> getOffer_offeredtokens_states() {
        return offer_offeredtokens_states;
    }

    public void addOffer_offeredtokens_state(Offer_offeredtokens_state offer_offeredtokens_state) {
        this.offer_offeredtokens_states.add(offer_offeredtokens_state);
    }

}