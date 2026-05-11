





import java.util.List;
import java.util.ArrayList;

public class Activities_BasicActivities_ActivityEdge extends RedefinableElement {






    private List<ActivityGroup> activitygroups;




    private ActivityNode activitynode;




    private List<ActivityEdge> activityedges;




    private StructuredActivityNode structuredactivitynode;




    private ActivityNode activitynode;




    private List<ActivityPartition> activitypartitions;


    public Activities_BasicActivities_ActivityEdge(
    ) {
        super(
        );
        this.activitygroups = new ArrayList<>();
        this.activityedges = new ArrayList<>();
        this.activitypartitions = new ArrayList<>();
    }

    public Activities_BasicActivities_ActivityEdge(
        ArrayList<ActivityGroup> activitygroups,        ArrayList<ActivityEdge> activityedges,        ArrayList<ActivityPartition> activitypartitions    ) {
        this.activitygroups = activitygroups;
        this.activityedges = activityedges;
        this.activitypartitions = activitypartitions;
    }


    public List<ActivityGroup> getActivitygroups() {
        return activitygroups;
    }

    public void addActivitygroup(Activitygroup activitygroup) {
        this.activitygroups.add(activitygroup);
    }
    public ActivityNode getActivitynode() {
        return activitynode;
    }

    public void setActivitynode(ActivityNode activitynode) {
        this.activitynode = activitynode;
    }
    public List<ActivityEdge> getActivityedges() {
        return activityedges;
    }

    public void addActivityedge(Activityedge activityedge) {
        this.activityedges.add(activityedge);
    }
    public StructuredActivityNode getStructuredactivitynode() {
        return structuredactivitynode;
    }

    public void setStructuredactivitynode(StructuredActivityNode structuredactivitynode) {
        this.structuredactivitynode = structuredactivitynode;
    }
    public ActivityNode getActivitynode() {
        return activitynode;
    }

    public void setActivitynode(ActivityNode activitynode) {
        this.activitynode = activitynode;
    }
    public List<ActivityPartition> getActivitypartitions() {
        return activitypartitions;
    }

    public void addActivitypartition(Activitypartition activitypartition) {
        this.activitypartitions.add(activitypartition);
    }

}