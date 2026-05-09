





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_GetMessageParameter extends ActionMessageExpressionElement {

    private String field;



    public HALL_Actions_GetMessageParameter(
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