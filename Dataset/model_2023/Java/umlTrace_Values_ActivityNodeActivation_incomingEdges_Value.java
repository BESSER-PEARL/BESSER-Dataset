





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ActivityNodeActivation_incomingEdges_Value  {






    private List<IntermediateActivities_TracedActivityEdgeInstance> intermediateactivities_tracedactivityedgeinstances;


    public umlTrace_Values_ActivityNodeActivation_incomingEdges_Value(
    ) {
        this.intermediateactivities_tracedactivityedgeinstances = new ArrayList<>();
    }

    public umlTrace_Values_ActivityNodeActivation_incomingEdges_Value(
        ArrayList<IntermediateActivities_TracedActivityEdgeInstance> intermediateactivities_tracedactivityedgeinstances    ) {
        this.intermediateactivities_tracedactivityedgeinstances = intermediateactivities_tracedactivityedgeinstances;
    }


    public List<IntermediateActivities_TracedActivityEdgeInstance> getIntermediateactivities_tracedactivityedgeinstances() {
        return intermediateactivities_tracedactivityedgeinstances;
    }

    public void addIntermediateactivities_tracedactivityedgeinstance(Intermediateactivities_tracedactivityedgeinstance intermediateactivities_tracedactivityedgeinstance) {
        this.intermediateactivities_tracedactivityedgeinstances.add(intermediateactivities_tracedactivityedgeinstance);
    }

}