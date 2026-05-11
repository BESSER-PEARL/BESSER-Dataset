





import java.util.List;
import java.util.ArrayList;

public class forms_CompositeCondition extends Condition {

    private String compositionType;





    private List<forms_Condition> forms_conditions;


    public forms_CompositeCondition(
        String compositionType    ) {
        super(
        );
        this.compositionType = compositionType;
        this.forms_conditions = new ArrayList<>();
    }

    public forms_CompositeCondition(
        String compositionType        ArrayList<forms_Condition> forms_conditions    ) {
        this.compositionType = compositionType;
        this.forms_conditions = forms_conditions;
    }

    public String getCompositiontype() {
        return compositionType;
    }

    public void setCompositiontype(String compositionType) {
        this.compositionType = compositionType;
    }

    public List<forms_Condition> getForms_conditions() {
        return forms_conditions;
    }

    public void addForms_condition(Forms_condition forms_condition) {
        this.forms_conditions.add(forms_condition);
    }

}