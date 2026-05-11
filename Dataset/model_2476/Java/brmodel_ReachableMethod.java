





import java.util.List;
import java.util.ArrayList;

public class brmodel_ReachableMethod extends Method {

    private String distance;





    private brmodel_RulePart brmodel_rulepart;


    public brmodel_ReachableMethod(
        String distance    ) {
        super(
        );
        this.distance = distance;
    }


    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }

    public brmodel_RulePart getBrmodel_rulepart() {
        return brmodel_rulepart;
    }

    public void setBrmodel_rulepart(brmodel_RulePart brmodel_rulepart) {
        this.brmodel_rulepart = brmodel_rulepart;
    }

}