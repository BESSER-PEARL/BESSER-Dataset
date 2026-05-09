





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_GetMessageParameter extends PosConditionMessageExpression {

    private String field;



    public HALL_Instructions_GetMessageParameter(
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