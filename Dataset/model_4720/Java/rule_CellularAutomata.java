





import java.util.List;
import java.util.ArrayList;

public class rule_CellularAutomata  {






    private List<rule_Rule> rule_rules;


    public rule_CellularAutomata(
    ) {
        this.rule_rules = new ArrayList<>();
    }

    public rule_CellularAutomata(
        ArrayList<rule_Rule> rule_rules    ) {
        this.rule_rules = rule_rules;
    }


    public List<rule_Rule> getRule_rules() {
        return rule_rules;
    }

    public void addRule_rule(Rule_rule rule_rule) {
        this.rule_rules.add(rule_rule);
    }

}