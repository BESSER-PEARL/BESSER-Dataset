





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_GetData extends ActionExpressionElement {

    private String field;



    public HALL_FSMActions_GetData(
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