





import java.util.List;
import java.util.ArrayList;

public class cobol_conditions_ExpressionList  {






    private List<Condition> conditions;


    public cobol_conditions_ExpressionList(
    ) {
        this.conditions = new ArrayList<>();
    }

    public cobol_conditions_ExpressionList(
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