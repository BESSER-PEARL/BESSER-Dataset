





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_GetData extends PosConditionExpressionElement {

    private String field;



    public HALL_FSMInstructions_GetData(
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