





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetData extends PosConditionExpression {

    private String field;





    private FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression;


    public HALL_FSMInstructions_SetData(
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

    public FSMInstructions_PosConditionExpression getFsminstructions_posconditionexpression() {
        return fsminstructions_posconditionexpression;
    }

    public void setFsminstructions_posconditionexpression(FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression) {
        this.fsminstructions_posconditionexpression = fsminstructions_posconditionexpression;
    }

}