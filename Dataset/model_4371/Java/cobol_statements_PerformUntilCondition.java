





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_PerformUntilCondition extends statements_VaryingUntilCondition, statements_Perform {

    private String position;





    private List<Condition> conditions;


    public cobol_statements_PerformUntilCondition(
        String position    ) {
        super(
        );
        this.position = position;
        this.conditions = new ArrayList<>();
    }

    public cobol_statements_PerformUntilCondition(
        String position        ArrayList<Condition> conditions    ) {
        this.position = position;
        this.conditions = conditions;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public List<Condition> getConditions() {
        return conditions;
    }

    public void addCondition(Condition condition) {
        this.conditions.add(condition);
    }

}