





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_SetData extends PosConditionMessageExpressionElement {

    private String field;





    private Instructions_PosConditionMessageExpressionElement instructions_posconditionmessageexpressionelement;


    public HALL_Instructions_SetData(
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

    public Instructions_PosConditionMessageExpressionElement getInstructions_posconditionmessageexpressionelement() {
        return instructions_posconditionmessageexpressionelement;
    }

    public void setInstructions_posconditionmessageexpressionelement(Instructions_PosConditionMessageExpressionElement instructions_posconditionmessageexpressionelement) {
        this.instructions_posconditionmessageexpressionelement = instructions_posconditionmessageexpressionelement;
    }

}