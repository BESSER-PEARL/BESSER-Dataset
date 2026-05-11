





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Trace  {






    private List<activitydiagram_ActivityNode> activitydiagram_activitynodes;


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

}