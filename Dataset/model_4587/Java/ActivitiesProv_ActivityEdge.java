





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ActivityEdge  {






    private ActivitiesProv_ActivityGroup activitiesprov_activitygroup;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private ActivitiesProv_Activity activitiesprov_activity;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private List<ActivitiesProv_ActivityGroup> activitiesprov_activitygroups;




    private List<ActivitiesProv_ActivityEdge> activitiesprov_activityedges;


    public ActivitiesProv_ActivityEdge(
    ) {
        this.activitiesprov_activitygroups = new ArrayList<>();
        this.activitiesprov_activityedges = new ArrayList<>();
    }

    public ActivitiesProv_ActivityEdge(
        ArrayList<ActivitiesProv_ActivityGroup> activitiesprov_activitygroups,        ArrayList<ActivitiesProv_ActivityEdge> activitiesprov_activityedges    ) {
        this.activitiesprov_activitygroups = activitiesprov_activitygroups;
        this.activitiesprov_activityedges = activitiesprov_activityedges;
    }


    public ActivitiesProv_ActivityGroup getActivitiesprov_activitygroup() {
        return activitiesprov_activitygroup;
    }

    public void setActivitiesprov_activitygroup(ActivitiesProv_ActivityGroup activitiesprov_activitygroup) {
        this.activitiesprov_activitygroup = activitiesprov_activitygroup;
    }
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
    }
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
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
    public ActivitiesProv_ActivityNode getActivitiesprov_activitynode() {
        return activitiesprov_activitynode;
    }

    public void setActivitiesprov_activitynode(ActivitiesProv_ActivityNode activitiesprov_activitynode) {
        this.activitiesprov_activitynode = activitiesprov_activitynode;
    }
    public List<ActivitiesProv_ActivityGroup> getActivitiesprov_activitygroups() {
        return activitiesprov_activitygroups;
    }

    public void addActivitiesprov_activitygroup(Activitiesprov_activitygroup activitiesprov_activitygroup) {
        this.activitiesprov_activitygroups.add(activitiesprov_activitygroup);
    }
    public List<ActivitiesProv_ActivityEdge> getActivitiesprov_activityedges() {
        return activitiesprov_activityedges;
    }

    public void addActivitiesprov_activityedge(Activitiesprov_activityedge activitiesprov_activityedge) {
        this.activitiesprov_activityedges.add(activitiesprov_activityedge);
    }

}