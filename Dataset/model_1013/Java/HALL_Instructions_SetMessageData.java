





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_SetMessageData extends PosConditionMessageExpression {

    private String field;





    private Instructions_PosConditionMessageExpression instructions_posconditionmessageexpression;


    public HALL_Instructions_SetMessageData(
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

    public Instructions_PosConditionMessageExpression getInstructions_posconditionmessageexpression() {
        return instructions_posconditionmessageexpression;
    }

    public void setInstructions_posconditionmessageexpression(Instructions_PosConditionMessageExpression instructions_posconditionmessageexpression) {
        this.instructions_posconditionmessageexpression = instructions_posconditionmessageexpression;
    }

}