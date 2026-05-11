





import java.util.List;
import java.util.ArrayList;

public class minuml2_ModelElement  {

    private String name;





    private minuml2_ActivityPartition minuml2_activitypartition;


    public minuml2_ModelElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public minuml2_ActivityPartition getMinuml2_activitypartition() {
        return minuml2_activitypartition;
    }

    public void setMinuml2_activitypartition(minuml2_ActivityPartition minuml2_activitypartition) {
        this.minuml2_activitypartition = minuml2_activitypartition;
    }

}