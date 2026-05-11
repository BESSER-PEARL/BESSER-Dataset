





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_InterruptibleActivityRegion extends ActivityGroup {






    private List<ActivitiesProv_ActivityEdge> activitiesprov_activityedges;




    private ActivitiesProv_ActivityEdge activitiesprov_activityedge;




    private List<ActivitiesProv_ActivityNode> activitiesprov_activitynodes;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;


    public ActivitiesProv_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.activitiesprov_activityedges = new ArrayList<>();
        this.activitiesprov_activitynodes = new ArrayList<>();
    }

    public ActivitiesProv_InterruptibleActivityRegion(
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
    public ActivitiesProv_ActivityEdge getActivitiesprov_activityedge() {
        return activitiesprov_activityedge;
    }

    public void setActivitiesprov_activityedge(ActivitiesProv_ActivityEdge activitiesprov_activityedge) {
        this.activitiesprov_activityedge = activitiesprov_activityedge;
    }
    public List<ActivitiesProv_ActivityNode> getActivitiesprov_activitynodes() {
        return activitiesprov_activitynodes;
    }

    public void addActivitiesprov_activitynode(Activitiesprov_activitynode activitiesprov_activitynode) {
        this.activitiesprov_activitynodes.add(activitiesprov_activitynode);
    }
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
    }

}