





import java.util.List;
import java.util.ArrayList;

public class ccsl_CompositeRule extends Rule {

    private String operator;





    private List<ccsl_Rule> ccsl_rules;


    public ccsl_CompositeRule(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.ccsl_rules = new ArrayList<>();
    }

    public ccsl_CompositeRule(
        String operator        ArrayList<ccsl_Rule> ccsl_rules    ) {
        this.operator = operator;
        this.ccsl_rules = ccsl_rules;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<ccsl_Rule> getCcsl_rules() {
        return ccsl_rules;
    }

    public void addCcsl_rule(Ccsl_rule ccsl_rule) {
        this.ccsl_rules.add(ccsl_rule);
    }

}