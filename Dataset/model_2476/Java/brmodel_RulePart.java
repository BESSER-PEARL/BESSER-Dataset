





import java.util.List;
import java.util.ArrayList;

public class brmodel_RulePart  {

    private String granularity;





    private brmodel_Rule brmodel_rule;


    public brmodel_RulePart(
        String granularity    ) {
        this.granularity = granularity;
    }


    public String getGranularity() {
        return granularity;
    }

    public void setGranularity(String granularity) {
        this.granularity = granularity;
    }

    public brmodel_Rule getBrmodel_rule() {
        return brmodel_rule;
    }

    public void setBrmodel_rule(brmodel_Rule brmodel_rule) {
        this.brmodel_rule = brmodel_rule;
    }

}