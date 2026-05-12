





import java.util.List;
import java.util.ArrayList;

public class rdal_PrioritizedSatDesignElementRef extends SatisfiableDesignElementRef {

    private String weight;
    private String priority;



    public rdal_PrioritizedSatDesignElementRef(
        String weight,        String priority    ) {
        super(
        );
        this.weight = weight;
        this.priority = priority;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }


}