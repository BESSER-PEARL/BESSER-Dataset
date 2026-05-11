





import java.util.List;
import java.util.ArrayList;

public class minuml2_Activity extends ModelElement {






    private List<minuml2_ActivityPartition> minuml2_activitypartitions;


    public minuml2_Activity(
    ) {
        super(
        );
        this.minuml2_activitypartitions = new ArrayList<>();
    }

    public minuml2_Activity(
        ArrayList<minuml2_ActivityPartition> minuml2_activitypartitions    ) {
        this.minuml2_activitypartitions = minuml2_activitypartitions;
    }


    public List<minuml2_ActivityPartition> getMinuml2_activitypartitions() {
        return minuml2_activitypartitions;
    }

    public void addMinuml2_activitypartition(Minuml2_activitypartition minuml2_activitypartition) {
        this.minuml2_activitypartitions.add(minuml2_activitypartition);
    }

}