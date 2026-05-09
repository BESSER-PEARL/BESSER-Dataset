





import java.util.List;
import java.util.ArrayList;

public class fUML_IntermediateActivities_ActivityNode extends RedefinableElement {






    private List<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges;




    private CompleteStructuredActivities_StructuredActivityNode completestructuredactivities_structuredactivitynode;




    private IntermediateActivities_Activity intermediateactivities_activity;




    private List<IntermediateActivities_ActivityEdge> intermediateactivities_activityedges;


    public fUML_IntermediateActivities_ActivityNode(
    ) {
        super(
        );
        this.intermediateactivities_activityedges = new ArrayList<>();
        this.intermediateactivities_activityedges = new ArrayList<>();
    }

    public fUML_IntermediateActivities_ActivityNode(
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
    public CompleteStructuredActivities_StructuredActivityNode getCompletestructuredactivities_structuredactivitynode() {
        return completestructuredactivities_structuredactivitynode;
    }

    public void setCompletestructuredactivities_structuredactivitynode(CompleteStructuredActivities_StructuredActivityNode completestructuredactivities_structuredactivitynode) {
        this.completestructuredactivities_structuredactivitynode = completestructuredactivities_structuredactivitynode;
    }
    public IntermediateActivities_Activity getIntermediateactivities_activity() {
        return intermediateactivities_activity;
    }

    public void setIntermediateactivities_activity(IntermediateActivities_Activity intermediateactivities_activity) {
        this.intermediateactivities_activity = intermediateactivities_activity;
    }
    public List<IntermediateActivities_ActivityEdge> getIntermediateactivities_activityedges() {
        return intermediateactivities_activityedges;
    }

    public void addIntermediateactivities_activityedge(Intermediateactivities_activityedge intermediateactivities_activityedge) {
        this.intermediateactivities_activityedges.add(intermediateactivities_activityedge);
    }

}