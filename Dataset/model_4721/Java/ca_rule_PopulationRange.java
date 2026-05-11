





import java.util.List;
import java.util.ArrayList;

public class ca_rule_PopulationRange  {

    private int lowerRange;
    private int upperRange;





    private ca_rule_Rule ca_rule_rule;


    public ca_rule_PopulationRange(
        int lowerRange,        int upperRange    ) {
        this.lowerRange = lowerRange;
        this.upperRange = upperRange;
    }


    public int getLowerrange() {
        return lowerRange;
    }

    public void setLowerrange(int lowerRange) {
        this.lowerRange = lowerRange;
    }
    public int getUpperrange() {
        return upperRange;
    }

    public void setUpperrange(int upperRange) {
        this.upperRange = upperRange;
    }

    public ca_rule_Rule getCa_rule_rule() {
        return ca_rule_rule;
    }

    public void setCa_rule_rule(ca_rule_Rule ca_rule_rule) {
        this.ca_rule_rule = ca_rule_rule;
    }

}