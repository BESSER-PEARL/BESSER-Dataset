





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_GetMessageData extends PosConditionMessageExpressionElement {

    private String field;



    public HALL_Instructions_GetMessageData(
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