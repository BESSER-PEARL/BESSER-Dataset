





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ActivityNode  {






    private ActivitiesProv_Activity activitiesprov_activity;




    private List<ActivitiesProv_ActivityNode> activitiesprov_activitynodes;


    public ActivitiesProv_ActivityNode(
    ) {
        this.activitiesprov_activitynodes = new ArrayList<>();
    }

    public ActivitiesProv_ActivityNode(
        ArrayList<ActivitiesProv_ActivityNode> activitiesprov_activitynodes    ) {
        this.activitiesprov_activitynodes = activitiesprov_activitynodes;
    }


    public ActivitiesProv_Activity getActivitiesprov_activity() {
        return activitiesprov_activity;
    }

    public void setActivitiesprov_activity(ActivitiesProv_Activity activitiesprov_activity) {
        this.activitiesprov_activity = activitiesprov_activity;
    }
    public List<ActivitiesProv_ActivityNode> getActivitiesprov_activitynodes() {
        return activitiesprov_activitynodes;
    }

    public void addActivitiesprov_activitynode(Activitiesprov_activitynode activitiesprov_activitynode) {
        this.activitiesprov_activitynodes.add(activitiesprov_activitynode);
    }

}