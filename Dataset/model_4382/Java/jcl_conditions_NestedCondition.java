





import java.util.List;
import java.util.ArrayList;

public class jcl_conditions_NestedCondition extends PrimaryCondition {






    private List<Condition> conditions;


    public jcl_conditions_NestedCondition(
    ) {
        super(
        );
        this.conditions = new ArrayList<>();
    }

    public jcl_conditions_NestedCondition(
        ArrayList<Condition> conditions    ) {
        this.conditions = conditions;
    }


    public List<Condition> getConditions() {
        return conditions;
    }

    public void addCondition(Condition condition) {
        this.conditions.add(condition);
    }

}