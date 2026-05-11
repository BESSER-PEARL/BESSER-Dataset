





import java.util.List;
import java.util.ArrayList;

public class rule_PopulationRange  {

    private int upperRange;
    private int lowerRange;





    private rule_Rule rule_rule;


    public rule_PopulationRange(
        int upperRange,        int lowerRange    ) {
        this.upperRange = upperRange;
        this.lowerRange = lowerRange;
    }


    public int getUpperrange() {
        return upperRange;
    }

    public void setUpperrange(int upperRange) {
        this.upperRange = upperRange;
    }
    public int getLowerrange() {
        return lowerRange;
    }

    public void setLowerrange(int lowerRange) {
        this.lowerRange = lowerRange;
    }

    public rule_Rule getRule_rule() {
        return rule_rule;
    }

    public void setRule_rule(rule_Rule rule_rule) {
        this.rule_rule = rule_rule;
    }

}