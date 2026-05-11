





import java.util.List;
import java.util.ArrayList;

public class eol_expression_IntegerExpression extends ComparableExpression, SummableExpression {

    private int value;



    public eol_expression_IntegerExpression(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}