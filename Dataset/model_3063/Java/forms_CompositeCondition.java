





import java.util.List;
import java.util.ArrayList;

public class forms_CompositeCondition extends Condition {

    private String operatorType;





    private forms_Condition forms_condition;




    private forms_Condition forms_condition;


    public forms_CompositeCondition(
        String operatorType    ) {
        super(
        );
        this.operatorType = operatorType;
    }


    public String getOperatortype() {
        return operatorType;
    }

    public void setOperatortype(String operatorType) {
        this.operatorType = operatorType;
    }

    public forms_Condition getForms_condition() {
        return forms_condition;
    }

    public void setForms_condition(forms_Condition forms_condition) {
        this.forms_condition = forms_condition;
    }
    public forms_Condition getForms_condition() {
        return forms_condition;
    }

    public void setForms_condition(forms_Condition forms_condition) {
        this.forms_condition = forms_condition;
    }

}