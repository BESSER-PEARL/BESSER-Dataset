





import java.util.List;
import java.util.ArrayList;

public class minuml2_Activity  {






    private List<minuml2_ActivityEdge> minuml2_activityedges;




    private List<minuml2_ActivityGroup> minuml2_activitygroups;


    public minuml2_Activity(
    ) {
        this.minuml2_activityedges = new ArrayList<>();
        this.minuml2_activitygroups = new ArrayList<>();
    }

    public minuml2_Activity(
        ArrayList<minuml2_ActivityEdge> minuml2_activityedges,        ArrayList<minuml2_ActivityGroup> minuml2_activitygroups    ) {
        this.minuml2_activityedges = minuml2_activityedges;
        this.minuml2_activitygroups = minuml2_activitygroups;
    }


    public List<minuml2_ActivityEdge> getMinuml2_activityedges() {
        return minuml2_activityedges;
    }

    public void addMinuml2_activityedge(Minuml2_activityedge minuml2_activityedge) {
        this.minuml2_activityedges.add(minuml2_activityedge);
    }
    public List<minuml2_ActivityGroup> getMinuml2_activitygroups() {
        return minuml2_activitygroups;
    }

    public void addMinuml2_activitygroup(Minuml2_activitygroup minuml2_activitygroup) {
        this.minuml2_activitygroups.add(minuml2_activitygroup);
    }

}