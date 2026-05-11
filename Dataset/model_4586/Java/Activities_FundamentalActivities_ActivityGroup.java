





import java.util.List;
import java.util.ArrayList;

public class Activities_FundamentalActivities_ActivityGroup extends NamedElement {






    private List<ActivityGroup> activitygroups;




    private List<ActivityNode> activitynodes;




    private List<ActivityEdge> activityedges;




    private ActivityGroup activitygroup;


    public Activities_FundamentalActivities_ActivityGroup(
    ) {
        super(
        );
        this.activitygroups = new ArrayList<>();
        this.activitynodes = new ArrayList<>();
        this.activityedges = new ArrayList<>();
    }

    public Activities_FundamentalActivities_ActivityGroup(
        ArrayList<ActivityGroup> activitygroups,        ArrayList<ActivityNode> activitynodes,        ArrayList<ActivityEdge> activityedges    ) {
        this.activitygroups = activitygroups;
        this.activitynodes = activitynodes;
        this.activityedges = activityedges;
    }


    public List<ActivityGroup> getActivitygroups() {
        return activitygroups;
    }

    public void addActivitygroup(Activitygroup activitygroup) {
        this.activitygroups.add(activitygroup);
    }
    public List<ActivityNode> getActivitynodes() {
        return activitynodes;
    }

    public void addActivitynode(Activitynode activitynode) {
        this.activitynodes.add(activitynode);
    }
    public List<ActivityEdge> getActivityedges() {
        return activityedges;
    }

    public void addActivityedge(Activityedge activityedge) {
        this.activityedges.add(activityedge);
    }
    public ActivityGroup getActivitygroup() {
        return activitygroup;
    }

    public void setActivitygroup(ActivityGroup activitygroup) {
        this.activitygroup = activitygroup;
    }

}