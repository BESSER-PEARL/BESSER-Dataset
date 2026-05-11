





import java.util.List;
import java.util.ArrayList;

public class Activities_IntermediateActivities_InterruptibleActivityRegion extends ActivityGroup {






    private List<ActivityNode> activitynodes;


    public Activities_IntermediateActivities_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.activitynodes = new ArrayList<>();
    }

    public Activities_IntermediateActivities_InterruptibleActivityRegion(
        ArrayList<ActivityNode> activitynodes    ) {
        this.activitynodes = activitynodes;
    }


    public List<ActivityNode> getActivitynodes() {
        return activitynodes;
    }

    public void addActivitynode(Activitynode activitynode) {
        this.activitynodes.add(activitynode);
    }

}