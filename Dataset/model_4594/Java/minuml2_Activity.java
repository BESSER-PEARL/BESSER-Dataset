





import java.util.List;
import java.util.ArrayList;

public class minuml2_Activity  {






    private List<minuml2_ActivityGroup> minuml2_activitygroups;


    public minuml2_Activity(
    ) {
        this.minuml2_activitygroups = new ArrayList<>();
    }

    public minuml2_Activity(
        ArrayList<minuml2_ActivityGroup> minuml2_activitygroups    ) {
        this.minuml2_activitygroups = minuml2_activitygroups;
    }


    public List<minuml2_ActivityGroup> getMinuml2_activitygroups() {
        return minuml2_activitygroups;
    }

    public void addMinuml2_activitygroup(Minuml2_activitygroup minuml2_activitygroup) {
        this.minuml2_activitygroups.add(minuml2_activitygroup);
    }

}