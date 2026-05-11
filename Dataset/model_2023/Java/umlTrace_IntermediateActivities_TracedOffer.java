





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedOffer  {






    private List<Offer_offeredTokens_Value> offer_offeredtokens_values;


    public umlTrace_IntermediateActivities_TracedOffer(
    ) {
        this.offer_offeredtokens_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedOffer(
        ArrayList<Offer_offeredTokens_Value> offer_offeredtokens_values    ) {
        this.offer_offeredtokens_values = offer_offeredtokens_values;
    }


    public List<Offer_offeredTokens_Value> getOffer_offeredtokens_values() {
        return offer_offeredtokens_values;
    }

    public void addOffer_offeredtokens_value(Offer_offeredtokens_value offer_offeredtokens_value) {
        this.offer_offeredtokens_values.add(offer_offeredtokens_value);
    }

}