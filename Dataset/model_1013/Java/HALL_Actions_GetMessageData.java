





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_GetMessageData extends ActionMessageExpression {

    private String field;



    public HALL_Actions_GetMessageData(
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