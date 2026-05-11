





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedObjectNodeActivation extends TracedActivityNodeActivation {






    private List<ObjectNodeActivation_offeredTokenCount_Value> objectnodeactivation_offeredtokencount_values;


    public umlTrace_IntermediateActivities_TracedObjectNodeActivation(
    ) {
        super(
        );
        this.objectnodeactivation_offeredtokencount_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedObjectNodeActivation(
        ArrayList<ObjectNodeActivation_offeredTokenCount_Value> objectnodeactivation_offeredtokencount_values    ) {
        this.objectnodeactivation_offeredtokencount_values = objectnodeactivation_offeredtokencount_values;
    }


    public List<ObjectNodeActivation_offeredTokenCount_Value> getObjectnodeactivation_offeredtokencount_values() {
        return objectnodeactivation_offeredtokencount_values;
    }

    public void addObjectnodeactivation_offeredtokencount_value(Objectnodeactivation_offeredtokencount_value objectnodeactivation_offeredtokencount_value) {
        this.objectnodeactivation_offeredtokencount_values.add(objectnodeactivation_offeredtokencount_value);
    }

}