





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ActivityPartition extends ActivityGroup {






    private List<ActivitiesProv_ActivityEdge> activitiesprov_activityedges;




    private ActivitiesProv_ActivityPartition activitiesprov_activitypartition;




    private ActivitiesProv_Activity activitiesprov_activity;




    private ActivitiesProv_ActivityPartition activitiesprov_activitypartition;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private List<ActivitiesProv_ActivityNode> activitiesprov_activitynodes;




    private ActivitiesProv_ActivityEdge activitiesprov_activityedge;


    public ActivitiesProv_ActivityPartition(
    ) {
        super(
        );
        this.activitiesprov_activityedges = new ArrayList<>();
        this.activitiesprov_activitynodes = new ArrayList<>();
    }

    public ActivitiesProv_ActivityPartition(
        ArrayList<ActivitiesProv_ActivityEdge> activitiesprov_activityedges,        ArrayList<ActivitiesProv_ActivityNode> activitiesprov_activitynodes    ) {
        this.activitiesprov_activityedges = activitiesprov_activityedges;
        this.activitiesprov_activitynodes = activitiesprov_activitynodes;
    }


    public List<ActivitiesProv_ActivityEdge> getActivitiesprov_activityedges() {
        return activitiesprov_activityedges;
    }

    public void addActivitiesprov_activityedge(Activitiesprov_activityedge activitiesprov_activityedge) {
        this.activitiesprov_activityedges.add(activitiesprov_activityedge);
    }
    public ActivitiesProv_ActivityPartition getActivitiesprov_activitypartition() {
        return activitiesprov_activitypartition;
    }

    public void setActivitiesprov_activitypartition(ActivitiesProv_ActivityPartition activitiesprov_activitypartition) {
        this.activitiesprov_activitypartition = activitiesprov_activitypartition;
    }
    public ActivitiesProv_Activity getActivitiesprov_activity() {
        return activitiesprov_activity;
    }

    public void setActivitiesprov_activity(ActivitiesProv_Activity activitiesprov_activity) {
        this.activitiesprov_activity = activitiesprov_activity;
    }
    public ActivitiesProv_ActivityPartition getActivitiesprov_activitypartition() {
        return activitiesprov_activitypartition;
    }

    public void setActivitiesprov_activitypartition(ActivitiesProv_ActivityPartition activitiesprov_activitypartition) {
        this.activitiesprov_activitypartition = activitiesprov_activitypartition;
    }
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
    }
    public List<ActivitiesProv_ActivityNode> getActivitiesprov_activitynodes() {
        return activitiesprov_activitynodes;
    }

    public void addActivitiesprov_activitynode(Activitiesprov_activitynode activitiesprov_activitynode) {
        this.activitiesprov_activitynodes.add(activitiesprov_activitynode);
    }
    public ActivitiesProv_ActivityEdge getActivitiesprov_activityedge() {
        return activitiesprov_activityedge;
    }

    public void setActivitiesprov_activityedge(ActivitiesProv_ActivityEdge activitiesprov_activityedge) {
        this.activitiesprov_activityedge = activitiesprov_activityedge;
    }

}