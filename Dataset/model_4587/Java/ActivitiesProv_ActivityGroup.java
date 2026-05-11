





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ActivityGroup  {






    private ActivitiesProv_ActivityGroup activitiesprov_activitygroup;




    private ActivitiesProv_Activity activitiesprov_activity;




    private ActivitiesProv_ActivityNode activitiesprov_activitynode;




    private ActivitiesProv_Activity activitiesprov_activity;




    private ActivitiesProv_ActivityGroup activitiesprov_activitygroup;




    private List<ActivitiesProv_ActivityNode> activitiesprov_activitynodes;


    public ActivitiesProv_ActivityGroup(
    ) {
        this.activitiesprov_activitynodes = new ArrayList<>();
    }

    public ActivitiesProv_ActivityGroup(
        ArrayList<ActivitiesProv_ActivityNode> activitiesprov_activitynodes    ) {
        this.activitiesprov_activitynodes = activitiesprov_activitynodes;
    }


    public ActivitiesProv_ActivityGroup getActivitiesprov_activitygroup() {
        return activitiesprov_activitygroup;
    }

    public void setActivitiesprov_activitygroup(ActivitiesProv_ActivityGroup activitiesprov_activitygroup) {
        this.activitiesprov_activitygroup = activitiesprov_activitygroup;
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
    public ActivitiesProv_Activity getActivitiesprov_activity() {
        return activitiesprov_activity;
    }

    public void setActivitiesprov_activity(ActivitiesProv_Activity activitiesprov_activity) {
        this.activitiesprov_activity = activitiesprov_activity;
    }
    public ActivitiesProv_ActivityGroup getActivitiesprov_activitygroup() {
        return activitiesprov_activitygroup;
    }

    public void setActivitiesprov_activitygroup(ActivitiesProv_ActivityGroup activitiesprov_activitygroup) {
        this.activitiesprov_activitygroup = activitiesprov_activitygroup;
    }
    public List<ActivitiesProv_ActivityNode> getActivitiesprov_activitynodes() {
        return activitiesprov_activitynodes;
    }

    public void addActivitiesprov_activitynode(Activitiesprov_activitynode activitiesprov_activitynode) {
        this.activitiesprov_activitynodes.add(activitiesprov_activitynode);
    }

}