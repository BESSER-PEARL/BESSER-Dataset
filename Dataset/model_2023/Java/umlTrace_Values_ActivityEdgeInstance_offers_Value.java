





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ActivityEdgeInstance_offers_Value  {






    private List<IntermediateActivities_TracedOffer> intermediateactivities_tracedoffers;




    private IntermediateActivities_TracedActivityEdgeInstance intermediateactivities_tracedactivityedgeinstance;


    public umlTrace_Values_ActivityEdgeInstance_offers_Value(
    ) {
        this.intermediateactivities_tracedoffers = new ArrayList<>();
    }

    public umlTrace_Values_ActivityEdgeInstance_offers_Value(
        ArrayList<IntermediateActivities_TracedOffer> intermediateactivities_tracedoffers    ) {
        this.intermediateactivities_tracedoffers = intermediateactivities_tracedoffers;
    }


    public List<IntermediateActivities_TracedOffer> getIntermediateactivities_tracedoffers() {
        return intermediateactivities_tracedoffers;
    }

    public void addIntermediateactivities_tracedoffer(Intermediateactivities_tracedoffer intermediateactivities_tracedoffer) {
        this.intermediateactivities_tracedoffers.add(intermediateactivities_tracedoffer);
    }
    public IntermediateActivities_TracedActivityEdgeInstance getIntermediateactivities_tracedactivityedgeinstance() {
        return intermediateactivities_tracedactivityedgeinstance;
    }

    public void setIntermediateactivities_tracedactivityedgeinstance(IntermediateActivities_TracedActivityEdgeInstance intermediateactivities_tracedactivityedgeinstance) {
        this.intermediateactivities_tracedactivityedgeinstance = intermediateactivities_tracedactivityedgeinstance;
    }

}