





import java.util.List;
import java.util.ArrayList;

public class express_rules_SupertypeRule extends CommonElement {

    private String assertsAbstract;





    private List<SubtypeConstraint> subtypeconstraints;


    public express_rules_SupertypeRule(
        String assertsAbstract    ) {
        super(
        );
        this.assertsAbstract = assertsAbstract;
        this.subtypeconstraints = new ArrayList<>();
    }

    public express_rules_SupertypeRule(
        String assertsAbstract        ArrayList<SubtypeConstraint> subtypeconstraints    ) {
        this.assertsAbstract = assertsAbstract;
        this.subtypeconstraints = subtypeconstraints;
    }

    public String getAssertsabstract() {
        return assertsAbstract;
    }

    public void setAssertsabstract(String assertsAbstract) {
        this.assertsAbstract = assertsAbstract;
    }

    public List<SubtypeConstraint> getSubtypeconstraints() {
        return subtypeconstraints;
    }

    public void addSubtypeconstraint(Subtypeconstraint subtypeconstraint) {
        this.subtypeconstraints.add(subtypeconstraint);
    }

}