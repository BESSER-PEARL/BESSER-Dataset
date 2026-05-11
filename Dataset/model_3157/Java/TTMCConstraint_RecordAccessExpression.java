





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_RecordAccessExpression extends AccessExpression {

    private String field;



    public TTMCConstraint_RecordAccessExpression(
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