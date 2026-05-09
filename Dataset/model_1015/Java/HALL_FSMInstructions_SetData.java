





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetData extends PosConditionExpressionElement {

    private String field;





    private FSMInstructions_PosConditionExpressionElement fsminstructions_posconditionexpressionelement;


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

    public FSMInstructions_PosConditionExpressionElement getFsminstructions_posconditionexpressionelement() {
        return fsminstructions_posconditionexpressionelement;
    }

    public void setFsminstructions_posconditionexpressionelement(FSMInstructions_PosConditionExpressionElement fsminstructions_posconditionexpressionelement) {
        this.fsminstructions_posconditionexpressionelement = fsminstructions_posconditionexpressionelement;
    }

}