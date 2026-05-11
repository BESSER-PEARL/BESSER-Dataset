





import java.util.List;
import java.util.ArrayList;

public class forms_CompositeCondition extends Condition {

    private String operator;





    private List<forms_Condition> forms_conditions;


    public forms_CompositeCondition(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.forms_conditions = new ArrayList<>();
    }

    public forms_CompositeCondition(
        String operator        ArrayList<forms_Condition> forms_conditions    ) {
        this.operator = operator;
        this.forms_conditions = forms_conditions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<forms_Condition> getForms_conditions() {
        return forms_conditions;
    }

    public void addForms_condition(Forms_condition forms_condition) {
        this.forms_conditions.add(forms_condition);
    }

}