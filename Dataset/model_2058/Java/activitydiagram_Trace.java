





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Trace  {






    private List<activitydiagram_ActivityNode> activitydiagram_activitynodes;




    private activitydiagram_Activity activitydiagram_activity;


    public activitydiagram_Trace(
    ) {
        this.activitydiagram_activitynodes = new ArrayList<>();
    }

    public activitydiagram_Trace(
        ArrayList<activitydiagram_ActivityNode> activitydiagram_activitynodes    ) {
        this.activitydiagram_activitynodes = activitydiagram_activitynodes;
    }


    public List<activitydiagram_ActivityNode> getActivitydiagram_activitynodes() {
        return activitydiagram_activitynodes;
    }

    public void addActivitydiagram_activitynode(Activitydiagram_activitynode activitydiagram_activitynode) {
        this.activitydiagram_activitynodes.add(activitydiagram_activitynode);
    }
    public activitydiagram_Activity getActivitydiagram_activity() {
        return activitydiagram_activity;
    }

    public void setActivitydiagram_activity(activitydiagram_Activity activitydiagram_activity) {
        this.activitydiagram_activity = activitydiagram_activity;
    }

}