





import java.util.List;
import java.util.ArrayList;

public class forms_Condition  {

    private String type;
    private String conditionID;



    public forms_Condition(
        String type,        String conditionID    ) {
        this.type = type;
        this.conditionID = conditionID;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getConditionid() {
        return conditionID;
    }

    public void setConditionid(String conditionID) {
        this.conditionID = conditionID;
    }


}