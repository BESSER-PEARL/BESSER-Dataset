





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_GetData extends PreConditionMessageExpressionElement {

    private String field;



    public HALL_Conditions_GetData(
        String field    ) {
        super(
        );
        this.field = field;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }


}