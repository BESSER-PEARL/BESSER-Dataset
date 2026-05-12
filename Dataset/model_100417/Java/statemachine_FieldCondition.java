





import java.util.List;
import java.util.ArrayList;

public class statemachine_FieldCondition extends AbstractCondition {

    private String fieldName;



    public statemachine_FieldCondition(
        String fieldName    ) {
        super(
        );
        this.fieldName = fieldName;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }


}