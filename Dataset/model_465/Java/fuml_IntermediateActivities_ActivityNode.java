





import java.util.List;
import java.util.ArrayList;

public class fuml_IntermediateActivities_ActivityNode extends RedefinableElement {






    private List<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges;




    private List<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges;




    private CompleteStructuredActivities_StructuredActivityNode completestructuredactivities_structuredactivitynode;


    public fuml_IntermediateActivities_ActivityNode(
    ) {
        super(
        );
        this.intermediateactivities_activityedges = new ArrayList<>();
        this.intermediateactivities_activityedges = new ArrayList<>();
    }

    public fuml_IntermediateActivities_ActivityNode(
        ArrayList<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges,        ArrayList<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges    ) {
        this.intermediateactivities_activityedges = intermediateactivities_activityedges;
        this.intermediateactivities_activityedges = intermediateactivities_activityedges;
    }


    public List<IntermediateActivities_ActivityEdge> getIntermediateactivities_activityedges() {
        return intermediateactivities_activityedges;
    }

    public void addIntermediateactivities_activityedge(Intermediateactivities_activityedge intermediateactivities_activityedge) {
        this.intermediateactivities_activityedges.add(intermediateactivities_activityedge);
    }
    public List<IntermediateActivities_ActivityEdge> getIntermediateactivities_activityedges() {
        return intermediateactivities_activityedges;
    }

    public void addIntermediateactivities_activityedge(Intermediateactivities_activityedge intermediateactivities_activityedge) {
        this.intermediateactivities_activityedges.add(intermediateactivities_activityedge);
    }
    public CompleteStructuredActivities_StructuredActivityNode getCompletestructuredactivities_structuredactivitynode() {
        return completestructuredactivities_structuredactivitynode;
    }

    public void setCompletestructuredactivities_structuredactivitynode(CompleteStructuredActivities_StructuredActivityNode completestructuredactivities_structuredactivitynode) {
        this.completestructuredactivities_structuredactivitynode = completestructuredactivities_structuredactivitynode;
    }

}