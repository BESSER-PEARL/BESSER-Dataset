





import java.util.List;
import java.util.ArrayList;

public class forms_Condition  {

    private String conditionID;
    private String type;





    private forms_Model forms_model;


    public forms_Condition(
        String conditionID,        String type    ) {
        this.conditionID = conditionID;
        this.type = type;
    }


    public String getConditionid() {
        return conditionID;
    }

    public void setConditionid(String conditionID) {
        this.conditionID = conditionID;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public forms_Model getForms_model() {
        return forms_model;
    }

    public void setForms_model(forms_Model forms_model) {
        this.forms_model = forms_model;
    }

}