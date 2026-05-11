





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_StructuredActivityNode extends ExecutableNode, ActivityGroup {

    private boolean mustIsolate;





    private List<ActivitiesProv_ActivityNode> activitiesprov_activitynodes;




    private ActivitiesProv_Activity activitiesprov_activity;




    private List<ActivitiesProv_ActivityEdge> activitiesprov_activityedges;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private ActivitiesProv_Activity activitiesprov_activity;




    private ActivitiesProv_ActivityEdge activitiesprov_activityedge;


    public ActivitiesProv_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.activitiesprov_activitynodes = new ArrayList<>();
        this.activitiesprov_activityedges = new ArrayList<>();
    }

    public ActivitiesProv_StructuredActivityNode(
        boolean mustIsolate        ArrayList<ActivitiesProv_ActivityNode> activitiesprov_activitynodes,        ArrayList<ActivitiesProv_ActivityEdge> activitiesprov_activityedges    ) {
        this.mustIsolate = mustIsolate;
        this.activitiesprov_activitynodes = activitiesprov_activitynodes;
        this.activitiesprov_activityedges = activitiesprov_activityedges;
    }

    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
    }

    public List<ActivitiesProv_ActivityNode> getActivitiesprov_activitynodes() {
        return activitiesprov_activitynodes;
    }

    public void addActivitiesprov_activitynode(Activitiesprov_activitynode activitiesprov_activitynode) {
        this.activitiesprov_activitynodes.add(activitiesprov_activitynode);
    }
    public ActivitiesProv_Activity getActivitiesprov_activity() {
        return activitiesprov_activity;
    }

    public void setActivitiesprov_activity(ActivitiesProv_Activity activitiesprov_activity) {
        this.activitiesprov_activity = activitiesprov_activity;
    }
    public List<ActivitiesProv_ActivityEdge> getActivitiesprov_activityedges() {
        return activitiesprov_activityedges;
    }

    public void addActivitiesprov_activityedge(Activitiesprov_activityedge activitiesprov_activityedge) {
        this.activitiesprov_activityedges.add(activitiesprov_activityedge);
    }
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
    }
    public ActivitiesProv_Activity getActivitiesprov_activity() {
        return activitiesprov_activity;
    }

    public void setActivitiesprov_activity(ActivitiesProv_Activity activitiesprov_activity) {
        this.activitiesprov_activity = activitiesprov_activity;
    }
    public ActivitiesProv_ActivityEdge getActivitiesprov_activityedge() {
        return activitiesprov_activityedge;
    }

    public void setActivitiesprov_activityedge(ActivitiesProv_ActivityEdge activitiesprov_activityedge) {
        this.activitiesprov_activityedge = activitiesprov_activityedge;
    }

}