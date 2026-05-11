





import java.util.List;
import java.util.ArrayList;

public class cobol_dataitems_Value extends DataItemAttribute {






    private List<Condition> conditions;


    public cobol_dataitems_Value(
    ) {
        super(
        );
        this.conditions = new ArrayList<>();
    }

    public cobol_dataitems_Value(
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