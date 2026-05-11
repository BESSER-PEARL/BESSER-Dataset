





import java.util.List;
import java.util.ArrayList;

public class ca_rule_CellularAutomata  {






    private List<ca_rule_Rule> ca_rule_rules;


    public ca_rule_CellularAutomata(
    ) {
        this.ca_rule_rules = new ArrayList<>();
    }

    public ca_rule_CellularAutomata(
        ArrayList<ca_rule_Rule> ca_rule_rules    ) {
        this.ca_rule_rules = ca_rule_rules;
    }


    public List<ca_rule_Rule> getCa_rule_rules() {
        return ca_rule_rules;
    }

    public void addCa_rule_rule(Ca_rule_rule ca_rule_rule) {
        this.ca_rule_rules.add(ca_rule_rule);
    }

}